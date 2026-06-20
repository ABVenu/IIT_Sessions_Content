# Introduction to LangChain: Concepts Architecture and First Demo

## Context of This Session

In the **previous** session, you installed **Ollama**, pulled a **light local model**, called it from **Python**, compared **local vs Ollama Cloud** on the same prompt, and kept **API keys** safe in **`.env`**. That solved *where the brain lives* — you can reach a model reliably from code.

Today you learn *how to wire that brain into a real product without the project falling apart*. Raw **Ollama API calls** work for one script. They break when you add **reusable prompts**, **parsing**, **memory**, **RAG**, and **tools** — the pieces you already built conceptually in earlier work.

**In this session, you will:**

- Understand what **LangChain** is and **why** teams use a **framework** over scattered API glue
- See where LangChain sits on the **agentic stack** between **model providers** and **your application**
- Learn the **Runnable** mental model and how **chains, agents, tools, memory, and retrievers** fit one **single-agent** workflow
- Distinguish **LangChain Core** from **Community** packages for typical projects
- Build or follow a **first LCEL chain**: **PromptTemplate → ChatOllama → StrOutputParser**

---

## Why “Just Call the LLM” Is Not Enough

Many people think an AI app is only: **send prompt → get answer → show user**. That was never enough for serious **agentic** products.

- **Official Definition:** A **modern LLM application** combines model calls with **pre-processing** (load data, build context), **post-processing** (format, validate, store), and often **memory**, **retrieval**, and **tool use**.
- **In Simple Words:** The LLM is the **brain**, but a real app also needs **hands** (tools), **notes** (memory), and **file cabinets** (documents / vector DB).
- **Real-Life Example:** Your college **hostel FAQ assistant** does not only chat. Week three it needs **mess-menu API** lookup; week five **RAG** over a handbook; week seven **conversation memory**. Each feature repeats the same five steps — prompt, model, parse, maybe retrieve — unless you standardise them.

![A real LLM app combines the model brain with tools, memory, documents, and pre/post-processing — not a single chat call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-01-modern-llm-app.png)

**Frameworks** like LangChain exist for the same reason **FastAPI** exists for Python APIs: you *could* build everything by hand, but you would repeat the same wiring again and again.

- **Common doubt:** *"I already call Ollama from Python — isn't that enough?"* — For one demo, yes. For twelve features across twelve files, copy-paste prompts and fragile `split()` parsing become unmaintainable.

> **[ Student Activity ]**
>
> **Prompt or Framework?**
>
> Your placement-cell chatbot has three Python files: one hard-codes a policy prompt, one calls **Ollama** for mess summaries, one slices replies with `split()` when format drifts. List **three pains** you would hit if you add **RAG** next without a framework — e.g. prompt wording out of sync, parser breaks on polite greetings, demo vs production scripts diverge.

---

## What Is LangChain?

- **Official Definition:** **LangChain** is an **open-source framework** for building **LLM-powered applications** by connecting **models**, **prompts**, **tools**, **memory**, **retrievers**, and **workflows** in a structured, composable way.
- **In Simple Words:** It is a **toolkit of ready-made blocks** and **connectors** so you compose apps instead of gluing every integration yourself.
- **Real-Life Example:** Think of **IRCTC** as one counter that talks to trains, buses, and hotels — you do not run to each office separately. LangChain is that **middle layer** for AI parts in **agentic applications**.

LangChain addresses the class of problems where a model does not only chat — it participates in a **longer workflow** with prompts, tools, memory, and retrieval.

![LangChain orchestrates your app with LLM providers (Ollama, cloud APIs), vector DBs, tools, and more — like one IRCTC counter for many services](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-02-langchain-orchestration.png)

| Piece LangChain helps with | Why it matters |
| --- | --- |
| **Prompts** | Reusable templates, not copy-paste strings |
| **Chains** | Step A → B → C in one pipeline |
| **Memory** | Chat remembers context across turns |
| **Retrievers** | **RAG** over company or campus docs |
| **Agents** | Model picks **which tool** to run next |
| **Provider switch** | Swap **Ollama** for cloud — smaller code change |

