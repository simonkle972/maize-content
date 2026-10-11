---
title: Example article (copy me into a section folder)
description: A template showing the front matter and Markdown conventions for a content page. Replace every line before publishing; this file is never built.
date: 2026-10-10
draft: true
---
Files under `content/_drafts/` are never built. To publish, move this file to
`content/resources/<slug>.md` or `content/ai-syllabus-policy/<slug>.md`, pick a
lowercase-with-dashes filename (it becomes the URL), remove `draft: true`, and
open a pull request.

## Headings start at h2

The page title is the h1. Use `##` for sections and `###` for subsections.

- Lists, **bold**, *italics*, [links](/ai-policy-generator) and tables all work (Python-Markdown "extra").
- Keep the description between 50 and 160 characters; the build fails otherwise.
- `updated: YYYY-MM-DD` sets the sitemap lastmod explicitly; otherwise it comes from the file's last git commit.
