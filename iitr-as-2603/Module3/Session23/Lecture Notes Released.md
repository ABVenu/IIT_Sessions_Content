# GenAI Concepts for Beginners

## Context of This Session

In the previous session, you closed the classical Machine Learning chapter with a practical workshop. You built **metric tables** to compare models side by side, judged **complexity** and **overfitting**, **saved and loaded** trained models with **joblib**, and walked through a **selection checklist** to pick the right algorithm for a real problem.

Every model you trained in that journey — regression, classification, clustering, time series — shared one trait: they expected **structured, tabular data** with fixed numeric columns. Rows in, prediction out. None of them could draft an email, translate a sentence, or hold a natural conversation.

This session opens the **Generative AI** world. You will build accurate mental models of how **Large Language Models (LLMs)** behave, where they shine, and where they fail — without any neural-network mathematics.

**In this session, you will:**

- Explain what an **LLM** is and how **token-based text generation** differs from **rule-based software**
- Define **tokens** and **context windows**, and predict when a prompt will exceed usable space
- Describe **hallucinations** and other common **failure modes** in plain language with examples
- Relate **GenAI capabilities** to the **ML ideas you already know** — patterns, training, and evaluation

---

## From Classical ML to Generative AI

Classical ML and GenAI both **learn from data** and **make predictions**. The input and output shapes are what change.

| Idea you already know (Classical ML) | GenAI version |
|---|---|
| Train on labelled rows | Train on massive text from books, websites, code |
| Predict a number or category | Predict the **next piece of text** |
| Features = numeric columns | **Tokens** = numbered chunks of text |
| Evaluate with MAE, F1, RMSE | Evaluate with usefulness, safety, grounding checks |
| One model per task (often) | One big model handles many language tasks |

- **Official Definition:** **Generative AI (GenAI)** refers to AI systems that **create new content** — text, images, code — rather than only classifying or scoring existing data.
- **In Simple Words:** Classical ML often answers *"Is this spam?"* GenAI answers *"Write a polite reply to this customer."*
- **Real-Life Example:** A **spam filter** (classical ML) puts mail in Inbox or Junk. **ChatGPT** (GenAI) writes the reply itself — new sentences every time.

The bridge is simple: ML taught you that models **find patterns in data**. LLMs found patterns in **human language** at a scale no decision tree or logistic regression could touch. You do not need matrix calculus to use them well — you need the right **mental model**.

---

## Rule-Based Software vs Token-Based LLMs

Before ChatGPT, most "smart" text tools were **rule-based** — engineers wrote explicit instructions.

**Rule-based software:**

- **Official Definition:** Programs that follow **fixed, human-written rules** — `if` conditions, keyword lists, regular expressions — to process input and produce output.
- **In Simple Words:** A flowchart frozen in code. Same input → same path → same output.
- **Real-Life Example:** An **IVR phone menu** — *"Press 1 for billing, Press 2 for support."* It never improvises.

**Token-based LLM:**

- **Official Definition:** A model that converts text into **tokens**, then generates output **one token at a time** by predicting what text is most likely to come next.
- **In Simple Words:** A very powerful **autocomplete** that read a huge slice of the internet during training.
- **Real-Life Example:** Your phone keyboard suggesting the next word — except the LLM version has read millions of documents and can finish entire paragraphs.

![Structured tabular ML grids versus free-form natural language — the same limitation that blocks email generation or chat from classical models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-01-tabular-vs-language.png)

| | Rule-based chatbot | LLM |
|---|---|---|
| **How it decides** | Keyword match, regex, decision tree of rules | Statistical next-token prediction |
| **New phrasing** | Often breaks | Usually handles |
| **Same question twice** | Identical answer | May vary |
| **Makes up facts?** | Only if programmer hard-coded wrong data | Can **hallucinate** plausible-sounding false facts |
| **Best for** | Narrow, predictable tasks (OTP flow, menu routing) | Open-ended language (summaries, drafting, Q&A) |

- **When rules win:** **OTP authentication** is a good rule-based job — send a code, user types it back, done. No creativity needed.
- **When LLMs win:** Summaries, email drafts, and open-ended Q&A where phrasing varies every time.
- **Common mistake:** Expecting an LLM to behave like a **database lookup** — it generates text, it does not fetch a stored answer row.
- **Common doubt:** *"If rules are predictable, why not always use rules?"* — Because human language has infinite phrasing. Rules scale poorly; pattern-based generation scales better.

### Quick Activity — Spot the Rule Break

Read these customer messages. A rule *"if message contains 'refund', route to billing"* fails on which ones?

