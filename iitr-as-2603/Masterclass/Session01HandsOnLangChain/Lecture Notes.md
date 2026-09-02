# Hands-On LangChain

## Context of This Session

In **previous** work you orchestrated agents as **graphs**: **nodes**, **edges**, **shared state**, **checkpoints**, and **retries**. You also built **RAG** on **Chroma**, called **Groq**, and practised **golden questions** before changing a prompt. That stack answers: *what ran, in which order, and did quality drop?*

Those graphs still need **reusable pieces** underneath — prompts, model wrappers, parsers, tools, and retrievers. **LangChain** is the toolkit that supplies those pieces. Today you learn it as a first-class library, then ship **one end-to-end app** in a single file.

**What you will learn:**

- **Define** LangChain and name its core building blocks
- **Contrast** LangChain with **LangGraph** — advantages, limits, and when each fits
- **Compose** an **LCEL** chain: `prompt | ChatGroq | StrOutputParser`
- **Build** a **T20 Rules & Match Inquiry Assistant** — RAG tool, live incident tool, memory, refusal
- **Measure** behaviour with a compact **EvalPack** and one controlled patch

---

## What Is LangChain

LangChain is a **Python library** for assembling LLM applications from **named, reusable blocks** instead of one-off API calls.

- **Official Definition:** **LangChain** is an open-source framework that provides **Runnables** (prompts, models, parsers, tools, retrievers) and a pipe operator (**LCEL**) so you can compose chat, RAG, and tool-calling agents as standard objects.
- **In Simple Words:** A **parts catalogue** for LLM apps — prompt, model, parser, tool — that snap together.
- **Real-Life Example:** A **hardware store** sells standardised pipes and valves. You still design the plumbing; you do not forge every joint from scrap metal.

You already know the *ideas*: prompt, Groq call, retrieve, tool. LangChain’s job is to make those ideas **objects you can reuse, test, and swap**.

| Block | Job in an app |
|---|---|
| **`ChatPromptTemplate`** | Reusable prompt with `{variables}` |
| **`ChatGroq`** | Same Groq model, wrapped as a LangChain chat model |
| **`StrOutputParser`** | Turn the model reply into plain text |
| **`@tool`** | Register a Python function the agent may call |
| **Retriever / Chroma** | Search *your* documents, not only training data |
| **`AgentExecutor`** | Run the tool loop with limits (`max_iterations`) |

- **Common mistake:** Treating LangChain as “a new chatbot.” It is **infrastructure**. The chatbot is what you *build* with it.
- **Common doubt:** *“Did we not already call Groq?”* Yes. Today Groq is one **block** inside a chain or agent, not a lone `client.chat.completions` call.

---

## LangChain and LangGraph — How They Differ

You already treat **LangGraph** as a **workflow map**. LangChain is not a replacement map. It is the **kit of blocks** that often sit *inside* those stations — or, for a single agent, *instead of* drawing a graph.

![LangChain versus LangGraph — pipeline of reusable blocks compared with a node-and-edge workflow and shared state](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session01-hands-on-langchain/session01-01-langchain-vs-langgraph.png)

- **Official Definition:** **LangGraph** is a library for **stateful multi-step workflows** (nodes, edges, checkpoints). **LangChain** is a library for **composing LLM primitives** (chains, tools, retrievers, agents).
- **In Simple Words:** LangGraph is the **workflow graph**. LangChain is the **set of blocks** each node may use.
- **Real-Life Example:** IRCTC’s **route map** (which station after which) is the graph. The **ticket printer, fare table, and ID scanner** at each counter are the LangChain-style tools.

| | **LangChain** | **LangGraph** |
|---|---|---|
| Core picture | Chain / agent of reusable blocks | Map of nodes + shared state |
| Best at | Prompts, LCEL, tools, RAG, one agent loop | Branching, resume, human gates, long jobs |
| Control | Pipe (`\|`) and `AgentExecutor` | Edges you draw; checkpoints you save |
| Memory | `chat_history` you append | Graph **state** the runtime persists |
| Typical “hello world” | `prompt \| llm \| parser` | `START → node_a → node_b → END` |

**Connecting idea:** A campus appointment flow with understand → check → confirm *and* a save-file is a **graph** job. A help desk that picks **rulebook search** or **incident lookup** in one loop is a **LangChain agent** job. Many production systems use **both**.

