# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)
You are improving a small e-commerce support desk bot. Customers often share an order ID in one message and ask a vague follow-up in the next (*"Where is it now?"*). Your task is to implement a **tool-calling agent with conversational memory** so turn 2 can resolve the order ID without asking again.

### Problem Statement
Build a Python program that:

1. Defines an in-memory `orders_db` with at least:
   - `ORD101` → status `"shipped"`
   - `ORD102` → status `"cancelled"`
2. Implements one tool with `@tool`:
   - `get_order_status(order_id: str) -> str`  
   (return a clear message for valid/invalid IDs)
3. Uses `ChatOllama` from `langchain_ollama` as the chat model (any locally available Ollama model with tool-calling support, for example `llama3.1`).
4. Imports `create_tool_calling_agent` and `AgentExecutor` from `langchain_classic.agents`.
5. Builds a `ChatPromptTemplate` that includes:
   - A system message telling the agent to remember order IDs for follow-ups
   - `MessagesPlaceholder(variable_name="chat_history", optional=True)`
   - Human input placeholder `{input}`
   - `MessagesPlaceholder(variable_name="agent_scratchpad")`
6. Creates a tool-calling agent with `create_tool_calling_agent` and runs it via `AgentExecutor` (`verbose=True` is enough).
7. Maintains a module-level `chat_history = []` list and an `ask_agent(user_input: str) -> str` function that:
   - Calls `agent_executor.invoke` with `input` and `chat_history`
   - Appends `HumanMessage` (user text) then `AIMessage` (final output) **after** each successful run
   - Returns the AI text
8. Runs this **two-turn demo** and prints labeled output:
   - **Turn 1 user:** `Hi, my order ID is ORD102.`
   - **Turn 2 user:** `What is the status of it?`
9. After Turn 2, print `len(chat_history)` (expected: **4** message objects if both turns completed once).

### Expected Outcome
- Turn 1: agent acknowledges or responds about ORD102.
- Turn 2: agent should use context (and ideally the tool) to answer about **ORD102** without the user repeating the ID.
- `len(chat_history)` after turn 2 should be **4** (two human + two AI messages).

### Submission Instruction
- code all the points mentioned in the VS Code in single `.py` file
- run the code and verify its working
- then submit the code in the code editor/answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough
1. Create `orders_db` with ORD101 and ORD102 statuses.
2. Define `get_order_status` with `@tool` and lookup logic.
3. Build prompt with **both** `chat_history` and `agent_scratchpad` placeholders.
4. Create agent + executor (pass `tools` as a **list**).
5. Keep one shared `chat_history` list across turns.
6. In `ask_agent`, invoke with current history, then append human and AI messages in order.
7. Run Turn 1 and Turn 2 queries; print outputs and final `len(chat_history)`.

### Complete Reference Code (Single File)
```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

orders_db = {
    "ORD101": {"status": "shipped"},
    "ORD102": {"status": "cancelled"},
}


@tool
def get_order_status(order_id: str) -> str:
    """Use when the user asks for order status or tracking."""
    order = orders_db.get(order_id)
    if not order:
        return f"Order with ID {order_id} not found."
    return f"Order status for {order_id} is {order['status']}."


tools = [get_order_status]

llm = ChatOllama(model="llama3.1", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful customer support agent. "
        "If the user gives an order ID, remember it for this conversation. "
        "For follow-ups like 'what is the status of it', use the order ID from chat history. "
        "Use tools when order status is required.",
    ),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

chat_history = []


def ask_agent(user_input: str) -> str:
    response = agent_executor.invoke({
        "input": user_input,
        "chat_history": chat_history,
    })
    ai_text = response["output"]
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=ai_text))
    return ai_text


def main() -> None:
    turn1 = "Hi, my order ID is ORD102."
    turn2 = "What is the status of it?"

    print("Turn 1 - User:", turn1)
    print("Turn 1 - AI:", ask_agent(turn1))
    print()

    print("Turn 2 - User:", turn2)
    print("Turn 2 - AI:", ask_agent(turn2))
    print()

    print("chat_history length:", len(chat_history))


if __name__ == "__main__":
    main()
```

### Alternative Valid Approaches
- Add a small `ask_agent_stateless` helper that always passes `chat_history=[]` on turn 2 to demonstrate failure before fixing append logic.
- Wrap the two-turn demo in a `main()` with assertions on `len(chat_history) == 4`.
- Use `max_iterations=3` and `handle_parsing_errors=True` on the executor for safer tool loops.

### Common Mistakes to Avoid
- Defining `MessagesPlaceholder("chat_history")` but never appending messages after `invoke`.
- Appending AI message before human message (wrong order).
- Passing `tool=get_order_status` instead of `tools=[get_order_status]` to the executor.
- Using a different invoke key than the placeholder variable name (e.g., `history` vs `chat_history`).
