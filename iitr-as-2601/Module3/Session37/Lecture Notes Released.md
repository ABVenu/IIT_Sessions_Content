# Open-Source LLMs

## What We Covered So Far & What's Coming Next

In our last session, we focused on **Prompt Engineering** — how to talk to an LLM so it gives you reliable answers. We learned **System Prompts** vs **User Prompts**, **Zero-Shot** and **Few-Shot** prompting, **Chain-of-Thought**, prompt templates, self-correction, and how to design a full **agent prompt flow**. All of that assumed you already had access to an LLM somewhere in the cloud.

Today we opened a second door: **running LLMs on your own machine** with **Ollama**, and we also worked with **cloud APIs** — especially **Groq** in Google Colab — so you can use powerful models without downloading 70B weights onto a laptop. You installed Ollama, pulled a **light local model**, chatted from the **terminal**, then switched to **Groq** (and saw the same pattern on OpenAI and Anthropic) to call big cloud models from Python.

**In this session, you will learn:**
- Why **local** and **open-source** LLMs matter for learning, privacy, and cost
- How to **install Ollama**, use the **GUI and CLI**, pull a **small model**, and chat from the **terminal**
- Why **heavy models** are a bad idea on a normal laptop — and what you trade off with **tiny models**
- How **Groq + Colab** gives you fast access to large cloud models with a free API key
- How the **same Python pattern** works across Groq, OpenAI, and Anthropic — swap the client and model name
- How to compare **cloud model outputs** on the same prompt and notice **training-data bias** (e.g. Chinese vs US models)
- What **model modalities** (text, vision, audio, video) mean — with a **Gemini + Google Photos** multimodal example
- How to call Ollama from **Python** locally (concept + notebook) and how **Ollama Cloud** would differ by changing the **host**

---

## Cloud LLMs vs Local LLMs — Why This Session Matters

Until now, most examples used LLMs as a **remote service**: your code sends a prompt over the internet, a company’s servers run the model, and the answer comes back. That is convenient, but it has limits.

**Official Definition:** A **local LLM** is a language model whose weights run on **your own computer** (CPU or GPU), without sending your prompt to a third-party cloud for inference. An **open-source LLM** is a model whose weights and often its code are **publicly available** for download, study, and self-hosting.

**In Simple Words:** A cloud LLM is like ordering food on Swiggy — fast and powerful, but you pay per order and the kitchen is far away. A local LLM is like cooking at home — you control ingredients and privacy, but your kitchen (laptop) has limited space and firepower.

**Real-Life Example:** If you are building a college project that reads **private placement data**, you may not want every question sent to a US server. Running a small model locally with Ollama keeps the data on your machine. For a **quick class demo** when your laptop cannot hold a 70B model, a **cloud API** (Groq, OpenAI, etc.) gives you power without local downloads.

![Cloud LLM sends prompts to remote servers for power and cost per token; local LLM runs on your laptop for privacy and free practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-01-cloud-vs-local.png)

### Why learners should care

- **Cost:** Local runs do not charge per token — useful when you are practising hundreds of prompts. Cloud APIs often have a **free tier** (Groq in class) but paid tiers charge **per token**.
- **Privacy:** Sensitive notes, internal documents, or personal journals stay on your device when you use local Ollama.
- **Learning:** You see that an LLM is **software + weights**, not magic in ChatGPT’s UI alone.
- **Speed on weak hardware:** A 70B model on Groq can answer in **under a second**; the same-sized model pulled locally on a basic laptop may take **minutes per reply** and heat the machine.
- **Agent building:** In upcoming work, **LangChain** and **RAG** will plug into Ollama or cloud APIs the same way — today you build that foundation.

> **Common doubt:** “If local is free, why use cloud at all?”  
> **Answer:** Big cloud models are trained on more data, run on faster hardware, and usually answer complex questions more accurately. Local tiny models are perfect for **learning, prototyping, and privacy**; cloud (Groq, OpenAI, Ollama Cloud, etc.) is better when **quality and speed** matter most on normal laptops.

### When enterprises choose local (on-premise)

