# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tests fixed eval set comparability. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Hit rate 3/5 = 60% matches released notes. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Context relevance = retrieval quality. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Expected supporting document definition. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Q2-style retrieval miss; retrieval fix first. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Separate judge model reduces bias. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Eval set design from released notes. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Retrieval-side tuning knobs. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, C. Relevancy: Yes. Retrieval failure = missing expected doc in top-k. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Agentic RAG routing architecture. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Clear submission instructions (case c — single `.py`): Yes. Corpus and eval set specified in prompt: Yes. Aligns with released notes: fixed eval set, keyword retriever, hit rate. No vector DB/LLM/agentic RAG required. |

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

## Scope Alignment Notes

- Questions align with **`Lecture Notes Released.md`** (conceptual measurement/diagnosis), not the pre-session hands-on tuning lab removed from release.
- Subjective is **simple implementation**: frozen `CORPUS` + `EVAL_SET`, keyword `retrieve_top_k`, `is_hit`, `retrieval_hit_rate`, printed trace — no vector DB, LLM, or agentic RAG build required.
- No session-reference phrasing in question prompts.

---

## Final QC Decision

All expected criteria are satisfied:
- Content Coverage, Creativity, Structural Adherence are all 5.
- No logical mistakes.
- No presentation mistakes.
