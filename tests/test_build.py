"""Build a tiny fixture site and check the outputs. Run: pytest -q"""
import datetime as dt
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


GOOD = """---
title: Writing an AI policy for problem sets
description: How to set an AI-use rule for problem sets that students can follow and you can explain, with wording you can paste.
date: 2026-10-01
---
## Start with the learning goal

Some *Markdown* and a [link](/ai-policy-generator).
"""


@pytest.fixture
def site(tmp_path):
    content = tmp_path / "content"
    write(content / "resources" / "_index.md",
          "---\ntitle: Resources for instructors\nnav_title: Resources\ndescription: Guides for instructors on AI in teaching, written from running Maize.\n---\nIntro.\n")
    write(content / "resources" / "ai-syllabus-policy" / "_index.md",
          "---\ntitle: AI syllabus policy examples\nnav_title: AI syllabus policy\ndescription: Guides and examples for writing a course AI policy, by assessment type and discipline.\n---\nIntro.\n")
    write(content / "resources" / "ai-syllabus-policy" / "problem-sets.md", GOOD)
    write(content / "resources" / "ai-syllabus-policy" / "hidden.md", GOOD.replace("date: 2026-10-01", "date: 2026-10-01\ndraft: true"))
    write(content / "resources" / "loose-guide.md", GOOD)
    write(content / "_drafts" / "x.md", "not even parsed")
    return content


def test_build_outputs_pages_and_sitemap(site, tmp_path):
    out = tmp_path / "dist"
    built = build.build(site, ROOT / "assets", ROOT / "templates", out)
    urls = sorted(b["url"] for b in built)
    assert urls == [
        "https://getmaize.ai/resources/",
        "https://getmaize.ai/resources/ai-syllabus-policy/",
        "https://getmaize.ai/resources/ai-syllabus-policy/problem-sets/",
        "https://getmaize.ai/resources/loose-guide/",
    ]
    page = (out / "resources" / "ai-syllabus-policy" / "problem-sets" / "index.html").read_text()
    assert "<title>Writing an AI policy for problem sets | Maize</title>" in page
    assert '<link rel="canonical" href="https://getmaize.ai/resources/ai-syllabus-policy/problem-sets/">' in page
    assert '"@type": "Article"' in page and '"datePublished": "2026-10-01"' in page
    assert '"position": 3, "name": "AI syllabus policy"' in page and '"position": 4' in page
    assert 'href="/resources/">Resources</a>' in page and 'href="/resources/ai-syllabus-policy/">AI syllabus policy</a>' in page
    assert "<h2" in page and "<em>Markdown</em>" in page
    assert 'href="/ai-syllabus-policy/"' not in page          # old footer link gone
    assert not (out / "resources" / "ai-syllabus-policy" / "hidden").exists()
    assert (out / "resources" / "assets" / "content.css").exists()

    cat = (out / "resources" / "ai-syllabus-policy" / "index.html").read_text()
    assert 'href="/resources/ai-syllabus-policy/problem-sets/"' in cat

    hub = (out / "resources" / "index.html").read_text()
    assert 'href="/resources/ai-syllabus-policy/"' in hub            # category block
    assert 'href="/resources/ai-syllabus-policy/problem-sets/"' in hub
    assert 'href="/resources/loose-guide/"' in hub

    legacy = (out / "ai-syllabus-policy" / "problem-sets" / "index.html").read_text()
    assert "noindex" in legacy and "https://getmaize.ai/resources/ai-syllabus-policy/problem-sets/" in legacy
    assert (out / "ai-syllabus-policy" / "index.html").exists()

    root = ET.fromstring((out / "sitemap-content.xml").read_text())
    locs = [u.find(NS + "loc").text for u in root.iter(NS + "url")]
    assert locs == urls                                               # stubs not in sitemap
    for u in root.iter(NS + "url"):
        dt.date.fromisoformat(u.find(NS + "lastmod").text)


def test_unknown_section_is_refused(site, tmp_path):
    write(site / "blog" / "_index.md", "---\ntitle: Blog\ndescription: " + "x" * 60 + "\n---\n")
    with pytest.raises(build.BuildError, match="not a known section"):
        build.build(site, ROOT / "assets", ROOT / "templates", tmp_path / "dist")


def test_category_needs_index(site, tmp_path):
    write(site / "resources" / "empty-cat" / "page.md", GOOD)
    with pytest.raises(build.BuildError, match="_index.md is required"):
        build.build(site, ROOT / "assets", ROOT / "templates", tmp_path / "dist")


def test_bad_front_matter_is_refused(site, tmp_path):
    write(site / "resources" / "short.md", "---\ntitle: T\ndescription: too short\n---\n")
    with pytest.raises(build.BuildError, match="description is"):
        build.build(site, ROOT / "assets", ROOT / "templates", tmp_path / "dist")
    write(site / "resources" / "short.md", "no front matter")
    with pytest.raises(build.BuildError, match="front matter"):
        build.build(site, ROOT / "assets", ROOT / "templates", tmp_path / "dist")


def test_bad_slug_is_refused(site, tmp_path):
    write(site / "resources" / "Bad_Slug.md", GOOD)
    with pytest.raises(build.BuildError, match="lowercase-with-dashes"):
        build.build(site, ROOT / "assets", ROOT / "templates", tmp_path / "dist")


def test_hub_previews_three_per_category_and_heads_loose_guides(site, tmp_path):
    many = site / "resources" / "ai-teaching-assistants"
    write(many / "_index.md",
          "---\ntitle: AI teaching assistants\ndescription: How an AI teaching assistant works inside a course, written from running Maize.\n---\nIntro.\n")
    for i, slug in enumerate(["first", "second", "third", "fourth"], start=1):
        write(many / f"{slug}.md", GOOD.replace("date: 2026-10-01", f"date: 2026-10-01\nweight: {i}"))
    out = tmp_path / "dist"
    build.build(site, ROOT / "assets", ROOT / "templates", out)

    hub = (out / "resources" / "index.html").read_text()
    for slug in ("first", "second", "third"):
        assert f'href="/resources/ai-teaching-assistants/{slug}/"' in hub
    assert 'href="/resources/ai-teaching-assistants/fourth/"' not in hub     # past the preview
    assert "See all 4 guides" in hub
    assert "See all 1 guides" not in hub and hub.count("See all") == 1        # small category: no link
    assert "<h2>More guides</h2>" in hub and 'href="/resources/loose-guide/"><h3>' in hub

    cat = (out / "resources" / "ai-teaching-assistants" / "index.html").read_text()
    assert 'href="/resources/ai-teaching-assistants/fourth/"' in cat          # category page lists all
