# LangChain Memory on Agents

## Learning Context

In the previous learning flow, you built a **tool-calling agent** with **`AgentExecutor`**: the model could pick tools, run them in a loop, and stop safely with limits like **`max_iterations`**.

You also used **`MessagesPlaceholder`** for **`agent_scratchpad`**. That scratchpad holds **tool steps for the current run**, not past user turns.

Every **AI agent** has three core parts: an **LLM** (the brain), **memory** (conversation context across turns), and **tools** (functions the LLM can call). The previous agent had LLM and tools; this lesson adds **memory** so the same agent can answer follow-ups like *"What is the status of it?"* without the user repeating the order ID.

By the end of this lesson, you will understand how to:

- Extend agent prompts with **`MessagesPlaceholder`** for rolling **`chat_history`**.
- Run a **multi-turn** support demo where turn 2 depends on turn 1.
- **Diagnose** missing manual appends and other common history wiring defects.
- **Compare** answer quality when history is present versus empty.
- Use **`RunnableWithMessageHistory`** with **session-scoped** in-memory stores.

## Why Agents Need Memory

![Why agents need memory — stateless calls forget prior turns; conversational memory carries chat_history into each invoke](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-01-why-agents-need-memory.png)

Your executor-based agent from the previous learning flow was powerful, but each `invoke` was still **stateless** unless you passed prior messages yourself.

**Stateless LLM call:**

- **Official Definition:** Each API call is independent; the model receives only what you send in that request unless you add prior messages yourself.
- **In Simple Words:** Every new call starts with a blank slate — it does not remember your last chat unless you paste it in again.
- **Real-Life Example:** You tell a shopkeeper your order number, leave, and a new person at the counter asks *"Which order?"* again — that is stateless service.

Without memory:

- Turn 1: *"My order ID is ORD102."* → status returned.
- Turn 2: *"What is the status of it?"* → the model does not know what *"it"* means.
- Tool calling still works on each turn, but **wrong or missing context** leads to repeated questions or wrong tool inputs.

**Conversational memory:**

- **Official Definition:** Keeping prior user and assistant messages and attaching them to each new invocation so the model sees the full dialogue.
- **In Simple Words:** You maintain a list — query 1, answer 1, query 2, answer 2 — and send that list with query 3.
- **Real-Life Example:** A clinic reception file: each visit adds a line; the doctor reads the whole file, not only your latest sentence.

You are not building a plain chatbot. You are building an **agent with tools and memory**.

## Core Libraries and Imports Used

The implementation uses these components:

- `ChatOllama` from `langchain_ollama` for local model access through Ollama.
- `ChatPromptTemplate` and `MessagesPlaceholder` from `langchain_core.prompts`.
- `HumanMessage` and `AIMessage` from `langchain_core.messages` for manual history append.
- `@tool` from `langchain_core.tools` for tool registration.
- `InMemoryChatMessageHistory` from `langchain_core.chat_history`.
- `RunnableWithMessageHistory` from `langchain_core.runnables.history`.
- `create_tool_calling_agent` and `AgentExecutor` from `langchain_classic.agents`.
- **`langchain-classic`** package for the managed agent runtime.

Import paths can change across LangChain versions. If an import fails, check the official docs for your installed version.

## Setting Up LangChain Classic

Agent functions live in a separate package from core LangChain utilities. Install the packages before running the lab:

```bash
pip install langchain-classic langchain-ollama langchain-core
```

- **`langchain-classic`** provides `AgentExecutor` and `create_tool_calling_agent`.
- **`langchain-ollama`** connects LangChain to your local Ollama server (for example, `llama3.1`).
- After installing, restart your editor or terminal so imports resolve cleanly.

If imports fail, verify the package name spelling and that your virtual environment is activated.

## MessagesPlaceholder and chat_history

![MessagesPlaceholder and chat_history in the prompt — system, rolling history, human input, and agent_scratchpad layers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-02-messages-placeholder-chat-history.png)

In the previous learning flow, `MessagesPlaceholder` held only `agent_scratchpad`. Now you add a second placeholder for past conversation turns.

**MessagesPlaceholder:**

- **Official Definition:** A slot inside **`ChatPromptTemplate`** where LangChain injects a **list of messages** at runtime (variable name you choose).
- **In Simple Words:** An empty chair in the prompt layout — you reserve space, then fill it with past chat lines when you run the agent.
- **Real-Life Example:** Reserving a seat in class with your pencil — the seat exists before you sit; the placeholder exists before messages are added.

Key points:

- Used inside **`ChatPromptTemplate.from_messages([...])`**.
- It does **not** store messages by itself — it only **allocates** where history will appear.
- For conversation recall, use variable name **`chat_history`** in the placeholder.

**optional=True:**

- On the first turn, **`chat_history`** is empty — that is valid.
- **`optional=True`** tells LangChain the placeholder may be empty without error.
- Without it, you may be forced to always pass a non-empty history list.

## Full Code: Agent with Manual chat_history

This demo continues the e-commerce support idea from the previous learning flow, with a focused status tool and rolling history.

```python
from langchain_ollama import ChatOllama  # import Ollama chat model wrapper from LangChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # import prompt and placeholder helpers
from langchain_core.messages import HumanMessage, AIMessage  # import typed message classes for history append
from langchain_core.tools import tool  # import decorator to convert Python functions into tools
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # import agent builder and executor

ORDERS = {  # define fake order database in application RAM
    "ORD101": {"status": "shipped"},  # sample shipped order from earlier demos
    "ORD102": {"status": "cancelled"},  # sample cancelled order from earlier demos
}  # end of fake order database


@tool  # register this function as a LangChain tool
def get_order_status(order_id: str) -> str:  # define tool to fetch order status
    """Use when the user asks for order status or tracking."""  # tool description used by the model
    order = ORDERS.get(order_id)  # look up order by id
    if not order:  # handle unknown order id
        return f"Order with ID {order_id} not found."  # return not-found message
    return f"Order status for {order_id} is {order['status']}."  # return status for valid order


tools = [get_order_status]  # collect tools for the agent

llm = ChatOllama(model="llama3.1", temperature=0)  # create deterministic local chat model via Ollama

prompt = ChatPromptTemplate.from_messages([  # build prompt with history and scratchpad slots
    ("system", (  # system instructions for support behavior
        "You are a helpful customer support agent. "  # set assistant role
        "If the user gives an order ID, remember it for this conversation. "  # ask model to reuse IDs
        "For follow-ups like 'track it' or 'what is the status of it', use the order ID from chat history. "  # guide pronoun resolution
        "Use tools when order status is required. "  # prefer tools for live status
        "If no order ID is available, ask politely for it."  # fallback when context is missing
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # reserve slot for past turns
    ("human", "{input}"),  # current user message placeholder
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # reserve slot for current-run tool steps
])  # end prompt template

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)  # create tool-calling agent

agent_executor = AgentExecutor(  # create runtime executor
    agent=agent,  # pass created agent
    tools=tools,  # pass tool list
    verbose=True,  # print internal logs for tracing
    max_iterations=3,  # keep the same safety limit idea from previous learning flow
    handle_parsing_errors=True,  # recover gracefully from parsing issues
)  # end executor config

chat_history = []  # start with empty conversation memory in Python list


def ask_agent(user_input: str) -> str:  # helper to run one turn and update history
    response = agent_executor.invoke({  # execute agent for current user input
        "input": user_input,  # pass current user message
        "chat_history": chat_history,  # pass all prior human/AI turns
    })  # end invoke call
    ai_text = response["output"]  # extract final assistant text
    chat_history.append(HumanMessage(content=user_input))  # append user message first
    chat_history.append(AIMessage(content=ai_text))  # append assistant reply second
    return ai_text  # return answer to caller


print("Turn 1")  # label first turn
print("User:", "Hi, my order ID is ORD102.")  # show user message
print("AI:", ask_agent("Hi, my order ID is ORD102."))  # run turn 1 and print answer
print()  # print blank line between turns
print("Turn 2")  # label second turn
print("User:", "What is the status of it?")  # show follow-up that depends on turn 1
print("AI:", ask_agent("What is the status of it?"))  # run turn 2 and print answer
```

### How the Code Works

- **`chat_history`** is your Python list — the placeholder only defines **where** it goes in the prompt.
- **`agent_scratchpad`** is separate: LangChain fills it with **tool-call steps for the current run**.
- **`invoke`** must include **`chat_history`** every turn, or the model sees an empty slot.
- After each run, **append human then AI** — order matters (user speaks first, then assistant replies).
- Turn 2 can call **`get_order_status("ORD102")`** even when the user does not repeat the ID.

### Quick Activity: Placeholder vs Storage

Mark **True** or **False**:

1. `MessagesPlaceholder` automatically saves every user message.
2. `optional=True` helps on the first turn when history is empty.
3. `agent_scratchpad` replaces `chat_history` for follow-up questions.

