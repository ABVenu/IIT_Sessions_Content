# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. `==` comparison returns `True` when values match — AC temperature scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `if` block skipped when condition is `False` — UPI balance scenario. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `else` runs when `if` is `False` — railway platform scenario. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. `=` vs `==` common mistake causes `SyntaxError` in `if`. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Correct `elif` chain execution for marks=85; higher band checked first. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: C. Relevancy: Yes. `input()` returns string; `int()` fix for `TypeError` on comparison. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. `and`, `or`, `not` with marks band; D distractor correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. `if`/`elif`/`else` chain behaviour; C (`else` mandatory) correctly excluded. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Login validation with case-sensitive username and ordered `elif` branches; C correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Wrong `elif` order causes high marks to get low grade; D (multiple prints) correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via OneCompiler (save public + share link in LMS): Yes. Step images included. No external dataset needed — four sample runs with exact I/O provided. Tests `int()`, boolean storage, `and`, ordered `if`/`elif`/`else`, and `input()`/`print()`. Does not require nested `if` blocks or concepts only covered at surface level. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria are satisfied:

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard).
- 1 medium subjective coding task with OneCompiler submission and complete answer explanation.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to booleans, comparison/logical operators, `if`/`elif`/`else`, indentation/colon rules, storing boolean results, `int()` on input, common mistakes (`=` vs `==`, string vs int), and ordered condition chains from released lecture notes.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## AssignmentCreation.csv QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | mcsc | Correct option: 1 (A). Relevancy: Yes. Markdown body; options without A/B/C prefixes. |
| Q2 | mcsc | Correct option: 2 (B). Relevancy: Yes. Code block preserved in markdown. |
| Q3 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q4 | mcsc | Correct option: 3 (C). Relevancy: Yes. |
| Q5 | mcsc | Correct option: 2 (B). Relevancy: Yes. difficultyLevel: 0.5. |
| Q6 | mcsc | Correct option: 3 (C). Relevancy: Yes. difficultyLevel: 0.5. |
| Q7 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 0.5. |
| Q8 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 0.5. |
| Q9 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 1. |
| Q10 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 1. |
| Q1 | subjective | Solution in answerExplanation only (not subjectiveAnswer). OneCompiler submission steps and images included. Reference code with proper indentation. difficultyLevel: 0.5. |

| CSV QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |
| CSV Parsing (11 rows, no errors) | Pass |
| tagRelationships (`6a2ee49b7dcd9d741d497322` on all rows) | Pass |

**CSV QC iteration:** 1 — passed.
