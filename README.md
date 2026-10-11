# maize-content

Static marketing pages for getmaize.ai, served by nginx straight from disk.
Publishing a page here never restarts the Maize app.

| URL | Source |
|---|---|
| `/resources/<slug>/` | `content/resources/<slug>.md` |
| `/ai-syllabus-policy/<slug>/` | `content/ai-syllabus-policy/<slug>.md` |
| `/resources/`, `/ai-syllabus-policy/` | that section's `_index.md` plus an auto-generated list of its pages |
| `/sitemap-content.xml` | generated from every built page; the app's `/sitemap.xml` index points at it |

## Add a page

1. Copy `content/_drafts/example-article.md` to `content/<section>/<slug>.md`. The filename is the URL: lowercase, dashes only.
2. Fill in the front matter. `title` and `description` (50 to 160 chars) are required; `date` is the published date; `draft: true` hides the page.
3. Write the body in Markdown. Headings start at `##`.
4. `python build.py --check` locally (optional), then open a pull request. The **check** job builds the whole site and fails on missing front matter, a bad description length, an unknown section or a bad filename.
5. Merge. The **deploy** job rsyncs the build to the VPS and curls the live URL. Pages are live within a minute; the app's sitemap index already links the content sitemap, so search engines pick the page up on their next crawl.

Only the sections listed in `SECTIONS` in `build.py` are built. A new section also needs an nginx location in the app repo (`deploy/nginx/maize-content.locations.conf`), so add both, in that order.

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
