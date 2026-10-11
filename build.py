#!/usr/bin/env python3
"""Build static marketing pages for getmaize.ai from Markdown.

    content/<section>/<slug>.md      ->  dist/<section>/<slug>/index.html
    content/<section>/_index.md      ->  dist/<section>/index.html   (lists the section's pages)
    assets/*                         ->  dist/resources/assets/*
                                     ->  dist/sitemap-content.xml    (every built page, lastmod from git)

Only the sections in SECTIONS are built. Each one must have a matching nginx
location in the app repo (deploy/nginx/maize-content.locations.conf); a new
section needs that nginx change first, so the build refuses unknown ones.

Front matter (YAML between --- lines) per page:
    title:        required, shown as <h1> and in <title> ("<title> | Maize")
    description:  required, 50-160 chars, used for meta description + Open Graph
    date:         optional YYYY-MM-DD, published date (Article schema)
    updated:      optional YYYY-MM-DD, overrides the git-derived lastmod
    image:        optional absolute URL for og:image (defaults to the site image)
    draft:        optional true -> not built, not in the sitemap
    weight:       optional int, ordering on the section index (lower first)

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

# section path -> human name. Must match the nginx locations in the app repo.
SECTIONS = {
    "resources": "Resources",
    "ai-syllabus-policy": "AI syllabus policy",
}
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


def article_jsonld(page: dict, url: str, section: str) -> dict:
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
                    {"@type": "ListItem", "position": 1, "name": "Maize", "item": SITE_URL + "/"},
                    {"@type": "ListItem", "position": 2, "name": SECTIONS[section],
                     "item": f"{SITE_URL}/{section}/"},
                    {"@type": "ListItem", "position": 3, "name": meta["title"], "item": url},
                ],
            },
        ],
    }
    if meta.get("date"):
        doc["@graph"][0]["datePublished"] = meta["date"].isoformat()
    return doc


def collect(content_dir: Path) -> dict:
    """{section: {"index": page|None, "pages": [page, ...]}} for non-draft pages."""
    found = {}
    for section_dir in sorted(p for p in content_dir.iterdir() if p.is_dir()):
        section = section_dir.name
        if section.startswith("_"):
            continue                        # _drafts and friends are never built
        if section not in SECTIONS:
            raise BuildError(
                f"content/{section}/ is not a known section. Add it to SECTIONS here AND to "
                f"deploy/nginx/maize-content.locations.conf in the app repo first.")
        entry = {"index": None, "pages": []}
        for md in sorted(section_dir.glob("*.md")):
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
        found[section] = entry
    return found


def build(content_dir: Path, assets_dir: Path, templates_dir: Path, out_dir: Path) -> list[dict]:
    env = Environment(loader=FileSystemLoader(str(templates_dir)), autoescape=select_autoescape(["html"]))
    env.globals.update(site_url=SITE_URL, assets_url=ASSETS_URL, sections=SECTIONS,
                       year=dt.date.today().year)
    page_tpl = env.get_template("page.html")
    section_tpl = env.get_template("section.html")

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    built = []   # {"url", "lastmod"}
    for section, entry in collect(content_dir).items():
        cards = []
        for page in entry["pages"]:
            url = f"{SITE_URL}/{section}/{page['slug']}/"
            page["lastmod"] = lastmod(page)
            html = page_tpl.render(
                meta=page["meta"], body=render_markdown(page["body"]), url=url,
                section=section, section_name=SECTIONS[section],
                jsonld=json.dumps(article_jsonld(page, url, section), ensure_ascii=False),
            )
            dest = out_dir / section / page["slug"] / "index.html"
            dest.parent.mkdir(parents=True)
            dest.write_text(html, encoding="utf-8")
            built.append({"url": url, "lastmod": page["lastmod"]})
            cards.append({"url": f"/{section}/{page['slug']}/", "title": page["meta"]["title"],
                          "description": page["meta"]["description"], "date": page["meta"].get("date")})

        index = entry["index"]
        if index is None:
            raise BuildError(f"content/{section}/_index.md is required (it becomes /{section}/)")
        url = f"{SITE_URL}/{section}/"
        index["lastmod"] = max([lastmod(index)] + [b["lastmod"] for b in built if b["url"].startswith(url)])
        html = section_tpl.render(
            meta=index["meta"], body=render_markdown(index["body"]), url=url,
            section=section, section_name=SECTIONS[section], cards=cards,
        )
        (out_dir / section).mkdir(exist_ok=True)
        (out_dir / section / "index.html").write_text(html, encoding="utf-8")
        built.append({"url": url, "lastmod": index["lastmod"]})

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
