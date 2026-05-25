# Assignment Question QC Report: Introduction to Vector Databases

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests same embedding model requirement for document and query vectors. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests exact-key lookup for structured id-based queries. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the core role of a vector database: store, index, and retrieve embeddings. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests semantic similarity search for meaning-based product retrieval. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests brute-force vector search limitation at scale. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests top-k retrieval as returning the best few nearest results. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests useful metadata fields stored with vectors. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests appropriate SQL vs vector search decisions and combined usage. |
| 9 | Objective MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Tests ANN speed-accuracy trade-off and index structure awareness. |
| 10 | Objective MSQ - Hard | Correct options: A, C, D, E. Relevancy: Yes. Tests end-to-end vector search flow, same model rule, indexing, K-means/KNN distinction, and FAISS awareness. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions: Yes. Dataset needed: No external dataset required; the scenario and constraints are provided. Tests applied understanding without requiring Chroma setup or full coding, matching the conceptual scope. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers embeddings, same-model rule, SQL vs vector search, vector database roles, metadata, similarity search, top-k, brute-force scale limits, Big O intuition, indexing, ANN, FAISS/HNSW awareness, K-means/KNN distinction, and end-to-end retrieval flow. |
| Creativity | 5 | Uses realistic scenarios such as course support bots, coaching institute support, shopping app retrieval, policy assistants, FAQ chunks, payments, and student questions. |
| Structural Adherence | 5 | Objective assignment has exactly 10 questions: 6 MCQs and 4 MSQs, ordered Easy to Moderate to Hard. Subjective assignment has exactly one medium applied practical task with clear answer format and submission instructions. |
| No Logical Mistakes | True | Correct answers align with the released notes. Distractors are false but plausible. The subjective task does not ask for Chroma implementation or advanced algorithms beyond the conceptual scope. |
| No Presentation Mistakes | True | Files are named as required. Questions are self-contained, professional, and do not reference the session wording. Explanations are complete for objective and subjective questions. |

## Final Status

Approved. All expected QC criteria are satisfied: ratings are 5 and there are no logical or presentation mistakes.
