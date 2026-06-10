# Assignment Question QC Report: Memory & Control Flow

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests short-term memory failure on follow-up *"And in 2023?"* without prior turns. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests short-term vs long-term memory definitions and storage patterns. |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests in-memory list vs JSON persist/reload across notebook restart. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests system → user → assistant message order in history. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests missing `load_history` / history context on turn 2 follow-up. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests runaway loop risk without `MAX_STEPS` or stop words. |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests `json.dump`/`json.load`, first-run empty list, append order, crash risk; rejects JSON = enterprise long-term memory (D). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests stop words, max steps, task-done break; rejects unbounded trust in LLM (D, E). |
| 9 | Objective MSQ - Hard | Correct options: A, B, D, E. Relevancy: Yes. Tests friendly `try/except`, call-site catch, blank-input guard; rejects raw `str(exception)` to user (C). |
| 10 | Objective MSQ - Hard | Correct options: A, B, D, E. Relevancy: Yes. Tests `build_question_with_memory`, JSON reload, summarization concept, Gradio POC scope; rejects latest-bubble-only (C). |
| 1 | Subjective - Easy Practical Task | Easy difficulty: Yes (simplified per user request). Clear submission instructions (case c): Yes. Dataset needed: Inline `mock_rag_answer` stub provided — no external download. Tests save/load JSON, `append_turn`, `chat_once` with inline history join + `try/except`, two-turn follow-up only. Loop termination, stop words, `SIMULATE_API_FAIL`, and separate `build_question_with_memory`/`run_chat_turn` removed. |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective covers short vs long-term memory, conversation history roles, JSON persist/reload, memory into RAG, loop termination, user-visible errors, summarization and Gradio as concepts. Subjective (easy) covers JSON persist/reload + two-turn memory demo; loop/stop-word hands-on deferred to objective questions. |
| Creativity | 5 | EcoDrive Motors analyst scenario; practical follow-up *"And in 2023?"* proof; ATM/runaway-loop and UPI-style error framing in objectives. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one easy single-file task with case-c submission and full answer explanation. |
| No Logical Mistakes | True | Correct options verified against released notes; subjective turn 2 requires persisted history for stub to return 14.1B. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; complete answer explanations; grammar checked. |

## Iteration 2 — Simplify Subjective (user request)

**Trigger:** Make subjective assignment easier.

| Change | Before | After |
|---|---|---|
| Difficulty | Medium | **Easy** |
| Core function | `run_chat_turn` + `build_question_with_memory` + while loop | Single **`chat_once`** with inline history join |
| Stop words / max steps | Required in subjective | Removed — tested in objective only |
| Demo turns | 3 (incl. `exit`) | **2** (2022 → And in 2023?) |
| `SIMULATE_API_FAIL` | Optional env test | Removed |

**Outcome:** QC re-run — all criteria still pass.

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