**Answers:** 1 → False, 2 → True, 3 → False.

## chat_history vs agent_scratchpad

Both placeholders appear in the same prompt, but they solve different problems.

| | **chat_history** | **agent_scratchpad** |
| --- | --- | --- |
| Purpose | Past **user ↔ assistant** turns across invocations | **Current run** tool steps (which tool, input, output) |
| Who fills it | **You** (manual append) or **`RunnableWithMessageHistory`** (auto) | **`AgentExecutor`** during the tool loop |
| Needed for | *"What is the status of it?"* | Reliable multi-step tool use in one query |
| Layer | Application RAM by default; DB if you persist | Working memory for one execution |

- For a **tool-calling agent with follow-ups**, you need **both** placeholders in the prompt.
- Scratchpad does **not** remember the order ID from turn 1 when turn 2 runs — that is **`chat_history`**'s job.

![chat_history vs agent_scratchpad — past turns across invocations vs tool steps for the current run only](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-03-chat-history-vs-scratchpad.png)

This distinction is easy to miss after the previous learning flow, because you already used `agent_scratchpad` successfully without any conversation memory.

## A Common Wiring Bug: Placeholder Without Append

**Symptom:** Turn 1 works; turn 2 asks *"Could you share the order ID?"* even though turn 1 already gave it.

![Classic bug — MessagesPlaceholder wired but chat_history never appended after invoke](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-04-bug-missing-append.png)

**Cause:** You defined **`MessagesPlaceholder("chat_history")`** and passed **`chat_history=[]`**, but never **appended** after each turn.

**Fix:** After **`invoke`**, append **`HumanMessage`** then **`AIMessage`** to the same list you pass next time.

**Common debug points for executor-based agents with memory:**

1. **Wrong placeholder variable name** — name in template must match key in **`invoke`** (for example, both `chat_history`).
2. **Forgot to append** (manual mode) — placeholder reserves space; your code must fill it.
3. **Wrong message order** — always **human first, then AI** per turn.
4. **Input key mismatch** — the key in your prompt template (for example, `{input}` in `("human", "{input}")`) must match **`input_messages_key`** in **`RunnableWithMessageHistory`**. If the prompt uses `human` but the wrapper expects `input`, history wiring breaks.
5. **Shared memory across sessions** — one global list for all users mixes conversations; use **per-session** stores in production.

If follow-ups fail, check history wiring before blaming the tool or the model.

## Stateless Baseline (Same Agent, Empty History)

![Stateless vs with memory — same turn-2 wording succeeds only when chat_history is appended](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-05-stateless-vs-with-memory.png)

To prove memory changes behavior, use the same agent but **never append** and always pass an empty list.

```python
def ask_agent_stateless(user_input: str) -> str:  # helper that never updates history
    response = agent_executor.invoke({  # execute agent for current user input only
        "input": user_input,  # pass current user message
        "chat_history": [],  # always pass empty history for stateless baseline
    })  # end invoke call
    return response["output"]  # return final assistant text


print("Turn 1 (stateless)")  # label first stateless turn
print(ask_agent_stateless("Hi, my order ID is ORD102."))  # run turn 1 without memory update
print("Turn 2 (stateless)")  # label second stateless turn
print(ask_agent_stateless("What is the status of it?"))  # run turn 2 without prior context
```

### How the Code Works

- Each turn sees **only** the current **`input`** and system rules — no prior turns.
- Turn 2 typically **fails to recall** ORD102 and may ask for the ID again.
- With memory and append, turn 2 **succeeds** on the same wording.

**When memory clearly helps:**

- Follow-ups with **pronouns** (*it*, *that order*, *both of us*).
- Facts spread across turns (ID in turn 1, action in turn 2).
- Tool calls that need **earlier user-supplied IDs**.

**When stateless is often enough:**

- Single-shot questions with all facts in one message.
- Stateless APIs where each request is self-contained by design.

### Quick Activity: Memory or Not?

Would you enable rolling **chat_history**? Write **Y** or **N**:

1. *"Refund policy for credit cards?"* (one message, complete)
2. *"My ID is E-4471"* then *"Draft mail for the dates we discussed"*
3. *"GST on ₹4,200"* (calculator-style, one shot)

**Answers:** 1 → N, 2 → Y, 3 → N.

## Automatic History: RunnableWithMessageHistory

![RunnableWithMessageHistory — load session history, inject chat_history, run AgentExecutor, append automatically](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-06-runnable-with-message-history.png)

