# Introduction to LangChain: Concepts, Chains, and Prompt Templates

## What We Covered Before and Where We Are Heading

In the previous session, you set up **Ollama** so you can run **open-source LLMs** on your laptop (or use **Ollama Cloud** when you need more power) without paying per token while you practise. You called models from the **terminal** and from **Python** using the same **POST + JSON** pattern you already know from cloud APIs.

That gave you a working **LLM engine**. Today you learn how to **organise** that engine inside a real product. Raw “call the model once and print text” is fine for a demo. It breaks when you need **reusable prompts**, **several steps in order**, **memory**, **document search**, and **tools** — the building blocks of **agentic** applications.

**In this session, you will learn:**
- What **LangChain** is and why teams use it instead of only raw LLM API calls
- Where LangChain sits on the **agentic stack** (between your app and models, databases, tools)
- The mental model: **Runnables** snapped into **chains**
- The **six core components** at overview level (models, prompts, chains, memory, indexes, agents)
- **PromptTemplate** vs hard-coded prompts on the same teaching task
- Your first **LCEL** chain: `prompt | llm | StrOutputParser` with **string output**

---

## Why “Just Call the LLM” Is Not Enough

Many people think an AI app is only: **send prompt → get answer → show user**. That was never enough for serious products.

- **Official Definition:** A **modern LLM application** combines model calls with **pre-processing** (load data, build context), **post-processing** (format, validate, store), and often **memory**, **retrieval**, and **tool use**.
- **In Simple Words:** The LLM is the **brain**, but a real app also needs **hands** (tools), **notes** (memory), and **file cabinets** (documents / vector DB).
- **Real-Life Example:** A **travel booking** site does not only chat. It checks **MakeMyTrip**, **Expedia**, your **itinerary DB**, and **email** — then the LLM explains the result in plain language.

The LLM stays the **brain**; it will not be replaced. But the work **before** and **after** the model call is where projects get messy without structure.

![A real LLM app combines the model brain with tools, memory, documents, and pre/post-processing — not a single chat call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-01-modern-llm-app.png)

**Frameworks** like LangChain exist for the same reason **FastAPI** exists for Python APIs: you *could* build everything by hand, but you would repeat the same wiring again and again.

---

## What Is LangChain?

- **Official Definition:** **LangChain** is an **open-source framework** for building **LLM-powered applications** by connecting **models**, **prompts**, **tools**, **memory**, **retrievers**, and **workflows** in a structured way.
- **In Simple Words:** It is a **toolkit of ready-made blocks** and **connectors** so you compose apps instead of gluing every integration yourself.
- **Real-Life Example:** Think of **IRCTC** as one counter that talks to trains, buses, and hotels — you do not run to each office separately. LangChain is that **middle layer** for AI parts.

LangChain is **one** framework among several; the course starts here because it is widely used and maps cleanly to **single-agent** workflows you will extend later.

![LangChain sits between your app and many backends — one orchestration layer for LLMs, vector DBs, tools, and APIs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-02-langchain-orchestration.png)

| Piece LangChain helps with | Why it matters |
| --- | --- |
| **Prompts** | Reusable templates, not copy-paste strings |
| **Chains** | Step A → B → C in one pipeline |
| **Memory** | Chat remembers context across turns |
| **Retrievers / indexes** | RAG over company docs |
| **Agents** | Model picks **which tool** to run next |
| **Provider switch** | Easier move from OpenAI to Gemini, etc. |

---

## Why Use a Framework Instead of Raw API Calls?

- **Official Definition:** A **framework** supplies shared implementations for repetitive tasks so developers focus on **business logic**.
- **In Simple Words:** Millions of people build the same “call API, parse JSON, retry” code — the framework does that once for everyone.
- **Real-Life Example:** **FastAPI** for Python APIs — you can write HTTP by hand, but FastAPI saves time on routing, validation, and docs.

### Composability and reuse

Only your **business logic** changes between projects; **boilerplate** (HTTP shape, prompt formatting, output parsing) repeats. Frameworks **outsource** that repetition so engineers solve harder problems.

### Orchestration layer on the agentic stack

Picture a **user** on your **website or app** → request hits your **backend** → backend must talk to **LLMs**, **vector DBs**, **weather APIs**, **email**, **embeddings**, and more.

Without LangChain, **you** wire every integration manually — error-prone and slow.

With LangChain, you get an **orchestration layer**:

```
User → UI / mobile app → Your backend → LangChain (orchestration)
                                              ↓
                         LLMs, DBs, tools, embeddings, external APIs
```

