# RAG Tool and Integrated LangChain Agent

## Context of This Session

In the **previous** class you built a **LangChain RAG pipeline** for a policy support bot: **loaders**, **text splitters**, **OpenAI embeddings**, **Chroma**, a **retriever**, and an **LCEL chain** that answers only from retrieved context. That flow always retrieved documents — the chain did not choose *whether* to search.

Earlier you also wired **conversational memory** into **tool-calling agents**: **`MessagesPlaceholder`** for **`chat_history`**, manual append after each turn, and **`agent_scratchpad`** for tool steps inside one run.

This session **unifies** those skills into one **integrated LangChain agent** — a **course support bot** with a **retriever-backed tool**, a **second auxiliary tool** (ticket lookup), **multi-turn memory**, and a compact **EvalPack** to test behaviour before you ship.

**In this session, you will:**

- Design **retriever-backed tools** whose **contracts** support **tool arbitration** next to non-retrieval tools
- Build **`ragagent.py`** — ingest policy docs, wrap the retriever with **`create_retriever_tool`**, add **`get_ticket_status`**, and run **`AgentExecutor`**
- Run **multi-turn** and **multi-tool** queries that combine **memory** with **retrieval-backed** answers
- Execute an **EvalPack** and **interpret failure signatures** — wrong tool, weak retrieval, over-refusal, missing memory

---

## From Standalone RAG Chain to Agentic RAG

- **Official Definition:** **Agentic RAG** wraps retrieval inside a **tool-calling agent** so the model can **decide** when to retrieve, when to call other tools, when to do both, or when to answer or refuse without tools.
- **In Simple Words:** Yesterday the bot **always** opened the policy file. Today a **supervisor** chooses which button to press.
- **Real-Life Example:** At a **coaching centre help desk**, one clerk searches the **rulebook**, another checks the **ticket system** — the front desk decides who to call.

**Previous pattern (standalone RAG):**

```
User question → always retrieve → prompt + chunks → LLM → answer
```

**Today's pattern (integrated agent):**

```
User question → Agent decides → [retriever tool | auxiliary tool | both | direct reply] → answer
```

| Piece | Standalone RAG chain | Integrated agent |
|---|---|---|
| Retrieval | **Always** runs | Runs **only when agent picks** the retriever tool |
| Other actions | Not supported | **Ticket lookup**, future calculators, etc. |
| Memory | Usually none in the chain | **`chat_history`** across turns |
| Testing | Manual one-off queries | **EvalPack** with expected tools and keywords |

- **Common doubt:** *Is `create_retriever_tool` a totally new idea?* No — it exposes your existing **retriever** as a **tool** the agent can select, like any `@tool` function.
- **Agentic RAG** is also called **tool-based RAG** in class — same idea.

![Standalone RAG vs Agentic RAG — yesterday always retrieved; today the agent chooses retriever tool, auxiliary tool, both, or a guarded direct reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-01-standalone-vs-agentic-rag.png)

---

## Tool Arbitration — Choosing the Right Tool

Tool arbitration is the **bridge** between having multiple capabilities and using the **right** one per question.

- **Official Definition:** **Tool arbitration** is the agent's ability to **choose the correct tool** (or no tool) for a user query based on tool names, descriptions, and prompt rules.
- **In Simple Words:** The model reads **menu cards** for each tool and picks the dish that matches the order.
- **Real-Life Example:** At **Swiggy support**, *"Where is my order?"* goes to **tracking**, not the **refund policy PDF**.

**Why tool descriptions matter:**

- Vague descriptions → wrong tool calls even when code is correct.
- A good description answers:
  - **What** does this tool do?
  - **When** should the agent call it?
  - **What user need** does it fulfil?

**Routing examples from class (course support bot):**

