# Ollama: Exploring Another World of LLMs

## Context of This Session

In the **previous session**, you closed **Module 2** with a **ShopKart tool agent** — the model **chose tools** (policy search and live weather), Python **executed** them, and **Groq** wrote a **grounded reply** from structured JSON. Every LLM call went to a **cloud API** you do not host yourself.

Today you add a **local path**: install **Ollama**, run a **light model**, call it from **Python**, compare **local vs Ollama Cloud** on the same prompt, and finish with **one script** that switches modes via **`.env`** — secrets stay out of Git.

**In this session, you will:**

- **Install and validate** Ollama with a laptop-friendly model
- **Call Ollama from Python** for chat completion
- **Compare local vs cloud** on an identical prompt using environment settings
- **Store API keys safely** in `.env` so the cohort can reproduce setup without leaking secrets

---

## Why Local LLMs — and What Ollama Does

Until now, your code sent prompts to **remote servers** (Groq, etc.). A **local LLM** runs **on your laptop** — no third party sees your text during inference.

- **Official Definition:** **Ollama** is an open-source tool to **download, run, and manage** LLMs locally. It exposes a **local HTTP API** at `http://localhost:11434` so terminal, Python, and LangChain can call it like any cloud API.
- **In Simple Words:** Ollama is **app store + player** for AI models — `ollama pull` downloads, `ollama run` or Python talks to it.
- **Real-Life Example:** Private placement notes stay on your machine with a local model; Ollama Cloud gives a **bigger model** for demos when your laptop is too small.

![Cloud LLM sends prompts to remote servers; local Ollama runs on your laptop for privacy and free practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-01-cloud-vs-local.png)

| Why use local | Why use cloud (Groq / Ollama Cloud) |
|---|---|
| Free practice, no per-token bill | Stronger reasoning on hard tasks |
| Privacy — data stays on device | Models too large for student laptops |
| Learn that LLM = software + weights | Faster on complex multi-step questions |

- **Common doubt:** *"If local is free, why Groq?"* — Tiny local models are for **learning and prototyping**; cloud models win on **quality** when it matters.
- **Upcoming work:** **LangChain** will plug into Ollama the same way it plugs into Groq — today you build that entry point. Ollama also supports **embeddings** and multimodal models later — start with **text chat** today.

---

## Install Ollama and Validate with a Light Model

Install **once** per machine, then validate with CLI before any Python.

### Windows

