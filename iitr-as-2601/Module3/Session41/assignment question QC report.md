# Assignment Question QC Report: RAG — Retrieval & Grounded Generation

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the Retrieve step in the five-step RAG loop. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests same embedding model rule when reopening a persisted index. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `temperature=0` for repeatable factual RAG answers. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests purpose of `#context` / `#question` delimiter tokens. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests low-k miss vs modest k increase trade-off. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests grounded refusal for out-of-corpus questions. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests LangChain retriever setup and persisted Chroma reload. |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests informal grounding audit checklist. |
| 9 | Objective MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Tests grounding illusion response: audit, tighten rules, tune k. |
| 10 | Objective MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests enterprise persistent RAG vs ChatGPT session upload; rejects customer upserts and mandatory custom LLM training. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions (case c): Yes. Dataset needed: Inline `CORPUS` provided — no external download. Tests index build, LangChain retriever k=3, `#context`/`#question` assembly, Groq `temperature=0`, in-corpus + out-of-corpus queries with retrieval trace. Gradio omitted (surface-level only). |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective covers top-k retrieval, delimiters, grounded generation, grounding audit, grounding illusions, enterprise vs session RAG. Subjective covers end-to-end retrieve → augment → generate on a self-contained corpus. |
| Creativity | 5 | FinSight / NovaTech analyst scenario; practical refusal test; grounding-illusion troubleshooting in MSQs. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one medium single-file task with case-c submission and full answer explanation. |
| No Logical Mistakes | True | Correct options verified against released notes; subjective expected outputs align with provided corpus (48.2B revenue; weather refusal). |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations; grammar checked. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
