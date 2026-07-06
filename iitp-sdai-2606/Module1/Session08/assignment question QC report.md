# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Sorting defined via library book call-number scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Bubble Sort adjacent-neighbour swap intuition via sports-day height line. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Python list index starts at 0. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Sorting requires multiple items in a list, not a single value. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Bubble Sort Pass 1 trace on `[5, 1, 4, 2, 8]` matches released lecture notes. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Selection Sort minimum-selection intuition via playing-cards scenario. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Bubble Sort adjacent comparison, largest value settling, O(n²); D distractor (always one pass) correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Nested-loop O(n²) reasoning; C distractor (nested loops always O(n²)) correctly excluded per lecture notes caution. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. O(1) space, O(n²) time, nearly sorted bubble-sort advantage; C distractor (selection sort more swaps per pass) correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Selection Sort code understanding; D distractor (O(n) claim) correctly excluded. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via OneCompiler (save public + share link in LMS): Yes — matches Session 1 format with step images. No external dataset needed — fixed score list and exact output format provided. Tests `def`, nested loops, `len()`, `range()`, swaps, Bubble Sort and Selection Sort implementation, and result comparison. Does not require bubble-sort early-termination optimization or built-in `sorted()`. |

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
- 1 medium subjective coding task with OneCompiler submission instructions matching Session 01.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to sorting definition, list/index/swap, bubble sort, selection sort, tracing, nested loops, O(n²) time, O(1) space, and algorithm comparison from released lecture notes.
- Bubble-sort optimization referenced only at objective level where relevant; not required in subjective implementation. No out-of-scope sort algorithms appear in questions.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## QC Iteration 2 (Confirmation)

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

### Observations

- Second review confirms practical scenarios (library, sports day, hackathon, playing cards) with no session-reference phrasing.
- Subjective task uses separate list copies so learners need not use `.copy()` (not explicitly taught).
- Reference solution verified: both sorts produce `[9, 15, 28, 35, 42]` from `[42, 15, 28, 9, 35]`.
- OneCompiler submission steps and images match Session 01 / Sessions 02–06 course pattern.

### Action Taken

- QC passed. Assignments ready for platform upload.

---

## AssignmentCreation.csv QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | mcsc | Correct option: 2 (B). Relevancy: Yes. Markdown body; options without A/B/C prefixes. |
| Q2 | mcsc | Correct option: 2 (B). Relevancy: Yes. No Merge Sort in options. |
| Q3 | mcsc | Correct option: 2 (B). Relevancy: Yes. Code block preserved in markdown. |
| Q4 | mcsc | Correct option: 3 (C). Relevancy: Yes. |
| Q5 | mcsc | Correct option: 2 (B). Relevancy: Yes. difficultyLevel: 0.5. |
| Q6 | mcsc | Correct option: 2 (B). Relevancy: Yes. difficultyLevel: 0.5. |
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
| tagRelationships (`6a4b5e1756d5d6a4de423942` on all rows) | Pass |

**CSV QC iteration:** 1 — passed.
