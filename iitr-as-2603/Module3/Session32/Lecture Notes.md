# Memory & Control Flow

## Context of This Session

In the **previous** session you built a **grounded Q&A helper** on **ShopEasy policies** — top-k retrieval on Chroma (`policy_chunks`), context assembly with **`===` delimiters** and **`source_id` / `page`** labels, and generation with **Ollama** or **Groq**. Each question was handled **on its own** — no memory of earlier turns.

That one-shot demo answered each question in isolation. Real customer chat is rarely one message. You ask *"How many days do I have to return a product?"* and get a grounded answer from the return policy. Ten seconds later you type only *"What about pickup?"* — no *"return"* repeated. Without **memory**, the bot treats it as a brand-new question and may search the wrong passages or ask you to repeat yourself.

Two other failures show up often: the **loop runs forever** (no stop rule), or the bot shows a **scary error log** when an API fails. Today you fix all three — **remember the chat**, **stop safely**, and **fail gracefully**.

**What you will learn:**

- **Define** an **AI agent** as a system that perceives, reasons, and acts using tools and memory  
- **Distinguish** **short-term memory** from **long-term memory**  
- **Persist and reload** conversation history across turns in a notebook  
- **Implement loop termination** so a chat loop cannot run forever  
- **Handle predictable errors** with clear, user-visible messages  

![One-shot ShopEasy RAG vs multi-turn chat with memory — the prior helper answered each question alone; follow-ups like What about pickup? need conversation history](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-01-one-shot-vs-multi-turn.png)

---

## What Is an AI Agent?

Before adding memory and stop rules, name the system you are building.

- **Official Definition:** An **AI agent** is a system that **perceives** input, **reasons** about what to do next, **acts** (often by calling tools such as search or an LLM), and can **remember** prior steps so later turns stay coherent.
- **In Simple Words:** Not a one-shot answer machine — a **small worker** that reads the question, uses tools, replies, and keeps a notepad.
- **Real-Life Example:** A **customer-care agent** hears your question, checks the policy folder (tool), answers, and remembers you already asked about returns when you say *"What about pickup?"*

| Step | Agent does | In this lab |
|---|---|---|
| **Perceive** | Read the new user message | `user_message` |
| **Reason** | Decide to search policies / reply / stop | Bounded loop + stop words |
| **Act** | Call your existing **`rag_answer`** | Chroma + Ollama/Groq from previous lab |
| **Remember** | Store the turn | `history` list + JSON file |
| **Stop** | End when done or unsafe | `MAX_STEPS`, `STOP_WORDS` |

- **Common doubt:** *Is every chatbot an agent?* A one-shot RAG call is **tool use**. Adding **memory + a controlled loop** is the beginner step toward agent behaviour on this track.
- Richer tool planning and multi-tool agents are covered in **later work**.

---

## Short-Term Memory vs Long-Term Memory

- **Official Definition:** **Short-term memory** is the **running chat history** for the **current session**. **Long-term memory** stores facts **across sessions** — saved queries, policy preferences, user profile notes.
- **In Simple Words:** Short-term is the **waiter's notepad for one table visit**. Long-term is the **loyalty card file at the counter**.
- **Real-Life Example:** On a **ShopEasy support chat**, everything said in that chat is short-term. When you close the tab, the helper forgets unless notes are saved.
- **Real-Life Example (long-term):** **ChatGPT Memories** stores facts about you across chats — that is long-term memory; the open chat window is short-term.

| Feature | Short-term | Long-term |
|---|---|---|
| **Duration** | This chat only | Days, weeks, months |
| **Storage** | Python `list`, JSON file | Database, vector store, user profile |
| **This session** | **Yes — main lab** | Introduced; deeper work **later** |

- **Common doubt:** *Do I need long-term memory for a three-message demo?* No — a **JSON history file** for this session is enough.
- Long-term memory matters when a shopper returns **next week** and expects the bot to remember last week's order issue without repeating.

![Short-term vs long-term memory — the lab uses a JSON history file for this session; database-style storage comes in later work](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-02-short-vs-long-term-memory.png)

---

## Conversation History — Your Short-Term Memory