---

## Why Use a Framework Instead of Raw API Calls?

- **Official Definition:** A **framework** supplies shared implementations for repetitive tasks so developers focus on **business logic**.
- **In Simple Words:** Millions of people build the same “call API, parse JSON, retry” code — the framework does that once for everyone.
- **Real-Life Example:** **FastAPI** for Python APIs — you can write HTTP by hand, but FastAPI saves time on routing, validation, and docs.

### Composability and maintainability

Only your **business logic** changes between projects; **boilerplate** (HTTP shape, prompt formatting, output parsing) repeats. **Composability** means small pieces **snap together**; **maintainability** means you change wording in **one template**, not three scripts.

| Approach | Good for | Pain when you grow |
| --- | --- | --- |
| One-off API script | Quick experiments | Copy-paste prompts everywhere |
| Framework (LangChain) | Composable agents | Learning curve upfront — pays back fast |
| Giant monolith file | Demos only | Nobody can debug it |

**Common mistake:** Judging LangChain on a **one-line** `invoke()` — value appears when you add **templates**, **chains**, **memory**, and **tools**.

---

## Where LangChain Sits on the Agentic Stack

Picture a **three-storey building**:

- **Ground floor — Model providers:** **Ollama** on your laptop, **Ollama Cloud**, Groq, OpenAI — whatever engine produces text.
- **Middle floor — LangChain:** Reusable **prompt templates**, **chains**, **agents**, **tools**, **memory**, and **retrievers** that snap together.
- **Top floor — Your application:** Hostel rules, placement workflows, the UI your user sees.

LangChain does **not** replace the model. It does **not** replace your business logic. It gives you a **common language** for the middle floor.

- **Official Definition:** **Orchestration** means a central component coordinates many subsystems so they produce one coherent outcome.
- **In Simple Words:** Like the **conductor** in an orchestra — each musician (tool, DB, model) plays their part; the conductor keeps timing.
- **Real-Life Example:** When you swap from a local **light model** to **Ollama Cloud** for a demo, you change **one model binding** — not every prompt string in the project.

```
User → UI / app → Your backend → LangChain (orchestration)
                                      ↓
                     LLMs, vector DBs, tools, embeddings, external APIs
```

![User request flows through your backend into LangChain, which coordinates LLMs, databases, tools, and embeddings like a conductor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-03-agentic-stack.png)

---

## The Runnable Mental Model and Chains

LangChain apps are built by connecting **small reusable components**.

- **Official Definition:** A **Runnable** is a unit of work that accepts an **input**, performs work, and returns an **output** — and can be **composed** with other runnables.
- **In Simple Words:** One LEGO brick you snap to the next brick.
- **Real-Life Example:** **Prompt** brick → **LLM** brick → **output parser** brick — like stations on the **Delhi Metro**: you board at one stop, interchange, exit at the next. You do not rebuild the track for every trip.

### What is a chain?

- **Official Definition:** A **chain** is a **sequence of connected steps** where **output of one step becomes input to the next** — a pipeline.
- **In Simple Words:** An assembly line where each station finishes one job and hands it to the next.
- **Real-Life Example:** Making **chai**: boil water → add tea → add milk → strain. Order matters.

The **simplest** useful LangChain app is often a **chain only** — **no agent, no tools** — just **prompt → model → (optional) parser**.

![Runnables snap together like LEGO blocks; a chain passes each step’s output to the next — like an assembly line](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-04-runnables-chain.png)

Runnables support **`invoke`**, **`stream`**, and **`batch`**. This session focuses on **`invoke`**; streaming and batching come in upcoming hands-on work.

> **[ Student Activity ]**
>
> **Draw Your First Chain**
>
> On paper, draw four boxes: `User question`, `PromptTemplate`, `LLM`, `Print answer`. Label arrows *"output becomes input."* That is your first mental chain before you write code.

---

## LangChain’s Modular Surface — One Single-Agent Workflow