1. *"I want a refund on order #4421."*
2. *"Please return my money for the damaged item."*
3. *"Can you reverse the charge from last Tuesday?"*

**Your notes:** Only message 1 hits the keyword. Messages 2 and 3 mean the same thing with different words — exactly where rule-based systems stumble and LLMs tend to cope better.

---

## What Is a Large Language Model?

An **LLM** is the engine behind ChatGPT, Gemini, Claude, and LLaMA.

- **Official Definition:** A **Large Language Model** is a machine-learning model with billions of learned parameters, trained on vast text corpora to **predict and generate** human-like language.
- **In Simple Words:** A program that has read an enormous library and learned how sentences usually flow — then uses that knowledge to continue any text you give it.
- **Real-Life Example:** A **junior copywriter** who has read every newspaper in the country — fast at drafting, but still capable of stating wrong "facts" confidently.

**Core behaviour — Text In → Text Out:**

- You send a **prompt** (your instruction or question).
- The model returns **generated text** (the completion).
- Everything happens through an **API** or chat interface — you do not run the full model on a normal laptop.

- **Prompt:** The input text that steers the model — *"Summarise this in three bullet points."*
- **Completion:** The model's generated response.
- **Model provider:** A company that hosts the model — OpenAI, Google, Anthropic, Meta (LLaMA), Groq, etc.

Unlike your **Random Forest** from the ML workshop, an LLM was not trained on 500 rows of tumour features. It was **pre-trained** once on a huge mix of general text — books, articles, code, forums — by learning to **predict the next token** billions of times. That single training run gives it grammar, facts, styles, and reasoning patterns across many topics.

**Specialised variants:** Providers often take a **base model** and train further on focused data — for example, a **code-specialised** variant (such as Codex-style models) writes better programs than the general chat model because it saw far more source code during extra training.

---

## The Rise of LLMs — A Short History

Understanding *why* LLMs exist helps you respect both their power and their limits. Here is the story in five beats — no math required.

### Beat 1 — Words Need Numbers

Computers only understand numbers. Early breakthrough: represent words as **vectors** (lists of numbers) so similar meanings sit close together — *"king"* and *"queen"* near each other, far from *"bicycle"*.

### Beat 2 — Reading One Word at a Time

**RNNs** (Recurrent Neural Networks) read text left to right, word by word. They worked for short sentences but **forgot** what was said at the start of long paragraphs — like remembering only the last page of a book.

### Beat 3 — The Transformer (2017)

Google's *"Attention Is All You Need"* paper introduced the **Transformer** — it looks at **all words at once** and learns which words matter for each other. *"The trophy did not fit in the bag because **it** was too large"* — attention links **it** to **trophy**, not **bag**.

![Every token considered together with weighted attention links — how Transformers relate distant words without reading strictly left-to-right](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-04-transformer-attention.png)

### Beat 4 — Pre-training at Internet Scale

**GPT** (Generative Pre-trained Transformer) trained on enormous text with one simple job: **guess the next token**. No manual labels for every task. After that, a smaller **fine-tuning** step adapts the model to helpful chat behaviour.

### Beat 5 — ChatGPT (2022)

When ChatGPT launched, anyone could type plain English and get fluent answers. That cultural moment is why **agentic systems** — bots that plan, use tools, and act — are now mainstream. The rest of this course builds on that foundation.

![From Word2Vec and RNNs to the 2017 Transformer, GPT-style pre-training, and the ChatGPT moment — the stack of ideas that produced modern LLMs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-05-llm-evolution-timeline.png)

- **Key shift from classical ML:** One expensive general training run replaces training a **separate model per task**.
- **Common doubt:** *"Did ChatGPT browse the web while I type?"* — Not by default. It generates from patterns learned during training plus whatever you put in the prompt.

---

## Tokens — How LLMs Read Text

LLMs do not see **words** on screen. They see **tokens**.

- **Official Definition:** A **token** is the smallest unit of text an LLM processes — a whole word, part of a word, punctuation, or whitespace chunk.
- **In Simple Words:** Lego bricks of language. *"unhappiness"* might become `["un", "happi", "ness"]`; *"cat"* might be one brick.
- **Real-Life Example:** A **ration shop** weighs rice in kilograms, not handfuls. APIs bill and limit by **tokens**, not by what looks like one word to you.

![Subword pieces mapped to IDs — variable-length text turned into a fixed-vocabulary stream the model can multiply and add over](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-06-tokens-lego-blocks.png)

**Why tokenisation exists:**

