# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Trajectory vs output-only testing for agents. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Meaning of `must_use_tools` in eval JSON. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Purpose of `results.csv` as sortable mark sheet. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `forbidden_tools` for private-data refusal case. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: C. Relevancy: Yes. Score formula with two failures (`1 − 0.5 = 0.50`). |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. `contextvars` per-case trace isolation. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Runner pipeline steps (load → invoke → score). |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Debugging `weak_grounding` with traces and expected JSON. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Harness extensibility when adding new tools. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Triage using lowest scores, failure traces, regression re-runs. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes (guided mini-lab). Submission case c (single `eval_scorer.py` in LMS): Yes. Provided JSON (3 cases) + starter with 3 TODOs; mock runs embedded; tests `must_use_tools`, `must_contain`, `should_refuse`, scoring formula, `results.csv`; expected 2 pass / 1 fail verified. |

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

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective guided mini-lab (starter code + 3 TODOs, single-file LMS submission).
- Complete answer explanations for every objective and subjective question.
- No “as taught in session” phrasing in learner-facing questions.
- Subjective scope: core eval JSON fields, mock grading, `results.csv`, refusal check, sample score rubric — lighter than full harness (no traces folder, no GitHub, no student-designed cases).
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## Iteration 2 — Subjective lightened

**Trigger:** User requested lighter subjective assignment.

| Question | Type | Remarks |
| --- | --- | --- |
| Q1 | Subjective | Reduced from 5-case GitHub harness to 3-case guided lab; starter `MOCK_RUNS` provided; only `contains_refusal`, `evaluate_case`, `write_results` to implement; case c LMS submission; answer explanation trimmed to TODO solutions only. |

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**Outcome:** Subjective QC passed after lightening.

---

## Iteration 3 — `assignment.csv` for Assess platform

**Trigger:** CSV export with `tagRelationships` = `6a30b1c9382684bc99b21dcf`.

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) |
| `tagRelationships` on all rows | `6a30b1c9382684bc99b21dcf` |
| CSV parse QC | Passed — no parsing errors |
| Content alignment | Matches current `assignment-objective.md` and lightened `assignment-subjective.md` |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) |
