# Assignment Question QC Report

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests why exact fee rules need a tool instead of LLM guessing, using an EdTech parent fee scenario. |
| Q2 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the purpose of `@tool` as wrapping a Python function for LangChain exposure. Incorrect options describe unrelated behaviour. |
| Q3 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests that `bind_tools` registers tool availability without executing tools. Other options confuse binding with execution or message conversion. |
| Q4 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests the separation of responsibilities — the application executes tools, not the LLM. Other options misassign execution to model, message class, or browser. |
| Q5 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests the manual loop step of executing tools, sending `ToolMessage`, and invoking again. Other options skip execution or break loop logic. |
| Q6 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests diagnosis of wrong argument names and wrong argument type in a realistic `tool_calls` payload. Other options invent invalid rules about `id`, `name`, or `type`. |
| Q7 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests what `@tool` exposes from a function. Option D is correctly excluded because `.env` secrets are not auto-shared. |
| Q8 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests good tool design practices (clear names, type hints, docstrings). Option D is correctly excluded as an anti-pattern. |
| Q9 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests manual loop components: `HumanMessage`, `AIMessage.tool_calls`, and `tool_map`. Option D is correctly excluded because `bind_tools` does not execute tools upfront. |
| Q10 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests temperature/model/trace debugging when `tool_calls` is empty. Option D is correctly excluded because removing docstrings harms tool selection. |
| Subjective | Practical Task - Medium | Medium difficulty: Yes. Clear submission instructions (case c — single `.py` file in LMS code box): Yes. Dataset needed: No — in-memory ticket dictionary provided in the question. Task stays within covered implementation: `@tool`, `bind_tools`, `tool_calls`, `ToolMessage`, `HumanMessage`, manual loop, and three demo-tool patterns. Does not require error-containment `try/except`, `max_steps`, GitHub repo submission, or surface-only MCP implementation. |

## Overall QC

| Criterion | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 / 5 | Covers why tools are needed, `@tool`, `bind_tools`, `tool_calls`, `ToolMessage`, manual tool-feedback loop, type hints/docstrings, multiple tool calls, fault diagnosis, and temperature/model debugging from the released notes. |
| Creativity | 5 / 5 | Questions use practical contexts such as parent fee queries, night-shift learner support, intern tool design, and realistic debugging traces. Subjective task applies the loop to a combined eligibility + fee scenario. |
| Structural Adherence | 5 / 5 | Objective assignment has exactly 10 questions: 6 MCQs (4 Easy, 2 Moderate) and 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Moderate → Hard. Subjective assignment has exactly 1 medium practical task. |
| No Logical Mistakes | True | Correct answers are valid; explanations justify incorrect options. Subjective solution matches requirements and uses only taught tool-calling patterns. |
| No Presentation Mistakes | True | Files named correctly, no session-reference phrasing in questions, self-contained prompts, complete answer explanations, and consistent formatting. |

## Final QC Outcome

PASS — Expected QC result achieved. No modification required.

## CSV export QC — `AssignmentCreation.csv`

**Trigger:** CSV export with `tagRelationships` = `6a4760b547567d189db92b75`.

| Check | Result |
|---|---|
| Row count | 11 data rows + header (6 MCSC, 4 MCMC, 1 subjective) |
| `tagRelationships` on all rows | `6a4760b547567d189db92b75` |
| Question bodies start without Q numbers/difficulty labels | Pass |
| Options start without A/B/C/D prefixes | Pass |
| `mcscAnswer` / `mcmcAnswer` indices | Pass — 1-based; MCMC uses `1, 2, 3` where applicable |
| `difficultyLevel` mapping | Pass — Easy `0`, Moderate `0.5`, Hard `1`, subjective `0.5` |
| Subjective solution in `answerExplanation` only | Pass — full code in explanation field |
| Markdown preserved in multiline/code fields | Pass |
| CSV parse test | Pass — 12 rows × 19 columns; no field-count or quoting errors |

**CSV QC outcome:** PASS
