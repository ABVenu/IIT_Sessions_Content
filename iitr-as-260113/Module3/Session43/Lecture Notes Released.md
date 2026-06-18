# Debugging and Iterating LangChain Agents

## Context of This Session

In the **previous** class you built a full **evaluation harness** for a LangChain agent. You wrote cases in **eval JSON**, ran a **runner**, saved scores in **results.csv**, opened **failure traces** for weak cases, and even logged **how long** each run took.

That harness answers: *what broke, and what path did the agent take?* Today's class closes the loop on **fixing** agents systematically — not by guessing, not by rewriting everything at once, and not by blaming *"the model is bad."*

**In this session, you will:**

- Understand **debugging** for agentic apps versus simple input–output programs
- Group mistakes into **failure classes** and pick the right **remediation** for each
- Learn **prompt patching**, **tool patching**, and **retrieval tuning** as controlled fixes
- Track **quality metrics**, **token usage**, and **latency**, including the **cost–latency trade-off**
- See a live **RAG retrieval tuning** demo where **chunk size** and **overlap** change the answer on the same query

![From evaluation harness to iteration loop — eval JSON and traces identify failure classes; prompt, tool, and retrieval patches improve quality metrics before ship](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session43/session43-01-eval-to-iteration-loop.png)

---

## What Is Debugging?

- **Official Definition:** **Debugging** is the process of finding the **root cause** of incorrect behaviour in software and applying a fix so the system works as expected.
- **In Simple Words:** Something is broken — you hunt **where** and **why**, then repair it.
- **Real-Life Example:** Your **UPI payment** fails. Debugging is not shouting at the bank app — it is checking whether the issue is **network**, **wrong PIN**, or **server downtime**.

A **bug** is any error or unexpected behaviour in code. Debugging always has two parts:

1. **Find** the exact place or step where things go wrong.
2. **Fix** the root cause — not just the symptom.

For a simple maths function, debugging is easy: input `2 + 2`, expected output `4`. If you get `5`, the function is wrong. End of story.

Agentic applications are not that simple — and that is where today's mindset begins.

---

## Why Agent Debugging Is Harder Than Traditional Apps

In a **traditional** app, you often compare **one input** to **one output**. In an **agentic** workflow, the journey has many steps:

```
User question → LLM reasons → tool call → tool output → maybe another tool → final answer
```

The agent can fail for dozens of reasons at any step:

- **Wrong data** in the knowledge base
- **Over-refusal** on a valid question
- **Under-refusal** on an out-of-domain question
- **Bad prompt** so the LLM misunderstands
- **Wrong arguments** passed to a tool
- **Missing API key** so a tool times out
- **Slow vector database** so retrieval lags

You cannot debug this with input–output alone. You must inspect **which step** failed.

- **Common mistake:** Saying *"the LLM is bad"* and swapping models without checking **prompt**, **tools**, or **retrieval**. Changing the model is a last resort, not the first excuse.
- **Common mistake:** Only reading the **final answer** when the real bug is in the **trajectory** — the agent called the **policy search tool** when it should have called the **calculator**.

![Simple input-output apps vs multi-step agent workflows — many failure points across prompt, tool choice, arguments, retrieval, and final text](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session43/session43-02-simple-io-vs-agent-workflow.png)

Each box is a place where debugging can start.

### Activity — Spot the Failure Layer

A user asks: *"What is my order refund status for order #8821?"*

The agent replies politely: *"I cannot help with weather queries."*

Write two lines:

1. Is the **final sentence** the main problem, or the **path** the agent took?
2. Name one **failure class** that likely applies (you will learn the full list next).

**Suggested answer:** The **path** is wrong — the agent refused a valid order question. Likely **over-refusal** or **wrong tool selection**.

---

## Failure Class — Grouping Defects Before You Fix

- **Official Definition:** A **failure class** is a **category of defect** responsible for an incorrect agent response.
- **In Simple Words:** A **label** for *what kind of mistake* happened — like sorting hospital cases into **fracture**, **fever**, or **allergy** before treatment.
- **Real-Life Example:** At a **railway complaint desk**, delays are filed under **signal fault**, **crew shortage**, or **weather** — each needs a different fix team.

The term appears in articles and internal runbooks. The idea matters more than the label: **name the defect type first**, then pick the matching remedy.

---

## Eight Common LangChain Agent Failure Classes

These are the failure patterns discussed in class for LangChain-style agents. Treat them as a **checklist** when reading traces or user complaints.