- **Official Definition:** **Orchestration** means a central component coordinates many subsystems so they produce one coherent outcome.
- **In Simple Words:** Like the **conductor** in an orchestra — each musician (tool, DB, model) plays their part; the conductor keeps timing.
- **Real-Life Example:** You do not personally call the **violinist**, **drummer**, and **flautist**; you trust the conductor.

LangChain **standardises** how you talk to models and related services so **migrating** (OpenAI today, Gemini tomorrow; one vector DB today, another later) needs **smaller code changes** — a **plug-and-play** feel once you see more examples.

![User request flows through your backend into LangChain, which coordinates LLMs, databases, tools, and embeddings like a conductor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-03-agentic-stack.png)

**Common doubt:** “For one `invoke()` call, LangChain looks the same size as raw OpenAI code.” **True for the simplest demo** — value shows up when you add **templates**, **chains**, **memory**, and **tools**.

---

## The LangChain Mental Model: Runnables and Chains

LangChain apps are built by connecting **small reusable components**.

- **Official Definition:** A **Runnable** is a unit of work that can be **invoked** (and later **streamed** or **batched**) and composed with other runnables.
- **In Simple Words:** One LEGO brick you can snap to the next brick.
- **Real-Life Example:** **Prompt** brick → **LLM** brick → **output parser** brick → **agent** brick → **tool** brick → **database** brick.

Typical flow taught in class:

```
Prompt → LLM → (optional) Agent → Tool → Database
```

Each box is one **runnable**. Arranged in order, they form a **chain**.

### What is a chain?

- **Official Definition:** A **chain** is a **sequence of connected steps** that pass **output of one step as input to the next** — like a pipeline.
- **In Simple Words:** An assembly line where each station finishes one job and hands it to the next.
- **Real-Life Example:** Making **chai**: boil water → add tea → add milk → strain. Order matters.

The word **chain** in LangChain is literal: **linked steps**, not one isolated API call.

The **simplest** LangChain app is often a **chain only** — **no agent, no tools** — just prompt → model → (optional) parser.

![Runnables snap together like LEGO blocks; a chain passes each step’s output to the next — like an assembly line](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-04-runnables-chain.png)

### Runnable operations (preview)

Runnables support **`invoke`**, **`stream`**, and **`batch`**. This session focused on **`invoke`**; streaming and batching come in a follow-up class.

**Try it yourself:** On paper, draw four boxes: `User question`, `PromptTemplate`, `LLM`, `Print answer`. Label arrows “output becomes input.” That is your first mental chain.

---

## Agents, Parallel Work, and Chain Types (Overview)

### Agent (concept)

- **Official Definition:** An **agent** is a component that **decides the next action** (often which **tool** to call) using the LLM’s reasoning.
- **In Simple Words:** The LLM is not only answering — it is **choosing what to do next**.
- **Real-Life Example:** You ask a travel agent: “Weather in Delhi in **Fahrenheit**?” The agent may call a **weather API**, then a **calculator** to convert °C → °F, then reply.

Agents need **LLM reasoning** plus **tools**. LangChain also supports **chain-of-thought** style flows; depth comes in later classes.

![An agent uses the LLM to choose tools — for example weather API then a calculator before replying in Fahrenheit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-05-agent-tools.png)

### Chain patterns mentioned in class

| Pattern | Meaning | Example from class |
| --- | --- | --- |
| **LLM chain** | PromptTemplate → model → (optional) output parser | Today’s `app2.py` |
| **Sequential chain** | A → B → C → D; output feeds next | Summarise doc → translate → email draft |
| **Composite chain** | Branching: after B, maybe X or Y or Z | Different path by condition |
| **Parallel chain** | Independent steps at the same time | YouTube upload: copyright check, captions, and 720p encode **in parallel** |

Parallel steps make sense when tasks **do not depend** on each other’s output — like multiple backend workers after one upload.

![Sequential, parallel, and composite chain patterns — linear pipelines versus independent workers versus branching paths](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-09-chain-patterns.png)

---

## Six Core Components of LangChain

LangChain groups most features under **six** building blocks. Today was **definitions + first code**; later classes go deeper.

![Six LangChain building blocks — models, prompts, chains, memory, indexes for RAG, and agents that pick tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-06-six-components.png)

### 1. Models

LangChain supports more than “one chat model”:

| Model type | Typical use |
| --- | --- |
| **LLMs** | Text generation, general reasoning |
| **Chat models** | Conversations with a **list of messages** (built on LLMs; naming differs) |
| **Embedding models** | Vectors for search / RAG (e.g. small/large embedding models) |

**Provider abstraction:** You talk to **LangChain’s interface**; LangChain talks to OpenAI, Gemini, Ollama, etc. You avoid rewriting every call when the provider changes.

### 2. Prompts

- **Official Definition:** A **prompt** is the **instruction** sent to a model to shape the output.
- **In Simple Words:** The question paper you give the student before they write the answer.
- **Real-Life Example:** “Explain SQL indexes to beginners in simple words.”

**Never hard-code** long prompts if the product must scale — change topic, audience, or tone and you would rewrite code every time.

| Approach | Problem |
| --- | --- |
| **Hard-coded prompt** | Same string in code; change audience = edit code |
| **PromptTemplate** | **Placeholders** `{topic}`, `{audience}`, `{tone}`, `{limit}` filled at runtime |

**PromptTemplate**

- **Official Definition:** A **PromptTemplate** is a **blueprint** with **variables** (placeholders) that becomes a final prompt when values are supplied.
- **In Simple Words:** A **Mad Libs** sentence — only the blanks change.
- **Real-Life Example:** “Explain `{topic}` to `{audience}` in `{tone}` tone, within `{limit}` words.”

![Hard-coded prompts fix one string in code; PromptTemplate fills {topic}, {audience}, {tone}, {limit} at runtime like a reusable blueprint](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-07-prompt-template.png)

**ChatPromptTemplate**

- **Official Definition:** A template that builds a **list of chat messages** (roles like system / human / AI) for **chat models**.
- **In Simple Words:** A script for a **group chat** with fixed roles, not one plain string.
- **Real-Life Example:** System says “You are a polite tutor”; human message is the student question.

Explained in class; **coded** with `PromptTemplate` today, not `ChatPromptTemplate`.

**Example selectors**

Linked to **few-shot prompting**: attach 1–3 example Q&A pairs so the model mimics the style you want.

### 3. Chains

Already covered: **sequence of runnables**. The **LLM chain** pattern = **template + model + optional parser**.

**Output parser**

- Optional. Use when you need a **specific output shape**.
- **String output parser** returns **only the text** your UI needs — not the full API object.

### 4. Memory

- **Official Definition:** **Memory** stores context across **turns** so chains/agents produce **context-aware, coherent** replies over multiple user messages.
- **In Simple Words:** The app **remembers** what you said two messages ago.
- **Real-Life Example:** A travel agent that knows you prefer **vegetarian food** and **morning flights** gives a better itinerary than a generic one.

Without memory, you repeat full history in every prompt → **token cost**, **slow** replies, bad UX.

Types mentioned earlier in the course: **short-term**, **long-term**, **conversational** memory (details in later sessions).

### 5. Indexes (for RAG)

- **Official Definition:** **Indexes** help **organise and retrieve document data**, especially for **RAG** apps backed by **vector databases**.
- **In Simple Words:** Like the **index page at the back of a textbook** — you jump to page 40 instead of reading every page to find “Chapter 5.”
- **Real-Life Example:** Thousands of PDF chunks in a vector DB — an index points to **where** relevant chunks live so search stays **fast**.

RAG flow (recap): chunk documents → **embed** → store in vector DB → on user query, **semantic search** → pass chunks to LLM.

LangChain helps **load** PDFs, CSVs, Excel, **split** chunks, store vectors, and build indexes. Provider-specific index details are handled inside the framework when you use LangChain’s abstractions.

### 6. Agents

- **Official Definition:** **Agents** are **dynamic decision-making** components that **select actions or tools** from user input (via LLM reasoning).
- **In Simple Words:** The model picks **which tool to run**, not you hard-coding every branch.
- **Real-Life Example:** “Book flight + hotel + email confirmation” — agent chooses flight API vs hotel API vs Gmail tool.

Today’s code stayed at **chain** level; agents come with tools in upcoming work.

---

## Hard-Coded Prompt vs PromptTemplate (Same Task)

**Hard-coded** (concept from class):

```text
Explain SQL indexes to beginner students in simple words.
```

Tomorrow you need **Java** for **advanced** students in **technical** tone — you rewrite the whole string.

**Templated:**

```text
Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words
```

Same skeleton; only **variables** change. In production, values often come from **user input fields** (name, age, destination) — a **middle layer** maps user text into template variables before the final prompt goes to the LLM.