- Computers need numbers → a **tokenizer** splits text into tokens → maps each token to an ID from a fixed **vocabulary** (~50k–100k entries).
- **Subword tokenisation** keeps rare words splittable without a dictionary of every word on earth.

| What you type | Token reality |
|---|---|
| Short English sentence | Often ~1 token per word, not always |
| Long URL or JSON | Many tokens — symbols split heavily |
| Hindi + English mix | Token count often **higher** than word count |
| Indian languages in native script | Often **2–3×** more tokens than equivalent English — affects **cost** |

**Rule of thumb (planning only):** ~1 token ≈ 0.75 English words, or ~4 characters. Always **measure** for production; rules of thumb are for quick estimates.

### Counting Tokens in Python

```python
# Install once in terminal: pip install tiktoken

import tiktoken  # OpenAI-compatible token counting library

# Load an encoding used by many modern chat models
encoding = tiktoken.get_encoding("cl100k_base")  # Load the subword vocabulary table

# Three sample texts to compare token counts
english_sentence = "The quick brown fox jumps over the lazy dog."  # Simple English line
hindi_english_mix = "Kal main office jaake meeting attend karunga."  # Hinglish-style sentence
long_url = "https://example.com/products?id=4421&ref=campaign_summer_2026"  # URL with symbols

samples = {  # Dictionary of label → text for looping
    "English": english_sentence,  # First sample text
    "Hinglish mix": hindi_english_mix,  # Second sample text
    "Long URL": long_url  # Third sample text — usually many tokens
}

for label, text in samples.items():  # Loop over each sample
    token_ids = encoding.encode(text)  # Convert text to list of token ID numbers
    tokens_as_text = [encoding.decode([t]) for t in token_ids]  # Show each token piece
    print(f"\n--- {label} ---")  # Print a header for this sample
    print("Token count:", len(token_ids))  # Print how many tokens this text uses
    print("Tokens:", tokens_as_text)  # Print how the sentence was split
```

**How the code works:**

- `tiktoken.get_encoding("cl100k_base")` loads a vocabulary table shared by many GPT-style models.
- `encoding.encode(text)` turns characters into a list of integer token IDs.
- `encoding.decode([t])` shows each token as readable text — notice spaces and punctuation are their own pieces.
- Comparing **English vs Hinglish vs URL** makes cost and context impact tangible.

### Quick Activity — Estimate Before You Measure

For each item, **guess** the token count, then run the code above (or an online tokenizer) to check.

1. A 10-word English email opening line
2. The same meaning written in Hindi (Devanagari script)
3. A pasted 2-page PDF paragraph (~800 words)

**Your notes:** Indian-language content often costs more per meaning. Long documents explode token counts — never paste a full report blindly into a prompt.

---

## Context Windows — The Model's Working Memory

**Tokens** and **context windows** work together. The window is the hard ceiling.

- **Official Definition:** The **context window** is the maximum number of tokens an LLM can process in **one API call** — your prompt **plus** the model's generated answer must both fit.
- **In Simple Words:** A fixed-size **tiffin box**. Instructions, chat history, PDF chunks, and the reply all share the same box. When it is full, something is left out.
- **Real-Life Example:** You can only read the **last 10 pages** of a 200-page book before answering a question. If the answer was on page 3, you will miss it — that is **context overflow**.

![A long document with only a sliding bright window visible — tokens outside the frame are invisible to the model on that API call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-07-context-window-viewport.png)

| Model (examples) | Context window | Rough pages |
|---|---|---|
| GPT-3.5 (early) | 4,096 tokens | ~3 pages |
| GPT-4o | 128,000 tokens | ~100 pages |
| Claude 3.5 | 200,000 tokens | ~150 pages |
| Gemini 1.5 Pro | 1,000,000 tokens | ~750 pages |

- **Usable context** is less than the advertised max — reserve space for the **answer** (often 500–2,000 tokens) and for **system instructions**.
- When content exceeds the window, earlier text is **truncated** or **dropped** — the model does not always warn you loudly.
- **Common mistake:** Stuffing an entire policy manual into one prompt instead of retrieving only relevant sections later.
- **Practical tip from class:** Avoid uploading one huge **500-page PDF** in a single shot. Split the document, upload smaller sections, and ask **targeted questions** — otherwise you hit the window ceiling and answers degrade.
- **Design takeaway:** A **bigger context window** helps, but **retrieving only the right sections** (you will build this pattern later) often matters more than pasting everything at once.

### Predicting When a Prompt Will Exceed Context

