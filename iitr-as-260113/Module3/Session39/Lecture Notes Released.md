# LangChain Memory on Agents

## Context of This Session

In the previous class, you built a **tool-calling agent** with **`AgentExecutor`**: the model could pick tools, run them in a loop, and stop safely with limits like **`max_iterations`**. You also saw **`MessagesPlaceholder`** briefly for **`agent_scratchpad`** — the scratchpad holds **tool steps for the current run**, not past user turns.

This session adds **conversational memory** so the same agent can answer follow-ups like *"What is the status of it?"* without the user repeating the order ID. You will wire **`chat_history`**, compare **with memory vs stateless**, fix a real wiring bug, and then use **`RunnableWithMessageHistory`** for automatic history updates across **sessions**.

**In this session, you will:**

- Extend agent prompts with **`MessagesPlaceholder`** for rolling **`chat_history`**
- Run a **multi-turn** customer-support demo where turn 2 depends on turn 1
- **Diagnose** missing manual appends and other common history defects
- **Compare** answer quality when history is present vs empty
- Use **`RunnableWithMessageHistory`** with **session-scoped** in-memory stores

---

## Why Agents Need Memory

![Why agents need memory — stateless calls forget prior turns; conversational memory carries chat_history into each invoke](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-01-why-agents-need-memory.png)

**Stateless LLM call:**

- **Official Definition:** Each API call is independent; the model receives only what you send in that request unless you add prior messages yourself.
- **In Simple Words:** Every new call starts with a blank slate — it does not remember your last chat unless you paste it in again.
- **Real-Life Example:** You tell a shopkeeper your order number, leave, and a new person at the counter asks *"Which order?"* again — that is stateless service.

- Turn 1: *"My order ID is ORD102."* → status returned.
- Turn 2: *"What is the status of it?"* → without history, the model does not know what *"it"* means.
- **Tool calling still works** on each turn, but **wrong or missing context** leads to repeated questions or wrong tool inputs.

**Conversational memory:**

- **Official Definition:** Keeping prior user and assistant messages and attaching them to each new invocation so the model sees the full dialogue in one conversation.
- **In Simple Words:** You maintain a list: query 1, answer 1, query 2, answer 2 — and send that list with query 3.
- **Real-Life Example:** A clinic reception file: each visit to the desk adds a line; the doctor reads the whole file, not only your latest sentence.

You are not building a plain chatbot — you are building an **agent with tools and memory**.

---

## MessagesPlaceholder and chat_history

![MessagesPlaceholder and chat_history in the prompt — system, rolling history, human input, and agent_scratchpad layers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-02-messages-placeholder-chat-history.png)

**MessagesPlaceholder:**

- **Official Definition:** A slot inside **`ChatPromptTemplate`** where LangChain injects a **list of messages** at runtime (variable name you choose).
- **In Simple Words:** An empty chair in the prompt layout — you reserve space, then fill it with past chat lines when you run the agent.
- **Real-Life Example:** Reserving a seat in class with your pencil — the seat exists before you sit; the placeholder exists before messages are added.

- Used inside **`ChatPromptTemplate.from_messages([...])`**.
- It does **not** store messages by itself — it only **allocates** where history will appear (like a placeholder in a school notebook).
- For conversation recall, use variable name **`chat_history`** in the placeholder.

**optional=True:**

- On the first turn, **`chat_history`** is empty — that is valid.
- **`optional=True`** tells LangChain the placeholder may be empty without error.
- Without it, you may be forced to always pass a non-empty history list.

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

# --- Fake order database (in application RAM; lost on restart) ---
ORDERS = {
    "ORD101": {"status": "out for delivery"},
    "ORD102": {"status": "cancelled"},
}

@tool
def get_order_status(order_id: str) -> str:
    """Use when the user asks for order status or tracking."""
    order = ORDERS.get(order_id)
    if not order:
        return f"Order with ID {order_id} not found."
    return f"Order status for {order_id} is {order['status']}."

