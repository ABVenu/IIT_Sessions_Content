# Building Your First LangChain Agent Executor

## What You Will Learn in This Session

In the previous class, you manually handled tool-calling flow with custom loop logic. You had to manage retries, failures, and tool sequencing using your own code. In this session, you move to a more production-ready approach by using **LangChain Agent Executor**.

By the end of this session, you will be able to:

- Build a **tool-calling agent** using `create_tool_calling_agent`.
- Execute that agent safely with **`AgentExecutor`**.
- Configure **`max_iterations`** and **`handle_parsing_errors`** to avoid unstable loops.
- Capture and inspect **intermediate steps** for observability and debugging.
- Validate behavior through a **cohort test pack** (single-tool, multi-tool, no-tool scenarios).

---

## Why Agent Executor Is Needed

When a user asks a query, the LLM can decide whether it needs a tool call or can answer directly. If a tool is needed, your application must call that tool, collect output, and feed it back for final response generation. Doing this manually works for learning, but becomes risky in larger systems.

![LangChain Agent Executor Overview](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-agent-executor-overview.png)

- **Official definition:** `AgentExecutor` is a runtime manager in LangChain that executes an agent loop and handles tool calls.
- **In simple words:** It is the operations manager that runs your tool-calling process safely.
- **Real-life example:** Think of a call-center supervisor who tracks which support team was contacted, what response came, and when to stop retries.

Without a runtime manager, your code can become difficult to debug, fragile under failures, and hard to scale.

---

## End-to-End Tool Calling Flow

The session repeatedly used this control flow:

![End-to-End Tool Calling Flow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-tool-calling-flow.png)

1. User sends a query.
2. Query goes to the LLM.
3. LLM decides:
   - Tool needed, or
   - No tool needed.
4. If no tool is needed, LLM answers directly.
5. If tool is needed, the selected tool is executed.
6. Tool output is sent back to LLM.
7. LLM generates a user-friendly final response.

This is the core pattern behind practical support assistants, order assistants, and workflow bots.

---

## Key Terms You Must Know

### Tool

- **Official definition:** A tool is an external callable function that the agent can invoke.
- **In simple words:** A tool is a Python function connected to real work.
- **Example from class:** `get_order_status(order_id)`.

Tools were created with the `@tool` decorator.

### Tool Calling Agent

- **Official definition:** An agent that can reason about when and which tool to call.
- **In simple words:** It is the decision-maker that chooses actions.
- **Class function used:** `create_tool_calling_agent(...)`.

### Agent Executor

- **Official definition:** Runtime execution layer for an agent and its tools.
- **In simple words:** It actually runs the agent, tracks steps, handles errors, and stops runaway loops.
- **Class object used:** `AgentExecutor(...)`.

### Max Iterations

- **Official definition:** Upper bound on how many action loops an agent can perform.
- **In simple words:** Retry limit to avoid infinite tool-calling.
- **Class value shown:** `max_iterations=3`.

### Handle Parsing Errors

- **Official definition:** A safety option for handling output parsing issues without immediate crash.
- **In simple words:** Instead of breaking the app, it lets the loop recover gracefully.
- **Class value shown:** `handle_parsing_errors=True`.

### Intermediate Steps

- **Official definition:** Structured traces of tool actions and observations across agent steps.
- **In simple words:** Debug logs showing which tool ran, with what input, and what output came back.
- **Class value shown:** `return_intermediate_steps=True`.

### Agent Scratchpad (`MessagesPlaceholder`)

- **Official definition:** Temporary working memory inside prompt flow for ongoing reasoning/tool traces in a request.
- **In simple words:** The agent’s notepad for the current run.
- **Why needed:** Without scratchpad, multi-step tool chaining loses context.

![Agent Scratchpad Working Memory](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-agent-scratchpad-memory.png)

---

## Core Libraries and Imports Used

The implementation used these components:

- `ChatOpenAI` for model access.
- `@tool` from `langchain_core.tools` for tool registration.
- `ChatPromptTemplate` and `MessagesPlaceholder` for prompt and scratchpad.
- `create_tool_calling_agent` for building the tool-aware agent.
- `AgentExecutor` for runtime execution.

The class also highlighted that import paths can change across LangChain versions, so always validate with official docs when import errors occur.

---

## Demo Use Case: E-Commerce Support Assistant

The class built a simple order-support assistant with a fake order database.

Sample order fields included:

- `status` (shipped/cancelled/delivered)
- `city`
- `amount`
- `delivery_days`

This practical setup made it easy to test tool routing behavior.

---

## Tool 1: Get Order Status

### Goal

Fetch current status for a specific order ID.

### Behavior

- If order not found -> return clear not-found message.
- If found -> return status, city, and amount information.

### Use Case

Queries like: "What is status of order ORD101?"

---

## Tool 2: Calculate Refund Amount

### Goal

Calculate or explain refund eligibility for a given order.

### Behavior Explained

- If `cancelled` -> eligible refund (typically full amount in this demo).
- If `delivered` -> eligibility depends on product/policy conditions.
- If `shipped` -> refund cannot be finalized immediately; cancellation/return path required.

