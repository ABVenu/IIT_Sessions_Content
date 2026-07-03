# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Missing `()` on function call produces no output. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Parameter vs argument using delivery-address scenario. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. `def` keyword for creating reusable functions. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `return` needed to reuse calculated values. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Default parameter `bonus=0` gives `500` when only `amount` is passed. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: C. Relevancy: Yes. Returned value `n=3` leads to natural-number sum `6`. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Parameters, arguments, and positional matching; D correctly excluded. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. `print()` vs `return` behaviour; C correctly excluded (`y` is `None`). |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. DRY, function chaining, and one-job-per-function modular design; D correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Default parameters, required-parameter error, and chained `add_tax` trace; D correctly excluded (`bill` is `12.1`). |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission via single `.py` file in VS Code and LMS code editor (case c): Yes. No external dataset needed — quantities taken from user input. Tests `def`, parameters, arguments, `return`, default parameter, function chaining, and modular billing logic. Sample outputs verified: `553.85` for input `5, 2, 3`; `220.0` for input `2, 1, 1`. |

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
- 1 medium subjective coding task with single-file VS Code + LMS submission instructions.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to `def`, function calls, parameters, arguments, `return`, default values, `print()` vs `return`, function chaining, modular programming, DRY, and common function mistakes from released lecture notes.
- Surface-level ideas such as calling one function from inside another are not required as a separate implementation task; they are covered only through objective checks.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified after correcting the subjective sample-output arithmetic.

**QC iteration:** 2 — passed.

---

## CSV Export QC

**File:** `AssignmentCreation.csv`  
**Trigger:** CSV export with `tagRelationships` = `6a4761641bd83eb6f24f2b94`.

| Check | Result |
| --- | --- |
| Total rows | 11 (10 objective + 1 subjective) |
| `tagRelationships` on all rows | `6a4761641bd83eb6f24f2b94` |
| Question types | 6 `mcsc`, 4 `mcmc`, 1 `subjective` |
| Difficulty flow | Easy (0) → Moderate (0.5) → Hard (1) |
| `contentType` / `answerExplanationType` | `markdown` on all rows |
| Question bodies | No question numbers or difficulty labels in `contentBody` |
| Options | No `A.` / `B.` prefixes; content starts directly |
| Subjective solution | Full reference code in `answerExplanation` only; `subjectiveAnswer` empty |
| CSV parsing | Passed — 11 rows round-trip with no errors |

**CSV QC iteration:** 1 — passed.
