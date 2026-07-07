# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy -> Moderate -> Hard

Question Types:
- 6 MCQ (Single Correct): Q1-Q6
- 4 MSQ (Multiple Correct): Q7-Q10

---

## Q1 (MCQ, Easy)
You are building a tool-calling chatbot. Which component is responsible for running the agent loop, calling tools, and returning the final response?

A. `ChatPromptTemplate`  
B. `AgentExecutor`  
C. `MessagesPlaceholder`  
D. `@tool`

**Correct Answer:** B

**Answer Explanation:**  
`AgentExecutor` is the runtime layer that executes the agent, invokes tools, and manages the loop until a final answer is produced.

**Why other options are wrong:**  
- A: `ChatPromptTemplate` defines prompt structure only.  
- C: `MessagesPlaceholder` stores interim messages in prompt flow.  
- D: `@tool` registers functions as tools; it does not run loops.

---

## Q2 (MCQ, Easy)
What is the main purpose of setting `max_iterations` in an agent executor?

A. To increase model creativity  
B. To limit repeated agent action loops  
C. To force tool usage in every query  
D. To hide intermediate steps

**Correct Answer:** B

**Answer Explanation:**  
`max_iterations` puts an upper bound on action loops, preventing runaway retries or infinite loops.

**Why other options are wrong:**  
- A: Creativity is controlled by model temperature, not iteration caps.  
- C: It does not force tool usage.  
- D: It does not control trace visibility.

---

## Q3 (MCQ, Easy)
What does `return_intermediate_steps=True` help you do?

A. Encrypt tool outputs  
B. Disable tool calls  
C. Inspect which tools were called and what they returned  
D. Improve internet speed for API calls

**Correct Answer:** C

**Answer Explanation:**  
This setting returns action-observation traces so you can debug tool selection and behavior.

**Why other options are wrong:**  
- A: No encryption behavior is provided by this flag.  
- B: It does not disable tools.  
- D: It has nothing to do with network performance.

---

## Q4 (MCQ, Easy)
What is the primary role of `create_tool_calling_agent` in a LangChain agent setup?

A. It builds the decision layer that chooses when and which tools to call  
B. It permanently stores all user chat history across sessions  
C. It downloads Ollama models automatically  
D. It replaces the need for any prompt template

**Correct Answer:** A

**Answer Explanation:**  
`create_tool_calling_agent` wires the LLM, tools, and prompt into an agent that can reason about tool use. The executor then runs that agent.

**Why other options are wrong:**  
- B: Persistent memory is a separate concern; this function does not store history.  
- C: Model download is handled by Ollama CLI, not this function.  
- D: A prompt template is still required when creating the agent.

---

## Q5 (MCQ, Moderate)
Your agent occasionally returns malformed structured outputs from the model and crashes during parsing. Which executor configuration directly improves resilience in this case?

A. `verbose=True`  
B. `return_intermediate_steps=True`  
C. `handle_parsing_errors=True`  
D. `max_iterations=1`

**Correct Answer:** C

**Answer Explanation:**  
`handle_parsing_errors=True` allows safer recovery from parse issues instead of immediate hard failure.

**Why other options are wrong:**  
- A: Verbose mode only prints logs.  
- B: This helps observation, not recovery.  
- D: Lowering iterations may reduce loops but does not solve parse handling.

---

## Q6 (MCQ, Moderate)
A user asks: "Tell me order status, ETA, and refund for ORD102." Which behavior best indicates a correctly functioning tool-calling agent?

A. It always responds without tools to save cost  
B. It calls exactly one random tool and fabricates the rest  
C. It calls relevant tools, aggregates observations, then returns one final user-friendly response  
D. It asks the user to provide source code before answering

**Correct Answer:** C

**Answer Explanation:**  
A proper agent decides required tools, executes them, uses tool outputs, and synthesizes a final response.

**Why other options are wrong:**  
- A: Avoiding tools can lead to incorrect or fabricated answers.  
- B: Random single-tool behavior is unreliable.  
- D: Source code is not required for this use case.

---

## Q7 (MSQ, Moderate)
Which settings directly contribute to safer and debuggable runtime behavior in a production-style tool-calling workflow?

A. `max_iterations`  
B. `handle_parsing_errors`  
C. `return_intermediate_steps`  
D. `temperature=1.5`

**Correct Answers:** A, B, C

**Answer Explanation:**  
- `max_iterations` prevents runaway loops.  
- `handle_parsing_errors` improves fault tolerance.  
- `return_intermediate_steps` enables traceability and debugging.

**Why option D is wrong:**  
High temperature increases randomness; it is not a core safety or debug control.

---

## Q8 (MSQ, Moderate)
You are validating an agent with a test pack. Which checks should be included to assess decision-path quality (not just final text quality)?

A. Compare expected tools vs actual tools used in intermediate steps  
B. Ensure at least one test where no tool should be called  
C. Ignore tool inputs because outputs are enough  
D. Include a case with missing or invalid order ID

**Correct Answers:** A, B, D

**Answer Explanation:**  
Decision-path validation requires checking tool-routing correctness, including no-tool and invalid-input scenarios.

**Why option C is wrong:**  
Tool inputs are crucial to catch argument-level mistakes.

---

## Q9 (MSQ, Hard)
You notice an agent repeatedly retries tool calls with no progress and eventually times out. Which interventions are valid and aligned with robust design?

A. Lower or cap `max_iterations`  
B. Add fallback messaging for repeated failures  
C. Remove all tool descriptions to reduce prompt length  
D. Use intermediate-step logs to identify failure stage

**Correct Answers:** A, B, D

**Answer Explanation:**  
Runaway behavior is addressed by iteration limits, robust fallback behavior, and observability for root-cause analysis.

**Why option C is wrong:**  
Removing tool descriptions usually worsens tool selection quality.

---

## Q10 (MSQ, Hard)
For multi-step agent behavior, which statements about the scratchpad (`MessagesPlaceholder`) are correct?

A. It helps preserve current-run reasoning and tool traces across steps  
B. It is useful for tool chaining in a single invocation  
C. It permanently stores all user history across sessions by default  
D. Without it, multi-step context handling can degrade

**Correct Answers:** A, B, D

**Answer Explanation:**  
Scratchpad is temporary working memory for the current run and supports coherent multi-step action flow.

**Why option C is wrong:**  
Persistent cross-session memory is not provided by scratchpad alone.
