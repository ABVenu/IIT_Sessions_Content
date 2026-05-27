# Assignment Question QC Report: Embeddings & Vector Search

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests embeddings as semantic coordinates via the music fingerprint analogy. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests 384-dimensional output of `all-MiniLM-L6-v2`. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the same-model rule when mixing encoders. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests Chroma as store/search vs embedding model. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests predicting top semantic match for a return/refund paraphrase. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests `query_embeddings` requirement when `embedding_function=None`. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests keyword vs semantic search strengths and combined use. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests post-upsert verification and aligned lists. |
| 9 | Objective MSQ - Hard | Correct options: A, B, D, E. Relevancy: Yes. Tests rank, distance interpretation, relative scores, and weak rank-1 when data is missing. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, D. Relevancy: Yes. Tests manual embed-upsert-query pipeline and get vs query roles. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions (case c): Yes. Dataset needed: No external dataset; all five FAQ rows and three queries are specified in the question. Gap-analysis block tests applied understanding of missing-topic retrieval. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers embeddings as coordinates, vector size, same-model rule, Chroma role, semantic vs keyword search, top-match prediction, manual query embeddings, verification steps, distance/rank interpretation, and full Chroma lab pipeline. |
| Creativity | 5 | Uses music-app analogy, e-commerce paraphrase scenarios, UPI gap-analysis coding task, and practical helpdesk framing throughout. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one medium coding task with case-c submission and full answer explanation. |
| No Logical Mistakes | True | Correct answers match lecture notes; UPI weak-match scenario aligns with taught content; no out-of-scope asks (PDF chunking, full RAG chatbot, metadata filters). |
| No Presentation Mistakes | True | Self-contained wording, no “as taught in session” references, complete answer explanations, required file names. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
