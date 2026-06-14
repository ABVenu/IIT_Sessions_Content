# Hands-On LangChain

## Module 3 at a Glance — What You Have Built

This masterclass is a **guided practice session**. You will rebuild the **LangChain journey of Module 3** in **one single file** — from a quick LCEL warm-up to a full **T20 Rules & Match Inquiry Assistant** that uses **tools**, **memory**, and **retrieval**.

Below is the **full map** of what the module covered. Use it as your mental checklist before you start coding.

| Theme | Core idea | Key building blocks |
|---|---|---|
| **LangChain foundations** | Organise LLM apps with reusable blocks instead of one-off API calls | **Runnables**, **PromptTemplate**, **LCEL** (`\|`), **StrOutputParser** |
| **Environment and first chain** | Stand up a clean project and prove one chain end-to-end | **venv**, **ChatOllama**, **ChatPromptTemplate** |
| **Tools** | Let the model **request actions** your Python code runs | **`@tool`**, **`bind_tools`**, **`tool_calls`**, **`ToolMessage`** |
| **Agent executor** | Stop writing the tool loop by hand | **`create_tool_calling_agent`**, **`AgentExecutor`**, **`max_iterations`**, **`verbose`** |
| **Memory on agents** | Remember past user turns across invocations | **`MessagesPlaceholder`**, **`chat_history`**, **`agent_scratchpad`** |
| **RAG pipeline** | Answer from **your documents**, not only training data | **Document**, **text splitter**, **Chroma**, **retriever**, **LCEL** |
| **Integrated agent** | One agent chooses **retrieval**, **auxiliary tools**, **both**, or **refusal** | **`create_retriever_tool`**, **tool arbitration**, **EvalPack** |
| **Evaluation harness** *(upcoming)* | Test agents with fixed cases and structured logs | **eval JSON**, **runner**, **results.csv** |
| **Debug and iterate** *(upcoming)* | Fix agents using eval feedback, not guesswork | **failure class**, **prompt/tool patch**, **retrieval tune** |

By the end of this hands-on, you should feel: *“I built one complete LangChain app — I can explain every part and extend it.”*

![IPL night stadium — T20 cricket energy sets the context for building a rules and match inquiry assistant](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-creative-01-ipl-night-stadium.png)

---

## What You Will Build — T20 Rules & Match Inquiry Assistant

Instead of another e-commerce bot, you will build an assistant for **T20 cricket** — a domain every Indian student can relate to.

| Part of the app | Real-life role | LangChain piece |
|---|---|---|
| **T20 rulebook search** | ICC-style handbook — powerplay, free hit, no-ball, DRS | **RAG** via **`t20_rules_search_tool`** |
| **Live match incident lookup** | Scorer’s log — penalty runs, warnings, review outcomes for a specific match moment | **`@tool`** → **`get_match_incident`** |
| **Multi-turn chat** | Umpire trainee asks follow-ups without repeating the incident ID | **`chat_history`** |
| **Safety** | Refuses unrelated trivia (*“Who won IPL auction?”*) | System prompt + **tool arbitration** |

- **Official Definition:** An **integrated LangChain agent** combines retrieval, custom tools, conversational memory, and bounded execution in one runnable application.
- **In Simple Words:** One **help desk** that can open the **rulebook** or check the **match log** — and remembers what you asked earlier.
- **Real-Life Example:** During an **IPL** game, a broadcast analyst checks the **playing conditions PDF** for powerplay rules *and* the **live feed** for what penalty was applied in over 12 — your app mimics that split.

![Broadcast analyst metaphor — rulebook on one side, live match feed on the other, same split as handbook search vs incident lookup](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-creative-02-broadcast-analyst.png)

![T20 assistant architecture — rule handbook search on one side, live match incident log on the other, with memory and safety refusal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-02-t20-app-two-sources.png)

> **Note:** The rule text and incident records in this lab are **short teaching samples**, not official ICC documents. In production you would load real PDFs and connect to a live scoring API.

