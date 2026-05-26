# Assignment Question QC Report: Implementing Vector Search Systems

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests Chroma collection as the container for ids, documents, metadata, and embeddings. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `PersistentClient` and local folder persistence. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the `document` field as human-readable stored text. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `collection.count()` as a storage verification method. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests manual query embeddings when `embedding_function=None` is used. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests `get()` as exact id lookup instead of meaning-based search. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, D. Relevancy: Yes. Tests aligned Chroma `upsert` inputs across ids, documents, metadatas, and embeddings. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests verification using `count`, `peek`, and `get`, while avoiding manual edits to Chroma storage. |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, D. Relevancy: Yes. Tests same-model rule, embedding dimensions, model choice trade-off, and unreliable distances when models are mixed. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests interpretation of rank, top-k behaviour, distance values, and weak lower-ranked matches. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions: Yes. Dataset needed: No external dataset required; the six FAQ records are defined in the task and expected code. Tests applied Chroma implementation using `PersistentClient`, `upsert`, `count`, `peek`, `get`, `query`, and distance interpretation. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers Chroma client and collection vocabulary, persistent storage, ids, documents, metadata, embeddings, manual embedding with Sentence Transformers, `upsert`, `count`, `peek`, `get`, `query`, top-k retrieval, distances, same-model rule, and local SQLite storage caution. |
| Creativity | 5 | Uses realistic support-search scenarios around e-commerce FAQ records, returns, refunds, shipping, account/password help, and payments. Questions are scenario-based and applied instead of direct recall only. |
| Structural Adherence | 5 | Objective assignment has exactly 10 questions: 6 MCQs and 4 MSQs, ordered Easy to Moderate to Hard. Subjective assignment has exactly one medium coding implementation task with clear constraints, expected behaviour, submission instructions, and full answer explanation. |
| No Logical Mistakes | True | Correct answers align with the released notes. Distractors are false but plausible. The subjective task stays within the implemented Chroma workflow and does not require later topics such as metadata filtering, ANN internals, or retrieval tuning. |
| No Presentation Mistakes | True | Files are named as required. Questions are self-contained, professional, and do not reference the session wording. Explanations are complete for objective and subjective questions. |

## Final Status

Approved. All expected QC criteria are satisfied: ratings are 5 and there are no logical or presentation mistakes.