Manual append is excellent for learning, but it is **error-prone** in production (forget a turn, wrong order, wrong session).

**RunnableWithMessageHistory:**

- **Official Definition:** A LangChain wrapper that loads session history, injects it into the prompt, runs the chain, and appends new user/assistant messages automatically.
- **In Simple Words:** A helper that acts like reception staff updating the clinic file after every visit — you only pass the new question and session ID.
- **Real-Life Example:** Chat tabs in a support app — each tab is a **session**; messages in tab A do not appear in tab B.

**InMemoryChatMessageHistory:**

- Stores messages in **application RAM** for that session (not a database).
- Restart the app → history is gone unless you persist to a database.

You may see a **deprecation warning** for `RunnableWithMessageHistory` in newer LangChain versions. The pattern taught here still works; LangGraph-based history is covered in a later learning flow.

```python
from langchain_ollama import ChatOllama  # import Ollama chat model wrapper from LangChain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # import prompt and placeholder helpers
from langchain_core.tools import tool  # import decorator to convert Python functions into tools
from langchain_core.chat_history import InMemoryChatMessageHistory  # import in-memory history store
from langchain_core.runnables.history import RunnableWithMessageHistory  # import auto history wrapper
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # import agent builder and executor

ORDERS = {  # define fake order database in application RAM
    "ORD101": {"status": "shipped"},  # sample shipped order
    "ORD102": {"status": "cancelled"},  # sample cancelled order
}  # end of fake order database


@tool  # register this function as a LangChain tool
def get_order_status(order_id: str) -> str:  # define tool to fetch order status
    """Use when the user asks for order status or tracking."""  # tool description used by the model
    order = ORDERS.get(order_id)  # look up order by id
    if not order:  # handle unknown order id
        return f"Order with ID {order_id} not found."  # return not-found message
    return f"Order status for {order_id} is {order['status']}."  # return status for valid order


tools = [get_order_status]  # collect tools for the agent
llm = ChatOllama(model="llama3.1", temperature=0)  # create deterministic local chat model via Ollama

prompt = ChatPromptTemplate.from_messages([  # build prompt with history and scratchpad slots
    ("system", (  # system instructions for support behavior
        "You are a helpful customer support agent. "  # set assistant role
        "Remember order IDs from the conversation. "  # ask model to reuse IDs from history
        "Use tools when order status is required."  # prefer tools for live status
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # reserve slot for past turns
    ("human", "{input}"),  # current user message placeholder
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # reserve slot for current-run tool steps
])  # end prompt template

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)  # create tool-calling agent
agent_executor = AgentExecutor(  # create runtime executor
    agent=agent,  # pass created agent
    tools=tools,  # pass tool list
    verbose=True,  # print internal logs for tracing
    max_iterations=3,  # keep bounded retries
    handle_parsing_errors=True,  # recover gracefully from parsing issues
)  # end executor config

store = {}  # map session_id to history objects in RAM


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:  # factory for session history
    if session_id not in store:  # create history only on first use
        store[session_id] = InMemoryChatMessageHistory()  # start empty history for this session
    return store[session_id]  # return existing or newly created history


agent_with_memory = RunnableWithMessageHistory(  # wrap executor with automatic history handling
    agent_executor,  # runnable to execute
    get_session_history,  # function that returns history for a session id
    input_messages_key="input",  # key for current user input
    history_messages_key="chat_history",  # key matching prompt placeholder
    output_messages_key="output",  # key for assistant output to append
)  # end history wrapper config


def ask_agent_auto(session_id: str, user_input: str) -> str:  # helper for one turn in a session
    result = agent_with_memory.invoke(  # run agent with automatic history load/append
        {"input": user_input},  # pass only the new user message
        config={"configurable": {"session_id": session_id}},  # select conversation bucket
    )  # end invoke call
    return result["output"]  # return final assistant text


SESSION_A = "user-001"  # first customer conversation id

print("Turn 1")  # label first turn in session A
print(ask_agent_auto(SESSION_A, "Hi, my order ID is ORD101."))  # store ORD101 in session A
print("Turn 2 (same session)")  # label follow-up in session A
print(ask_agent_auto(SESSION_A, "What is the status of it?"))  # resolve "it" using session A history

SESSION_B = "user-002"  # second customer conversation id
print("Turn 1 in other session (should not see ORD101)")  # label isolated session B turn
print(ask_agent_auto(SESSION_B, "What is my order ID?"))  # session B must not know ORD101
```

### How the Code Works