LangChain’s modules map cleanly to ideas you already know from building **tool agents** and **RAG** pipelines. Together they describe one **coherent single-agent workflow**:

| LangChain module | Role in a single-agent app |
| --- | --- |
| **Chains** | Fixed steps in order — prompt, then model, then parse |
| **Agents** | Model **chooses tools** based on the question |
| **Tools** | External actions — APIs, calculators, weather |
| **Memory** | Short-term chat history across turns |
| **Retrievers** | **RAG** — fetch relevant chunks before answering |

Picture one student question flowing through the system:

1. **Retriever** (optional) fetches handbook chunks for *"guest-entry timing?"*
2. **PromptTemplate** fills `{question}` and `{context}` slots.
3. **LLM** (**ChatOllama**) generates an answer.
4. **Output parser** returns clean text for the UI.
5. **Memory** (later) remembers the student's hostel block so they do not repeat it.

Today is the **map of that building** — not moving all the furniture yet. You will extend this spine with tools, memory, and RAG in upcoming labs.

![Six LangChain building blocks — models, prompts, chains, memory, indexes for RAG, and agents that pick tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-06-six-components.png)

### Agents (overview only)

- **Official Definition:** An **agent** is a component that **decides the next action** (often which **tool** to call) using the LLM’s reasoning.
- **In Simple Words:** The LLM is not only answering — it is **choosing what to do next**.
- **Real-Life Example:** *"Weather in Delhi in Fahrenheit?"* — agent may call a **weather API**, then a **calculator** to convert °C → °F, then reply.

![An agent uses the LLM to choose tools — for example weather API then a calculator before replying in Fahrenheit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-05-agent-tools.png)

---

## LangChain Core vs Community

LangChain splits into packages on purpose — know **which box** an import comes from when debugging.

| Package | What it is | Think of it as |
| --- | --- | --- |
| **LangChain Core** (`langchain-core`) | Stable building blocks: **Runnables**, **LCEL**, **PromptTemplate**, **StrOutputParser**, base abstractions | **Engine and chassis** |
| **LangChain Community** (`langchain-community`) | Integrations — vector stores, document loaders, some legacy model wrappers | **Optional accessories** |
| **Provider packages** (e.g. `langchain-ollama`) | Dedicated bindings for **Ollama**, OpenAI, etc. | **Brand-specific connector** |

For a typical cohort project you need **Core** plus the **provider package** for your model (**`langchain-ollama`** for local Ollama). Pull **Community** integrations only when you need them — e.g. a specific vector store — not every package on PyPI.

- **Common mistake:** Installing every LangChain-related package before a minimal chain — environment conflicts and import confusion.
- **Common mistake:** Importing a **Community** vector-store helper for a chain that only needs **prompt + model + parser** today.

> **[ Student Activity ]**
>
> **Core or Community?**
>
> For this week's minimal **PromptTemplate → ChatOllama → StrOutputParser** chain, list which packages you actually need (`langchain-core`, `langchain-ollama`) and name one **Community** integration you would add **later** when you build **RAG** — not today.

---

## PromptTemplate and ChatPromptTemplate

Prompts should not live as scattered **f-strings** across files. You define **slots** once and reuse them.

### PromptTemplate

- **Official Definition:** A **PromptTemplate** is a **blueprint** with **variables** (placeholders) that becomes a final prompt when values are supplied at runtime.
- **In Simple Words:** A **Mad Libs** sentence — only the blanks change.
- **Real-Life Example:** *"Explain `{topic}` to `{audience}` in `{tone}` tone, within `{limit}` words."*

![Hard-coded prompts fix one string in code; PromptTemplate fills {topic}, {audience}, {tone}, {limit} at runtime like a reusable blueprint](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-07-prompt-template.png)

### ChatPromptTemplate

- **Official Definition:** A template that builds a **list of chat messages** (roles like **system**, **human**, **assistant**) for **chat models**.
- **In Simple Words:** A script for a **group chat** with fixed roles, not one flat string.
- **Real-Life Example:** System says *"You are a polite hostel helpdesk assistant"*; human message is the student's question.

