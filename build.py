#!/usr/bin/env python3
"""Build static marketing pages for getmaize.ai from Markdown.

    content/resources/_index.md                ->  dist/resources/index.html (hub: categories + loose pages)
    content/resources/<slug>.md                ->  dist/resources/<slug>/index.html
    content/resources/<category>/_index.md     ->  dist/resources/<category>/index.html
    content/resources/<category>/<slug>.md     ->  dist/resources/<category>/<slug>/index.html
    assets/*                                   ->  dist/resources/assets/*
                                               ->  dist/sitemap-content.xml

Everything lives under /resources/, the only nginx-routed section. Categories
are plain subfolders and need no nginx change. LEGACY maps old URL prefixes
to new ones; the build writes noindex redirect stubs there so links keep
working until nginx 301s them.

Front matter (YAML between --- lines) per page:
    title:        required, shown as <h1> and in <title> ("<title> | Maize")
    description:  required, 50-160 chars, used for meta description + Open Graph
    date:         optional YYYY-MM-DD, published date (Article schema)
    updated:      optional YYYY-MM-DD, overrides the git-derived lastmod
    image:        optional absolute URL for og:image (defaults to the site image)
    draft:        optional true -> not built, not in the sitemap
    weight:       optional int, ordering on the section index (lower first)
    nav_title:    optional, short name for a category in breadcrumbs (_index.md only)

Run `python build.py` from the repo root; `python build.py --check` builds into
a temp dir and only reports problems (used on pull requests).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
SITE_URL = os.environ.get("SITE_URL", "https://getmaize.ai").rstrip("/")
DEFAULT_IMAGE = f"{SITE_URL}/static/images/og-default.png"

# The only routed top-level section (nginx location in the app repo).
SECTION = "resources"
SECTIONS = {SECTION: "Resources"}
# old URL prefix -> new prefix; stubs are written so old links keep working.
LEGACY = {"ai-syllabus-policy": "resources/ai-syllabus-policy"}
ASSETS_URL = "/resources/assets"   # assets ride along under a routed section

FRONT = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.S)
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class BuildError(Exception):
    pass


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONT.match(text)
    if not m:
        raise BuildError(f"{path}: missing front matter (--- block at top)")
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    for key in ("title", "description"):
        if not meta.get(key) or not str(meta[key]).strip():
            raise BuildError(f"{path}: front matter needs `{key}`")
    meta["title"] = str(meta["title"]).strip()
    meta["description"] = " ".join(str(meta["description"]).split())
    n = len(meta["description"])
    if n < 50 or n > 160:
        raise BuildError(f"{path}: description is {n} chars; keep it between 50 and 160")
    if len(meta["title"]) > 60:
        print(f"warning: {path}: title is {len(meta['title'])} chars; under 60 shows fully in search results")
    for key in ("date", "updated"):
        if key in meta and meta[key] is not None:
            if isinstance(meta[key], dt.datetime):
                meta[key] = meta[key].date()
            if not isinstance(meta[key], dt.date):
                raise BuildError(f"{path}: `{key}` must be YYYY-MM-DD")
    return {"meta": meta, "body": body, "path": path}


def git_lastmod(path: Path) -> dt.date | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        return dt.date.fromisoformat(out) if out else None
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return None


def lastmod(page: dict) -> dt.date:
    meta = page["meta"]
    return meta.get("updated") or git_lastmod(page["path"]) or meta.get("date") or dt.date.today()


def render_markdown(body: str) -> str:
    return markdown.markdown(body, extensions=["extra", "toc", "sane_lists", "smarty"])


def article_jsonld(page: dict, url: str, crumbs: list[tuple[str, str]]) -> dict:
    meta = page["meta"]
    org = {"@type": "Organization", "name": "Maize", "url": SITE_URL + "/",
           "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/static/images/maize-logo.png"}}
    doc = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": url + "#article",
                "headline": meta["title"],
                "description": meta["description"],
                "url": url,
                "mainEntityOfPage": url,
                "image": meta.get("image") or DEFAULT_IMAGE,
                "author": org,
                "publisher": org,
                "dateModified": page["lastmod"].isoformat(),
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": name, "item": item}
                    for i, (name, item) in enumerate(
                        [("Maize", SITE_URL + "/")]
                        + [(n, SITE_URL + u) for n, u in crumbs]
                        + [(meta["title"], url)])
                ],
            },
        ],
    }
    if meta.get("date"):
        doc["@graph"][0]["datePublished"] = meta["date"].isoformat()
    return doc


def load_dir(d: Path) -> dict:
    """{"index": page|None, "pages": [...]} for the .md files directly in d (non-draft)."""
    entry = {"index": None, "pages": []}
    for md in sorted(d.glob("*.md")):
        page = parse(md)
        if page["meta"].get("draft"):
            continue
        if md.stem == "_index":
            entry["index"] = page
            continue
        if not SLUG.match(md.stem):
            raise BuildError(f"{md}: filename must be lowercase-with-dashes (it becomes the URL)")
        page["slug"] = md.stem
        entry["pages"].append(page)
    entry["pages"].sort(key=lambda p: (p["meta"].get("weight", 1000), p["meta"].get("date") or dt.date.min, p["slug"]))
    return entry


def collect(content_dir: Path) -> dict:
    """{"root": entry, "categories": [(slug, entry), ...]}"""
    for d in sorted(p for p in content_dir.iterdir() if p.is_dir()):
        if d.name.startswith("_") or d.name == SECTION:
            continue
        raise BuildError(
            f"content/{d.name}/ is not a known section. New topics go in "
            f"content/{SECTION}/<category>/ (no nginx change needed).")
    root_dir = content_dir / SECTION
    root = load_dir(root_dir)
    if root["index"] is None:
        raise BuildError(f"content/{SECTION}/_index.md is required (it becomes /{SECTION}/)")
    cats = []
    for d in sorted(p for p in root_dir.iterdir() if p.is_dir()):
        if d.name.startswith("_") or d.name == "assets":
            continue
        if not SLUG.match(d.name):
            raise BuildError(f"{d}: category folder must be lowercase-with-dashes")
        entry = load_dir(d)
        if entry["index"] is None:
            raise BuildError(f"{d}/_index.md is required (it becomes /{SECTION}/{d.name}/)")
        if any(p.is_dir() for p in d.iterdir()):
            raise BuildError(f"{d}: categories can't be nested further")
        cats.append((d.name, entry))
    cats.sort(key=lambda c: (c[1]["index"]["meta"].get("weight", 1000), c[0]))
    return {"root": root, "categories": cats}


def card(page: dict, path: str) -> dict:
    return {"url": path, "title": page["meta"]["title"],
            "description": page["meta"]["description"], "date": page["meta"].get("date")}


def stub(target: str) -> str:
    t = escape(target, {'"': "&quot;"})
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{t}">'
            f'<meta http-equiv="refresh" content="0; url={t}"><title>Moved</title></head>'
            f'<body><p>This page moved to <a href="{t}">{t}</a>.</p></body></html>\n')


def build(content_dir: Path, assets_dir: Path, templates_dir: Path, out_dir: Path) -> list[dict]:
    env = Environment(loader=FileSystemLoader(str(templates_dir)), autoescape=select_autoescape(["html"]))
    env.globals.update(site_url=SITE_URL, assets_url=ASSETS_URL, year=dt.date.today().year)
    page_tpl = env.get_template("page.html")
    section_tpl = env.get_template("section.html")

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    site = collect(content_dir)
    root_crumb = (SECTIONS[SECTION], f"/{SECTION}/")
    built = []   # {"url", "lastmod"}

    def write(path: str, html: str):
        dest = out_dir / path.strip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")

    def render_pages(entry: dict, base: str, crumbs: list) -> list[dict]:
        cards = []
        for page in entry["pages"]:
            path = f"{base}{page['slug']}/"
            url = SITE_URL + path
            page["lastmod"] = lastmod(page)
            write(path, page_tpl.render(
                meta=page["meta"], body=render_markdown(page["body"]), url=url, crumbs=crumbs,
                jsonld=json.dumps(article_jsonld(page, url, crumbs), ensure_ascii=False)))
            built.append({"url": url, "lastmod": page["lastmod"]})
            cards.append(card(page, path))
        return cards

    def index_lastmod(index: dict, prefix: str) -> dt.date:
        return max([lastmod(index)] + [b["lastmod"] for b in built if b["url"].startswith(SITE_URL + prefix)])

    groups = []
    for slug, entry in site["categories"]:
        base = f"/{SECTION}/{slug}/"
        index = entry["index"]
        name = index["meta"].get("nav_title") or index["meta"]["title"]
        cards = render_pages(entry, base, [root_crumb, (name, base)])
        index["lastmod"] = index_lastmod(index, base)
        write(base, section_tpl.render(
            meta=index["meta"], body=render_markdown(index["body"]), url=SITE_URL + base,
            crumbs=[root_crumb], cards=cards, groups=[]))
        built.append({"url": SITE_URL + base, "lastmod": index["lastmod"]})
        groups.append({"url": base, "title": index["meta"]["title"],
                       "description": index["meta"]["description"], "cards": cards})

    base = f"/{SECTION}/"
    loose = render_pages(site["root"], base, [root_crumb])
    hub = site["root"]["index"]
    hub["lastmod"] = index_lastmod(hub, base)
    write(base, section_tpl.render(
        meta=hub["meta"], body=render_markdown(hub["body"]), url=SITE_URL + base,
        crumbs=[], cards=loose, groups=groups))
    built.append({"url": SITE_URL + base, "lastmod": hub["lastmod"]})

    for old, new in LEGACY.items():
        prefix = f"{SITE_URL}/{new}/"
        for b in built:
            if b["url"].startswith(prefix):
                write(f"/{old}/" + b["url"][len(prefix):], stub(b["url"]))

    if assets_dir.exists():
        shutil.copytree(assets_dir, out_dir / ASSETS_URL.strip("/"), dirs_exist_ok=True)

    (out_dir / "sitemap-content.xml").write_text(sitemap(built), encoding="utf-8")
    return built


def sitemap(built: list[dict]) -> str:
    rows = "".join(
        f"  <url><loc>{escape(b['url'])}</loc><lastmod>{b['lastmod'].isoformat()}</lastmod></url>\n"
        for b in sorted(built, key=lambda b: b["url"])
    )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{rows}</urlset>\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="build into a temp dir and report only")
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args(argv)
    out = Path(tempfile.mkdtemp(prefix="maize-content-")) if args.check else Path(args.out)
    try:
        built = build(ROOT / "content", ROOT / "assets", ROOT / "templates", out)
    except BuildError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    for b in built:
        print(f"{b['lastmod']}  {b['url']}")
    print(f"{len(built)} pages -> {out}")
    if args.check:
        shutil.rmtree(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
