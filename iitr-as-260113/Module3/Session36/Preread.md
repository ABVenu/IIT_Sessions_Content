# Pre-read: LangChain Environment Setup and First LCEL Chain

## Context from the previous session

In the **previous session** you studied **LangChain** as a composition framework: **Runnables**, **chains**, **PromptTemplate**, and the first **LCEL** pattern:

```text
prompt | llm | StrOutputParser
```

Class examples used **`ChatOpenAI`** and an API key. You also have **Ollama** installed locally (or configured for cloud) from earlier modules.

This session moves from **concept** to **project setup**: an isolated Python environment, a standard folder layout, configuration via **environment variables**, and the same LCEL pattern wired to **`ChatOllama`** instead of a cloud chat model.

**Session objective:** Stand up the LangChain project environment and run a first LCEL chain end-to-end on Ollama.

---

## Why environment setup matters (technical view)

LangChain projects depend on **version-matched Python packages** (`langchain`, `langchain-core`, Ollama integration libraries, and helpers such as **`python-dotenv`**). Installing them into the **system Python** often causes:

- **`ModuleNotFoundError`** when a teammate uses a different machine
- **Version conflicts** between this course repo and other projects on the same laptop
- **Accidental commits** of API keys or base URLs inside `.py` files

The fix is standard in professional Python work: a **virtual environment (`venv`)**, a **repeatable dependency install**, secrets in **`.env`**, and a small **directory layout** so scripts and config stay separated.

---

## 1. Virtual environment (`venv`)

- **Definition:** A **`venv`** is an isolated Python interpreter and `site-packages` directory for one project.
- **Typical workflow:**

```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
pip install -U pip
pip install langchain langchain-core langchain-ollama python-dotenv
```

- **Check:** `which python` should point inside `.venv`, not `/usr/bin/python3`.
- **Deactivate:** `deactivate` when you leave the project.

Only packages installed **after** activation belong to this module’s worktree.

---

## 2. Project layout and `.env`

A minimal collaborative layout:

| Path | Role |
| --- | --- |
| `.venv/` | Local virtual environment (usually **not** committed) |
| `.env` | Machine-local secrets and settings (model name, `OLLAMA_HOST`, cloud API key if used) |
| `.env.example` | Committed template with **empty** or placeholder values |
| `.gitignore` | Must list `.env` and `.venv` |
| `hello_chain.py` (or `chains/`) | Runnable that defines and invokes the LCEL chain |

**`.env` loading:** At the top of your script (or a small `config` module), load variables before constructing the model:

```python
from dotenv import load_dotenv
import os

load_dotenv()
model_name = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")
```

- **Rule:** Never commit real keys or production URLs to Git. Share **`.env.example`**; each developer copies it to **`.env`** locally.

---

## 3. `ChatOllama` — local model as a Runnable

In the previous session the model step was **`ChatOpenAI`**. For Ollama, LangChain provides **`ChatOllama`** (from **`langchain-ollama`**).

| Aspect | `ChatOpenAI` (previous session) | `ChatOllama` (this session) |
| --- | --- | --- |
| Backend | OpenAI API | Ollama server (`localhost` or configured host) |
| Auth | `OPENAI_API_KEY` | Usually none for local; cloud may need key in `.env` |
| Model id | e.g. `gpt-4o-mini` | e.g. `qwen2.5:0.5b` (must match `ollama list`) |
| In LCEL | Same position: middle runnable | Same position: middle runnable |

**Prerequisites before `invoke`:**

1. Ollama daemon running (`ollama serve` or desktop app).
2. Model pulled: `ollama pull <model_name>`.
3. **`ChatOllama(model=...)`** uses the same name as in `ollama list`.

Constructor parameters (host, model) should come from **environment variables**, not hardcoded strings scattered across files.

---

## 4. `ChatPromptTemplate` and LCEL

**`PromptTemplate`** (previous session) produces one formatted **string**. **`ChatPromptTemplate`** builds a **list of chat messages** (e.g. system + human) with placeholders—better aligned with chat models.