**Official Definition:** An **on-premise** (on-prem) LLM runs inside an organisation’s own data centre or private servers — not on a public cloud API.

**In Simple Words:** The company buys the “kitchen” and keeps all cooking inside its own building.

**Real-Life Example:** **Pharmaceutical companies** (e.g. AstraZenica-style setups discussed in class) handle **patient trial data** and drug research that cannot leave their network. Banks and defence projects follow the same rule. They invest in **local servers and GPUs** so prompts never go to OpenAI’s public API — even though that hardware is expensive.

For **students and POCs**, cloud APIs are usually the practical choice when privacy is not the main constraint. The **concept** of on-prem local LLMs still matters so you understand why Ollama exists in industry.

---

## What Is Ollama?

**Official Definition:** **Ollama** is an open-source tool that makes it easy to **download, run, and manage** large language models on your computer. It exposes a **local HTTP API** (default: `http://localhost:11434`) so programs — terminal, Python, LangChain — can talk to the model the same way they talk to a cloud API.

**In Simple Words:** Ollama is like **Google Play Store + player** for AI models on your laptop. You “install” a model once (`ollama pull`), then “open” it whenever you need (`ollama run` or Python).

**Real-Life Example:** Think of Ollama as a **chai stall machine** in your hostel room. You stock one blend of tea leaves (the model file). Anytime you press the button (send a prompt), it brews a cup (generates text) without calling an outside café.

![Ollama pulls model weights to your machine once, then serves chat through a local API — like an app store plus player for LLMs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-02-what-is-ollama.png)

### Ollama GUI vs CLI

In class we used **both** interfaces:

| Interface | What you do there | When to use it |
|---|---|---|
| **Desktop app (GUI)** | **New chat**, browse models, **Settings** (account sign-in, models folder path) | Quick visual check; see where models are stored on disk |
| **Terminal (CLI)** | `ollama pull`, `ollama run`, `ollama list` | Primary workflow for class; matches what agents and scripts call |

**In Simple Words:** The app is the friendly front door; the terminal is the engine room most developers use daily.

- Open the Ollama app → **Settings** shows your **models directory** (large files live here).
- You can create an **Ollama account** in settings (used for some cloud-tagged models on ollama.com) — we did **not** create an Ollama API key live; our live API key exercise was on **Groq**.
- For hands-on work, the instructor emphasised **CLI** after install: `ollama --version`, `ollama pull`, `ollama run`.

### What Ollama can do (overview)

| Capability | What it means | Covered in class |
|---|---|---|
| **Chat** | Back-and-forth messages with roles (`user`, `assistant`, `system`) | ✓ `ollama run` interactive CLI |
| **Text generation** | Single prompt → completion | ✓ Same CLI flow; generation is the default behaviour |
| **Embeddings** | Turn text into number vectors for search | Mentioned as a capability; full RAG/embeddings demo comes later |
| **Multimodal models** | Models that accept images, audio, or video (when you pull them) | ✓ Browsed on ollama.com/library and search filters |

We go deeper into **model types** later in this session. First: get Ollama running on your machine.

---

## Installing Ollama and Verifying the Setup

You only need to install Ollama **once** per computer. In class we walked through **Windows** (EXE from ollama.com); **Mac** install was noted for students on macOS.

### Windows

