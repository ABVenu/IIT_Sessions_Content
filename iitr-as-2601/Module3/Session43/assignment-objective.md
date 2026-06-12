# Objective Assignment: Agent Tool Use

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

Rahul's team is building a **FinPulse** assistant that must look up today's index prices on the web and run exact interest calculations in Python before replying.

Which definition best describes what they are building?

A. An **AI agent** — an LLM working in a loop with **tools** and a **system prompt** to reach a user goal  
B. A plain chatbot that only generates text from training data with no external actions  
C. A static PDF keyword search with no language model  
D. A spreadsheet macro that cannot call an LLM

**Correct Answer:** A

**Answer Explanation:**  
A is correct because an agent pairs an LLM with tools (search, code runner, etc.) and a prompt inside a reasoning loop.

B is incorrect because a chatbot alone cannot invoke live search or a Python runtime. C is incorrect because PDF search is retrieval, not an agent loop with tools. D is incorrect because spreadsheets do not define the LLM + tools + prompt pattern taught for agents.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A verbose agent log shows lines like `Thought: ...`, `Action: python_repl`, `Observation: 503.41`, and finally `Final Answer: ...`.

What does **ReAct** stand for in this design?

A. **Reasoning + Acting**  
B. **Recursive + Automated**  
C. **Retrieval + Augmentation**  
D. **Reactive + Compiled**

**Correct Answer:** A

**Answer Explanation:**  
A is correct — ReAct alternates reasoning traces with tool actions and observations.

B, C, and D are plausible-sounding acronyms but do not match the Thought → Action → Observation framework used by ReAct agents.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

In a ReAct trace, the line `Observation: SyntaxError: invalid syntax` appears immediately after `Action: python_repl`.

What is the **Observation** in this step?

A. The **raw output** returned from the tool run — including errors — before the manager writes the next **Thought**  
B. The user's original question in English  
C. The LangChain Hub URL for the prompt template  
D. The final polished answer shown to the end user

**Correct Answer:** A

**Answer Explanation:**  
A is correct because Observation is whatever the tool returns (success or error) and the LLM must read it before continuing.

B is incorrect because the user question enters as input, not Observation. C is incorrect because hub URLs are setup metadata, not per-step trace lines. D is incorrect because Final Answer is a separate closing step after enough observations.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

Before adding a Python REPL or Serper search to a LangChain agent, you wrap each callable with `Tool(...)`.

Which three fields are required in that wrapper?

A. **`name`**, **`description`**, **`func`**  
B. **`temperature`**, **`model`**, **`api_key`**  
C. **`chunk_size`**, **`overlap`**, **`embedder`**  
D. **`user`**, **`assistant`**, **`system`**

**Correct Answer:** A

**Answer Explanation:**  
A is correct — the tool schema in beginner form is name (id for Action lines), description (what the manager reads), and func (callable to run).

B is incorrect because those are LLM client settings, not Tool fields. C is incorrect because chunking belongs to document indexing, not tool registration. D is incorrect because those are chat roles, not Tool components.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A developer registers two tools for a ReAct agent:

- `python_repl` — clear description about executing Python commands  
- `serper_search` — description says only *"helps with stuff"*

An analyst asks: *"What is the closing stock price of Nifty today?"*

What is the **most likely** problem?

A. The vague search **description** may cause the manager to pick the wrong worker or skip search entirely  
B. `temperature=0` automatically blocks all Serper calls  
C. `AgentExecutor` ignores descriptions and always picks the first tool in the list  
D. Python REPL cannot print numeric results

**Correct Answer:** A

**Answer Explanation:**  
A is correct — tool descriptions act like worker biodata; vague text hurts correct delegation.

B is incorrect because temperature controls randomness, not tool routing. C is incorrect because the ReAct prompt exposes descriptions for selection. D is incorrect because Python REPL is designed to return printed output as observations.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Meera wires `create_react_agent(...)` and then `AgentExecutor(agent=react_agent, tools=[...])`.

What is the **best** distinction between these two objects?