- Go to [https://ollama.com/download](https://ollama.com/download) and download the Windows installer.
- Run the installer — Ollama usually starts in the background automatically.
- Open **PowerShell** and run `ollama --version`.
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

- Use **clear, short prompts** — skills from your **previous prompt work** apply directly.
- Add a **system message**: *"If you are unsure, say you do not know."*
- When quality matters, switch to **Ollama Cloud** or Groq for that task only.

> **Common doubt:** *"My local model gave a wrong exam date — is Ollama broken?"*  
> **Answer:** The model **predicted** plausible text; it did not look up a calendar. Fix with better prompts, grounding (RAG), or a larger model.

---

## Call Ollama from Python (Local)

Cloud or local — the pattern is the same: Python sends a **JSON chat request** and gets text back. For Ollama, the server is on **your machine** at port **11434**.

![Python sends JSON to localhost:11434 and reads the assistant reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-05-ollama-api-flow.png)

```text
pip install ollama
```

Save as `ask_ollama_local.py`:

```python
# Import Ollama's chat helper (talks to localhost:11434 by default)
from ollama import chat

# Must match a model from "ollama list"
LOCAL_MODEL = "qwen2.5:0.5b"

# Question to send
user_question = "List three healthy breakfast options for a busy college student in India."

# Chat request — role + content, same pattern as Groq
response = chat(
    model=LOCAL_MODEL,  # Which downloaded model to use
    messages=[  # List of chat turns
        {"role": "user", "content": user_question},  # The human question
    ],
)

# Extract assistant text from the response dict
answer_text = response["message"]["content"]

# Print which model answered
print("Model:", LOCAL_MODEL)
# Print the question for your lab log
print("Question:", user_question)
# Print the generated answer
print("Answer:", answer_text)
```

**How the code works:**
- `from ollama import chat` — wrapper around the local HTTP API; no raw `requests` needed.
- `LOCAL_MODEL` — must match a model from `ollama list` on your machine.
- `messages=[...]` — list of **role + content** dicts; same shape as Groq chat.
- `chat(...)` — sends to **localhost**; Ollama app must be running.
- `response["message"]["content"]` — the generated answer string.

> **Common mistake:** Model not pulled → "model not found". Connection error → Ollama app not running.

> **[ Student Activity ]**
>
> **Python Local Call**
>
> - Run the script with *"Explain blockchain to my grandmother in 80 words."*
> - Change only `user_question` and run again.
> - If it fails, run `ollama list` and confirm the model name matches `LOCAL_MODEL`.

---

## Ollama Cloud and Secure Credentials

Sometimes you need a **bigger model** than your laptop can hold. **Ollama Cloud** runs selected models on Ollama’s servers — same `messages` format, different **host** and **auth**.

- **Official Definition:** **Ollama Cloud** provides hosted inference at `https://ollama.com`. You authenticate with an **API key** using a **Bearer** token in the request header.
- **In Simple Words:** Same brand (Ollama), but the “kitchen” moves to their cloud when your laptop is too small.
- **Real-Life Example:** You practise with a local 0.5B model at home; for a hard reasoning demo you rent Ollama Cloud’s bigger kitchen.

### Get an API key

1. Sign up at [ollama.com](https://ollama.com) → **Settings → API keys** ([ollama.com/settings/keys](https://ollama.com/settings/keys)).
2. Click **Create API key** and copy once — treat like a password.
3. Optional: `ollama signin` and `ollama pull gpt-oss:120b-cloud` — verify names on [ollama.com/library](https://ollama.com/library).

For one-off tests you can `export OLLAMA_API_KEY=...` in the terminal; for reproducible cohort setup use **`.env`** below.

### Keep secrets out of Git

- **Official Definition:** A **`.env` file** holds `KEY=value` pairs locally. **`python-dotenv`** loads them into `os.environ`. **`.gitignore`** stops Git from uploading `.env`.
- **In Simple Words:** `.env` is a **private sticky note**; `.gitignore` says "don't photocopy this for the class repo."
- **Real-Life Example:** The shared GitHub repo is a **hostel whiteboard**; your API key stays on a **sticky note in your drawer** (`.env`).

**`.gitignore`** (commit this):

```text
.env
__pycache__/
*.pyc
.venv/
```

**`.env.example`** (commit — placeholders only):

```text
OLLAMA_API_KEY=your_ollama_api_key_here
USE_CLOUD=0
```

**`.env`** (each student — **never commit**):

```text
OLLAMA_API_KEY=paste_your_real_key_here
USE_CLOUD=0
```

- `USE_CLOUD=0` → local laptop; `USE_CLOUD=1` → Ollama Cloud.
- Run `git status` and confirm `.env` does **not** appear as a file to commit.

```text
pip install python-dotenv
```

> **Common mistake:** Committing `.env` "for backup" — rotate the key on ollama.com if leaked.

> **[ Student Activity ]**
>
> **Secret Hygiene Check**
>
> - Create `.env`, `.env.example`, and `.gitignore` in your lab folder.
> - Run `git status` — `.env` must not be listed.
> - Flip `USE_CLOUD` between `0` and `1` in `.env` and confirm the capstone script picks up the change without editing Python.

---

## Compare Local vs Cloud — One Script, Two Modes

Fair comparison needs the **same question** and honest notes about **speed**, **reasoning**, and **privacy**. Your capstone reads **`USE_CLOUD`** from `.env` so the **prompt string stays identical** — only the backend changes.

![One script branches on USE_CLOUD — local vs Ollama Cloud with API key](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-09-one-script-toggle.png)

### What changes in code (local vs cloud)

| Piece | Local | Ollama Cloud |
|---|---|---|
| **Host** | Default `localhost:11434` | `https://ollama.com` |
| **Client** | `chat()` helper | `Client(host=..., headers=...)` |
| **Auth** | None | `Authorization: Bearer <OLLAMA_API_KEY>` |
| **Model name** | e.g. `qwen2.5:0.5b` | e.g. `gpt-oss:120b` (verify on ollama.com) |

### Comparison prompt (use in both modes)

```text
A train leaves Delhi at 9:00 AM at 60 km/h. Another leaves Mumbai at 10:00 AM at 80 km/h toward Delhi. The cities are 1400 km apart. When do they meet? Show reasoning step by step, then give the final time.
```

| Dimension | Local `qwen2.5:0.5b` | Ollama Cloud (larger) |
|---|---|---|
| **Speed** | Fast after first load on CPU | Network-dependent |
| **Reasoning** | May skip steps or invent numbers | Usually more structured steps |
| **Hallucination** | Higher risk on math | Lower, but still verify |
| **Privacy** | Stays on laptop | Sent to Ollama servers |
| **Cost** | Free on your machine | Cloud tier limits apply |

### Discussion table (fill during lab)

| Check | Local answer | Cloud answer |
|---|---|---|
| Did it show steps? | Yes / No | Yes / No |
| Final time plausible? | Yes / No | Yes / No |
| Any invented facts? | Notes | Notes |

**Connecting idea:** Good prompts improve *how* you ask; model size improves *what* the model can reason. Agents need **both** — plus tools and RAG when facts must be grounded.

Save as `ask_ollama.py` — **capstone script**:

```python
# Load secrets and mode from .env
import os  # Read environment variables

from dotenv import load_dotenv  # Load .env file into os.environ
from ollama import Client, chat  # Local chat helper and cloud Client

# Read .env before any API call
load_dotenv()

# "0" = local, "1" = cloud — change in .env, not in code
USE_CLOUD = os.environ.get("USE_CLOUD", "0")

# Model names — must match pulled local tag and cloud library name
LOCAL_MODEL = "qwen2.5:0.5b"
CLOUD_MODEL = "gpt-oss:120b"

# Same prompt for fair local vs cloud comparison
user_question = (
    "A train leaves Delhi at 9:00 AM at 60 km/h. Another leaves Mumbai at "
    "10:00 AM at 80 km/h toward Delhi. The cities are 1400 km apart. When do "
    "they meet? Show reasoning step by step, then give the final time."
)


def ask_local(question: str) -> str:
    """Chat with Ollama on this computer."""
    response = chat(
        model=LOCAL_MODEL,  # Small model on localhost
        messages=[{"role": "user", "content": question}],  # Single user turn
    )
    return response["message"]["content"]  # Assistant reply text


def ask_cloud(question: str) -> str:
    """Chat with Ollama Cloud using API key from .env."""
    api_key = os.environ.get("OLLAMA_API_KEY")  # Secret from .env
    if not api_key:  # Stop early if cloud mode has no key
        raise ValueError("Cloud mode needs OLLAMA_API_KEY in your .env file.")

    cloud_client = Client(
        host="https://ollama.com",  # Remote Ollama host
        headers={"Authorization": "Bearer " + api_key},  # Prove identity
    )
    response = cloud_client.chat(
        model=CLOUD_MODEL,  # Larger cloud model name
        messages=[{"role": "user", "content": question}],  # Same message shape
    )
    return response["message"]["content"]  # Assistant reply text


def main() -> None:
    """Run local or cloud based on USE_CLOUD and print the answer."""
    if USE_CLOUD == "1":  # Cloud branch
        mode_label = "CLOUD"
        answer = ask_cloud(user_question)
        model_label = CLOUD_MODEL
    else:  # Local branch (default)
        mode_label = "LOCAL"
        answer = ask_local(user_question)
        model_label = LOCAL_MODEL

    print("Mode:", mode_label)  # LOCAL or CLOUD
    print("Model:", model_label)  # Which model tag ran
    print("Question:", user_question)  # Prompt sent
    print("Answer:")  # Label before body
    print(answer)  # Generated text


if __name__ == "__main__":  # Run only when executed directly
    main()
```

**How the code works:**
- `load_dotenv()` — loads `OLLAMA_API_KEY` and `USE_CLOUD` from `.env`.
- `ask_local` — default `chat()` → `localhost:11434`.
- `ask_cloud` — `Client` with `https://ollama.com` and **Bearer** token.
- `main()` — one entry point; flip mode by editing `.env` only.
- `if __name__ == "__main__"` — runs `main()` only when you execute the file directly.

### Run both modes

**Local** — in `.env`: `USE_CLOUD=0` then `python ask_ollama.py`

**Cloud** — in `.env`: `OLLAMA_API_KEY=your_key` and `USE_CLOUD=1` then `python ask_ollama.py`

> **[ Student Activity ]**
>
> **Local vs Cloud Showdown**
>
> - Run the capstone in **local** mode, then **cloud** mode with the same prompt.
> - Fill the discussion table above. Which answer would you trust for homework vs a hackathon demo?

> **[ Student Activity ]**
>
> **Capstone Checklist**
>
> - [ ] Ollama installed; light model pulled; CLI chat works
> - [ ] `.env`, `.env.example`, `.gitignore` set up; `.env` not in `git status`
> - [ ] `ask_ollama_local.py` and `ask_ollama.py` both return answers
> - [ ] Same prompt in both modes — you can explain one quality difference

---

## Key Takeaways

- **Ollama** gives you a **local LLM API** at `localhost:11434` — `ollama pull` + `ollama run` validate setup before Python; **tiny models** trade reasoning quality for speed.
- **Python `ollama` package** uses the same **messages** format as Groq — `chat()` for local, `Client(host=...)` for cloud.
- Compare fairly: **same prompt**, switch only **`USE_CLOUD`** in `.env`; note privacy and quality differences honestly.
- **Never commit secrets** — `.env` stays local, `.env.example` + `.gitignore` go in the repo so the cohort reproduces setup safely.
- This **dual-mode script** is the reproducible entry point **LangChain** will build on in upcoming work.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Category | Meaning |
|---|---|---|
| **Ollama** | Tool | Pull, run, and API-serve LLMs locally |
| **Local LLM** | Concept | Inference on your computer, not a remote datacenter |
| **Open-source LLM** | Concept | Weights publicly available to download and self-host |
| `ollama --version` | CLI | Verify installation |
| `ollama pull MODEL` | CLI | Download model (e.g. `qwen2.5:0.5b`) |
| `ollama run MODEL` | CLI | Interactive terminal chat |
| `ollama list` / `ollama ps` | CLI | List models / see loaded model |
| `ollama signin` | CLI | Log in for Ollama Cloud features |
| `ollama rm MODEL` | CLI | Delete a model to free disk |
| **Parameters (0.5B, 1B, 70B)** | Concept | Rough measure of model size and capability |
| **localhost:11434** | API | Default local Ollama address |
| `https://ollama.com` | API | Ollama Cloud host |
| `pip install ollama` | Python | Official Ollama library |
| `from ollama import chat` | Python | Simple local chat |
| `from ollama import Client` | Python | Custom host + headers for cloud |
| **OLLAMA_API_KEY** | Env var | Secret for Ollama Cloud |
| **USE_CLOUD** | Env var | `0` local, `1` cloud |
| **`.env`** | File | Local secrets — never commit |
| **`.env.example`** | File | Safe template for the cohort |
| **`.gitignore`** | File | Excludes `.env` from Git |
| `pip install python-dotenv` | Python | Load `.env` at runtime |
| `from dotenv import load_dotenv` | Python | Load key=value pairs from `.env` |
| **Bearer token** | Security | `Authorization: Bearer <key>` header |
| **Hallucination** | Concept | Confident but incorrect model output |
| **Chat API** | API type | Messages with roles → assistant reply |
| **qwen2.5:0.5b** | Model | Example light local model |
| **llama3.2:1b** | Model | Example small text model |
| **gpt-oss:120b** | Model | Example cloud model (verify on ollama.com) |