### 1. Wrong Tool Selection

The agent calls a tool that does not fit the question.

- **Example:** User asks about **return policy**, but the agent calls **get ticket status** or a **weather API**.
- **Likely causes:** Vague **tool name**, weak **tool description**, unclear **system prompt**.
- **Why it hurts:** Even a fluent final answer is untrustworthy if the wrong backend was used.

### 2. Missing Tool Call

The agent answers **without** calling a tool when it should have.

- **Example:** User asks for **live order status**, but the model guesses from memory instead of calling **get_order_status**.
- **Likely causes:** Prompt does not list tools clearly; no instruction that certain queries **require** a tool.
- **Fix hint (preview):** Sometimes adding the word **must** — *"You must call this tool for order queries"* — changes behaviour.

### 3. Bad Tool Arguments

The right tool is called, but **inputs** are wrong.

- **Official Definition:** **Arguments** are the **parameters** you pass into a tool — order ID, ticket ID, date range, etc.
- **In Simple Words:** You knocked on the **correct door** but asked for the **wrong flat number**.
- **Example:** `get_refund_status(order_id="")` or a mistyped ID — the tool runs but returns garbage.

### 4. Weak Retrieval

- **Official Definition:** **Weak retrieval** means the vector search returns **irrelevant or insufficient chunks** for the user query.
- **In Simple Words:** You opened the right **library**, but pulled the **wrong shelf** — or only half a page.
- **Real-Life Example:** A **coaching centre** chatbot searches past-year papers but fetches **chemistry** notes for a **maths** doubt.

**Common causes:**

| Cause | What to check |
|---|---|
| Corpus missing facts | No amount of tuning fixes missing policy text in source files |
| **K** too low | `k=1` may drop needed context; class often uses **3–5** as a starting range |
| **K** too high | Noise chunks confuse the LLM |
| Wrong **search type** | Try **similarity** vs **MMR** (maximal marginal relevance) and compare |
| Bad **chunking** | Chunk splits can separate the keyword from the answer (demo later) |

- **Remember:** Similarity search is **probabilistic** — it finds *nearby* text, not guaranteed exact phrase matches.

### 5. Hallucinated Final Response

The model answers **confidently** without proper support.

- Often linked to **weak retrieval** — the agent had thin context but still spoke up.
- In non-RAG apps, the model may invent facts when it lacks context.
- **Detection:** User feedback over time; evaluation cases that check **groundedness**; traces showing thin or irrelevant context.

### 6. Over-Refusal and Under-Refusal

- **Refusal:** The agent **declines** to answer — usually because of **guardrails** in the prompt.
- **Over-refusal:** It refuses **valid in-domain** questions — e.g. a **Masai course bot** rejecting a real batch-timing question.
- **Under-refusal:** It answers **out-of-domain** or **unsupported** questions it should block — e.g. random **cricket scores** on a course support bot.

Both are tricky at scale. Production teams watch **refusal rate** over time — if a steady **5%** refusal suddenly becomes **30%**, that is an incident.

### 7. Excessive Tool Calling (Loops)

The agent keeps calling tools again and again — sometimes forever.

- **Example:** API is down; the agent retries without stopping.
- **Fix pattern:** Set **`max_iterations`** (or equivalent loop cap) so the run terminates safely.
- **Real-Life Example:** A **lift** that keeps reopening doors — you need a **maximum retry** before alarm.

### 8. Slow Response (High Latency)

The answer is correct but takes too long.

- Measure **start time** and **end time** per tool call and per full request.
- At scale (millions of queries), manual checking is impossible — you need **observability** (next section).

### Activity — Match Symptom to Failure Class

| Symptom | Failure class |
|---|---|
| Agent cites policy text that never appeared in retrieved chunks | Hallucinated response / weak grounding |
| GST math question routed to document search | Wrong tool selection |
| Valid refund question gets *"I cannot help"* | Over-refusal |
| Agent calls refund API with empty `order_id` | Bad tool arguments |
| Same search tool fires six times until timeout | Excessive tool calling |

Cover the table with a notebook, fill it, then check your labels against the list above.

---

## Final Answer vs Trajectory Debugging

- **Official Definition:** **Trajectory debugging** inspects the **step-by-step path** — tool choices, retrievals, intermediate messages — not only the last string shown to the user.
- **In Simple Words:** Checking **how the student solved the sum**, not only whether the final number is right.
- **Real-Life Example:** A **delivery** failed. Trajectory debugging is tracking **warehouse → hub → rider**; final-answer debugging is only reading *"not delivered"* on the app.

