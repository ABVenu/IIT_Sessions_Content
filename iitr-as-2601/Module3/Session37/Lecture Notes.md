# Open-Source LLMs

## What We Covered So Far & What's Coming Next

In our last session, we focused on **Prompt Engineering** — how to talk to an LLM so it gives you reliable answers. We learned **System Prompts** vs **User Prompts**, **Zero-Shot** and **Few-Shot** prompting, **Chain-of-Thought**, prompt templates, self-correction, and how to design a full **agent prompt flow**. All of that assumed you already had access to an LLM somewhere in the cloud.

Today we open a second door: **running LLMs on your own machine** (or through Ollama’s free cloud tier) without depending only on paid APIs like OpenAI. You will install **Ollama**, run a **light local model**, call it from **Python**, then switch the same script to **Ollama Cloud** and compare the results.

**In this session, you will learn:**
- Why **local** and **open-source** LLMs matter for learning, privacy, and cost
- How to **install Ollama**, pull a **small model**, and chat from the **terminal**
- Why **heavy models** are a bad idea on a normal laptop — and what you trade off with **tiny models**
- How to call Ollama from **Python** (local first, then cloud with an API key)
- What Ollama can do beyond chat: **embeddings**, **vision**, **audio**, and more
- How to finish with **one script** that works for **local or cloud** by changing settings only

---

## Cloud LLMs vs Local LLMs — Why This Session Matters

Until now, most examples used LLMs as a **remote service**: your code sends a prompt over the internet, a company’s servers run the model, and the answer comes back. That is convenient, but it has limits.

**Official Definition:** A **local LLM** is a language model whose weights run on **your own computer** (CPU or GPU), without sending your prompt to a third-party cloud for inference. An **open-source LLM** is a model whose weights and often its code are **publicly available** for download, study, and self-hosting.

**In Simple Words:** A cloud LLM is like ordering food on Swiggy — fast and powerful, but you pay per order and the kitchen is far away. A local LLM is like cooking at home — you control ingredients and privacy, but your kitchen (laptop) has limited space and firepower.

**Real-Life Example:** If you are building a college project that reads **private placement data**, you may not want every question sent to a US server. Running a small model locally with Ollama keeps the data on your machine. For a **demo to the class**, Ollama Cloud gives you a bigger model without buying a GPU.

![Cloud LLM sends prompts to remote servers for power and cost per token; local LLM runs on your laptop for privacy and free practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-01-cloud-vs-local.png)

### Why learners should care

- **Cost:** Local runs do not charge per token — useful when you are practising hundreds of prompts.
- **Privacy:** Sensitive notes, internal documents, or personal journals stay on your device.
- **Learning:** You see that an LLM is **software + weights**, not magic in ChatGPT’s UI alone.
- **Agent building:** In upcoming sessions, **LangChain** and **RAG** will plug into Ollama the same way they plug into OpenAI — today you build that foundation.

> **Common doubt:** “If local is free, why use OpenAI at all?”  
> **Answer:** Big cloud models are trained on more data, run on faster hardware, and usually answer complex questions more accurately. Local tiny models are perfect for **learning, prototyping, and privacy**; cloud (OpenAI, Ollama Cloud, etc.) is better when **quality and speed** matter most.

---

## What Is Ollama?

**Official Definition:** **Ollama** is an open-source tool that makes it easy to **download, run, and manage** large language models on your computer. It exposes a **local HTTP API** (default: `http://localhost:11434`) so programs — terminal, Python, LangChain — can talk to the model the same way they talk to a cloud API.

**In Simple Words:** Ollama is like **Google Play Store + player** for AI models on your laptop. You “install” a model once (`ollama pull`), then “open” it whenever you need (`ollama run` or Python).

**Real-Life Example:** Think of Ollama as a **chai stall machine** in your hostel room. You stock one blend of tea leaves (the model file). Anytime you press the button (send a prompt), it brews a cup (generates text) without calling an outside café.

