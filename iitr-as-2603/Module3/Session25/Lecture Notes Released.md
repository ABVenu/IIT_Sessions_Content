# LLM Internals for Designers

## Context of This Session

In the **previous** session you learned **prompt engineering** — how **system** and **user** roles split stable rules from live questions, how **zero-shot** and **few-shot** examples lock format, how **chain-of-thought** steps guide multi-step reasoning, and how **reusable templates** keep beginner agents consistent.

Before that, you built a foundation in **GenAI concepts** — **tokens**, **context windows**, **hallucinations**, and how LLMs **predict text** instead of looking up facts like a database.

This session goes one level deeper — not to train models, but to **design better prompts and products**. You will measure real **token counts**, understand **billing and latency trade-offs**, budget the **context window** across system prompts, examples, and chat history, and tune **temperature** for reliable testing in Python.

**In this session, you will:**

- Measure **token counts** for real prompts and relate them to **billing**, **latency**, and **length trade-offs**
- Explain how **context window limits** shape choices for **system prompts**, **few-shot examples**, and **conversation history**
- Configure **temperature** to trade **creativity vs consistency** when testing prompt variants in the **Groq API**
- Predict **user-visible effects** when context is **truncated or overloaded** — forgotten instructions, tone drift, and factual slips in long chats

---

## Why Designers Need LLM Internals

Prompt engineering tells you *what to write*. **LLM internals** tell you *what the model can actually hold and how it behaves* when you press Send.

- **Official Definition:** **LLM internals (for designers)** are the practical limits and controls — tokens, context windows, sampling settings — that shape model behaviour without requiring model training or neural-network math.
- **In Simple Words:** The **fuel tank size**, **meter reading**, and **accelerator sensitivity** of your AI car — you do not build the engine, but you must know how far it goes and how hard to press.
- **Real-Life Example:** A **Zomato delivery app** does not cook food — but the product team must know restaurant prep time, rider capacity, and peak-hour delays to design an honest ETA screen. Same idea for LLM-powered features.

| Designer question | Internal concept that answers it |
|---|---|
| *"Why did my bill spike this month?"* | **Input + output tokens** × price per token |
| *"Why did the bot forget my rules?"* | **Context window overflow** — early text dropped |
| *"Why do two test runs differ?"* | **Temperature** and **sampling randomness** |
| *"Why does my JSON prompt cost more than it looks?"* | **Tokenisation** — symbols and code split into many tokens |

- **Common mistake:** Judging prompt size by **word count** or **page count** — providers bill and limit by **tokens**.
- **Why this session matters:** Every agent you design packs **system rules + examples + history + user input + reply** into one shared window. Overspending any layer breaks the others.

---

## Tokens vs Words — Applied Depth

You already know that LLMs read **tokens**, not words. Here we apply that idea to **real prompts**, **money**, and **speed**.

- **Official Definition:** A **token** is the smallest text unit the model processes — a word, subword, punctuation mark, or space chunk mapped to a numeric ID.
- **In Simple Words:** The model's **alphabet** is not A–Z — it is ~50k–100k numbered pieces of language.
- **Real-Life Example:** A **prepaid mobile plan** charges per **MB**, not per "photo you sent." LLM APIs charge per **token**, not per sentence you typed.

![Subword pieces mapped to IDs — variable-length text turned into a fixed-vocabulary stream the model can process](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-06-tokens-lego-blocks.png)

### When One Word Is Not One Token

In class we used **"unbelievable"** as the anchor example — one English word, but **three tokens** when split into reusable subword pieces (`un`, `believ`, `able`). Different models tokenise differently, but the design lesson is the same.

| What you type | Token reality | Design impact |
|---|---|---|
| Plain English sentence | Often ~1 token per word | Easy to underestimate long chats |
| JSON, code, URLs | Symbols split heavily | API payloads cost more than they look |
| Long rare words | Split into subword pieces | Token count can exceed word count |

