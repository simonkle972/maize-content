---
title: AI policy for an operations course, with examples
description: Sample AI syllabus policies for operations and quantitative methods courses at three levels of use, with clauses for models, Solver output and disclosure.
date: 2026-11-09
weight: 90
---
**Short answer:** an operations management or quantitative methods course is built on modeling problems: linear programs, forecasts, inventory and queuing models, simulations and decision trees, usually set up in a spreadsheet. AI tools can now write out a model formulation from the problem statement, and the output looks right even when the answer is wrong. Your policy should say which modeling students must do themselves, how they show the model behind a number, and how they check what an AI tool gives them. Pick one of the three policies below, then add the operations-specific clauses that fit your course.

## What makes operations and quantitative methods different

- **Formulation is the skill, and AI is fairly good at it.** In one 2026 classroom study, AI tools usually got linear programming formulations right, and most of their errors came later, in the solution stage, such as misidentifying the feasible region ([Yoo and Kim, 2026](https://doi.org/10.1287/ited.2025.0175)). A correct-looking setup in a submission says little about who wrote it.
- **Spreadsheet output hides the work.** A Solver result or a sensitivity report shows the answer, not whether the student chose the decision variables and constraints. You see the reasoning only if you ask for the model itself.
- **The recommendation is what managers need.** Most courses grade whether students can turn a solution into a decision: what to produce, how much to stock, what a shadow price means. That written step is short, and it is where you can see understanding.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini or Copilot) may not be used to formulate models, build spreadsheets, solve problems or write recommendations for any graded assignment, case or exam in this course. The goal of [course] is for you to learn to turn a business problem into a model you can solve and explain, and these tools skip that step. You may use course materials, software help pages and help from the teaching staff. If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept such as a shadow price or a service level, generate practice problems, or help you understand a Solver error in a model you built. You may not use them to produce formulations, spreadsheets, solutions or recommendations that you submit. Everything you hand in should be work you can explain step by step. If you used an AI tool while studying for an assignment, add one sentence at the end saying how.

### 3. AI allowed with disclosure

> You may use generative AI tools on [homework / the case / the project] as long as you disclose it. Attempt each problem yourself first. For each assignment, list the tool, what you used it for and the key prompts. You are responsible for every number you submit: check that the model's constraints match the problem, that the solution is feasible and that the result makes sense. Recommendations must be written in your own words. AI use is not allowed on [exams / in-class assessments].

## Clauses worth adding for operations and quantitative methods

- **Submit the model, not just the answer.** "Each answer must include the decision variables, objective and constraints in words or algebra, and the spreadsheet you solved. Answers without the model will not receive full credit, whether or not AI was used." MIT's Teaching + Learning Lab also suggests asking students, for one or two problems per set, why they chose a method and what they assumed ([MIT TLL](https://tll.mit.edu/rethinking-your-problem-sets-in-the-world-of-generative-ai)).
- **Check the AI's solution.** Under a permissive policy, ask students to verify feasibility and plug the solution back into the constraints, and to note any error they found. The study above found that students who asked follow-up questions about corner points were better at catching AI errors.
- **Write the recommendation yourself.** Require a few sentences that state the decision, the key assumption and one sensitivity result in plain language. Keep this requirement under all three policies.
- **What to disclose.** Name the tool, what it was used for and the prompts that shaped the answer, or attach the chat log. One engineering example on KU's list asks students who use AI to submit a chat log ([KU CTE](https://cte.ku.edu/building-ai-policies-your-syllabus)).

## What one recent classroom study found

Yoo and Kim studied a linear programming assignment in an asynchronous online undergraduate operations management course at a regional public institution in spring 2025; 35 of the 44 enrolled students took part ([INFORMS Transactions on Education, 2026](https://doi.org/10.1287/ited.2025.0175)). Students first solved three problems without AI, then used an AI tool of their choice and refined its answers through at least three rounds of chat.

- The AI tools did well at formulation. Most errors occurred in the solution stage, for example in identifying the feasible region and evaluating corner points.
- Students who pasted the problem statement with little else as their prompt often got incomplete or wrong answers. Students who asked follow-up questions about corner points and intermediate steps were better at catching errors, though some follow-ups introduced new mistakes.
- Students rated the overall experience positively (3.94 on a 5-point scale) but did not feel the tools improved their understanding much (2.86).

The study had no control group, ran in one course and did not standardize which AI model students used, so treat it as one data point. The practical takeaway: if you allow AI, ask students to check the solution, not just the setup, and keep some assessment where they build and solve a model without it.

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- Yoo and Kim, Integrating Generative AI into Teaching Linear Programming: Understanding Student-AI Interaction, Limitations, and Perceptions, *INFORMS Transactions on Education*, published online August 2026, [doi:10.1287/ited.2025.0175](https://doi.org/10.1287/ited.2025.0175)
- MIT Teaching + Learning Lab, [Rethinking your problem sets in the world of generative AI](https://tll.mit.edu/rethinking-your-problem-sets-in-the-world-of-generative-ai)
- University of Kansas Center for Teaching Excellence, [Building AI policies into your syllabus](https://cte.ku.edu/building-ai-policies-your-syllabus)
