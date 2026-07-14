# Hands-On LangChain II — UPI Dispute Desk

## Module 3 Recap — Same Stack, New Product

This masterclass is a **second guided practice**. You already built a **T20 Rules & Match Inquiry Assistant**. Today you rebuild the **same Module 3 LangChain stack** in a **new domain** — a **UPI Payment Dispute Desk** — with more focus on **evaluation logging** and **controlled debug patches**.

You are not learning a new framework. You are proving you can **port the pattern**.

| Theme | Key building blocks |
|---|---|
| **Foundations / LCEL** | **Runnables**, **PromptTemplate**, **`\|`**, **StrOutputParser**, **ChatOllama** |
| **Tools + Agent** | **`@tool`**, **`create_tool_calling_agent`**, **`AgentExecutor`**, **`max_iterations`** |
| **Memory** | **`MessagesPlaceholder`**, **`chat_history`**, **`agent_scratchpad`** |
| **RAG + integrated agent** | **Document**, **Chroma**, **`create_retriever_tool`**, **tool arbitration** |
| **Eval + debug** | **EVAL_CASES**, **results log**, **failure class** → **one patch** |

By the end: *“I can swap the domain, keep the architecture, and prove quality with an eval harness.”*

---

## What You Will Build — UPI Payment Dispute Desk

Everyday India: money leaves via **UPI**, but the merchant says “not received.” Your assistant is a **bank / PSP help-desk trainee**.

| Part of the app | Real-life role | LangChain piece |
|---|---|---|
| **UPI FAQ search** | Policy handbook — failed debit, auto reverse, dispute SLA, PIN lock | **RAG** → **`upi_faq_search_tool`** |
| **Transaction lookup** | Ops console — status of `TXN-…` | **`@tool`** → **`get_transaction_status`** |
| **Multi-turn chat** | Follow-ups without repeating the TXN id | **`chat_history`** |
| **Safety** | Refuses stocks / sports trivia | System prompt + **tool arbitration** |

- **Official Definition:** An **integrated LangChain agent** combines retrieval, custom tools, conversational memory, and bounded execution in one app.
- **In Simple Words:** One help desk that opens the **UPI FAQ** or checks a **transaction log** — and remembers the case id.
- **Real-Life Example:** Care agent opens the **policy PDF** for “auto reverse in 24 hours” *and* the **ops screen** for `TXN-501`.

```text
User → AgentExecutor (+ memory) → chooses:
   upi_faq_search_tool (Chroma)  |  get_transaction_status  |  polite refusal
```

> **Note:** FAQ and txn records are **teaching samples**, not official NPCI / bank policy.

| | **Hands-On I (T20)** | **Hands-On II (UPI)** |
|---|---|---|
| Domain | Cricket rules + match incidents | Payments FAQ + txn status |
| RAG / aux tools | `t20_rules_search_tool` / `get_match_incident` | `upi_faq_search_tool` / `get_transaction_status` |
| Phase 3 | Compact keyword EvalPack | **Results log** + **failure-class patch** |

Same architecture. New story. Stronger quality loop.

---

## Today's Agenda — One File, Three Phases

Everything lives in **`upi_dispute_assistant.py`**.

| Phase | Focus | What you prove |
|---|---|---|
| **1 — Warm-up** | **`demo_lcel_chain()`** | LCEL `prompt \| llm \| parser` |
| **2 — Build** | Ingest → tools → agent → **`ask()`** | End-to-end app in a new domain |
| **3 — Eval & debug** | **`run_eval()`** + **one patch** | Harness, results log, iteration |

```text
langchain_hands_on_2/
├── venv/
└── upi_dispute_assistant.py
```

---

## Before You Start — Quick Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core langchain-ollama langchain-chroma langchain-text-splitters langchain-classic
ollama pull qwen2.5:0.5b
ollama pull nomic-embed-text
```

Create **`upi_dispute_assistant.py`**, paste the file below, then run phases in order.

---

## The Complete App — `upi_dispute_assistant.py`

```python
# =============================================================================
# UPI Payment Dispute Desk — Hands-On LangChain II
# One file | Three phases: warm-up → build → eval & debug
# =============================================================================

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.tools.retriever import create_retriever_tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent


# =============================================================================
# PHASE 1 — LCEL WARM-UP
# =============================================================================

def demo_lcel_chain() -> None:
    """prompt → ChatOllama → StrOutputParser. Proves env before the agent."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a UPI payments explainer. Answer in 2 sentences max."),
        ("human", "Explain {topic} in simple words."),
    ])
    llm = ChatOllama(model="qwen2.5:0.5b", base_url="http://localhost:11434", temperature=0.2)
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"topic": "what happens when a UPI debit fails but money left the account"})
    print("Phase 1 — LCEL warm-up output:\n", answer)


# =============================================================================
# PHASE 2 — BUILD THE APP
# =============================================================================

# --- 2a. UPI FAQ corpus (RAG source) ---
UPI_FAQ_DOCS = [
    Document(page_content=(
        "Failed UPI debit: If money leaves the payer account but the merchant did not receive it, "
        "the payer bank must auto-reverse the amount usually within 24 hours under UPI guidance."
    )),
    Document(page_content=(
        "Pending transaction: A UPI txn can stay pending for a short window while the switch confirms status. "
        "Do not retry the same payment until the pending state clears or reverses."
    )),
    Document(page_content=(
        "Merchant dispute SLA: For goods not delivered after a successful UPI debit, raise a merchant dispute "
        "within 7 days through the banking app; investigation may take up to 5 working days."
    )),
    Document(page_content=(
        "UPI PIN locked: After 3 consecutive wrong PIN attempts, UPI PIN is locked. "
        "Unlock via the bank app using debit card and ATM PIN as per bank process."
    )),
    Document(page_content=(
        "Collect request fraud: Never approve unknown collect requests. Banks will not ask for UPI PIN on phone. "
        "Reject unexpected collect requests and report through the banking app."
    )),
    Document(page_content=(
        "Complaint ticket: If auto-reverse does not happen after 24 hours, raise a complaint with RRN / UTR. "
        "Keep screenshots of debit SMS and merchant chat as supporting evidence."
    )),
]

# --- 2b. Ingest: split → embed → Chroma → retriever tool ---
_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
_faq_chunks = _splitter.split_documents(UPI_FAQ_DOCS)
_embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")
_vectorstore = Chroma.from_documents(
    documents=_faq_chunks, embedding=_embeddings, collection_name="upi_faq_demo",
)
_retriever = _vectorstore.as_retriever(search_kwargs={"k": 2})

upi_faq_search_tool = create_retriever_tool(
    _retriever,
    name="upi_faq_search_tool",
    description=(
        "Search UPI payment FAQ and dispute policy. "
        "Use for failed debit, auto reverse, pending txn, merchant dispute SLA, PIN lock, collect fraud, complaint steps. "
        "Do NOT use for looking up a specific transaction id status."
    ),
)

# --- 2c. Auxiliary tool: live transaction status ---
TRANSACTIONS = {
    "TXN-501": (
        "TXN-501 | Amount INR 850 | Status: DEBITED_NOT_CREDITED | "
        "Merchant: QuickMart | Last update: waiting for auto-reverse clock (14h elapsed)."
    ),
    "TXN-502": (
        "TXN-502 | Amount INR 1200 | Status: SUCCESS | "
        "Merchant: CityCab | Both legs confirmed; no dispute open."
    ),
    "TXN-503": (
        "TXN-503 | Amount INR 499 | Status: REVERSED | "
        "Auto-reverse credited back to payer account at 11:42 IST."
    ),
}

@tool
def get_transaction_status(transaction_id: str) -> str:
    """Use when the user asks about a specific UPI transaction by ID (format: TXN-501)."""
    return TRANSACTIONS.get(transaction_id, f"No transaction found for ID {transaction_id}.")

TOOLS = [upi_faq_search_tool, get_transaction_status]

# --- 2d. Agent + memory ---
_llm = ChatOllama(model="qwen2.5:0.5b", base_url="http://localhost:11434", temperature=0)

_agent_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a UPI payment dispute help-desk assistant. "
        "Use upi_faq_search_tool for policy FAQ questions (failed debit, auto reverse, pending, dispute SLA, PIN lock, fraud). "
        "Use get_transaction_status for live txn IDs like TXN-501. "
        "Remember transaction IDs and topics from earlier turns. "
        "Refuse politely for unrelated topics (stocks, sports scores, celebrity gossip). "
        "Ground policy answers in retrieved text. Be concise."
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

_agent = create_tool_calling_agent(llm=_llm, tools=TOOLS, prompt=_agent_prompt)
_executor = AgentExecutor(
    agent=_agent, tools=TOOLS, verbose=True, max_iterations=4, handle_parsing_errors=True,
)

chat_history: list = []


def ask(user_text: str) -> str:
    """One user turn + update chat_history."""
    result = _executor.invoke({"input": user_text, "chat_history": chat_history})
    answer = result["output"]
    chat_history.append(HumanMessage(content=user_text))
    chat_history.append(AIMessage(content=answer))
    return answer


def demo_live_queries() -> None:
    """Tool arbitration, memory, and refusal demos."""
    print("\n--- Q1: FAQ (expect upi_faq_search_tool) ---")
    print(ask("My UPI debit left my account but merchant did not get it. How long for auto reverse?"))

    print("\n--- Q2: Live txn (expect get_transaction_status) ---")
    print(ask("What is the status of transaction TXN-501?"))

    print("\n--- Q3: Multi-turn memory ---")
    print(ask("Based on that status, what should I do next according to policy?"))

    print("\n--- Q4: Out of domain (expect refusal) ---")
    print(ask("What is the share price of Tata Motors today?"))


# =============================================================================
# PHASE 3 — EVAL HARNESS + RESULTS LOG
# =============================================================================

EVAL_CASES = [
    {
        "name": "auto_reverse_window",
        "input": "If UPI money left my account but merchant did not receive it, how soon should it reverse?",
        "expect_keywords": ["24", "reverse"],
        "expect_tool": "upi_faq_search_tool",
        "failure_if_miss": "weak_retrieval",
    },
    {
        "name": "txn_lookup",
        "input": "Tell me about transaction TXN-503.",
        "expect_keywords": ["REVERSED"],
        "expect_tool": "get_transaction_status",
        "failure_if_miss": "wrong_tool",
    },
    {
        "name": "merchant_dispute_sla",
        "input": "How many days do I have to raise a merchant dispute for goods not delivered?",
        "expect_keywords": ["7"],
        "expect_tool": "upi_faq_search_tool",
        "failure_if_miss": "weak_retrieval",
    },
    {
        "name": "out_of_domain",
        "input": "Who won the last Cricket World Cup?",
        "expect_keywords": [],
        "expect_tool": None,
        "failure_if_miss": "over_refusal_or_hallucination",
    },
]


def run_eval() -> list[dict]:
    """Fixed cases; clear history between cases; print results log."""
    results: list[dict] = []
    for case in EVAL_CASES:
        chat_history.clear()
        print("\n=== EVAL:", case["name"], "===")
        output = ask(case["input"])
        print("Output:", output)
        missing = [kw for kw in case["expect_keywords"] if kw.lower() not in output.lower()]
        keywords_ok = len(missing) == 0
        row = {
            "name": case["name"],
            "keywords_pass": keywords_ok,
            "missing_keywords": missing,
            "expect_tool": case["expect_tool"],
            "hint_failure_class": case["failure_if_miss"] if not keywords_ok else None,
        }
        results.append(row)
        print("Keywords:", "PASS" if keywords_ok else f"FAIL missing={missing}")
        print("Expected tool (check verbose log):", case["expect_tool"])
        if not keywords_ok:
            print("First fix hint:", case["failure_if_miss"])

    print("\n========== EVAL RESULTS LOG ==========")
    passed = sum(1 for r in results if r["keywords_pass"])
    print(f"Summary: {passed}/{len(results)} cases keyword-pass")
    for r in results:
        flag = "PASS" if r["keywords_pass"] else "FAIL"
        print(f"  [{flag}] {r['name']} | tool≈{r['expect_tool']} | hint={r['hint_failure_class']}")
    print("======================================\n")
    return results


def apply_debug_patch_example() -> None:
    """Print failure-class → fix menu. Change ONE item, then re-run run_eval()."""
    print(
        "Debug patch menu (change ONE item, then re-run run_eval):\n"
        "  wrong_tool      → sharpen get_transaction_status description (mention TXN-xxx)\n"
        "  weak_retrieval  → raise chunk_size to 220 OR set k=3 OR clarify FAQ Document text\n"
        "  over_refusal    → loosen system prompt; expand when-to-use on upi_faq_search_tool\n"
        "  missing_memory  → restore chat_history.append lines inside ask()\n"
    )


if __name__ == "__main__":
    demo_lcel_chain()
    demo_live_queries()
    chat_history.clear()
    run_eval()
    apply_debug_patch_example()
```

**How the file works**

- **Phase 1** — `prompt | llm | StrOutputParser`; healthy stack if failed-debit text prints.
- **Phase 2a–2b** — `UPI_FAQ_DOCS` → Chroma → `upi_faq_search_tool` (**agentic RAG**).
- **Phase 2c** — `get_transaction_status` for ops data the FAQ does not have → **arbitrate**.
- **Phase 2d** — `chat_history` + `agent_scratchpad` + `AgentExecutor` + `ask()`.
- **Phase 3** — `run_eval()` prints a **results log**; `apply_debug_patch_example()` shows the **fix menu**.

---

## Phase 1 — LCEL Warm-Up

```bash
python3 -c "from upi_dispute_assistant import demo_lcel_chain; demo_lcel_chain()"
```

- **Official Definition:** **LCEL** composes **Runnables** with **`|`** so output flows step by step.
- **In Simple Words:** UPI rail — phone → bank app → switch → merchant; each hop forwards a clear payload.
- **Real-Life Example:** SMS “debited” → FAQ advice. The warm-up is the smallest version of that pipeline.

**Activity:** Change invoke topic to **`"why you should not approve unknown UPI collect requests"`**. Only the input changes — that is **composability**.

---

## Phase 2 — Build the App

### 2a–2b. FAQ corpus and ingest

Inline **`Document`** objects (production would use PDF loaders).

| Topic | Example question |
|---|---|
| Failed debit / auto reverse | *"Money left but merchant unpaid — how long?"* |
| Merchant dispute SLA | *"How many days to raise a dispute?"* |
| PIN lock / collect fraud | *"PIN locked after wrong attempts?"* |

```text
UPI_FAQ_DOCS → splitter → OllamaEmbeddings → Chroma → create_retriever_tool
                                                    → upi_faq_search_tool
```

Retrieval lives **inside a tool** the agent may choose — not always-on.

### 2c. Why two tools?

| Query | Correct tool | Wrong choice |
|---|---|---|
| *"Auto reverse window?"* | `upi_faq_search_tool` | `get_transaction_status` |
| *"Status of TXN-501?"* | `get_transaction_status` | `upi_faq_search_tool` |
| *"Tata Motors share price?"* | neither — refuse | any tool |

- **Official Definition:** **Tool arbitration** — pick the right tool (or none) from names and descriptions.
- **In Simple Words:** Open **policy** or **ops screen** — not both blindly.
- **Real-Life Example:** *"Where is my INR 850?"* needs **TXN-501**, not a PIN-lock paragraph.

### 2d. Memory

| | **`chat_history`** | **`agent_scratchpad`** |
|---|---|---|
| Holds | Past user ↔ assistant turns | Current-run tool I/O |
| You maintain? | **Yes** — append in `ask()` | **No** — executor fills it |
| UPI example | Turn 1: TXN-501 → Turn 2: “what next?” | FAQ search after txn lookup in one run |

**Activity — routing table:** Run `demo_live_queries()` with `verbose=True`. Note which tool each of Q1–Q4 used. If routing fails, **rewrite tool descriptions first**.

**Activity — break memory:** Comment out both `chat_history.append` lines in `ask()`. Re-run Q2 then Q3 — Turn 3 should forget TXN-501. Restore the lines (**missing memory** signature).

---

## Phase 3 — Eval Harness, Results Log, Debug Patch

- **Official Definition:** An **evaluation harness** is fixed inputs with expected keywords/tools plus a **results log** you compare before and after a patch.
- **In Simple Words:** Same trainee exam every change — plus a score sheet.
- **Real-Life Example:** Before a payments release, ops runs the same dispute queries and counts pass rate.

```bash
python3 -c "from upi_dispute_assistant import run_eval; run_eval()"
```

| Signature | Symptom | First fix |
|---|---|---|
| **Wrong tool** | TXN id → FAQ search | Sharpen `get_transaction_status` (`TXN-xxx`) |
| **Weak retrieval** | Right tool, wrong chunk | Tune `chunk_size` / `k` or FAQ text |
| **Over-refusal** | Refuses valid FAQ | Loosen system prompt; expand when-to-use |
| **Missing memory** | Forgets TXN-501 | Restore `chat_history.append` |

**Activity — one patch (before / after):**

1. Note the **EVAL RESULTS LOG** summary (`N/M` keyword-pass).
2. Pick one failing case (or deliberately weaken a tool description).
3. Change **one** thing only — tool description, `chunk_size` / `k`, or one system-prompt line.
4. Re-run `run_eval()` and compare the summary line.
5. If the score did not move, **revert** and try a different failure-class fix.

That loop is the heart of **debug and iterate**: measure → classify → patch once → re-measure.

---

## End-to-End Map

```text
Phase 1  demo_lcel_chain()     prompt | llm | StrOutputParser
              ↓
Phase 2  UPI_FAQ_DOCS → Chroma → upi_faq_search_tool
         get_transaction_status (@tool) + AgentExecutor + ask()
              ↓
Phase 3  EVAL_CASES → run_eval() → results log → one patch → re-run
```

---

## Confidence Checkpoint — Explain Without Looking

1. What stays the same between the T20 assistant and the UPI desk? What changes?
2. Why does `get_transaction_status` exist beside `upi_faq_search_tool`?
3. What does the **EVAL RESULTS LOG** give you that one manual chat does not?
4. If TXN queries open the FAQ tool, what do you fix **first**?
5. Why must `chat_history.clear()` run between eval cases?

If you can answer all five, you can carry this pattern into new products.

---

## Key Takeaways

- **Portability** — same LangChain blocks; domain text and tools change, architecture does not.
- **UPI FAQ + txn status** practice **tool arbitration**: handbook (RAG) vs ops (`@tool`) vs refusal.
- **Phase 3 depth** — results log + failure-class menu make debugging evidence-based.
- **`ask()` + `chat_history`** keep multi-turn natural (*"that txn"* → *"what next?"*).
- **One patch at a time** — measure before and after.

---

## Packages, Imports, and Key Terms

| Package | Why needed |
|---|---|
| `langchain-core` | Prompts, messages, documents, parsers, `@tool` |
| `langchain-ollama` | `ChatOllama`, `OllamaEmbeddings` |
| `langchain-chroma` | Chroma vector store |
| `langchain-text-splitters` | Chunk FAQ docs |
| `langchain-classic` | `AgentExecutor`, `create_tool_calling_agent` |
| `langchain` *(with classic)* | `create_retriever_tool` |

| Term | Meaning |
|---|---|
| `upi_dispute_assistant.py` | One-file UPI desk — all three phases |
| `demo_lcel_chain()` / `ask()` / `run_eval()` | Phase 1 / 2 / 3 entry points |
| `upi_faq_search_tool` | Retriever-backed FAQ search |
| `get_transaction_status` | Live txn lookup by TXN-ID |
| `\|` / LCEL | Pipe connecting Runnables |
| `MessagesPlaceholder` | Slot for `chat_history` or `agent_scratchpad` |
| **Tool arbitration** | Agent picks correct tool (or none) |
| **Agentic RAG** | FAQ retrieval inside the tool-calling agent |
| **Eval harness / results log** | Fixed cases + printed pass/fail rows |
| **Failure signature** | Named failure → first targeted fix |
| `ollama pull qwen2.5:0.5b` | Chat model |
| `ollama pull nomic-embed-text` | Embedding model for RAG |