Before saving to disk, use a simple **list of messages**. Each message has a **role** and **content**.

| Role | Who spoke |
|---|---|
| **`user`** | The shopper (you) |
| **`assistant`** | The ShopEasy policy bot |
| **`system`** | Hidden rules (optional) |

- **Order matters:** Always append **user** first, then **assistant**, for each completed turn.
- **Common mistake:** Sending only the **latest** message to the model — that erases everything from earlier turns.

```python
# Start with an empty history list
history = []

# After turn 1 — shopper asks, bot replies
history.append({"role": "user", "content": "How many days do I have to return a product?"})
history.append({"role": "assistant", "content": "You may return unused products within 30 days of delivery (from returns_policy.txt)."})

# After turn 2 — follow-up without repeating "return"
history.append({"role": "user", "content": "What about pickup?"})
history.append({"role": "assistant", "content": "[Pickup or related policy details from retrieved chunks]."})
```

**How the code works:**

- **`history`** is a Python list — easy to grow, save, and reload.
- Each dict has **`role`** and **`content`** — the same shape most LLM APIs expect.
- Turn 2 works because **return** and **30 days** are still in the list from turn 1 — so *"What about pickup?"* is understood in context.

![Conversation history as a message list — user and assistant turns appended in order; Turn 2 follow-up relies on Turn 1 context](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-03-conversation-history-list.png)

---

## Persist and Reload Conversation History

In-memory lists vanish when you **close the notebook**. **Persist** means save to a file; **reload** means read it back on the next run.

- **Official Definition:** **Persist** writes history to durable storage. **Reload** reads that storage back into your program.
- **In Simple Words:** Save the notepad to a file; open the same file next time.
- **Real-Life Example:** A clinic desk **writes visit notes in a folder** — tomorrow's staff reads it before calling the patient.

### Save and load with JSON

```python
import json  # Save and load conversation history as text

HISTORY_FILE = "shop_easy_chat_history.json"  # Short-term memory on disk


def save_history(history):
    """Write the full message list to JSON."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)  # Pretty-print for easy inspection


def load_history():
    """Reload history from disk, or start empty on first run."""
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)  # Same list structure as in memory
    except FileNotFoundError:
        return []  # First run — start fresh
```

**How the code works:**

- **`json.dump`** writes the list to a text file you can open in any editor.
- **`json.load`** reads it back into the same list structure.
- **`FileNotFoundError`** on first run returns an empty list — safe default.

### Append and save after each turn

```python
def append_turn(history, user_text, bot_text):
    """Add one user + assistant pair and persist immediately."""
    history.append({"role": "user", "content": user_text})  # Shopper message first
    history.append({"role": "assistant", "content": bot_text})  # Bot reply second
    save_history(history)  # Persist right away — survives a notebook restart
    return history
```

**How the code works:**

- **`append_turn`** keeps the **user-then-assistant** order every time.
- Saving **after each turn** means a kernel restart does not wipe the last exchange.
- **Common mistake:** Saving only at the end of the demo — one crash loses everything.

### Simple Activity — Persist and Reload

1. Run `load_history()` on a fresh folder — you should get an **empty list**.
2. Call `append_turn` with a sample user line and bot reply.
3. Run `load_history()` again **without** re-running append — confirm both messages appear.
4. One sentence: what breaks if you skip step 3 before the next shopper question?

![Persist and reload with JSON history file — save_history after each turn; load_history survives notebook restart](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-04-persist-reload-json.png)

---

## Pass Memory Into Your Existing RAG Helper

Your **previous** `rag_answer(user_query, collection, embed_model)` handled one isolated question against **`policy_chunks`**. For multi-turn follow-ups on the same policies, build the query from **history + new message** — do not rewrite retrieval or the generator backend.

- **In Simple Words:** Hand the model the **whole chat so far**, not just the newest bubble.
- **Real-Life Example:** A **support agent** re-reads earlier lines in the chat thread before answering the latest reply — not just the last sentence.

```python
def build_question_with_memory(history, new_message):
    """Join prior turns into one text block the RAG helper can search with."""
    parts = []
    for msg in history:
        parts.append(f"{msg['role']}: {msg['content']}")  # Prior turns in order
    parts.append(f"user: {new_message}")  # Latest shopper message last
    return "\n".join(parts)
```

