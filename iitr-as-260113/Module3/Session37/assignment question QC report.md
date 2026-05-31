# Assignment Question QC Report — Session 37 (LangChain Tools: Custom Tools and Tool Calling)

**Source notes:** `Lecture Notes Released.md` (LangChain Tools: Custom Tools and Tool Calling)  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`

---

## Per-question QC table

| # | Type | Remarks |
|---|------|---------|
| Q1 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (LLM-only apps may guess live order data instead of using APIs/tools). |
| Q2 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (`@tool` decorator registers a Python function as a LangChain tool). |
| Q3 | MCQ — Easy | Correct: **C**; relevancy: **Yes** (application code executes tools, not the LLM). |
| Q4 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (`ToolMessage` carries tool output linked by `tool_call_id`). |
| Q5 | MCQ — Moderate | Correct: **A**; relevancy: **Yes** (`bind_tools` attaches tool definitions for structured `tool_calls`). |
| Q6 | MCQ — Moderate | Correct: **B**; relevancy: **Yes** (second model turn formats raw tool data for users). |
| Q7 | MSQ — Moderate | Correct: **A, B, C**; relevancy: **Yes** (Pydantic validation, `Field` descriptions, `Literal` constraints). |
| Q8 | MSQ — Moderate | Correct: **A, B, C**; relevancy: **Yes** (safe execution, `tools_by_name`, unknown-tool errors). |
| Q9 | MSQ — Hard | Correct: **A, B, C**; relevancy: **Yes** (system prompt, tool metadata, tracing `tool_calls` for wrong selection). |
| Q10 | MSQ — Hard | Correct: **A, B, C**; relevancy: **Yes** (manual loop: append `AIMessage`, exit when no `tool_calls`, `max_steps` safety). |
| Subjective | Coding implementation (starter + TODOs) | Easy–medium difficulty: **Yes** (one tool, short two-invoke loop, no `unknown_tool` / policy tool / `max_steps` agent required); clear submission instructions (Case C): **Yes**; dataset required: **No** (single mock order in prompt + skeleton). Reference solution included. |

---

## Overall QC ratings (both assignments)

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Covers why tools are needed, `@tool`, Pydantic `args_schema`/`Literal`, `bind_tools`, `tool_calls`, `ToolMessage`, safe execution, manual agent loop, structured JSON errors, diagnosing tool selection, and bounded `max_steps`. |
| Creativity | 5 | Scenarios use food delivery and Campus Crate order help—not bare definitions. Subjective uses a guided starter so learners apply the tool loop without rebuilding the full class agent. |
| Structural Adherence | 5 | Objective: exactly 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Subjective: one easy–medium coding task with Case C submission, starter skeleton, and full answer explanation. |
| No Logical Mistakes | True | All correct options and MSQ sets verified against lecture notes; distractors are plausible but clearly wrong. |
| No Presentation Mistakes | True | Grammar, spelling, formatting, and no “as taught in session” phrasing in questions. |

---

## Improvisation log

- **Round 1:** Initial objective, subjective, and QC tables reviewed. All criteria met.
- **Round 2 (subjective only):** Simplified per learner feedback—reduced to **one tool**, provided **starter skeleton with TODOs**, removed policy/`Literal` tool, removed full `execute_tool_call_safely` + `max_steps` agent; kept core `@tool` → `bind_tools` → `ToolMessage` → second invoke. Subjective QC re-run: all criteria still met.

---

**QC sign-off:** Expected result satisfied — Content Coverage, Creativity, and Structural Adherence are **not less than 5**; **No Logical Mistakes** and **No Presentation Mistakes** are **True**.
