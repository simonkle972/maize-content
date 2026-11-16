---
title: AI policy for a linear algebra course, with examples
description: Sample AI syllabus policies for linear algebra at three levels of use, with clauses for computations, proofs and software.
date: 2026-11-16
weight: 120
---
**Short answer:** a linear algebra course mixes routine computation (row reduction, determinants, eigenvalues) with conceptual questions and, in many courses, short proofs. Current AI tools handle the computation well and the proofs less reliably, and they present both with the same confidence. Your policy should say which practice students must do themselves, how you will check that they understand what they submit, and how AI chatbots relate to the software the course already allows. Pick one of the three policies below, then add the clauses that fit your course.

## What makes linear algebra different

- **AI does well on first-year exam questions, but not uniformly.** A University College London case study gave the 2024 to 2025 first-year mathematics exams to one model (chatgpt-4o-latest). In the two modules with linear algebra content it averaged 61.4 in Logic and Linear Algebra against a student average of 74.0, and 63.6 in Groups and Matrices against 70.6. On "prove or disprove" questions it was unreliable, sometimes giving a wrong proof or a confidently wrong counterexample ([Walker et al., 2025](https://arxiv.org/html/2509.13359v4)). That is one model with one simple prompt, which the authors call a "crude lower bound".
- **Computation and understanding come apart easily.** A student can get the right eigenvalues without knowing what they say about the matrix. AI makes this gap wider, since it will produce both the computation and a plausible explanation.
- **Software is already part of many courses.** Many courses allow MATLAB, Python or a calculator for row reduction. Your policy should say whether an AI chatbot counts as one more tool of that kind or as something different.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini or Copilot) may not be used on homework, quizzes or exams in this course. Working computations by hand and writing your own arguments is how you learn to think with vectors and matrices, and these tools skip that step. You may use the textbook, lecture notes, [approved software such as MATLAB or Python for computation], classmates [if allowed] and office hours. I may ask you to explain any submitted work in person. If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept such as linear independence or a change of basis, to generate extra practice problems, or to check your understanding after you have attempted a problem on your own. You may not use them to produce computations, proofs or explanations that you submit. Write your solutions yourself, without looking at AI output while you write. If you used an AI tool while studying for an assignment, add one sentence at the end saying how.

### 3. AI allowed with disclosure

> On [homework / the project], you may use generative AI tools if you disclose it. For each assignment, state every resource you used, including the AI tool, what you used it for and the key prompts. Copying an AI-generated solution and submitting it as your own is not allowed. You are responsible for every step you submit: check each computation, make sure each proof step follows, and use only results covered in this course. AI tools may not be used on [quizzes / exams], where you show your understanding on your own.

## Clauses worth adding for linear algebra

- **Oral check.** "I may ask you to explain any submitted solution in person, without notice. If you cannot, that part of the work may receive no credit." Duke's Math 403 (Advanced Linear Algebra) prohibits generative AI for all parts of the course and pairs that with a rule that students may be asked to defend written work orally ([Duke Math 403](https://sites.math.duke.edu/~ezra/403/403.html)).
- **State all resources.** The University of Illinois Math 416 (Abstract Linear Algebra) syllabus allows AI tools for study and asks students to state every resource they used, including AI tools, when they submit homework ([UIUC Math 416](https://www.jacobbeckey.com/assets/math416-syllabus-fall25.pdf)).
- **Software versus AI chatbots.** If you allow MATLAB, Python or a calculator for computation, say whether AI assistants count under the same rule. A useful line: software may do the arithmetic, but the setup and interpretation must be the student's.
- **Course results only.** Say that proofs must use results from the course. AI tools sometimes reach for results students have not seen, which makes a proof look complete while skipping the point of the exercise. In the UCL study this happened in the Integration module, where the model used results taught in the third year ([Walker et al., 2025](https://arxiv.org/html/2509.13359v4)).

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- Walker, Kalaydzhieva, Navarro Lameda and Reynolds, [Generative AI performance in core undergraduate mathematics: a curriculum-level case study](https://arxiv.org/html/2509.13359v4), University College London, arXiv preprint, 2025
- Duke University Mathematics, [Math 403: Advanced Linear Algebra, Spring 2026](https://sites.math.duke.edu/~ezra/403/403.html)
- University of Illinois Urbana-Champaign, [MATH 416: Abstract Linear Algebra syllabus, Fall 2025](https://www.jacobbeckey.com/assets/math416-syllabus-fall25.pdf)