- **Rule of thumb (planning only):** ~1 token ≈ 0.75 English words, or ~4 characters. **Always measure** before shipping — thumb rules fail on code and long technical terms.
- **Common doubt:** *"If Gemini accepts 1M tokens, why worry?"* — Larger windows reduce **overflow** but still charge **per token processed**. Cost and latency scale with size.

### Measuring Tokens for Real Prompts

Use **tiktoken** (OpenAI-compatible counting) or your provider's **usage dashboard**. Count **every layer** of a production prompt:

1. **System prompt** — persona, scope, workflow
2. **Few-shot examples** — each demo input + output
3. **Retrieved documents** — FAQ chunks, policy excerpts
4. **Conversation history** — prior user + assistant turns
5. **Current user message**
6. **Reserved space for the reply** — never use 100% of the window for input

In the live session, **tiktoken** was introduced as the Python package for programmatic counting. In day-to-day work, platforms like **Groq** also show **input** and **output** token counts on every API call — you do not have to count manually for every demo.

```python
# pip install tiktoken
# token_audit.py — measure a full prompt stack and estimate cost

import tiktoken  # Library for counting tokens the way many chat models do

PRICE_PER_1M_INPUT_TOKENS = 0.50   # Example USD rate — replace with your provider's price
PRICE_PER_1M_OUTPUT_TOKENS = 1.50  # Output is often priced higher than input

encoding = tiktoken.get_encoding("cl100k_base")  # Vocabulary table used by many GPT-style models

system_prompt = """
You are Meera, a campus library FAQ assistant.
Scope: timings, issue rules, fines only. Refuse off-topic politely.
Reply in under 120 words with one next-step suggestion.
"""  # Background rules sent once per conversation

few_shot_block = """
Example 1
User: What is the fine for a late book?
Assistant: Late fine is Rs 5 per day after the due date. Return the book at the front desk.

Example 2
User: Can I eat inside the reading hall?
Assistant: Food is not allowed in the reading hall. Use the cafeteria on the ground floor.
"""  # Two demonstrations that teach answer format

faq_context = """
Library hours: Mon–Sat 8 AM–8 PM, Sun 10 AM–4 PM.
Max books per student: 3. Loan period: 14 days.
"""  # Grounding text pasted from your knowledge base

user_question = "I lost my library card — what should I do?"  # Live question this turn

history = [
    ("user", "Is the library open on Sunday?"),
    ("assistant", "Yes, Sunday hours are 10 AM to 4 PM."),
]  # Prior turns that still sit in the chat window

def count_tokens(text):  # Helper to count tokens in any string
    return len(encoding.encode(text))  # Encode text to ID list; length = token count

def build_full_prompt(system, examples, context, history_pairs, question):  # Stack all layers
    history_text = ""  # Start with empty history string
    for role, message in history_pairs:  # Loop over each past turn
        history_text += f"{role.upper()}: {message}\n"  # Add role label and text
    full = f"SYSTEM:\n{system}\n\nEXAMPLES:\n{examples}\n\nCONTEXT:\n{context}\n\nHISTORY:\n{history_text}\n\nUSER:\n{question}"  # Join every layer
    return full  # Return one string representing the full prompt sent to the API

full_prompt = build_full_prompt(system_prompt, few_shot_block, faq_context, history, user_question)  # Build the stacked prompt

system_tokens = count_tokens(system_prompt)  # Tokens used by system rules alone
examples_tokens = count_tokens(few_shot_block)  # Tokens used by few-shot demos
context_tokens = count_tokens(faq_context)  # Tokens used by grounding text
history_tokens = count_tokens("\n".join(f"{r}: {m}" for r, m in history))  # Tokens from chat history
user_tokens = count_tokens(user_question)  # Tokens in the current question
total_input_tokens = count_tokens(full_prompt)  # Total tokens the model reads this call

estimated_output_tokens = 150  # Guess for the reply — adjust from your app's max length setting
total_billable_tokens = total_input_tokens + estimated_output_tokens  # Input plus output for one call

input_cost = (total_input_tokens / 1_000_000) * PRICE_PER_1M_INPUT_TOKENS  # Cost for reading the prompt
output_cost = (estimated_output_tokens / 1_000_000) * PRICE_PER_1M_OUTPUT_TOKENS  # Cost for generating the reply
total_cost = input_cost + output_cost  # Combined cost for one user message

print("--- Token breakdown ---")  # Header for the report
print(f"System prompt:     {system_tokens} tokens")  # Show system layer size
print(f"Few-shot examples: {examples_tokens} tokens")  # Show example layer size
print(f"FAQ context:       {context_tokens} tokens")  # Show grounding layer size
print(f"Chat history:      {history_tokens} tokens")  # Show history layer size
print(f"User question:     {user_tokens} tokens")  # Show current question size
print(f"TOTAL input:       {total_input_tokens} tokens")  # Sum of all input layers
print(f"Estimated output:  {estimated_output_tokens} tokens")  # Space for the reply
print(f"Estimated cost:    ${total_cost:.6f} per message")  # Dollar estimate for one turn
```