**How the code works:**

- Loops over **`history`** so turn 2 still carries **return / 30 days** context from turn 1.
- The **new message** is added at the end — the latest shopper input.
- Pass the result to your existing **`rag_answer(full_question, collection, embed_model)`** — retrieval and generation stay unchanged.

### One-turn chat function (reuses prior lab)

```python
def chat_once(user_message, history, collection, embed_model):
    """One shopper message — search, reply, remember, save."""
    full_question = build_question_with_memory(history, user_message)

    try:
        result = rag_answer(full_question, collection, embed_model)  # From previous lab
        bot_reply = result["answer"]
    except Exception:
        bot_reply = "Search is unavailable right now. Please try again in a minute."

    append_turn(history, user_message, bot_reply)
    return bot_reply
```

**How the code works:**

- **`rag_answer`**, **`collection`**, and **`embed_model`** come from your **previous** ShopEasy RAG lab — no need to rebuild Chroma here.
- **`try/except`** returns a friendly line instead of a red traceback.
- **`append_turn`** updates memory and saves JSON in one step.

### Simple Activity — Two-Turn Follow-Up

Run these two messages in order (reuse your existing **`collection`** on `policy_chunks` from the prior lab):

1. *"How many days do I have to return a product?"*
2. *"What about pickup?"*

Check `shop_easy_chat_history.json` — turn 1 must be present before turn 2 runs. One sentence: what would go wrong without that file?

![Pass memory into rag_answer — build_question_with_memory joins history and new message; reuse policy_chunks from prior lab](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-05-memory-into-rag.png)

---

## Loop Termination — Stop Rules That Protect You

Sometimes one shopper message needs **two or three internal steps** — search policies, draft reply, check if anything is missing. A **loop** handles that. Without a **stop rule**, the loop runs forever and your API bill rises.

- **Official Definition:** **Loop termination** is an explicit condition that **ends** the loop — max steps reached, task done, or user typed stop.
- **In Simple Words:** The head waiter's rule — *"After three kitchen trips for the same table, call the manager."*
- **Real-Life Example:** An ATM gives **3 PIN tries** then keeps the card — a hard stop protects the system.

### Stop rules for the lab

| Rule | What it checks |
|---|---|
| **Max steps** | `step >= MAX_STEPS` — hard ceiling on loop iterations |
| **Task done** | Model produced a final reply (no more tool/search needed) |
| **User stop** | Shopper typed `quit`, `exit`, or `stop` |

- **Max steps is non-negotiable** — even if the model wants to keep trying, your code must stop.
- **Common mistake:** Trusting the model to say *"I'm done"* with **no step limit** — it can loop on rephrased searches forever.

### Simple bounded loop

```python
MAX_STEPS = 5  # Hard ceiling — never remove this guard
STOP_WORDS = {"quit", "exit", "stop"}  # Clean user exit phrases


def run_chat_turn(user_message, history, collection, embed_model):
    """Repeat internal steps until done or max steps — then return one reply."""

    if user_message.strip().lower() in STOP_WORDS:
        return "Chat ended. Thank you for using the ShopEasy policy assistant."

    step = 0
    bot_reply = ""

    while step < MAX_STEPS:
        step += 1

        full_question = build_question_with_memory(history, user_message)

        try:
            result = rag_answer(full_question, collection, embed_model)
            bot_reply = result["answer"]
        except Exception:
            return "Search is unavailable right now. Please try again in a minute."

        # For this beginner lab: one RAG call = task done
        break

    if step >= MAX_STEPS and not bot_reply:
        bot_reply = "I could not finish within the safe step limit. Please try a simpler question."

    append_turn(history, user_message, bot_reply)
    return bot_reply
```

**How the code works:**

- **`MAX_STEPS = 5`** is the safety rail — raise it only after testing; never remove it.
- **`STOP_WORDS`** lets the shopper exit cleanly.
- The loop **`break`s** after one successful `rag_answer` — task done.
- If the loop ever ran all 5 steps with no reply, the user sees a **polite stop message** instead of silence.
- **`append_turn`** saves memory after the loop finishes.

