---
title: AI policy for a machine learning course, with examples
description: Sample AI syllabus policies for machine learning courses at three levels of use, with clauses for derivations, model code and evaluation.
date: 2026-11-02
weight: 70
---
**Short answer:** a machine learning course usually grades three things: math derivations, code that implements or trains a model, and judgment about whether the results can be trusted. A general AI policy rarely separates them. Your policy should say which of the three students must do themselves, whether assignment text may go into an AI tool, and how students show they understand what they submit. Pick one of the three policies below, then add the machine learning clauses that fit your course.

## What makes machine learning different

- **Homework mixes math and code.** A single assignment can ask for a derivation and a working implementation, as UC Berkeley's CS 189 homework does ([CS 189 syllabus](https://eecs189.org/sp26/syllabus/)). Your policy may need a separate answer for each, because the skills differ.
- **A model that runs proves little.** Code can train without error and still leak test data, use the wrong metric or tune on the wrong split. A course at Carnegie Mellon warns students that AI tools often produce "plausible-looking but incorrect answers" ([Machine Learning in Production](https://mlip-cmu.github.io/s2026/)). Catching those mistakes is much of what the course teaches.
- **Course policies vary widely, even at the same university.** The four syllabi summarized below run from a near ban on AI during first-attempt homework to no restrictions at all. Students may take two of these courses in one year, so say plainly which rules apply in yours.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini, Copilot or coding agents), including AI code completion in your editor, may not be used on homework, coding labs, quizzes or exams in this course. Working through a derivation, implementing an algorithm and debugging a training run are how you learn how these methods behave, and these tools skip that work. You may use the textbook, lecture notes, library documentation and help from the teaching staff. If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept such as regularization, to work through a practice problem that is not assigned, or to explain an error message in code you wrote. You may not use them to produce derivations, code, results or written answers that you submit, and you may not paste assignment text into them. Everything you hand in should be work you can explain step by step. If you used an AI tool while studying for an assignment, add one sentence at the end saying how.

### 3. AI allowed with disclosure

> On [homework / the final project], you may use generative AI tools, including to draft or debug code, if you disclose it. Near the top of each submission, name the tool, what you used it for and the key prompts. [Derivations and the implementation of ____ must be your own.] You are responsible for everything you submit: check that the math is right, that the code does what you intend and that your evaluation is sound. You may be asked to explain your work in a short meeting. AI tools may not be used on [quizzes / exams].

## Clauses worth adding for machine learning

- **Explain-your-work check.** "I may ask you to walk me through any part of your submission. If you cannot explain it, it may receive no credit." CS 189 randomly selects students for a short interview or recorded walkthrough, and a student who cannot explain the approach may get a zero on that homework.
- **Say what can go into a prompt.** CS 189 bars pasting assignment text into AI tools, and UBC's CPSC 330 tells students not to paste course assessments directly into them ([CPSC 330 syllabus](https://ubc-cs.github.io/cpsc330-2026S1/syllabus/)). Under a permissive policy you may decide otherwise, but say so. If students use course or research data, say whether it may be pasted in.
- **Ask for the evaluation in the student's own words.** Require a few sentences on how the data was split, which metric was used and why, and what the student checked before trusting the result. Keep this requirement under all three policies.
- **What to disclose.** Name the tool, what it was used for and the prompts that shaped the answer, or attach the chat log. One engineering example on KU's list requires a header comment on every homework and a chat log if AI was used ([KU CTE](https://cte.ku.edu/building-ai-policies-your-syllabus)).

## How four machine learning courses handle it

We read four 2026 syllabi. They show what instructors chose, not what worked, since none of them reports results.

- **Carnegie Mellon, Introduction to Machine Learning (10-301/601), spring 2026.** Homework has two rounds. Students first submit with no AI, then staff mark which questions were wrong, and students can redo only those with AI and full collaboration. Each question counts at the higher of the two scores. AI is never allowed in coding labs, and exams are proctored in person ([syllabus](https://www.cs.cmu.edu/~mgormley/courses/10601/)).
- **UC Berkeley, Introduction to Machine Learning (CS 189/289A), spring 2026.** AI is "a consulting tool, not an author." Students may cite it for concepts and error messages, and tab code completion is allowed if they could reproduce the work on their own. Asking for solutions and having agents do the assignment are not allowed. Exams make up most of the grade ([syllabus](https://eecs189.org/sp26/syllabus/)).
- **UBC, Applied Machine Learning (CPSC 330), 2026.** AI use is allowed with a note naming the tool and how it was used, but submitted work must reflect the student's own thinking. Students who seem to rely on it too much may be asked to explain their work orally. Exams carry 70% of the tentative grade weighting ([syllabus](https://ubc-cs.github.io/cpsc330-2026S1/syllabus/)).
- **Carnegie Mellon, Machine Learning in Production (spring 2026).** There are no restrictions and no disclosure rule. Instead, students must explain their solutions to course staff, and they answer TA questions in labs ([course page](https://mlip-cmu.github.io/s2026/)). This is a project course about building systems, so its approach may not fit a first course in the theory.

The common thread: each course pairs its AI rule with work the instructors can observe, such as exams, coding labs or spoken explanations. The two-round homework at Carnegie Mellon is also worth a look if you want a first attempt without AI and a guided use of it afterward.

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- Carnegie Mellon University, [10-301/601 Introduction to Machine Learning](https://www.cs.cmu.edu/~mgormley/courses/10601/), spring 2026 syllabus
- University of California, Berkeley, [CS 189/289A Introduction to Machine Learning](https://eecs189.org/sp26/syllabus/), spring 2026 syllabus
- University of British Columbia, [CPSC 330 Applied Machine Learning](https://ubc-cs.github.io/cpsc330-2026S1/syllabus/), 2026 syllabus
- Carnegie Mellon University, [Machine Learning in Production / AI Engineering](https://mlip-cmu.github.io/s2026/), spring 2026 course page
- University of Kansas Center for Teaching Excellence, [Building AI policies into your syllabus](https://cte.ku.edu/building-ai-policies-your-syllabus)