**How the code works:**

- `build_full_prompt` mirrors how a real app stacks **system + examples + context + history + user** before each API call.
- The breakdown prints which layer eats the most tokens — usually **history** or **pasted documents**, not the user question.
- `PRICE_PER_1M_*` are placeholders — copy live rates from your provider's pricing page (in class we walked through **OpenAI's pricing table** as a reference).
- Multiplying by daily active users × messages per day turns a tiny per-message cost into a **product budget**.

### Billing, Latency, and Length Trade-offs

Three forces pull in different directions when you design LLM features.

| Force | What increases it | What you feel |
|---|---|---|
| **Billing** | More input tokens + longer outputs | Higher monthly API bill |
| **Latency** | More tokens to read and write | Slower "typing" response for users |
| **Quality / safety** | Rich system prompt, few-shot demos, grounding context | Better format and fewer hallucinations — but heavier prompt |

- **Billing logic:** Most providers charge **input tokens** (everything you send) and **output tokens** (everything the model generates) separately. Output is often **priced higher**.
- **Latency logic:** The model processes your prompt **before** writing the first word of the answer. A 20,000-token prompt feels slower than a 500-token prompt — even for the same question.
- **Length trade-off:** A **long system prompt** with ten few-shot examples may produce perfect JSON — but leaves little room for **chat history** and **user documents**. Design is **budget allocation**, not "more prompt = always better."

In class we linked this back to **prompt engineering**: more **few-shot** examples, longer **chain-of-thought** instructions, and richer **system prompts** improve quality — but each extra word is **input tokens** you pay for on **every API call**. That is the **cost-benefit balance** you must judge as a designer.

| Design choice | Saves tokens | Risk |
|---|---|---|
| Shorter system prompt | Yes | Model drifts off scope |
| Fewer few-shot examples (0–2) | Yes | Format inconsistency |
| Summarise old chat turns | Yes | Loses fine detail from early conversation |
| Retrieve 2 FAQ chunks instead of 10 | Yes | May miss the right fact |
| Cap `max_tokens` on replies | Yes (output bill) | Answers cut mid-sentence |

### Monitoring Tokens on the Groq Platform

The live session used **Groq** for Python API calls. Every `client.chat.completions.create` request gets a **request ID** and appears in the Groq **Usage → Activity** dashboard.

| What you can see | Why it matters |
|---|---|
| **Input tokens** per call | How big your system + user stack really is |
| **Output tokens** per call | How long the model's reply was |
| **Latency** per call | How long users wait — can vary even for similar token counts |
| **Request ID** | Trace which code cell or user action caused a spike |

- **Real classroom example:** After just two demos (medical-notes extraction and meeting summarization), the class account had already used **~4,500 tokens** — a reminder that costs add up fast across many students and sessions.
- **Enterprise angle:** Production teams monitor the same metrics to answer *"Why did this request take 4× longer?"* or *"Who is burning tokens?"*

