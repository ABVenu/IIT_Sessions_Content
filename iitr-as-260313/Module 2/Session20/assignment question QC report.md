# Assignment Question QC Report: RAG Architecture and Pipeline

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests knowledge boundary behaviour when a customer question is outside allowed ShopKart policy sources. |
| 2 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests the difference between retrieval-only search and a complete RAG loop with generation. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests ingestion as the offline embed-and-store component in the minimal pipeline. |
| 4 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests secure `.env` usage for `GROQ_API_KEY` instead of hard-coding secrets. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests manual query embeddings when `embedding_function=None` is used in Chroma. |
| 6 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests why retrieve-first, generate-second order matters for grounded answers. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests practical retrieval-intent inspection using category, excerpt text, and semantic intent. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests grounded-prompt rules that restrict guessing and unsupported policy claims. |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests BGE same-model rule, 384-dimensional embeddings, unreliable mixed-model distances, and manual encoding workflow. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests realistic RAG failure modes across retrieval, generation, stale policy text, and evidence auditing. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions: Yes (single `.py` file, run and submit in LMS). Dataset needed: No external dataset required; the four ShopKart policy records and three demo queries are defined in the task. Tests applied RAG implementation using BGE embeddings, Chroma indexing/query, Groq grounded generation, `.env` key loading, retrieval inspection, and retrieve-before-generate order. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers knowledge boundary, ingestion/retrieval/generation roles, Chroma manual embeddings, BGE 384-dim vectors, top-k retrieval, grounded prompt rules, Groq generation, `.env` security, retrieval inspection, evidence auditing, and realistic failure modes. LLM-only baseline and metadata filtering are excluded because they were not part of the released implementation scope. |
| Creativity | 5 | Uses realistic ShopKart support scenarios around returns, shipping, warranty, refunds, COD refunds, opened-item eligibility, and express delivery. Questions are scenario-based and applied rather than direct recall only. |
| Structural Adherence | 5 | Objective assignment has exactly 10 questions: 6 MCQs (4 Easy, 2 Moderate) and 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Moderate → Hard. Subjective assignment has exactly one medium coding implementation task with clear constraints, expected behaviour, submission instructions, and full answer explanation. |
| No Logical Mistakes | True | Correct answers align with the released notes. Distractors are false but plausible. The subjective task stays within the taught minimal RAG workflow and does not require later topics such as metadata filtering or LLM-only baseline comparison. |
| No Presentation Mistakes | True | Files are named as required. Questions are self-contained, professional, and do not reference session wording. Explanations are complete for objective and subjective questions. |

## Final Status

Approved. All expected QC criteria are satisfied: ratings are 5 and there are no logical or presentation mistakes.
