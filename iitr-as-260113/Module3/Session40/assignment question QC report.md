# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Practical LLM-vs-RAG scenario for company policy gaps. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. Tests Chroma `persist_directory` meaning. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. `DirectoryLoader` + `**/*.md` glob behaviour. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: A. Relevancy: Yes. `chunk_overlap` boundary context. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. Stale vectors after editing source `.md` without re-ingest. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. `RunnablePassthrough` role in LCEL RAG chain. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Offline ingest vs online retriever invoke. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Retriever similarity search and `k` parameter. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B. Relevancy: Yes. Prompt guardrails for citation and honest refusal. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Embedding mismatch, stale Chroma, invalid overlap config. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Submission case d (multi-file repo: `documents/`, `ingest.py`, `rag_app.py`): Yes. Dataset provided inline in prompt (two policy files): Yes. Tests loaders, splitter, Chroma persist, LCEL chain, and grounded vs refusal queries. |

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
- 1 medium subjective coding task with multi-file LangChain RAG pipeline and full answer explanation.
- No “as taught in session” phrasing in learner-facing questions.
- Scope limited to LangChain loaders, chunking, Chroma persist, retriever, LCEL chain, and grounding guardrails from lecture notes.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.
