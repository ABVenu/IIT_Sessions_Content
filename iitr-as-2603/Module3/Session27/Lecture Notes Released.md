# Open-Source LLMs

## Context of This Session

In the **previous session**, you learned how **agents fetch live data** through **REST APIs** — **HTTP methods**, **status codes**, **JSON** parsing in Python, and **mapping API fields** into **downstream LLM prompts** (for example, campus weather for event planning). When you called an LLM, inference still ran on a **remote cloud API** such as **Groq** — not on your laptop.

Today you explore **open-source LLMs**: why they matter, how to **choose** between models, when **local** beats **cloud**, and how to **install Ollama**, run a **light model**, and call it from **Python** using the same **OpenAI-compatible** pattern you already know. You also set up **Ollama Cloud** and **`.env`** files so API keys stay out of Git.

**In this session, you will:**

- **Understand** paid vs open-source models and how **benchmarks** help you pick the right model
- **Compare** cloud vs local LLM trade-offs for **latency**, **privacy**, and **cost**
- **Install and validate** Ollama with a laptop-friendly model
- **Call Ollama from Python** for chat completion (local and cloud)
- **Store API keys safely** in `.env` so the cohort can reproduce setup without leaking secrets

---

## Paid vs Open-Source LLMs

Until now, your main provider was **Groq** — a cloud platform hosting open-source weights. Other popular options (**GPT**, **Gemini**, **Claude**) are **paid API-only** models: you cannot download the weights; you pay per token through an API key.

- **Official Definition:** An **open-source LLM** has **publicly downloadable weights** you can run on your own hardware or through tools like **Ollama**.
- **In Simple Words:** Paid models are like **Netflix** — you stream, you never own the file. Open-source models are like **buying the DVD** — you can play it on your own player.
- **Real-Life Example:** A **startup** prototyping chat features uses a tiny local model for free demos; a **bank** may still prefer a hosted enterprise cloud for compliance — but both may use the **same Python calling pattern**.

| Paid API models (GPT, Gemini, Claude) | Open-source models (Llama, Qwen, DeepSeek, Gemma) |
|---|---|
| Higher benchmark scores on hard tasks | Downloadable and self-hostable |
| Pay per input/output token | Free on your own machine (you pay with RAM and electricity) |
| Data leaves your device during inference | Local run keeps prompts on your laptop |
| No weight download | Available on **Ollama**, Groq, Azure Foundry, etc. |

- **Platform-agnostic code:** Whether you use Groq, OpenAI, Azure, or Ollama, the shape is the same — `client.chat.completions.create` with `messages` (system/user roles). You mostly change **client**, **base URL**, and **model name**.
- **Common doubt:** *"If Groq is free in class, why learn local?"* — Real projects face **privacy**, **latency**, and **offline** needs that a remote API cannot always satisfy.

---

## How to Compare Models — Benchmarks

When a customer asks *"Why model A over model B?"*, you need more than personal preference — you need **benchmarks**.

- **Official Definition:** An **LLM benchmark** is a **standardized test suite** that scores models on tasks like reasoning, coding, or truthfulness so results are comparable across providers.
- **In Simple Words:** Benchmarks are like **board exam mark sheets** for AI models — same paper, different students.
- **Real-Life Example:** Choosing between two **placement-prep chatbots** — you pick the model with a higher **MMLU** score if factual accuracy matters most.

| Benchmark | What it measures |
|---|---|
| **MMLU** | Broad knowledge and reasoning across many subjects |
| **SWE-bench** | Software engineering — can the model fix real GitHub issues? |
| **HellaSwag** | Common-sense completion of everyday situations |
| **TruthfulQA** | Does the model answer truthfully instead of sounding confident but wrong? |
| **ARC** | Science exam-style reasoning questions |

- **Leaderboards** (for example, papers-with-code style sites) plot models side by side — useful when thousands of open-source models exist and you cannot try each one manually.
- **Cost vs quality:** A stronger model often costs **more per token** on paid APIs. Benchmarks plus **cost tables** justify your choice to stakeholders.
- **Common mistake:** Picking the biggest model for every task — a **0.5B local model** may match a **70B cloud model** on simple prompts like *"What is 2 + 2?"*

---

## Cloud vs Local — When Each Wins

