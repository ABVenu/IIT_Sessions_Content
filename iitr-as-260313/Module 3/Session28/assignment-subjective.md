# Subjective Assignment: Build a Learner Support Tool-Calling Assistant

## Practical Task (Medium)

A night-shift learner support desk for an online coding bootcamp wants a small Python assistant that can answer structured questions about fees, eligibility, and ticket status using LangChain tool calling. Your task is to build a **single-file** program that registers custom tools, binds them to a local chat model, and completes one manual tool-feedback loop.

### Scenario

A learner sends this message to the support bot:

*"I have a laptop and can study 12 hours every week. Please also calculate my final fee after a 10% discount on ₹45,000."*

The bot should let the model decide which tools to call, execute those tools in Python, return results through `ToolMessage`, and then produce one final natural-language reply.

### Requirements

Write a Python program named `learner_support_agent.py` that:

1. Imports `ChatOllama` from `langchain_ollama`, `tool` from `langchain_core.tools`, and `HumanMessage`, `ToolMessage` from `langchain_core.messages`.
2. Defines these three `@tool` functions with the exact logic below:
   - **`calculate_final_fee(base_fee: int, discount_percent: int) -> int`**  
     Docstring: *"Calculate the final course fee after applying a discount percentage."*  
     Logic: `discount_amount = base_fee * discount_percent // 100`, return `base_fee - discount_amount`.
   - **`check_course_eligibility(has_laptop: bool, weekly_hours: int) -> str`**  
     Docstring: *"Check if a learner is eligible for a coding-heavy online course."*  
     Logic: if no laptop → `"Not eligible yet: a laptop is required for hands-on practice."`; elif `weekly_hours < 10` → `"Not eligible yet: at least 10 hours per week are needed."`; else → `"Eligible: the learner has the basic setup and time commitment."`
   - **`get_ticket_status(ticket_id: str) -> str`**  
     Docstring: *"Get the current status of a learner support ticket by ticket ID."*  
     Use this in-memory dictionary:
     ```python
     {
         "T101": "Open: waiting for mentor review.",
         "T102": "Resolved: refund confirmation sent.",
         "T103": "In progress: technical team is checking the issue.",
     }
     ```
     Return `"Ticket not found."` when the ID is missing.
3. Stores all three tools in a list named `tools`.
4. Builds `tool_map = {current_tool.name: current_tool for current_tool in tools}`.
5. Creates `model = ChatOllama(model="llama3.1", temperature=0.3)`.  
   If `llama3.1` is not available on your machine, replace the model string with any tool-capable model from `ollama list` (for example `qwen2.5:0.5b`) and mention the model name in a comment at the top of the file.
6. Creates `model_with_tools = model.bind_tools(tools)`.
7. Starts the conversation with exactly this user message wrapped as a `HumanMessage`:

```python
messages = [
    HumanMessage(
        content=(
            "I have a laptop and can study 12 hours every week. "
            "Please also calculate my final fee after a 10% discount on 45000 rupees."
        )
    )
]
```

8. Calls `first_response = model_with_tools.invoke(messages)` and appends `first_response` to `messages`.
9. Loops through every item in `first_response.tool_calls`:
   - finds the tool using `tool_map`
   - runs `selected_tool.invoke(tool_call["args"])`
   - appends a `ToolMessage(content=str(tool_result), tool_call_id=tool_call["id"])` to `messages`
10. Calls `final_response = model_with_tools.invoke(messages)`.
11. Prints:
    - a heading `FIRST TOOL CALLS:` followed by `first_response.tool_calls`
    - a heading `FINAL ANSWER:` followed by `final_response.content`

### Example Output Shape

Exact tool-call count and final wording may vary by model, but your program output should look similar to this:

```text
FIRST TOOL CALLS:
[{'name': 'check_course_eligibility', 'args': {'has_laptop': True, 'weekly_hours': 12}, 'id': '...', 'type': 'tool_call'},
 {'name': 'calculate_final_fee', 'args': {'base_fee': 45000, 'discount_percent': 10}, 'id': '...', 'type': 'tool_call'}]
FINAL ANSWER:
You are eligible for the course. After a 10% discount on ₹45,000, your final fee is ₹40,500.
```

### Constraints

- Use a **single** Python file named `learner_support_agent.py`.
- Use only the LangChain tool-calling pieces listed in the requirements.
- Do not use agents, retrievers, vector databases, or memory modules.
- Ollama must be installed and running locally.
- Install required packages inside your activated virtual environment:

```bash
pip install langchain-core langchain-ollama
```

- Pull a compatible model if needed, for example:

```bash
ollama pull llama3.1
```

### Submission Instruction

1. Code all the points mentioned above in VS Code in a single `.py` file named `learner_support_agent.py`.
2. Run the code and verify that it is working.
3. Submit the complete code in the code editor/answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

The program mirrors the manual tool-feedback loop from the lesson: register focused `@tool` helpers, bind them with `bind_tools`, let the model emit structured `tool_calls`, execute matching Python functions, return `ToolMessage` objects linked by `tool_call_id`, and invoke the model again for a polished answer.

The combined learner message should trigger **multiple** tool calls — eligibility check and fee calculation — which tests the `for tool_call in first_response.tool_calls` loop. Printing `first_response.tool_calls` before the final answer supports debugging, just like a controlled query set.

### Complete Code

```python
from langchain_ollama import ChatOllama  # Local chat model integration
from langchain_core.tools import tool  # Decorator that registers Python functions as tools
from langchain_core.messages import HumanMessage, ToolMessage  # Conversation message types


@tool  # Expose this function as a LangChain tool
def calculate_final_fee(base_fee: int, discount_percent: int) -> int:
    """Calculate the final course fee after applying a discount percentage."""
    discount_amount = base_fee * discount_percent // 100  # Integer discount amount
    final_fee = base_fee - discount_amount  # Payable fee after discount
    return final_fee  # Return exact fee for ToolMessage


@tool  # Expose eligibility checker as a tool
def check_course_eligibility(has_laptop: bool, weekly_hours: int) -> str:
    """Check if a learner is eligible for a coding-heavy online course."""
    if not has_laptop:  # Laptop is required for hands-on practice
        return "Not eligible yet: a laptop is required for hands-on practice."
    if weekly_hours < 10:  # Minimum weekly study time rule
        return "Not eligible yet: at least 10 hours per week are needed."
    return "Eligible: the learner has the basic setup and time commitment."


@tool  # Expose ticket lookup as a tool
def get_ticket_status(ticket_id: str) -> str:
    """Get the current status of a learner support ticket by ticket ID."""
    ticket_database = {  # Simulated support ticket store
        "T101": "Open: waiting for mentor review.",
        "T102": "Resolved: refund confirmation sent.",
        "T103": "In progress: technical team is checking the issue.",
    }
    return ticket_database.get(ticket_id, "Ticket not found.")  # Safe fallback


tools = [calculate_final_fee, check_course_eligibility, get_ticket_status]  # All registered tools
tool_map = {current_tool.name: current_tool for current_tool in tools}  # Name → callable lookup

# Use any tool-capable model available in `ollama list`
model = ChatOllama(model="llama3.1", temperature=0.3)  # Slightly stable but not fully random
model_with_tools = model.bind_tools(tools)  # Attach tool menu to the model

messages = [  # Start conversation with the learner support query
    HumanMessage(
        content=(
            "I have a laptop and can study 12 hours every week. "
            "Please also calculate my final fee after a 10% discount on 45000 rupees."
        )
    )
]

first_response = model_with_tools.invoke(messages)  # Model decides which tools to request
messages.append(first_response)  # Keep AI message in history

for tool_call in first_response.tool_calls:  # Handle zero, one, or many tool calls
    selected_tool = tool_map[tool_call["name"]]  # Resolve tool by model-provided name
    tool_result = selected_tool.invoke(tool_call["args"])  # Run Python business logic
    tool_message = ToolMessage(
        content=str(tool_result),  # Model reads tool output as text
        tool_call_id=tool_call["id"],  # Must match the originating tool call
    )
    messages.append(tool_message)  # Add tool result to conversation history

final_response = model_with_tools.invoke(messages)  # Model writes final user-facing answer

print("FIRST TOOL CALLS:")  # Debug trace — what the model requested
print(first_response.tool_calls)
print("FINAL ANSWER:")  # Polished reply after tools ran
print(final_response.content)
```

### Alternative Approaches

- You may wrap the invoke → tool loop → final invoke steps in a small function such as `run_support_turn(user_text)` for readability; behaviour should stay the same.
- If the model returns only one tool call on the first run, your loop still works because it iterates over whatever is present in `first_response.tool_calls`.
- For more stable traces during grading, set `temperature=0` or switch to a stronger local model — the assignment focuses on correct loop structure, not perfect model behaviour every time.