Today's demo uses **`PromptTemplate`** for clarity. **`ChatPromptTemplate`** is the same idea with **message roles** — you will use it when system instructions and user turns need separate slots.

### Hard-coded vs templated (same task)

**Hard-coded:**

```text
Explain REST APIs to beginner students in simple words.
```

Tomorrow you need **SQL indexes** for **advanced** students in **technical** tone — you rewrite the whole string.

**Templated:**

```text
Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words
```

Same skeleton; only **variables** change. In production, values often come from **user input** or your API — a middle layer maps them into template variables before the model call.

> **[ Student Activity ]**
>
> **Template Upgrade**
>
> Write one hard-coded prompt for *"Explain vector databases to beginners."* Rewrite it with `{topic}` and `{audience}` only. List three new topics you can support **without** changing the sentence structure.

---

## LCEL and the Pipe Operator

- **Official Definition:** **LCEL** (**LangChain Expression Language**) lets you connect **Runnables** with the **pipe operator** `|` into a single **chain**.
- **In Simple Words:** A **conveyor belt**: station 1 → station 2 → station 3.
- **Real-Life Example:** `prompt | llm | output_parser` — LangChain knows output of **prompt** feeds **llm**, then **parser**.

![LCEL chain flow with LangChain and Ollama — input dictionary through prompt template, ChatOllama at localhost:11434, StrOutputParser to plain string](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-02-lcel-chain-flow.png)

The diagram shows **ChatPromptTemplate**; today's demo uses **PromptTemplate** — the **`|`** pipe and step order work the same way.

You do **not** manually write *"step 1 then step 2"*; the **`|` syntax** declares order. LangChain runs **A → B → C** automatically.

Think of the **dosa counter at Saravana Bhavan**: the **template** is the standard order form; the **cook** is the model; the **parser** is the server who plates consistently so billing always sees the same dish shape.

---

## Output Parsers and Predictable String Output

Models return **rich objects** — text, token counts, model name, metadata. Your UI usually needs **plain text**.

- **Official Definition:** An **output parser** converts the model's raw reply into a **clean, predictable form** for downstream steps.
- **In Simple Words:** It removes the extra packaging and gives only the answer text.
- **Real-Life Example:** When you order from Swiggy, you eat the food — not the bag and bill. **`StrOutputParser`** gives only the useful part.

- **Official Definition:** **StrOutputParser** extracts **text content** from the model response and returns a Python **string**.
- **In Simple Words:** Strips fluff like *"Certainly! Here is your answer:"* patterns when configured, and always returns a string your app can print or send to the UI.

| Version | What `print` shows |
| --- | --- |
| Raw `invoke` on model (no parser) | Full response object with `.content`, metadata, … |
| Chain ending in **`StrOutputParser`** | **Plain answer string** ready for UI |

![Without StrOutputParser, invoke returns a full response object with metadata; with StrOutputParser, the chain returns a plain answer string ready for your UI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-10-app1-vs-app2.png)

In this session, **`template_only.py`** reads **`.content`** manually (left side of the diagram); **`first_chain.py`** pipes through **`StrOutputParser`** so the result is already a string (right side).

**Common mistake:** Placeholder `{limit}` in template but key `word_count` in `invoke` dict — keys must match **exactly**.

---

## Setup: Environment and Packages

Work in a folder such as `langchain_intro/` with a virtual environment. **Ollama must be running** with your model pulled (e.g. `qwen2.5:0.5b` from your local setup).

```bash
python3 -m venv venv
source venv/bin/activate
pip install langchain-core langchain-ollama
```

On Windows:

```bash
python3 -m venv venv
venv\Scripts\activate
pip install langchain-core langchain-ollama
```

| Package | Role |
| --- | --- |
| `langchain-core` | **PromptTemplate**, **StrOutputParser**, **LCEL**, Runnable base |
| `langchain-ollama` | **ChatOllama** — LangChain wrapper for your **Ollama** server |