LangChain does **not** erase what you learned. Checkpoints, timeouts, and visible branches stay on the graph. Today you add the **standard parts** those graphs (or a single agent) actually call.

### Advantages of LangChain

- **Speed to a working agent** — templates, parsers, `@tool`, and `AgentExecutor` are already wired.
- **Swappable blocks** — change Groq model or prompt without rewriting the loop.
- **RAG as a tool** — `create_retriever_tool` turns Chroma search into something the agent can *choose*.
- **Ecosystem** — loaders, splitters, and vector stores share one style.

### Disadvantages of LangChain

- **Hidden control flow** — `AgentExecutor` is convenient; a graph makes every branch visible.
- **Version drift** — import paths change across package splits (`langchain-core`, `langchain-classic`). Pin what the lab uses.
- **Not a substitute for checkpoints** — long jobs that must **resume after crash** still belong on a graph.
- **Overkill for one Groq call** — a three-line API script does not need a chain.

### When to pick which

| Situation | Prefer |
|---|---|
| One chain or one tool-calling help desk | **LangChain** |
| Conditional routes, pause/resume, human stamp | **LangGraph** |
| Stations that each need a prompt + retriever | **Both** — graph outside, LangChain inside nodes |

### Real-life applications of LangChain

- **Bank / UPI help desk** — FAQ retriever + transaction-status tool + memory of the TXN id.
- **Campus policy bot** — search the handbook; refuse out-of-scope gossip.
- **Broadcast / sports desk** — search playing conditions; look up a match incident id (today’s app).
- **Internal IT assistant** — retrieve runbooks; call a ticket-status function.

You are not replacing LangGraph. You are adding the **standard parts library** next to the **orchestration map** you already have.

### Activity — Label the job

For each need, write **LangChain**, **LangGraph**, or **both**:

| Need | Your label |
|---|---|
| Swap the prompt without rewriting the Groq call | |
| Resume a half-finished letter after the laptop sleeps | |
| Let the model choose FAQ search vs ticket-id lookup | |
| Stations extract → policy → route, each station uses a prompt template | |

**Suggested answers:** LangChain · LangGraph · LangChain · both

---

## What You Will Build — T20 Rules & Match Inquiry Assistant

The framework is defined. Now you apply it as **one product**, not seven notebooks.

![T20 Rules Assistant architecture — user question into AgentExecutor, then rulebook RAG, incident lookup, or refusal, with conversation history and current-run trace](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session01-hands-on-langchain/session01-02-t20-assistant-architecture.png)

| Part of the app | Real-life role | LangChain piece |
|---|---|---|
| **T20 rulebook search** | Playing-conditions handbook | **RAG** via `t20_rules_search_tool` |
| **Match incident lookup** | Scorer’s log for `INC-…` | **`@tool`** → `get_match_incident` |
| **Multi-turn chat** | Follow-ups without repeating the id | **`chat_history`** |
| **Safety** | Refuse auction trivia / FIFA | System prompt + **tool arbitration** |

- **Official Definition:** An **integrated LangChain agent** combines retrieval, custom tools, conversational memory, and bounded execution in one runnable app.
- **In Simple Words:** One help desk that can open the **rulebook** or the **match log** — and remembers the last incident id.
- **Real-Life Example:** A broadcast analyst opens the **conditions PDF** for powerplay *and* the **live incident feed** for over 12.3.

> Rule text and incident records here are **teaching samples**, not official ICC documents.

Everything lives in **`t20_rules_assistant.py`**.

| Phase | Focus | What you prove |
|---|---|---|
| **1 — Warm-up** | `demo_lcel_chain()` | `prompt \| llm \| parser` on Groq |
| **2 — Build** | ingest → tools → agent → `ask()` | Full end-to-end app |
| **3 — Eval** | `run_eval()` | Keywords, expected tool, one patch |

```text
langchain_hands_on/
├── venv/
└── t20_rules_assistant.py
```

---

## LCEL — The Pipe Pattern

Before the agent, prove the smallest LangChain idea: **LCEL**.

- **Official Definition:** **LCEL** (LangChain Expression Language) composes **Runnables** with **`|`** so each step’s output becomes the next step’s input.
- **In Simple Words:** A **filter coffee** chain — water → powder → filter → cup. Same pipe, different beans.
- **Real-Life Example:** UPI rail — phone → bank app → switch → merchant. Each hop forwards a payload.