| User query | Expected action | Why |
|---|---|---|
| *"What is the refund policy?"* | **`course_policy_tool`** (retriever) | Answer lives in **policy documents** |
| *"What is my ticket status?"* | **`get_ticket_status`** | Live **ticket record**, not a policy paragraph |
| *"What is the status of my refund ticket?"* | **Possibly both** | Status from ticket DB; extra **refund rules** from policy if status is rejected |
| *"Who won IPL 2025?"* | **No tool / out-of-domain refusal** | Not in corpus; guardrails should **block** general LLM trivia (like asking DSA on a McDonald's bot) |

- **Wrong tool** often starts with a weak description — fix the **contract** before retraining anything.
- **Out-of-domain refusal** is honest limits: refuse cleanly instead of inventing or saying *"I cannot help with anything."*

![Tool arbitration — the agent reads each tool's contract and routes refund questions to course_policy_tool, ticket IDs to get_ticket_status, combined needs to both, and trivia to polite refusal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-02-tool-arbitration.png)

### Quick Activity — Pick the Tool

For each query, write which tool should run: **`course_policy_tool`**, **`get_ticket_status`**, **both**, or **neither**.

1. *"Can I miss three classes and still change my batch?"*  
2. *"Status of ticket TKT-1002?"*  
3. *"What is the capital of France?"*

**Suggested answers:** 1 → `course_policy_tool`, 2 → `get_ticket_status`, 3 → neither (polite out-of-domain refusal).

---

## The Course Support Agent — What You Build

The live demo is a **student course support assistant** inside the **`langchain_apps`** folder (same project tree as earlier LangChain labs).

**Two tools:**

| Tool | Type | Job |
|---|---|---|
| **`course_policy_tool`** | Retriever-backed (`create_retriever_tool`) | Search **official course policies** — refund, attendance, batch change, project submission, career services |
| **`get_ticket_status`** | Auxiliary `@tool` | Return **support ticket status** from a **fake in-memory ticket database** |

![Course support agent architecture — ragagent.py binds course_policy_tool and get_ticket_status to AgentExecutor with chat_history and max_iterations=3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-03-course-support-agent.png)

**Policy corpus (five inline documents in code):**

- Career services policy  
- Batch change policy  
- Project submission policy  
- Attendance policy  
- Refund policy  

**Ingest path (inside `ragagent.py`):**

1. Build **`Document`** objects with optional **`metadata`** (e.g. `source`).  
2. **`RecursiveCharacterTextSplitter`** — demo used small docs; chunk size ~500, overlap ~50–80.  
3. **`OpenAIEmbeddings`** with **`text-embedding-3-small`** (same family as the previous RAG lab).  
4. **`Chroma.from_documents`** with collection name **`course_policy_docs`**.  
5. **`vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})`**.

- **Metadata** can hold `source`, `last_updated`, `doc_type` — useful later for filtering; demo used at least **`source`**.

![Ingest path inside ragagent.py — inline documents, splitter, OpenAI embeddings, Chroma collection, retriever, then create_retriever_tool](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-04-ingest-to-retriever-tool.png)

---

## Full Code — `ragagent.py`

Save this as **`ragagent.py`** in your LangChain apps folder. Set **`OPENAI_API_KEY`** before running.

```python
import os  # Read API key from environment

from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # LLM + embeddings
from langchain_core.documents import Document  # Policy text + metadata wrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Agent prompt layout
from langchain_core.messages import HumanMessage, AIMessage  # Chat history message types
from langchain_core.tools import tool  # Decorator for auxiliary tools
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Chunk long policies
from langchain_chroma import Chroma  # Vector store for policy search
from langchain.tools.retriever import create_retriever_tool  # Wrap retriever as agent tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # Agent loop

# --- 1. Inline policy corpus (five small course policy documents) ---
RAW_DOCUMENTS = [
    Document(
        page_content=(
            "Career services policy: Placement support requires minimum 75% attendance "
            "and completion of all mandatory projects. Resume reviews are available weekly."
        ),
        metadata={"source": "career_services_policy.md"},
    ),
    Document(
        page_content=(
            "Batch change policy: Students may request one batch change per cohort. "
            "Approval depends on seat availability. Missing more than three classes "
            "without approved leave may delay batch change."
        ),
        metadata={"source": "batch_change_policy.md"},
    ),
    Document(
        page_content=(
            "Project submission policy: All capstone milestones must be submitted "
            "before the deadline. Late submissions lose 10% per day up to three days."
        ),
        metadata={"source": "project_submission_policy.md"},
    ),
    Document(
        page_content=(
            "Attendance policy: Minimum 75% attendance is required for certification. "
            "Placement support requires the same threshold."
        ),
        metadata={"source": "attendance_policy.md"},
    ),
    Document(
        page_content=(
            "Refund policy: Full refund within 7 days of enrollment if no live class attended. "
            "Partial refund within 30 days per program rules. After 30 days, refunds are not available."
        ),
        metadata={"source": "refund_policy.md"},
    ),
]

# --- 2. Chunk documents (small corpus — tuning still shown for habit) ---
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Max characters per chunk
    chunk_overlap=80,  # Overlap so sentences at boundaries are not lost
)
split_documents = text_splitter.split_documents(RAW_DOCUMENTS)  # List of chunked Document objects

# --- 3. Embed and store in Chroma ---
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # Same embedding family as prior RAG lab

vectorstore = Chroma.from_documents(
    documents=split_documents,  # Chunked policies to index
    embedding=embeddings,  # Embedding function for store + query
    collection_name="course_policy_docs",  # Separate collection from e-commerce demo
)

retriever = vectorstore.as_retriever(
    search_type="similarity",  # Semantic nearest-neighbour search
    search_kwargs={"k": 3},  # Top 3 chunks per policy question
)

# --- 4. Retriever-backed tool (Button A — policy library) ---
course_policy_tool = create_retriever_tool(
    retriever=retriever,  # Existing retriever from Chroma
    name="course_policy_tool",  # Short, clear tool name for the LLM
    description=(
        "Searches official course policy documents for refund rules, attendance requirements, "
        "batch change policy, project submission deadlines, and career services rules. "
        "Use when the user asks about official course policies or program rules."
    ),
)

# --- 5. Auxiliary tool (Button B — ticket desk) ---
FAKE_TICKET_DATABASE = {
    "TKT-1001": "Refund request under review. Expected response in 2 working days.",
    "TKT-1002": "Batch change request approved. New batch starts next Monday.",
    "TKT-51001": "Refund request under review. Expected response in 2 working days.",
    "TKT-9001": "Technical issue ticket closed. Solution emailed to student.",
}

@tool
def get_ticket_status(ticket_id: str) -> str:
    """Returns support ticket status for the given ticket ID.

    Use this tool when the user asks about ticket status, refund request status,
    or support ticket progress for a specific ticket ID.
    """
    ticket_status = FAKE_TICKET_DATABASE.get(ticket_id)  # Lookup in fake DB
    if not ticket_status:  # Unknown ticket ID
        return f"Ticket status not found for ticket ID {ticket_id}."
    return ticket_status  # Return status string to the agent

tools = [course_policy_tool, get_ticket_status]  # Both tools bound to the agent

# --- 6. LLM ---
llm = ChatOpenAI(
    model="gpt-4o-mini",  # Demo used a recent GPT model; pick one your key supports
    temperature=0,  # Factual routing and policy answers
)

# --- 7. Prompt — memory + scratchpad + routing rules ---
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        (
            "You are a helpful course support assistant. "
            "You have access to two tools: course_policy_tool and get_ticket_status. "
            "If the question is about official course policy, use course_policy_tool. "
            "If the question is about ticket status for a given ticket ID, use get_ticket_status. "
            "If the question needs both policy and ticket status, you may use both tools. "
            "If the user gives a ticket ID in an earlier message and asks for status later, "
            "use chat history to find the ticket ID. "
            "If the question is outside course support, politely say you can only help with "
            "course policies and support tickets. "
            "When answering from documents, mention that the answer is based on available policy documents. "
            "Keep answers clear and student-friendly."
        ),
    ),
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # Past turns — you maintain this list
    ("human", "{input}"),  # Current user message
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # Tool steps for this run — filled by executor
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)  # Tool-calling agent graph

agent_executor = AgentExecutor(
    agent=agent,  # Compiled agent
    tools=tools,  # Same tool list (required by executor)
    verbose=True,  # Print tool calls in terminal — great for debugging
    max_iterations=3,  # Stop after 3 tool loops — prevents runaway agents
)

chat_history = []  # Starts empty; grows across ask_agent calls

def ask_agent(user_query: str) -> str:
    """Send one user message to the agent and append the turn to chat_history."""
    response = agent_executor.invoke({
        "input": user_query,  # Current question
        "chat_history": chat_history,  # All prior HumanMessage / AIMessage objects
    })
    answer = response["output"]  # Final natural-language reply

    chat_history.append(HumanMessage(content=user_query))  # Record what user asked
    chat_history.append(AIMessage(content=answer))  # Record what agent answered
    return answer

# --- 8. Compact EvalPack — small fixed test set ---
EVAL_CASES = [
    {
        "name": "refund_policy",
        "input": "What is the refund policy within the first week?",
        "expected_tool": "course_policy_tool",
        "expected_keywords": ["7 days", "refund", "30 days"],
        "failure_type": "weak_retriever_or_missing_retrieval",
    },
    {
        "name": "ticket_status",
        "input": "What is the status of ticket TKT-51001?",
        "expected_tool": "get_ticket_status",
        "expected_keywords": ["review", "working days"],
        "failure_type": "wrong_tool",
    },
    {
        "name": "batch_change_policy",
        "input": "Can I change my batch if I missed three classes?",
        "expected_tool": "course_policy_tool",
        "expected_keywords": ["batch", "class"],
        "failure_type": "weak_retriever_or_missing_retrieval",
    },
    {
        "name": "out_of_domain",
        "input": "Who won IPL 2025?",
        "expected_tool": None,
        "expected_keywords": ["course", "policy", "ticket", "help"],
        "failure_type": "should_refuse_out_of_domain",
    },
]

def run_eval_pack():
    """Run each EvalPack case and print name, input, expected tool, and agent output."""
    for case in EVAL_CASES:
        print("=" * 60)
        print("Test case:", case["name"])
        print("Input:", case["input"])
        print("Expected tool:", case["expected_tool"])
        output = ask_agent(case["input"])
        print("Agent output:", output)
        print("Expected keywords (check manually):", case["expected_keywords"])
        print("Likely failure if bad:", case["failure_type"])
        print()

if __name__ == "__main__":
    # --- Manual demo queries (same flow as live class) ---
    query_1 = "What is the refund policy?"
    print("User:", query_1)
    print("AI:", ask_agent(query_1))
    print()

    query_2 = "What is the status of ticket TKT-51001?"
    print("User:", query_2)
    print("AI:", ask_agent(query_2))
    print()

    # Multi-tool single query — ticket status + refund policy in one message
    query_3 = (
        "What is the status of my ticket TKT-1002? "
        "Also tell me the refund policy."
    )
    print("User:", query_3)
    print("AI:", ask_agent(query_3))
    print()

    # Uncomment to run the full EvalPack after manual demos:
    # chat_history.clear()
    # run_eval_pack()
```

**How the code works:**

- **Steps 1–3** repeat the RAG **prepare** path from the previous lab — but inside one agent file with a **course** corpus.  
- **`create_retriever_tool`** turns **`retriever`** into **`course_policy_tool`** — the agent sees it like **`get_ticket_status`**.  
- **`@tool` + docstring** is the **contract** for the ticket tool — the LLM reads that text when arbitrating.  
- **`chat_history`** is **manual** — without append after **`invoke`**, turn 2 forgets the ticket ID.  
- **`agent_scratchpad`** is **automatic** — tracks tool calls **within** one **`ask_agent`** call.  
- **`max_iterations=3`** caps tool loops — same safety idea as earlier agent labs.  
- **`EVAL_CASES`** is your **bounded evaluation** — name, input, expected tool, keywords, failure hint.

**Run:**

```bash
export OPENAI_API_KEY="your-key-here"
python3 ragagent.py
```

---

## Live Demo Walkthrough — What You Should See

When **`verbose=True`**, the terminal shows **which tool fired**.

**Query 1 — refund policy (retrieval / in-domain):**

- User: *"What is the refund policy?"*  
- Agent invokes **`course_policy_tool`**.  
- Answer mentions **7-day / 30-day** style rules from retrieved chunks.  
- Phrasing like *"based on available policy documents"* matches the system prompt.

**Query 2 — ticket status (tool-first):**

- User: *"What is the status of ticket TKT-51001?"*  
- Agent invokes **`get_ticket_status`**.  
- Output includes **review** and **working days** from the fake DB — not a policy search.

**Query 3 — multi-tool in one turn:**

- User: *"What is the status of my ticket TKT-1002? Also tell me the refund policy."*  
- Agent should call **`get_ticket_status`** first, then **`course_policy_tool`**.  
- Final answer combines **batch change approved** with **refund rules**.

- **Multi-tool** = two tools in **one** user message.  
- **Multi-turn** = **several** messages where later turns use **`chat_history`** (e.g. ticket ID in turn 1, *"What is the status?"* in turn 2).

![Live demo query patterns — refund policy triggers course_policy_tool, ticket status triggers get_ticket_status, combined query runs both tools in one turn](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-06-live-demo-queries.png)

### Simple Activity — Read the Trace

Run **Query 1** with **`verbose=True`**. In your notebook, answer:

1. Which tool name appears in the trace?  
2. Does the final answer cite policy documents?  
3. If you renamed the tool to `search_stuff` with a vague description, would arbitration get harder?

---

## Memory, Multi-Turn Q&A, and Scratchpad

Memory connects **this** session to the **agent + history** work you did earlier — but now retrieval can run on later turns too.

- **Official Definition:** **Multi-turn document Q&A** keeps **`chat_history`** across invocations so follow-ups can reuse entities (ticket IDs, topics) and still call **retrieval tools** when needed.
- **In Simple Words:** The desk **remembers the notepad** and can still open the **policy file** on turn 3.
- **Real-Life Example:** Turn 1: *"My ticket is TKT-1002."* Turn 2: *"What is its status?"* — memory supplies **TKT-1002**; **`get_ticket_status`** supplies live status.

**`chat_history` vs `agent_scratchpad` (quick recap):**

| | **chat_history** | **agent_scratchpad** |
|---|---|---|
| Holds | Past **user ↔ assistant** messages | **Current run** tool inputs/outputs |
| You maintain? | **Yes** (append after each `ask_agent`) | **No** — executor fills it |
| Needed for | *"Status of it?"* without repeating ID | Multi-step tool use in **one** query |

- **Without `agent_scratchpad`**, tool-calling agents **cannot track** tool steps reliably inside one run.  
- **Without appending `chat_history`**, the placeholder exists but stays **empty** — classic bug from earlier memory labs.

![chat_history vs agent_scratchpad — you maintain past turns manually; the executor fills tool steps for the current run only](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-05-chat-history-vs-scratchpad.png)

### Simple Activity — Two-Turn Memory

After running Query 1 and Query 2 above, add a third call **without clearing history**:

```python
query_4 = "What is the status of it?"  # Deliberately omit ticket ID — only works if turn 2 mentioned TKT-51001
print("User:", query_4)
print("AI:", ask_agent(query_4))
```

Note whether the agent uses **`chat_history`** to recover **TKT-51001**. If it asks for the ID again, check that **`chat_history.append`** runs after every turn.

---

## EvalPack — Bounded Evaluation

An **EvalPack** is a **small, fixed set of test cases** used to validate **integrated agent behaviour** — not a one-off demo that always looks fine.

- **Official Definition:** A **compact evaluation pack** is a list of scripted inputs with **expected tools**, **expected answer keywords**, and **failure type labels** for regression testing.
- **In Simple Words:** A **exam paper** with ten predictable questions you run after every code change.
- **Real-Life Example:** Before releasing a **BYJU'S** or **upGrad** support bot, QA runs the same refund, ticket, and nonsense questions every build.

**Scenario types in the cohort pack:**

| Scenario | What it tests | Example from class |
|---|---|---|
| **In-domain** | Should retrieve and ground in policies | Refund policy question → **`course_policy_tool`** |
| **Tool-first** | Should call auxiliary tool, not RAG | Ticket status → **`get_ticket_status`** |
| **Out-of-domain** | Should refuse, not hallucinate | *"Who won IPL 2025?"* → no tool; polite limit |
| **Multi-turn** | Memory + correct tool on later turn | Ticket ID then *"status of it?"* |

**Each EvalPack row typically has:**

- **`name`** — test label  
- **`input`** — user query  
- **`expected_tool`** — which tool should appear in the trace  
- **`expected_keywords`** — substrings that should appear in a good answer (e.g. **7 days**, **refund**, **30 days**)  
- **`failure_type`** — what went wrong if the case fails (e.g. **weak_retriever_or_missing_retrieval**)

**Running the pack:**

- Loop **`for case in EVAL_CASES`**, print case name, call **`ask_agent(case["input"])`**, compare output.  
- **Post-lab improvement:** assert **`expected_keywords`** appear in output and parse **`verbose`** logs for **`expected_tool`**.

- Live class executed cases **one by one** in order — same pattern as **`run_eval_pack()`** above.  
- **Out-of-domain** was taught strongly in the **arbitration** section; add it to your pack even if you only ran policy + ticket cases live.

![EvalPack scenario types — in-domain retrieval, tool-first ticket lookup, out-of-domain refusal, and multi-turn memory cases with expected tools and keywords](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-07-evalpack-scenarios.png)

### Simple Activity — Extend One Eval Case

Add a row where the user asks for **both** ticket status and refund rules in **one** sentence. Set **`expected_tool`** to **both** tools (or note *"two tool calls"* in remarks). Run it and check the trace.

---

## Failure Signatures — What Broke and What to Fix First

When the EvalPack fails, the **failure signature** tells you **which knob to turn** — not random prompt edits.

![Failure signatures — wrong tool, weak retrieval, over-refusal, and missing memory each map to a prioritized first fix](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session41/session41-08-failure-signatures.png)

### 1. Wrong tool call

- **Symptom:** Policy question triggers **`get_ticket_status`**, or ticket question searches policies.  
- **Likely cause:** Vague tool names/descriptions or conflicting prompt rules.  
- **Fix first:** **Improve tool descriptions** → **re-read system prompt** for contradictory instructions.  
- **Eval link:** **`failure_type: wrong_tool`** on ticket-status cases.

### 2. Weak retrieval

- **Symptom:** Right tool fires but answer uses **wrong policy chunk** (batch change text for a refund question) or irrelevant passages.  
- **Likely cause:** Chunking, embeddings, or search config — not memory.  
- **Fix options (in order of class discussion):**  
  - **`chunk_size` too large or too small**  
  - **`chunk_overlap` too low**  
  - **`k` too low** — increase top-k  
  - **`search_type`** — try **MMR** if similarity alone returns near-duplicates  
  - Re-check **embedding model** matches ingest vs query  
- **Eval link:** **`weak_retriever_or_missing_retrieval`** on refund-policy case.

### 3. Over-refusal

- **Symptom:** Agent says *"I cannot help"* when the policy **does** cover the topic (e.g. attendance for placement).  
- **Likely cause:** **Too strict** system prompt or tool description that discourages retrieval.  
- **Fix first:** Loosen refusal wording; ensure **`course_policy_tool`** description lists the topic.  
- **Real-Life Example:** Clerk refuses to open the rulebook even though the answer is on **page 4**.

### 4. Missing memory

- **Symptom:** Turn 2 forgets ticket ID or topic from turn 1.  
- **Likely cause:** **`chat_history` not appended** or wrong placeholder variable name.  
- **Fix first:** Append **`HumanMessage`** + **`AIMessage`** after every **`invoke`**; pass the **same list** next time.  
- **Production note:** Persist **`chat_history`** to a **database** for real bots — RAM-only lists reset on restart.

| Failure signature | First fix to try |
|---|---|
| Wrong tool | Tool description + prompt rules |
| Weak retrieval | Chunk size / overlap / k / search type |
| Over-refusal | Relax strict prompt; clarify tool when-to-use |
| Missing memory | Append `chat_history`; verify placeholder name |

---

## Agentic RAG vs Standalone RAG — When the Wrapper Helps

- **Standalone LCEL RAG** is ideal when **every** question should hit the vector index — simple, predictable, fewer moving parts.  
- **Integrated agent** is ideal when **support** needs **policy search + ticket lookup + memory + refusal** in one product shape.  
- **Trade-off:** Agents add **arbitration risk** — each tool needs a clear contract and an **EvalPack**.  
- **Upcoming work** on **multi-agent collaboration** and **deployment** builds on this single-agent shape.

---

## Common Mistakes and Fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| `OpenAI API key` error | Key not exported | `export OPENAI_API_KEY=...` before `python3 ragagent.py` |
| Agent never calls retriever | Vague `course_policy_tool` description | Rewrite **when to use** lines; add policy examples |
| Ticket tool not called | Ticket ID format mismatch | Align user wording with keys in **`FAKE_TICKET_DATABASE`** |
| Turn 2 asks for ticket ID again | History not appended | Fix **`ask_agent`** append block |
| Infinite tool loop | No iteration cap | Set **`max_iterations`** on **`AgentExecutor`** |
| Eval always passes manually but fails in pack | Different `chat_history` state | **`chat_history.clear()`** before **`run_eval_pack()`** |

---

## Key Takeaways

- **Agentic RAG** lets an agent **choose** retrieval, auxiliary tools, both, or a guarded direct reply — unlike a chain that **always** retrieves.  
- **`create_retriever_tool`** exposes your Chroma **retriever** as **`course_policy_tool`** with a strong **name + description** for **tool arbitration**.  
- **`get_ticket_status`** proves **non-retrieval tools** can sit beside RAG in one **`AgentExecutor`** workflow.  
- **`chat_history`** and **`agent_scratchpad`** solve different problems — past turns vs current tool trace.  
- An **EvalPack** with **in-domain**, **tool-first**, and **out-of-domain** cases plus **failure signatures** turns debugging into **prioritised fixes**, not guesswork.  
- This integrated pattern is the foundation for **multi-agent** and **deployment** topics ahead — memory, retrieval, tools, and tests in one place.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `ragagent.py` | File | Course support agent — ingest, tools, memory, eval |
| `create_retriever_tool` | Function | Wrap a retriever as a LangChain agent tool |
| `course_policy_tool` | Tool | Retriever-backed search over course policy Chroma index |
| `get_ticket_status` | Tool | Auxiliary ticket lookup (fake DB in demo) |
| **Tool arbitration** | Concept | Agent picks the right tool per query |
| **Agentic RAG** | Concept | RAG retrieval exposed as a tool inside an agent |
| `AgentExecutor` | Class | Runs tool-calling loop with limits and verbose logging |
| `create_tool_calling_agent` | Function | Builds agent graph bound to tools + prompt |
| `MessagesPlaceholder` | Class | Slot for `chat_history` or `agent_scratchpad` |
| `chat_history` | Variable | List of past `HumanMessage` / `AIMessage` turns |
| `agent_scratchpad` | Placeholder | Tool steps for the **current** invocation |
| `max_iterations` | Param | Cap tool loops per user message |
| `verbose=True` | Param | Print tool calls — essential for debugging |
| `ask_agent()` | Function | Invoke executor + append history |
| **EvalPack** | Concept | Compact scripted tests with expected tools/keywords |
| **In-domain** | Eval type | Question answerable from corpus/tools |
| **Out-of-domain** | Eval type | Should refuse — e.g. IPL trivia on course bot |
| **Tool-first** | Eval type | Auxiliary tool before or instead of retrieval |
| **Wrong tool** | Failure signature | Incorrect tool selected |
| **Weak retrieval** | Failure signature | Right tool, poor chunks |
| **Over-refusal** | Failure signature | Refuses when answer exists in corpus |
| `Chroma.from_documents` | Method | Embed + store policy chunks |
| `text-embedding-3-small` | Model | OpenAI embeddings used in demo |
| `search_kwargs={"k": 3}` | Config | Top 3 chunks per retrieval |
| `export OPENAI_API_KEY=...` | Shell | Authenticate OpenAI calls |
| `python3 ragagent.py` | Command | Run demo queries and optional EvalPack |