- **`store`** maps **session_id → InMemoryChatMessageHistory** (session-wise memory, not one global list).
- **`get_session_history`** creates an empty history object the first time a session appears.
- **`RunnableWithMessageHistory`** wires **`input`**, **`chat_history`**, and **`output`** keys to match your prompt and executor.
- **`config={"configurable": {"session_id": ...}}`** picks which conversation bucket to use.
- No manual **`append`** — the wrapper updates history after each **`invoke`**.

### Session Isolation

![Session isolation — separate session stores keep each conversation bucket independent](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-07-session-isolation-rolling.png)

- **Session A** and **Session B** each get their own **`InMemoryChatMessageHistory`** object.
- Facts shared in session A (for example, ORD101) do **not** leak into session B.
- This mirrors separate chat tabs in a support app — each tab is an independent conversation.

### Quick Activity: Session Isolation

User shares ORD101 in **session A**. In **session B**, they ask *"What is my order ID?"*

What should happen if wiring is correct?

**Answer:** Session B should **not** know ORD101 — histories are separate.

## Persistence and Production Notes

- **Default in demos:** history lives in **RAM** — restart clears it.
- **Production:** load and save **`chat_history`** per user or session in a **database** (for example, PostgreSQL) — same pattern, different backend.
- **Multi-tenant apps:** never share one **`chat_history`** list across customers — always key by **session / conversation ID**.
- The fake **`ORDERS`** map is also RAM-only — same idea as the earlier tool demos. In production, tools would call real APIs instead.

## Three Patterns Side by Side

| Pattern | History behavior | Best use |
| --- | --- | --- |
| **With memory (manual)** | You append human/AI after each turn | Learning and debugging wiring |
| **Stateless** | Always pass `chat_history=[]` | Single-shot requests |
| **With memory (auto)** | `RunnableWithMessageHistory` + session store | Multi-user apps with less append risk |

Understand the **logic** first. Variable names can be looked up from notes when you code.

## Simple Self-Practice Activities

Try these individually:

1. Run the manual-memory agent for ORD102, then ask *"What is the status of it?"* and confirm the tool uses ORD102.
2. Remove the two `append` lines and observe how turn 2 fails.
3. Run the stateless baseline on the same two turns and compare answers.
4. Use `RunnableWithMessageHistory` with two session IDs and prove session B cannot see session A's order ID.

These activities strengthen your understanding of history wiring and session isolation.

## Key Takeaways

- Default LLM calls are **stateless**; agents need explicit **`chat_history`** for multi-turn continuity.
- **`MessagesPlaceholder`** reserves prompt space — **you** (or **`RunnableWithMessageHistory`**) must supply and update the list.
- **`agent_scratchpad`** tracks **tool steps for the current run**; **`chat_history`** tracks **past user/assistant turns**.
- Missing **append** after **`invoke`** is the classic bug: the app runs, but follow-ups still fail.
- **Session-scoped** stores prevent User A's order ID from leaking into User B's chat.

This foundation prepares you to combine **memory**, **tools**, and later **retrieval** in one production-style agent.

## Important Commands, Libraries, Terminologies Used

| Item | Type | Simple Meaning |
| --- | --- | --- |
| `pip install langchain-classic` | CLI command | Installs the managed agent runtime package. |
| `ChatOllama` | Chat model class | Connects LangChain to a local Ollama model. |
| `MessagesPlaceholder` | Prompt helper | Injects a message list slot into `ChatPromptTemplate`. |
| `chat_history` | Prompt variable | Prior human/AI turns across invocations. |
| `optional=True` | Placeholder option | Allows empty history on the first turn. |
| `agent_scratchpad` | Prompt variable | Holds tool-call intermediate steps for the current run. |
| `HumanMessage` / `AIMessage` | Message classes | Typed message objects for manual history append. |
| `AgentExecutor.invoke` | Method | Runs agent; pass `input` and `chat_history`. |
| `create_tool_calling_agent` | Function | Builds a tool-aware agent from LLM, tools, and prompt. |
| `RunnableWithMessageHistory` | Wrapper | Auto load, inject, and append session history. |
| `InMemoryChatMessageHistory` | History store | Per-session message store in RAM. |
| `get_session_history` | Factory function | Returns history for a given `session_id`. |
| `configurable.session_id` | Config key | Selects which conversation bucket to use. |
| `input_messages_key` | Config key | Must match the user-input key in your prompt template. |
| Stateless agent | Pattern | Same executor, empty or unchanged history each turn. |
| Conversational memory | Pattern | Prior turns included in each new invocation. |