**Try it yourself:** Write one hard-coded prompt for “Explain REST API to beginners.” Then rewrite it with `{topic}` and `{audience}` only. List three new topics you can support **without** changing the sentence structure.

---

## Setup: Virtual Environment and Packages

Work in a folder such as `langchain_apps/` with a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain langchain-openai langchain-core
export OPENAI_API_KEY="your-key-here"
```

| Package | Role |
| --- | --- |
| `langchain` | Main framework entry |
| `langchain-openai` | OpenAI chat models (`ChatOpenAI`) |
| `langchain-core` | Core pieces like `PromptTemplate`, output parsers |

**Common mistake:** Installing only `langchain` and forgetting `langchain-openai` → import errors for `ChatOpenAI`.

**Common mistake:** Typo in import path — `langchain_core.prompts`, not `langchain.core.compts`.

---

## App 1 — Direct LLM Call (Hard-Coded Prompt)

This mirrors what you already did with raw OpenAI — useful to see that **simple invoke** alone does not show LangChain’s full power.

**File: `app1.py`**

```python
# Import the OpenAI chat model wrapper from LangChain's OpenAI package
from langchain_openai import ChatOpenAI

# Create a client object; model name must match what your API key can access
client = ChatOpenAI(model="gpt-5.2")

# Hard-coded prompt string — same text every run unless you edit the code
prompt = "Explain SQL indexes to beginner students in simple words."

# invoke sends the prompt to the model and returns a full response object
response = client.invoke(prompt)

# .content holds the assistant's text; other fields hold tokens, model name, etc.
print(response.content)
```

### How the code works

- **`ChatOpenAI`** is LangChain’s wrapper around OpenAI’s chat API.
- **`invoke(prompt)`** returns a **rich object** (content, token usage, model name, ids, …).
- **`print(response.content)`** shows only the answer text — you ignore metadata manually.

**Run:**

```bash
python3 app1.py
```

**Observation:** Line count is similar to a raw OpenAI script — fair question: “Why LangChain?” Answer: **templates and chains** in the next file.

---

## App 1b — PromptTemplate with Manual invoke

Same app, but prompt built from a template (still calling `client.invoke` directly, not LCEL yet).

**Add to a copy of `app1.py` or a separate section:**

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

client = ChatOpenAI(model="gpt-5.2")

# from_template defines placeholders in curly braces
prompt_template = PromptTemplate.from_template(
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy to explain the concept
- Keep the response within {limit} words"""
)

# format() fills placeholders at runtime — values can later come from a web form
final_prompt = prompt_template.format(
    topic="SQL indexes",
    audience="beginners",
    tone="simple",
    limit="200",
)

response = client.invoke(final_prompt)
print(response.content)
```

### How the code works

- **`from_template`** registers variable names matching `{topic}`, `{audience}`, etc.
- **`format(...)`** produces one **final string** prompt.
- Changing **topic** to `FastAPI` or **limit** to `1000` does not require rewriting the template body.

In class, the instructor changed values (e.g. 1000 words) and got a longer answer — proof that **runtime variables** drive behaviour.

---

## LCEL — LangChain Expression Language

- **Official Definition:** **LCEL** (**LangChain Expression Language**) lets you connect runnables with the **pipe operator** `|` into a single **chain**.
- **In Simple Words:** Conveyor belt: station 1 → station 2 → station 3.
- **Real-Life Example:** `prompt | llm | output_parser` — LangChain knows output of **prompt** feeds **llm**, then **parser**.

![LCEL builds a chain with the pipe operator — PromptTemplate, then ChatOpenAI, then StrOutputParser returns a plain string](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-08-lcel-pipeline.png)

You do **not** manually write “step 1 then step 2”; the **`|` syntax** declares order. LangChain runs **A → B → C** automatically.

---

## App 2 — First LCEL Chain with String Output

**File: `app2.py`**

```python
# Chat model from LangChain OpenAI integration
from langchain_openai import ChatOpenAI

# PromptTemplate builds dynamic prompts; StrOutputParser returns plain text only
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM runnable — same model as app1 for fair comparison
llm = ChatOpenAI(model="gpt-5.2")

# Reusable template with four variables
prompt = PromptTemplate.from_template(
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy to explain the concept
- Keep the response within {limit} words"""
)

# Parser extracts only the answer string from the model's response object
output_parser = StrOutputParser()

# LCEL chain: formatted prompt -> model -> string output
chain = prompt | llm | output_parser

# invoke on the chain passes variables into the template step
result = chain.invoke({
    "topic": "SQL indexes",
    "audience": "beginners",
    "tone": "simple",
    "limit": "100",
})

# result is already a string when StrOutputParser is last
print(result)
```

