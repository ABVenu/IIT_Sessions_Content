# Assignment Question QC Report: RAG Foundations

**Cohort:** iitr-as-2603 / Module3 / Session28  
**Source:** Reused from iitr-as-2601 / Module3 / Session38 with Q9 option A wording aligned to Session28 delivery (Groq limits + ChatGPT upload vs manual paste only).  
**Aligned to:** `Lecture Notes Released.md`

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests LLM limitations for private and recent information; aligns with Siemens HR / knowledge-cutoff content in released notes. |
| 2 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests the definition of Retrieval-Augmented Generation through a practical helpdesk scenario. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests context window limitation with a large policy manual scenario. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests grounding through a prompt instruction that restricts answers to context. |
| 5 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests the correct five-step RAG flow: ingest, prepare, retrieve, augment, generate. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests diagnosis of a generator ignoring supplied context and the need for stronger grounding. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests privacy, cost, and freshness benefits of RAG without overclaiming perfection. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests embeddings as numeric vectors, meaning-space closeness, and vector DB storage; matches Sentence Transformers demo. |
| 9 | Objective MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Option A updated to "without document access vs supplied context (paste or upload)" to match Session28 Groq/ChatGPT demos; B and D match embedding demo and vector DB bridge. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests retriever, generator, grounding, and augment step roles in a RAG setup. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions: Yes. Dataset needed: No external dataset required; all four input sentences are provided in the question. Tests the covered embeddings implementation (`all-MiniLM-L6-v2`, 384-dim) without asking for full RAG/vector search implementation. |

---

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers LLM limits, RAG definition, five-step flow, retriever/generator/grounding, without/with document context concept, embeddings, vector DB bridge, privacy/cost benefits, and context window — all present in Session28 released notes. |
| Creativity | 5 | Questions use practical settings such as helpdesk, company policy assistant, support assistant, startup RAG planning, and mini embedding explorer. |
| Structural Adherence | 5 | Objective file has exactly 10 questions: 6 MCQs and 4 MSQs, ordered Easy to Moderate to Hard. Subjective file has exactly one medium practical coding task with submission instructions and complete answer explanation. |
| No Logical Mistakes | True | Correct answers align with Session28 released notes. No question requires full coded RAG pipeline, cosine similarity tuning, or LangChain implementation beyond taught scope. |
| No Presentation Mistakes | True | Files named as required, question wording is self-contained, answer explanations are complete, and no question uses unprofessional session references. |

---

## Final Status

Approved. Reused from Session38 (iitr-as-2601) with one wording update on Q9A. All required QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