![LCEL pipeline — user topic, prompt template, ChatGroq, string parser, then plain text answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session01-hands-on-langchain/session01-03-lcel-pipe.png)

```text
ChatPromptTemplate → ChatGroq → StrOutputParser → string
```

If Phase 1 prints a short free-hit explanation, your **key**, **packages**, and **pipe** are healthy. Only then build the agent.

A **Runnable** is anything that supports `.invoke()` (and often `.stream()`). Prompts, chat models, and parsers are Runnables, so the pipe is legal.

- **Official Definition:** A **Runnable** is LangChain’s common interface: input in, output out, same `.invoke` habit.
- **In Simple Words:** Every block speaks the same language — like every charger using the same USB-C port.
- **Real-Life Example:** A **metro smart card** works at every gate. You do not learn a new swipe for each station.
- **Common mistake:** Calling Groq *outside* the pipe and then wondering why `StrOutputParser` never ran.

### Activity — Swap the Topic

In `demo_lcel_chain()`, change the invoke topic to **`"wide ball rules in T20"`**. The chain code stays identical. That is **composability**.

---

## Before You Start — Setup

Reuse **Python 3**, a **venv**, and the same **`GROQ_API_KEY`** habit from earlier Groq labs. Embeddings are **local MiniLM** — no extra embedding API.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core langchain-groq langchain-chroma langchain-text-splitters langchain-classic langchain-community sentence-transformers
export GROQ_API_KEY="your_key_here"
```

Create **`t20_rules_assistant.py`**, paste the file below, then run phases in order.

| Package | Why this app needs it |
|---|---|
| **`langchain-core`** | Prompts, messages, documents, parsers, `@tool` |
| **`langchain-groq`** | `ChatGroq` — Groq as a Runnable |
| **`langchain-chroma`** | Chroma vector store for the rulebook |
| **`langchain-text-splitters`** | `RecursiveCharacterTextSplitter` |
| **`langchain-classic`** | `AgentExecutor`, `create_tool_calling_agent` (also pulls `langchain` for `create_retriever_tool`) |
| **`langchain-community`** | `HuggingFaceEmbeddings` (same MiniLM family as earlier RAG) |
| **`sentence-transformers`** | Downloads and runs `all-MiniLM-L6-v2` locally |

Keep the key in the environment. Never paste it into the file.

---

## The Complete App — `t20_rules_assistant.py`

```python
# T20 Rules & Match Inquiry Assistant — Hands-On LangChain (one file, three phases)
import os  # Read GROQ_API_KEY from the environment; never hard-code the secret
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Prompt layout plus history and scratchpad slots
from langchain_core.output_parsers import StrOutputParser  # Convert the Phase 1 model reply into a plain string
from langchain_core.documents import Document  # Wrap each T20 rule paragraph so the splitter and Chroma can ingest it
from langchain_core.messages import HumanMessage, AIMessage  # Append user and assistant turns to chat_history
from langchain_core.tools import tool  # Decorator that registers get_match_incident as a structured agent tool
from langchain_groq import ChatGroq  # Groq chat model, same backend as earlier labs, now a LangChain Runnable
from langchain_community.embeddings import HuggingFaceEmbeddings  # Local MiniLM vectors, same family as earlier RAG labs
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Split long rule text into small searchable chunks
from langchain_chroma import Chroma  # Local vector store for rulebook similarity search
from langchain.tools.retriever import create_retriever_tool  # Expose the Chroma retriever as an agent-selectable tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # Managed tool-calling loop with limits

if not os.environ.get("GROQ_API_KEY"):  # Fail fast if the secret is missing
    raise RuntimeError("Set GROQ_API_KEY in the environment before running.")  # Do not start ingest or the agent without a key


