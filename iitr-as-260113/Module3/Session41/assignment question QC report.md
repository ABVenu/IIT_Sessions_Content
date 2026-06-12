# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Standalone RAG vs integrated agent arbitration scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Purpose of `create_retriever_tool`. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tool-first routing for ticket TKT-1002. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. `chat_history` vs `agent_scratchpad` for multi-turn entity resolution. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Wrong-tool failure — fix tool descriptions first. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Missing manual `chat_history` append symptom. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Agent + executor + scratchpad for tool-calling with memory. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. EvalPack fields (`expected_tool`, keywords, `failure_type`). |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Failure signatures and first fixes; D distractor (temperature) correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Routing for policy, ticket, and out-of-domain IPL refusal. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission case c (single `.py` file in LMS): Yes. Inline policy + ticket dataset provided in prompt: Yes. Tests `create_retriever_tool`, `@tool`, memory, routing, and out-of-domain refusal across four labelled demos. |

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
- 1 medium subjective coding task with single-file integrated agent and complete answer explanation.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to agentic RAG, `create_retriever_tool`, tool arbitration, memory/scratchpad, EvalPack concepts, and failure signatures from lecture notes.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.