tools = [get_order_status]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful customer support agent. "
        "If the user gives an order ID, remember it for this conversation. "
        "For follow-ups like 'track it' or 'what is the status of it', use the order ID from chat history. "
        "Use tools when order status is required. "
        "If no order ID is available, ask politely for it."
    )),
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

print("Turn 1")
print("User:", "Hi, my order ID is ORD102.")
print("AI:", ask_agent("Hi, my order ID is ORD102."))
print()
print("Turn 2")
print("User:", "What is the status of it?")
print("AI:", ask_agent("What is the status of it?"))
```

**How the code works:**

- **`chat_history`** is your Python list — the placeholder only defines **where** it goes in the prompt.
- **`agent_scratchpad`** is separate: LangChain fills it with **tool-call steps for the current run** (inputs, outputs, errors).
- **`invoke`** must include **`chat_history`** every turn, or the model sees an empty slot.
- After each run, **append human then AI** — order matters (user speaks first, then assistant replies).
- Turn 2 can call **`get_order_status("ORD102")`** even when the user does not repeat the ID.

### Quick Activity — Placeholder vs Storage

Mark **True** or **False**:

1. `MessagesPlaceholder` automatically saves every user message.  
2. `optional=True` helps on the first turn when history is empty.  
3. `agent_scratchpad` replaces `chat_history` for follow-up questions.  

**Answers:** 1 → False, 2 → True, 3 → False.

---

## chat_history vs agent_scratchpad

| | **chat_history** | **agent_scratchpad** |
|---|---|---|
| Purpose | Past **user ↔ assistant** turns across invocations | **Current run** tool steps (which tool, input, output) |
| Who fills it | **You** (manual append) or **RunnableWithMessageHistory** (auto) | **AgentExecutor** during tool loop |
| Needed for | *"What is the status of it?"* | Reliable multi-step tool use in one query |
| Layer | Application RAM by default; DB if you persist | Working memory for one execution |

- For a **tool-calling agent with follow-ups**, you need **both** placeholders in the prompt.
- Scratchpad does **not** remember order ID from turn 1 when turn 2 runs — that is **`chat_history`**'s job.

![chat_history vs agent_scratchpad — past turns across invocations vs tool steps for the current run only](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-03-chat-history-vs-scratchpad.png)

---

## The Bug You Saw in Class: Placeholder Without Append

**Symptom:** Turn 1 works; turn 2 asks *"Could you share the order ID?"* even though turn 1 already gave it.

![Classic bug — MessagesPlaceholder wired but chat_history never appended after invoke](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-04-bug-missing-append.png)

**Cause:** You defined **`MessagesPlaceholder("chat_history")`** and passed **`chat_history=[]`**, but never **appended** after each turn.

**Fix:** After **`invoke`**, append **`HumanMessage`** then **`AIMessage`** to the same list you pass next time.

**Common debug points for executor-based agents with memory:**

1. **Wrong placeholder variable name** — name in template must match key in **`invoke`** (e.g. both `chat_history`).
2. **Forgot to append** (manual mode) — placeholder reserves space; your code must fill it.
3. **Wrong message order** — always **human first, then AI** per turn.
4. **Shared memory across sessions** — one global list for all users mixes conversations; use **per-session** stores in production.

---

## Stateless Baseline (Same Agent, Empty History)

![Stateless vs with memory — same turn-2 wording succeeds only when chat_history is appended](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-05-stateless-vs-with-memory.png)

To prove memory changes behavior, use the same agent file but **never append** and always pass an empty list (or skip updates).

```python
# Same agent_executor setup as above; chat_history stays []

def ask_agent_stateless(user_input: str) -> str:
    response = agent_executor.invoke({
        "input": user_input,
        "chat_history": [],
    })
    return response["output"]