Before installing Ollama, understand **why** teams run models locally at all.

- **Official Definition:** A **cloud LLM** runs on a provider's remote servers; a **local LLM** runs on **your machine** (CPU/GPU/RAM on your laptop or workstation).
- **In Simple Words:** Cloud = order from **Swiggy**; local = cook in your **hostel kitchen** — nobody outside sees your ingredients if you cook at home.
- **Real-Life Example:** **Tesla** cannot wait for an API round-trip to America before braking — on-device models decide in milliseconds. A **bank developer** typing confidential notes in VS Code may not want that text sent to a third-party API.

![Cloud LLM sends prompts to remote servers; local Ollama runs on your laptop for privacy and free practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-01-cloud-vs-local.png)

| Cloud LLM (Groq, Ollama Cloud, OpenAI API) | Local LLM (Ollama on laptop) |
|---|---|
| Stronger reasoning on hard multi-step tasks | Data stays on device — better **privacy** |
| No local RAM/GPU burden | **Free** practice — no per-token bill |
| Network latency on every request | **Low latency** after model is loaded (especially small models) |
| Subscription or usage limits | Model size limited by your **RAM** |

### Limitations of API-only cloud calls

- **Latency:** Prompt travels to remote servers and back — fine for chat apps, too slow for **real-time control** (vehicles, robotics, some games).
- **Privacy:** Your prompt may be logged or processed on third-party infrastructure — risky for **PII**, **financial**, or **legal** text.
- **Cost at scale:** Free tiers help learning; production usage is billed per token.

### Enterprise middle ground — Azure Foundry

Large companies often avoid calling OpenAI directly from employee laptops. Instead they deploy models on **Microsoft Azure Foundry** — GPT, DeepSeek, and open-source models hosted inside Azure.

- **Official Definition:** **Azure Foundry** is Microsoft's portal to **deploy and call** many LLMs inside an **Azure subscription** with enterprise controls.
- **In Simple Words:** Same GPT-style models, but the **kitchen is inside your company's cloud account**, not on OpenAI's public website.
- **Real-Life Example:** A retailer already on **Azure** adds a GPT deployment for internal tools — developers still use `client.chat.completions.create`, but point to an **Azure endpoint** and **Azure API key**.

- **Same code pattern:** Only **endpoint** and **API key** change — messages, roles, and JSON responses stay familiar.
- **Not fully on-prem:** Data still lives in cloud regions (often abroad) — but enterprises trust **their Azure contract** more than a direct consumer API.

---

## Why Local LLMs — and What Ollama Does

**Ollama** is the tool this course uses to run open-source models on your laptop.

- **Official Definition:** **Ollama** is an open-source tool to **download, run, and manage** LLMs locally. It exposes a **local HTTP API** at `http://localhost:11434` so terminal, Python, and LangChain can call it like any cloud API.
- **In Simple Words:** Ollama is **app store + player** for AI models — `ollama pull` downloads, `ollama run` or Python talks to it.
- **Real-Life Example:** Private placement notes stay on your machine with a local model; **Ollama Cloud** gives a **bigger model** when your laptop is too small.

| Why use local | Why use cloud (Groq / Ollama Cloud) |
|---|---|
| Free practice, no per-token bill | Stronger reasoning on hard tasks |
| Privacy — data stays on device | Models too large for student laptops |
| Learn that LLM = software + weights | Faster provider infrastructure on big models |

- **Upcoming work:** **LangChain** will plug into Ollama the same way it plugs into Groq — today you build that entry point.

---

## Install Ollama and Validate with a Light Model

Install **once** per machine, then validate with CLI before any Python.

### Windows