A. **`create_react_agent`** builds the **reasoning policy** (Thought / Action / Observation format); **`AgentExecutor`** is the **runtime** that runs the loop when you call **`invoke`**  
B. They are duplicate aliases — only one is needed  
C. **`AgentExecutor`** defines tool descriptions; **`create_react_agent`** only prints API keys  
D. **`create_react_agent`** runs Python code; **`AgentExecutor`** only fetches prompts from the hub

**Correct Answer:** A

**Answer Explanation:**  
A is correct — the agent object is the playbook; the executor is the referee that executes steps until a final answer.

B is incorrect because both are required in the standard LangChain pattern. C is incorrect because descriptions are set on `Tool`, not on the executor alone. D is incorrect because both are orchestration layers, not direct replacements for REPL or hub pulls.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A QA engineer reviews a ReAct verbose log before trusting `response["output"]` for a factual stock-price answer.

Which statements about **tool result handling** are **correct**?

A. Every **Observation** should reach the model **before** the next **Thought** for grounded reasoning  
B. A **Final Answer** about live market data is unsafe if no search **Observation** appears in the trace  
C. **`verbose=True`** helps verify that each **Action** is followed by an **Observation**  
D. The manager may skip reading tool output if the **Final Answer** already sounds confident  
E. **`AgentExecutor`** appends observations to the scratchpad automatically during the loop

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the observation-before-next-reasoning rule and debugging practice from the lab.

D is incorrect because skipping tool output defeats grounding — confident text can still be wrong.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

An intern is registering **Python REPL** and **Serper search** tools before building a two-tool ReAct agent.

Which steps are **valid** parts of that setup?

A. Wrap each callable with **`Tool(name=..., description=..., func=...)`**  
B. Pass the **same** `tools=[...]` list to both **`create_react_agent`** and **`AgentExecutor`**  
C. Call **`repl_tool.invoke(...)`** and **`search_tool.invoke(...)`** once to sanity-check before paying for LLM calls  
D. Pass the raw **`PythonREPL`** object directly to **`create_react_agent`** without a **`Tool`** wrapper  
E. Pull **`hub.pull("hwchase17/react")`** to supply the standard Thought / Action / Observation template

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are the taught registration and bind pattern.

D is incorrect because LangChain expects tools to be wrapped with name and description before binding to the agent.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A production agent starts looping on syntax errors, burning API quota during a demo.

Which responses follow **sound loop control and debugging** practice?

A. Set **`max_iterations`** on **`AgentExecutor`** to cap Thought → Action → Observation rounds  
B. Remember that each loop round can consume **many tokens**, raising cost and rate-limit risk  
C. Read the **verbose** trace to see whether the manager picked the wrong tool or sent bad Python syntax  
D. Always show the full **verbose** trace to retail banking customers in the chat UI  
E. If a Groq model hits **rate limits**, switch models or wait before retrying

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E align with max_iterations, token awareness, trace debugging, and rate-limit handling.

D is incorrect because production UIs usually show only the final answer while developers log traces internally.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

An analyst asks a two-tool ReAct agent:

*"What is the latest stock price of Nvidia, and if I had invested $100 a week ago, how much would I have today?"*

Which expectations about the **tool sequence and trace** are **correct**?

A. **`serper_search`** will likely run **before** **`python_repl`** to fetch live or recent price data  
B. **`python_repl` alone** can know today's live Nvidia price without any search observation  
C. The run may require **multiple** Thought → Action → Observation cycles (including retries on bad Python syntax)  
D. The **first Observation** may contain search snippets, not the final investment dollar amount  
E. A trustworthy **Final Answer** can be produced with **zero** tool observations if the LLM memorized prices

**Correct Answers:** A, C, D

**Answer Explanation:**  
A, C, and D match the multi-tool Nvidia demo pattern: search first, several steps possible, intermediate observations differ from the final reply.

B is incorrect because live prices require search (or another live data tool), not REPL alone. E is incorrect because skipping observations means the answer is not grounded in tool results.