### How the code works

- **`prompt | llm | output_parser`** defines three steps in one expression.
- **`chain.invoke({...})`** passes a **dict** whose keys match template variables (`limit`, not `word_count` — names must match placeholders).
- **`StrOutputParser`** strips metadata so `print(result)` is **only content**, not token counts and model ids.

**Run:**

```bash
python3 app2.py
```

### With vs without `StrOutputParser`

| Version | What `print` shows |
| --- | --- |
| **`app1.py`** (`response` object) | Full object: `.content`, token fields, model name, ids, … |
| **`app2.py`** with parser | **Plain answer string** ready for UI |

![app1.py prints the full response object; app2.py with StrOutputParser returns only the answer text your UI needs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-10-app1-vs-app2.png)

**Common mistake:** Placeholder `{limit}` in template but key `word_count` in `invoke` dict → “missing variables” error. Keys must match **exactly**.

**Common mistake:** Forgetting default values for optional template variables — if the user omits a field, define a **fallback** in your app logic before `invoke`.

**Future methods on chains:** `chain.stream(...)` and `chain.batch(...)` — covered in the next class; same chain, different way to run it.

---

## LangChain vs Raw OpenAI for One-Line Demos

| Situation | Raw OpenAI SDK | LangChain |
| --- | --- | --- |
| Single static prompt | Few lines, equally simple | Few lines, equally simple |
| Many prompts / users / steps | Lots of custom glue | Templates + chains + parsers |
| Switch provider | Rewrite client code | Swap model class, keep chain |
| Add memory, RAG, tools | You design everything | Built-in patterns |

After a few more sessions, the **same** `app2.py` pattern scales by adding runnables on the belt — memory, retriever, agent — without rewriting from scratch.

---

## Provider Abstraction and Local LLMs (Pointer)

Class used **OpenAI** via `langchain-openai`. The same ideas apply if you point LangChain at **Ollama** or another provider — swap the **model runnable**, keep **template | parser** structure. Check LangChain docs for the exact import for your local server.

---

## Key Takeaways

- **LangChain** is an open-source framework that connects **models, prompts, tools, memory, retrievers, and workflows** so real LLM apps stay maintainable.
- Apps are built from **Runnables** linked into **chains**; the simplest useful app is often **PromptTemplate → LLM → (optional) parser** without agents yet.
- **PromptTemplate** beats hard-coded strings when **topic, audience, tone, and limits** change per user.
- **LCEL** (`|`) declares pipelines cleanly; **`StrOutputParser`** gives **string output** your UI can display directly.
- **Next**, you will extend chains with **streaming**, **batch**, **memory**, **retrieval**, and **agents** — today’s chain is the spine.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / command | Meaning |
| --- | --- |
| **LangChain** | Framework for composing LLM applications from reusable parts |
| **Runnable** | Invokable unit of work (prompt, model, parser, tool, …) |
| **Chain** | Ordered runnables; output of one step feeds the next |
| **Orchestration layer** | LangChain coordinates models, DBs, tools, embeddings |
| **PromptTemplate** | Prompt string with `{variables}` filled at runtime |
| **ChatPromptTemplate** | Template producing a list of chat messages |
| **LCEL** | LangChain Expression Language; build chains with `\|` |
| **LLM chain** | Template + model + optional output parser |
| **StrOutputParser** | Returns only text content from model response |
| **`invoke`** | Run chain/runnable once with input dict |
| **`stream` / `batch`** | Token stream or many inputs (next class) |
| **Memory** | Context across conversation turns |
| **Index** | Fast lookup structure for documents in RAG |
| **Agent** | LLM-driven choice of tools/actions |
| **Retriever** | Fetches relevant documents for RAG |
| **Few-shot / example selectors** | Examples embedded to steer model style |
| **Provider abstraction** | Same pattern, different model vendor |
| `pip3 install langchain langchain-openai langchain-core` | Install stack used in class |
| `export OPENAI_API_KEY="..."` | Set key for OpenAI calls |
| `prompt \| llm \| StrOutputParser()` | Basic LCEL pattern |
| `PromptTemplate.from_template("...{x}...")` | Define placeholders |
| `.format(x="value")` | Fill template without LCEL |
| `chain.invoke({"x": "value"})` | Run LCEL chain with variables |
