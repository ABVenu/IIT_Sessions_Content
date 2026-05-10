# Pre-read: GenAI Concepts for Beginners

Think about how you use **English or Hindi typing** on WhatsApp every day — long messages, slang, corrections, jokes, and reminders that rarely sound the same twice. Now think about the models you met in the last module: brilliant at **rows and columns**, at predicting a number or a yes/no label when every input sat neatly in a table.

Almost every job advertisement today mentions **ChatGPT**, **assistants**, or **AI agents** that read and write like humans. Employers are no longer impressed only by “I can fit data into a spreadsheet model.” They are asking who can safely use tools that handle **conversation, drafts, translation, and open-ended answers**. That gap between “tabular thinking” and “language-ready thinking” is exactly where Module 3 begins.

---

## What If Every Customer Phrased the Same Complaint Ten Different Ways?

Picture a busy support queue. One person writes, *“I need my refund.”* Another says, *“I’d like my money back.”* A third taps, *“This order never arrived — what happens next financially?”*

If you forced this into classical machine learning style, you would need **fixed columns**: word counts, flags, rigid rules. Words like **“bank”** would be one label in a column whether the sentence was about a **riverside bank** or a **money bank** — the model cannot “listen” to the rest of the sentence the way your brain does. Rule-based tricks (keywords, patterns) work until someone **changes the wording**; then everything breaks.

**What if** you needed software not just to classify a ticket, but to **compose a polite reply**, **summarise a long note**, or **keep track of meaning across a whole chat**? The tools from Module 2 were never built for that world. Something else had to emerge — models that treat **sequences of meaning**, not just numbers in cells.

---

## The Story We Open — From Layered Patterns to Words That Flow

Meet **Large Language Models (LLMs)**. Under the hood sit **neural networks** — many thin “thinking steps” stacked instead of one. Think of **recognising someone in a photograph**: edges and patches first, then eyes or a nose, then the whole face, then “that is my cousin.” Each stage hands a **cleaner snapshot** onward. Models do something similar once text becomes numbers — from early tricks with word lists and reading left-to-right to today’s **Transformer** setups that weigh **which words relate to which** even across long gaps.

Heavy maths stays off the agenda. Stay with one mental image: outputs are **built one step at a time**, like turbo-charged **next-word suggestion** — not like a search engine returning the exact same saved page every time.

---

## The Core Picture — Text as Small, Standard Pieces

> **Imagine text built out of Lego bricks.** A brick might be a whole common word, a slice of a long word, a space pattern, even punctuation. Whatever you type gets **snapped into these bricks** so the machine can feed them in and work with them as numbers — that snapping process is what people mean by **tokens**. Just as Lego lets you reuse a small set of pieces to build almost anything large, tokenisation lets a model handle huge vocabulary without storing one giant list of every possible word on Earth.

Then **cost** and **memory** make sense together: clouds often bill per token, and every model carries a **context window** — a cap on how much it “sees” in one shot, **like flipping open only the last dozen pages before an exam.** We will tie this to **working code** and to **Indian languages**, where richer scripts can mean **more tokens for the same idea** — handy when you forecast bills for Bharat-wide launches.

---

## In this pre-read, you'll discover:

- **Why language breaks the “spreadsheet model” of classical ML** — ambiguity, phrasing, and meaning that refuse to sit in fixed columns
- **How neural networks and LLMs fit into one story** — from layered pattern-finding to modern assistants, without drowning in jargon
- **What tokens and context windows actually change for you** when you call an API or design a conversation
- **Why answers can vary, feel creative, or sound wrong-with-confidence** — and what **temperature** and **hallucination** mean in plain terms before you rely on outputs in serious work

---

When people say **“temperature,”** here they simply mean **how adventurous the model feels** when picking the next piece of text — turned down low, it hugs safe, repeatable wording; turned up, it dances more wildly. When they say **“hallucination,”** they mean the model kept going in smooth, fluent language **without a built-in fact checker** — so it can describe things that never happened **as confidently** as something true.

---

## What's Next After the Session

Once we close this first GenAI session together, you should be able to:

- **Explain to a friend or colleague** why your Module 2 models could not “write an email” the way an LLM can, using a clear example of language or ambiguity
- **Speak confidently about tokens and context limits** — and rough-size a prompt so you know when a chunk of text probably will not fit a given model’s window
- **Describe the autocomplete-style behaviour** that makes two runs of the **same prompt** legitimately produce different wording
- **Name when to dial temperature up or down** for tasks like factual support versus brainstorming
- **Spot the hall-of-mirrors risk** — fluent-but-wrong replies — especially when an **agent** takes real-world actions instead of only showing text on screen

---

## Before the Session — Keep These Alive in Your Mind

We will unpack every one of these ideas live — with demos, sketches, and code you can revisit later.

> **1.** If someone says “I went to the **bank**” with no extra words, why can your brain guess the meaning from a fuller story — but a single rigid “keyword = feature” trick often fails?

> **2.** You type “Write one line about rain” twice into an assistant **without changing settings**. Should you expect identical wording both times — and why or why not?

> **3.** Rough guess: Does a chunky **technical report in Indian languages** likely cost **more tokens** than the **same gist in tidy English paragraphs** — and what would that mean for **API bills** aimed at Bharat-wide users?

Show up curious. The leap from tidy tables to **talking machines** anchors Agentic Systems — and together we sketch that map in calm language you can reuse at work from day one.

---

*See you in the session — bring your curiosity!*