---

## Today's Hands-On Agenda — One File, Three Phases

Everything lives in **`t20_rules_assistant.py`**. You build it **top to bottom** in one sitting.

| Phase | Focus | What you prove |
|---|---|---|
| **Phase 1 — Warm-up** | Run **`demo_lcel_chain()`** | Environment works; LCEL `prompt \| llm \| parser` pattern |
| **Phase 2 — Build the app** | Ingest rules → tools → agent → **`ask()`** | Full end-to-end LangChain app |
| **Phase 3 — Test the app** | Run **`run_eval()`** | EvalPack + failure signatures |

```text
langchain_hands_on/
├── venv/
└── t20_rules_assistant.py    ← one file, three phases
```

You are not jumping between seven files. You are shipping **one app**.

![Three-phase build flow — warm up the chain, build the full assistant, then run quality tests](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-01-one-file-three-phases.png)

---

## Before You Start — Quick Setup

You should already have **Python 3**, a **virtual environment**, and **Ollama** running from earlier module work.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core langchain-ollama langchain-chroma langchain-text-splitters langchain-classic
ollama pull qwen2.5:0.5b
ollama pull nomic-embed-text
```

Create **`t20_rules_assistant.py`** and paste the **full file** from the next section. Then work through each phase in order.

---

## The Complete App — `t20_rules_assistant.py`

Save this as one file. Comment blocks mark **Phase 1**, **Phase 2**, and **Phase 3**.

```python
# =============================================================================
# T20 Rules & Match Inquiry Assistant — Hands-On LangChain (Module 3 recap)
# One file | Three phases: warm-up → build → eval
# =============================================================================

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # Reusable prompt layout; slots for chat_history and agent_scratchpad
from langchain_core.output_parsers import StrOutputParser  # Convert raw LLM response into plain text string (Phase 1 LCEL chain)
from langchain_core.documents import Document  # Wrap T20 rule text so splitters and Chroma can ingest it
from langchain_core.messages import HumanMessage, AIMessage  # Store past user and assistant turns in chat_history
from langchain_core.tools import tool  # Register get_match_incident as a structured agent tool
from langchain_ollama import ChatOllama, OllamaEmbeddings  # ChatOllama: local LLM; OllamaEmbeddings: vectors for Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Split long rule docs into small searchable chunks
from langchain_chroma import Chroma  # Local vector database to store and search rule embeddings
from langchain.tools.retriever import create_retriever_tool  # Expose Chroma retriever as t20_rules_search_tool for the agent
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # Managed tool-calling loop (replaces manual bind_tools loop)


# =============================================================================
# PHASE 1 — LCEL WARM-UP (run once to confirm setup)
# =============================================================================