def demo_lcel_chain() -> None:
    """Phase 1: prompt | llm | parser. Proves Groq + LCEL before the agent starts."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a cricket rules explainer. Answer in 2 sentences max."),
        ("human", "Explain {topic} in simple words."),
    ])  # Template with a {topic} slot — same chain, different questions
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)  # Classroom Groq model; switch if rate-limited
    chain = prompt | llm | StrOutputParser()  # LCEL pipe: prompt output feeds the model, model output feeds the parser
    print("Phase 1 — LCEL warm-up:\n", chain.invoke({"topic": "what is a free hit in T20"}))  # One invoke proves the stack


T20_RULE_DOCS = [  # Inline teaching corpus — production would load PDFs instead
    Document(page_content="Powerplay rules (T20): Mandatory powerplay covers overs 1 to 6. A maximum of 2 fielders may be positioned outside the 30-yard circle during powerplay."),  # Rule chunk: fielding limits in overs 1–6
    Document(page_content="Free hit rules: After a no-ball is called, the next legal delivery is a free hit. On a free hit the batter can only be dismissed run out, hit the ball twice, or obstruct the field."),  # Rule chunk: dismissal limits on a free hit
    Document(page_content="No-ball rules: Front-foot no-ball if the bowler's front foot lands beyond the popping crease. A no-ball adds one run and the next ball is a free hit in T20."),  # Rule chunk: no-ball plus free-hit consequence
    Document(page_content="Wide ball rules: A wide is called if the ball passes wide of the batter without being touched. A wide adds one run."),  # Rule chunk: wide extras
    Document(page_content="DRS rules (T20): Each team receives 2 unsuccessful player reviews per innings."),  # Rule chunk: review quota
    Document(page_content="Dead ball rules: The umpire may call dead ball for a dangerous delivery or serious distraction. No run is scored on that delivery unless already completed."),  # Rule chunk: dead-ball conditions
    Document(page_content="Penalty runs (T20): After a warning, the umpire may award 5 penalty runs to the batting side if the bowler runs on the protected area of the pitch."),  # Grounds Q3 follow-up on INC-101
]

_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)  # Small chunks so retrieval hits one rule, not the whole book
_rule_chunks = _splitter.split_documents(T20_RULE_DOCS)  # Split each Document into overlapping pieces
_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Local embeddings; no extra API key
_vectorstore = Chroma.from_documents(documents=_rule_chunks, embedding=_embeddings, collection_name="t20_rules_demo")  # Build the in-memory rule index
_retriever = _vectorstore.as_retriever(search_kwargs={"k": 2})  # Return the top 2 most similar chunks at query time
t20_rules_search_tool = create_retriever_tool(
    _retriever,
    name="t20_rules_search_tool",
    description="Search official T20 playing rules. Use for powerplay, free hit, no-ball, wide, dead ball, DRS. Do NOT use for live match incident logs.",
)  # Agent may choose this tool; retrieval is not always-on

MATCH_INCIDENTS = {  # Live log the static rulebook does not contain
    "INC-101": "Match MI vs CSK, over 12.3: Bowler warned for running on the pitch. Penalty: 5 runs awarded to batting side.",  # Pitch-running warning + 5-run penalty
    "INC-102": "Match RCB vs RR, over 8.1: Front-foot no-ball called. One run added; free hit on next delivery.",  # No-ball incident used in eval
    "INC-103": "Match GT vs DC, over 15.4: DRS review upheld — batter out LBW. Batting team has 1 review remaining.",  # DRS incident with remaining reviews
}


@tool  # Register get_match_incident so the agent can call it by name
def get_match_incident(incident_id: str) -> str:
    """Use when the user asks about a specific live match incident by ID (format: INC-101)."""
    return MATCH_INCIDENTS.get(incident_id, f"No incident found for ID {incident_id}.")  # Dict lookup; unknown ids return a clear miss


TOOLS = [t20_rules_search_tool, get_match_incident]  # Two tools — the agent must pick, or pick neither
_llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)  # Temperature 0 for more stable tool routing in class
_agent_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a T20 cricket rules and match inquiry assistant. Use t20_rules_search_tool for rulebook questions. Use get_match_incident for live incident IDs like INC-101. Remember incident IDs from earlier turns. Refuse politely for unrelated trivia. Ground rule answers in retrieved text. Be concise."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # Past user ↔ assistant turns you maintain
    ("human", "{input}"),  # Current user question
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # Current-run tool trace filled by the executor
])
_agent = create_tool_calling_agent(llm=_llm, tools=TOOLS, prompt=_agent_prompt)  # Wire model + tools + prompt
_executor = AgentExecutor(agent=_agent, tools=TOOLS, verbose=True, max_iterations=4, handle_parsing_errors=True)  # Bounded loop; verbose shows tool names
chat_history: list = []  # Shared list passed into invoke and appended after each turn


def ask(user_text: str) -> str:
    """One user turn: invoke the agent, then append both messages to chat_history."""
    result = _executor.invoke({"input": user_text, "chat_history": chat_history})  # Run the tool loop for this turn
    answer = result["output"]  # Public string the app returns to the student
    chat_history.append(HumanMessage(content=user_text))  # Store the user turn for the next invoke
    chat_history.append(AIMessage(content=answer))  # Store the assistant turn so follow-ups can say "that incident"
    return answer  # Caller prints or scores this string


def demo_live_queries() -> None:
    """Four queries: rulebook, incident, memory follow-up, out-of-domain refusal."""
    print("\n--- Q1: Rulebook (expect t20_rules_search_tool) ---")  # Should search the handbook
    print(ask("How many fielders can stand outside the circle during powerplay?"))  # Rule question
    print("\n--- Q2: Live incident (expect get_match_incident) ---")  # Should call the incident tool
    print(ask("What happened in incident INC-101?"))  # Ops-id question
    print("\n--- Q3: Multi-turn memory (expect incident context + maybe rules search) ---")  # Relies on chat_history
    print(ask("What does the rulebook say about the penalty type mentioned for that incident?"))  # Follow-up without repeating INC-101
    print("\n--- Q4: Out of domain (expect polite refusal, no tool) ---")  # Safety / arbitration
    print(ask("What was the highest bid in the IPL auction this year?"))  # Unrelated trivia


EVAL_CASES = [
    {"name": "powerplay_rule", "input": "During powerplay in T20, how many fielders can be outside the 30-yard circle?", "expect_keywords": ["2", "powerplay"], "expect_tool": "t20_rules_search_tool", "failure_if_miss": "weak_retrieval"},
    {"name": "incident_lookup", "input": "Tell me about match incident INC-102.", "expect_keywords": ["no-ball", "free hit"], "expect_tool": "get_match_incident", "failure_if_miss": "wrong_tool"},
    {"name": "out_of_domain", "input": "Who won the FIFA World Cup?", "expect_keywords": [], "expect_tool": None, "failure_if_miss": "over_refusal_or_hallucination"},
]  # Golden-style pack: empty keywords means check verbose log, not a fake PASS


def run_eval() -> list[dict]:
    """Fixed cases; clear history between cases; print a results log."""
    results: list[dict] = []  # Collect one row per case for the summary
    for case in EVAL_CASES:  # Same exam paper after every prompt or tool change
        chat_history.clear()  # Prevent memory bleed so case 2 cannot cheat from case 1
        print("\n=== EVAL:", case["name"], "===")  # Banner so traces are easy to split
        output = ask(case["input"])  # Run the live agent
        print("Output:", output)  # Student-facing answer to inspect
        if not case["expect_keywords"]:  # Refusal cases are not scored by keyword hunt
            keywords_ok, missing = None, []  # None = N/A, not a fake PASS
            print("Keywords: N/A (check verbose log — expect no tool / polite refusal)")  # Student checks refusal in the trace
        else:
            missing = [kw for kw in case["expect_keywords"] if kw.lower() not in output.lower()]  # Case-insensitive keyword hunt
            keywords_ok = len(missing) == 0  # True only when every expected token appears
            print("Keywords:", "PASS" if keywords_ok else f"FAIL missing={missing}")  # Compact per-case line
        row = {"name": case["name"], "keywords_pass": keywords_ok, "expect_tool": case["expect_tool"], "hint_failure_class": case["failure_if_miss"] if keywords_ok is False else None}  # One log row
        results.append(row)  # Keep rows for the summary
        print("Expected tool (check verbose log):", case["expect_tool"])  # Tool check is visual in verbose output
        if keywords_ok is False:
            print("First fix hint:", case["failure_if_miss"])  # Point to a failure class, not a random rewrite
    scored = [r for r in results if r["keywords_pass"] is not None]  # Skip N/A refusal cases
    passed = sum(1 for r in scored if r["keywords_pass"])  # Count keyword passes only
    print(f"\n===== EVAL RESULTS LOG =====\nSummary: {passed}/{len(scored)} keyword-pass (N/A cases are not counted)")  # Before/after comparison line
    for r in results:
        flag = "N/A" if r["keywords_pass"] is None else ("PASS" if r["keywords_pass"] else "FAIL")  # Three-way flag
        print(f"  [{flag}] {r['name']} | tool≈{r['expect_tool']} | hint={r['hint_failure_class']}")  # One row per case
    return results  # Caller can ignore the return; printing is the classroom interface


if __name__ == "__main__":
    demo_lcel_chain()  # Phase 1
    demo_live_queries()  # Phase 2
    chat_history.clear()  # Reset so demo memory does not bleed into eval
    run_eval()  # Phase 3
```

**How the code works**

- **Phase 1** — `prompt | ChatGroq | StrOutputParser` is LCEL. If a free-hit sentence prints, Groq and packages are fine.
- **Phase 2a–2b** — `T20_RULE_DOCS` → splitter → MiniLM → Chroma → `t20_rules_search_tool`. Retrieval sits **inside a tool** (**agentic RAG**), not always-on.
- **Phase 2c** — `get_match_incident` holds **ops data** the handbook does not have. The agent **arbitrates**.
- **Phase 2d** — `chat_history` is past turns **you** append. `agent_scratchpad` is **this run’s** tool trace, filled by the executor.
- **Phase 3** — `run_eval()` is a tiny golden set. Empty `expect_keywords` prints **N/A** and is **not** counted as a keyword PASS. `chat_history.clear()` between cases.

- **Official Definition:** **Agentic RAG** is retrieval exposed as a **tool** the agent may call zero or more times, instead of a fixed retrieve-then-generate path.
- **In Simple Words:** Open the handbook only when the question needs it — not on every greeting.
- **Real-Life Example:** A bank clerk opens the **policy binder** for “auto reverse in 24 hours,” not for “what is my account number?”

- **Common mistake:** Forgetting `export GROQ_API_KEY` — every chain and agent call fails immediately.
- **Common mistake:** Expecting MiniLM to download instantly the first time — the model caches after one fetch.

**Imports this file skips on purpose**

| Skipped | Why |
|---|---|
| PDF / `TextLoader` | Rule text is inline `Document` objects — fewer moving parts in class |
| Manual `bind_tools` / `ToolMessage` loop | `AgentExecutor` already runs that loop |
| `RunnablePassthrough` standalone RAG chain | Retrieval lives inside `create_retriever_tool` |
| LangGraph `StateGraph` | Today is one agent desk, not a multi-station map |

Run Phase 1 alone if you want to check Groq before ingest:

```bash
python3 -c "from t20_rules_assistant import demo_lcel_chain; demo_lcel_chain()"
```

---

## Build Walkthrough — Tools, Memory, Eval

### Why two tools?

The **rulebook** says *what the laws are*. The **incident log** says *what happened in a match*.

| Query | Correct tool | Wrong choice |
|---|---|---|
| *"Free hit dismissal modes?"* | `t20_rules_search_tool` | `get_match_incident` |
| *"What happened in INC-102?"* | `get_match_incident` | `t20_rules_search_tool` |
| *"IPL auction highest bid?"* | neither — refuse | any tool |

- **Official Definition:** **Tool arbitration** is the agent picking the right tool (or none) from **names and descriptions**.
- **In Simple Words:** Pick the right drawer — handbook or match log — or close both.
- **Real-Life Example:** A **third umpire** picks one replay angle, not every camera for every shout.
- **Fix first when routing fails:** rewrite the **tool description**, not the model size.

### Memory — two notebooks

| | **`chat_history`** | **`agent_scratchpad`** |
|---|---|---|
| Holds | Past user ↔ assistant turns | Current-run tool inputs/outputs |
| You maintain? | **Yes** — append in `ask()` | **No** — executor fills it |
| T20 example | Turn 1: INC-101 → Turn 2: *that penalty* | One question that searches rules *after* an incident lookup |

### Activity — Routing table

Run `demo_live_queries()` with `verbose=True`. Fill from the trace:

| Query | Expected tool | Your trace |
|---|---|---|
| Powerplay fielders | `t20_rules_search_tool` | |
| INC-101 | `get_match_incident` | |
| Follow-up on that penalty | incident context + maybe rules search | |
| IPL auction bid | none | |

### Activity — Break memory on purpose

Comment out both `chat_history.append` lines in `ask()`. Re-run Q2 then Q3. Turn 3 should forget **INC-101**. Restore the lines — that is the **missing memory** signature.

### EvalPack and first fixes

You already practised **golden questions** before promoting a prompt. This pack is the same habit inside LangChain.

- **Official Definition:** An **EvalPack** is a scripted list of inputs with **expected keywords** and **expected tools**, plus a results log you compare before and after a patch.
- **In Simple Words:** The same exam paper after every change — plus a score sheet.
- **Real-Life Example:** Before a payments release, ops run the same dispute queries and count pass rate.

![EvalPack dashboard — golden cases with expected tools, pass or check-log results, and a first-fix panel](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session01-hands-on-langchain/session01-04-evalpack.png)

```bash
python3 t20_rules_assistant.py
```

| Signature | Symptom | First fix |
|---|---|---|
| **Wrong tool** | INC id triggers rule search | Sharpen `get_match_incident` (`INC-xxx`) |
| **Weak retrieval** | Right tool, wrong chunk | Tune `chunk_size` / `k` or rule text |
| **Over-refusal** | Refuses a valid powerplay question | Loosen system prompt; expand when-to-use |
| **Missing memory** | Forgets INC-101 | Restore `chat_history.append` |

**Activity — one patch:** Note the results-log summary. Change **one** thing (description, `k`, or one prompt line). Re-run `run_eval()` and compare `N/M`. If the score did not move, revert and try a different **failure-class** fix.

If Groq rate-limits `llama-3.1-8b-instant`, switch `model=` to another classroom Groq id — same `ChatGroq` pattern.

Importing the file also builds the Chroma index. The first MiniLM download can take a minute; later runs use the local cache.

```text
Phase 1  demo_lcel_chain()     prompt | ChatGroq | StrOutputParser
              ↓
Phase 2  T20_RULE_DOCS → Chroma → t20_rules_search_tool
         get_match_incident (@tool) + AgentExecutor + ask()
              ↓
Phase 3  EVAL_CASES → run_eval() → results log → one patch → re-run
```

---

## Confidence Checkpoint — Explain Without Looking

1. What is LangChain for, in one sentence, compared with LangGraph?
2. When would you still draw a **graph** instead of only `AgentExecutor`?
3. What is the difference between `agent_scratchpad` and `chat_history`?
4. Why does `get_match_incident` exist beside `t20_rules_search_tool`?
5. If incident queries open the rulebook tool, what do you fix **first**?

If you can answer all five, you can port this pattern to a UPI desk or campus FAQ without changing the architecture.

---

## Key Takeaways

- **LangChain** is a **parts catalogue** (prompts, Groq wrapper, parsers, tools, retrievers). **LangGraph** is a **workflow map** (nodes, state, checkpoints). Use LangChain for chains and one-agent desks; keep graphs for branching and resume.
- **LCEL** (`prompt | llm | parser`) is the smallest proof that blocks compose.
- One file can ship **agentic RAG + auxiliary tool + memory + refusal** — the T20 desk is the product shape, not the only domain.
- **EvalPack + failure class + one patch** is the same golden-set habit you already use, now on a LangChain agent.
- Next you can drop these same blocks **inside** LangGraph nodes, or port the file to a new handbook + ops-id pair.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `t20_rules_assistant.py` | File | One-file T20 assistant — all three phases |
| **LCEL** / `\|` | Concept / operator | Pipe connecting Runnables left → right |
| `ChatPromptTemplate` | Class | Reusable prompt with `{variables}` |
| `ChatGroq` | Class | LangChain wrapper for Groq chat models |
| `StrOutputParser` | Class | Extract plain text from model output |
| `HuggingFaceEmbeddings` | Class | Local MiniLM vectors for Chroma |
| `@tool` | Decorator | Register a Python function as an agent tool |
| `create_retriever_tool` | Function | Expose a retriever as an agent tool |
| `create_tool_calling_agent` | Function | Wire LLM + tools + prompt |
| `AgentExecutor` | Class | Run the tool loop with `max_iterations` and `verbose` |
| `MessagesPlaceholder` | Class | Slot for `chat_history` or `agent_scratchpad` |
| **Tool arbitration** | Concept | Agent picks the correct tool or none |
| **Agentic RAG** | Concept | Retrieval inside a tool the agent may skip |
| **EvalPack** | Concept | Fixed cases with expected keywords/tools |
| `GROQ_API_KEY` | Config | Environment secret — never commit it |
| `llama-3.1-8b-instant` | Model | Classroom Groq chat model used in this lab |
| `all-MiniLM-L6-v2` | Model | Local embedding model for the rule index |
| `max_iterations=4` | Setting | Stops a runaway tool loop |
| `verbose=True` | Setting | Prints which tool ran — read this during eval |
| **LangGraph** (contrast) | Library | Nodes, edges, state, checkpoints — the workflow graph, not today’s file |