### Important Learning

Tool output should communicate policy logic clearly, not just yes/no.

---

## Tool 3: Estimate Delivery Timeline

### Goal

Provide ETA for a specific order.

### Behavior

- If `shipped` -> expected delivery in remaining days.
- If `delivered` -> already delivered message.
- If `cancelled` -> no delivery timeline available.
- If order ID invalid -> order not found message.

This tool helped students understand condition-based response design.

---

## Building the Prompt Template

The prompt was created using `ChatPromptTemplate.from_messages(...)` with:

- A **system message** for assistant behavior boundaries.
- A **human input placeholder** for user query.
- A **messages placeholder** (`agent_scratchpad`) for intermediate reasoning flow.

This setup ensures the agent can reason across tool interactions during a single invocation.

---

## Creating and Executing the Agent

### Agent Construction

The class created the agent using:

- model (LLM),
- tool list,
- prompt template.

Then wrapped it in executor with:

- `verbose=True`
- `max_iterations=3`
- `handle_parsing_errors=True`
- `return_intermediate_steps=True`

### Why This Matters

This single configuration moves the implementation closer to production behavior:

- bounded retries,
- transparent traceability,
- safer parsing,
- structured debugging.

---

## Reading Intermediate Steps for Observability

The class printed each step from `result["intermediate_steps"]` and extracted:

![Observability with Intermediate Steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-observability-intermediate-steps.png)

- step number
- selected tool name
- tool input
- tool observation/output

This gave step-level visibility into actual control flow.

### Why Observability Is Critical

- You can verify if expected tool was chosen.
- You can inspect wrong arguments quickly.
- You can locate where failures happened.
- You can separate model reasoning issues from tool implementation issues.

For real applications, this is essential for quality and reliability.

---

## Single-Tool vs Multi-Tool Behavior

The class tested multiple query patterns:

- Query needing one tool (order status only).
- Query needing multiple tools (status + ETA + refund).
- Query requiring no available tool (e.g., flight booking request).

When no matching tool existed, the model gave a direct fallback-style response instead of executing unknown functionality. This showed how tool boundaries protect system scope.

---

## Production-Side Error Thinking Covered

The session connected implementation choices to real deployment risks:

- Tool calls can fail due to network/API/server timeouts.
- Retry must be limited.
- Parsing can fail when output format changes.
- Fallback messaging is needed after repeated failure.

This is exactly why `max_iterations` and parsing control were emphasized.

---

## Cohort Test Pack: Practical Validation Strategy

The class introduced a simple but useful test pack approach for agent behavior validation.

![Cohort Test Pack Validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-cohort-test-pack.png)

### Query Classes Covered

- Single tool call
- Multi-tool call
- No tool call
- Missing order ID

### Expected vs Actual Validation

For each test case:

1. Run executor with test query.
2. Extract actual tools from intermediate steps.
3. Compare against expected tool list.
4. Mark pass/fail.

This method checks not only final output, but also decision path correctness.

---

## Full Code (Class-Aligned Example with Line-by-Line Comments)