### Practice — Token Audit for a Product Prompt

Pick one prompt you wrote in the **previous** session (FAQ bot, study helper, or tagline generator). Paste it into the audit script above — or use an online tokenizer.

1. Count tokens for the **system prompt alone**.
2. Add **two few-shot examples** — recount total.
3. Estimate cost for **1,000 users × 5 messages/day** at your provider's rate.

**Your notes:** Write one sentence on which layer you would trim first if the bill doubled — and what user experience you would sacrifice.

---

## Zero-Shot Prompting in Python (Groq API Recap)

Before diving into token internals, the session ported your **previous prompt-engineering demos** from the browser into **raw Python** using the **Groq** client.

- **Official Definition:** A **zero-shot prompt** gives the model a task instruction with **no worked examples** — the model relies on patterns from training plus your system and user messages.
- **In Simple Words:** You state the job once; you do not show sample Q&A pairs first.
- **Real-Life Example:** Telling a new intern *"Summarise this meeting note in three bullets"* without handing them three finished summaries to copy.

**Setup pattern used in class:**

1. Store your API key in **Colab Secrets** as `GROQ_API_KEY` (never paste keys into notebook cells).
2. Install and import the Groq client.
3. Call `client.chat.completions.create` with `model`, `messages` (system + user roles), and optional parameters.

```python
# pip install groq
# zero_shot_demo.py — same pattern as prior prompt demos, now in Python

import os  # Read secrets from the environment
from groq import Groq  # Groq Python client

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Connect using your Colab secret

system_message = "You are an assistant to hospital administration. Extract age, gender, diagnosis, weight, and smoking status as JSON. Do not invent missing fields."  # Stable rules in system slot

user_message = "Patient: 45-year-old male, 72 kg, mild pneumonia, current smoker. Discharged after 3 days."  # Changing input each turn

response = client.chat.completions.create(  # One API request → one response
    model="llama-3.3-70b-versatile",  # Model hosted on Groq
    messages=[  # Chat roles the API expects
        {"role": "system", "content": system_message},  # Pinned instructions
        {"role": "user", "content": user_message},  # Live task for this call
    ],
)

print(response.choices[0].message.content)  # Assistant reply text
```

**How the code works:**

- `messages` is a list of role/content pairs — same **system vs user** split you practised in the browser.
- Each `create` call is a **fresh request** with its own **request ID** and token usage in the Groq dashboard.
- This template stays the same when you add **`max_tokens`** and **`temperature`** later in the session.

---

## Context Window Limits — Designing What Fits

**Tokens** are the currency. The **context window** is the **wallet size** — everything must fit in one API call.

- **Official Definition:** The **context window** is the maximum number of tokens an LLM can process in **one request** — your full input **plus** the model's generated output.
- **In Simple Words:** A fixed-size **tiffin box**. System rules, examples, history, documents, and the reply **share the same box**.
- **Real-Life Example:** A **NEET aspirant** can only reference the **last 10 pages** of their notebook during a timed test. Facts from page 1 are unreachable — not because they forgot studying, but because the **window** is full.

![A long document with only a sliding bright window visible — tokens outside the frame are invisible to the model on that API call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-07-context-window-viewport.png)

| Model tier (examples) | Advertised window | Practical note |
|---|---|---|
| Smaller / older chat models | 4k–8k tokens | Tight for agents with history |
| Mainstream chat models (e.g. OpenAI GPT) | 128k–256k tokens | Comfortable for most FAQ bots |
| Long-context flagship models (e.g. Gemini, Claude) | 200k–1M+ tokens | Still billed per token; latency rises |

- **Usable context < advertised max:** Reserve **500–2,000 tokens** for the reply and **200+ tokens** for formatting overhead.
- **Common mistake:** Treating "1M context" as "paste anything for free." You **can** attach large files — but you **pay** and **wait** for every token read.

### File Attachments and Chat History Eat the Same Window

