---
title: AI policy for a statistics course, with examples
description: Sample AI syllabus policies for statistics courses at three levels of use, with clauses for code, output interpretation and disclosure.
date: 2026-10-12
weight: 10
---
**Short answer:** a statistics AI policy has to cover two things a general policy usually skips: code (R, Python, SAS, Stata) and the interpretation of output. AI tools now write working analysis code from a one-line prompt, so the question to settle is which parts of the work you need students to do themselves. Pick one of the three policies below, then add the statistics-specific clauses that fit your assessments.

## What makes statistics different

- **Code is easy to generate and hard to judge.** An AI tool can produce code that runs and returns a plausible table. A student who cannot read that code cannot tell whether the model, the filter or the test is wrong.
- **Interpretation is the skill most courses grade.** Saying what a coefficient, interval or p-value means in context is where students show understanding, and it is also where pasted AI text is easiest to slip in.
- **Software help is already normal.** Students already use documentation, Stack Overflow and autocomplete in their editor. Your policy should say whether AI coding assistants count as one of these or as something different.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini or Copilot) may not be used to write code, choose methods or write interpretations for any graded assignment or exam in this course. The goal of [course] is for you to build the ability to set up and read an analysis yourself, and these tools skip that step. You may use course materials, software documentation and help from the teaching staff. If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept, quiz yourself or understand an error message in code you wrote. You may not use them to produce code, analysis or written answers that you submit. Everything you hand in should be work you can explain line by line. If you used an AI tool while studying for an assignment, add one sentence at the end saying how.

### 3. AI allowed with disclosure

> You may use generative AI tools on [homework / the project], including to draft or debug code, as long as you disclose it. For each assignment, list the tool, what you used it for and the key prompts. You are responsible for every line of code and every claim in your submission: check that the code does what you intend and that the output supports your interpretation. Interpretations must be written in your own words. AI use is not allowed on [exams / in-class assessments].

## Clauses worth adding for statistics

- **Explain-your-code check.** "I may ask you to walk me through any part of your submitted code. If you cannot explain it, it will be treated as work that is not your own."
- **Interpretation in your own words.** Even under a permissive policy, require that written interpretation of results be the student's own.
- **What to disclose.** Name the tool, what it was used for and the prompts that shaped the answer. Teaching centers commonly recommend asking for this kind of record ([KU CTE](https://cte.ku.edu/building-ai-policies-your-syllabus)).
- **Data.** If students work with course or research data that should not leave the course, say that it may not be pasted into an AI tool.

## What one recent comparison found

At Elon University, four instructors each taught two sections of the same introductory statistics course in 2025 and 2026, one section under a "must cite" AI policy and one under an "AI prohibited" policy, with SAS coding assessments ([eCOTS 2026 session](https://causeweb.org/cause/node/26628)). Their slides report survey results only, and sections were not randomly assigned, so treat this as one data point rather than a verdict:

- Students' confidence, enjoyment and pride in their SAS skills showed no meaningful difference between the two policies.
- About half of "must cite" respondents and about a third of "AI prohibited" respondents reported using AI on SAS assignments.
- The presenters said they plan to move to "no AI" policies paired with more in-class coding assessments.

The practical takeaway: a policy on its own does not determine behavior. Whatever you choose, pair it with at least some assessment you can observe, such as in-class coding or a short oral walkthrough.

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- University of Kansas Center for Teaching Excellence, [Building AI policies into your syllabus](https://cte.ku.edu/building-ai-policies-your-syllabus)
- Weaver, Taylor, Bussberg and Doehler, [Comparing Alternative AI Syllabus Policies for Teaching Introductory Statistical Computing](https://causeweb.org/cause/node/26628), eCOTS 2026 ([slides](https://causeweb.org/cause/sites/default/files/ecots/ecots22/materials/Elon_eCOTS2026_AISyllabus_slides.pdf))
