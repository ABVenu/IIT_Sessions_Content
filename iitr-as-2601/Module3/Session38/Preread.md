# Pre-read: RAG Foundations — Give AI Its Own Library

You finally have a **language model on your own machine** — thanks to **Ollama** from the last session. You can ask questions, run small scripts, and even saw a preview of **embeddings**: turning a sentence into a list of numbers that capture **meaning**.

Now imagine you are on the **student support desk** for a large online programme. A learner messages at midnight: *"What is the late-submission rule for our March 2026 batch?"* The answer lives in **one internal PDF** — not on the public internet. You paste the question into your local AI and get a reply that sounds **professional, polite, and completely wrong**. It might invent a generic university rule because it never read your handbook.

That moment — **confident AI, wrong fact** — is why teams stop treating the model as an all-knowing oracle and start giving it a **library** of their own documents. Today's session is the **big picture** of that idea, before we wire up the full automated system in later classes.

---

## When the smartest student never saw your notes

A **Large Language Model (LLM)** is trained on huge amounts of public text up to a **knowledge cutoff** — a last date in its training memory. When you ask a question, it **predicts** likely words. It does not automatically open your company's PDFs or this morning's notice unless **you put that text in front of it**.

Think of it like a student who read the whole internet until last year. Ask about **your institute's 2026 refund line** and they may **fill the gap** with something that sounds right but was never in your files. That gap-filling is called **hallucination** — fluent text that is still **false**.

Three problems show up again and again:

| Problem | What it means for you |
|---|---|
| **Knowledge cutoff** | New policies and products may not exist in training data |
| **No private data** | Your internal docs were never in training |
| **Hallucination** | The model guesses when it lacks the real page |

**Prompt engineering** helps you *talk* to the model clearly. **RAG** — **Retrieval-Augmented Generation** — helps you *feed* it the right **pages** from your library before it speaks. Search first, then speak.

---

## The open-book exam your company needs

What if every policy question required a human to **hunt through five hundred PDFs** and paste the right paragraph before the AI could answer safely?

What if the model kept sounding authoritative while your **actual rule** sat in a folder it never opened?

What if wrong answers did not stay on a chat screen — they triggered **wrong refunds, wrong emails, or wrong agent actions**?

That is the challenge: you need answers grounded in **your documents**, updated when PDFs change, without retraining the whole model every week.

The pattern we open today is **RAG** — giving the model a **searchable external library** instead of relying only on training memory. In plain terms: **find the right notes, then write the answer from those notes.**

---

## A simple analogy you already know

Picture a **DU photocopy shop** near campus. You need one fact from a thick course pack. The keeper does not recite the whole syllabus from memory. They **pull the right folder** from the shelf (**retrieval**), you **read the page** (**context in the prompt**), then you **explain it in your own words** (**generation**).

Your PDFs are the **books on shelves**. **Embeddings** — those number lists from last session — act like a **catalog sorted by meaning**, not only by title spelling. The **retriever** plays librarian; the **LLM** plays the student explaining after reading. **Grounding** means sticking to the page on an open-book test — not inventing platform 5 at the railway station because it "sounds right."

We will **not** build the full coded RAG app today. We **will** learn the **five-step map** once, compare **one question with and without** your handbook text, and run a **hands-on demo** that turns sentences into **embedding vectors** — the bridge to **vector databases** and full retrieval in upcoming sessions.

---

In this pre-read, you'll discover:

- **Why** an LLM alone is risky for **private or up-to-date** questions — and how a manual "paste the handbook" test proves the idea before automation
- **What** **RAG** means and the **five-step flow**: ingest → prepare → retrieve → augment → generate — at a conceptual level you can reuse in any tool
- **How** the **retriever**, **generator**, and **grounding** work together — including one prompt rule that stops confident guessing when the fact is already in your context
- **How** input text becomes **embeddings** with **Ollama**, and why those numbers lead to **vector search** and a complete **RAG loop** in the sessions ahead

---

## Ideas worth knowing before we go live

- **RAG (Retrieval-Augmented Generation):** Search your knowledge base, pull relevant text, add it to the prompt, then let the LLM generate — **search first, then speak**.
- **External library:** Your PDFs, wikis, and notices **outside** the model's fixed weights — fresh facts without retraining.
- **Five-step pipeline:** **Ingest** documents → **Prepare** (clean, chunk, embed, index) → **Retrieve** best chunks → **Augment** the prompt → **Generate** the answer.
- **Retriever:** Finds evidence from the library. **Generator:** The LLM that writes. **Grounding:** Answer from **supplied context** when the library has the fact.
- **Embedding:** A list of numbers representing **meaning**; similar topics sit **closer** in math space — like a library sorted by subject.
- **Vector database (upcoming):** A specialised store that keeps those vectors and finds the **nearest** ones fast when a user asks a question.
- **RAG vs fine-tuning (one minute):** Fine-tuning **memorises** the book inside the brain; RAG **brings the book** to each exam. Changing PDFs usually starts with **RAG**.

---

## Questions we will tackle in the live session

1. **The honesty test:** You ask about the **March 2026 late-submission rule** with **no extra text**, then again with the **exact handbook line** pasted as context. What changes in the answer — and what part of that process will **RAG automate** so you do not paste by hand every time?

2. **The librarian's job:** When RAG gives a **confident wrong fact**, how do you tell whether the **retriever** picked the wrong page, the **generator** ignored good context, or the **library** itself is outdated?

3. **From numbers to answers:** You run the **embedding demo** on three sentences — two about refunds, one about exams. In one sentence: what would a RAG system **do with those vectors** after storing them — and which step of the five-step map is that?

---

## After this session, you will be able to

- Explain **why LLMs alone** fall short on **organisation-specific** and **up-to-date** questions — **knowledge cutoff**, private data, and **hallucination**
- Describe **RAG** as a **searchable library** pattern and walk through **ingest → prepare → retrieve → augment → generate** without needing a full app yet
- Separate **retriever**, **generator**, and **grounding** — and use a simple **"answer only from context"** instruction in a prompt
- Run the **manual compare**: same question **without** vs **with** handbook context on **Ollama**, and state what RAG will automate later
- Turn text into **embeddings** with **`nomic-embed-text`** and connect that to **vector DBs**, **retrieval**, and the **full RAG loop** in upcoming classes
- Enter the next sessions ready for **vector search** and **building a RAG app** — with the map already in your head

Come with **Ollama running**, the embedding model pulled (`ollama pull nomic-embed-text`), and the Python setup from last week. Today's class is **concepts plus one honest demo** — you will feel the difference between **guessing** and **reading your own page** before we teach the machine to find that page for you.

See you in class. The step from *"the model sounds smart"* to *"the model cites our documents"* is what makes agents trustworthy enough to use on real policies and real customers.
