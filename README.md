# maize-content

Static marketing pages for getmaize.ai, served by nginx straight from disk.
Publishing a page here never restarts the Maize app.

Everything lives under `/resources/`. Topics are categories (subfolders) inside it.

| URL | Source |
|---|---|
| `/resources/` | `content/resources/_index.md` plus a block per category (its first 3 pages and a "See all N guides" link when it has more) and a "More guides" block for top-level guides |
| `/resources/<slug>/` | `content/resources/<slug>.md` (a guide that fits no category; prefer a category) |
| `/resources/<category>/` | `content/resources/<category>/_index.md` plus an auto-generated list of its pages |
| `/resources/<category>/<slug>/` | `content/resources/<category>/<slug>.md` |
| `/sitemap-content.xml` | generated from every built page; the app's `/sitemap.xml` index points at it |

Current categories, in hub order (`weight`):

| Category | For |
|---|---|
| `ai-syllabus-policy` (10) | AI syllabus policy examples, one page per discipline |
| `ai-teaching-assistants` (20) | How an AI teaching assistant works in a course: what students ask, what it leaves to the instructor, what it shows the instructor |

Within a category, `weight` on each page sets its order (lower first), and the hub previews the first 3, so give the pages you want on the hub the lowest weights.

## Add a page

1. Copy `content/_drafts/example-article.md` to `content/resources/<category>/<slug>.md` (or `content/resources/<slug>.md`). The filename is the URL: lowercase, dashes only.
2. Fill in the front matter. `title` and `description` (50 to 160 chars) are required; `date` is the published date; `draft: true` hides the page.
3. Write the body in Markdown. Headings start at `##`.
4. `python build.py --check` locally (optional), then open a pull request. The **check** job builds the whole site and fails on missing front matter, a bad description length, an unknown section or a bad filename.
5. Merge. The **deploy** job rsyncs the build to the VPS and curls the live URL. Pages are live within a minute; the app's sitemap index already links the content sitemap, so search engines pick the page up on their next crawl.

## Add a category

Create `content/resources/<category>/_index.md` with `title`, `description`, an optional short `nav_title` for breadcrumbs, and an optional `weight` for its order on the hub. No nginx change is needed, because everything is under `/resources/`. Categories are one level deep.

## Moved URLs

`LEGACY` in `build.py` maps old URL prefixes to new ones. The build writes small noindex redirect pages at the old paths so links keep working; once nginx 301s the old prefix, those stubs are never served. `/ai-syllabus-policy/*` moved to `/resources/ai-syllabus-policy/*` on 2026-10-12.

## Local build

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest -q
python build.py            # writes dist/
python -m http.server -d dist 8080   # http://localhost:8080/resources/ (app CSS and images will 404 locally)
```

## Deploy setup (one time)

The GitHub Action needs four repository secrets and a restricted `deploy` user on the VPS. The runbook is in the app repo at `docs/DEPLOYMENT.md`, section "Static content (maize-content)".

| Secret | Value |
|---|---|
| `DEPLOY_HOST` | VPS hostname or IP |
| `DEPLOY_USER` | `deploy` |
| `DEPLOY_SSH_KEY` | private half of the key whose public half is in `/home/deploy/.ssh/authorized_keys` |
| `DEPLOY_KNOWN_HOSTS` | output of `ssh-keyscan -H <host>` |

Pages reuse the app's stylesheets (`/static/css/style.css`, `/static/css/landing.css`) and images, so they inherit the site header and footer. Content-only styles are in `assets/content.css`, published at `/resources/assets/content.css`.
