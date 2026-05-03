# Pre-read: Building a RAG Pipeline

## Have You Ever Wished a Customer Support Bot Actually Knew the Answer?

Picture this: you ordered a phone online, it arrived damaged, and now you need to know — **can you return it? How many days do you have? Do you get a full refund or a store credit?**

You open the company's chat support. The bot says: *"I'm sorry, I don't have information about that."*

Infuriating, right?

Now flip the situation. You are the one building that bot for a company. The company hands you four big documents — a returns policy, a shipping policy, a warranty document, and a refund guide. Together they have hundreds of pages. Your task: make the bot read all of them and answer any customer question, instantly and correctly.

How would you even begin?

---

## The Challenge That Seems Impossible at First

Imagine you have to manually read through 400 pages of policy documents every time a customer asks *"How long does it take to get my refund?"*

That's not realistic. And even if you tried, you'd end up reading the whole document just to find two sentences that answer the question.

Now imagine doing this for 10,000 customers a day.

A human customer support team cannot scale like this. You need a system — one that reads documents once, remembers the important parts, and instantly finds the right answer whenever someone asks a question.

**What if a computer could do all of this for you, automatically?**

That's exactly the problem we are solving in this session.

---

## The Hero of This Session: A Real RAG Pipeline

In the last session, you got your first look at a RAG system — a Retrieval-Augmented Generation system. You saw how it combines a **retriever** (that finds relevant information) with a **generator** (that writes the answer).

But we were working with toy-sized examples — a handful of handwritten policy sentences.

In this session, we **go real**. We will work with actual documents — PDFs, text files, and more. We will build a complete, step-by-step pipeline that:

- **Loads** the documents from your computer
- **Cleans and organizes** the content
- **Splits** large documents into small, searchable pieces
- **Converts** those pieces into a form the computer can search through
- **Retrieves** the right piece when a customer asks a question
- **Generates** a clear, grounded answer

By the end of the session, you will have built a working customer support assistant for a fictional company called **ShopEasy** — one that can answer questions across four different policy documents, all at once.

---

## Think of It Like a Well-Organised Library

Here is an analogy that makes the whole thing click.

Imagine you walk into a library and ask: *"Where can I find information about returning a product?"*

A librarian doesn't read every single book to answer you. Instead, they:
1. Know which shelves hold which books
2. Use the index to jump to the right chapter
3. Hand you exactly the page you need

A RAG pipeline does the same thing — but for documents on your computer.

- **Document Loaders** are like the people who bring new books into the library and place them on the right shelf.
- **Chunking** is like dividing each book into chapters and adding an index.
- **Embeddings** are like giving every chapter a unique label that captures its meaning.
- **The Vector Database** is the organised shelf system — it stores everything so the librarian can find it instantly.
- **The Retriever** is the librarian — it finds the right chapter when a question arrives.
- **The LLM** is the expert reader — it reads what the librarian brings and writes a clear answer.

Every piece has a job. Together, they form a pipeline that is faster, smarter, and more reliable than any human support team working alone.

---

## In This Pre-read, You'll Discover:

- **Understand** why real-world documents need special handling before an AI can search through them
- **Discover** what "chunking" means and why cutting documents into small pieces makes search dramatically more accurate
- **Learn** how a computer turns text into numbers — and why that's the secret to fast, meaningful search
- **Understand** how all these steps connect into one flowing pipeline, from raw document to final customer answer

---

## A Few Concepts to Know Before You Walk In

**Document Loader** — Think of it as a scanner for your files. You give it a PDF or a text file, and it reads everything inside and hands it to your program in a neat, usable format. Different formats (PDF, `.txt`, web pages) need different types of scanners.

**Chunking** — When a document is too long to process at once, we break it into smaller pieces called *chunks*. Each chunk is like one paragraph or section. The system searches through chunks instead of the whole document — which makes it much faster and more accurate.

**Chunk Overlap** — When we split a document into chunks, we deliberately repeat a small part at the end of one chunk at the start of the next. Why? Because important information often sits right at the cut point. The overlap acts as a safety net so nothing meaningful is lost.

**Embedding** — This is where things get interesting. A computer cannot understand words the way you do. So we convert each chunk of text into a list of numbers that captures its meaning. Two chunks about similar topics will produce similar sets of numbers — and that's how the system knows they are related.

**Vector Database** — This is the storage room for all those number-lists (vectors). It's built for one purpose: finding the numbers that are closest to your query's numbers. This is how the retriever finds relevant chunks in milliseconds.

**Prompt Template** — Before the AI writes an answer, we give it structured instructions: *"Here are the relevant policy sections. Here is the customer's question. Now answer using only what's in these sections."* A prompt template is the fill-in-the-blank form that organises all of this before it reaches the AI.

---

## Get Curious — Questions We'll Answer Live

Before you join the session, sit with these questions for a moment. They don't have easy, obvious answers — and that's exactly what makes the session worth attending.

> **1. If you split a document into very small chunks — say, just 5 words each — what goes wrong?**
>
> And if your chunks are too large — say, the entire document in one piece — what problem does that create? Is there a "sweet spot"? How would you find it?

> **2. What happens when a policy document gets updated?**
>
> Say ShopEasy changes their return window from 30 days to 45 days. Your AI assistant was trained on the old document. How do you update it — without rebuilding the entire system from scratch? Is a partial update safe, or does it create new problems?

> **3. When a customer asks a vague question like "Tell me everything about returns" — how does the retriever decide which chunks to bring back?**
>
> It can only return a limited number. What if the most important chunk doesn't make the cut? What would you change to make the system more reliable?

---

These questions will come alive the moment you see the code running. You'll watch the pipeline load documents, split them, search through them, and generate an answer — step by step.

**Don't miss it.**
