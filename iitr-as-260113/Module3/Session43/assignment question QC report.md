# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Debugging definition via UPI payment scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Final-answer-only vs trajectory debugging for wrong-tool path. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Meaning of failure class as defect category. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Wrong tool selection → tool patch for vague description. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. Over-refusal on valid in-domain refund question. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Weak retrieval from bad chunking (electronics without seven days). |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Missing tool call remediation (prompt, tool, examples). |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Observability signals: latency, memory, tokens. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Cost–latency trade-off when raising retrieval K. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Controlled iteration, harness re-run, resource checks. |
| Q1 | Subjective (Practical, Easy) | Easy implementation (no TODO/starter blanks): Yes. Submission case c (single `debug_helper.py` in LMS): Yes. Full spec for 3 functions + main; top-1 chunk diagnosis verified (50/10 → 5 chunks, weak_retrieval_split; 150/20 → 2 chunks, ok_both_present); four symptom→remediation mappings; no API keys required. |

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
- 1 easy subjective implementation task (chunk simulation + failure triage; single-file LMS submission; no fill-in-the-blanks starter).
- Complete answer explanations for every objective and subjective question.
- No “as taught in session” phrasing in learner-facing questions.
- Subjective scope: retrieval tuning concept (character chunks + top-1 diagnosis) and remediation mapping — aligned with lecture demo without requiring OpenAI/Chroma.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified after top-1 diagnosis fix.

**QC iteration:** 1 — passed.

---

## Iteration 2 — Subjective expected-output fix

**Trigger:** Initial expected chunk counts (4 / 1) did not match reference implementation; diagnosis updated to **top-1 retrieved chunk** (matches lecture weak-retrieval story).

| Question | Type | Remarks |
| --- | --- | --- |
| Q1 | Subjective | Expected table corrected to 5 chunks @ 50/10 and 2 chunks @ 150/20; `diagnose_chunk_gap` docstring clarifies top-1 simulation; reference solution re-verified in Python. |

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**Outcome:** Subjective QC passed after expected-output correction.

---

## Iteration 3 — Subjective rewritten as full implementation

**Trigger:** User requested no fill-in-the-blanks / TODO starter — implementation type only; keep easy/simple.

| Question | Type | Remarks |
| --- | --- | --- |
| Q1 | Subjective | Removed starter skeleton with `pass` / TODO markers; replaced with full specification + expected stdout; difficulty lowered to Easy; complete reference solution in answer explanation only. |

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**Outcome:** Subjective QC passed after implementation-style rewrite.

---

## Iteration 4 — `assignment.csv` for Assess platform

**Trigger:** CSV export with `tagRelationships` = `6a33a77a7edb35dffca5c4b7`.

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) |
| `tagRelationships` on all rows | `6a33a77a7edb35dffca5c4b7` |
| CSV parse QC | Passed — no parsing errors |
| Content alignment | Matches `assignment-objective.md` and implementation-style `assignment-subjective.md` |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) |
| Question bodies | No Q-number/difficulty prefix; options without A/B/C labels |