**Common mistake:** Forgetting to start **Ollama** before running Python — `connection refused` on `localhost:11434`.

---

## Step 1 — Raw Ollama Call (What You Already Know)

This mirrors your **previous** Python work — useful to see the baseline before adding LangChain structure.

**File: `raw_ollama.py`**

```python
# Import Ollama chat helper — same pattern as your dual-mode script
from ollama import chat  # Local chat function hitting localhost:11434

# Hard-coded prompt — same text every run unless you edit code
user_question = "Explain REST APIs to beginner students in simple words."

# Call the model with a single user message
response = chat(
    model="qwen2.5:0.5b",  # Must match a model from `ollama list`
    messages=[{"role": "user", "content": user_question}],  # One user turn
)

# Extract assistant text from the response dict
answer = response["message"]["content"]  # Plain string answer
print(answer)  # Show result in terminal
```

### How the code works

- **`chat()`** sends JSON to your local **Ollama** server — no LangChain yet.
- **`model`** must match a tag you pulled with `ollama pull`.
- **`messages`** is the chat format Ollama expects.
- You manually built the prompt string and manually read `["message"]["content"]`.

**Run:** `python3 raw_ollama.py`

---

## Step 2 — PromptTemplate Before LCEL

Same task, but the prompt is **reusable** — still calling the model directly, not piping yet.

**File: `template_only.py`**

```python
# LangChain Core — prompt building blocks live here
from langchain_core.prompts import PromptTemplate  # Reusable prompt with {placeholders}

# Ollama integration for LangChain
from langchain_ollama import ChatOllama  # Runnable wrapper around Ollama chat models

# Create the model runnable — connects to local Ollama
llm = ChatOllama(
    model="qwen2.5:0.5b",  # Same local model tag as raw script
    base_url="http://localhost:11434",  # Default Ollama address
    temperature=0.3,  # Lower = more focused answers for teaching demos
)

# Define template once — placeholders match keys you will fill later
prompt_template = PromptTemplate.from_template(
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words"""
)

# format() fills placeholders at runtime — values can come from a web form later
final_prompt = prompt_template.format(
    topic="REST APIs",  # Subject for this run
    audience="beginners",  # Who the answer is for
    tone="simple",  # Writing style
    limit="150",  # Word cap as a string
)

# invoke on the LLM runnable with the finished prompt string
response = llm.invoke(final_prompt)  # Returns a message object, not plain str
print(response.content)  # .content holds assistant text — you extract manually
```

### How the code works

- **`PromptTemplate.from_template`** registers `{topic}`, `{audience}`, `{tone}`, `{limit}`.
- **`format(...)`** produces one **final string** before the model sees it.
- **`ChatOllama`** is a **Runnable** — same model as raw Ollama, but LangChain-shaped.
- You still manually read **`.content`** — no parser yet.

Change **`topic`** to `"SQL indexes"` or **`limit`** to `"300"` without rewriting the template body.

---

## Step 3 — First LCEL Chain (Instructor Demo)

**File: `first_chain.py`** — the capstone pattern for this session.

```python
# Chat model wrapper for Ollama — provider-specific package
from langchain_ollama import ChatOllama  # Runnable LLM bound to local Ollama

# Core prompt and parser components
from langchain_core.prompts import PromptTemplate  # Template with {variable} slots
from langchain_core.output_parsers import StrOutputParser  # Returns plain string only

# LLM runnable — swap model name here when you change Ollama tags
llm = ChatOllama(
    model="qwen2.5:0.5b",  # Light model for laptop practice
    base_url="http://localhost:11434",  # Where Ollama listens
    temperature=0.3,  # Slightly deterministic for classroom demos
)

# Reusable template — same skeleton for many topics
prompt = PromptTemplate.from_template(
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words"""
)

# Parser strips metadata — chain output becomes a Python string
output_parser = StrOutputParser()  # Last step in the pipeline

# LCEL: formatted prompt -> model -> string output
chain = prompt | llm | output_parser  # Pipe declares order left to right

# invoke passes a dict — keys must match template placeholder names exactly
result = chain.invoke({
    "topic": "REST APIs",  # Fills {topic}
    "audience": "beginners",  # Fills {audience}
    "tone": "simple",  # Fills {tone}
    "limit": "150",  # Fills {limit}
})

# result is already a plain string because StrOutputParser is last
print(result)  # Safe to send to a UI or log file
```