print("Turn 1 (stateless)")
print(ask_agent_stateless("Hi, my order ID is ORD102."))
print("Turn 2 (stateless)")
print(ask_agent_stateless("What is the status of it?"))
```

**How the code works:**

- Each turn sees **only** the current **`input`** and system rules — no prior turns.
- Turn 2 typically **fails to recall** ORD102 and may ask for the ID again.
- With memory + append, turn 2 **succeeds** on the same wording.

**When memory clearly helps:**

- Follow-ups with **pronouns** (*it*, *that order*, *both of us*).
- Facts spread across turns (ID in turn 1, action in turn 2).
- Tool calls that need **earlier user-supplied IDs**.

**When stateless is often enough:**

- Single-shot questions with all facts in one message.
- Stateless APIs where each request is self-contained by design.

### Quick Activity — Memory or Not?

Would you enable rolling **chat_history**? Write **Y** or **N**:

1. *"Refund policy for credit cards?"* (one message, complete)  
2. *"My ID is E-4471"* then *"Draft mail for the dates we discussed"*  
3. *"GST on ₹4,200"* (calculator-style, one shot)  

**Answers:** 1 → N, 2 → Y, 3 → N.

---

## Automatic History: RunnableWithMessageHistory

![RunnableWithMessageHistory — load session history, inject chat_history, run AgentExecutor, append automatically](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-06-runnable-with-message-history.png)

Manual append is fine for learning but **error-prone** in production (forget a turn, wrong order, wrong session).

**RunnableWithMessageHistory:**

- **Official Definition:** A LangChain wrapper that loads session history, injects it into the prompt, runs the chain, and appends new user/assistant messages automatically.
- **In Simple Words:** A helper that acts like reception staff updating the clinic file after every visit — you only pass the new question and session ID.
- **Real-Life Example:** ChatGPT tabs — each tab is a **session**; messages in tab A do not appear in tab B.

**InMemoryChatMessageHistory:**

- Stores messages in **application RAM** for that session (not a database).
- Restart the app → history is gone unless you persist to a DB (as ChatGPT does for old chats).

```python
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

os.environ["OPENAI_API_KEY"] = "your-key-here"

ORDERS = {"ORD101": {"status": "out for delivery"}, "ORD102": {"status": "cancelled"}}

@tool
def get_order_status(order_id: str) -> str:
    """Use when the user asks for order status or tracking."""
    order = ORDERS.get(order_id)
    if not order:
        return f"Order with ID {order_id} not found."
    return f"Order status for {order_id} is {order['status']}."

tools = [get_order_status]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful customer support agent. "
        "Remember order IDs from the conversation. "
        "Use tools when order status is required."
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

agent_with_memory = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="output",
)

def ask_agent_auto(session_id: str, user_input: str) -> str:
    result = agent_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}},
    )
    return result["output"]

SESSION_A = "user-001"

print("Turn 1")
print(ask_agent_auto(SESSION_A, "Hi, my order ID is ORD101."))
print("Turn 2 (same session)")
print(ask_agent_auto(SESSION_A, "What is the status of it?"))

