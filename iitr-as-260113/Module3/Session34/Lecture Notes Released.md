# Ollama: Exploring Another World of LLMs

## What We Covered Before and Where We Are Heading

In the previous module, you built the foundation for **agentic systems**: how **APIs** and **JSON** connect software, how agents use **function calling** to pick tools, and how Python with **Pydantic** and **SQLAlchemy** validates data and talks to databases. Those sessions used **cloud LLMs** (for example OpenAI) over the internet — you set an API key, sent a request, and the model ran on someone else’s servers.

Today we open **Module 3** with a practical shift: you can run **open-source LLMs on your own machine** (or on **Ollama Cloud** when you need more power) using **Ollama** — at **no model cost** for learning. That matters because every agent you build will need an LLM behind it; owning a local setup means you can experiment freely before wiring agents in upcoming sessions.

**In this session, you will learn:**
- Why cloud LLMs (OpenAI, Gemini, Claude) differ from **local open-source** models
- How to **install Ollama**, verify it, and run a **small model** from the terminal
- Why **heavy models** are a bad idea on a normal laptop, and what **trade-offs** small models have
- How to call a local model from **Python** with the same **POST + JSON** pattern you already know
- How to use **Ollama Cloud** with an API key and host change
- What Ollama can do (chat, generation, embeddings, and more) and which **model families** exist (text, vision, audio, video)

---

## Recap: How You Have Used LLMs So Far

You have already called LLMs many times in class — always through an **API**.

- **Official Definition:** An **LLM API** is a network interface that lets your code send a prompt to a remote model and receive generated text back, usually as JSON.
- **In Simple Words:** Your Python script is the customer; the LLM company’s server is the kitchen. You place an order (prompt) and get food (response) delivered over the internet.
- **Real-Life Example:** Using ChatGPT on the web is like dining inside the restaurant. Using `client.responses.create(...)` from Python is like **Swiggy** — same kitchen, but you order from your app.

### API keys and environment variables

Proprietary models (OpenAI GPT, Google Gemini, Anthropic Claude) are **not free to download**. You create an account, get an **API key**, and the provider checks whether you are allowed to use a given model (subscription, balance, etc.).

**Best practice from earlier classes:** do not hard-code the API key in your file. Set it once in the terminal:

```bash
export OPENAI_API_KEY="your-key-here"
```

Your Python client reads it from the environment so the key does not leak on GitHub.

- **Common mistake:** Renaming the variable (for example `MY_KEY`) without updating what the library expects — the client will behave as if no key was set.

### Where cloud models actually run

When you call OpenAI from Delhi, your laptop sends a request over the **internet** to a **data center** (cloud) — maybe in the US, Singapore, or elsewhere. No internet means no API call. That is the default mental model: **client on your machine → server in the cloud → response back**.

![Cloud LLM sends prompts to remote servers for power and per-token cost; local LLM runs on your laptop for privacy and free practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-01-cloud-vs-local.png)

---

## Running LLMs Locally — A Different Path

There is another option: run an LLM **on your own laptop**, using your **CPU**, **RAM**, and **disk**.

- **Official Definition:** **Local LLM inference** means loading model weights onto your machine and generating text without sending the prompt to a third-party cloud for that step.
- **In Simple Words:** The “kitchen” moves into your house. The prompt never has to leave your computer for the model to answer.
- **Real-Life Example:** Downloading a movie to watch offline vs streaming on Netflix every time — local is yours on disk; cloud needs a live connection.

### What you cannot run locally

You **cannot** download and run **OpenAI**, **Claude**, or **Gemini** weights — they are **private** and live only on their companies’ servers. Local use is limited to models that are **open source** and **published for download**.

### Why local LLMs are useful (especially for learners)

| Reason | What it means for you |
| --- | --- |
| **Cost** | No per-token bill while practising on small open models |
| **Privacy** | Sensitive prompts and data stay on your machine |
| **Speed (sometimes)** | No long round-trip to a faraway data center |
| **Learning** | You can break things, re-run scripts, and inspect responses without fear of a huge cloud bill |

Companies may run local models at scale on many machines; as a student, a **small** local model on one laptop is enough to learn how agents will call an LLM later.

---

## What Is Ollama?

**Ollama** is a tool that makes local (and cloud) open-source models easy to manage.

- **Official Definition:** **Ollama** is a runtime and CLI that downloads, runs, and serves open-source LLMs, exposing a consistent **HTTP API** (similar in spirit to OpenAI’s chat API).
- **In Simple Words:** One friendly shop that stocks hundreds of models — you ask Ollama for a model by name instead of learning a different install process for each one.
- **Real-Life Example:** **Amazon** aggregates many sellers; you talk to Amazon, not each seller’s warehouse. Ollama aggregates many **open models**; you talk to Ollama, not each model’s separate tooling.