- Go to [https://ollama.com/download](https://ollama.com/download) and download the Windows installer (~1.3–1.4 GB).
- Run the installer — Ollama usually starts in the background automatically.
- Open **PowerShell** and run `ollama --version`.
- Check the **system tray** for the Ollama icon — that means the Windows service is running.
- **If `ollama` is not recognized:** close and reopen the terminal, or restart the PC so PATH updates apply.

### macOS

- Download the app from [ollama.com/download](https://ollama.com/download), or run `brew install ollama`.
- Start Ollama from **Applications** — a menu bar icon appears when the service is running.
- Open **Terminal** and run `ollama --version`.

### Linux

- Run the official install script, then verify:

```text
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
```

### Health check

| Command | Good result |
|---|---|
| `ollama --version` | Version string, no error |
| `ollama list` | Empty list or your models — not "connection refused" |
| `ollama serve` | Only if the app is not running; most installs start the service automatically |

> **Common mistake:** `ollama pull` before the **service** is running — open the Ollama app (or run `ollama serve` on Linux) first.

---

## Explore the Ollama Model Library

At [ollama.com/library](https://ollama.com/library) you browse **hundreds of open-source models** — Qwen, DeepSeek, Gemma, Mistral, GPT-OSS, Nemotron, Llama, and more.

- **Official Definition:** A **model tag** (for example `qwen2.5:0.5b`) identifies a specific **size variant** of a model family on Ollama.
- **In Simple Words:** Tags are like **shirt sizes** — same brand, different fit for your machine.
- **Real-Life Example:** **Qwen 2.5 0.5B** fits a class laptop; **Qwen 72B** needs tens of GB of RAM and will freeze most student machines.

**Rough sizing rule from class:** about **1 billion parameters ≈ 1 GB** of storage/RAM (approximate guide, not exact).

| Your machine | Sensible starting tags |
|---|---|
| 8–16 GB RAM, no GPU | `qwen2.5:0.5b`, `llama3.2:1b` |
| 16 GB+ RAM | up to ~7B–8B with patience on CPU |
| **Avoid** 70B+ on laptops | Needs 40+ GB RAM — use **Groq** or **Ollama Cloud** instead |

- **VRAM vs system RAM:** A dedicated **GPU** speeds inference, but Ollama can fall back to **CPU and system RAM** — slower, still works for learning.
- **Common doubt:** *"Do I need a GPU?"* — No for demos; yes for fast production on large models.

---

## Pull a Light Model and Run Your First Prompt (CLI)

With Ollama running, download a **small model** and confirm chat works in the terminal before moving to Python.

- **Official Definition:** **`ollama pull`** downloads model weights; **`ollama run`** loads the model and opens interactive terminal chat.
- **In Simple Words:** `pull` = download the brain file; `run` = start chatting.
- **Real-Life Example:** `pull` is like saving a movie for offline view; `run` is pressing Play.

![ollama pull downloads weights to disk; ollama run opens interactive terminal chat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-03-pull-vs-run.png)

```text
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

At the `>>>` prompt, try: *Explain photosynthesis in two sentences for a Class 8 student.* Exit with `/bye` or **Ctrl+D** (Mac/Linux) / **Ctrl+Z** then Enter (Windows).

| Model tag | Approx. size | Use on class laptops |
|---|---|---|
| `qwen2.5:0.5b` | ~0.5B parameters | Default — fastest smoke test |
| `llama3.2:1b` | ~1B parameters | Slightly better, still light |
| `gemma2:2b` | ~2B parameters | Only if 8 GB+ RAM free |
| **Avoid** `70b`+ tags | 40+ GB RAM needed | Will freeze most student laptops |

![Small models fit laptops; 70B+ models need tens of GB RAM and freeze most student machines](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-04-small-vs-heavy-models.png)

**Useful CLI commands:**

```text
ollama list          # Models you have pulled
ollama ps            # Model loaded in RAM right now
ollama rm MODEL_NAME # Delete a model to free disk
```

> **[ Student Activity ]**
>
> **Install & First Chat**
>
> - Install Ollama and confirm `ollama --version` and `ollama list` work.
> - Pull `qwen2.5:0.5b`, run one prompt in the terminal, note one place the tiny model sounds vague or wrong.

---

## Trade-offs of Very Small Local Models

Smaller models are not “worse AI” — they are **different tools**, like a scooter vs a truck.

- **Official Definition:** **Model parameters** (0.5B, 1B, 7B) roughly measure size and capacity. **Hallucination** is when the model states confident but **false** facts.
- **In Simple Words:** A 0.5B model has a **tiny brain** — fast to run, but weaker memory than a 70B cloud model.
- **Real-Life Example:** Asking a 0.5B model for detailed legal advice is like asking a **first-year student** to draft a court petition — confident tone, possible errors.

| Advantage of tiny local models | Disadvantage |
|---|---|
| Runs on almost any laptop | **Limited reasoning** on multi-step problems |
| Fast enough for demos | **Weaker** on niche facts and some languages |
| No API bill per token | **Higher hallucination risk** without RAG/tools |

**How to get better answers anyway:**

- Use **clear, short prompts** — the same discipline you used when **mapping API facts into grounded prompts** applies here.
- Add a **system message**: *"If you are unsure, say you do not know."*
- When quality matters, switch to **Groq** or **Ollama Cloud** for that task only.

> **Common doubt:** *"My local model gave a wrong exam date — is Ollama broken?"*  
> **Answer:** The model **predicted** plausible text; it did not look up a calendar. Fix with better prompts, grounding (RAG), or a larger model.

---

## Call Ollama from Python (Local) — OpenAI-Compatible Client

In class we used the **`openai` Python package** pointing at **localhost** — the same `chat.completions.create` pattern as **Groq**, because **Ollama's API is OpenAI-compatible**.

- **Official Definition:** **OpenAI-compatible API** means a server accepts the same **REST shape** (client, messages, model) as OpenAI's chat completions endpoint.
- **In Simple Words:** Same **remote control** works on a different **TV brand** — you only change the address.
- **Real-Life Example:** All your Groq notebooks still work — swap `client = Groq(...)` for `client = OpenAI(base_url="http://localhost:11434/v1", ...)`.

![Python sends JSON to localhost:11434 and reads the assistant reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-05-ollama-api-flow.png)

```text
pip install openai
```

Save as `ask_ollama_local.py`:

```python
# OpenAI-compatible client — talks to Ollama on your machine
from openai import OpenAI  # Same library used for Groq-style calls

# Local Ollama server (default port 11434); api_key can be any non-empty string locally
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama's OpenAI-compatible endpoint
    api_key="ollama",  # Required by the library but not checked locally
)

# Must match a model from "ollama list"
LOCAL_MODEL = "qwen2.5:0.5b"

# Question to send
user_question = "List three healthy breakfast options for a busy college student in India."

# Chat request — same messages shape as Groq
response = client.chat.completions.create(
    model=LOCAL_MODEL,  # Which downloaded model to use
    messages=[  # List of chat turns
        {"role": "user", "content": user_question},  # The human question
    ],
)

# Extract assistant text from the response object
answer_text = response.choices[0].message.content

# Print which model answered
print("Model:", LOCAL_MODEL)
# Print the question for your lab log
print("Question:", user_question)
# Print the generated answer
print("Answer:", answer_text)
```

**How the code works:**
- `OpenAI(base_url=...)` — points the client at **your laptop** instead of openai.com.
- `api_key="ollama"` — satisfies the library; Ollama does not validate it for local calls.
- `LOCAL_MODEL` — must match a tag from `ollama list`.
- `messages=[...]` — list of **role + content** dicts; identical to Groq chat.
- `client.chat.completions.create(...)` — sends JSON to **localhost**; Ollama app must be running.
- `response.choices[0].message.content` — the generated answer string.

> **Common mistake:** Model not pulled → "model not found". Connection error → Ollama app not running.

### Alternative — native `ollama` package (optional)

Ollama also ships a **`from ollama import chat`** helper. It works, but the syntax differs from Groq. In this course we prefer the **OpenAI-compatible** style so one pattern works across Groq, Azure, Ollama local, and Ollama Cloud.

> **[ Student Activity ]**
>
> **Python Local Call**
>
> - Run the script with *"Explain blockchain to my grandmother in 80 words."*
> - Change only `user_question` and run again.
> - If it fails, run `ollama list` and confirm the model name matches `LOCAL_MODEL`.

---

## Ollama Cloud

When your laptop cannot hold a large model, **Ollama Cloud** runs selected models on Ollama's servers — same **messages** format, different **host** and **API key**.

- **Official Definition:** **Ollama Cloud** provides hosted inference at `https://ollama.com`. You authenticate with an **API key** created under **Settings → API keys**.
- **In Simple Words:** Same brand (Ollama), but the model runs on **their GPU farm** when your RAM is too small.
- **Real-Life Example:** You practise with **Qwen 0.5B** locally; for a harder reasoning demo you call a **20B+ cloud model** through Ollama Cloud.

### Get an API key

1. Sign up at [ollama.com](https://ollama.com) → **Settings → API keys** ([ollama.com/settings/keys](https://ollama.com/settings/keys)).
2. Click **Create API key** and copy once — treat like a password.
3. Verify cloud model names on [ollama.com/library](https://ollama.com/library) — not every local tag exists on cloud.

Save as `ask_ollama_cloud.py`:

```python
# Load secrets from .env before creating the client
import os  # Read environment variables

from dotenv import load_dotenv  # Load .env file into os.environ
from openai import OpenAI  # OpenAI-compatible client for Ollama Cloud

load_dotenv()  # Read .env in the current folder

# API key from .env — never hardcode in shared code
api_key = os.getenv("OLLAMA_API_KEY")  # Secret string from .env file

if not api_key:  # Stop early if key is missing
    raise ValueError("Set OLLAMA_API_KEY in your .env file.")

# Client pointed at Ollama Cloud
client = OpenAI(
    base_url="https://ollama.com/v1",  # Remote Ollama Cloud endpoint
    api_key=api_key,  # Proves your identity to Ollama Cloud
)

# Cloud model name — verify on ollama.com/library
CLOUD_MODEL = "gpt-oss:20b"

user_question = "Summarise three pros and cons of running LLMs locally for a college project."

response = client.chat.completions.create(
    model=CLOUD_MODEL,  # Cloud-hosted model tag
    messages=[{"role": "user", "content": user_question}],  # Same message shape as local
)

print("Model:", CLOUD_MODEL)
print("Question:", user_question)
print("Answer:", response.choices[0].message.content)
```

**How the code works:**
- `load_dotenv()` — loads `OLLAMA_API_KEY` from `.env` into the environment.
- `os.getenv("OLLAMA_API_KEY")` — reads the secret without embedding it in source code.
- `base_url="https://ollama.com/v1"` — switches from localhost to **Ollama Cloud**.
- Everything else mirrors the **local** script — only host, auth, and model name change.

- **Free tier:** Ollama Cloud offers limited free usage (resets on a schedule — check your dashboard).
- **Common mistake:** Using a **local-only** tag on cloud — always confirm the name on the library page.

---

## Groq vs Ollama Cloud — Speed in Class

We ran the **same prompt** on **Groq** (large hosted model) and **Ollama Cloud** and compared **response time**.

| Provider | Example model size (class demo) | Typical observation |
|---|---|---|
| **Groq** | ~70B class model | Answer in ~**3 seconds** — Groq optimizes for **inference speed** |
| **Ollama Cloud** | ~20B class model | Answer in ~**10 seconds** — still reasonable, slower in that live test |

- **Takeaway:** For **hackathon demos** where speed matters, Groq often wins. For **learning Ollama's ecosystem** (local + cloud in one brand), Ollama Cloud is still useful — especially when you already pulled models locally.
- **Fair compare rule:** Same **system message**, same **user message**, then compare **latency**, **step quality**, and **privacy** — not just which answer "sounds nicer."

> **[ Student Activity ]**
>
> **Timed Cloud Compare**
>
> - Pick one short reasoning question (for example, a two-step math word problem).
> - Run it on **Groq** and on **Ollama Cloud** with the same messages.
> - Note seconds to first useful answer and whether steps look complete.

---

## Secure Credentials with `.env` and Git

Running from **VS Code** (not Colab Secrets) means you store keys in a **`.env` file** on disk.

- **Official Definition:** A **`.env` file** holds `KEY=value` pairs locally. **`python-dotenv`** loads them into `os.environ`. **`.gitignore`** stops Git from uploading `.env`.
- **In Simple Words:** `.env` is a **private sticky note**; `.gitignore` says "don't photocopy this for the class repo."
- **Real-Life Example:** The shared GitHub repo is a **hostel whiteboard**; your API keys stay on a **sticky note in your drawer** (`.env`).

**`.gitignore`** (commit this):

```text
.env
__pycache__/
*.pyc
.venv/
```

**`.env.example`** (commit — placeholders only):

```text
GROQ_API_KEY=your_groq_api_key_here
OLLAMA_API_KEY=your_ollama_api_key_here
```

**`.env`** (each student — **never commit**):

```text
GROQ_API_KEY=paste_your_real_groq_key_here
OLLAMA_API_KEY=paste_your_real_ollama_key_here
```

```text
pip install python-dotenv openai
```

Example — call **Groq** from VS Code using `.env`:

```python
import os  # Read environment variables

from dotenv import load_dotenv  # Load .env into os.environ
from groq import Groq  # Groq client (same pattern as earlier sessions)

load_dotenv()  # Load keys from .env before any API call

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Key from .env, not hardcoded

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Example Groq model
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(response.choices[0].message.content)  # Print assistant reply
```

- **Why not hardcode keys in `.py` or notebooks?** Shared files leak secrets — whoever has your key can spend your quota.
- **Other formats:** JSON or YAML config files work too — `.env` is popular because it is a simple **key=value** list and tools know to **ignore** it in Git.
- Run `git status` and confirm `.env` does **not** appear as a file to commit.

> **Common mistake:** Committing `.env` "for backup" — rotate the key on the provider site if leaked.

> **[ Student Activity ]**
>
> **Secret Hygiene Check**
>
> - Create `.env`, `.env.example`, and `.gitignore` in your lab folder.
> - Add your **Groq** and **Ollama** keys to `.env`.
> - Run `git status` — `.env` must not be listed.

---

## Key Takeaways

- **Open-source LLMs** are downloadable weights; **paid APIs** (GPT, Gemini) and **hosted platforms** (Groq, Ollama Cloud, Azure) let you use stronger models without local RAM.
- **Benchmarks** (MMLU, SWE-bench, TruthfulQA, etc.) help you justify model choice on **quality**, **cost**, and **latency**.
- **Ollama** gives a **local API** at `localhost:11434` — validate with `ollama --version`, `ollama list`, `ollama pull`, and optional `ollama run` before Python.
- Call Ollama from Python with the **OpenAI-compatible client** — same `chat.completions.create` pattern as Groq; point `base_url` to localhost or Ollama Cloud.
- **Never commit secrets** — `.env` stays local, `.env.example` + `.gitignore` go in the repo so the cohort reproduces setup safely.
- This local + cloud entry point prepares you for **LangChain** integration in upcoming work.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Category | Meaning |
|---|---|---|
| **Ollama** | Tool | Pull, run, and API-serve LLMs locally |
| **Local LLM** | Concept | Inference on your computer, not a remote datacenter |
| **Open-source LLM** | Concept | Weights publicly available to download and self-host |
| **MMLU / SWE-bench / TruthfulQA** | Benchmark | Standard tests to compare model quality |
| **Azure Foundry** | Platform | Deploy and call many LLMs inside Microsoft Azure |
| `ollama --version` | CLI | Verify installation |
| `ollama pull MODEL` | CLI | Download model (e.g. `qwen2.5:0.5b`) |
| `ollama run MODEL` | CLI | Interactive terminal chat |
| `ollama list` / `ollama ps` | CLI | List models / see loaded model |
| **Parameters (0.5B, 1B, 70B)** | Concept | Rough measure of model size and capability |
| **localhost:11434** | API | Default local Ollama address |
| `https://ollama.com/v1` | API | Ollama Cloud OpenAI-compatible endpoint |
| `pip install openai` | Python | OpenAI-compatible client for Ollama |
| `from openai import OpenAI` | Python | Preferred calling style in this session |
| `from ollama import chat` | Python | Optional native Ollama helper (different syntax) |
| **GROQ_API_KEY** | Env var | Secret for Groq cloud calls from VS Code |
| **OLLAMA_API_KEY** | Env var | Secret for Ollama Cloud |
| **`.env`** | File | Local secrets — never commit |
| **`.env.example`** | File | Safe template for the cohort |
| **`.gitignore`** | File | Excludes `.env` from Git |
| `pip install python-dotenv` | Python | Load `.env` at runtime |
| `from dotenv import load_dotenv` | Python | Load key=value pairs from `.env` |
| **Hallucination** | Concept | Confident but incorrect model output |
| **OpenAI-compatible API** | Concept | Same chat completions shape across providers |
| **qwen2.5:0.5b** | Model | Example light local model used in class |
