# In-Class Quiz — Session 33: Agent Tool Use

**Instructions:** Each question has **one correct option**. Choose the best answer.

================================================================================

## Part 1 — First Half of Notes (Introduction to AI Agents, ReAct, Tools, Python Agent)

### Question 1

Which of the following best describes how an **AI agent** differs from a plain **chatbot**?

A. There is no difference — both mean the same thing  
B. An agent never uses tools; a chatbot always runs Python  
C. A chatbot can search the web and run code; an agent only replies from training data  
D. A chatbot only generates text from memory; an agent can plan, pick a tool, run it, and use the result before answering

**Correct Answer:** D

**Answer Explanation:**  
D is correct — an agent works in a loop with tools (search, Python, etc.), while a chatbot mainly generates text from what it already knows.

A ignores the difference taught in class. B and C reverse or misstate how agents and chatbots behave.

---

### Question 2

What does **ReAct** stand for, and what is the correct order of steps in the loop (before **Final Answer**)?

A. Reasoning + Acting — Thought → Action → Observation  
B. Reading + Acting — Observation → Action → Thought → Final Answer with scratchpad logging at every step  
C. Reacting + Answering — Action → Thought → Final Answer → Observation in a continuous retry loop  
D. Retrieval + Acting — Final Answer → Observation → Thought → Action using only the Serper search tool

**Correct Answer:** A

**Answer Explanation:**  
A is correct — ReAct means Reasoning + Acting, and the agent alternates Thought → Action → Observation until it can give a Final Answer.

B, C, and D use wrong expansions, wrong step order, or extra details that do not match the ReAct paradigm.

================================================================================

## Part 2 — Second Half of Notes (Search Agent, Agent Loop, Debugging, Built-in vs Custom)

### Question 3

In LangChain, what is the difference between **`create_react_agent`** and **`AgentExecutor`**?

A. Both do the same job  
B. `AgentExecutor` builds the reasoning policy and registers tools; `create_react_agent` is only used to pull the ReAct prompt from LangChain Hub and never runs the loop  
C. `create_react_agent` builds the reasoning policy; `AgentExecutor` runs the Thought → Action → Observation loop  
D. `create_react_agent` runs Serper search directly; `AgentExecutor` replaces the need for a Groq API key and writes all observations to a JSON history file automatically

**Correct Answer:** C

**Answer Explanation:**  
C is correct — the agent is the playbook (policy); the executor is the runtime that runs each step until a final answer.

A treats them as identical. B swaps their roles and adds incorrect duties. D mixes in unrelated setup steps.

---

### Question 4

When building or testing a ReAct agent in the notebook, why should you use **`verbose=True`**, and what does **`max_iterations`** do?

A. `verbose=True` hides tool steps from the notebook; `max_iterations` sets the LLM temperature to zero for every Groq model call in the agent loop  
B. `verbose=True` prints Thought / Action / Observation for debugging; `max_iterations` caps how many loop rounds can run  
C. `verbose=True` saves chat history to JSON  
D. `verbose=True` removes API keys

**Correct Answer:** B

**Answer Explanation:**  
B is correct — verbose traces help you see how the agent reasoned and which tools ran; `max_iterations` is a hard stop on loop rounds (same idea as `MAX_STEPS` in the memory lab).

A describes the opposite of verbose and misstates `max_iterations`. C and D are too short and do not match what these settings actually do.

================================================================================

## Answer Key (quick)

| Q# | Part | Answer |
|---|---|---|
| 1 | First half — AI agent vs chatbot | D |
| 2 | First half — ReAct paradigm | A |
| 3 | Second half — Agent vs Executor | C |
| 4 | Second half — Verbose & loop control | B |
