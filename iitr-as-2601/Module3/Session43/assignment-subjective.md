# Subjective Assignment: FinPulse ReAct Agent

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

**FinPulse Research Desk** helps junior analysts answer questions that need **live web facts** (for example today's index price) and **exact Python math** (for example compound growth) in one workflow.

Your task is to build a **single-file ReAct agent script** that:

1. Wraps and smoke-tests two LangChain tools  
2. Runs a **Python-only** ReAct agent for a calculation question  
3. Runs a **search + Python** ReAct agent for a live-market question  

Use **Groq** and **Serper** API keys from environment variables: `GROQ_API_KEY` and `SERPER_API_KEY`.

---

## Task

Create one file: `finpulse_react_agent.py`

### Step 1 — Setup and tools

- Import `os`, `hub`, `ChatGroq`, `Tool`, `AgentExecutor`, `create_react_agent`, `PythonREPL`, and `GoogleSerperAPIWrapper`.
- Read both API keys from `os.environ`.
- Create `groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key, temperature=0)`.
- Wrap **`repl_tool`** with `name="python_repl"`, a clear description, and `func=python_repl.run`.
- Wrap **`search_tool`** with `name="serper_search"`, a clear description, and `func=serper_search.run`.

### Step 2 — Smoke-test both tools

Write `test_tools(repl_tool, search_tool)` that:

- Calls `repl_tool.invoke('print(1250 * 1.08)')` and prints the result.
- Calls `search_tool.invoke("Who is the founder of Tesla?")` and prints the first **120 characters** of the result.

### Step 3 — Python-only ReAct agent

- Pull `react_prompt = hub.pull("hwchase17/react")`.
- Build a Python agent with `create_react_agent(llm=groq_llm, tools=[repl_tool], prompt=react_prompt)`.
- Build an executor with `AgentExecutor(agent=..., tools=[repl_tool], verbose=True)`.
- Run this query and print the final answer:

```text
If $ 450 amounts to $ 630 in 6 years, what will it amount to in 2 years at the same interest rate?
```

### Step 4 — Search + Python ReAct agent

- Reuse the same `react_prompt`.
- Build a second agent with **both** tools: `[search_tool, repl_tool]` — use the **same list** in `create_react_agent` and `AgentExecutor`.
- Set `verbose=True` and `max_iterations=8` on the executor.
- Run this query and print the final answer:

```text
What is the closing stock price of Nifty today?
```

### Step 5 — `main()` entry point

```python
def main():
    # Step 1: read keys, create groq_llm, repl_tool, search_tool

    print("=== Tool smoke tests ===")
    test_tools(repl_tool, search_tool)

    print("\n=== Python-only agent ===")
    # Step 3 here

    print("\n=== Two-tool search agent ===")
    # Step 4 here


if __name__ == "__main__":
    main()
```

---

## Expected behaviour

When you run `python finpulse_react_agent.py`:

| Section | What you should see |
|---|---|
| Tool smoke tests | A numeric REPL result (for example `1350.0`) and a short Tesla-founder search snippet |
| Python-only agent | A natural-language answer to the compound-interest question |
| Two-tool search agent | An answer about **Nifty** based on live search (exact wording may vary by market day) |

With `verbose=True`, you should see **Thought → Action → Observation** steps before each **Final Answer**.

---

## Submission Instructions

- Code all steps in VS Code in a single `.py` file named `finpulse_react_agent.py`.
- Export `GROQ_API_KEY` and `SERPER_API_KEY`, run the script, and verify all three sections print output.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. **Step 1** registers each worker (`repl_tool`, `search_tool`) with a **name**, **description**, and **func** — the manager reads these before picking a tool.
2. **Step 2** proves each tool works on its own with `.invoke()` before paying for agent loops.
3. **Step 3** binds one tool via `create_react_agent` and runs the ReAct loop through `AgentExecutor.invoke`.
4. **Step 4** adds a second tool and `max_iterations=8` so the loop cannot run forever on live-search questions.
5. **`verbose=True`** prints Thought / Action / Observation so you can confirm tool results arrive before the final answer.

### Reference Solution

```python
import os

from langchain import hub
from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_experimental.utilities import PythonREPL
from langchain_community.utilities import GoogleSerperAPIWrapper


def test_tools(repl_tool, search_tool):
    print("REPL:", repl_tool.invoke("print(1250 * 1.08)"))
    snippet = search_tool.invoke("Who is the founder of Tesla?")
    print("Search:", snippet[:120])


def main():
    groq_api_key = os.environ["GROQ_API_KEY"]
    serper_api_key = os.environ["SERPER_API_KEY"]

    groq_llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=groq_api_key,
        temperature=0,
    )

    python_repl = PythonREPL()
    repl_tool = Tool(
        name="python_repl",
        description="A Python shell used to execute python commands. Input should be a valid python command.",
        func=python_repl.run,
    )

    serper_search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
    search_tool = Tool(
        name="serper_search",
        description="An interface to the Serper search engine. Input should be a string.",
        func=serper_search.run,
    )

    print("=== Tool smoke tests ===")
    test_tools(repl_tool, search_tool)

    react_prompt = hub.pull("hwchase17/react")

    python_agent = create_react_agent(
        llm=groq_llm, tools=[repl_tool], prompt=react_prompt
    )
    python_executor = AgentExecutor(
        agent=python_agent, tools=[repl_tool], verbose=True
    )

    compound_query = (
        "If $ 450 amounts to $ 630 in 6 years, what will it amount to in 2 years "
        "at the same interest rate?"
    )
    print("\n=== Python-only agent ===")
    result_python = python_executor.invoke({"input": compound_query})
    print("Python agent answer:", result_python["output"])

    search_agent = create_react_agent(
        llm=groq_llm, tools=[search_tool, repl_tool], prompt=react_prompt
    )
    search_executor = AgentExecutor(
        agent=search_agent,
        tools=[search_tool, repl_tool],
        verbose=True,
        max_iterations=8,
    )

    nifty_query = "What is the closing stock price of Nifty today?"
    print("\n=== Two-tool search agent ===")
    result_search = search_executor.invoke({"input": nifty_query})
    print("Search agent answer:", result_search["output"])


if __name__ == "__main__":
    main()
```

### Alternative approaches

- Use a different Groq model (for example Gemma) if rate limits occur — keep `temperature=0`.
- Swap the Step 4 query for the Nvidia + `$100` multi-tool question for a harder self-test.
- Wrap `invoke` calls in `try/except` and print a friendly message on API failure (optional).

### Notes for evaluation

- Compound-interest wording may vary slightly; the answer should reflect a 2-year amount at the rate implied by the 6-year growth.
- Nifty answer wording depends on live search results — credit for a coherent price answer with evidence of `serper_search` in the verbose trace.
- Missing API keys or skipped `Tool` wrapper should be marked incomplete.
- `tools=` lists must match between `create_react_agent` and `AgentExecutor`.