```python
# pip install tiktoken  (if not already installed)

import tiktoken  # Token counting library

MODEL_CONTEXT_LIMIT = 4096  # Example: smaller model window size in tokens
RESERVED_FOR_REPLY = 600  # Tokens to leave empty for the model's answer
SAFETY_BUFFER = 200  # Extra buffer for system message and formatting overhead

def check_context_fit(prompt_text, model_limit=MODEL_CONTEXT_LIMIT):  # Define checker function
    encoding = tiktoken.get_encoding("cl100k_base")  # Same encoding as before
    input_tokens = len(encoding.encode(prompt_text))  # Count tokens in your prompt only
    usable_limit = model_limit - RESERVED_FOR_REPLY - SAFETY_BUFFER  # Space left for input
    fits = input_tokens <= usable_limit  # True if prompt fits with room for reply
    overflow = max(0, input_tokens - usable_limit)  # How many tokens over the safe limit
    return {  # Return a small report dictionary
        "input_tokens": input_tokens,  # Tokens your prompt consumes
        "usable_limit": usable_limit,  # Safe maximum for input text
        "fits": fits,  # Whether you are within safe limits
        "overflow_tokens": overflow  # How far past the limit (0 if fits)
    }

# Example: a long pasted document (~5000 words ≈ ~6667 tokens by rule of thumb)
long_chapter = "word " * 5000  # Placeholder — replace with real chapter text in practice

report = check_context_fit(long_chapter)  # Run the check on the long text

print("Input tokens:", report["input_tokens"])  # Show measured token count
print("Usable limit:", report["usable_limit"])  # Show safe input ceiling
print("Fits safely:", report["fits"])  # True or False
if not report["fits"]:  # Only print warning when over limit
    print("Overflow by:", report["overflow_tokens"], "tokens")  # How much to trim or split
```

**How the code works:**

- `MODEL_CONTEXT_LIMIT` is the model's advertised window — check your provider's docs.
- `RESERVED_FOR_REPLY` and `SAFETY_BUFFER` stop you from using 100% of the window for input.
- `encoding.encode(prompt_text)` gives an exact token count — better than guessing from word count.
- `overflow_tokens` tells you how much to cut, chunk, or retrieve separately.

### Quick Activity — Context Budget Estimation

Work through these scenarios with pen and paper first, then verify with the checker code.

1. **WhatsApp thread:** 200 short messages averaging 15 words each → estimate tokens. Does it fit in 4,096?
2. **PDF report:** 50 pages × ~300 words/page → estimate tokens. Does it fit in 128k?
3. **Agent design sketch:** System prompt (400 tokens) + last 10 chat turns (2,500 tokens) + tool log (1,800 tokens) + user question (50 tokens) → total? What gets dropped first if you are over limit?

**Your notes:** In future agent builds, **history + instructions + tool output** compete for the same window. Trimming verbose logs is a design skill, not an afterthought.

---

## How LLMs Generate Text — Prediction, Not Retrieval

This is the mental-model shift that explains both the magic and the risk.

- **Official Definition:** **Probabilistic text generation** means the model produces output **one token at a time**, each time choosing a likely next token given everything before it.
- **In Simple Words:** It does not look up an answer in a filing cabinet. It **writes forward**, word by word, like autocomplete on a global scale.
- **Real-Life Example:** Keyboard suggestions after *"Happy birth…"* almost always offer *"day"*. The LLM does the same — but with far richer context.

![Fluent, confident wording is not a guarantee of truth — models optimise for plausible next tokens, not a verified facts database](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-09-hallucination-fluent-not-true.png)

- The model does **not** look up answers in a stored table — it **writes forward** token by token, like a powerful autocomplete.
- The **same question twice** can produce **different answers** because each step is probabilistic, not a fixed rule path.
- **Common doubt:** *"If grammar is rule-based, how can an LLM fix grammar?"* — It learned well-formed sentences from millions of books during training. It predicts **likely** structure, not a grammar rulebook. Tools like **Grammarly** can still flag errors in LLM-generated text.
- **Common mistake:** Treating a confident tone as proof of correctness — the model is optimised to sound right, not to be right.

---

## When LLMs Fail — Hallucinations and Other Failure Modes

LLMs are powerful and **unsafe to trust blindly**. Know the main failure modes so you design around them. Chat apps now show disclaimers similar to mutual-fund ads — *returns subject to market risk* — because fluent text is **not** a guarantee of truth.

### Hallucinations

