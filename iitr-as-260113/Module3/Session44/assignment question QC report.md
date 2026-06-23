# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. RAG retrieval step in enterprise agent pattern (leave policy search). |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Finance guardrail — policy-bound reimbursement approval. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. InMemoryVectorStore for small lab prototype. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. AIMessage vs ToolMessage for end-user display. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. `get_mandatory_trainings` for role-based training query. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Escalation when policy evidence missing. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Finance vs HR vs content domain differences. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. HR answer format components; D is deliberate distractor (PIN). |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Eval harness refusal + forbidden tool failures. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Stakeholder demo and residual risks. |
| Q1 | Subjective (Applied Explanation, Easy) | Simple explanation type — no coding per user request. Submission case a (type in answer box): Yes. Clear dual-scenario prompt (in-domain leave vs out-of-corpus weather); four bullet points per message; 150–250 word limit; ideal answer table + sample in explanation only. |

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
- 1 subjective **applied explanation** question — simple, no coding; LMS answer-box submission.
- Complete answer explanations for every objective and subjective question.
- No “as taught in session” phrasing in learner-facing questions.
- Objective scope: enterprise pattern, finance/HR/content contrast, InMemoryVectorStore, tools, messages, escalation, eval refusal, stakeholder demo.
- Subjective tests in-domain vs out-of-corpus handling, tool choice, evidence/refusal, and risk — aligned with lecture notes without implementation requirement.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## Iteration 2 — Subjective simplification verification

**Trigger:** User requested subjective keep simple, no coding, explanation type only.

| Question | Type | Remarks |
| --- | --- | --- |
| Q1 | Subjective | Confirmed no code blocks in learner task; difficulty Easy; word limit keeps response bounded; Priya/Rahul scenario is self-contained. |

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**Outcome:** Subjective QC passed on iteration 2.

---

## Iteration 3 — `assignment.csv` for Assess platform

**Trigger:** CSV export with `tagRelationships` = `6a3a2ba5f376a4a6b8e33b9c`.

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) |
| `tagRelationships` on all rows | `6a3a2ba5f376a4a6b8e33b9c` |
| CSV parse QC | Passed — Python `csv.DictReader` no errors |
| Content alignment | Matches `assignment-objective.md` and `assignment-subjective.md` |
| Subjective solution | In `answerExplanation` only (not `subjectiveAnswer`) |
| Question bodies | No Q-number/difficulty prefix; options without A/B/C labels |
| Difficulty levels | Easy MCQ `0`; Moderate MCQ/MSQ `0.5`; Hard MSQ `1`; Subjective `0` |
