# LLM Internals for Designers

## Introduction

**Retrieval-augmented generation (RAG)**, **conversation memory**, and **tool-using agents** are common ways to build useful LLM products. Each pattern packs text into every API call — retrieved chunks, chat history, and tool observations all share one fixed **context window**.

This document explains **LLM internals for designers** — **tokens**, **context limits**, **temperature**, and **determinism**. The goal is practical: know what drives **billing**, **latency**, **consistency**, and what users feel when context runs out.

**What you will learn:**

- **Relate** **tokens** to **billing**, **latency**, and how long your prompts should be
- **Explain** how **context limits** shape **RAG**, **memory**, and **agent** design choices
- **Configure** **temperature** (and **seed** where available) for **consistency** vs **creativity**
- **Predict** what users see when **context is truncated** or **overloaded** in multi-turn agent loops

![LLM internals for designers — RAG chunks, chat history, and tool logs share one context window tiffin box](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-01-designer-llm-internals.png?v=20250614)

---

## Why Designers Need LLM Internals

You do not need to train a model to ship a useful agent. You **do** need to know what the model **eats**, what it **forgets**, and why two runs with the same question can differ.

- **Official Definition:** **LLM internals** (for product and design) are the **measurable behaviours** of a language model — tokenisation, context window size, sampling randomness, and latency — that affect **cost**, **reliability**, and **user experience**.
- **In Simple Words:** The model is like a **tiffin box with a fixed number of compartments**. Everything you put in — instructions, PDF chunks, chat history, tool logs — shares that space. When the box is full, something gets thrown out.
- **Real-Life Example:** A **DMRC metro train** has a maximum capacity. Passengers (tokens) keep boarding at each station (each turn). Once full, new people cannot enter unless someone gets off — that is **truncation**.

| Common design decision | Hidden internal it depends on |
|---|---|
| **`top_k=3`** in RAG | Fewer chunks → fewer **tokens** in the prompt |
| **Persisted chat history file** | Every saved turn adds **tokens** when reloaded into the next call |
| **Verbose agent trace** | **Thought / Observation** text is sent back into the loop |
| **`temperature=0`** | Low **randomness** — more repeatable answers |

- **Common mistake:** Treating the LLM like **unlimited Google Drive** — long prompts slow down answers, cost more, and eventually **drop** older content without a clear error banner.
- **Core design questions:** *"How much can I pack into one request?"* and *"Why did the bot forget what the user said three turns ago?"*

---

## Tokens vs Words

When you type *"Namaste, how are you?"* you see **six words**. The model does not count words — it counts **tokens**.

- **Official Definition:** A **token** is the smallest unit of text an LLM reads and generates. Tokens come from **subword** pieces — whole words, parts of words, punctuation, or spaces — after **tokenisation**.
- **In Simple Words:** The model chops your sentence into **bite-sized pieces** it has seen during training. *"ChatGPT"* might be one token; a rare Hindi-English mix might split into more pieces.
- **Real-Life Example:** At a **ration shop**, the clerk weighs rice in **kilograms**, not "handfuls." APIs bill and limit by **tokens**, not by what looks like one word on your screen.

| What you see | What the API measures |
|---|---|
| 1 word in English (short) | Often ~1 token, not always |
| Long URL or JSON blob | Many tokens — symbols split heavily |
| Hindi + English mix | Token count can exceed word count |
| Empty line breaks | Still cost a few tokens |

![Tokens vs words — screen shows words; API bills and limits by tokens including URLs and mixed language](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-02-tokens-vs-words.png?v=20250614)

**Rule of thumb for planning (not exact):** ~4 characters ≈ 1 token in English prose. Always **measure** for production; use this only for back-of-envelope sketches.

- **Billing:** Cloud APIs (Groq, OpenAI, etc.) charge per **input token** and **output token**. A fat RAG prompt with **`k=10`** large chunks costs more than **`k=3`** — even if the user asked a five-word question.
- **Latency:** More tokens → more work per request. Users feel this as **longer waits** before the first word appears — especially when **history + retrieval + tool logs** stack up.
- **Prompt length decisions:** Designers trim **instructions**, cap **chunk size**, limit **history turns**, and compress **tool observations** to stay inside budget — same way you shorten a WhatsApp status to fit the character limit.

