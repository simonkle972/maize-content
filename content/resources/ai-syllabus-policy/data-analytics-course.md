---
title: AI policy for a data analytics course, with examples
description: Sample AI syllabus policies for data analytics courses at three levels of use, with clauses for SQL, dashboards, data handling and disclosure.
date: 2026-11-02
weight: 80
---
**Short answer:** in a data analytics course, students work in tools like SQL, Excel, Tableau, Power BI or Python, and AI can now help with most of the steps, from writing a query to drafting the summary of a chart. Your policy should say which steps students must do themselves, whether AI features built into their software count, what data may go into an AI tool, and how students show that they checked the result. Pick one of the three policies below, then add the analytics-specific clauses that fit your course.

## What makes data analytics different

- **Well-structured assignments are easy for AI.** A study of three data science courses found ChatGPT did well on assignments that described the dataset and broke the work into step-by-step questions. On the weaker assignments, techniques such as splitting a question into steps and describing the data helped a lot ([Shen et al., 2024](https://sigcse2024.sigcse.org/details/sigcse-ts-2024-Papers-1/127/Implications-of-ChatGPT-for-Data-Science-Education)). Many analytics assignments are written in just that format.
- **AI now sits inside the course software.** A policy that says "no ChatGPT" may not settle what students can do in the tools you teach. One Carnegie Mellon Tableau course treated the Explain Data feature as a generative AI tool ([Gongora-Svartzman](https://www.cmu.edu/teaching/gaitar/project-descriptions/gongora-svartzman.html)).
- **Checking the result is the skill.** Students have to decide whether the query returned the right rows, whether the chart misleads and what the numbers mean for the decision at hand. In a 2024-2025 survey of 119 statistics and data science students at one university, 80% had used ChatGPT, but only 40.6% felt confident explaining AI output, and nearly 70% said they had run into errors, bias or made-up content at least occasionally ([Hasan and Mostafa, 2026](https://jds-online.org/journal/JDS/article/1491/file/pdf)). This is self-reported data from a single campus, so read it as a signal, not a national rate.

## Three sample policies

Copy the one closest to your course and edit the bracketed parts.

### 1. No generative AI on graded work

> Generative AI tools (for example ChatGPT, Claude, Gemini or Copilot) may not be used on assignments, cases, quizzes or exams in this course. This includes AI features built into [Excel / Tableau / Power BI / your code editor]. Writing the query, shaping the data and choosing the chart yourself is how you learn to spot when something is wrong. You may use course materials, software documentation and help from the teaching staff. If you are unsure whether something is allowed, ask before you submit.

### 2. AI for studying, not for submitted work

> You may use generative AI tools to study: to explain a concept such as a join or a window function, to generate practice questions, or to explain an error message in a query you wrote. You may not use them to produce queries, formulas, charts, findings or written answers that you submit, and you may not use AI features built into [course software] on graded work. Everything you hand in should be work you can explain step by step. If you used an AI tool while studying for an assignment, add one sentence at the end saying how.

### 3. AI allowed with disclosure

> On [assignments / the project], you may use generative AI tools, including features built into [course software], to draft queries, formulas or code, if you disclose it. For each assignment, list the tool, what you used it for and the key prompts. You are responsible for every number you report: check row counts and totals against the source data, and confirm that any chart shows what you say it shows. Your findings and recommendations must be written in your own words. AI tools may not be used on [quizzes / exams].

## Clauses worth adding for data analytics

- **Say what data can go in.** "Do not paste [client / company / student / course] data into an AI tool unless I have told you that the tool is approved for it." If your course uses live data from a partner organization, this one matters most.
- **Show how you checked.** Ask for two or three sentences on how the student confirmed the result, such as a row count, a total matched to the source or a second method. This is short to grade and works under all three policies.
- **Explain-your-work check.** "I may ask you to walk me through any query, formula or chart you submit. If you cannot explain it, it may receive no credit."
- **What to disclose.** One business example on KU's list says AI can help with SQL statements, Alteryx workflows and Power BI visuals, while keeping it out of quizzes and graded answers. Students must describe the role AI played, share their prompts and name the platform. It also says students are not required to pay for or use these tools, which is worth copying ([KU CTE](https://cte.ku.edu/building-ai-policies-your-syllabus)).

## What one course comparison found

At Carnegie Mellon, one instructor changed how a 7-week Data Analytics with Tableau course introduced Tableau's Explain Data feature. Twenty-five students in one spring 2024 section got a brief introduction near the end of the course, and 55 students in two fall 2024 sections got an earlier, scaffolded one ([Gongora-Svartzman](https://www.cmu.edu/teaching/gaitar/project-descriptions/gongora-svartzman.html)).

- Performance on in-class exercises, group projects and case challenges did not differ significantly between the two terms.
- Students in the fall sections reported higher confidence in their data literacy after the course than before it.

Keep the limits in mind: the spring students already scored very high, which made any gain hard to detect, and confidence was not measured in the spring section, so the rise cannot be credited to the change. This is one course, with groups taught in different terms. The practical takeaway is modest: introducing an AI feature early, with structure, did not visibly hurt performance on the course work here.

## Write yours in a few minutes

The [free AI policy generator](/ai-policy-generator) asks a few questions about your course and assessments and produces a policy you can paste into your syllabus.

## Sources

- Shen, Ai, Soosai Raj, Leo John and Syamkumar, [Implications of ChatGPT for Data Science Education](https://sigcse2024.sigcse.org/details/sigcse-ts-2024-Papers-1/127/Implications-of-ChatGPT-for-Data-Science-Education), SIGCSE Technical Symposium, 2024
- Hasan and Mostafa, [Perceptions and Utilization of GenAI Tools among Data Science Students and Faculty](https://jds-online.org/journal/JDS/article/1491/file/pdf), *Journal of Data Science* 24(4), 2026
- Gongora-Svartzman, [project description](https://www.cmu.edu/teaching/gaitar/project-descriptions/gongora-svartzman.html), Carnegie Mellon University GAITAR program
- University of Kansas Center for Teaching Excellence, [Building AI policies into your syllabus](https://cte.ku.edu/building-ai-policies-your-syllabus)