- **Why a loop if we break after one step?** This session teaches the **pattern**. In **later work** the loop will run multiple search-or-reply steps before `break`.
- Duplicate-action detection and multi-step planning loops are **advanced topics** — not needed in this lab.

### Simple Activity — Test the Step Limit

Temporarily set `MAX_STEPS = 0` and call `run_chat_turn` with any question. Confirm you get the polite step-limit message instead of an infinite loop. Set `MAX_STEPS` back to `5` before continuing.

![Loop termination — MAX_STEPS ceiling, task-done break, and STOP_WORDS prevent runaway iterations and protect API cost](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-06-loop-termination.png)

---

## Basic Error Handling — User-Visible Messages

When APIs fail, beginners often print **raw tracebacks**. Shoppers and demo users need **plain language**.

- **Official Definition:** **User-visible error handling** catches predictable failures and returns a short, friendly message.
- **In Simple Words:** When the kitchen printer jams, say *"Small delay — I'll update you shortly"* — not the printer error code.
- **Real-Life Example:** A UPI app shows *"Bank server busy, try again"* — not a Java stack trace.

| Error type | User-visible message (example) |
|---|---|
| **Connection / API down** | *"Search is unavailable. Please try again in a minute."* |
| **Empty index** | *"Document index is empty. Please run setup first."* |
| **Blank input** | *"Please type a question."* |

- **Catch at the call site** — wrap `rag_answer` in `try/except`, not only the outer notebook cell.
- **Log for yourself, simplify for the user** — `print(error)` in the notebook is fine; the **returned string** must stay friendly.
- **Common mistake:** Returning `str(exception)` to the user — exposes messy internal text.

```python
def safe_rag_answer(question, collection, embed_model):
    """Call rag_answer; return answer or a friendly error string."""
    if not question.strip():
        return "Please type a question."

    try:
        result = rag_answer(question, collection, embed_model)  # Same helper as previous lab
        return result["answer"]
    except Exception:
        return "Search is unavailable right now. Please try again in a minute."
```

**How the code works:**

- Checks for **blank input** before any API call.
- **`try/except`** catches network, Chroma, and generator failures in one place.
- Returns a **fixed friendly string** — same message every time, easy to trust in demos.

Swap `rag_answer(...)` inside `chat_once` or `run_chat_turn` with `safe_rag_answer(...)` if you want error handling in its own function.

![User-visible error handling — try/except returns a friendly message instead of exposing raw tracebacks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-07-error-handling.png)

---

## Notebook Demo — Put It Together

This is the **one lab path** for the session. Reuse **`collection`**, **`embed_model`**, and **`rag_answer`** from your **previous** ShopEasy RAG notebook — new cells only add **memory** and **control flow** on the same `policy_chunks` index.

```python
# --- Already built in previous lab — run once, do not rewrite ---
# client = chromadb.PersistentClient(path="./chroma_store")
# collection = client.get_or_create_collection(name="policy_chunks", embedding_function=None)
# embed_model = SentenceTransformer("all-MiniLM-L6-v2")
# rag_answer(user_query, collection, embed_model)  →  {"answer": ..., "retrieved_chunks": ...}

# --- Memory + control flow (new cells) ---
history = load_history()  # Reload prior turns if JSON exists

user_input = "How many days do I have to return a product?"
reply = run_chat_turn(user_input, history, collection, embed_model)
print("Bot:", reply)

user_input = "What about pickup?"  # Follow-up — topic not fully repeated
history = load_history()  # Fresh load — shows persist across cells
reply = run_chat_turn(user_input, history, collection, embed_model)
print("Bot:", reply)
```

**How the code works:**

- **`collection`**, **`embed_model`**, and **`rag_answer`** are unchanged from the **previous** grounded Q&A lab.
- **`load_history`** picks up any saved chat from an earlier cell or a prior run.
- **`run_chat_turn`** adds stop rules, calls RAG with full history, appends, and saves JSON.
- Turn 2 only says *"What about pickup?"* — but history still holds the **return-days** exchange from turn 1.