- **Common doubt:** *"If Groq is fast, why does my agent feel slow?"* — Often **token volume**, not the brand. Ten ReAct steps with long **Observation** strings multiply tokens every loop.
- **Common mistake:** Pasting a **full 40-page PDF** into one prompt instead of **chunking + retrieval** — you pay for the whole paste and may exceed the window.

### Measuring Tokens in Python

Use **`tiktoken`** (or your provider's counter) so design choices are based on numbers, not guesses.

```python
# Install once: pip install tiktoken
import tiktoken  # OpenAI-compatible token counting library

# Pick an encoding — cl100k_base matches many modern chat models
encoding = tiktoken.get_encoding("cl100k_base")  # Load the subword vocabulary table

sample_prompt = """
You are an annual report assistant for Acme Corp.
Answer ONLY from the context below.

=== CONTEXT START ===
Chunk 1 (source_id=acme_2023_p12): Revenue grew 19% year over year ...
=== CONTEXT END ===

Question: What was revenue growth in 2023?
"""

token_ids = encoding.encode(sample_prompt)  # Convert text to a list of token IDs
token_count = len(token_ids)  # Number of tokens in the whole prompt string

print(f"Words (split by space): {len(sample_prompt.split())}")  # Rough word count for comparison
print(f"Tokens (tiktoken): {token_count}")  # What matters for billing and limits
```

**How the code works:**

- **`get_encoding("cl100k_base")`** loads the same style of tokenizer many GPT-family and compatible APIs use.
- **`encode(text)`** returns integer token IDs — one ID per token piece.
- **`len(token_ids)`** is your **prompt token count** before the model generates an answer.
- Word count and token count **diverge** most on code, tables, and mixed-language text — always print both in early design drafts.
- **Groq / Llama note:** **`tiktoken`** uses an OpenAI-style encoding — counts are **close enough for budgeting** in lab; for exact Groq billing, use the **provider's token counter** in API responses when available.

### Activity 1 — Token Budget for One RAG Call

Build a sample RAG prompt with this structure: **instructions** (2–3 sentences), **three retrieved chunks** wrapped in `=== CONTEXT START ===` / `=== CONTEXT END ===`, and **one user question**. Run the full prompt through the **`tiktoken`** snippet above.

Fill in:

| Block | Approximate tokens |
|---|---|
| Instructions only | ? |
| All retrieved chunks | ? |
| User question | ? |
| **Total input** | ? |

Answer these follow-ups:

1. If the model's context window is **8,000 tokens**, what **percentage** did this single question use before the answer?  
2. At **₹0.002 per 1,000 input tokens**, what is the **input cost** for this one call?  
3. Two sentences: what would you trim first if users complain about **slow replies** — instructions, chunks, or history?

---

## Context Limits and the Context Window

Every model accepts only a **maximum** number of tokens per request — input plus output together. That ceiling is the **context window**.

- **Official Definition:** The **context window** (or **context limit**) is the maximum number of tokens an LLM can process in one forward pass — including system text, user messages, retrieved documents, tool results, and the generated reply.
- **In Simple Words:** It is the **size of the model's short-term desk**. Only what fits on the desk can be "seen" at once. Everything else is simply not there for that call.
- **Real-Life Example:** A **single-page exam answer sheet** — if you write past the margin, the invigilator does not read the overflow. The model behaves similarly: overflow tokens are **dropped** or **never sent**.

| Model class (examples) | Typical window (check your provider docs) |
|---|---|
| Smaller chat models | 4k–8k tokens |
| Mid-size production models | 8k–32k tokens |
| Long-context variants | 128k+ tokens |

Exact numbers change by **model name** and **provider** — always read the current Groq or API card. Design habits stay the same: **budget**, **measure**, **trim**.

- **Input + output share one budget:** A 8k window with 7k tokens of prompt leaves ~1k for the answer — long answers may get **cut off** mid-sentence.
- **RAG implication:** **`top_k`**, **chunk size**, and **metadata lines** (`source_id`, page) all compete for the same window. Raising **`k`** without shrinking chunks can **push out** older chat turns silently.
- **Memory implication:** Saving **full** history to a file (e.g. `chat_history.json`) is correct for persistence — but **loading all of it** into every API call is not always wise. Designers often keep **last N turns** or a **summary** for long sessions.
- **Agent implication:** Each ReAct cycle appends **Thought**, **Action**, and **Observation** to the scratchpad. Five tool calls with verbose web snippets can consume more window than the entire RAG corpus you carefully chunked.

![Context window budget — system, RAG, history, tool logs, question, and output slot share one fixed ceiling](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-03-context-window-budget.png?v=20250614)


- **Common mistake:** Assuming **JSON file on disk** equals **model memory** — the file can be huge while the **API call** only includes what your code attaches this turn.
- **Design pattern:** **Progressive disclosure** — retrieve less first; if the answer is thin, run a **second** search with higher **`k`** instead of always shipping everything.

---

## How Context Limits Constrain RAG Design

**RAG** was introduced so the model does not need the whole library in the prompt. Context limits are **why** RAG exists — and **why** RAG tuning matters.

- **Official Definition:** **Retrieval-augmented generation (RAG)** grounds answers by injecting **only relevant chunks** into the prompt instead of the full corpus.
- **In Simple Words:** You bring **two recipe cards** from the kitchen shelf, not the entire cookbook, because the counter is small.
- **Real-Life Example:** **IRCTC** shows only the trains for your route and date — not every train in India — because the screen and your patience have limits.

| RAG knob | When window is tight | When window is large |
|---|---|---|
| **`top_k`** | Keep low (2–4); precision over recall | Can raise slightly if answers miss facts |
| **Chunk size** | Smaller chunks — fit more variety | Larger chunks — more local context per hit |
| **Delimiter overhead** | `=== CONTEXT START ===` lines also cost tokens | Same — do not waste lines on decoration |
| **Citation labels** | Keep `source_id` short | Still keep them — grounding audits need them |

- **Reason to keep delimiters anyway:** Labels like **`source_id=acme_2023_p12`** cost tokens but save **trust** — designers shorten labels, not remove structure.
- **Grounding vs stuffing:** More chunks ≠ better answers. Irrelevant chunks add **noise** and **eat memory** for chat history — the model may cite the wrong paragraph.
- **Second-pass retrieval:** If the first answer says *"not in context,"* run retrieval again with a **rephrased query** before dumping more static text into the system prompt.

![RAG token budget — top_k chunks hard-capped at MAX_CONTEXT_TOKENS; excess chunks dropped from prompt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-04-rag-token-budget.png?v=20250614)

### Full Example — Trim Context Assembly for Token Budget

This script measures each stage and **hard-caps** how many chunks fit.

```python
# pip install tiktoken
import tiktoken  # Token counting

encoding = tiktoken.get_encoding("cl100k_base")  # Encoding for measurement

# Sample chunks returned from a vector database — newest first
retrieved_chunks = [
    {"source_id": "t23_p12", "page": 12, "text": "Revenue grew 19% year over year to $96.8B in 2023."},
    {"source_id": "t23_p8", "page": 8, "text": "Automotive gross margin improved sequentially in Q4."},
    {"source_id": "t23_p44", "page": 44, "text": "Energy storage deployments reached record levels."},
    {"source_id": "t22_p12", "page": 12, "text": "2022 revenue was $81.5B."},
]

MAX_CONTEXT_TOKENS = 600  # Designer-set budget for retrieval block only
INSTRUCTIONS = "Answer ONLY from CONTEXT. If missing, say you do not know."

def count_tokens(text: str) -> int:
    return len(encoding.encode(text))  # Helper — tokens in any string

def format_chunk(chunk: dict) -> str:
    # Compact label — long labels waste tokens
    header = f"[{chunk['source_id']} p{chunk['page']}]"  # Short citation tag
    return f"{header}\n{chunk['text']}"  # One chunk as prompt text

def build_context_block(chunks: list, max_tokens: int) -> str:
    parts = []  # Lines we will join
    used = 0  # Running token total for retrieval section
    for chunk in chunks:
        piece = format_chunk(chunk)  # Format one hit
        piece_tokens = count_tokens(piece)  # Measure this chunk
        if used + piece_tokens > max_tokens:
            break  # Stop — budget full; drop remaining chunks
        parts.append(piece)  # Accept chunk
        used += piece_tokens  # Update running total
    body = "\n---\n".join(parts)  # Delimiter between chunks
    return f"=== CONTEXT START ===\n{body}\n=== CONTEXT END ===", used  # Final block + count

context_block, ctx_tokens = build_context_block(retrieved_chunks, MAX_CONTEXT_TOKENS)
question = "What was 2023 revenue growth?"
full_prompt = f"{INSTRUCTIONS}\n\n{context_block}\n\nQuestion: {question}"

print("Chunks included:", context_block.count("---") + 1 if "---" in context_block else 1)
print("Context tokens:", ctx_tokens)
print("Full prompt tokens:", count_tokens(full_prompt))
```

**How the code works:**

- **`MAX_CONTEXT_TOKENS`** is a **designer knob** — separate from the model's full window; leave room for history and the answer.
- The loop **stops early** when the next chunk would overflow — mimics what you must do when **`top_k`** retrieval returns too much text.
- Short **`source_id`** labels save tokens without losing traceability.
- **`count_tokens(full_prompt)`** is what you compare against the provider's **context window**.

---

## How Context Limits Constrain Memory and Agent Loops

**Short-term memory** and **ReAct loops** append text every turn. Context limits decide **what the model still "remembers"** even when your JSON file remembers everything.

- **Official Definition:** **Short-term memory** in agents is the **conversation and scratchpad text** included in the **current** API request — not everything stored on disk.
- **In Simple Words:** Your **phone gallery** can hold 5,000 photos, but you can only **attach ten** to one email. The model only "sees" what you attach this time.
- **Real-Life Example:** A **doctor's case sheet** for today's visit — yesterday's full file exists in the cabinet, but only the **summary sticky note** is on the desk during your appointment.

| Source of growth | What gets long fast | Designer lever |
|---|---|---|
| Multi-turn chat | User + assistant pairs | **Last N turns**, rolling **summary** |
| ReAct scratchpad | Thoughts + observations | **`max_iterations`**, shorter tool outputs |
| Tool results | Web search JSON, dataframe prints | **Truncate** observation before re-prompt |
| RAG + memory together | Both in one call | **Shared budget table** per product feature |

- **`max_iterations`** or **`MAX_STEPS`** stops **infinite loops** — context limits stop **infinite text**. A production agent needs **both**.
- **Silent truncation:** Many stacks **drop oldest messages** when over limit — users see the bot "forget" a constraint from ten turns ago with **no error toast**.
- **Visible truncation:** Sometimes the answer ends abruptly or the model says *"I don't have access to earlier context"* — treat that as a **window signal**, not random stupidity.

![Memory truncation — full chat_history.json on disk vs only last N messages sent to model; grounding rule dropped](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-05-truncation-memory.png?v=20250614)

### Simulating Truncation — What Users Feel

```python
# No API key needed — pure design demonstration
MAX_MESSAGES = 4  # Designer cap: only last 4 messages sent to model

# Full history saved on disk (could be hundreds)
full_history = [
    {"role": "user", "content": "Use only Acme annual report facts."},
    {"role": "assistant", "content": "Understood — grounded answers only."},
    {"role": "user", "content": "2022 revenue?"},
    {"role": "assistant", "content": "$81.5B per report."},
    {"role": "user", "content": "And in 2023?"},
    {"role": "assistant", "content": "19% growth to $96.8B."},
    {"role": "user", "content": "What was Q4 automotive margin trend?"},
]

def windowed_history(history: list, max_messages: int) -> list:
    if len(history) <= max_messages:
        return history  # Everything fits — send all
    dropped = history[:-max_messages]  # Older messages that will NOT reach the model
    kept = history[-max_messages:]  # Tail — what the model actually sees
    return kept, dropped

kept, dropped = windowed_history(full_history, MAX_MESSAGES)

print("Messages sent to model:", len(kept))
for msg in kept:
    print(msg["role"], ":", msg["content"][:50])

print("\nDropped messages (still in JSON, invisible to model):")
for msg in dropped:
    print(msg["role"], ":", msg["content"][:50])
```

**How the code works:**

- **`full_history`** mimics a persisted `chat_history.json` — complete log on disk.
- **`windowed_history`** keeps only the **tail** — what many apps send when nearing token limits.
- The **system rule** (*"Use only Acme annual report facts"*) is in **`dropped`** — the model may **ignore grounding** even though the user set it at the start.
- **User-visible effect:** Follow-up questions that need **early constraints** fail unless you **re-inject** rules or **summarise** dropped turns.

### Activity 2 — Context Budget Planner

Imagine a support agent with a **12,000-token** window that uses **RAG**, **chat history**, and **tool observations**. Allocate tokens (rough estimates are fine):

| Component | Your token budget | Notes |
|---|---|---|
| System + safety rules | ? | |
| RAG chunks (max) | ? | |
| Last 5 chat turns | ? | |
| Tool observations (this turn) | ? | |
| Room for model answer | ? | Must stay ≥ 500 |
| **Total** | ≤ 12,000 | |

Then run the **truncation simulation** script above with **`MAX_MESSAGES=4`**. A user reports: *"The bot stopped following 'answer only from the report' after a long chat."*

Write four bullets:

1. Which message with the grounding rule was **dropped**?  
2. What would you **drop first** in a 20-turn debate — oldest chat turns, extra chunks, or tool logs?  
3. What **design change** fixes silent forgetting — repeat rules, summary memory, or larger window?  
4. What should the **user see** when truncation happens — silent failure or a banner?

---

## Temperature, Determinism, and Seed

**Temperature** controls how **random** the next token choice feels. **`temperature=0`** is the default habit for **grounded, factual** answers — this section explains **when to raise it** and **when never to**.

- **Official Definition:** **Temperature** is a sampling parameter that scales the randomness of token probabilities. **Lower** values sharpen the peak choice; **higher** values flatten the distribution so less likely tokens appear more often.
- **In Simple Words:** Choosing the next word is like picking a **cricket playing style**. **Temperature 0** is *play the safest single* every ball. **Temperature 1** is *sometimes try the risky scoop*.
- **Real-Life Example:** **Board exam marking** — you want the **same key** every year (**low temperature**). **Rangoli design** — you want **variation** across diwali (**higher temperature**).

| Setting | Behaviour | Good for |
|---|---|---|
| **`temperature=0`** | Nearly **deterministic** — same prompt → same answer (mostly) | RAG facts, policy bots, tool argument JSON |
| **`0.2 – 0.5`** | Slight variation — still professional | Support tone, light paraphrase |
| **`0.7 – 1.0`** | Creative, diverse wording | Marketing copy, brainstorming names |
| **Above 1.0** | Often chaotic — rare in production | Experiments only |

![Temperature and determinism — temperature 0 stable for RAG and tools; 0.8 varied for creative copy; seed for QA](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-06-temperature-determinism.png?v=20250614)

- **Determinism:** Even at **0**, tiny differences (API updates, batching) can shift output slightly — design for **"stable enough,"** not physics-level repeatability.
- **Seed (where available):** Some APIs accept a **`seed`** integer so random sampling becomes **reproducible** for tests. Not every provider exposes it — check Groq docs for your model.
- **Agents:** Use **low temperature** for steps that **call tools** or **cite sources**; consider **higher** only for a separate **"creative draft"** mode — not the same chain that emits **`Action: python_repl`**.

- **Common mistake:** High temperature on a **returns-policy bot** — users get conflicting refund rules turn to turn.
- **Common mistake:** Expecting **`temperature=0`** to fix **bad retrieval** — wrong chunks still produce confidently wrong facts; grounding is a **data** problem first.

### Full Example — Same Prompt, Two Temperatures

```python
# pip install langchain-groq
import os  # Environment variables for API key
from langchain_groq import ChatGroq  # Groq chat wrapper

groq_api_key = os.environ.get("GROQ_API_KEY")  # Your Groq key

prompt = "In one sentence, explain why over-the-air software updates matter for electric vehicles."

# Low temperature — stable, factual tone (RAG-friendly)
llm_strict = ChatGroq(
    model="llama-3.3-70b-versatile",  # Example Groq chat model
    api_key=groq_api_key,
    temperature=0,  # Minimise random token choices
)

# Higher temperature — more varied phrasing (creative mode)
llm_creative = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0.8,  # Allow less likely word choices
)

print("=== temperature=0 (three runs) ===")
for i in range(3):
    print(i + 1, llm_strict.invoke(prompt).content)

print("\n=== temperature=0.8 (three runs) ===")
for i in range(3):
    print(i + 1, llm_creative.invoke(prompt).content)
```

**How the code works:**

- Same **`prompt`**, same **`model`** — only **`temperature`** changes.
- **`temperature=0`** runs should look **almost identical** — good for regression tests on RAG answers.
- **`temperature=0.8`** runs should **differ in wording** while staying on topic — acceptable for marketing, risky for compliance numbers.
- Run this **three times** so you **see** variation — do not trust a single demo run.

### Activity 3 — Temperature, Seed, and Feature Design

**Part A — Run the comparison:** Execute the **Same Prompt, Two Temperatures** script above (or study sample output). Note whether **`temperature=0`** replies match across three runs and whether **`temperature=0.8`** replies vary.

**Part B — Assign settings:** For a **ShopEasy** product with RAG policy lookup, ReAct order-status tool, and a **"write festive SMS banner"** button, complete the table:

| Feature | Temperature (`0` / `0.3` / `0.9`) | Use fixed `seed`? (yes/no) | One-line reason |
|---|---|---|---|
| Refund policy Q&A (RAG) | ? | ? | |
| `lookup_order` tool planning | ? | ? | |
| Festive SMS generator | ? | ? | |

**Part C — Agent overload:** Users report *"After 15 questions, the bot invents revenue numbers."* List two causes tied to **context truncation** and one tied to **temperature**. One **design fix** for each.

---

## Randomness in Multi-Turn Agent Loops

A single chat message is one sampling pass. An **agent** chains **many** passes — randomness and context pressure **multiply**.

- **Official Definition:** A **multi-turn agent loop** is a repeated cycle of **model call → optional tool execution → model call again** until a stop condition, with **state** carried forward each time.
- **In Simple Words:** Each lap of the race, the runner carries a **heavier backpack** (more tokens). Temperature decides how **creatively** they pick the path each lap.
- **Real-Life Example:** **Auto-rickshaw negotiations** — each round adds more context (*"last offer was ₹120"*). If the driver forgets the first offer (**truncation**) or changes mood randomly (**high temperature**), you get a confusing ride.

| Loop stage | Token risk | Randomness risk |
|---|---|---|
| Initial plan | Moderate — system + user | Wrong tool choice if temp high |
| After search tool | **High** — snippets are long | Model may paraphrase numbers incorrectly |
| After Python REPL | Medium — numeric output | Low if temp=0 |
| Final answer | Competes with all prior steps | User sees **inconsistent tone** if temp high |

- **Designer checklist for agent loops:**
  - **`temperature=0`** (or very low) for tool-heavy chains  
  - **Cap observation length** — store full JSON in logs, pass **summary** to the model  
  - **`max_iterations`** / **`MAX_STEPS`** — stop runaway loops before the window explodes  
  - **Re-inject grounding rules** after truncation — never assume turn-1 instructions survive turn-20  

- **User-visible effects when overloaded:**
  - **Forgotten constraints** — *"I never said you could guess stock prices"*  
  - **Contradictory answers** — turn 4 says ₹337.50, turn 9 invents a different CAGR  
  - **Sudden brevity or refusal** — model lacks room for a proper answer  
  - **Tool hallucination** — model skips **`Action`** and guesses because scratchpad was trimmed  

![Multi-turn agent token growth — each ReAct lap adds tokens to scratchpad; cap observations and use temperature 0](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-07-agent-loop-token-growth.png?v=20250614)

---

## Designer Playbook — Practical Implications

Use this section as a **one-page checklist** when reviewing any RAG or agent feature before demo day.

| Question to ask | If answer is "yes" | Action |
|---|---|---|
| Does one request include **RAG + history + tools**? | Window risk | Build a **token budget table** per request |
| Are tool observations **>500 tokens** each? | Loop risk | Summarise before re-prompt |
| Must answers match **exact policy wording**? | Randomness risk | **`temperature=0`**, add **seed** in tests |
| Can sessions run **20+ turns**? | Truncation risk | **Summary memory** or **rule re-injection** |
| Are users billed per message? | Cost risk | Show **estimated usage** in admin docs |

- **Latency UX:** Show a **typing indicator** early; for long agent runs, show **step labels** (*"Searching…"*, *"Calculating…"*) so users know tokens are working, not stuck.
- **Error UX:** When the API returns **context length exceeded**, map it to *"This chat got too long — start a new thread or clear history"* — not a raw JSON traceback.
- **Testing habit:** Save three **golden prompts** with expected substrings; rerun after any **`temperature`**, **`top_k`**, or **history window** change.

---

## Putting It Together — End-to-End Request Anatomy

A typical **RAG + memory + agent** request might look like this inside the window:

```
[System instructions & grounding rules]     ~200 tokens
[Retrieved chunks — top_k=3]                ~900 tokens
[Windowed chat history — last 6 messages] ~1,400 tokens
[ReAct scratchpad this turn]                ~2,000 tokens
[New user question]                         ~30 tokens
[Reserved for model output]                 ~1,000 tokens
─────────────────────────────────────────────────────────
Estimated total                             ~5,530 tokens
```

![End-to-end request anatomy — typical RAG memory agent call token breakdown totaling about 5530 tokens](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session44/session44-08-end-to-end-anatomy.png?v=20250614)

- Numbers are **illustrative** — replace guesses with **`tiktoken`** counts on real prompts.
- The **designer job** is to ensure the **sum** stays below your provider window with **safety margin** (~10–15% free for longer answers).
- When you add a **second tool** or **raise k**, update this table **before** user testing — not after complaints.

---

## Key Takeaways

- **Tokens** are the model's billing and capacity unit — not words. Measure prompts with a counter; **`top_k`**, chunk size, history, and tool logs all add up.
- **Context windows** are shared desks — RAG chunks, memory, and agent scratchpads compete for the same space; overflow causes **silent forgetting** or **cut-off answers**.
- **`temperature=0`** (and **seed** when available) keeps RAG and tool loops **stable**; raise temperature only for **creative** surfaces, not compliance or numeric tools.
- **Multi-turn agents** multiply token and randomness risk — cap observations, limit iterations, and **re-inject rules** when history is windowed.
- **Designers** ship better agents when they budget tokens like money and treat truncation as a **user-visible state**, not a surprise.

Treating every prompt as a **finite token budget** is the foundation for tuning **chunking**, **retrieval**, and **executor** settings in any production LLM pipeline.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Token** | Concept | Smallest text unit the LLM processes; basis for billing and limits |
| **Tokenisation** | Concept | Splitting text into subword tokens before model input |
| **tiktoken** | Library | Count tokens (`encode`, `get_encoding`) for prompt budgeting |
| **Context window** | Concept | Max tokens per request — input + output combined |
| **Truncation** | Concept | Dropping oldest or excess text when over the window |
| **Input tokens** | Billing | Tokens you send — instructions, RAG, history, tools |
| **Output tokens** | Billing | Tokens the model generates in the reply |
| **Temperature** | Config | Randomness dial — 0 ≈ deterministic, higher = more varied |
| **Determinism** | Concept | Same input producing the same output (practical, not absolute) |
| **Seed** | Config | Fixed integer for reproducible sampling where supported |
| **`temperature=0`** | Config | Habit for RAG, policy, and tool-planning chains |
| **`top_k` retrieval** | Design knob | Fewer chunks → fewer tokens; trades recall for space |
| **Chunk size** | Design knob | Larger chunks → richer local context but heavier prompts |
| **Windowed history** | Pattern | Send only last **N** turns to stay inside budget |
| **Scratchpad** | Concept | ReAct Thought / Action / Observation text in the loop |
| **`max_iterations` / `MAX_STEPS`** | Config | Stops loops — separate from but related to token limits |
| **Observation truncation** | Pattern | Short summary to model; full tool JSON in logs only |
| **Progressive disclosure** | Pattern | Retrieve small first; expand only if answer is weak |
| **Context length exceeded** | Error | API signal — map to friendly "start new chat" UX |
| **`count_tokens(text)`** | Code pattern | `len(encoding.encode(text))` for design measurements |
| **`ChatGroq(temperature=...)`** | Code | Same model, different randomness per use case |
| **Silent forgetting** | UX risk | User constraints dropped without notification |
| **Token budget table** | Design doc | Per-feature allocation of window space before build |
