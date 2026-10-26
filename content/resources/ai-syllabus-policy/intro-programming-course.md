---
title: AI policy for an intro programming course, with examples
description: Sample AI syllabus policies for introductory programming courses at three levels of use, with clauses for code, explanations and disclosure.
date: 2026-10-26
weight: 50
---
**Short answer:** in an introductory programming course, AI coding assistants can write a working solution to most assignments from the prompt alone. A program that runs no longer shows that the student wrote it or understands it. Your policy should say which assignments students must code on their own, how they show that they understand what they submit, and where AI help is fine. Pick one of the three policies below, then add the programming-specific clauses that fit your course.

## What makes intro programming different

- **The assignment is the code, and AI writes code.** In most courses, the graded artifact is a program that passes tests. AI tools produce that artifact directly, often inside the editor students already use, so the line between autocomplete and having the assignment done for you is easy to cross without noticing.
- **Homework and exam results can drift apart.** In interviews with 13 US computer science instructors, several described students who "turn in perfect homework but perform poorly on exams," and nine had moved to some form of paper exam ([Gu et al., 2026](https://arxiv.org/html/2607.16475v2)).
- **Struggle is part of learning to program.** Reading error messages, tracing a loop by hand and debugging are skills the first course builds. The same instructors worried that AI lets students skip that productive struggle and leaves them thinking they understand more than they do.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini or Copilot), including AI code completion in your editor, may not be used on programming assignments, quizzes or exams in this course. Writing, testing and debugging code yourself, including getting stuck and finding the bug, is how you learn to program, and these tools skip that step. You may use the textbook, lecture notes, the official language documentation, classmates [for discussion only, not shared code] and office hours. [Turn off AI code completion in your editor for this course.] If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept such as recursion, to explain an error message in code you wrote, or to generate extra practice problems. You may not use them to write, complete or fix code that you submit, and AI code completion should be turned off while you work on assignments. Everything you hand in should be code you can explain line by line. If you used an AI tool while studying for an assignment, add a comment at the top of your file saying how.

### 3. AI allowed with disclosure

> On [programming assignments / the final project], you may use generative AI tools, including to draft or debug code, if you disclose it. Add a comment at the top of each file naming the tool, what you used it for and the key prompts [or attach the chat log]. You are responsible for every line you submit: test it, and use only [language features / libraries] covered in this course unless the assignment says otherwise. You may be asked to explain your code in a short meeting, and that explanation counts toward your grade. AI tools may not be used on [quizzes / exams], where you write code on your own.

## Clauses worth adding for intro programming

- **Explain-your-code check.** "I may ask you to walk me through any part of your submitted code. If you cannot explain it, that part of the work may receive no credit." This works under any of the three policies.
- **Say where code completion stands.** Editors now suggest whole functions as students type. Say whether AI code completion counts as an AI tool under your policy, so students do not have to guess.
- **Course features only.** Ask that solutions use the language features and libraries taught so far. AI output can use constructs a first-year student has not seen yet, and this rule keeps the assignment about the skill you are teaching.
- **What to disclose.** Name the tool, what it was used for and the prompts that shaped the answer, or attach the chat log. Teaching centers commonly recommend asking for this kind of record; one engineering example on KU's list asks students to "include a chatlog in your submission" ([KU CTE](https://cte.ku.edu/building-ai-policies-your-syllabus)).

## What one recent course redesign found

At Utah State University, one instructor taught a 96-student introductory programming course in fall 2025 with no restrictions on AI use, on one condition: after each assignment, every student had a mandatory, roughly 15-minute in-person code review in which a TA or the instructor asked about the design and code ([Fowles et al., 2026](https://arxiv.org/html/2605.21374)). The course also became a flipped classroom. Compared with the same instructor's 2023 and 2024 sections, which banned AI on coding assignments:

- Exam scores showed no statistically significant difference.
- Keystroke logs showed a larger share of pasted characters (68.1% against 61.0% in fall 2024), which the authors read as more AI use, with no significant change in time on task.
- In the end-of-term survey, 65% of respondents agreed the code reviews helped them avoid relying too much on AI, and 72% agreed the course should keep them. The most common complaint was that difficulty varied between TAs.

Keep the limits in mind: one course, one instructor, no randomized control group, a flipped classroom introduced at the same time, and a manuscript that had not yet been peer reviewed. The design also needs enough TA time to meet every student after every assignment. The practical takeaway is that a permissive policy can hold up when part of the grade comes from work you observe, such as a short oral walkthrough.

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- Gu, Santo, Zumel Dumlao and Ericson, [To Police or to Guide: How Higher Education Computer Science Instructors Design and Implement Generative AI Policies](https://arxiv.org/html/2607.16475v2), University of Michigan, arXiv preprint, 2026
- Fowles, Falor, Bhattarai, Edwards and Poulsen, [Allowing Generative AI in CS1 with Code Review Interviews and a Flipped Classroom](https://arxiv.org/html/2605.21374), Utah State University, arXiv preprint, 2026
- University of Kansas Center for Teaching Excellence, [Building AI policies into your syllabus](https://cte.ku.edu/building-ai-policies-your-syllabus)
