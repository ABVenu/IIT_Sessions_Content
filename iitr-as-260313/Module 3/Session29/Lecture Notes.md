# Building Your First LangChain Agent

## Learning Context

In the previous learning flow, you authored LangChain tools with `@tool`, attached them using `bind_tools`, read structured `tool_calls`, and sent results back with `ToolMessage`.

You also built a **manual tool-feedback loop** with a safety limit (`max_steps`), recoverable error handling, and a controlled query set for diagnosis.

That manual loop taught you every step clearly. Now we move one step ahead: let LangChain’s **agent runtime** manage the same loop for you, with built-in limits and step-level traces.

By the end of this lesson, you will understand how to:

- Build a **tool-calling agent** using `create_tool_calling_agent`.
- Run that agent safely with **`AgentExecutor`**.
- Configure **`max_iterations`** and **`handle_parsing_errors`** so loops stay bounded and recoverable.
- Capture **intermediate steps** for transparent observability.
- Validate behavior with a **cohort test pack** (single-tool, multi-tool, and no-tool queries).

## Why Agent Executor Is Needed

You already know the tool-calling flow: the model requests a tool, your app runs it, and the model uses the result to answer.

Writing that loop yourself is excellent for learning. In larger apps, the same loop must also handle retries, parsing issues, logging, and stop conditions.

- **Official Definition:** `AgentExecutor` is a LangChain runtime that runs an agent loop, executes tools, and applies safety controls.
- **In Simple Words:** It is the operations manager that runs your tool-calling process safely.
- **Real-Life Example:** Think of a call-centre supervisor who tracks which support desk was contacted, what reply came back, and when to stop retries.

Without a runtime manager, your code can become hard to debug, fragile under failures, and difficult to scale.

![LangChain Agent Executor Overview](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-agent-executor-overview.png)

The ideas you used earlier still apply:

- Clear tool names and descriptions help correct tool selection.
- A loop limit prevents runaway retries.
- Traces help you diagnose wrong tools or wrong arguments.
- Failures should surface as recoverable signals, not hard crashes.

`AgentExecutor` packages those ideas into one managed runtime.

## End-to-End Tool Calling Flow

The control flow is the same pattern you practised manually. The difference is who manages the loop.

![End-to-End Tool Calling Flow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-tool-calling-flow.png)

1. User sends a query.
2. Query goes to the LLM.
3. LLM decides whether a tool is needed.
4. If no tool is needed, the LLM answers directly.
5. If a tool is needed, the selected tool is executed.
6. Tool output is sent back to the LLM.
7. The LLM generates a user-friendly final response.

In the previous learning flow, **you** wrote the code for steps 5 and 6. With `AgentExecutor`, LangChain runs those steps for you while you keep control through configuration.

This is the core pattern behind support assistants, order assistants, and workflow bots.

## Key Terms You Must Know

### Tool

- **Official Definition:** A tool is an external callable function that the agent can invoke.
- **In Simple Words:** A tool is a Python function connected to real work.
- **Real-Life Example:** `get_order_status(order_id)` is like asking the courier desk for a parcel update.

You still create tools with the `@tool` decorator, just as before.

### Tool Calling Agent

- **Official Definition:** An agent that can reason about when and which tool to call.
- **In Simple Words:** It is the decision-maker that chooses actions.
- **Function used:** `create_tool_calling_agent(...)`.

This replaces the part where you called `bind_tools` and inspected `tool_calls` yourself.

### Agent Executor

- **Official Definition:** Runtime execution layer for an agent and its tools.
- **In Simple Words:** It actually runs the agent, tracks steps, handles errors, and stops runaway loops.
- **Object used:** `AgentExecutor(...)`.

### Max Iterations

- **Official Definition:** Upper bound on how many action loops an agent can perform.
- **In Simple Words:** A retry limit to avoid infinite tool-calling.
- **Typical value:** `max_iterations=3`.

This is the managed version of the `max_steps` limit you used in the manual loop.

### Handle Parsing Errors

- **Official Definition:** A safety option for handling output parsing issues without an immediate crash.
- **In Simple Words:** Instead of breaking the app, the loop can recover gracefully.
- **Typical value:** `handle_parsing_errors=True`.

This continues the recoverable-error idea from the previous learning flow.

### Intermediate Steps

- **Official Definition:** Structured traces of tool actions and observations across agent steps.
- **In Simple Words:** Debug logs showing which tool ran, with what input, and what output came back.
- **Typical value:** `return_intermediate_steps=True`.

These traces replace the print statements you wrote while diagnosing tool-selection and argument faults.

### Agent Scratchpad (`MessagesPlaceholder`)

- **Official Definition:** Temporary working memory inside the prompt for ongoing reasoning and tool traces in one request.
- **In Simple Words:** The agent’s notepad for the current run.
- **Why needed:** Without a scratchpad, multi-step tool chaining loses context.

![Agent Scratchpad Working Memory](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-agent-scratchpad-memory.png)

## Core Libraries and Imports Used

The implementation uses these components:

- `ChatOpenAI` for model access (any chat model with tool-calling support can follow the same pattern).
- `@tool` from `langchain_core.tools` for tool registration.
- `ChatPromptTemplate` and `MessagesPlaceholder` for prompt and scratchpad.
- `create_tool_calling_agent` for building the tool-aware agent.
- `AgentExecutor` for runtime execution.

Import paths can change across LangChain versions. If an import fails, check the official docs for your installed version.

## Demo Use Case: E-Commerce Support Assistant

We will build a simple order-support assistant with a fake order database.

Sample order fields include:

- `status` (shipped / cancelled / delivered)
- `city`
- `amount`
- `delivery_days`

This setup makes tool routing easy to test. It is the same idea as the fee, eligibility, and ticket tools from the previous learning flow — one clear job per tool.

## Tool 1: Get Order Status

### Goal

Fetch current status for a specific order ID.

### Behavior

- If the order is not found, return a clear not-found message.
- If found, return status, city, and amount information.

### Use Case

Queries like: "What is the status of order ORD101?"

Clear tool descriptions matter here. A vague description can cause the model to pick the wrong tool, just as you saw while diagnosing tool-selection faults earlier.

## Tool 2: Calculate Refund Amount

### Goal

Calculate or explain refund eligibility for a given order.

### Behavior

- If `cancelled`, the order is eligible for refund (full amount in this demo).
- If `delivered`, eligibility depends on product or policy conditions.
- If `shipped`, refund cannot be finalized immediately; cancellation or return is required first.

Tool output should communicate policy logic clearly, not only yes or no. That helps the model write a better final reply for the user.

## Tool 3: Estimate Delivery Timeline

### Goal

Provide an ETA for a specific order.

### Behavior

- If `shipped`, report expected delivery in remaining days.
- If `delivered`, report that delivery is already complete.
- If `cancelled`, report that no delivery timeline exists.
- If the order ID is invalid, return an order-not-found message.

Condition-based responses keep each tool focused on one responsibility.

## Building the Prompt Template

The prompt is created with `ChatPromptTemplate.from_messages(...)` and includes:

- A **system message** for assistant behavior boundaries.
- A **human input placeholder** for the user query.
- A **messages placeholder** (`agent_scratchpad`) for intermediate reasoning flow.

This setup lets the agent reason across tool interactions during a single invocation.

Without `agent_scratchpad`, the executor cannot pass tool observations back into the next model turn correctly.

## Creating and Executing the Agent

### Agent Construction

Create the agent with:

- the model (LLM),
- the tool list,
- the prompt template.

Then wrap it in an executor with:

- `verbose=True`
- `max_iterations=3`
- `handle_parsing_errors=True`
- `return_intermediate_steps=True`

### Why This Configuration Matters

This single setup moves the implementation closer to production behavior:

- **Bounded retries** through `max_iterations`.
- **Transparent traceability** through intermediate steps and verbose logs.
- **Safer parsing** through `handle_parsing_errors`.
- **Structured debugging** without writing a full manual loop.

You still own tool design and validation. The executor owns the repetitive orchestration.

## Reading Intermediate Steps for Observability

After `agent_executor.invoke(...)`, read `result["intermediate_steps"]` and extract:

![Observability with Intermediate Steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-observability-intermediate-steps.png)

- step number
- selected tool name
- tool input
- tool observation / output

This gives step-level visibility into the actual control flow.

Observability helps you:

- verify that the expected tool was chosen
- inspect wrong arguments quickly
- locate where a failure happened
- separate model reasoning issues from tool implementation issues

For real applications, this is essential for quality and reliability.

## Single-Tool, Multi-Tool, and No-Tool Behavior

Agents behave differently depending on the query class.

- **Single-tool query:** needs one tool only (for example, order status).
- **Multi-tool query:** needs several tools (status + ETA + refund).
- **No-tool query:** needs no available tool (for example, a flight booking request).

When no matching tool exists, the model should give a direct fallback-style response instead of inventing unknown functionality.

Tool boundaries protect system scope. The agent should not pretend it can book flights if that tool was never provided.

## Production-Side Error Thinking

Implementation choices connect directly to real deployment risks:

- Tool calls can fail due to network, API, or server timeouts.
- Retry must be limited.
- Parsing can fail when output format changes.
- Fallback messaging is needed after repeated failure.

That is why `max_iterations` and parsing control are configured explicitly, not left as defaults you never inspect.

## Cohort Test Pack: Practical Validation Strategy

A cohort test pack is a small, fixed set of representative queries used to validate agent behavior repeatedly.

![Cohort Test Pack Validation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session38/session38-cohort-test-pack.png)

### Query Classes Covered

- Single tool call
- Multi-tool call
- No tool call
- Missing order ID

### Expected vs Actual Validation

For each test case:

1. Run the executor with the test query.
2. Extract actual tools from intermediate steps.
3. Compare against the expected tool list.
4. Mark pass or fail.

This method checks not only final output, but also decision-path correctness.

It is the managed-agent version of the controlled query set you used earlier for diagnosis.