![Ollama pulls model weights to your machine once, then serves chat through a local API — like an app store plus player for LLMs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-02-what-is-ollama.png)

### What Ollama can do (overview)

| Capability | What it means | Typical use |
|---|---|---|
| **Chat** | Back-and-forth messages with roles (`user`, `assistant`, `system`) | Tutor bots, Q&A |
| **Text generation** | Single prompt → completion (no chat history) | Summaries, titles |
| **Embeddings** | Turn text into number vectors for search | RAG, similarity (coming in RAG sessions) |
| **Multimodal models** | Models that accept images, audio, or video (when you pull them) | Describe an image, transcribe audio |

We go deeper into **model types** later in this session. First: get Ollama running on your machine.

---

## Installing Ollama and Verifying the Setup

You only need to install Ollama **once** per computer. Pick the steps for your operating system.

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
| 3 | `ollama serve` | Only if the app is not running; most installs start the service automatically |

> **Common mistake:** Running `ollama pull` before the Ollama **service** is running. On Windows/Mac, open the Ollama app first. On Linux, ensure `ollama serve` is active if the desktop app is not used.

> **[ Student Activity ]**
>
> **Install & Verify (10 minutes)**
>
> - Install Ollama on your machine using the steps for your OS.
> - Run `ollama --version` and `ollama list`.
> - Raise your hand when both work — note one classmate’s OS if yours fails (Windows PATH issues are the most common).

---

## Pulling a Light Model and Running Your First Prompt (CLI)

**Official Definition:** **`ollama pull`** downloads a model’s weights from Ollama’s library to your machine. **`ollama run`** loads that model and opens an interactive chat in the terminal.

**In Simple Words:** `pull` = download the “brain file.” `run` = start chatting with that brain.

**Real-Life Example:** `pull` is like downloading a movie on Netflix for offline view. `run` is pressing Play.

![ollama pull downloads model weights to disk; ollama run loads the model and opens an interactive terminal chat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-03-pull-vs-run.png)

### Choose a light model (recommended for class laptops)

| Model tag | Approx. size | Good for |
|---|---|---|
| `qwen2.5:0.5b` | Very small (~0.5B parameters) | Fastest smoke test on weak laptops |
| `llama3.2:1b` | Small (~1B parameters) | Slightly better answers, still laptop-friendly |
| `gemma2:2b` | Small–medium | Use only if your machine has 8 GB+ RAM free |

**Avoid for regular laptops in class:** `llama3.1:70b`, `qwen2.5:72b`, or any **70B+** tag — they need large GPU RAM and will freeze or crash most student machines.

### Step-by-step CLI demo

```text
# Step 1: Download the small model (one-time, needs internet)
ollama pull qwen2.5:0.5b

# Step 2: Start an interactive chat session
ollama run qwen2.5:0.5b
```

When the `>>>` prompt appears, type a simple question:

```text
Explain photosynthesis in two simple sentences for a Class 8 student.
```

- Press **Enter** and wait — first reply may be slow while the model loads into RAM.
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
> - Everyone pulls the **same** small model (`qwen2.5:0.5b` or whatever the instructor standardizes).
> - Run the **same** three prompts: (1) a math word problem, (2) a Hindi translation task, (3) a creative story in 50 words.
> - Compare answers with your neighbour — note where the tiny model **hallucinates** or sounds vague.

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
- For factual work, combine with **RAG** (next sessions) so the model reads real documents instead of guessing.
- When quality matters, switch to **Ollama Cloud** or OpenAI for that task only.

> **Common doubt:** “My local model gave a wrong date for an exam — is Ollama broken?”  
> **Answer:** The model **predicted** plausible text; it did not look up a calendar. That is expected for small models — fix with better prompts, grounding (RAG), or a larger model.

---

## Calling a Local Model from Python (Ollama API)

Cloud or local — the pattern is the same: your Python code sends a **JSON request** to an API and gets text back. For local Ollama, the “server” is on **your machine** at port **11434**.