In **Gemini**, when you attach files or images plus type a question, the **entire bundle** counts as input toward the context window. A **years-long WhatsApp export** (.txt) can reach **millions of tokens** — far beyond even a 1M window.

**Class exercise (try after the session):**

1. Export a long WhatsApp chat to a `.txt` file.
2. Upload it to **Gemini** (or another long-context chat UI).
3. Ask a question about an **early** message in the thread.
4. Observe whether the model saw the full file or only a **truncated portion**.

### How the Window Shapes System Prompt Choices

Your **system prompt** is the permanent rulebook. It competes with everything else for space.

| System prompt habit | Token cost | When it is worth it |
|---|---|---|
| Short persona + scope (6–10 lines) | Low | Simple FAQ, single-task bots |
| Numbered CoT workflow (10–15 lines) | Medium | Multi-step reasoning tasks |
| Long legal disclaimers + 5 examples in system | High | Rarely — move examples to few-shot user block or trim |

- **Design rule:** Put **stable rules** in the system slot — persona, scope, refusal lines, output format.
- **Design rule:** Keep the system prompt **as short as clarity allows**. Every line there is **paid on every turn** and **cannot be dropped** without code changes.
- **Common error:** Duplicating the same instructions in system **and** first user message — wastes tokens and still drops when history overflows.

### How the Window Shapes Few-Shot Example Choices

**Few-shot** examples teach format by demonstration. Each example is **input tokens you pay every call**.

| Few-shot strategy | Token impact | Best for |
|---|---|---|
| **Zero-shot** (no examples) | Lowest | Common tasks with strong system rules |
| **2 compact examples** | Moderate | Custom JSON keys, brand tone, labels |
| **5+ long examples** | High | Diminishing returns; often pushes out history |

- **Two strong examples beat ten weak ones** — the model copies **pattern**, not **volume**.
- **Cost reminder from class:** Every extra few-shot line and every chain-of-thought step from your **previous prompt work** adds **input tokens** and **latency** — quality improves, but the window and bill shrink.

### How the Window Shapes Conversation History Choices

In a live chat product, **history grows every turn**. Something must give.

| History strategy | How it works | Trade-off |
|---|---|---|
| **Full history** | Send every prior turn | Simple; breaks on long chats |
| **Last N turns** | Keep only recent messages | Fast; may forget early facts user mentioned |
| **Rolling summary** | Replace old turns with a short summary | Saves tokens; summary may lose nuance |
| **Sliding window + pinned system** | System fixed; history trimmed from middle | Industry standard for support bots |

- **What drops first (typical API behaviour):** Oldest messages — including early **user instructions** buried in turn 1, not in the system slot.
- **Product design implication:** Never rely on turn-1 user messages for **critical rules**. Put them in the **system prompt** so they stay pinned.

### Practice — Context Budget for a Support Bot

Assume an **8,192-token** model. Allocate tokens across:

- System prompt: **350 tokens**
- Two few-shot examples: **280 tokens**
- Retrieved FAQ chunk: **600 tokens**
- Reply reserve: **800 tokens**
- Safety buffer: **200 tokens**

1. Calculate **remaining budget for chat history**.
2. If each turn averages **120 tokens** (user + assistant), how many full turns fit?
3. What user-visible symptom appears when turn 31 arrives?

**Your notes:** Write whether you would use **last-N turns**, a **summary**, or a **shorter system prompt** — and justify in one line.

---

## Temperature, Determinism, and Sampling

Even with identical prompts, LLMs can produce **different words** each run. **Temperature** controls how adventurous the model is when picking the next token.

- **Official Definition:** **Temperature** is a sampling parameter (usually 0.0–2.0) that scales randomness when the model chooses each next token. **Lower** values favour high-probability (predictable) choices; **higher** values allow lower-probability (surprising) choices.
- **In Simple Words:** A **spice dial** on chai — low heat gives the same taste every time; high heat changes the flavour batch to batch.
- **Real-Life Example:** A **DMV clerk** reading a fixed script (temperature ≈ 0) vs a **poet** at a mushaira improvising metaphors (temperature ≈ 1).