![Ollama pulls model weights to your machine once, then serves chat through a local API — like an app store plus player for open-source LLMs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-02-what-is-ollama.png)

### Two ways to use Ollama

1. **Local** — Model files sit on your disk; Ollama serves `http://localhost:11434`. No API key needed for local calls.
2. **Ollama Cloud** — Stronger models run on Ollama’s infrastructure. You use an **API key** and host `https://ollama.com` (same JSON body, different URL and headers).

You can think of Ollama locally as a **small AI server on your laptop** — like the **FastAPI** server you ran earlier, but specialised for LLM chat.

![Local Ollama on localhost:11434 needs no API key; Ollama Cloud on ollama.com uses a Bearer token for stronger models — same JSON chat API on both paths](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-03-local-vs-ollama-cloud.png)

### Default local address

| Piece | Value |
| --- | --- |
| **Host** | `http://localhost:11434` |
| **Chat API path** | `/api/chat` |
| **Full URL (local)** | `http://localhost:11434/api/chat` |

`localhost` means “this same computer.” Port **11434** is Ollama’s default.

---

## Install Ollama and Verify the Setup

### Step 1 — Account and download

1. Go to **https://ollama.com**
2. **Create an account** (needed for cloud API keys; useful for the model library)
3. Open **Download**, pick your OS (Windows, macOS, or Linux), or use the install command shown on the site
4. Run the installer (few MB for the app itself — **models are separate downloads**)

### Step 2 — Verify installation

Open a terminal and run:

```bash
ollama -v
```

If you see a **version number**, Ollama is installed correctly.

### Step 3 — Optional quick chat in the terminal

```bash
ollama
```

This can open an interactive session. In class, the main path was **`ollama run <model-name>`** for a specific model.

**Try it yourself:** After install, run `ollama -v` and note the version in your notebook. If the command is “not found,” restart the terminal or check that Ollama is in your system PATH.

---

## Pull and Run a Light Local Model (CLI)

### Choosing a small model

On the Ollama website, browse **Models** and check **size** and **RAM** hints. The instructor demonstrated **small Qwen** variants (for example around **395 MB** to **1.1 GB** on disk) — suitable for learning on a normal laptop.

- **Avoid** models that need **tens of GB** of RAM (examples shown in class: 24 GB, 55 GB, 100 GB requirements) unless you have a workstation built for it.
- Metadata mentions **0.5B** and **1B** parameter models as examples of “light” — on the site, use **size/RAM** labels; many small listings are in that family even if the exact “0.5B” label is not on every card.

### Pull and run (one command)

```bash
ollama run qwen2.5:0.5b
```

Replace the name with the exact tag you chose from the library (copy from the model page).

- **First time:** Ollama **pulls** (downloads) weights — you will see progress (for example “downloading 1.1 GB”).
- **Later runs:** If the model is already on disk, it **starts without re-downloading**.

![ollama pull downloads model weights to disk; ollama run loads the model and opens an interactive terminal chat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-04-pull-vs-run.png)

### Simple prompt in the terminal

After the model loads, type a prompt at the `>>>` prompt, for example:

```text
Should I use an OpenAI model or a local model via Ollama?
```

Press **Enter**. The answer is generated **on your machine** — the request does not go to OpenAI.

**Try it yourself:** Run one factual question and one creative question. Notice whether answers feel short or vague — that leads to the trade-off section below.

---

## Why You Should Avoid Heavy Models on a Regular Laptop

Large models (billions or trillions of parameters, multi‑GB or 100+ GB RAM) are built for **servers**, not a typical student laptop.

- They **fill disk** and **RAM**, making the system **slow** or **frozen**
- They take a long time to **download**
- For **learning and testing**, they add little value compared to a **small** model

**Rule of thumb:** If the model page shows **many GB of RAM** required and your laptop has 8–16 GB total system RAM, pick a **smaller** tag.

![Tiny 0.5B–2B models fit normal laptops; 70B+ models need tens of gigabytes of RAM and will freeze most student machines](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-05-small-vs-heavy-models.png)

---

## Trade-offs of Very Small Local Models

More parameters generally mean the model was trained on more capacity and can sound **smarter**. A **tiny** local model is fast and free but weaker.