- Go to [https://ollama.com/download](https://ollama.com/download) and download the Windows installer.
- Run the installer and finish the setup wizard — Ollama usually starts in the background automatically.
- Open **PowerShell** or **Command Prompt** and run:

```text
ollama --version
```

- If you see a version number (for example `ollama version 0.6.x`), installation succeeded.
- **If `ollama` is not recognized:** close and reopen the terminal, or restart the PC so PATH updates apply.

### macOS

- Download the app from [https://ollama.com/download](https://ollama.com/download), or install via Homebrew:

```text
brew install ollama
```

- Start Ollama from Applications (menu bar icon appears when the service is running).
- Open **Terminal** and verify:

```text
ollama --version
```

### Linux

- Run the official install script (check [ollama.com](https://ollama.com) for the latest one-liner), then verify:

```text
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
```

### Quick health check after install

| Step | Command | What “good” looks like |
|---|---|---|
| 1 | `ollama --version` | Version string printed, no error |
| 2 | `ollama list` | Empty list or list of models you already pulled — not “connection refused” |
| 3 | Open Ollama app → Settings | Models folder path visible; service running |

> **Common mistake:** Running `ollama pull` before the Ollama **service** is running. On Windows/Mac, open the Ollama app first.

> **[ Student Activity ]**
>
> **Install & Verify (10 minutes)**
>
> - Install Ollama on your machine using the steps for your OS.
> - Run `ollama --version` and `ollama list`.
> - Open the Ollama app once and note the command line and GUI both work on your system.

---

## Pulling a Light Model and Running Your First Prompt (CLI)

**Official Definition:** **`ollama pull`** downloads a model’s weights from Ollama’s library to your machine. **`ollama run`** loads that model and opens an interactive chat in the terminal.

**In Simple Words:** `pull` = download the “brain file.” `run` = start chatting with that brain.

**Real-Life Example:** `pull` is like downloading a movie on Netflix for offline view. `run` is pressing Play.

![ollama pull downloads model weights to disk; ollama run loads the model and opens an interactive terminal chat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-03-pull-vs-run.png)

### Choose a light model (recommended for class laptops)

In class we pulled **Qwen 2.5 0.5B** (~397 MB) and optionally a ~1B Llama (~1.3 GB):

| Model tag | Approx. size | Good for |
|---|---|---|
| `qwen2.5:0.5b` | Very small (~0.5B parameters) | Fastest smoke test on weak laptops |
| `llama3.2:1b` | Small (~1B parameters) | Slightly better answers, still laptop-friendly |

**Avoid on regular laptops:** `llama3.1:70b`, `qwen2.5:72b`, or any **70B+** tag — they need large GPU RAM and will freeze or crash most student machines. The instructor demo’d a heavier **DeepSeek 14B** pull only to show risk — **students were told not to repeat that**.

### Step-by-step CLI demo

```text
# Step 1: Download the small model (one-time, needs internet)
ollama pull qwen2.5:0.5b

# Step 2: See what you have
ollama list

# Step 3: Start an interactive chat session
ollama run qwen2.5:0.5b
```

When the `>>>` prompt appears, type a simple question (as in class):

```text
Explain photosynthesis in two simple sentences for a Class 8 student.
```

- Press **Enter** and wait — first reply may be slow while the model loads into RAM.
- Watch **Task Manager** (Windows) during a heavier run — **CPU/RAM** spike and **token** generation speed show why local inference feels different from cloud.
- Type `/bye` or press **Ctrl+D** (Mac/Linux) / **Ctrl+Z** then Enter (Windows) to exit.

### Other useful CLI commands

```text
ollama list          # Shows models you have pulled
ollama ps            # Shows which model is loaded in memory right now
ollama rm MODEL_NAME # Deletes a model file to free disk space
```

> **Why avoid heavy models on a normal laptop?**
> - **RAM:** A 70B model can need **40+ GB** of memory; most laptops have 8–16 GB total.
> - **Speed:** Without a strong **GPU**, generation becomes **minutes per sentence**, not seconds.
> - **Heat & battery:** The CPU runs at 100% for long periods — fans spin, session becomes unusable in class.
> - **Disk:** Large weights fill your SSD; one wrong `pull` can cost **tens of GB**.

![Tiny 0.5B–2B models fit normal laptops; 70B+ models need tens of gigabytes of RAM and will freeze most student machines](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-04-small-vs-heavy-models.png)

> **[ Student Activity ]**
>
> **CLI Prompt Battle (15 minutes)**
>
> - Pull the **same** small model as the class (`qwen2.5:0.5b`).
> - Run the **same** three prompts: (1) a math word problem, (2) a Hindi translation task, (3) a creative story in 50 words.
> - Compare answers with your own second try — note where the tiny model **hallucinates** or sounds vague.

---

## Trade-offs of Very Small Local Models

Smaller models are not “worse AI” — they are **different tools**, like a scooter vs a truck.

**Official Definition:** **Model parameters** (e.g. 0.5B, 1B, 7B) roughly measure model size and capacity. **Hallucination** is when the model states confident but **false** facts. **Training data** is the text the model learned from during pre-training.

**In Simple Words:** A 0.5B model has a **tiny brain** — fast and cheap to run, but it has read less and remembers patterns more weakly than a 70B model.

**Real-Life Example:** Asking a 0.5B model for detailed legal advice is like asking a **first-year student** to draft a Supreme Court petition — they might sound confident and still be wrong.

### Trade-offs to remember

| Advantage of tiny local models | Disadvantage |
|---|---|
| Runs on almost any laptop | **Limited reasoning** on multi-step problems |
| Fast enough for demos | **Weaker languages** and niche facts |
| No API bill per token | **Higher hallucination risk** on obscure topics |
| Great for learning APIs & agents | Not ideal for production quality without RAG/tools |

### How to get better answers from a small model anyway

- Use **clear, short prompts** — skills from the Prompt Engineering session apply directly.
- Add a **system message**: “If you are unsure, say you do not know.”
- For factual work, combine with **RAG** (coming next) so the model reads real documents instead of guessing.
- When quality matters on a weak laptop, use a **cloud API** (Groq in class) for that task only.

> **Common doubt:** “My local model gave a wrong date for an exam — is Ollama broken?”  
> **Answer:** The model **predicted** plausible text; it did not look up a calendar. That is expected for small models — fix with better prompts, grounding (RAG), or a larger model.

---

## Training-Data Bias — Chinese vs US Models

When you pull models like **Qwen** or run **DeepSeek**, you are not just choosing size — you are choosing **what data the model was trained on**.

**Official Definition:** **Training-data bias** means a model’s answers reflect the geography, language, and viewpoints present in its pre-training corpus — not an neutral encyclopedia.

**In Simple Words:** Two news channels can report the “same event” differently; LLMs trained on different countries’ internet text do the same in answer form.

**Real-Life Example (from class):** Ask about **Taiwan**, **Palestine**, or **Iran** on **DeepSeek** (Chinese-trained context) vs **ChatGPT** (US/Western-trained context). Wording, framing, and “controversial” labels can differ sharply — not because one API is broken, but because **internal knowledge** comes from different propaganda and media ecosystems.

### What to do as a builder

- **Know the model’s origin** before using it for sensitive or geopolitical content.
- **Do not assume** open-source equals neutral — open weights still carry **cultural bias**.
- For regulated or enterprise work, teams often pick models audited for their **jurisdiction and compliance** needs.
- Same **prompt engineering** rules apply; bias is a **data** issue, not a prompt-format issue.

> **[ Student Activity ]**
>
> **Bias Spot Check (10 minutes)**
>
> - Pick **one factual-but-political** question (keep it respectful and course-appropriate).
> - Run it on a **Chinese-origin** model you have access to (e.g. Qwen local or DeepSeek web) and on **ChatGPT** or another US/Western model.
> - Write two sentences: what is **similar** in both answers, and what **framing** differs.

---

## Groq Cloud API — Fast Inference Without Local Downloads

After the Ollama segment, class moved to **Groq** — a cloud platform that hosts large models (e.g. **Llama 3.3 70B**) with **very fast inference**, avoiding local heat and slowness.

**Official Definition:** **Groq** is a hosted inference platform that exposes LLMs through an **HTTP API** (similar in shape to OpenAI’s chat completions API). You create an **API key** at [console.groq.com](https://console.groq.com) and call models remotely.

**In Simple Words:** Groq is the **professional cloud kitchen** — you do not store the 70B “recipe book” at home; you send the order and get food in seconds.

**Real-Life Example:** Running **DeepSeek 9B** locally on the instructor’s basic laptop was **painfully slow**. The **same class of large model** on Groq returned in **under a second** — that contrast is why cloud POCs are popular for students.

### Step 1 — Create a Groq API key

1. Go to [https://console.groq.com](https://console.groq.com) and sign in.
2. Open **API Keys** → **Create API key**.
3. Name the key (e.g. `class-demo`), choose expiration if prompted, click **Submit**.
4. **Copy the key immediately** — you often cannot see the full secret again after leaving the page.
5. Paste it temporarily into **Notepad** (never commit keys to GitHub or WhatsApp).

### Step 2 — Open the class notebook in Google Colab

- Use the **session class notebook** uploaded for this lecture (Jupyter / Colab).
- Colab gives you a browser-based Python environment with no local GPU required.

### Step 3 — Store the key in Colab Secrets

1. In Colab, click the **key icon** (Secrets) in the left sidebar.
2. Click **Add new secret**.
3. **Name:** `GROQ_API_KEY` (must match what the notebook expects).
4. **Value:** paste your Groq API key from Notepad.
5. Toggle access for the notebook if Colab asks.

**In Simple Words:** Secrets are Colab’s locked drawer — your code reads the key without showing it on screen in every cell.

### Step 4 — Run the Groq chat cell

The live notebook followed the same pattern you saw in Prompt Engineering: **system message**, **user message**, then **`client.chat.completions.create`**.

```python
# Install the Groq Python library (run once in Colab)
# !pip install groq

# Import Groq and os for reading secrets
import os
from groq import Groq

# Read the API key from Colab secrets / environment
api_key = os.environ.get("GROQ_API_KEY")

# Create a client that talks to Groq's servers
client = Groq(api_key=api_key)

# System prompt sets the assistant's role for the whole call
system_message = "You are a helpful hospital assistant. Return structured notes only."

# User message is the live input (e.g. doctor's raw notes)
user_message = "Patient: 45F, Krishna Veni. Complains of mild fever for 2 days."

# Pick a cloud model Groq hosts (class used a Llama 3.3 variant)
model_name = "llama-3.3-70b-versatile"

# Send the chat request — same shape as OpenAI
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
)

# Print the assistant's reply text
print(response.choices[0].message.content)
```

**How the code works:**
- `Groq(api_key=...)` — connects to Groq using your secret key.
- `messages=[...]` — **system** + **user** roles from Prompt Engineering; nothing new in concept, only **implementation**.
- `client.chat.completions.create(...)` — standard OpenAI-style chat call; Groq uses the same pattern.
- `response.choices[0].message.content` — the generated answer string.

> **Common mistake:** Secret name typo (`GROQ_API_KEY` must match exactly) or forgetting to enable secret access for the notebook — the cell fails with “API key not found.”

> **[ Student Activity ]**
>
> **Groq First Run (20 minutes)**
>
> - Create your Groq API key and add it to Colab Secrets as `GROQ_API_KEY`.
> - Run the notebook cell until you see a **checkmark** and a printed response.
> - Change only the **user_message** to a question about your favourite subject and run again.

---

## The Same Pattern Everywhere — OpenAI and Anthropic

Once Groq worked, the instructor showed that **most cloud LLM APIs look alike** — change the **client**, **API key**, and **model name**; keep **messages** the same.

**Official Definition:** A **chat completions API** accepts a list of `{role, content}` messages and returns an assistant reply. OpenAI popularised this shape; Groq follows it closely; Anthropic uses a closely related **messages API**.

**In Simple Words:** Same restaurant order slip — different kitchens (companies) fulfil it.

| Provider | Where you get keys | Typical Python client | Call method |
|---|---|---|---|
| **Groq** | [console.groq.com](https://console.groq.com) | `from groq import Groq` | `client.chat.completions.create(...)` |
| **OpenAI** | [platform.openai.com](https://platform.openai.com) | `from openai import OpenAI` | `client.chat.completions.create(...)` |
| **Anthropic** | [platform.anthropic.com](https://platform.anthropic.com) | `from anthropic import Anthropic` | `client.messages.create(...)` |

**Groq and OpenAI** — same story in class: `client.chat.completions.create`, system + user messages, swap model string.

**Anthropic** — small difference: method name is **`messages.create`** instead of **`chat.completions.create`**, but roles and content idea match.

```python
# OpenAI-style (Groq and OpenAI — same structure)
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Return JSON with name and diagnosis fields."},
    ],
)
print(response.choices[0].message.content)
```

```python
# Anthropic-style — note messages.create instead of chat.completions.create
from anthropic import Anthropic

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a helpful assistant.",
    messages=[
        {"role": "user", "content": "Return JSON with name and diagnosis fields."},
    ],
)
print(response.content[0].text)
```

**How the code works:**
- All three providers need a **secret API key** from their developer console — never hard-code in files.
- **System** instructions plus **user** input combine into one API call behind the scenes (same idea as the hospital demo UI from the previous session).
- Paid models (GPT-4 class, Claude Sonnet) cost more — class used them mainly to show **pattern parity**, not as your default homework stack.

> **Common doubt:** “Do I need to learn three different languages?”  
> **Answer:** No — learn **one message list pattern**. Provider docs differ slightly in client class and method names; agents and LangChain hide most of that later.

---

## Comparing Cloud Models on the Same Prompt

In class we ran the **same prompt and code** with only the **model** changed — e.g. Groq Llama vs OpenAI GPT — and compared outputs side by side.

**Official Definition:** A **fair model comparison** keeps prompt text, system rules, and temperature fixed; only the **model identifier** changes.

**In Simple Words:** Same exam question paper, different students — see who writes clearer answers.

### What we observed live

| Dimension | Smaller / free-tier cloud model | Stronger paid model (e.g. GPT-4 class) |
|---|---|---|
| **JSON structure** | Sometimes extra prose or messy formatting | Often **clean JSON** when asked |
| **Reasoning** | Good for demos; may miss edge cases | More reliable step-by-step answers |
| **Speed (Groq)** | Very fast on large open models | Depends on provider load |
| **Cost** | Groq free tier for learning | OpenAI/Anthropic tiers are **much costlier** — enterprises use them when quality pays off |

**Class example:** A medical-notes prompt that should return JSON — one model wrapped extra text; another returned **clean JSON** only. **Same prompt, same code** — only `model=` changed.

> **[ Student Activity ]**
>
> **Same Prompt, Two Models (15 minutes)**
>
> - In the notebook, run one **JSON-format** prompt on Groq.
> - Change only the model name (or provider if you have a second key) and run again.
> - Note one difference in **formatting** and one in **factual depth**.

**Connecting idea:** Prompt Engineering improves *how* you ask; model choice improves *what* the model can reason. Agents need **both**.

---

## Calling a Local Model from Python (Ollama API)

Cloud or local — the pattern is the same: your Python code sends a **JSON request** to an API and gets text back. For local Ollama, the “server” is on **your machine** at port **11434**.

This was **walkthrough content** at the end of class (notebook-style); the **live executed Python** segment used **Groq**. Follow the uploaded class notebook for the exact cells.

![Python sends a JSON chat request to Ollama on localhost:11434 and reads the assistant reply from the response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-05-ollama-api-flow.png)

### Install the Python library

```text
pip install ollama
```

### Script — Local Ollama

Save as `ask_ollama_local.py`:

```python
# Import the chat helper from the official Ollama Python package
from ollama import chat

# Name the small model you already pulled with "ollama pull"
LOCAL_MODEL = "qwen2.5:0.5b"

# Write the user question you want the model to answer
user_question = "List three healthy breakfast options for a busy college student in India."

# Call the local Ollama API (default host: http://localhost:11434)
response = chat(
    model=LOCAL_MODEL,  # Which downloaded model to use
    messages=[  # Chat format: a list of role + content pairs
        {
            "role": "user",  # This message is from the human
            "content": user_question,  # The actual text of the question
        }
    ],
)

# Pull the assistant's reply text out of the response dictionary
answer_text = response["message"]["content"]

# Show the answer in the terminal
print("Model used:", LOCAL_MODEL)
print("Question:", user_question)
print("Answer:")
print(answer_text)
```

**How the code works:**
- `from ollama import chat` — uses Ollama’s Python wrapper instead of raw HTTP.
- `LOCAL_MODEL` — must match a model from `ollama list` on your machine.
- `messages=[...]` — same chat structure as Groq/OpenAI: role + content.
- `chat(...)` — sends the request to **localhost**; Ollama must be running.
- Compared to Groq: no API key; processing happens **on your laptop** (slower for big models).

> **Common mistake:** Forgetting to `ollama pull` the model first — Python will error with “model not found.”

### Ollama Cloud (concept only — not live demo)

Ollama also offers **cloud-hosted models** on [ollama.com](https://ollama.com). The instructor explained that programmatically you would:

- Point **`host`** to `https://ollama.com` instead of localhost.
- Pass an **`Authorization: Bearer <API_KEY>`** header (from Ollama account settings).

**Same message list** as local — only **where processing runs** changes. We did **not** create an Ollama API key or run a live Ollama Cloud call in class; use **Groq** for your working cloud script today, and revisit Ollama Cloud when your notebook adds those cells.

> **[ Student Activity ]**
>
> **Python Local Call (follow-up)**
>
> - After class, run `ask_ollama_local.py` with: *“Explain blockchain to my grandmother in 80 words.”*
> - Change only the `user_question` string and run again.
> - If you get a connection error, open the Ollama app and run `ollama list`.

---

## Model Types Available Through Ollama

Ollama’s library is not only “chat text.” Tags and model cards tell you the **modality**.

**Official Definition:** A **modality** is the type of input/output a model supports — text, image, audio, or video.

**In Simple Words:** Some models only read **words**; others also “see” **pictures** or “hear” **sound**.

**Real-Life Example:** A text-only model is like a friend you can only **WhatsApp**. A vision model is like a friend you can also send **photos** to for feedback.

![Ollama model types by modality — text chat, vision with images, audio, and heavier video models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-07-modalities.png)

| Type | What it does | Example model families (library changes over time) |
|---|---|---|
| **Text** | Chat, completion, code help | Llama, Qwen, Gemma, Mistral |
| **Vision** | Image + text → description, Q&A | LLaVA, Llama 3.2 vision variants |
| **Audio** | Speech understanding or generation | Whisper-based tags (check library) |
| **Video** | Emerging; fewer models, heavier hardware | Check [ollama.com/search](https://ollama.com/search) for latest |

### How to check before you pull

- Visit [https://ollama.com/library](https://ollama.com/library) and read the model card.
- Use [https://ollama.com/search](https://ollama.com/search) filters: **vision**, **tools**, **thinking**, etc.
- Most **frontier chat models today are multimodal** — they accept more than plain text even in consumer UIs.

> **Common mistake:** Pulling a **vision** model for a text-only assignment — it wastes disk and RAM with no benefit.

---

## Multimodal AI in Action — Gemini and Google Photos

Beyond Ollama’s library browse, class closed with a **consumer multimodal** demo: **Gemini** connected to **Google Photos**.

**Official Definition:** **Multimodal** models accept and reason over **more than one data type** (text + images, voice, video metadata, etc.) in one conversation.

**In Simple Words:** You ask in plain English; the AI searches your **photos**, not just the web.

**Real-Life Example (from class):** Prompt: *“Show me all my photos of **sunrise and sunset** that I took **from flights**.”* Gemini searches connected Google Photos, pulls matching images, and answers in natural language — **true multimodality**, not keyword filename search.

This connects to **RAG and document search** you will build next — retrieve relevant media or text first, then generate an answer. Today’s takeaway: modern LLMs are not text-only toys; they **ground** answers in your data when permitted.

> **[ Student Activity ]**
>
> **Multimodal Thought Experiment (5 minutes)**
>
> - Write one prompt you could ask an AI if it had access to **your phone gallery** (e.g. “find receipts from March” or “photos with my dog at the beach”).
> - Write one sentence on why an enterprise might **not** want that gallery connected to a public cloud API.

---

## Open-Source LLMs Beyond Ollama (Big Picture)

Ollama is your **hands-on local tool**; the ecosystem is wider.

- **Hugging Face** hosts thousands of open models — researchers and companies publish weights there; useful when local hardware is insufficient for a quick POC.
- **Groq** (used heavily in class) hosts open models with fast inference — complementary to Ollama, not a replacement for learning local install.
- **llama.cpp**, **vLLM**, and others run models efficiently — Ollama wraps similar ideas for simplicity.
- **Open-weight** does not always mean **free for commercial use** — read each model’s **license** before shipping a product.

**Why this matters for agentic systems:** Agents need an LLM **engine**. You can swap engines (small local Ollama, Groq cloud, OpenAI paid) with small code changes — exactly what **LangChain** will automate in upcoming sessions.

---

## Key Takeaways

- **Local LLMs** (Ollama) run on your machine for privacy, practice, and zero per-token bills; **cloud APIs** (Groq in class) give speed and large models when your laptop cannot hold 70B weights.
- **Ollama CLI:** `ollama pull` + `ollama run` + `ollama list` are your core local tools; the **GUI** helps with settings and model storage paths.
- **Tiny models (0.5B–2B)** fit normal laptops but trade **accuracy** for **speed** — expect hallucinations; **training-data bias** differs across Chinese vs US model families.
- **Groq + Colab Secrets** is the standard class pattern for cloud inference: `GROQ_API_KEY`, `client.chat.completions.create`, system + user messages — same idea as OpenAI; Anthropic uses `messages.create`.
- **Same prompt, different model** shows real differences in JSON quality, reasoning, and cost — pick the engine for the task.
- **Multimodal** models (vision/audio/video tags on ollama.com; Gemini + Photos demo) show LLMs moving beyond plain chat — **RAG** builds on this next.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Category | Meaning |
|---|---|---|
| **Open-source LLM** | Concept | Model weights/code publicly available to download and self-host |
| **Local LLM** | Concept | Model inference runs on your computer, not a remote datacenter |
| **On-premise LLM** | Concept | Model runs inside an organisation’s private infrastructure |
| **Ollama** | Tool | App to pull, run, and API-serve LLMs locally (and route to some cloud models) |
| `ollama --version` | CLI | Check Ollama is installed |
| `ollama pull MODEL` | CLI | Download a model (e.g. `qwen2.5:0.5b`) |
| `ollama run MODEL` | CLI | Interactive chat in terminal |
| `ollama list` | CLI | Show downloaded models |
| `ollama ps` | CLI | Show model loaded in RAM |
| `ollama rm MODEL` | CLI | Delete a model to free disk |
| **Parameters (0.5B, 1B, 70B)** | Concept | Rough measure of model size and capability |
| **Hallucination** | Concept | Model outputs confident but incorrect information |
| **Training-data bias** | Concept | Answers shaped by where/how the model was trained |
| **Token** | Concept | Chunk of text the model reads/generates; speed = tokens per second |
| **localhost:11434** | API | Default local Ollama API address |
| `https://ollama.com` | API | Ollama Cloud host (concept — change `host` for cloud calls) |
| **Groq** | Platform | Fast cloud inference; [console.groq.com](https://console.groq.com) for API keys |
| **GROQ_API_KEY** | Env / Secret | Secret key for Groq API calls (Colab Secrets in class) |
| `pip install groq` | Python | Install Groq Python SDK |
| `client.chat.completions.create` | API | OpenAI-style chat call (Groq & OpenAI) |
| `client.messages.create` | API | Anthropic-style chat call |
| `pip install ollama` | Python | Install official Ollama Python library |
| `from ollama import chat` | Python | Simple local chat helper |
| **Chat API** | API type | Messages with roles → assistant reply |
| **Modality** | Concept | Input/output type: text, vision, audio, video |
| **Multimodal** | Concept | Model handles multiple input types (text + images, etc.) |
| **RAG** | Concept | Retrieve documents first, then generate answer (next topic) |
| **Hugging Face** | Platform | Hub for open model weights and datasets |
| **qwen2.5:0.5b** | Model | Example ultra-light text model for laptops |
| **llama3.3-70b-versatile** | Model | Example large model on Groq used in class |
