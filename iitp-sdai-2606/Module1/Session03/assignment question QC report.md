# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Fixed-count repetition with `for` + `range()` — PE warm-up scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `range(4)` → 0–3; off-by-one / exclusive stop concept. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Missing counter increment causes infinite `while` loop — ATM scenario. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Python has no `++`; use `= + 1` or `+= 1`. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: C. Relevancy: Yes. `range(1, 6)` prints 1–5 — fitness rep counter scenario. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. `continue` skips one iteration — odd-number / tiffin packing scenario. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, C, D. Relevancy: Yes. Three forms of `range()`; B (includes 5) correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. `for` vs `while` selection; D (manual increment in `for`) correctly excluded. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. `continue` in `while` without pre-increment causes infinite loop; D correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Accumulator init, average outside loop, safe `student_count`; C (inside loop average) correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via OneCompiler (save public + share link in LMS): Yes. Step images included. No external dataset — three sample runs with exact I/O. Tests `for` + `range()`, dual accumulators, `if` inside loop, average outside loop, and `int()` on input. Scope matches released lecture notes; does not require `break`, list iteration, or concepts only introduced at surface level. |

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
- Scope limited to `for`/`while` loops, `range()`, `break`/`continue` concepts, loop selection, infinite-loop pitfall, accumulator pattern, average outside loop, Python increment rules, and `if` inside loops from released lecture notes.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## AssignmentCreation.csv QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | mcsc | Correct option: 2 (B). Relevancy: Yes. Markdown body; options without A/B/C prefixes. |
| Q2 | mcsc | Correct option: 2 (B). Relevancy: Yes. Code block preserved in markdown. |
| Q3 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q4 | mcsc | Correct option: 3 (C). Relevancy: Yes. |
| Q5 | mcsc | Correct option: 3 (C). Relevancy: Yes. difficultyLevel: 0.5. |
| Q6 | mcsc | Correct option: 2 (B). Relevancy: Yes. difficultyLevel: 0.5. |
| Q7 | mcmc | Correct options: 1, 3, 4. Relevancy: Yes. difficultyLevel: 0.5. |
| Q8 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 0.5. |
| Q9 | mcmc | Correct options: 1, 2, 3. Relevancy: Yes. difficultyLevel: 1. |
| Q10 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 1. |
| Q1 | subjective | Solution in answerExplanation only (not subjectiveAnswer). OneCompiler submission steps and images included. Reference code with proper indentation. difficultyLevel: 0.5. |

| CSV QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |
| CSV Parsing (11 rows, no errors) | Pass |
| tagRelationships (`6a34f2ef9d08498d508e04b3` on all rows) | Pass |

**CSV QC iteration:** 1 — passed.