| Debug style | What you compare | Enough for agents? |
|---|---|---|
| **Final answer** | Expected text vs actual text | Sometimes — never alone |
| **Trajectory** | Expected tools, retrievals, refusals vs actual steps | Yes — this is professional practice |

Your **evaluation harness** from the **previous** class is built for trajectory thinking — **expected tools**, traces, and per-step logs.

![Final answer debugging vs trajectory debugging — compare only the last sentence or inspect tools, retrievals, and refusals step by step](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session43/session43-03-trajectory-vs-final-answer.png)

---

## Remediation Strategies by Defect Category

Once you label a **failure class**, apply a **targeted fix** — not a random full prompt rewrite.

| Failure class | Remediation strategy |
|---|---|
| **Wrong tool selection** | **Tool patch** — clearer **tool name** and **description**; improve **system prompt** with examples of which tool fits which query |
| **Missing tool call** | **Prompt patch** — list tools explicitly; add *"You **must** call [tool] for [query type]"*; add more few-shot examples |
| **Bad tool arguments** | **Tool patch** — tighten **tool schema**; document required parameters; validate inputs before the tool runs |
| **Weak retrieval** | **Retrieval tune** — adjust **K**, **search type** (similarity / MMR), **metadata filters**; fix corpus gaps |
| **Hallucinated response** | **Prompt patch** — *answer only from retrieved context*; refuse when context is insufficient |
| **Over-refusal** | **Prompt patch** — **relax** overly strict guardrails for in-domain topics |
| **Under-refusal** | **Prompt patch** — **tighten** rules; clarify what is out of scope |
| **Excessive tool calling** | Set **`max_iterations`**; fix retry logic when APIs fail |
| **Slow response / high latency** | Remove unnecessary tool calls and retrievals; add **caching** for repeated queries |

- **One change at a time:** If three engineers change prompt, tools, and chunks on the same day, nobody knows what helped.
- **Regression risk:** A fix for one case can break three others — that is why you re-run the **full** evaluation set, not only the failures.

![Failure class to remediation map — wrong tool, missing call, weak retrieval, hallucination, loops, and latency each have a targeted patch strategy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session43/session43-04-failure-class-remediation.png)

### Activity — Pick the First Fix

**Case A:** `results.csv` shows five failures. All are arithmetic questions that called **`search_course_policy`** instead of **`calculate_gst`**.

**Case B:** The agent answers baby-product return rules even though **no baby policy** exists in the corpus. Retrieved chunks are empty or irrelevant.

For each case, write:

1. The **failure class**
2. The **first** remediation you would try (**prompt patch**, **tool patch**, or **retrieval tune**)

**Suggested approach:**

- **Case A:** Wrong tool selection → **tool patch** on calculator description + small **prompt patch** with *must call* language.
- **Case B:** Weak retrieval or hallucination → **retrieval tune** first; add **prompt patch** grounding rule *"say I don't know if context is missing."*

---

## Observability and Monitoring

- **Official Definition:** **Observability** is the ability to understand system health from **metrics, logs, and traces** — especially in production.
- **In Simple Words:** **CCTV plus alarms** for your agent — not checking every customer manually.
- **Real-Life Example:** A **Swiggy**-scale chatbot cannot have one engineer timing each chat by hand. Tools plot **latency graphs** automatically.

**What to observe:**

| Signal | Why it matters |
|---|---|
| **Latency** (response time) | Users leave slow chats; SLA breaches cost money |
| **Memory usage** | Leaks or huge contexts can crash the service |
| **Failure count** | Spikes show broken tools or bad deploys |
| **Token usage** | Direct **cost** line on LLM bills |

**Healthy range mental model:**

Imagine a graph of response time per request. Most points sit between **1–2 seconds** — your **healthy band**. When times drift to **3 seconds**, raise a **level 1 alert**. If the issue is temporary, the graph returns to normal. If not, latency keeps climbing — **level 2** at **5 seconds**, **level 3** at **6–7 seconds** for managers.

- You set a **cutoff threshold** — e.g. alert if p95 latency **> 3 seconds**.
- Same pattern applies to **memory**, **error rate**, and **token spikes**.

This connects to the timing logic you added in the **previous** evaluation lab — production teams automate it with dashboards instead of `print` statements.