- **Official Definition:** A **hallucination** is when an LLM states **false or fabricated information** with **confident, fluent** language.
- **In Simple Words:** The model guesses the next likely token, not the next **true** token. Plausible beats accurate.
- **Real-Life Example:** A **junior copywriter** who read every newspaper — fast at drafting, but can state wrong "facts" confidently because they **believe** what they wrote sounds right.

**Documented case:** In 2023, US lawyers submitted a legal brief with **six fake court cases** generated by ChatGPT. The cases did not exist; the lawyers were fined.

- **Why it happens:** Training rewards **fluent continuation**, not fact-checking. There is no built-in verification step inside the model.
- **Mitigation preview:** Ground answers in source documents, instruct the model to refuse when unsure, keep humans in the loop for high-stakes actions. You will build these patterns later in the course.

### Other Common Failure Modes

| Failure mode | What goes wrong | Plain example |
|---|---|---|
| **Knowledge cutoff** | Model unaware of events after training date | Wrong answer about a 2025 election result |
| **No live data** | Model cannot see your database or today's news unless you pass it in | Invented stock price unless you attach a feed |
| **Math and counting errors** | Token prediction is not a calculator | Wrong total on a long invoice line-item list |
| **Inconsistency** | Probabilistic sampling changes answers | Two different summaries of the same paragraph |
| **Sycophancy** | Model agrees with a wrong premise in your prompt | *"Why is the earth flat?"* → fabricated "reasons" |
| **Context loss** | Early instructions fall off when the window fills | Bot forgets *"never mention competitors"* mid-chat |
| **Bias from training data** | Stereotypes from web text surface in outputs | Gendered assumptions in career advice |

### Quick Activity — Failure Mode Detective

Label each scenario with the best failure mode from the table above.

1. The model says a product launched in 2024, but your company launched it in 2025.
2. The model gives a different word count every time you ask about the same paragraph.
3. After a 40-message chat, the bot ignores your original *"respond only in Hindi"* instruction.
4. The model adds a refund policy clause that does not exist in the document you pasted.

**Your notes:** (1) Knowledge cutoff or no live data, (2) Inconsistency / probabilistic generation, (3) Context loss, (4) Hallucination. Real systems often need **multiple safeguards** — not one fix.

---

## Key Takeaways

- **Classical ML and GenAI share the pattern-learning idea**, but GenAI operates on **free-form language** and **generates new text** instead of scoring fixed table rows.
- **Rule-based software** follows explicit paths; **LLMs** use **token-by-token prediction** — flexible language, but **not** a truth database.
- **Tokens** drive **cost**, **speed**, and **limits**; **context windows** cap what the model can see in one call — always measure and reserve space for the reply.
- **Probabilistic generation** explains creative outputs, **inconsistency**, and why fluency does not equal accuracy.
- **Hallucinations and related failure modes** are expected risks, not rare bugs — design with grounding, refusal instructions, and human oversight especially when agents take real-world actions.
- **Retrieval and tools** (coming next) help ground answers in real documents instead of imagination alone.

In upcoming sessions you will learn how to **steer** these models with better **prompts**, use **RAG** to ground answers in source documents, and connect **tools** so agents act on real data.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / Tool | What It Means |
|---|---|
| **LLM (Large Language Model)** | A large model trained on vast text to understand and generate language |
| **GenAI** | AI that creates new content (text, images, code) rather than only classifying |
| **Prompt** | The input text/instruction you send to the model |
| **Completion** | The text the model generates in response |
| **Token** | Smallest text unit the model processes (~0.75 English words on average) |
| **Tokenisation** | Splitting text into tokens and mapping them to numeric IDs |
| **Context window** | Maximum tokens (input + output) in one API call |
| **Pre-training** | Large-scale training on general text by predicting next tokens |
| **Transformer** | Architecture that processes all tokens together using attention |
| **Probabilistic generation** | Writing one token at a time by sampling likely continuations |
| **Hallucination** | Confident but false or fabricated model output |
| **RAG (preview)** | Retrieve relevant documents first, then generate — reduces hallucination risk |
| **Fine-tuned / specialised model** | Base LLM trained further on focused data (e.g., code) for one domain |
| **Knowledge cutoff** | Last date of training data — no built-in awareness after that |
| **Rule-based software** | Fixed if/keyword logic — same path every time |
| **API** | Interface your code uses to send prompts and receive completions |
| **tiktoken** | Python library to count and inspect tokens (`pip install tiktoken`) |
| **`cl100k_base`** | Common tiktoken encoding used by many modern chat models |
| **`encoding.encode(text)`** | Returns token ID list for a string |
| **`encoding.decode([id])`** | Turns a token ID back into readable text |