![Python sends a JSON chat request to Ollama on localhost:11434 and reads the assistant reply from the response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-05-ollama-api-flow.png)

### Install the Python library

```text
pip install ollama
```

### Script 1 — Local Ollama only

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
- `from ollama import chat` — uses Ollama’s Python wrapper instead of writing raw HTTP yourself.
- `LOCAL_MODEL` — must match a model from `ollama list` on your machine.
- `messages=[...]` — same chat structure as ChatGPT APIs: role + content.
- `chat(...)` — sends the request to **localhost**; Ollama must be running.
- `response["message"]["content"]` — the generated answer string.

> **Common mistake:** Forgetting to `ollama pull` the model first — Python will error with “model not found.”

> **[ Student Activity ]**
>
> **Python Local Call (20 minutes)**
>
> - Run `ask_ollama_local.py` with the class prompt: *“Explain blockchain to my grandmother in 80 words.”*
> - Change only the `user_question` string and run again.
> - If you get a connection error, check that the Ollama app is open and run `ollama list`.

---

## Ollama Cloud — Account, API Key, and Stronger Models

Sometimes you need a **bigger model** than your laptop can hold. **Ollama Cloud** runs selected models on Ollama’s servers while keeping a similar workflow to local Ollama.

**Official Definition:** **Ollama Cloud** provides hosted inference for certain models. You can use them via **`ollama signin`** and cloud-tagged models locally, or call **`https://ollama.com`** directly with an **API key**.

**In Simple Words:** Same brand (Ollama), but the “kitchen” moves to their cloud when your laptop is too small.

**Real-Life Example:** You practise cooking dal at home (local 0.5B). For a wedding catering order (hard reasoning task), you rent a professional kitchen (Ollama Cloud).

### Create account and API key

