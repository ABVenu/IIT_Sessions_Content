# Assignment — Objective (Session: LangChain Tools — Custom Tools and Tool Calling)

**Instructions:** Answer all questions. **MCQ** = exactly one correct option. **MSQ** = select *all* options that apply; partial marking may apply per platform rules.

---

## Section A — Easy (MCQ)

### Q1 (MCQ — Easy)

A food-delivery startup ships a chatbot that must tell customers the **live** location of their order using data from the company’s tracking API. The team uses only a plain LLM with no tools connected. What is the **most likely** problem in production?

- A) The model will always refuse to answer politely  
- B) The model may **guess** order status instead of reading real tracking data  
- C) The API automatically runs inside the model weights during inference  
- D) Tool calling is only for image generation, not text chatbots  

---

### Q2 (MCQ — Easy)

In a LangChain support app, a Python function `get_order_status(order_id: str)` is registered so the model can request it. Which decorator is used to expose that function as a LangChain tool?

- A) `@chain`  
- B) `@tool`  
- C) `@parser`  
- D) `@bind`  

---

### Q3 (MCQ — Easy)

During the tool-calling loop, the model emits a structured `tool_calls` entry with a name and arguments. **Who actually runs** the Python function or API behind that tool?

- A) The LLM runtime inside the GPU  
- B) LangChain automatically without your code  
- C) **Your application code** (for example `tool.invoke(args)` in a handler you wrote)  
- D) The end user’s browser only  

---

### Q4 (MCQ — Easy)

After your app runs a tool, you append a message so the model can write a friendly final reply. Which message type carries the tool’s output and links back to the model’s request using `tool_call_id`?

- A) `HumanMessage`  
- B) `ToolMessage`  
- C) `SystemMessage` only  
- D) `StrOutputParser`  

---

## Section B — Moderate (MCQ)

### Q5 (MCQ — Moderate)

A developer calls `model_with_tools = model.bind_tools(tools)` before invoking the chat model. What does `bind_tools` accomplish?

- A) It attaches tool definitions to the model so replies **may include** structured `tool_calls`  
- B) It downloads all Ollama models into the project folder  
- C) It replaces the need for a system prompt  
- D) It executes every tool automatically on every user message  

---

### Q6 (MCQ — Moderate)

A customer-support agent already received JSON from `get_order_status` via a tool. The developer invokes the model **one more time** with that result in the message history. Why is this second model call useful?

- A) To re-run the same tool in an infinite loop  
- B) To turn raw tool output into a **consistent, user-friendly** natural-language answer  
- C) Because `ToolMessage` cannot be stored in conversation history  
- D) Because tools always return empty strings  

---

## Section C — Moderate (MSQ)

### Q7 (MSQ — Moderate)

A team adds Pydantic `args_schema` to `@tool` for `lookup_policy`, with `topic: Literal["refund", "shipping", "warranty"]`. Which statements are correct?

- A) Invalid `topic` values can fail validation **before** the tool’s business logic runs  
- B) `Field(description=...)` helps document arguments for both developers and the model’s schema  
- C) `Literal[...]` restricts a field to a fixed set of allowed string values  
- D) Pydantic replaces the need for your app to call `tool.invoke` — the model runs Python directly  

---

### Q8 (MSQ — Moderate)

In `execute_tool_call_safely`, the class pattern wraps `selected_tool.invoke(tool_args)` in `try/except` and returns `ToolMessage` on failure. Which practices match **safe tool execution**?

- A) Catch exceptions and return structured error content in a `ToolMessage` instead of crashing the app  
- B) Build a `tools_by_name` dictionary so each `tool_call["name"]` maps to the right tool object  
- C) If the model requests an unknown tool name, return an error payload (for example `error_type: unknown_tool`)  
- D) Let uncaught exceptions bubble up and terminate the whole web server on every bad argument  

---

## Section D — Hard (MSQ)

### Q9 (MSQ — Hard)

In testing, the model answers “Your order ORD1001 shipped yesterday” **without** calling `get_order_status`, even though live order data exists only in your database. Which fixes align with good tool-calling design?

- A) Clarify in the **system prompt** that live order/policy/refund data must come from tools, not guesses  
- B) Improve each tool’s **name** and **docstring** so the model can choose the right capability  
- C) Print or log `tool_calls` each step to compare expected vs actual tool use  
- D) Remove `bind_tools` so the model is forced to invent data faster  