SESSION_B = "user-002"
print("Turn 1 in other session (should not see ORD101)")
print(ask_agent_auto(SESSION_B, "What is my order ID?"))
```

**How the code works:**

- **`store`** maps **session_id → InMemoryChatMessageHistory** (session-wise memory, not one global list).
- **`get_session_history`** creates an empty history object the first time a session appears.
- **`RunnableWithMessageHistory`** wires **`input`**, **`chat_history`**, and **`output`** keys to match your prompt and executor.
- **`config={"configurable": {"session_id": ...}}`** picks which conversation bucket to use — like ChatGPT conversation IDs on different tabs.
- No manual **`append`** — the wrapper updates history after each **`invoke`**.

### Quick Activity — Session Isolation

User shares ORD101 in **session A**. In **session B**, they ask *"What is my order ID?"*

What should happen if wiring is correct?

**Answer:** Session B should **not** know ORD101 — histories are separate.

---

## Rolling Conversation History (n_messages)

![Session isolation and rolling history — separate session stores; n_messages caps the sliding window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session39/session39-07-session-isolation-rolling.png)

Long chats can **fill RAM** and **blow token limits**. **Rolling history** keeps only the last **N** messages (sliding window).

- Set on **`MessagesPlaceholder`**: `MessagesPlaceholder("chat_history", optional=True, n_messages=10)`
- When message 11 arrives, the **oldest** drops — like a fixed-size window sliding forward.
- ChatGPT also effectively limits how much of a very long thread fits in context.

| Approach | Pros | Cons |
|---|---|---|
| **Full history** | Best recall within the window | More tokens and RAM |
| **Rolling (`n_messages`)** | Bounded cost | May forget very old facts in the same thread |

- **Full** is better when you can afford it; **rolling** is safer at scale.
- Production chat products usually **persist** history in a **database** after the session, not only RAM.

### Practice Extension

In your auto-memory file, add **`n_messages=10`** to the **`chat_history`** placeholder and run **12+ turns** in one session. Confirm the earliest turns no longer appear in stored messages when you print **`store[session_id].messages`**.

---

## Persistence and Production Notes

- **Default in class demos:** history lives in **RAM** — restart clears it.
- **Production:** load/save **`chat_history`** per user/session in a **database** (same pattern, different backend).
- **Multi-tenant apps:** never share one **`chat_history`** list across customers — always key by **session / conversation ID**.
- **`get_order_status`** fake DB is also RAM-only — same lesson as the previous tool demos.

---

## Three Patterns You Built Today

| Pattern | File idea | History behavior |
|---|---|---|
| **With memory (manual)** | `langchain_agent_with_memory.py` | You append human/AI after each turn |
| **Stateless** | `langchain_agent_stateless.py` | Always pass `chat_history=[]` |
| **With memory (auto)** | `langchain_agent_memory_auto.py` | `RunnableWithMessageHistory` + session store |

Understand the **logic** first; variable names can be looked up from notes when you code, same as in a live implementation session.

---

## Key Takeaways

- Default LLM calls are **stateless**; agents need explicit **`chat_history`** for multi-turn continuity.
- **`MessagesPlaceholder`** reserves prompt space — **you** (or **`RunnableWithMessageHistory`**) must supply and update the list.
- **`agent_scratchpad`** tracks **tool steps for the current run**; **`chat_history`** tracks **past user/assistant turns**.
- Missing **append** after **`invoke`** is the classic bug: app runs, but follow-ups still fail.
- **Session-scoped** stores prevent User A's order ID from leaking into User B's chat.

This foundation prepares you to combine **memory**, **tools**, and later **retrieval** in one production-style agent.

---

## Important Commands, Libraries, Terminologies Used

| Item | Meaning / Usage |
| --- | --- |
| `MessagesPlaceholder` | Injects a message list slot into `ChatPromptTemplate` |
| `chat_history` | Variable for prior human/AI turns across invocations |
| `optional=True` | Allows empty history on first turn |
| `agent_scratchpad` | Holds tool-call intermediate steps for current run |
| `HumanMessage` / `AIMessage` | Typed message objects for manual history append |
| `AgentExecutor.invoke` | Runs agent; pass `input` and `chat_history` |
| `create_tool_calling_agent` | Builds tool-aware agent from LLM, tools, prompt |
| `RunnableWithMessageHistory` | Auto load/inject/append session history |
| `InMemoryChatMessageHistory` | Per-session message store in RAM |
| `get_session_history` | Factory returning history for a `session_id` |
| `configurable.session_id` | Selects which conversation bucket to use |
| `n_messages` | Rolling window cap on placeholder history |
| Stateless agent | Same executor, empty or unchanged history each turn |
| Conversational memory | Prior turns included in each new invocation |