| Aspect | Small local model | Large cloud / big local model |
| --- | --- | --- |
| **Quality** | May miss nuance, shorter answers | Stronger reasoning and knowledge |
| **Hallucination risk** | **Higher** — may sound confident but be wrong | Lower, but never zero |
| **Context / training** | Less “world knowledge” baked in | More coverage from scale |
| **Trust** | Do **not** blindly trust outputs for medical, legal, or production decisions | Still verify; never fully automatic trust |

The instructor’s line in class: **small models can hallucinate** because they lack enough context — treat them as a **learning sandbox**, not a replacement for GPT‑class models on hard tasks.

**Try it yourself:** Ask your small local model for today’s exact stock price or a very recent news event. Compare mentally with what you know is unknowable offline — that builds intuition for hallucination without needing cloud yet.

---

## Hardware: What a Local Model Uses

Running a model is not “free” for your machine. It consumes:

- **CPU** and often **GPU** (if available)
- **RAM** (model weights loaded into memory)
- **Disk** (stored weights)
- **Battery** and internal **data movement** (disk ↔ RAM)

If many apps are open, RAM fills up and the OS slows down — same as opening too many Chrome tabs.

**After practice:** Use `ollama rm <model-name>` to delete models you no longer need and free disk space.

---

## Useful Ollama CLI Commands

| Command | Purpose |
| --- | --- |
| `ollama -v` | Check installed version |
| `ollama run <model>` | Download (if needed) and run model; interactive chat |
| `ollama list` | List models downloaded on your machine |
| `ollama rm <model>` | Remove a model from disk |
| `ollama ps` | Show models currently running (like `ps` for processes) |
| `ollama stop <model>` | Stop a running model |

**Behaviour worth knowing:** If you call the API while the model is stopped, Ollama may **auto-start** the model in the background to serve the request — so “stopped” in one place does not always mean “no process anywhere” until things settle.

---

## Call a Local Model from Python (Full Script)

You do **not** need the OpenAI Python package for Ollama local chat. Use the **`requests`** library — same **POST** + **JSON** idea as earlier API classes.

![Python sends a JSON chat POST to Ollama on localhost:11434/api/chat and reads the assistant reply from message.content](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-06-python-ollama-api-flow.png)

### Setup project folder

```bash
mkdir local_llm
cd local_llm
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install requests
```

Create a file named `app.py` with the following **complete** code:

```python
# app.py — call a local Ollama model via HTTP API

import requests  # Library to make HTTP calls (GET, POST, etc.)

# Base URL where Ollama listens on your laptop
ollama_host = "http://localhost:11434"

# API path for chat (from Ollama documentation)
api_path = "/api/chat"

# Full URL = host + path
url = ollama_host + api_path

# Exact model name you pulled with `ollama run` (copy from `ollama list`)
model_name = "qwen2.5:0.5b"

# The question you want to ask the model
prompt = "Explain REST API in a beginner friendly way."

# JSON body (payload) sent to the server
payload = {
    "model": model_name,  # Which local model to use
    "messages": [  # Chat-style message list (like OpenAI)
        {
            "role": "user",  # You are the user in this conversation
            "content": prompt,  # Your actual question
        }
    ],
    "stream": False,  # False = return full answer in one shot (see streaming section)
}

# POST request: create/generate a chat response
response = requests.post(
    url,
    json=payload,  # Send payload as JSON in the body
    timeout=120,  # Wait up to 120 seconds, then fail (you own the server — set a limit)
)

# Convert HTTP response body to a Python dictionary
data = response.json()

# Print only the assistant's text (nested inside "message" -> "content")
print(data["message"]["content"])
```

**How the code works:**
- **`requests.post`** sends a **POST** request because you are **creating** a new chat completion (same idea as “create resource” from HTTP class).
- **`json=payload`** serialises your Python dict to JSON automatically.
- **`messages`** mirrors OpenAI-style chat: role + content; optional **role prompting** (for example “act like a doctor”) can be added later.
- **`stream: False`** waits until the full answer is ready, then prints once.
- **`timeout=120`** avoids hanging forever if the local server is stuck — on cloud APIs the provider often sets a default; locally **you** are responsible.
- If you use a **wrong `model_name`**, you may get errors like **model not found** — always match the name from `ollama list`.

**Try it yourself:** Run `python3 app.py` twice. Change only the prompt. Then change `model_name` to a model you have **not** pulled and observe the error message.

---

## Streaming vs Non-Streaming Responses

![stream false waits for the full reply in one JSON response; stream true delivers tokens gradually like live typing in ChatGPT](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-07-streaming-vs-non-streaming.png)