Example shape (conceptual):

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise assistant."),
    ("human", "Say hello to {name} in one short sentence."),
])
```

**LCEL** (**LangChain Expression Language**) connects runnables with **`|`**:

```text
chain = prompt | llm | output_parser
```

Data flow:

1. **`invoke({"name": "Priya"})`** → template fills `{name}` → message list
2. **`ChatOllama`** → model response object (`AIMessage`)
3. **`StrOutputParser`** → plain `str` for `print` or UI

---

## 5. `StrOutputParser` and `hello_chain.py`

Without a parser, `chain.invoke(...)` often returns a **message object**, and `print(result)` shows something like `<AIMessage ...>`, not the answer text.

| Chain end | Typical `print` output |
| --- | --- |
| `prompt \| llm` | Full `AIMessage` (content + metadata) |
| `prompt \| llm \| StrOutputParser()` | **String** — answer text only |

**`hello_chain.py`** is the reference script: define `prompt`, `llm = ChatOllama(...)`, `parser = StrOutputParser()`, build `chain`, call `chain.invoke` with a **dict** whose keys match template placeholders **exactly**.

**Validation (success criteria):**

- Run with **at least two** different values for the same variable (e.g. two names).
- Output is **readable text**, not a Python object repr.
- Behaviour is **consistent** (same structure; content changes with input).
- Failures (Ollama stopped, wrong model name, missing env) produce **clear errors** you can trace: venv → packages → Ollama → `.env` → chain.

---

## 6. End-to-end pipeline (reference diagram)

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────┐     ┌──────────────────┐
│  invoke input   │ --> │ ChatPromptTemplate│ --> │ ChatOllama  │ --> │ StrOutputParser  │
│  {"name": "…"}  │     │  fill placeholders│     │  Ollama API │     │  str result      │
└─────────────────┘     └──────────────────┘     └─────────────┘     └──────────────────┘
```

Same mental model as the previous session’s **`app2.py`**; only the **model runnable** and **configuration source** change.

---

## Topics covered in this session

- Create and use a **`venv`** with LangChain + Ollama dependencies  
- Apply **folder** and **`.env`** conventions for team-safe repos  
- Bind **`ChatOllama`** to your Ollama host and model name  
- Compose **`ChatPromptTemplate | ChatOllama | StrOutputParser`**  
- Run and validate **`hello_chain.py`** on multiple inputs  

---

## Terminology quick reference

| Term | Meaning |
| --- | --- |
| **venv** | Project-local Python environment and packages |
| **`python-dotenv`** | Loads key-value pairs from `.env` into `os.environ` |
| **`ChatOllama`** | LangChain chat-model wrapper for Ollama |
| **`ChatPromptTemplate`** | Chat-message template with `{variables}` |
| **LCEL** | Chain syntax using `\|` between runnables |
| **`StrOutputParser`** | Extracts string content from model output |
| **`invoke`** | Single run of a chain with an input dict |
| **`hello_chain.py`** | Minimal end-to-end proof script for the module worktree |

---

## Before class — checklist

- [ ] Ollama installed; at least one model pulled (`ollama list` shows it)  
- [ ] Previous session notes reviewed: **Runnable**, **LCEL**, **`StrOutputParser`**  
- [ ] Empty project folder ready for `venv` and `.env`  
- [ ] Git basics: you understand why **`.env`** must not be pushed  

---

## Self-check (prepare answers in your notebook)

1. List the **order of debugging** if `python hello_chain.py` fails with `ModuleNotFoundError: langchain_ollama`.
2. What is the difference between **`.env`** and **`.env.example`**, and which belongs in version control?
3. If `invoke({"name": "Amit"})` works but `invoke({"student": "Amit"})` raises a missing-variable error, which layer failed—template, model, or parser?

---

## Key points to remember

- **Provider swap** in LCEL: change the **model runnable** (`ChatOpenAI` → **`ChatOllama`**); keep **template | parser** structure.  
- **Configuration** (model name, host, keys) belongs in **`.env`**, not in committed source.  
- **`StrOutputParser`** is required when downstream code expects a **string**, not an `AIMessage`.  
- This chain is the **base pipeline** for later sessions (memory, tools, retrieval).