| Temperature | Behaviour | Good for |
|---|---|---|
| **0.0 – 0.2** | Nearly deterministic; same prompt → very similar output | JSON extraction, fee amounts, classification labels |
| **0.3 – 0.7** | Balanced; small wording changes | FAQ answers, email drafts, support replies |
| **0.8 – 1.2+** | Creative; more variation run to run | Taglines, story ideas, brainstorming |
| **> 1.5** | Often chaotic or messy | Rarely useful in production products |

- **ChatGPT / Gemini default:** Consumer chat apps often run around **0.6–0.7** — enough variety to feel conversational, not so high that every reply is wild. You do not see this slider in the UI, but it is set server-side.

### How Temperature Works — Next-Token Intuition

Language models **predict the next token** from a probability distribution over the vocabulary. **Temperature** reshapes that distribution:

- **High temperature:** More tokens get similar probability — the model may pick surprising words; each rerun can look quite different.
- **Low / zero temperature:** The highest-probability token wins almost every time — near-identical answers on repeat runs.

Behind the scenes, providers apply a **softmax** function over logits; temperature scales those scores before sampling. You do not need the math to design well — you need the intuition: **low = consistent, high = creative**.

### Creativity vs Consistency When Testing Prompts

When you **A/B test** prompt variants, uncontrolled randomness hides whether a wording change helped.

| Testing goal | Temperature setting | How many runs |
|---|---|---|
| Compare **JSON field names** | 0.0 | 1–3 runs |
| Compare **tone** (formal vs friendly) | 0.3–0.5 | 3 runs each variant |
| Compare **creative taglines** | 0.8–1.0 | 5 runs; pick best manually |
| Debug a **buggy prompt** | 0.0 | 1 run — check structure, not luck |

- **Common mistake:** Declaring "Prompt B is better" after **one** run at temperature 0.9 — luck, not design.
- **Better workflow:** Lock temperature low → fix **structure and grounding** → raise temperature only for **creative** layers.

### Configuring `max_tokens` and Temperature in Python (Groq API)

The live demo used a **Razer gaming-laptop marketing assistant** — system message sets the role, user message carries laptop specs, and prompt parameters control output length and creativity.

```python
# pip install groq
# temperature_max_tokens_demo.py — marketing copy with capped output and temperature control

import os  # Environment variables for secrets
from groq import Groq  # Groq client library

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Authenticate with your API key

system_message = "You are an assistant to the marketing team for the gaming company Razer. Help create advertising content for the company."  # Persona and scope

user_message = """
Laptop specs: Intel i9, 32GB RAM, RTX 4080, 240Hz display, 1.2kg chassis.
Write a short marketing blurb highlighting performance and portability.
"""  # Product details for this turn

response = client.chat.completions.create(  # Send one chat completion request
    model="llama-3.3-70b-versatile",  # Model name from Groq docs
    messages=[  # Standard chat message list
        {"role": "system", "content": system_message},  # System rules
        {"role": "user", "content": user_message},  # User input
    ],
    temperature=1.0,  # High — expect different wording each rerun
    max_tokens=1000,  # Cap completion length — controls bill and rambling
)

print(response.choices[0].message.content)  # Print generated marketing copy
```

**How the code works:**

- `max_tokens` (or `max_completion_tokens` on some APIs) limits **output tokens** — without it, the model could generate a very long (expensive) reply.
- `temperature=1.0` in class produced **visibly different** marketing copy each time the same cell was rerun — different adjectives, bullet formatting, and emphasis.
- Re-run with `temperature=0.0` — outputs become **near-identical** across runs; ideal when you are testing **structure**, not creative flair.
- Pair **low temperature** with a tight **`max_tokens`** cap for routing, JSON keys, and classification tasks.

### Practice — Prompt Variant Test with Controlled Temperature

