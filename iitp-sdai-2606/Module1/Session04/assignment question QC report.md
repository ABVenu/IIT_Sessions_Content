# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. `append` three times → `len(cart)` is 3; grocery cart scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Zero-based indexing — `festivals[0]` is `"Holi"`. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Last positive index of 6-char string is `5` (`len - 1`). |
| Q4 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. `[ ]` is list; `( )` is tuple — common beginner mistake. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. `temps[2:5]` → indices 2,3,4 → `[31, 33, 35]`; exclusive stop. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. `pop(1)` removes `"Pencil"`; remaining list verified. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. List mutability, `append`, empty list; C (parentheses = list) correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Concatenation, `str()`, immutability; C (auto-convert with `+`) correctly excluded. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. `sort(reverse=True)` in-place, slice copy unchanged, mixed-type `TypeError`; C (sort returns new list) correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. `sum` total 35800, `len` 5, `max`/`min` values; C (`sum` removes items) correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via OneCompiler (save public + share link in LMS): Yes. Step images included. No external dataset — three sample runs with exact I/O. Tests parallel lists, `append` in `for` loop, `sum`/`len`/`max`/`min`, slice copy + `sort()`, and `str()` concatenation. Scope matches released lecture notes; does not require f-strings, `sorted()` built-in, or `list.index()` name lookup. |

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
- Scope limited to lists (`[]`, `append`, `pop`, `sort`), indexing and slicing, string concatenation with `str()`, `for` loop with `range()`, and built-ins `len()`, `min()`, `max()`, `sum()` from released lecture notes.
- f-strings and `sorted()` built-in excluded from scope (not in released notes).
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## AssignmentCreation.csv QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | mcsc | Correct option: 3 (C). Relevancy: Yes. Markdown body; options without A/B/C prefixes. |
| Q2 | mcsc | Correct option: 1 (A). Relevancy: Yes. Code block preserved in markdown. |
| Q3 | mcsc | Correct option: 2 (B). Relevancy: Yes. |
| Q4 | mcsc | Correct option: 3 (C). Relevancy: Yes. |
| Q5 | mcsc | Correct option: 1 (A). Relevancy: Yes. difficultyLevel: 0.5. |
| Q6 | mcsc | Correct option: 1 (A). Relevancy: Yes. difficultyLevel: 0.5. |
| Q7 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 0.5. |
| Q8 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 0.5. |
| Q9 | mcmc | Correct options: 1, 2, 4. Relevancy: Yes. difficultyLevel: 1. |
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
| tagRelationships (`6a3a2b20b59fd37f6abddb16` on all rows) | Pass |

**CSV QC iteration:** 1 — passed.
