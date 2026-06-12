# Assignment Question QC Report: Agent Tool Use

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests AI agent definition (LLM + tools + prompt in a loop) via FinPulse scenario. |
| 2 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests ReAct acronym (Reasoning + Acting). |
| 3 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests Observation as raw tool output before next Thought. |
| 4 | Objective MCQ - Easy | Correct option: A. Relevancy: Yes. Tests LangChain Tool schema fields: name, description, func. |
| 5 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests vague tool description causing wrong tool selection on Nifty query. |
| 6 | Objective MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests create_react_agent (policy) vs AgentExecutor (runtime invoke loop). |
| 7 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests observation-before-next-reasoning, verbose debugging, AgentExecutor scratchpad; rejects skipping tool output (D). |
| 8 | Objective MSQ - Moderate | Correct options: A, B, C, E. Relevancy: Yes. Tests Tool wrap, matching tool lists, invoke smoke tests, hub prompt; rejects raw PythonREPL without Tool (D). |
| 9 | Objective MSQ - Hard | Correct options: A, B, C, E. Relevancy: Yes. Tests max_iterations, token/rate-limit awareness, verbose trace debugging; rejects showing verbose to end users (D). |
| 10 | Objective MSQ - Hard | Correct options: A, C, D. Relevancy: Yes. Tests multi-tool Nvidia sequence (search before Python, multiple cycles, intermediate vs final observations); rejects REPL-only live price (B) and zero-observation answers (E). |
| 1 | Subjective - Medium Practical Task | Medium difficulty: Yes. Clear submission instructions (case c): Yes — single `.py` file, run and verify, submit in LMS. No external dataset needed; API keys via `os.environ` documented. Covers Tool wrap, invoke smoke tests, Python-only agent, two-tool agent with `max_iterations=8`, compound-interest + Nifty queries. FinPulse desk scenario; simplified to 5 steps (removed custom `validate_tool_lists` helper). |

## Overall Assignment QC

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Objective covers agent definition, ReAct steps, Tool schema, manager/worker descriptions, register/bind, observation handling, AgentExecutor vs policy, max_iterations/tokens/debugging, multi-tool routing. Subjective implements core ReAct lab path: tools, smoke tests, one-tool agent, two-tool agent with loop cap. |
| Creativity | 5 | FinPulse Research Desk scenario; applied analyst queries (Nifty, compound interest); manager/worker framing in objective Q5. |
| Structural Adherence | 5 | Objective: 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard. Subjective: one medium single-file task with case-c submission and full answer explanation (walkthrough, reference code, alternatives, evaluation notes). |
| No Logical Mistakes | True | Correct options verified against Lecture Notes Released.md; subjective queries and expected outputs match taught demos; matching `tools=` lists noted in evaluation without requiring a separate validation function. |
| No Presentation Mistakes | True | Self-contained wording; no “as taught in session” references; expected-behaviour table for clarity; complete answer explanations for all 11 questions; grammar checked. |

## Final Status

Approved. All QC criteria meet the expected result: ratings are 5 and there are no logical or presentation mistakes.