![Notebook demo flow — load_history, run_chat_turn, rag_answer on policy_chunks, append_turn; two-turn follow-up](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session42/session42-08-notebook-demo-flow.png)

---

## Managing Token Limits — Summarization

As multi-turn history grows, you may hit **token limits** on the LLM API — the model cannot accept an infinitely long prompt.

- **Official Definition:** **Summarization** compresses older turns into a shorter summary so the model keeps context without sending every full message.
- **In Simple Words:** Tear out the middle pages of a thick file and keep a **one-page summary** plus the latest replies.
- **Real-Life Example:** A long **ChatGPT** thread — behind the scenes, very old messages may be summarized so new replies still make sense.

**Ideas to remember:**

- Track a **token counter** after every few turns — when usage crosses a threshold, summarize.
- Pass the bloated history to the LLM once and ask for a **short summary** — often compress thousands of tokens down to a few hundred.
- Keep the **system message**, the **summary**, and the **latest user message** in the next call.
- This is **production practice** — your beginner lab uses a short JSON file, but real support chats need this guardrail.

### Simple Activity — Spot the Limit

After three turns in your ShopEasy demo, check how many messages are in `history`. One sentence: what would happen on turn 20 if you never summarized and never trimmed?

---

## When Something Goes Wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Turn 2 asks to repeat the topic | History not saved or not loaded | Call `append_turn`; run `load_history()` before turn 2 |
| Loop never stops | No `MAX_STEPS` | Keep `MAX_STEPS = 5`; never remove the while check |
| Empty history after restart | Wrong file name or path | Confirm `shop_easy_chat_history.json` exists in your folder |
| Red traceback in output | Raw exception shown | Use `safe_rag_answer` or `try/except` in `chat_once` |

- Most follow-up bugs are **missing append**, not a weak model — check `len(history)` after each turn.

---

## Key Takeaways

- An **AI agent** perceives, reasons, acts with tools, **remembers**, and **stops** — this lab adds memory and control flow on top of your ShopEasy RAG helper.
- **Short-term memory** is this session's chat list; **long-term memory** across weeks is **later work**.
- **Persist and reload** with JSON so *"What about pickup?"* still knows you were asking about **returns** without repeating the full question.
- **Loop termination** via **`MAX_STEPS`** and **stop words** prevents runaway iterations.
- **`try/except`** with a **friendly message** builds trust when APIs fail — essential for live demos.
- **Summarization** trims long histories when token limits bite — summarize old turns, keep recent messages.
- Richer tool loops and long-term user memory build on this pattern in **later work** on the same track.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **AI agent** | Concept | Perceive → reason → act with tools, memory, and stop rules |
| **Short-term memory** | Concept | Running chat history for this session |
| **Long-term memory** | Concept | Facts stored across sessions |
| **Conversation history** | Concept | List of `{role, content}` messages |
| **Bounded loop** | Concept | Repeat steps until done or max steps |
| **Loop termination** | Concept | Rules that end the loop |
| **Persist / reload** | Concept | Save and load history from JSON |
| **User-visible error** | Concept | Friendly failure text for the user |
| **Summarization** | Concept | Compress old chat turns to save tokens |
| **Token limit** | Concept | Maximum tokens an API accepts per request |
| `history` | Code | In-memory list of messages |
| `save_history` / `load_history` | Code | Write/read JSON file |
| `append_turn` | Code | Add user + assistant pair and save |
| `build_question_with_memory` | Code | Join history + new message for RAG |
| `chat_once` | Code | One turn: RAG + remember + save |
| `run_chat_turn` | Code | Bounded loop with stop rules |
| `safe_rag_answer` | Code | RAG call with friendly error fallback |
| `MAX_STEPS` | Config | Hard ceiling on loop iterations |
| `STOP_WORDS` | Config | User words that end the chat |
| `shop_easy_chat_history.json` | File | Saved short-term memory for ShopEasy chat demo |
| `json.dump` / `json.load` | Code | Serialize and parse history |
| `rag_answer` | Code | Prior ShopEasy RAG lab — `rag_answer(user_query, collection, embed_model)` |
| `policy_chunks` | Code | Chroma collection reused from previous labs |