---

### Q10 (MSQ — Hard)

Consider a manual agent loop like `run_customer_support_agent(user_query, max_steps=5)` that calls `model_with_tools.invoke(messages)` repeatedly. Which statements about this loop are correct?

- A) Each turn’s `AIMessage` should be **appended** to `messages` before deciding the next step  
- B) If `tool_calls` is empty, the model’s `content` can be treated as the **final** answer to return  
- C) `max_steps` is a safety cap so the agent cannot loop forever on complex queries  
- D) The LLM itself executes `get_order_status` inside the model weights without your Python code  

---

## Answer Explanations (for Assess platform — paste per item)

### Q1 — Correct: **B**

**Reasoning:** An LLM without tools only has training knowledge and text generation. It cannot reliably read a live order-tracking API, so it may hallucinate status instead of using real data.

**Why others are wrong:** A) The model may still answer confidently but incorrectly. C) External APIs are not inside model weights. D) Tool calling is central to text agents that need live data.

---

### Q2 — Correct: **B**

**Reasoning:** The `@tool` decorator from `langchain.tools` registers a Python function as a LangChain tool with metadata (name, description, schema) exposed to the model.

**Why others are wrong:** A) `@chain` is not the standard tool registration decorator taught here. C) Parsers format output; they do not register callable tools. D) `bind_tools` is a model method, not a function decorator.

---

### Q3 — Correct: **C**

**Reasoning:** The model only **requests** tools via structured `tool_calls`. Your application must invoke the tool and pass results back—typically with `tool.invoke(args)` inside your handler.

**Why others are wrong:** A) The LLM does not run your database code internally. B) Execution still requires explicit application logic you control. D) The browser is not the standard execution layer for backend tools in this pattern.

---

### Q4 — Correct: **B**

**Reasoning:** `ToolMessage` carries one tool’s output back into chat history and is linked to the originating request through `tool_call_id`.

**Why others are wrong:** A) `HumanMessage` represents user input, not tool results. C) System messages set behavior; they are not the tool result channel. D) `StrOutputParser` converts model output format; it is not a chat message type for tool results.

---

### Q5 — Correct: **A**

**Reasoning:** `bind_tools(tools)` attaches the list of tool definitions to the chat model so its responses may include structured `tool_calls` the app can execute.

**Why others are wrong:** B) Model downloading is unrelated to `bind_tools`. C) System prompts remain important for correct tool use. D) Tools are not auto-executed on every message—the app runs them when `tool_calls` appear.

---

### Q6 — Correct: **B**

**Reasoning:** Tools return data in shapes like JSON strings. A follow-up model turn turns that into one polite, consistent reply for the UI instead of dumping raw payloads on users.

**Why others are wrong:** A) The goal is not an infinite re-run of the same tool. C) `ToolMessage` is designed to be appended to history. D) Well-designed tools return structured content, not empty strings by default.

---

### Q7 — Correct: **A, B, C**

**Reasoning:** Pydantic validates inputs early, `Field` descriptions document the schema for humans and the model, and `Literal` enforces allowed enum-like string choices such as policy topics.

**Why others are wrong:** D) The application still executes tools; Pydantic validates arguments—it does not run Python on the model’s behalf.

---

### Q8 — Correct: **A, B, C**

**Reasoning:** Safe execution catches failures, maps tool names to callables, and returns recoverable error signals (including unknown tools) as `ToolMessage` content.

**Why others are wrong:** D) Uncaught exceptions would crash the agent flow instead of letting the model explain the error to the user.

---

### Q9 — Correct: **A, B, C**

**Reasoning:** Wrong tool selection is reduced with clear system instructions, precise tool names/descriptions, and step-by-step tracing of `tool_calls`.

**Why others are wrong:** D) Removing `bind_tools` removes structured tool access and encourages more guessing, not less.

---

### Q10 — Correct: **A, B, C**

**Reasoning:** The manual loop appends each `AIMessage`, exits when there are no `tool_calls`, and uses `max_steps` as a bounded safety limit for multi-tool conversations.

**Why others are wrong:** D) Tool execution remains application-side; the LLM only plans and requests tools.

---

**End of objective assignment**
