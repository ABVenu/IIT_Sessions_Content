# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)
You are building a mini support assistant for an online store. Implement a Python program that uses a tool-calling agent runtime to handle user support queries for order operations.

### Problem Statement
Create an assistant that can:
1. Fetch order status for an order ID.
2. Estimate delivery timeline for an order ID.
3. Provide refund-related response based on order status.

The program must:
- Define an in-memory `orders_db` with at least 3 orders covering `shipped`, `cancelled`, and `delivered`.
- Create 3 tools using `@tool`:  
  - `get_order_status(order_id: str) -> str`  
  - `estimate_delivery_timeline(order_id: str) -> str`  
  - `calculate_refund_amount(order_id: str) -> str`
- Build an agent using `create_tool_calling_agent`.
- Execute it using `AgentExecutor` with:
  - `max_iterations=3`
  - `handle_parsing_errors=True`
  - `return_intermediate_steps=True`
- Run at least 4 test queries:
  1. Single-tool query
  2. Multi-tool query
  3. No-tool query
  4. Invalid order ID query
- Print:
  - Final output
  - Intermediate steps (tool selected, tool input, tool observation)

### Expected Outcome
Your output should demonstrate:
- Correct tool routing for each test case
- Stable handling of invalid IDs or unsupported requests
- Clear traceability through intermediate steps

### Submission Instruction
- code all the points mentioned in the VS Code in single `.py` file
- run the code and verify its working
- then submit the code in the code editor/answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough
1. Create a mock `orders_db` with shipped, cancelled, and delivered samples.
2. Define three tools with `@tool` and clear response logic for valid and invalid order IDs.
3. Build prompt with:
   - system instruction,
   - human input placeholder,
   - `MessagesPlaceholder("agent_scratchpad")` for step memory.
4. Create the tool-calling agent using `create_tool_calling_agent`.
5. Wrap it in `AgentExecutor` with safe runtime settings.
6. Run four test cases (single-tool, multi-tool, no-tool, invalid-ID).
7. Print final output and each intermediate step (tool, input, observation).
8. Validate expected tools against actual tools for each test case.

### Complete Reference Code (Single File)
```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent


# Mock in-memory order data
orders_db = {
    "ORD101": {"status": "shipped", "city": "Delhi", "amount": 2500, "delivery_days": 2},
    "ORD102": {"status": "cancelled", "city": "Bangalore", "amount": 1800, "delivery_days": 0},
    "ORD103": {"status": "delivered", "city": "Mumbai", "amount": 3200, "delivery_days": 0},
}


@tool
def get_order_status(order_id: str) -> str:
    """Get the current status for a given order ID."""
    order = orders_db.get(order_id)
    if not order:
        return f"No order found for order ID {order_id}."
    return (
        f"Order {order_id} is {order['status']} in {order['city']}. "
        f"Order amount is {order['amount']}."
    )


@tool
def estimate_delivery_timeline(order_id: str) -> str:
    """Estimate delivery timeline for a given order ID."""
    order = orders_db.get(order_id)
    if not order:
        return f"No order found for order ID {order_id}."

    status = order["status"]
    if status == "shipped":
        return f"Order {order_id} is shipped and expected in {order['delivery_days']} days."
    if status == "delivered":
        return f"Order {order_id} has already been delivered."
    if status == "cancelled":
        return f"Order {order_id} is cancelled, so no delivery timeline exists."
    return f"Delivery timeline for order {order_id} is currently unavailable."


@tool
def calculate_refund_amount(order_id: str) -> str:
    """Return refund-related response for a given order ID."""
    order = orders_db.get(order_id)
    if not order:
        return f"No order found for order ID {order_id}."

    status = order["status"]
    if status == "cancelled":
        return f"Refund amount for order {order_id} is {order['amount']}."
    if status == "delivered":
        return (
            f"Order {order_id} is delivered. Refund eligibility depends on return policy "
            f"and product category."
        )
    if status == "shipped":
        return (
            f"Order {order_id} is shipped. Refund cannot be finalized until cancellation "
            f"or return is initiated."
        )
    return f"Refund details for order {order_id} are currently unavailable."


def print_trace(result: dict) -> None:
    """Print final output and intermediate tool traces."""
    print("Final Output:")
    print(result["output"])
    print("\nIntermediate Steps:")
    for idx, (action, observation) in enumerate(result["intermediate_steps"], start=1):
        print(f"\nStep {idx}")
        print("Tool Selected:", action.tool)
        print("Tool Input:", action.tool_input)
        print("Tool Observation:", observation)


def main() -> None:
    tools = [get_order_status, estimate_delivery_timeline, calculate_refund_amount]

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an e-commerce support assistant. Use tools whenever required "
                "to provide accurate responses.",
            ),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=3,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
    )

    test_cases = [
        {
            "name": "Single-tool query",
            "query": "What is the status of order ORD101?",
            "expected_tools": {"get_order_status"},
        },
        {
            "name": "Multi-tool query",
            "query": "For ORD102, check status, delivery timeline, and refund details.",
            "expected_tools": {
                "get_order_status",
                "estimate_delivery_timeline",
                "calculate_refund_amount",
            },
        },
        {
            "name": "No-tool query",
            "query": "Can you suggest a good weekend movie?",
            "expected_tools": set(),
        },
        {
            "name": "Invalid order ID query",
            "query": "Get status and refund info for order ORD999.",
            "expected_tools": {"get_order_status", "calculate_refund_amount"},
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        print("\n" + "=" * 80)
        print(f"Test Case {i}: {case['name']}")
        print("Query:", case["query"])
        print("=" * 80)

        result = agent_executor.invoke({"input": case["query"]})
        print_trace(result)

        actual_tools = {action.tool for action, _ in result["intermediate_steps"]}
        print("\nValidation")
        print("Expected Tools:", sorted(case["expected_tools"]))
        print("Actual Tools  :", sorted(actual_tools))
        print("Match         :", case["expected_tools"].issubset(actual_tools))


if __name__ == "__main__":
    main()
```

### Alternative Valid Approaches
- Use separate validators for strict tool-order checking.
- Replace in-memory dictionary with a lightweight JSON/file-backed mock.
- Add try/except around `invoke` for explicit runtime error reporting.