---

## Prompt Patching, Tool Patching, and Retrieval Tuning

Three vocabulary words for **small, controlled changes** — not rebuilding the whole agent.

### Prompt Patch

- **Official Definition:** A **prompt patch** is a **focused edit** to system or agent instructions — adding, removing, or tightening rules.
- **In Simple Words:** Fixing one paragraph in the **instruction manual**, not rewriting the entire book.
- **Example:** Add *"Do not answer out-of-domain queries strictly"* to reduce under-refusal.

You have done this before when a one-line guardrail changed agent behaviour.

### Tool Patch

- **Official Definition:** A **tool patch** updates a tool's **name, description, schema, or output shape** so the LLM routes calls correctly.
- **In Simple Words:** Rewriting a team member's **job description** so the manager assigns work properly.
- **Example:** Rename `tool1` to `search_return_policy` with a description that mentions **refunds, cancellations, and return windows**.

### Retrieval Tune

- **Official Definition:** **Retrieval tuning** adjusts how documents are **split, embedded, and searched** — chunk size, overlap, K, search algorithm.
- **In Simple Words:** Reorganising **library shelves** so the right chapter lands on the desk.
- **Knobs:** `chunk_size`, `chunk_overlap`, `k`, `search_type`, metadata filters.

**Class demo workflow** (same ShopEasy-style RAG pipeline from earlier labs):

1. **`langchain_rag_ingest.py`** — load policies, split, embed, store in **Chroma**
2. **`langchain_rag_app.py`** — retriever + prompt + LLM chain; ask a fixed question

Only **ingest settings** changed between a **failed** run and a **passing** run on the **same query**.

---

## Quality Metrics — Measuring Agent Health

- **Official Definition:** **Quality metrics** are **measurable indicators** of whether an agent meets expectations across accuracy, safety, speed, and cost.
- **In Simple Words:** The **report card** you track week after week — not gut feeling.
- **Real-Life Example:** A **call centre** tracks **average handle time**, **first-call resolution**, and **complaint rate** — not one manager's mood.

| Metric | What it checks |
|---|---|
| **Response accuracy** | Is the final answer correct? |
| **Tool accuracy** | Did the agent call the **expected tool**? (matches **eval JSON** expected tools from the harness) |
| **Argument accuracy** | Were tool inputs valid and complete? |
| **Retrieval accuracy** | Did search return useful chunks? |
| **Groundedness** | Is the answer supported by retrieved or tool data — not invented? |
| **Refusal accuracy** | Should this query be refused? Did the agent refuse or answer correctly? |
| **Latency** | Average and tail response times |
| **Token utilization** | Tokens consumed per run or per day |

**Watching trends:** If daily tokens rise **30–50%** with no traffic spike, investigate prompt bloat, higher **K**, or runaway tool loops. A **10%** drift might be normal seasonal noise — **2×** growth is not.

**Quantifying improvement:** Re-run the **same runner** on the **same eval cases** after each patch. Compare pass counts and failure-class totals in **results.csv**. That before/after discipline is how teams prove a fix worked — even when the live class focused on concepts and a RAG demo rather than re-scoring every case on screen.

**Knowing when to stop:** Agree a **quality bar** with stakeholders — e.g. *"90% pass on in-domain cases, zero fabrication on out-of-domain, latency under 2 seconds in testing."* Try **10–20 retrieval combinations** in real projects, then stop when metrics meet the bar or **marginal gains** no longer justify **cost and latency**. Endless tweaking without a bar leads to **analysis paralysis**.

---

## Cost vs Latency Trade-Off

- **Official Definition:** A **trade-off** means gaining one benefit by accepting a cost elsewhere — you cannot maximise everything at once.
- **In Simple Words:** **Something for something** — better performance often means paying more or waiting differently.
- **Real-Life Example:** A **high-end laptop** gives speed and battery life you like, but costs **two to three lakh rupees**. You choose how much performance your budget allows.

**Cost vs latency** is discussed heavily in senior engineering reviews for agent systems.

| Change | Quality effect | Cost / latency effect |
|---|---|---|
| Higher **K** (e.g. 3 → 5 chunks) | More context → often better answers | More **input tokens** → higher **bill** and slightly slower |
| **Better / larger LLM** | Stronger reasoning | **Higher per-token price** |
| **Larger context window** | Longer conversations possible | **Premium pricing** from the provider |
| **Smaller chunks** in prompt | Less noise per retrieval | Lower tokens per query |
| **Caching** repeated queries | Same answer quality for repeats | Lower average latency and cost |