| `stream` value | Behaviour |
| --- | --- |
| **`false`** | Model generates the **full** reply, then sends it in **one** JSON response |
| **`true`** | Tokens arrive **gradually** (word by word), like ChatGPT typing live |

In the terminal demo, with streaming enabled, you see text appear incrementally. With `stream: false` in Python, you wait, then get the complete string in `message.content`.

**Try it yourself:** Set `"stream": True` in the payload and print chunks as they arrive (read Ollama docs for the streaming response format). Notice how it feels more interactive but needs slightly more parsing code.

---

## Ollama Cloud — Account, API Key, and Python

When a **small local** model is not enough, use **Ollama Cloud**: stronger open models on Ollama’s servers, still with an OpenAI-like flow.

![Ollama Cloud uses https://ollama.com/api/chat with Authorization Bearer OLLAMA_API_KEY — same JSON body as local, different host and headers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-08-ollama-cloud-auth.png)

### Steps

1. Log in at **https://ollama.com**
2. Go to **Account → Settings → Keys**
3. **Generate** an API key
4. In the terminal:

```bash
export OLLAMA_API_KEY="your-key-here"
```

5. For some cloud models, **pull** once so your local Ollama knows the name (may show **size null** — weights are not stored locally):

```bash
ollama pull gpt-oss:120b-cloud
```

(Use the exact tag from the model page you intend to call.)

### Full cloud script — `app2.py`

```python
# app2.py — call Ollama Cloud via HTTP API

import os  # Read environment variables safely
import requests  # HTTP client

# Read API key from environment (set with export OLLAMA_API_KEY=...)
api_key = os.environ.get("OLLAMA_API_KEY")

# Fail fast if the key is missing
if not api_key:
    raise ValueError("OLLAMA_API_KEY is not set. Run: export OLLAMA_API_KEY='your-key'")

# Cloud host + path (not localhost)
url = "https://ollama.com/api/chat"

# Same style of body as local — model must be a cloud-capable name you pulled/registered
payload = {
    "model": "gpt-oss:120b-cloud",  # Example from class; use a tag from the Ollama library
    "messages": [
        {
            "role": "user",
            "content": "Explain REST API in a beginner friendly way.",
        }
    ],
    "stream": False,
}

# Bearer token in header — standard way to send API keys
headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.post(
    url,
    json=payload,
    headers=headers,
    timeout=120,
)

data = response.json()
print(data["message"]["content"])
```

**How the code works:**
- **Local** calls use `http://localhost:11434` and **no** API key.
- **Cloud** calls use **`https://ollama.com/api/chat`** plus **`Authorization: Bearer <key>`**.
- The **payload shape stays the same** — only host, headers, and often the **model name** change.
- Cloud models may **not** appear as large files in `ollama list`; size can show **null** because inference runs remotely.

**Common errors:** `401` / authorisation issues → key not set or wrong header. `405 Method not allowed` → wrong URL or HTTP method. Fix by matching official docs for cloud chat.

---

## One Script for Local or Cloud (Assignment Pattern)

The live session demonstrated **`app.py`** (local) and **`app2.py`** (cloud) separately. The intended finish line is **one** program that switches with a variable such as **`mode`**.

![One capstone script branches on mode — local localhost chat versus Ollama Cloud with an API key](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-09-unified-script-toggle.png)

**Try it yourself — complete this combined script:**

```python
# app_unified.py — local OR cloud based on mode

import os
import requests

# Change this to "local" or "cloud"
mode = "local"

model_name = "qwen2.5:0.5b"  # For cloud, use your cloud tag e.g. gpt-oss:120b-cloud
prompt = "Explain REST API in a beginner friendly way."

payload = {
    "model": model_name,
    "messages": [{"role": "user", "content": prompt}],
    "stream": False,
}

if mode == "local":
    # Local branch — no API key
    url = "http://localhost:11434/api/chat"
    headers = None
else:
    # Cloud branch — need API key
    api_key = os.environ.get("OLLAMA_API_KEY")
    if not api_key:
        raise ValueError("OLLAMA_API_KEY is not set for cloud mode.")
    url = "https://ollama.com/api/chat"
    headers = {"Authorization": f"Bearer {api_key}"}

response = requests.post(url, json=payload, headers=headers, timeout=120)
print(response.json()["message"]["content"])
```

Run once with `mode = "local"`, then with `mode = "cloud"` (after setting `OLLAMA_API_KEY`).

---

## Compare Local vs Cloud on the Same Prompt

This was assigned as a **learning check** rather than a long in-class demo. Use the **same prompt string** in both modes and compare:

![Same prompt on two paths — local tiny model for privacy and zero cost versus Ollama Cloud for stronger, richer answers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-10-local-vs-cloud-compare.png)

| What to observe | Local small model | Ollama Cloud |
| --- | --- | --- |
| **Speed** | Often fast after first load; depends on CPU | Depends on network and cloud load |
| **Depth** | Shorter, simpler explanations | Usually richer answers |
| **Factual risk** | May hallucinate more on hard facts | Better, but still verify |
| **Cost** | No API token charge for local weights | Subject to Ollama cloud/free-tier limits |

**Try it yourself:** Use the prompt *“Explain REST API in a beginner friendly way.”* Run local and cloud back-to-back. Save both outputs in a text file and underline one place where the local model was weaker.

---

## What Ollama Can Do (Capabilities)

Ollama is not only chat. The platform supports several **modalities** and tasks, including:

- **Chat** — multi-turn conversation via `/api/chat`
- **Text generation** — completion-style use cases
- **Embeddings** — turn text into vectors for search/RAG (mentioned in recap; deep dive may come when you build retrieval)
- **Audio / video / image** models — depending on which weights you pull (multimodal models)

For this session, the **hands-on focus** was **chat** over HTTP. Embeddings and other endpoints follow the same idea: correct URL, JSON body, and model name from the docs.

---

## Model Families on Ollama (Text, Vision, Audio, Video)

On **ollama.com → Models**, you can filter and browse:

![Ollama model types by modality — text chat, vision with images, audio, and heavier video models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session34/session34-11-model-modalities.png)

| Type | Typical use |
| --- | --- |
| **Text-only** | Chat, Q&A, coding help (smaller, easier on laptops) |
| **Vision** | Image + text (larger disk/RAM) |
| **Audio** | Speech-related models |
| **Video** | Video understanding/generation (usually very large) |
| **Thinking / reasoning** | Models tuned for harder step-by-step tasks |
| **Code** | Models tuned for programming (often large, e.g. Code Llama variants) |

**Multimodal** means one model can work with more than one kind of input (for example **text + image**). Bigger multimodal models can reach **tens of GB** — treat them like heavy models unless you have the hardware.

**Try it yourself:** Open the model library, filter by **Vision**, and write down the **RAM/size** of the smallest vision model you find. Decide yes/no: “Can I run this on my laptop?”

---

## Key Takeaways

- **Cloud proprietary LLMs** (OpenAI, Claude, Gemini) need internet and API keys; **open-source** models can run **locally** through **Ollama** on your disk and RAM.
- **Install → `ollama -v` → `ollama run <small-model>`** gives you a working, low-cost practice environment before building agents.
- **Small models** are ideal for learning but **hallucinate more** and answer less deeply than large cloud models — pick local for experiments and cloud when you need strength.
- **Python + `requests.post`** to `localhost:11434/api/chat` mirrors the API patterns you already know; cloud only changes **URL**, **Bearer token**, and **model tag**.
- **Next**, you will connect LLMs to **prompt engineering** and **agent workflows** — today’s setup is the engine those systems will call.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / command | Meaning |
| --- | --- |
| **LLM** | Large Language Model — predicts text from learned patterns |
| **Open-source model** | Weights you may download and run yourself (subject to license) |
| **Ollama** | Tool to pull, run, and serve open models locally or via cloud API |
| **Pull** | Download model weights to your machine (`ollama run` triggers pull) |
| **localhost:11434** | Default local Ollama server address |
| **`/api/chat`** | Chat completion HTTP path |
| **`ollama -v`** | Verify installation |
| **`ollama run <model>`** | Run / chat with a model |
| **`ollama list`** | List downloaded models |
| **`ollama rm <model>`** | Delete model from disk |
| **`ollama ps`** | List running Ollama models |
| **`ollama stop <model>`** | Stop a running model |
| **`requests`** | Python library for HTTP calls |
| **POST** | HTTP method used to send JSON body and create a response |
| **Payload / request body** | JSON dict sent with the POST (model, messages, stream, …) |
| **`stream: false`** | Wait for full reply in one response |
| **`stream: true`** | Token-by-token streaming |
| **`OLLAMA_API_KEY`** | Environment variable for Ollama Cloud |
| **Bearer token** | `Authorization: Bearer <key>` header format |
| **Hallucination** | Confident but incorrect model output |
| **Multimodal** | Model handles more than one input type (text, image, audio, …) |
| `export OLLAMA_API_KEY="..."` | Set cloud API key in terminal session |
| `python3 app.py` | Run local LLM script |