## Full Code: Bounded Tool-Calling Agent

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
- The model receives a clear instruction to use tools only when required.
- `create_tool_calling_agent` builds decision logic for tool use.
- `AgentExecutor` executes that decision flow with safe runtime controls.
- Intermediate steps provide transparent and testable traces.

## Cohort Test Pack Code

Use this small test pack to validate tool-path correctness across the standard query classes.

```python
test_pack = [  # define representative query classes
    {  # single-tool case
        "query": "What is the status of order ORD101?",  # ask only for status
        "expected_tools": ["get_order_status"],  # expect one tool
    },
    {  # multi-tool case
        "query": "For order ORD102, check status, delivery estimate, and refund amount.",  # ask for three things
        "expected_tools": [  # expect all three tools in some order
            "get_order_status",
            "estimate_delivery_timeline",
            "calculate_refund_amount",
        ],
    },
    {  # no-tool case
        "query": "Can you book a flight from Delhi to Mumbai?",  # request outside tool scope
        "expected_tools": [],  # expect no tool calls
    },
    {  # missing order id case
        "query": "What is my refund amount?",  # refund asked without order id
        "expected_tools": [],  # agent should ask for id or answer without inventing a tool path
    },
]

for case in test_pack:  # run each validation case
    result = agent_executor.invoke({"input": case["query"]})  # execute agent for this query
    actual_tools = [action.tool for action, _ in result["intermediate_steps"]]  # collect tools actually used
    expected = set(case["expected_tools"])  # convert expected list to set for order-independent compare
    actual = set(actual_tools)  # convert actual list to set
    status = "PASS" if actual == expected else "FAIL"  # mark pass or fail
    print(case["query"])  # print the query under test
    print("Expected:", sorted(expected))  # print expected tools
    print("Actual:", sorted(actual))  # print actual tools
    print("Result:", status)  # print validation result
    print("-" * 40)  # print separator between cases
```

### How the Code Works

- Each case represents one query class from the cohort test pack.
- Intermediate steps reveal the real tool path, not only the final sentence.
- Set comparison ignores tool order, which is useful when the model calls valid tools in a different sequence.
- Pass/fail output makes regressions easy to spot after prompt or tool changes.

## Manual Loop vs Agent Executor

You now have both mental models side by side.

| Approach | Who manages the loop | Strength |
| --- | --- | --- |
| Manual tool-feedback loop | Your Python code | Full visibility and custom validation |
| `AgentExecutor` | LangChain runtime | Faster setup with built-in limits and traces |

Use the manual loop when you need deep control. Use `AgentExecutor` when the standard tool-calling pattern is enough and you want safer defaults quickly.

In both cases, good tools, clear descriptions, loop limits, and observability remain non-negotiable.

## Simple Self-Practice Activities

Try these individually:

1. Change `max_iterations` from 3 to 1 and observe behavior for a multi-step query.
2. Toggle `return_intermediate_steps` between `True` and `False` and compare outputs.
3. Add one new order to `orders_db` and test all three tools for that ID.
4. Write one no-tool query and verify that no tool is called.
5. Build a small assertion check to compare expected and actual tools for each test case.

These activities strengthen your understanding of runtime controls and observability.

## Key Takeaways

- `create_tool_calling_agent` builds the decision layer; `AgentExecutor` runs it safely.
- `max_iterations` protects your app from unbounded retries, just as `max_steps` did in the manual loop.
- `handle_parsing_errors=True` improves resilience when model output is imperfect.
- `return_intermediate_steps=True` and `verbose=True` enable strong observability.
- Cohort test packs validate not only answer quality, but also tool-path correctness.

In upcoming learning flows, this foundation connects naturally with memory, retrieval patterns, and stronger production-grade governance for agents.

## Important Commands, Libraries, Terminologies Used

| Item | Type | Simple Meaning |
| --- | --- | --- |
| `@tool` | Decorator | Converts a Python function into a LangChain tool. |
| `create_tool_calling_agent` | Function | Creates an agent capable of tool selection. |
| `AgentExecutor` | Runtime class | Executes the tool-calling loop with safety controls. |
| `max_iterations` | Executor setting | Maximum retry/loop limit during execution. |
| `handle_parsing_errors` | Executor setting | Enables safe recovery from parsing issues. |
| `return_intermediate_steps` | Executor setting | Returns step-level action/observation traces. |
| `verbose=True` | Executor setting | Prints internal execution logs. |
| `ChatPromptTemplate` | Prompt class | Builds the chat-style prompt for the agent. |
| `MessagesPlaceholder` | Prompt helper | Injects scratchpad memory into the prompt. |
| `agent_scratchpad` | Prompt variable | Temporary working memory for the current request. |
| Intermediate steps | Trace data | Tool name, input, and observation for each step. |
| Observability | Practice | Monitoring and tracing internal execution behavior. |
| Cohort test pack | Testing idea | Structured set of representative validation queries. |
| Manual tool-feedback loop | Prior pattern | Hand-written loop using `tool_calls` and `ToolMessage`. |