You can always buy faster hardware and bigger models — but **budget is finite**. Professional teams pick: *"I accept ~2 second latency and this monthly token budget for this quality level."*

- **Common mistake:** Doubling **K** and **chunk size** together, then wondering why the bill doubled — tune one knob, measure, then decide.

### Activity — Trade-Off Decision

Your agent passes **17 of 20** eval cases. Raising **K** from 3 to 8 fixes two more cases but **doubles** average tokens per query.

1. Will **response accuracy** likely rise?
2. What happens to **token utilization**?
3. One sentence: would you ship this change if your product owner capped cost per query?

There is no single right answer — the exercise is to articulate **quality gained** versus **money spent**.

---

## Hands-On Retrieval Tuning — Chunk Size and Overlap Demo

The instructor re-ran the ShopEasy **RAG pipeline** with different **ingest** settings. The **query stayed the same**:

*"What is the return window for electronics items?"*

### Why small chunks broke the answer

With **`chunk_size=50`** and **`chunk_overlap=10`**:

- The corpus produced **many tiny chunks** (59 in the demo).
- Similarity search matched **"electronics"** in **chunk 2**.
- The actual rule — *"return within seven days"* — lived in **chunk 4**.
- The LLM received a chunk mentioning **electronics** but **not** the return window → *"I don't know based on the provided documents."*

This is **weak retrieval caused by bad chunking**, not a bad LLM.

With **`chunk_size=150`** and **`chunk_overlap=20`**:

- Fewer, richer chunks (21 in the demo).
- The same query retrieved a chunk containing **both** the product category and the **policy sentence**.
- The answer became correct — **same files, same app code**, only **ingest parameters** changed.

**Takeaway:** Wrong **chunk size** or **overlap** can move an app from **useless** to **correct** without touching the LLM model name.

![Chunk tuning demo — chunk_size 50 retrieved electronics but missed the 7-day rule; chunk_size 150 returned the correct answer on the same query](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session43/session43-05-chunk-tuning-electronics-demo.png)

### Retriever tuning in the app file

In **`langchain_rag_app.py`**, the retriever is created like this:

```python
retriever = vector_store.as_retriever(  # Turn Chroma store into a retriever
    search_type="similarity",  # Algorithm: rank by embedding distance
    search_kwargs={"k": 3},  # Return top 3 chunks — try 3, 4, 5 and compare
)
```

You can change **`search_type`** (e.g. try **MMR**) and **`k`** without re-ingesting — but **chunk size** changes require **re-running ingest**.

### Full code — `langchain_rag_ingest.py` (retrieval tuning variant)

Use this after your policy `.md` files exist in `documents/` (from the corpus-creation step in earlier labs). Set **`OPENAI_API_KEY`** in your environment before running.

```python
import shutil  # Delete old Chroma folder when re-ingesting with new chunk settings
from pathlib import Path  # Paths to documents/ and chroma_db/

from langchain_chroma import Chroma  # Vector database wrapper
from langchain_community.document_loaders import DirectoryLoader, TextLoader  # Load .md policy files
from langchain_openai import OpenAIEmbeddings  # Embedding API wrapper
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Split text into chunks

DATA_DIR = Path("documents")  # Folder with return_policy.md etc.
CHROMA_DIR = Path("chroma_db")  # Persisted vectors on disk
COLLECTION_NAME = "e_commerce_policy_docs"  # Collection name inside Chroma
EMBEDDING_MODEL = "text-embedding-3-small"  # Must match the app file at query time

# --- Tuning knobs demonstrated in class ---
CHUNK_SIZE = 150  # Class demo: 50 failed electronics query; 150 fixed it
CHUNK_OVERLAP = 20  # Overlap shares tail characters between neighbouring chunks

if CHROMA_DIR.exists():  # Clean slate when chunk settings change
    shutil.rmtree(CHROMA_DIR)  # Old vectors were built with different splits

loader = DirectoryLoader(  # Load every Markdown policy file
    str(DATA_DIR),
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
)
documents = loader.load()  # List of Document objects
print(f"Original documents loaded: {len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(  # Standard recursive splitter
    chunk_size=CHUNK_SIZE,  # Max characters per chunk
    chunk_overlap=CHUNK_OVERLAP,  # Repeated margin so sentences are not cut in half
    add_start_index=True,  # Track where each chunk started in the source file
)
chunks = text_splitter.split_documents(documents)  # Apply splitting
print(f"Chunks generated: {len(chunks)}")  # Compare runs: 59 vs 21 in class demo

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)  # Same model for ingest and query

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)
vector_store.add_documents(chunks)  # Embed and store every chunk
print(f"Stored {len(chunks)} chunks in '{COLLECTION_NAME}' at '{CHROMA_DIR}'")
```

