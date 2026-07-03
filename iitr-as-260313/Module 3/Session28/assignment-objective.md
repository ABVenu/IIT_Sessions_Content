# Objective Assignment: LangChain Tools — Custom Tools and Tool Calling

## Multiple Choice Questions (Single Correct)

### Q1. Easy

An online course platform receives this parent message: *"The course fee is ₹40,000 and we have a 15% discount. What is the exact amount to pay?"* The product team wants reliable fee answers that follow the company's discount rules every time. Why should the app expose a `calculate_final_fee` tool instead of letting the LLM calculate from memory alone?

A. A tool applies exact business rules in code; the LLM may guess or round incorrectly  
B. The LLM cannot read Python function names  
C. Tools remove the need for any chat model in the application  
D. The `@tool` decorator automatically transfers money to the bank  

**Correct Answer:** A

**Answer Explanation:**  
Fee calculation with fixed rules is safer through a Python tool that runs deterministic logic. The LLM is strong at language but should not be blindly trusted for exact arithmetic or policy. Option B is unrelated to the business need. Option C is wrong because tools work *with* the model, not instead of it. Option D describes behaviour that `@tool` does not provide.

---

### Q2. Easy

Ravi has a plain Python function that checks whether a learner has a laptop and enough weekly study hours. He adds `@tool` above the function definition. What is the main purpose of that decorator?

A. It wraps the function so LangChain can expose its name, description, and input schema to the model  
B. It runs the function automatically every time the Python file is saved  
C. It converts the function into a downloadable Ollama model  
D. It hides the function docstring from the model for security  

**Correct Answer:** A

**Answer Explanation:**  
`@tool` registers a Python function as a LangChain-compatible tool by reading its name, docstring, type hints, and return type. It does not auto-run on save (B), download models (C), or hide docstrings — docstrings actually help the model choose the tool (D).

---

### Q3. Easy

After defining a list of tools, a developer writes:

```python
model_with_tools = model.bind_tools(tools)
```

What happens at this step?

A. The model becomes aware of the available tools; no tool is executed yet  
B. Every tool runs once immediately with empty arguments  
C. The model converts all tools into `ToolMessage` objects automatically  
D. `tool_calls` are replaced by the final polished answer  

**Correct Answer:** A

**Answer Explanation:**  
`bind_tools` attaches the tool menu to the model for upcoming invocations. Execution happens only when your application reads `tool_calls` and invokes the matching function. Options B, C, and D describe steps that occur later in the loop or not at all.

---

### Q4. Easy

In the restaurant analogy used for tool calling, the customer gives an order, the waiter writes a slip, and the kitchen prepares the food. In software terms, who actually runs the Python tool function?

A. Your Python application  
B. The LLM inside the model weights  
C. The `HumanMessage` class before the model replies  
D. The user's browser without any backend code  

**Correct Answer:** A

**Answer Explanation:**  
The model only emits a structured request (`tool_calls`). Your application is responsible for executing the matching Python function and returning the result. The LLM does not directly run arbitrary Python (B). `HumanMessage` carries the user query (C). The browser does not execute backend tools by itself (D).

---

### Q5. Moderate

During a manual tool loop, the model returns an `AIMessage` with a non-empty `tool_calls` list. What must the developer do before asking the model for the final user-facing answer?

A. Run each requested tool, wrap results in `ToolMessage` with matching `tool_call_id`, append them to `messages`, and invoke the model again  
B. Delete the `AIMessage` from history and restart the conversation from scratch  
C. Return `tool_calls` directly to the user without executing any function  
D. Call `bind_tools` again after every individual tool execution  

**Correct Answer:** A

**Answer Explanation:**  
The manual loop pattern is: model request → execute tools → send `ToolMessage` results back → model produces a final natural-language answer. Deleting history (B) loses context. Returning raw `tool_calls` (C) skips execution. Re-binding tools after every call (D) is unnecessary; bind once, then loop over messages.

---

### Q6. Moderate

A developer inspects this model-emitted tool call during debugging:

```python
{
    "name": "calculate_final_fee",
    "args": {
        "fee": 50000,
        "discount": "twenty"
    },
    "id": "call_123",
    "type": "tool_call"
}
```

The function signature expects `base_fee: int` and `discount_percent: int`. What are the main faults?

A. Wrong argument names and a string used where a numeric discount percentage is expected  
B. The `id` field must always be omitted for fee tools  
C. The tool `name` should be `ToolMessage` instead of `calculate_final_fee`  
D. The `type` field must be `"human_message"` for all calculator tools  

**Correct Answer:** A

**Answer Explanation:**  
The model passed `fee` and `discount` instead of `base_fee` and `discount_percent`, and used the string `"twenty"` instead of an integer like `20`. The `id` field is required to link results back (B is wrong). `ToolMessage` is for returning results, not naming tools (C). `type` identifies a tool call request, not a human message (D).

---

## Multiple Select Questions (Multiple Correct)

### Q7. Moderate

When you decorate a Python function with `@tool`, which pieces of information does LangChain typically expose to the model?

A. The function name  
B. The docstring as the tool description  
C. Argument names and type hints from the function signature  
D. The developer's private `.env` file contents  

**Correct Answers:** A, B, C

**Answer Explanation:**  
`@tool` reads the callable's name, docstring, typed parameters, and return information to build a structured tool definition. Environment secrets are never auto-exposed through `@tool`, so option D must not be selected.

---

### Q8. Moderate

An intern is building tools for a learner support chatbot. Which choices follow good tool design practices?

A. Use a clear name like `get_ticket_status` instead of `process_data`  
B. Add type hints such as `int`, `bool`, and `str` on tool arguments  
C. Write a docstring that explains when the model should call the tool  
D. Combine fee calculation, email sending, and ticket lookup inside one large `@tool` function  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Clear names, type hints, and specific docstrings help reliable model-driven tool selection. One tool should do one clear job; a giant mixed tool (D) makes selection and debugging harder.

---

### Q9. Hard

A developer implements a manual tool-feedback loop using `HumanMessage`, `bind_tools`, and a `tool_map` dictionary. Which statements about the flow are correct?

A. `HumanMessage` stores the user's query in LangChain message format  
B. The model returns an `AIMessage` that may contain `tool_calls`, but Python still executes the actual tool functions  
C. `tool_map[tool_call["name"]]` helps locate the correct callable tool by name  
D. `bind_tools` executes every registered tool before the first `invoke` finishes  

**Correct Answers:** A, B, C

**Answer Explanation:**  
The loop starts with a human message, the model requests tools via `AIMessage.tool_calls`, and the app maps names to functions through `tool_map`. `bind_tools` only registers availability; it does not execute tools upfront, so D is incorrect.

---

### Q10. Hard

After running a controlled query set, Meera notices that a fee-related question returns empty `tool_calls` when using a small local model at `temperature=0.8`. Her `@tool` definitions look correct. Which debugging actions align with reliable tool-calling practice?

A. Re-run the same queries with a lower temperature such as `0` or `0.3`  
B. Try a model that supports tool calling more reliably, such as `llama3.1` if available locally  
C. Print `response.tool_calls` for each test query before assuming the Python tool code is wrong  
D. Remove all docstrings because they always prevent tool calling  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Temperature and model choice strongly affect whether structured `tool_calls` appear. A controlled query set with printed traces helps separate model behaviour from code bugs. Docstrings help tool selection; removing them (D) would make behaviour worse, not better.