Take a **JSON extraction** or **single-label classification** prompt from your earlier work.

1. Set **temperature to 0.0** in your Groq Python script.
2. Run the **same user input five times** — record whether field names and values match.
3. Raise temperature to **0.7** and repeat five times.
4. Note the first run where format **breaks** (extra sentence, wrong key name, invented field).

**Your notes:** One sentence — for your product, is **consistency** or **creativity** more important? Set a default temperature and write it in your prompt design doc.

---

## When Context Overflows — What Users Actually See

Truncation is often **silent**. The model does not show a red error banner — it simply **cannot read** what fell off the edge.

- **Official Definition:** **Context truncation** occurs when the combined input exceeds the model's window and **early or middle portions** of the prompt are dropped or compressed before generation.
- **In Simple Words:** Pages **ripped out** of the middle of your notebook — the model answers from whatever pages remain.
- **Real-Life Example:** A **WhatsApp group** where only the last 50 messages load on a new phone — you miss the pin that said "Venue changed to Hall B."

In class we called this **context overflow** or **forced truncation**. Uploading a **multi-year chat export** that exceeds Gemini's window is the clearest demo: the model may answer from **recent** messages while **early years** of the chat never entered the window.

### Symptom 1 — Forgotten Instructions

| What the user sees | Likely cause | Design fix |
|---|---|---|
| Bot answers off-topic after a long chat | System rules or scope **truncated** | Shorten system prompt; pin rules in system slot; trim history |
| Bot ignores "do not quote prices" | Rule was in **turn 2 user message**, not system | Move constraints to **system prompt** |
| Bot switches language mid-chat | Language rule dropped from early context | Repeat critical rule in system; lower history length |

- **User quote:** *"It worked fine for ten minutes, then it became useless."* — Classic **history overflow**, not model "getting tired."

### Symptom 2 — Inconsistent Tone

| What the user sees | Likely cause | Design fix |
|---|---|---|
| Formal tone, then casual slang | Few-shot examples or tone rules **pushed out** | Keep tone rules in compact **system** block |
| Brand voice drifts in long threads | Old style demos no longer in window | Reduce history; add one-line tone reminder in system |
| Answers get longer and rambling | No `max_tokens`; model fills available space | Set output cap; restate length limit in system |

- **Temperature interaction:** High temperature **plus** missing tone rules feels like a **different character** — fix **context** first, then tune temperature.

### Symptom 3 — Sudden Factual Drift

| What the user sees | Likely cause | Design fix |
|---|---|---|
| Correct FAQ answer, then wrong fee amount | **Retrieved FAQ chunk** rotated out; model guesses | Re-retrieve relevant chunk each turn; grounding rule in system |
| Invents policy details late in chat | **Hallucination** when grounding text truncated | Shorten history; refresh context; refuse when unsure |
| Contradicts itself from earlier in thread | Model sees **partial** history after trim | Summarise with verified facts only; show sources in UI |

- **Grounding rule reminder:** *"Answer only from provided context; say 'I don't have that information' otherwise."* — Works only if the **context still contains** the FAQ text.

### Practice — Failure Story Analysis

Read this support chat scenario. Identify **which symptom** appears and **one design fix**.

> A student uses a campus bot for 40 minutes. Early turns correctly refuse medical advice. After turn 35, the bot suggests a home remedy for fever. The system prompt still says "no medical advice" in your codebase — but users see violations.

1. Name the likely internal cause (**truncation**, **temperature**, or **both**).
2. Propose one change to **history handling** and one to **system prompt placement**.
3. Would **temperature 0** alone fix this? Write yes or no with one reason.

**Your notes:** Silent truncation is a **product bug**, not a user error — design monitoring before users lose trust.

---

## Putting It Together — Designer Checklist

Before shipping any LLM feature, walk this list. Each item maps directly to a section above.