def demo_lcel_chain() -> None:
    """Quick chain: prompt → ChatOllama → StrOutputParser. Proves env before the agent."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a cricket rules explainer. Answer in 2 sentences max."),
        ("human", "Explain {topic} in simple words."),
    ])
    llm = ChatOllama(
        model="qwen2.5:0.5b",
        base_url="http://localhost:11434",
        temperature=0.2,
    )
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"topic": "what is a free hit in T20"})
    print("Phase 1 — LCEL warm-up output:\n", answer)


# =============================================================================
# PHASE 2 — BUILD THE APP (ingest + tools + agent + memory)
# =============================================================================

# --- 2a. T20 rulebook corpus (RAG source — static handbook text) ---
T20_RULE_DOCS = [
    Document(page_content=(
        "Powerplay rules (T20): Mandatory powerplay covers overs 1 to 6. "
        "A maximum of 2 fielders may be positioned outside the 30-yard circle during powerplay."
    )),
    Document(page_content=(
        "Free hit rules: After a no-ball is called, the next legal delivery is a free hit. "
        "On a free hit the batter can only be dismissed run out, hit the ball twice, or obstruct the field."
    )),
    Document(page_content=(
        "No-ball rules: Front-foot no-ball if the bowler's front foot lands beyond the popping crease. "
        "A no-ball adds one run and the next ball is a free hit in T20."
    )),
    Document(page_content=(
        "Wide ball rules: A wide is called if the ball passes wide of the batter on the off side "
        "without being touched, or on the leg side outside the leg-stump line, and wide adds one run."
    )),
    Document(page_content=(
        "DRS rules (T20): Each team receives 2 unsuccessful player reviews per innings. "
        "Reviews are reset for the knockout stage in some tournaments — check playing conditions."
    )),
    Document(page_content=(
        "Dead ball rules: The umpire may call dead ball for a dangerous delivery, serious distraction, "
        "or if the batter is not ready. No run scored on that delivery unless already completed."
    )),
]

# --- 2b. Ingest: split → embed → Chroma → retriever ---
_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
_rule_chunks = _splitter.split_documents(T20_RULE_DOCS)

_embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")
_vectorstore = Chroma.from_documents(
    documents=_rule_chunks,
    embedding=_embeddings,
    collection_name="t20_rules_demo",
)
_retriever = _vectorstore.as_retriever(search_kwargs={"k": 2})

t20_rules_search_tool = create_retriever_tool(
    _retriever,
    name="t20_rules_search_tool",
    description=(
        "Search official T20 playing rules and regulations. "
        "Use for powerplay, free hit, no-ball, wide, dead ball, DRS, fielding restrictions. "
        "Do NOT use for live match scores or incident logs."
    ),
)

# --- 2c. Auxiliary tool: live match incident log (not in the static rulebook) ---
MATCH_INCIDENTS = {
    "INC-101": (
        "Match MI vs CSK, over 12.3: Bowler warned for running on the pitch. "
        "Penalty: 5 runs awarded to batting side."
    ),
    "INC-102": (
        "Match RCB vs RR, over 8.1: Front-foot no-ball called. "
        "One run added; free hit on next delivery."
    ),
    "INC-103": (
        "Match GT vs DC, over 15.4: DRS review upheld — batter out LBW. "
        "Batting team has 1 review remaining this innings."
    ),
}

@tool
def get_match_incident(incident_id: str) -> str:
    """Use when the user asks about a specific live match incident by ID (format: INC-101)."""
    return MATCH_INCIDENTS.get(incident_id, f"No incident found for ID {incident_id}.")

TOOLS = [t20_rules_search_tool, get_match_incident]

# --- 2d. Agent: prompt + AgentExecutor + conversational memory ---
_llm = ChatOllama(model="qwen2.5:0.5b", base_url="http://localhost:11434", temperature=0)

_agent_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a T20 cricket rules and match inquiry assistant. "
        "Use t20_rules_search_tool for rulebook questions (powerplay, free hit, no-ball, wide, DRS, dead ball). "
        "Use get_match_incident for live incident IDs like INC-101. "
        "Remember incident IDs and topics from earlier turns. "
        "Refuse politely for unrelated general trivia (celebrity gossip, stock prices, non-cricket topics). "
        "Ground rule answers in retrieved text. Be concise."
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

_agent = create_tool_calling_agent(llm=_llm, tools=TOOLS, prompt=_agent_prompt)

_executor = AgentExecutor(
    agent=_agent,
    tools=TOOLS,
    verbose=True,
    max_iterations=4,
    handle_parsing_errors=True,
)

chat_history: list = []  # Shared list — passed into invoke and appended after each turn


def ask(user_text: str) -> str:
    """Run the agent for one user turn and update chat_history."""
    result = _executor.invoke({"input": user_text, "chat_history": chat_history})
    answer = result["output"]
    chat_history.append(HumanMessage(content=user_text))
    chat_history.append(AIMessage(content=answer))
    return answer


def demo_live_queries() -> None:
    """Sample queries showing tool arbitration, memory, and refusal."""
    print("\n--- Q1: Rulebook (expect t20_rules_search_tool) ---")
    print(ask("How many fielders can stand outside the circle during powerplay?"))

    print("\n--- Q2: Live incident (expect get_match_incident) ---")
    print(ask("What happened in incident INC-101?"))

    print("\n--- Q3: Multi-turn memory (expect get_match_incident, reusing INC-101) ---")
    print(ask("What does the rulebook say about the penalty type mentioned for that incident?"))

    print("\n--- Q4: Out of domain (expect polite refusal, no tool) ---")
    print(ask("What was the highest bid in the IPL auction this year?"))


# =============================================================================
# PHASE 3 — EVAL PACK (measure behaviour, not vibes)
# =============================================================================

EVAL_CASES = [
    {
        "name": "powerplay_rule",
        "input": "During powerplay in T20, how many fielders can be outside the 30-yard circle?",
        "expect_keywords": ["2", "powerplay"],
        "expect_tool": "t20_rules_search_tool",
    },
    {
        "name": "incident_lookup",
        "input": "Tell me about match incident INC-102.",
        "expect_keywords": ["no-ball", "free hit"],
        "expect_tool": "get_match_incident",
    },
    {
        "name": "out_of_domain",
        "input": "Who won the FIFA World Cup?",
        "expect_keywords": [],
        "expect_tool": None,
    },
]


def run_eval() -> None:
    """Run fixed test cases. Clear history between cases for fair comparison."""
    for case in EVAL_CASES:
        chat_history.clear()
        print("\n=== EVAL:", case["name"], "===")
        output = ask(case["input"])
        print("Output:", output)
        missing = [kw for kw in case["expect_keywords"] if kw.lower() not in output.lower()]
        if missing:
            print("FAIL — keywords missing:", missing)
        else:
            print("PASS — keywords")
        print("Expected tool (check verbose log):", case["expect_tool"])


# =============================================================================
# MAIN — run phases in order during the masterclass
# =============================================================================

if __name__ == "__main__":
    demo_lcel_chain()       # Phase 1
    demo_live_queries()     # Phase 2
    chat_history.clear()    # Reset before eval so Q4 memory does not bleed into tests
    run_eval()              # Phase 3
```

**How the full file works**

- **Phase 1** — **`demo_lcel_chain()`** is the same **`prompt | llm | StrOutputParser`** pattern from the module. If it prints a free-hit explanation, your stack is healthy.
- **Phase 2a–2b** — **`T20_RULE_DOCS`** → splitter → **Chroma** → **`t20_rules_search_tool`**. This is the **RAG pipeline** you learned, now exposed as an agent tool (**agentic RAG**).
- **Phase 2c** — **`get_match_incident`** handles **live log data** the rulebook does not contain. The agent must **arbitrate**: rule question → search tool; incident ID → match tool.
- **Phase 2d** — **`chat_history`** + **`agent_scratchpad`** + **`AgentExecutor`** complete the integrated agent. **`ask()`** is your app’s public interface.
- **Phase 3** — **`run_eval()`** runs a compact **EvalPack**. **`chat_history.clear()`** between cases prevents false passes from memory bleed.

---

## Phase 1 — LCEL Warm-Up

Run only Phase 1 first if you are building the file line by line:

```bash
python3 -c "from t20_rules_assistant import demo_lcel_chain; demo_lcel_chain()"
```

Or comment out **`demo_live_queries()`** and **`run_eval()`** in **`__main__`**, then:

```bash
python3 t20_rules_assistant.py
```

- **Official Definition:** **LCEL** composes LangChain **Runnables** with **`|`** so output flows step by step.
- **In Simple Words:** Filter coffee — water → powder → filter → cup.
- **Real-Life Example:** A **DRS review** chain: camera clip → slow-mo → third umpire → decision on screen. Each step passes output forward.

![Third umpire DRS review — creative analogy for Phase 1 LCEL chain where each step passes output to the next](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-creative-03-third-umpire-drs.png)

![Basic chain pattern — user input flows through prompt template, language model, to clean text output](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-07-lcel-warmup.png)

### Activity — Swap the Topic

Change the invoke topic to **`"wide ball rules in T20"`**. The chain code stays identical — only the input changes. That is **composability**.

---

## Phase 2 — Build the App

Phase 2 is the **main body** of the masterclass. As you type each block, connect it to what you learned in the module.

### 2a. Rulebook corpus (RAG source)

Static **T20 regulations** live as **`Document`** objects. In production these would be PDF loaders; here we use **inline text** to keep imports minimal.

| Document topic | Example user question |
|---|---|
| Powerplay | *"How many fielders outside the circle?"* |
| Free hit | *"When is a batter out on a free hit?"* |
| No-ball / wide | *"What happens after a no-ball?"* |
| DRS | *"How many reviews per innings?"* |

![Artistic aerial powerplay view — max 2 fielders outside the 30-yard circle during T20 powerplay overs 1–6](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-creative-04-powerplay-aerial.png)

### 2b. Ingest path

```text
T20_RULE_DOCS → RecursiveCharacterTextSplitter → OllamaEmbeddings → Chroma → retriever
                              ↓
                  create_retriever_tool → t20_rules_search_tool
```

This is the **same offline → online RAG flow** from class. The only change: retrieval is **inside a tool**, not always-on.

![Document retrieval pipeline — load, split, embed, store, search, then expose as an agent capability](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-03-rag-ingest-path.png)

### 2c. Match incident tool — why two tools?

The **rulebook** says *what the laws are*. The **incident log** says *what happened in a specific match*.

| Query type | Correct tool | Wrong choice |
|---|---|---|
| *"Free hit dismissal modes?"* | `t20_rules_search_tool` | `get_match_incident` |
| *"What happened in INC-102?"* | `get_match_incident` | `t20_rules_search_tool` |
| *"IPL auction highest bid?"* | neither — polite refusal | any tool |

- **Official Definition:** **Tool arbitration** is the agent’s ability to pick the right tool (or none) from names and descriptions.
- **In Simple Words:** The **third umpire** decides which replay angle to check — not every camera for every decision.
- **Real-Life Example:** Ask *"Was that a no-ball?"* during a live game — you need **foot placement replay** (incident), not the **MCC handbook chapter list** (rules index).

![Tool arbitration — agent routes rule questions to handbook search, incident IDs to match log, unrelated topics to refusal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-04-tool-arbitration.png)

### 2d. Memory — scratchpad vs chat_history

| | **`chat_history`** | **`agent_scratchpad`** |
|---|---|---|
| Holds | Past **user ↔ assistant** turns | **Current run** tool inputs/outputs |
| You maintain? | **Yes** — append in **`ask()`** | **No** — executor fills it |
| T20 example | Turn 1: *"INC-101"* → Turn 2: *"that penalty"* | One question needs rules search **after** incident lookup |

![Conversation memory vs current-run trace — past turns you maintain separately from tool steps inside one question](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-05-memory-scratchpad.png)

### Activity — Tool Routing Table

Run **`demo_live_queries()`** with **`verbose=True`**. Fill this table from the trace:

| Query | Expected tool | Your trace |
|---|---|---|
| Powerplay fielders | `t20_rules_search_tool` | |
| INC-101 incident | `get_match_incident` | |
| Rule follow-up on INC-101 | both (incident context + rules search) | |
| IPL auction bid | none | |

If routing fails, **rewrite tool descriptions first** — not the model size.

### Activity — Break Memory on Purpose

Comment out the two **`chat_history.append`** lines in **`ask()`**. Run Q2 and Q3 again. Turn 3 should forget **INC-101**. Restore the lines — this is the **missing memory** failure signature.

---

## Phase 3 — Eval and Debug Drill

Professional teams ship only after a fixed **EvalPack** passes.

- **Official Definition:** An **EvalPack** is a scripted list of inputs with **expected keywords** and **expected tools**.
- **In Simple Words:** The same **umpire exam paper** after every code change.
- **Real-Life Example:** Before **IPL** season, broadcast ops test the same 20 rule queries on the graphics engine every build.

Run Phase 3:

```bash
python3 -c "from t20_rules_assistant import run_eval; run_eval()"
```

Or run the full file — **`run_eval()`** runs after **`demo_live_queries()`**.

![Quality test pack — rule question, incident lookup, and off-topic refusal scenarios with common failure fixes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/masterclass01-hands-on-langchain/masterclass01-06-evalpack.png)

### Failure Signatures — What to Fix First

| Signature | Symptom in T20 app | First fix |
|---|---|---|
| **Wrong tool** | Incident ID triggers rule search | Sharpen **`get_match_incident`** description |
| **Weak retrieval** | Right tool, wrong rule chunk | Tune **`chunk_size`**, **`k`**, or add clearer doc text |
| **Over-refusal** | Refuses valid powerplay question | Loosen system prompt; expand tool **when-to-use** lines |
| **Missing memory** | Follow-up forgets INC-101 | Restore **`chat_history.append`** in **`ask()`** |

### Activity — One Patch Iteration

Pick one failing eval case. Change **one thing** — tool description, chunk size, or one system prompt line. Re-run only that case. Note whether the output improved.

---

## End-to-End Map — One File, Three Phases

```text
Phase 1  demo_lcel_chain()     prompt | llm | StrOutputParser
              ↓
Phase 2  T20_RULE_DOCS → Chroma → t20_rules_search_tool
         get_match_incident (@tool)
         AgentExecutor + chat_history + ask()
              ↓
Phase 3  EVAL_CASES → run_eval() → failure signature → one patch
```

You leave with **one runnable file** — not seven disconnected scripts.

---

## Confidence Checkpoint — Explain Without Looking

1. What is the difference between **`agent_scratchpad`** and **`chat_history`**?
2. Why does **`get_match_incident`** exist alongside **`t20_rules_search_tool`**?
3. What does **`max_iterations=4`** protect you from?
4. If incident queries trigger rule search, what do you fix **first**?
5. Where in the file does **RAG ingest** happen vs where does **agentic retrieval** happen?

If you can answer all five, you are **module-ready**.

---

## Key Takeaways

- **One file, three phases** — warm-up, build, eval — gives a true **end-to-end LangChain app** with less friction.
- **T20 rules + match incidents** show **tool arbitration**: static handbook (RAG) vs live log (**`@tool`**) vs refusal.
- **LCEL**, **AgentExecutor**, **memory**, and **Chroma** are the same patterns from the module — now in one product-shaped script.
- **`ask()`** + **`chat_history`** make multi-turn queries natural (*"that incident"* → *"what rule applies?"*).
- **EvalPack** + **failure signatures** turn debugging into targeted fixes, not random prompt edits.
- This single-agent app prepares you for **formal eval harnesses**, **iteration loops**, and **multi-agent** work ahead.

---

## Why Each Import and Package Is Needed

Every line at the top of **`t20_rules_assistant.py`** maps to one job in the app. If you know **why** it is there, debugging import errors becomes much faster.

### Pip packages (install once)

| Package | Why this app needs it |
|---|---|
| **`langchain-core`** | Base building blocks — prompts, messages, documents, output parsers, `@tool` |
| **`langchain-ollama`** | Connect to **ChatOllama** (chat) and **OllamaEmbeddings** (vectors) on your laptop |
| **`langchain-chroma`** | **Chroma** vector store for T20 rulebook search |
| **`langchain-text-splitters`** | **RecursiveCharacterTextSplitter** to chunk rule documents before embedding |
| **`langchain-classic`** | **AgentExecutor** and **create_tool_calling_agent** for the managed agent loop |
| **`langchain`** *(auto-installed with classic)* | **create_retriever_tool** — wraps retriever as an agent tool |

### Python imports (inside the file)

| Import | From package | Used in | Why it is needed |
|---|---|---|---|
| `ChatPromptTemplate` | langchain-core | Phase 1, 2 | Builds reusable prompt templates with `{input}` and `{topic}` variables |
| `MessagesPlaceholder` | langchain-core | Phase 2 | Reserves slots for **`chat_history`** (past turns) and **`agent_scratchpad`** (current tool trace) |
| `StrOutputParser` | langchain-core | Phase 1 | Extracts clean text from LLM response — last step in LCEL warm-up chain |
| `Document` | langchain-core | Phase 2 | Wraps each T20 rule paragraph as ingestible text for RAG |
| `HumanMessage`, `AIMessage` | langchain-core | Phase 2 | Message types appended to **`chat_history`** after each **`ask()`** call |
| `tool` | langchain-core | Phase 2 | Decorator that registers **`get_match_incident`** so the agent can call it |
| `ChatOllama` | langchain-ollama | Phase 1, 2 | Local chat model — same LLM for warm-up chain and agent |
| `OllamaEmbeddings` | langchain-ollama | Phase 2 | Turns rule chunks into numeric vectors stored in Chroma |
| `RecursiveCharacterTextSplitter` | langchain-text-splitters | Phase 2 | Splits rule docs into small chunks so retrieval finds the right rule, not the whole book |
| `Chroma` | langchain-chroma | Phase 2 | Vector database — similarity search over T20 rules at query time |
| `create_retriever_tool` | langchain | Phase 2 | Converts retriever into **`t20_rules_search_tool`** the agent can choose like any `@tool` |
| `create_tool_calling_agent` | langchain-classic | Phase 2 | Wires LLM + tools + prompt into an agent graph |
| `AgentExecutor` | langchain-classic | Phase 2 | Runs the tool loop safely with **`max_iterations`**, **`verbose`**, error handling |

### Imports you do **not** need in this app

| Skipped import | Why skipped |
|---|---|
| `TextLoader` / PDF loaders | Rule text is inline **`Document`** objects — keeps the demo to essential packages |
| `bind_tools`, `ToolMessage` | **AgentExecutor** handles the tool loop; manual loop not needed here |
| `RunnablePassthrough` | Standalone RAG chain skipped — retrieval lives inside **`create_retriever_tool`** |
| OpenAI / cloud SDKs | Local **Ollama** covers both chat and embeddings for this hands-on |

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `t20_rules_assistant.py` | File | One-file T20 assistant — all three phases |
| `demo_lcel_chain()` | Function | Phase 1 LCEL warm-up |
| `ask()` | Function | Phase 2 public interface — invoke + memory |
| `run_eval()` | Function | Phase 3 EvalPack runner |
| `t20_rules_search_tool` | Tool | Retriever-backed T20 rulebook search |
| `get_match_incident` | Tool | Live incident log lookup by INC-ID |
| `\|` (pipe) | LCEL operator | Connects Runnables left → right |
| `ChatPromptTemplate` | Class | Reusable prompt with `{variables}` |
| `StrOutputParser` | Class | Extract plain text from model output |
| `ChatOllama` | Class | LangChain wrapper for Ollama chat models |
| `OllamaEmbeddings` | Class | Local embeddings for Chroma |
| `@tool` | Decorator | Register a Python function as an agent tool |
| `create_tool_calling_agent` | Function | Build tool-aware agent graph |
| `AgentExecutor` | Class | Run agent loop with limits and logging |
| `MessagesPlaceholder` | Class | Slot for `chat_history` or `agent_scratchpad` |
| `create_retriever_tool` | Function | Expose retriever as an agent tool |
| **Tool arbitration** | Concept | Agent picks correct tool per query |
| **Agentic RAG** | Concept | Rulebook retrieval inside tool-calling agent |
| **EvalPack** | Concept | Fixed test cases with expected behaviour |
| **Failure signature** | Concept | Named failure type → targeted fix |
| `ollama pull qwen2.5:0.5b` | Command | Download small chat model |
| `ollama pull nomic-embed-text` | Command | Download embedding model for RAG |
