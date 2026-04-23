# Pre-read: Introduction to RAG

Imagine you need a clear answer about your own company’s leave policy, last year’s region-wise sales, or a line in a medical report. You would not happily accept a confident guess from someone who has “general knowledge” but has never seen your actual file. You want the answer to line up with **your** facts—and you want to know *which* document it came from.

Picture the same situation for a shop owner checking this week’s revised GST slab, or a student asking about *this year’s* exam circular on the university site. The world changes. Documents update. Private numbers do not live on the public internet. A smooth talker who cannot look things up will sometimes sound right and still be wrong.

**The problem**

What if a helpful assistant could talk fluently about almost anything, but could not truly “open your PDF” or “check today’s notice”? What if it sounded sure even when it was stitching together memory and guesswork? That gap between **smooth language** and **verified truth** is what we tackle.

Many teams discover this the hard way: the model answers like a smart generalist, but it may be outdated, off-policy, or simply inventing a “reasonable-looking” number. In this session we give that problem a name, a picture, and a practical direction.

**The idea we will build toward**

We introduce **Retrieval-Augmented Generation**, or **RAG** for short. In simple terms, RAG means: **first fetch the right material from sources you trust, then write the answer with that material in view.** We call this **grounding**: the reply is tied to evidence you can point to—not only to what the model once memorised during training.

You can think of RAG as adding a “reading step” before the “writing step.” The session topic is the hero that helps answers stay closer to what your organisation actually stores—policies, manuals, tickets, research PDFs, or product docs.

**A simple analogy**

Think of an **open-book exam with a careful librarian**. The exam writer (language + reasoning) is strong at forming sentences. The librarian (retrieval) finds the relevant pages *before* the writer commits to an answer. If the librarian brings the wrong chapter, even a brilliant writer can write a polished mistake—so **retrieval quality matters**.

Another everyday picture: **Google Search + careful note-taking**, but aimed at *your* closed corpus. You are not asking the internet; you are asking *your* knowledge base, and you pass the best snippets to the person who will compose the final reply.

**How an LLM answers (high level, no maths)**

At a high level, a large language model (LLM) predicts the **next likely words** based on patterns it learned from huge text it was trained on. It is not “looking up a database” inside its head for each sentence the way a search engine does for every query in real time. That strength makes it flexible—but it also explains why it can drift when facts are niche, private, or freshly updated.

**In plain language**

- **Static knowledge cut-off**: training happened up to a point in time. Anything newer—new circular, new product launch, new law—may be missing unless you bring it in from outside.
- **Domain and privacy gaps**: your internal playbooks, customer tickets, or HR policy PDFs were not necessarily in the training set the way *you* need them quoted.
- **Real-time data**: stock price, weather, today’s outage status—these usually need a fresh fetch from a tool or feed, not a vague memory of “typical” numbers.
- **Hallucination**: the model fabricates or misstates facts when evidence is thin; it can read as confident prose. It is a behaviour risk, not a moral choice—often a symptom of missing or weak grounding.
- **Grounding**: tying claims to **retrieved** text or structured facts so the answer can be checked against a source span. Grounding does not magically remove all errors, but it moves you from “pure guessing” toward “answer with receipts.”
- **RAG (high level)**: **your question → retrieve relevant chunks → pass them as context → generate an answer** that leans on those chunks. Bad retrieval in; weak answer out—so we will later care about chunking, indexing, and evaluation.
- **Vector search (the one-minute version)**: documents and questions get represented in a way where “similar meaning” sits closer than “similar spelling.” That helps find the right paragraph even when the user’s wording differs from the manual’s wording.
- **LLM-only vs RAG-style (conceptual)**: *LLM-only* answers from broad pretrained knowledge; *RAG-based* answers are written **after** pulling likely evidence from **your** store. Same writer, different inputs.

**Where RAG shows up (so it feels real)**

- **Enterprise knowledge assistants**: “What is our travel reimbursement rule for international trips?” pulled from the internal policy hub.
- **Document-based Q&A**: long PDFs, contracts, or research papers where users ask in normal language.
- **Domain-specific chat**: legal, medical, finance support systems where answers must lean on curated sources—not random forum gossip.

**RAG inside agentic thinking**

Agents often need to **act**—file a ticket, draft an email, pick a next step. Retrieval helps them **read before they jump**: fetch past similar incidents, pull the runbook paragraph, check the latest SOP. When retrieval is careless, the agent’s plan looks smart but starts from the wrong facts—so we repeatedly return to one theme: **better retrieval, more reliable behaviour.**

**Questions we will answer in the live session**

- Why can a fluent LLM still be wrong about *your* world, and what does “hallucination” look like when a team audits answers against real documents?
- How does RAG change the story when we compare **pure model knowledge** with **retrieval-first** answers on the same question?
- How does **vector search** connect to “find the right passage,” and where does **grounding** show up in the pipeline?
- How do **agents** use retrieval as a step before decisions, and why is “retrieval quality” a product problem—not only a model problem?

**After this session, you should be able to**

- Explain, in simple terms, how LLMs generate text via next-token patterns and why pretrained knowledge has **limits** (time, domain, privacy, freshness).
- Name concrete limitations: static cut-off, lack of organisation-specific context, no automatic access to private or live data unless wired in.
- Define **hallucination** as incorrect or invented content that can appear fluent, and connect it to **missing or weak evidence**.
- State why **grounded** systems aim to rely on **external, verifiable** material for accuracy-sensitive answers.
- Describe **RAG** as retrieval plus generationx, and narrate the flow: **query → retrieve → context → generate**.
- Contrast **LLM-only** versus **RAG-style** responses using a plain example (e.g. generic HR advice vs policy-backed wording from *your* handbook).
- Connect **vector search** to “semantic” retrieval for RAG at a high level—without getting lost in equations.
- List realistic use cases: **enterprise knowledge assistants**, **document question answering**, and **domain-specific chat**.
- Relate RAG to **agentic systems**: retrieval as a knowledge step before action, and why improving retrieval improves **trust and outcomes**.