```python
from langchain_openai import ChatOpenAI  # import OpenAI chat model wrapper from LangChain
from langchain_core.tools import tool  # import decorator to convert Python functions into tools
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # import prompt helpers
from langchain.agents import AgentExecutor, create_tool_calling_agent  # import agent builder and executor

# fake order database for demo purpose
orders_db = {  # define in-memory dictionary as mock database
    "ORD101": {"status": "shipped", "city": "Delhi", "amount": 2500, "delivery_days": 2},  # sample shipped order
    "ORD102": {"status": "cancelled", "city": "Bangalore", "amount": 1800, "delivery_days": 0},  # sample cancelled order
    "ORD103": {"status": "delivered", "city": "Mumbai", "amount": 3200, "delivery_days": 0},  # sample delivered order
}  # end of fake database


@tool  # register this function as a LangChain tool
def get_order_status(order_id: str) -> str:  # define tool to fetch order status
    """Get the current status of a specific order ID."""  # tool description used by LLM
    order = orders_db.get(order_id)  # fetch order object from mock db
    if not order:  # check if order id does not exist
        return f"No order found for order ID {order_id}."  # return not-found message
    return (  # return formatted order details
        f"Order {order_id} is currently {order['status']} "  # include current order status
        f"for {order['city']} and amount is {order['amount']}."  # include city and amount
    )  # end return


@tool  # register refund calculator tool
def calculate_refund_amount(order_id: str) -> str:  # define refund logic tool
    """Calculate refund-related response for a specific order ID."""  # describe tool intent
    order = orders_db.get(order_id)  # fetch order from db
    if not order:  # if invalid order id
        return f"No order found for order ID {order_id}."  # return not-found response
    if order["status"] == "cancelled":  # if cancelled order
        return f"Refund amount for order {order_id} is {order['amount']}."  # full refund case
    if order["status"] == "delivered":  # if already delivered
        return (  # return policy-oriented message
            f"Order {order_id} is delivered. Refund eligibility depends on product policy."
        )  # end delivered response
    return (  # fallback for shipped/in-transit states
        f"Order {order_id} is shipped. Refund cannot be finalized at this stage."
    )  # end fallback


@tool  # register delivery estimate tool
def estimate_delivery_timeline(order_id: str) -> str:  # define ETA tool
    """Estimate delivery timeline for a specific order ID."""  # describe ETA tool
    order = orders_db.get(order_id)  # get order record
    if not order:  # handle invalid order id
        return f"No order found for order ID {order_id}."  # return invalid id message
    if order["status"] == "shipped":  # if order is in transit
        return (  # return ETA message
            f"Order {order_id} is shipped and expected in {order['delivery_days']} days."
        )  # end shipped response
    if order["status"] == "delivered":  # if order already delivered
        return f"Order {order_id} has already been delivered."  # delivered response
    if order["status"] == "cancelled":  # if order cancelled
        return f"Order {order_id} is cancelled, so no delivery timeline exists."  # cancelled response
    return f"Delivery status for order {order_id} is currently unavailable."  # handle unknown status


tools = [get_order_status, calculate_refund_amount, estimate_delivery_timeline]  # collect all tools

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # create deterministic chat model instance

prompt = ChatPromptTemplate.from_messages([  # create chat prompt template
    ("system", "You are a helpful e-commerce support assistant. Use tools only when required."),  # system role prompt
    ("human", "{input}"),  # user input placeholder
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # placeholder for step memory
])  # end prompt template

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)  # create tool-calling agent

agent_executor = AgentExecutor(  # create runtime executor
    agent=agent,  # pass created agent
    tools=tools,  # pass tool list
    verbose=True,  # print internal logs for tracing
    max_iterations=3,  # prevent infinite retries/loops
    handle_parsing_errors=True,  # recover gracefully from parsing issues
    return_intermediate_steps=True,  # include step-by-step tool traces in output
)  # end executor config

user_query = "For order ORD102, check status, delivery estimate, and refund amount."  # sample multi-tool query
result = agent_executor.invoke({"input": user_query})  # execute agent on user query

print("Final Output:", result["output"])  # print final user-facing answer

for idx, (action, observation) in enumerate(result["intermediate_steps"], start=1):  # iterate step traces
    print(f"\nStep {idx}")  # print step number
    print("Tool Selected:", action.tool)  # print tool name called in this step
    print("Tool Input:", action.tool_input)  # print input args sent to tool
    print("Tool Observation:", observation)  # print output returned by tool
```

### How the Code Works

- Three business tools are created for status, refund, and ETA.
- The model receives clear instruction to use tools only when required.
- `create_tool_calling_agent` builds decision logic for tool use.
- `AgentExecutor` executes that decision flow with safe runtime controls.
- Intermediate steps provide transparent and testable traces.

---

## Common Mistakes and How to Avoid Them

- Missing or vague tool descriptions can cause wrong tool selection.
- Not setting iteration limits can create runaway loops in failure cases.
- Ignoring intermediate traces makes debugging much slower.
- Treating parsing errors as fatal crashes reduces reliability.
- Mixing too many responsibilities in one tool reduces maintainability.

---

## Simple Self-Practice Activities

Try these individually after class:

1. Change `max_iterations` from 3 to 1 and observe behavior for multi-step query.
2. Toggle `return_intermediate_steps` between `True` and `False` and compare outputs.
3. Add one new order and test all three tools for that ID.
4. Write one no-tool query and verify that no tool is called.
5. Build a small assertion check to compare expected and actual tools for each test case.

These activities strengthen your understanding of runtime controls and observability.

---

## Key Takeaways

- `create_tool_calling_agent` builds the decision layer; `AgentExecutor` runs it safely.
- `max_iterations` protects your app from unbounded retries.
- `handle_parsing_errors=True` improves resilience in real-world outputs.
- `return_intermediate_steps=True` and `verbose=True` enable strong observability.
- Cohort test packs validate not just answer quality, but tool-path correctness.

In upcoming sessions, this foundation will connect naturally with memory, RAG integration, and stronger production-grade governance.

---

## Important Commands, Libraries, Terminologies Used

| Item | Meaning / Usage |
| --- | --- |
| `@tool` | Converts a Python function into a LangChain tool |
| `create_tool_calling_agent` | Creates an agent capable of tool selection |
| `AgentExecutor` | Runtime manager that executes tool-calling flow |
| `max_iterations` | Maximum retry/loop limit during execution |
| `handle_parsing_errors` | Enables safe recovery from parsing issues |
| `return_intermediate_steps` | Returns step-level action/observation traces |
| `verbose=True` | Prints internal execution logs |
| `MessagesPlaceholder` | Injects scratchpad memory into prompt |
| `agent_scratchpad` | Temporary working memory for current request |
| Observability | Monitoring and tracing internal execution behavior |
| Traceability | Ability to follow request path step by step |
| Cohort test pack | Structured set of representative validation queries |