**How the code works:**

- **`CHUNK_SIZE` / `CHUNK_OVERLAP`** are the main **retrieval tune** levers at ingest time.
- **`shutil.rmtree`** ensures you are not querying **stale vectors** from an old split.
- Print **chunk count** after each experiment — sudden jumps (59 tiny chunks) are a warning sign.
- Re-run **`langchain_rag_app.py`** with the **same question** after each ingest to compare answers.

### Full code — `langchain_rag_app.py` (query + optional prompt patch)

```python
from pathlib import Path  # Optional path constants

from langchain_chroma import Chroma  # Load persisted Chroma
from langchain_core.output_parsers import StrOutputParser  # LLM output → plain string
from langchain_core.prompts import ChatPromptTemplate  # Template with {context} and {question}
from langchain_core.runnables import RunnablePassthrough  # Pass question through unchanged
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # Chat + embeddings

CHROMA_DIR = Path("chroma_db")  # Must match ingest script
COLLECTION_NAME = "e_commerce_policy_docs"  # Must match ingest script
EMBEDDING_MODEL = "text-embedding-3-small"  # Must match ingest script

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)  # Required to query existing vectors

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)

retriever = vector_store.as_retriever(
    search_type="similarity",  # Try "mmr" in your own experiments
    search_kwargs={"k": 3},  # Retrieval tune: compare k=3 vs k=5
)

def format_docs(docs):  # Join retrieved chunks into one context block
    return "\n\n".join(doc.page_content for doc in docs)

prompt = ChatPromptTemplate.from_template(  # Prompt patch target: edit guardrails here
    """You are a helpful customer support assistant for an e-commerce company.
Use only the retrieved context to answer the user's question.
If the answer is present in the context, answer clearly.
If the answer is not present in the context, say: I don't know based on the provided documents.
Do not use outside knowledge.
Do not answer any out-of-domain query strictly.
Mention the source file name wherever possible.

Context:
{context}

Question:
{question}
"""
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)  # Low temperature for factual answers

rag_chain = (
    {
        "context": retriever | format_docs,  # Retrieve then format
        "question": RunnablePassthrough(),  # Original user string
    }
    | prompt
    | llm
    | StrOutputParser()  # Note the parentheses — common syntax mistake
)

question = "What is the return window for electronics items?"  # Same query every tuning run
answer = rag_chain.invoke(question)
print("\nQ:", question)
print("A:", answer)  # Expect grounded 7-day rule after chunk_size=150 ingest
```

**How the code works:**

- **Ingest** controls **what** gets stored; **retriever `k` and `search_type`** control **what** gets fetched at query time.
- **Prompt patch** example in class: added stricter *out-of-domain* language — a behavioural fix separate from chunking.
- **Tool patch** applies to agent tools (name, description, schema) — same idea as sharpening retriever metadata in agent setups.

### Simple Activity — Two-Ingest Comparison

1. Run ingest with **`CHUNK_SIZE=50`**, **`CHUNK_OVERLAP=10`**; run the app question; save the answer in one line.
2. Run ingest with **`CHUNK_SIZE=150`**, **`CHUNK_OVERLAP=20`**; run the same question again.
3. Write one sentence: *Why did similarity search find "electronics" but still fail the first time?*

### Simple Activity — Prompt Patch vs Retrieval Tune

For each issue, circle **prompt patch**, **tool patch**, or **retrieval tune** as the **first** fix:

1. Agent invents baby-item return rules — no baby policy in corpus, retrieval returns junk.
2. Agent uses `search_policy` for a GST calculation question.
3. Agent answers general knowledge questions on a course-only bot.

---

## Optimizing Cost Without Breaking Quality

When the agent works but the **bill** is too high, common levers from class:

| Lever | Idea |
|---|---|
| **Dynamic LLM selection** | Cheap model for simple queries; premium model only for hard ones |
| **Limit tool calls** | Stop redundant retrieval on every turn |
| **Shrink prompts** | Pass only relevant context — not two huge files every time |
| **Caching** | Store answers or retrieval results for repeated questions |
| **Ideal top K** | Do not retrieve more chunks than you need |
| **Smaller chunks** | Fewer tokens per prompt when chunks are right-sized |

**Cost is measured in tokens** — input tokens plus output tokens. Bigger prompts and more chunks mean bigger invoices.

---

## Closing the Module — From Evaluation to Iteration

This session completes the **LangChain agent quality** thread for the current module:

- **Evaluation** tells you **what** failed.
- **Failure classes** tell you **which category** of bug it is.
- **Prompt / tool / retrieval fixes** are **controlled patches**.
- **Metrics** (accuracy, latency, tokens) tell you if life got better.
- **Trade-offs** remind you that **perfect** is expensive — pick a bar and ship.

In the **upcoming** module, the focus shifts toward **multi-agent collaboration**, **deployment**, and platform tools (**N8N**, **CrewAI**, **AutoGen**) — putting agents on **public APIs** with **monitoring** and **governance**. The debugging habits from today still apply: no guesswork, measure, patch one layer at a time.

---

## Key Takeaways

- **Debugging** agents means tracing **workflows** — not only comparing final text to expected text.
- **Failure classes** (wrong tool, missing call, bad arguments, weak retrieval, hallucination, over/under-refusal, loops, slowness) point to **specific remedies**.
- **Prompt patch**, **tool patch**, and **retrieval tune** are small, targeted changes — prefer them over rewriting the whole system.
- **Observability** (latency, memory, failures, tokens) with **threshold alerts** is mandatory at production scale.
- **Chunk size and overlap** can make the **same RAG query** succeed or fail without changing the LLM model.
- **Quality metrics** and **cost–latency trade-offs** help you decide when an agent is **good enough** to ship.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Debugging** | Concept | Find root cause of incorrect behaviour and fix it |
| **Bug** | Concept | Error or unexpected behaviour in code |
| **Failure class** | Concept | Category of defect behind a bad agent response |
| **Trajectory** | Concept | Step-by-step path: tools, retrievals, messages |
| **Wrong tool selection** | Failure class | Agent called an inappropriate tool |
| **Missing tool call** | Failure class | Agent answered without required tool use |
| **Bad tool arguments** | Failure class | Tool called with wrong or empty parameters |
| **Weak retrieval** | Failure class | Search returned irrelevant or insufficient chunks |
| **Hallucinated response** | Failure class | Confident answer not supported by data |
| **Over-refusal** | Failure class | Valid in-domain query rejected |
| **Under-refusal** | Failure class | Out-of-domain query answered anyway |
| **Excessive tool calling** | Failure class | Looping or redundant tool use |
| **Prompt patch** | Practice | Small, focused edit to system / agent instructions |
| **Tool patch** | Practice | Update tool name, description, or schema |
| **Retrieval tune** | Practice | Adjust chunking, K, search type, filters |
| **Observability** | Concept | Metrics, logs, traces for production health |
| **Groundedness** | Metric | Answer supported by retrieved or tool evidence |
| **Token utilization** | Metric | Tokens consumed — direct cost signal |
| **Latency** | Metric | Time per response or per tool call |
| **Cost–latency trade-off** | Concept | Quality/speed improvements vs money and time |
| **`max_iterations`** | Config | Cap on agent loop steps to prevent runaway tools |
| **`chunk_size`** | Param | Max characters per chunk at ingest |
| **`chunk_overlap`** | Param | Shared characters between neighbouring chunks |
| **`search_type`** | Param | Retriever algorithm (e.g. `similarity`, MMR) |
| **`search_kwargs={"k": 3}`** | Param | How many chunks to retrieve |
| **`langchain_rag_ingest.py`** | File | Load, split, embed, persist Chroma |
| **`langchain_rag_app.py`** | File | LCEL RAG chain with guardrail prompt |
| **`RecursiveCharacterTextSplitter`** | Class | LangChain text splitter for chunking |
| **`vector_store.as_retriever()`** | Method | Create retriever from Chroma store |
| **`python3 langchain_rag_ingest.py`** | Command | Rebuild vectors after chunk or corpus changes |
| **`python3 langchain_rag_app.py`** | Command | Run grounded Q&A against persisted Chroma |
| **Caching** | Technique | Reuse prior answers or retrievals to cut latency/cost |