1. Open [https://ollama.com](https://ollama.com) and **sign up** (or sign in).
2. Go to **Settings → API keys** ([ollama.com/settings/keys](https://ollama.com/settings/keys)).
3. Click **Create API key** and copy it once — treat it like a password.
4. Set it in your terminal session (do not paste keys into GitHub or WhatsApp):

**macOS / Linux:**

```text
export OLLAMA_API_KEY="paste_your_key_here"
```

**Windows PowerShell:**

```text
$env:OLLAMA_API_KEY="paste_your_key_here"
```

5. Optional CLI sign-in for cloud models through the desktop app:

```text
ollama signin
```

6. Pull a cloud-capable model (example from Ollama docs — your instructor may pick another):

```text
ollama pull gpt-oss:120b-cloud
```

> **Security rule:** Never commit API keys in code. Use environment variables only.

---

## Updating Python to Call Ollama Cloud

Only two ideas change versus local: **`host`** points to `https://ollama.com`, and **`Authorization`** header carries your API key.

### Script 2 — Ollama Cloud only

Save as `ask_ollama_cloud.py`:

```python
# Read secret API key from environment (set before running the script)
import os

# Import Client so we can set host and headers for cloud
from ollama import Client

# Read the API key from the environment variable OLLAMA_API_KEY
api_key = os.environ.get("OLLAMA_API_KEY")

# Stop early with a clear message if the key is missing
if not api_key:
    raise ValueError("Set OLLAMA_API_KEY in your terminal before running this script.")

# Build a client that talks to Ollama Cloud instead of localhost
cloud_client = Client(
    host="https://ollama.com",  # Remote Ollama host
    headers={
        "Authorization": "Bearer " + api_key,  # Prove who you are
    },
)

# Pick a cloud model name (must be available on your Ollama account/plan)
CLOUD_MODEL = "gpt-oss:120b"

# The question you want answered
user_question = "List three healthy breakfast options for a busy college student in India."

# Send the chat request to Ollama Cloud
response = cloud_client.chat(
    model=CLOUD_MODEL,
    messages=[
        {
            "role": "user",
            "content": user_question,
        }
    ],
)

# Extract assistant text from the response
answer_text = response["message"]["content"]

# Print results for comparison with local output
print("Model used:", CLOUD_MODEL)
print("Host: https://ollama.com (cloud)")
print("Question:", user_question)
print("Answer:")
print(answer_text)
```

**How the code works:**
- `os.environ.get("OLLAMA_API_KEY")` — loads the key without hard-coding it.
- `Client(host="https://ollama.com", headers={...})` — switches from laptop to cloud server.
- `Bearer` token — standard way APIs accept secret keys.
- `cloud_client.chat(...)` — same `messages` shape as local; only the **endpoint** changed.

> **Common mistake:** Using a **local-only** model name on cloud (or vice versa). Check [ollama.com/library](https://ollama.com/library) for cloud-supported tags.

---

## Comparing Local Light Model vs Ollama Cloud on the Same Prompt

Fair comparison needs the **same question**, **same system rules**, and honest notes about **speed** and **accuracy**.

### Suggested comparison prompt

Use this exact text in both scripts:

```text
A train leaves Delhi at 9:00 AM at 60 km/h. Another leaves Mumbai at 10:00 AM at 80 km/h toward Delhi. The cities are 1400 km apart. When do they meet? Show reasoning step by step, then give the final time.
```

### What to observe

| Dimension | Local (`qwen2.5:0.5b`) | Ollama Cloud (larger model) |
|---|---|---|
| **Speed** | Often faster after first load on weak GPU-less laptops | Depends on network; first token may take longer |
| **Reasoning** | May skip steps or invent numbers | Usually more structured CoT-style steps |
| **Hallucination** | Higher risk on math/facts | Lower, but still possible — always verify |
| **Cost** | Free on your machine | Subject to Ollama cloud/free-tier limits |
| **Privacy** | Prompt stays local | Prompt sent to Ollama servers |

![Same prompt on two paths — local tiny model for privacy and zero cost versus Ollama Cloud for stronger step-by-step reasoning](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-06-local-vs-cloud-compare.png)

### Sample discussion table (fill during class)

| Check | Local answer | Cloud answer |
|---|---|---|
| Did it show steps? | Yes / No | Yes / No |
| Final time plausible? | Yes / No | Yes / No |
| Any invented facts? | Notes | Notes |

> **[ Student Activity ]**
>
> **Local vs Cloud Showdown (25 minutes)**
>
> - Run the **same** comparison prompt on local and cloud scripts.
> - Copy one paragraph from each answer into a shared doc.
> - Vote: which answer would you **trust** for homework? Which would you **trust** for a hackathon demo?

**Connecting idea:** Prompt Engineering improves *how* you ask; model size improves *what* the model can reason. Agents need **both** — good prompts on the right model.

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
- Look for labels like **vision**, **image**, **audio**, or **embeddings**.
- Start with **text** models in this course; try vision/audio only if RAM allows.

> **Common mistake:** Pulling a **vision** model for a text-only assignment — it wastes disk and RAM with no benefit.

---

## Embeddings with Ollama (Preview for RAG)

**Official Definition:** An **embedding** is a list of numbers representing the **meaning** of a piece of text. Similar meanings → similar number patterns. **RAG** uses embeddings to find the right document chunk before the LLM answers.

**In Simple Words:** Embeddings turn sentences into **GPS coordinates in meaning-space** so “refund policy” and “money back rules” land near each other.

**Real-Life Example:** In a library, embeddings are like putting each book on a shelf by **topic** instead of only by title spelling.

![Similar sentences map to nearby points in embedding space — the foundation RAG uses to find the right document chunk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-08-embeddings-meaning-space.png)

### Minimal embeddings example (local)

```python
# Import the embed function from Ollama's Python package
from ollama import embed

# Choose a model that supports embeddings (example; check "ollama list" / library)
EMBED_MODEL = "nomic-embed-text"

# Two short sentences we want to compare semantically
sentence_a = "How do I return a product?"
sentence_b = "What is the refund policy?"

# Ask Ollama to convert the first sentence into a vector (list of numbers)
vector_a = embed(model=EMBED_MODEL, input=sentence_a)["embeddings"][0]

# Convert the second sentence the same way
vector_b = embed(model=EMBED_MODEL, input=sentence_b)["embeddings"][0]

# Show only the length and first few numbers (full vector is long)
print("Embedding length:", len(vector_a))
print("First 5 numbers of sentence A:", vector_a[:5])
print("First 5 numbers of sentence B:", vector_b[:5])
```

**How the code works:**
- `embed(model=..., input=...)` — calls Ollama’s embeddings endpoint locally.
- `["embeddings"][0]` — first vector in the response list.
- You normally compute **similarity** between vectors in RAG — full pipeline comes in **RAG Foundations**.

> Pull the embed model once: `ollama pull nomic-embed-text`

---

## One Python Script — Local or Cloud (Session Capstone)

The goal is **one file** where you flip between local and cloud using settings — no copy-paste of two separate projects.

![One capstone script branches on USE_CLOUD — local localhost chat versus Ollama Cloud with an API key](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session37/session37-09-one-script-toggle.png)

Save as `ask_ollama.py`:

```python
# Use os.environ for secrets and mode flags
import os

# Client for custom host; chat for simple local one-liners
from ollama import Client, chat

# ----- SETTINGS (change only this block) -----

# Set USE_CLOUD to "1" for Ollama Cloud, "0" for local laptop
USE_CLOUD = os.environ.get("USE_CLOUD", "0")

# Model names (must match what you pulled / have on cloud)
LOCAL_MODEL = "qwen2.5:0.5b"
CLOUD_MODEL = "gpt-oss:120b"

# The prompt you want to test
user_question = "Explain what an AI agent is in 60 words for a beginner."

# ----- END SETTINGS -----


def ask_local(question: str) -> str:
    """Send a chat request to Ollama running on this computer."""
    response = chat(
        model=LOCAL_MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return response["message"]["content"]


def ask_cloud(question: str) -> str:
    """Send a chat request to Ollama Cloud with API key auth."""
    api_key = os.environ.get("OLLAMA_API_KEY")
    if not api_key:
        raise ValueError("For cloud mode, set OLLAMA_API_KEY in your environment.")

    cloud_client = Client(
        host="https://ollama.com",
        headers={"Authorization": "Bearer " + api_key},
    )
    response = cloud_client.chat(
        model=CLOUD_MODEL,
        messages=[{"role": "user", "content": question}],
    )
    return response["message"]["content"]


def main() -> None:
    """Pick local or cloud based on USE_CLOUD and print the answer."""
    if USE_CLOUD == "1":
        mode_label = "CLOUD"
        answer = ask_cloud(user_question)
        model_label = CLOUD_MODEL
    else:
        mode_label = "LOCAL"
        answer = ask_local(user_question)
        model_label = LOCAL_MODEL

    print("Mode:", mode_label)
    print("Model:", model_label)
    print("Question:", user_question)
    print("Answer:")
    print(answer)


# Run main only when this file is executed directly (not imported)
if __name__ == "__main__":
    main()
```

**How the code works:**
- `USE_CLOUD` — environment flag: `0` = laptop, `1` = cloud.
- `ask_local` — uses default `chat()` → `localhost:11434`.
- `ask_cloud` — builds `Client` with `https://ollama.com` and Bearer token.
- `main()` — single entry point; prints which mode ran.
- `if __name__ == "__main__"` — standard Python pattern so imports stay clean.

### How to run both modes

**Local (default):**

```text
python ask_ollama.py
```

**Cloud:**

```text
export OLLAMA_API_KEY="your_key"
export USE_CLOUD=1
python ask_ollama.py
```

> **[ Student Activity ]**
>
> **Capstone Checklist (30 minutes)**
>
> - [ ] Ollama installed; `ollama --version` works  
> - [ ] Light model pulled; CLI chat works  
> - [ ] `ask_ollama.py` returns an answer in **local** mode  
> - [ ] API key created; **cloud** mode works with `USE_CLOUD=1`  
> - [ ] Same prompt run twice — you can explain **one** difference in quality  
>
> *Instructor: spot-check 3 students’ terminals live.*

---

## Open-Source LLMs Beyond Ollama (Big Picture)

Ollama is your **hands-on tool** today; the ecosystem is wider.

- **Hugging Face** hosts thousands of open models — researchers and companies publish weights there.
- **llama.cpp**, **vLLM**, and others run models efficiently — Ollama wraps similar ideas for simplicity.
- **Open-weight** does not always mean **free for commercial use** — read each model’s **license** before shipping a product.

**Why this matters for agentic systems:** Agents need an LLM **engine**. Ollama lets you swap engines (small local, big cloud, embeddings) with small code changes — exactly what **LangChain** will automate in the next module sessions.

---

## Key Takeaways

- **Local LLMs** run on your machine for privacy, practice, and zero per-token bills; **cloud LLMs** (including Ollama Cloud) give more power when your laptop cannot hold large weights.
- **Ollama** downloads and serves models through an easy CLI and a **localhost API** at port **11434**; **`ollama pull`** + **`ollama run`** are your first tools every time.
- **Tiny models (0.5B–2B)** are perfect for learning and scripting, but expect **weaker reasoning** and more **hallucinations** — use clear prompts and later **RAG** for facts.
- **Python + `pip install ollama`** lets you call local or cloud by changing **host**, **model name**, and **`OLLAMA_API_KEY`** — same message format as other LLM APIs.
- Your **capstone script** should switch **local vs cloud** with one setting; upcoming sessions plug this into **LangChain** and **RAG** so agents can use your own library of documents.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Category | Meaning |
|---|---|---|
| **Open-source LLM** | Concept | Model weights/code publicly available to download and self-host |
| **Local LLM** | Concept | Model inference runs on your computer, not a remote datacenter |
| **Ollama** | Tool | App to pull, run, and API-serve LLMs locally (and route to cloud models) |
| `ollama --version` | CLI | Check Ollama is installed |
| `ollama pull MODEL` | CLI | Download a model (e.g. `qwen2.5:0.5b`) |
| `ollama run MODEL` | CLI | Interactive chat in terminal |
| `ollama list` | CLI | Show downloaded models |
| `ollama ps` | CLI | Show model loaded in RAM |
| `ollama signin` | CLI | Log in for Ollama Cloud features |
| `ollama rm MODEL` | CLI | Delete a model to free disk |
| **Parameters (0.5B, 1B, 70B)** | Concept | Rough measure of model size and capability |
| **Hallucination** | Concept | Model outputs confident but incorrect information |
| **localhost:11434** | API | Default local Ollama API address |
| `https://ollama.com` | API | Ollama Cloud API host |
| **OLLAMA_API_KEY** | Env var | Secret key for direct Ollama Cloud API calls |
| **USE_CLOUD** | Env var | Custom flag in capstone script (`0` local, `1` cloud) |
| `pip install ollama` | Python | Install official Ollama Python library |
| `from ollama import chat` | Python | Simple local chat helper |
| `from ollama import Client` | Python | Client with custom `host` and headers |
| `from ollama import embed` | Python | Create embedding vectors for RAG |
| **Chat API** | API type | Messages with roles → assistant reply |
| **Embeddings** | API type | Text → numeric vectors for semantic search |
| **Modality** | Concept | Input/output type: text, vision, audio, video |
| **RAG** | Concept | Retrieve documents first, then generate answer (next session) |
| **Bearer token** | Security | `Authorization: Bearer <API_KEY>` header format |
| **qwen2.5:0.5b** | Model | Example ultra-light text model for laptops |
| **llama3.2:1b** | Model | Example small text model |
| **nomic-embed-text** | Model | Example embedding model for local RAG prep |
| **gpt-oss:120b** | Model | Example large cloud model name (verify on ollama.com) |