| Check | Question to answer | Tool |
|---|---|---|
| **Token audit** | What does one message cost in tokens and rupees/dollars? | `tiktoken` or provider dashboard |
| **Layer breakdown** | Which layer is largest — system, examples, history, or docs? | Token audit script |
| **Window fit** | Does stack fit with reply reserve + buffer? | Manual layer tally |
| **History policy** | Last N turns, summary, or new chat button? | Product spec |
| **Temperature default** | Low for structure, higher only for creative modes? | API `temperature` parameter |
| **Output cap** | Is `max_tokens` set to prevent runaway completions? | API `max_tokens` parameter |
| **Overflow UX** | What does the user see before silent failure? | Warning banner, fresh session |
| **Grounding refresh** | Is FAQ/context re-sent or re-retrieved each turn? | Agent architecture |

### Capstone Practice — Internals-Aware Prompt Package

Revise one prompt package from your earlier work with internals in mind:

1. Run a **token breakdown** — list five layers with counts.
2. Confirm the stack **fits** your target model with **800-token reply reserve**.
3. Set **temperature 0.0** and run **three identical tests** — confirm format stability.
4. Write **two sentences** describing what users will see if they chat for **50 turns** without a reset.

---

## Key Takeaways

- **Tokens ≠ words** — measure every prompt layer; **billing**, **latency**, and **context fit** all scale with token count, especially for code, URLs, and subword splits.
- The **context window** is a shared budget — **system prompts**, **few-shot examples**, **retrieved docs**, and **chat history** compete; trim history before dropping scope rules.
- **Groq dashboards** show **input/output tokens**, **latency**, and **request IDs** — use them to debug cost and speed, not only code.
- **Temperature** trades **creativity for consistency** — use **low values** (0.0–0.3) for structured outputs and **controlled higher values** only when variation is desired; pair with **`max_tokens`** to cap cost.
- **Context overflow** causes **silent failures** — forgotten instructions, tone drift, and factual slips in long chats; fix with **system-slot rules**, **history limits**, **context refresh**, and **user-facing reset** flows.

In upcoming work you will connect these internals to **API integrations and agent workflows**, where token budgets and sampling settings become **code-level defaults** rather than playground experiments.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / Tool | What It Means |
|---|---|
| **Token** | Smallest text unit the model processes — billed and limited by APIs |
| **Tokenizer** | Tool that splits text into tokens (e.g. `tiktoken`, provider dashboards) |
| **tiktoken** | Python library for counting tokens with OpenAI-compatible encodings |
| **`cl100k_base`** | Common encoding name used by many modern chat models for counting |
| **Context window** | Max tokens per API call — input (all layers) + output (reply) combined |
| **Usable context** | Advertised window minus reply reserve and safety buffer |
| **Input tokens** | Tokens you send — system, examples, history, documents, user message |
| **Output tokens** | Tokens the model generates — often priced higher than input |
| **Truncation** | Silent dropping of early/middle prompt text when over window limit |
| **Context overflow** | Input exceeds window; model processes only what fits |
| **Temperature** | Sampling parameter controlling randomness (0 = steady, 1+ = creative) |
| **Determinism** | Same prompt producing the same output — approached with temp ≈ 0 |
| **`max_tokens`** | API cap on generated length — controls cost and rambling |
| **Few-shot cost** | Every example token is paid on **every** API call — budget accordingly |
| **History trimming** | Keeping last N turns or a summary to stay inside the context window |
| **Grounding refresh** | Re-sending or re-retrieving source text each turn so facts stay visible |
| **Groq** | Hosted API used in class for open models (e.g. Llama 3.3 70B) |
| **`GROQ_API_KEY`** | Environment variable / Colab secret holding your Groq API key |
| **Request ID** | Unique ID per API call — trace usage in Groq Activity logs |
| **Latency** | Response delay — grows with total tokens read and written |
| **Token audit** | Measuring each prompt layer before shipping a feature |
| **Overflow symptom** | User-visible failure from truncation — scope loss, tone drift, wrong facts |
| **Softmax** | Math that turns model scores into probabilities; temperature scales it |
