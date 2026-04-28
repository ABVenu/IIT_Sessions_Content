# Pre-read: RAG Architecture and Pipeline

Imagine you are the smartest assistant at a company. Your boss walks up and asks, "What was the revenue figure from last quarter's report?" Now, you have two options. Option one — you try to recall everything you have ever read and guess the answer from memory. Option two — you quickly open the company's filing cabinet, pull out the exact report, read the relevant paragraph, and give a precise answer.

Which assistant would you trust more?

This is exactly the problem that AI systems face today — and it is a much bigger challenge than it sounds.

---

## The Problem with "Memory-Only" AI

Most of us have used AI chatbots and been impressed. But if you ask that same AI about something very recent — say, a news event from last week, or a policy document your company released yesterday — it will either confidently give you the wrong answer or admit it does not know.

Why? Because that AI only knows what it was trained on. Its "knowledge" is frozen at a certain point in time, like a textbook that was printed two years ago. It cannot look things up. It cannot access your files. It simply repeats what it memorised during training.

Now imagine you are building an AI assistant for a hospital. Doctors need accurate, up-to-date information from medical databases. An AI that "makes up" answers based on old training data is not just unhelpful — it is dangerous.

This is the core limitation: **AI systems trained on fixed data cannot reliably answer questions about specific, current, or private information.**

So how do we fix this?

---

## Meet the Solution: RAG

The answer is a design approach called **RAG — Retrieval-Augmented Generation**. Do not let the technical name intimidate you. The idea behind it is surprisingly simple, and once you hear the analogy, you will never forget it.

Think of RAG as giving the AI a **"cheat sheet system."** Instead of relying purely on what the AI memorised during training, RAG allows the AI to first *go and search* for relevant information from a trusted source, and then use that information to construct its answer.

It is like the difference between a student who writes an exam purely from memory versus a student in an open-book exam who can reference the correct chapters before answering. The open-book student will almost always give a more accurate, reliable answer.

That is RAG in a nutshell — **Retrieve first, then Generate.**

---

## How the Pipeline Actually Works

A RAG system has three key players working together like a well-coordinated team.

**The Knowledge Source** is the filing cabinet. It is the collection of documents, PDFs, databases, articles, or any information that the AI should be able to refer to. This could be your company's internal wiki, a set of research papers, or even a product catalogue. The knowledge source is where the *truth* lives.

**The Retriever** is the research assistant. When a user asks a question, the Retriever does not read the entire filing cabinet — that would take forever. Instead, it quickly scans and finds the most relevant pieces of information related to the question. Think of it like a very fast librarian who knows exactly which shelf to go to.

**The Generator** is the writer. Once the Retriever hands over the relevant information, the Generator reads it and crafts a clear, natural-sounding answer. The Generator is typically a Large Language Model (LLM) — the same kind of AI behind chatbots — but now instead of relying on memory alone, it has actual reference material in front of it.

These three components — Knowledge Source, Retriever, and Generator — work in a pipeline. A pipeline simply means they work in a sequence, one passing its output to the next, like an assembly line in a factory.

---

## Why This Matters for You

If you are building any kind of AI-powered product — a customer support bot, a legal document analyser, a medical assistant, an internal company tool — RAG is the foundational architecture you will need to understand.

Without RAG, your AI is essentially guessing. With RAG, your AI becomes a **reliable, source-backed responder** that can handle real-world, up-to-date, and domain-specific questions.

This is not a niche research topic. It is one of the most widely used patterns in production AI systems today.

---

## In this pre-read, you'll discover:

- Why AI systems built on training data alone have a critical limitation when dealing with specific or current information
- What RAG (Retrieval-Augmented Generation) is and the simple idea behind how it works
- The three core components of a RAG pipeline — knowledge sources, retriever, and generator — and what role each plays
- How these components connect to form a working pipeline that makes AI far more accurate and trustworthy

---

## After This Session, You Will Be Able To:

- Explain what RAG is to anyone, in plain and simple language
- Describe the three components of a RAG pipeline and how they interact
- Identify situations where RAG would be the right architectural choice for an AI product
- Think about AI system design not just as "plug in an LLM" but as a structured pipeline with distinct, purposeful components

---

## Questions to Think About Before the Session

Here are a few things to sit with before the live lecture. Do not worry about having the answers — these are exactly the questions the session will crack open.

1. If the Retriever fetches the wrong documents from the knowledge source, what happens to the final answer? And how would you even know the answer was wrong?

2. What if two documents in your knowledge source contradict each other — which one does the system trust, and how does it decide?

3. RAG makes AI more accurate — but does adding a Retrieval step make it slower? How would you design around that in a real product where users expect instant responses?

Come with your curiosity. The session is going to be a hands-on walkthrough of this entire pipeline — and by the end, you will see exactly how these three pieces click together to build something genuinely powerful.
