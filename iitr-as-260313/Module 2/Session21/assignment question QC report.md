# Assignment Question QC Report: Building a RAG Pipeline

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests the document loader role when policy content moves from code strings to external files. |
| 2 | Objective MCQ - Easy | Correct option: B. Relevancy: Yes. Tests why ingestion is an offline preparation phase separate from live customer queries. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `pypdf` / `PdfReader` as the PDF text extraction approach taught in the lab. |
| 4 | Objective MCQ - Easy | Correct option: C. Relevancy: Yes. Tests filename-based `category` inference for `returns_policy.txt`. |
| 5 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests overlap stride math (`100 - 20 = 80`) for consecutive chunks. |
| 6 | Objective MCQ - Moderate | Correct option: B. Relevancy: Yes. Tests why wrong Rank 1 category points to ingestion/chunking before blaming the generator. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests the logical order inside `build_knowledge_base` (load → chunk → index). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests practical retrieval inspection using category, excerpt text, and semantic intent. |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests multi-chunk indexing, same-model embedding rule, manual query embeddings, and metadata traceability. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests realistic failure modes for file-based ingestion, chunk boundaries, stale policy text, and folder-path misconfiguration. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions: Yes (single `rag_pipeline.py` in LMS; policy files created locally). Dataset needed: No external dataset — four policy TXT contents and two demo queries are defined in the task. Tests file loading, cleaning, chunking, BGE indexing into `shopkart_policy_kb_v2`, top-2 retrieval with distances, grounded Groq generation, and retrieve-before-generate auditing. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers document loaders, offline ingestion, TXT/PDF loader pattern, `clean_text`, overlap chunking, metadata from filenames, `build_knowledge_base`, multi-chunk Chroma indexing, top-2 retrieval with distances, grounded prompts, and file-based pipeline setup. Recursive/paragraph chunking and policy-refresh workflows are excluded (surface-level or deferred in released notes). |
| Creativity | 5 | Uses realistic ShopKart support scenarios—sealed earbuds return and 8-month charger warranty—and applied troubleshooting prompts instead of direct recall-only wording. |
| Structural Adherence | 5 | Objective assignment has exactly 10 questions: 6 MCQs (4 Easy, 2 Moderate) and 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Moderate → Hard. Subjective assignment has exactly one medium coding task with case-c submission (single `rag_pipeline.py` in LMS), constraints, expected behaviour, and full answer explanation. |
| No Logical Mistakes | True | Correct answers align with released lecture notes. Distractors are false but plausible. Overlap stride, ingestion order, and folder-path failure cases are logically consistent. Subjective task stays within taught file-based RAG scope. |
| No Presentation Mistakes | True | Files named as required. Questions are self-contained, professional, and free of session-reference wording. Answer explanations are complete for all objective and subjective items. |

## AssignmentCreation.csv QC

| Check | Result |
|---|---|
| File created | `AssignmentCreation.csv` in Session21 folder |
| Row count | 11 (10 objective + 1 subjective) |
| tagRelationships | `6a27cbfc3bfa06082c5c33e6` on all rows |
| Question bodies | No question numbers or difficulty labels in `contentBody` |
| Options | Plain option text only (no A/B/C prefixes) |
| CSV parse test | Pass — 12 rows (header + 11 data), 20 columns each |
| Subjective solution | Full reference code in `answerExplanation` only |

## Final Status

Approved. All expected QC criteria are satisfied: ratings are 5 and there are no logical or presentation mistakes. `AssignmentCreation.csv` generated and parse-verified.