### How the code works

- **`prompt | llm | output_parser`** defines three **Runnables** in one expression.
- **`chain.invoke({...})`** passes variables into the template step automatically.
- **`StrOutputParser`** means `result` is a **string** — not a message object.
- Adding a fourth step later (e.g. logging or a retriever) means extending the pipe — not rewriting three scripts.

**Run:** `python3 first_chain.py`

> **[ Student Activity ]**
>
> **Chain Experiment**
>
> Run `first_chain.py` with `topic="vector databases"` and `limit="100"`. Change only `limit` to `"400"` and run again. Note how the template stays fixed while **runtime variables** drive behaviour — that is **composability** in action.

---

## Raw Ollama vs LangChain Chain

| Situation | Raw Ollama `chat()` | LangChain LCEL chain |
| --- | --- | --- |
| Single static prompt | Few lines, equally simple | Few lines, equally simple |
| Many prompts / users / steps | Lots of custom glue | Templates + chains + parsers |
| Swap local ↔ cloud model | Rewrite client setup | Swap **ChatOllama** config, keep chain |
| Add memory, RAG, tools | You design everything | Extend the pipe with new Runnables |

The user may see **similar answers** today. The second setup is **worth the structure** when you add a fourth step — logging, retrieval, or a tool hook — without copy-pasting the first three.

---

## Key Takeaways

- **LangChain** is an open-source **framework** for **agentic applications** — it connects **models, prompts, tools, memory, and retrievers** so projects stay **composable** and **maintainable**.
- LangChain sits **between model providers** (like **Ollama**) and **your application logic** as an **orchestration layer**.
- Apps are built from **Runnables** linked into **chains**; today's spine is **PromptTemplate → ChatOllama → StrOutputParser**.
- **LangChain Core** holds stable abstractions; **provider packages** (`langchain-ollama`) and **Community** integrations are added **when needed**.
- In upcoming work you will extend this chain with **memory**, **retrieval**, **tools**, and **agents** — the same **LCEL** pipe grows instead of rewriting from scratch.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / command | Meaning |
| --- | --- |
| **LangChain** | Framework for composing LLM applications from reusable parts |
| **Runnable** | Component that takes input, returns output, and can be chained |
| **Chain** | Ordered runnables; output of one step feeds the next |
| **Orchestration layer** | LangChain coordinates models, DBs, tools, embeddings |
| **LangChain Core** | `langchain-core` — PromptTemplate, LCEL, StrOutputParser |
| **LangChain Community** | Optional integrations — vector stores, loaders, legacy wrappers |
| **langchain-ollama** | **ChatOllama** binding for local/cloud Ollama |
| **PromptTemplate** | Prompt string with `{variables}` filled at runtime |
| **ChatPromptTemplate** | Template producing a list of chat messages (system/human/…) |
| **LCEL** | LangChain Expression Language; build chains with `\|` |
| **StrOutputParser** | Returns only text content from model response |
| **`invoke`** | Run chain/runnable once with input dict |
| **Agent** | LLM-driven choice of tools/actions |
| **Retriever** | Fetches relevant documents for RAG |
| **Memory** | Context across conversation turns |
| `pip install langchain-core langchain-ollama` | Minimal stack for today's demo |
| `prompt \| llm \| StrOutputParser()` | Basic LCEL pattern |
| `PromptTemplate.from_template("...{x}...")` | Define placeholders |
| `chain.invoke({"x": "value"})` | Run LCEL chain with variables |
| `ollama list` | Confirm local model tag matches `ChatOllama(model=...)` |
