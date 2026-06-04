# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tests stateless LLM behavior in a practical support scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Clarifies placeholder vs storage responsibility. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tests `optional=True` for empty first-turn history. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Distinguishes scratchpad from long-term chat memory. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Targets the missing-append wiring defect from lecture notes. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. Applied follow-up scenario requiring rolling history. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Manual memory wiring best practices. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Multi-user session isolation concepts. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Correct split between `chat_history` and `agent_scratchpad`. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Production trade-offs (`n_messages`, RAM, shared-list bug). |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Clear submission instructions (case c, single `.py`): Yes. Dataset need: Not required (`orders_db` specified in prompt). Covers manual memory, two-turn demo, append order, and history length check. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1-5) | 5 |
| Creativity (1-5) | 5 |
| Structural Adherence (1-5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria are satisfied:
- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective coding task with full answer explanation and reference solution.
- No session-reference phrasing in learner-facing questions.
- Content Coverage, Creativity, Structural Adherence are all 5.
- No logical or presentation mistakes identified.
