# Introduction to RAG

## Context of the Session

In the previous session, we built a small end-to-end vector search pipeline. We learned how to convert text into **embeddings**, store those embeddings inside a **vector database** like Chroma, run a **similarity search** using a user query, and retrieve the **top-k** most relevant results with basic metadata filtering.

That gave us a useful piece of machinery: given any question, we can now find the most relevant chunks of text from a knowledge base. But finding the right chunks is only half the job — a student still wants a clean, natural answer, not a list of document snippets.

This is where today's session comes in. We will study **Retrieval-Augmented Generation (RAG)**, which takes the retrieval part we already built and plugs it into a **Large Language Model (LLM)** so the model can answer using real, trusted information instead of only its own memory.

**In this session you will learn:**

- How an LLM actually generates a response, and why it sometimes gets things wrong.
- The main limitations of LLM knowledge — **static knowledge**, **no domain context**, and **no real-time data**.
- What **hallucination** means and why it is dangerous.
- What **grounding** means and why AI systems need it.
- The full definition and **high-level flow** of **RAG**: *query → retrieve → context → generate*.
- The difference between an **LLM-only** answer and a **RAG-based** answer.
- How **vector search** powers retrieval inside RAG.
- Real-world use cases of RAG — **enterprise knowledge assistants**, **document Q&A**, and **domain-specific chatbots**.
- How RAG fits inside **agentic systems** and why **retrieval quality** decides the final answer quality.

---

## How an LLM Generates a Response

Before we can understand *why* we need RAG, we must first understand *how* a plain LLM answers a question. This sets up the problem that RAG is designed to solve.

- **Official Definition:** A **Large Language Model (LLM)** is a deep learning model trained on very large text data that predicts the most likely next word (token) given a prompt.
- **In Simple Words:** An LLM is like a very well-read person who has read lakhs of books and web pages in the past, and now speaks only from memory.
- **Real-Life Example:** Think of a senior uncle at a family function who has read every newspaper for 20 years. If you ask him a general question, he answers confidently from memory — but he has not read *today's* newspaper.

**What actually happens when a user sends a query:**

- The LLM receives three things: the **trained knowledge** inside its parameters, the **current prompt** you typed, and the **conversation history**.
- It does **not** open Google, check your company PDF, or read a database by default — unless a system is specifically built to do that.
- It simply predicts the most likely next words, one after another, until a full response is formed.
- That is why it can answer "What is Java?" very well — "Java is an object-oriented programming language used for backend and Android development" is common knowledge the model has seen many times.
- **Common doubt:** Students often believe ChatGPT is "searching the internet live." By default, it is not — it is speaking from memory.

LLMs are genuinely very strong at **language generation**, **summarization**, **paraphrasing**, **explanation**, and **general question answering**. But this memory-only way of working hits a wall the moment the question depends on *fresh* or *private* information, which brings us to the next topic.

---

## Limitations of LLM Knowledge

LLMs are powerful, but their memory has three important limitations. These three limits are the exact reason RAG exists, so we will go through them one by one.

### Limitation 1: Static Knowledge

- **Official Definition:** **Static knowledge** means the model's internal information is fixed at the time of training (the **knowledge cutoff**) and does not update automatically.
- **In Simple Words:** The model "stopped reading" on a certain date, so anything that changed after that date is unknown to it.
- **Real-Life Example:** It is like a college textbook printed in 2022. If the syllabus changed in 2024, the book is still showing the 2022 version.

**Why this matters in real projects:**

- A company policy may have changed last week — the model will not know.
- Stock prices, product catalogs, medical guidelines, and government rules keep changing.
- Example: Suppose a company changed its leave policy from **15 days to 20 days** last week. A plain LLM may still answer with the old "15 days" because that is what it saw during training.

### Limitation 2: Lack of Domain-Specific Context

- **Official Definition:** **Domain-specific context** is private or specialized information (company documents, internal wikis, product manuals) that was never part of the model's public training data.
- **In Simple Words:** The LLM does not know *your* company's rules, *your* project's code, or *your* college's grading policy.
- **Real-Life Example:** A new employee on day one is very smart in general, but has no idea where the coffee machine is, who approves leaves, or what the reimbursement limit is — because that information lives only inside the company.

- A general-purpose LLM cannot answer questions based on your HR handbook, your support manuals, or your internal architecture docs — unless that content is given to it.
- Example: If a student asks, *"What are the grading rules in our institute?"*, the LLM cannot answer correctly unless someone retrieves those rules and puts them in the prompt.

### Limitation 3: No Built-in Access to External or Real-Time Data

- **Official Definition:** An LLM by default has **no tool access** — it cannot call APIs, search engines, or databases to fetch live data unless a system is wired around it.
- **In Simple Words:** The model cannot "look things up" on its own. It only speaks from what it already remembers.
- **Real-Life Example:** Like a very smart friend without a phone — he can discuss cricket history for hours, but cannot tell you today's live IPL score.

This means a plain LLM will usually fail on questions like:

- "What is the *current* refund policy?"
- "What is the *latest* version of our API?"
- "Which document mentions Project Falcon?"
- "What was *today's* ticket count?"

And here is the dangerous part — even when the model does not know, it often still answers **confidently**. That behaviour has a name, and that is our next topic.

---

## Hallucination in LLMs

When an LLM is forced to answer a question it does not actually know, it often "fills the gap" using its language skills. The output sounds fluent and correct, but the content is invented.

- **Official Definition:** **Hallucination** is when an LLM generates information that is incorrect, fabricated, unsupported, or misleading, while presenting it as a confident factual answer.
- **In Simple Words:** The model is making things up, but saying it in a very sure, professional tone.
- **Real-Life Example:** Like a student in an oral exam who does not know the answer but still speaks fluently for one minute — the delivery is great, but the facts are wrong.

**Why hallucination happens:**

- The model does **not** actually know the answer.
- The **prompt** does not provide enough information.
- The model tries to fill the gap using **language patterns** it has learned (it knows what a "policy-style answer" *looks* like, so it writes something that looks like a policy).

**Example 1 — Fake policy numbers**

A user asks: *"What does our company's 2026 reimbursement policy say about certification courses?"*

If the LLM has never seen that document, it may still answer:

> "Employees are eligible for up to ₹50,000 per year for certification reimbursements."

It sounds professional, but the number may be completely made up.

**Example 2 — Fake summary of a PDF**

A student uploads a PDF and asks: *"What does page 12 conclude?"*

If the system is not actually reading page 12, the model may invent a confident-sounding summary that has nothing to do with the real page.

**The core problem:**

- **Hallucination is dangerous because the answer often *looks* correct even when it is not.**
- Students often ask, *"Can't we just tell it to not hallucinate?"* — Prompting helps a little, but the only real fix is to give the model **real, retrieved information** to work from.

So we cannot depend on LLM memory alone for serious applications. We need AI systems that answer from real, verifiable sources — and this is exactly the idea of **grounding**.

---

## Why We Need Grounded AI Systems

For real-world use cases — HR, healthcare, legal, banking, customer support — "sounding good" is not enough. We need answers that are **accurate**, **verifiable**, and **backed by a source**.

- **Official Definition:** A **grounded AI system** is one whose responses are based on external, verifiable information (documents, databases, trusted sources) rather than only on the model's internal memory.
- **In Simple Words:** The AI first *checks the actual document*, and then answers.
- **Real-Life Example:** Imagine two employees answering "How many casual leaves do I get?". Employee A answers from memory: *"I think around 10."* Employee B first opens the HR policy PDF and then says: *"As per the HR policy section 3.2, you get 8 casual leaves per year."* Employee B is **grounded** — and that is the kind of AI we want.

**A grounded AI should ideally answer using:**

- retrieved **documents**,
- **database** records,
- **company policies** and product manuals,
- **support articles**,
- **medical / legal references**,
- or any **trusted knowledge source**.

That is the exact difference between an LLM-only system and a **RAG** system, which we will now define properly.

---

## What is Retrieval-Augmented Generation (RAG)?

We now have the full motivation: LLMs are powerful but have static, general memory and tend to hallucinate. The fix is to let them *look things up* before answering — and that is RAG.

- **Official Definition:** **Retrieval-Augmented Generation (RAG)** is an approach that combines an **information retrieval** step with a **language generation** step, so that an LLM answers a user's query using external knowledge retrieved at runtime.
- **In Simple Words:** RAG = *first search, then answer*. The LLM first pulls the relevant content from a knowledge base, and only then writes the response using that content.
- **Real-Life Example:** Like a lawyer in court. Before giving an opinion, they first pull out the relevant law book, read the exact clause, and only then argue. The LLM in a RAG system behaves exactly like that lawyer.

**The RAG idea in one line:**

- Instead of answering only from memory, the model answers using **retrieved evidence** plus its own language ability.

### Why RAG is Important

RAG directly solves the limitations we saw earlier. It improves:

- **Accuracy** — answers are based on real documents, not guesses.
- **Relevance** — the response is tied to *your* data, not generic internet knowledge.
- **Trustworthiness** — you can cite the source document/chunk.
- **Domain awareness** — HR, legal, medical, banking content is handled correctly.
- **Explainability** — you can show *which* document the answer came from.

**Small comparison example — "What is the leave encashment policy in our company?"**

- **LLM-only response:** A generic HR-style answer based on what "most companies" do.
- **RAG-based response:** The system retrieves *your* HR policy, finds the "leave encashment" section, and answers using that exact text.

The second answer is the one a real business can actually trust and deploy.

---

## What "Grounding" Means in RAG

The word **grounding** will come up again and again, so it is worth locking down clearly.

- **Official Definition:** **Grounding** in RAG means anchoring the model's response to the actual retrieved content, so that the generation step is guided (and constrained) by real evidence.
- **In Simple Words:** The LLM is not allowed to "invent" the answer — it is told: *"Answer this question using only this retrieved text."*
- **Real-Life Example:** Like open-book exams in college. You must answer using the textbook in front of you, not your own imagination.

**Example:** Suppose a retrieved document says:

> "Employees may carry forward up to **10** unused leave days to the next calendar year."

A grounded response would be:

> "According to the policy document, employees can carry forward up to 10 unused leave days."

That is far more useful than a generic guess like "usually 5 to 15 days."

**Why grounding matters:**

- It **reduces hallucination** because the model has real text to rely on.
- It **improves factual correctness**.
- It makes the response **domain-specific** (matches your org, your product).
- It makes the answer **traceable** — you can point to the source chunk.

To see grounding in action, let us now walk through the actual RAG pipeline step by step.

---

## High-Level Flow of RAG

The core flow of any RAG system has four steps:

**Query → Retrieve → Context → Generate**

### Step 1: User Asks a Query

This is simply the user's question in natural language. For example: *"What is the refund rule for damaged products?"*

### Step 2: System Retrieves Relevant Information

The system searches its **knowledge base** to find the most relevant documents or chunks. The knowledge base can be made of:

- PDFs,
- company documents,
- FAQs,
- database records,
- wiki pages,
- product manuals,
- knowledge base articles.

For the refund query, the retrieval system might pull back this chunk:

> "Damaged products reported within 48 hours of delivery are eligible for replacement or refund after verification."

### Step 3: Retrieved Content is Given to the LLM as Context

The LLM prompt now has two parts:

- the **user's question**, and
- the **retrieved chunk(s)**.

So the model is no longer answering blindly — it has supporting material attached to the prompt.

### Step 4: LLM Generates the Final Answer

The LLM uses the retrieved content to produce a clean, natural-language response:

> "According to the policy, damaged products reported within 48 hours of delivery may qualify for a replacement or refund after verification."

### The Flow in One Diagram

![RAG high-level flow: Query → Retrieve → Context → Generate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session28/lecture-notes-images/session28-rag-four-step-flow.png)

```text
User Query
    ↓
Retrieve relevant documents / chunks (from vector DB or KB)
    ↓
Pass retrieved context + query to LLM
    ↓
LLM generates grounded answer
```

Notice how this flow reuses *everything* we built in the last session — embeddings, vector DB, similarity search — and only adds an LLM at the end. That is a very important connection, and we will come back to it in a minute.

---

## LLM-Only vs RAG-Based Responses

To cement the difference, let us compare both approaches side-by-side.

![LLM-only vs RAG: memory-only answers vs grounded answers with retrieval](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session28/lecture-notes-images/session28-llm-vs-rag.png)

| Aspect                           | LLM-only                      | RAG-based                                      |
| -------------------------------- | ----------------------------- | ---------------------------------------------- |
| Knowledge source                 | Pretrained memory only        | Pretrained memory **+ retrieved external data** |
| Access to latest info            | Usually no (fixed cutoff)     | Yes, if the knowledge base is kept updated     |
| Domain-specific accuracy         | Limited                       | Much better                                    |
| Hallucination risk               | **Higher**                    | **Lower** (but not zero if retrieval is bad)   |
| Traceability / citations         | Weak                          | Stronger — you can point to the source         |
| Usefulness for enterprise data   | Poor to moderate              | High                                           |

**Example — "What is the latest onboarding process for new employees in our company?"**

- **LLM-only answer:** A generic onboarding flow — account creation, document verification, team intro, training. Sounds fine but may not match the company's real process.
- **RAG-based answer:** The system retrieves the latest HR onboarding guide and answers with the actual steps — pre-joining document submission, laptop collection, internal tool setup, manager introduction, mandatory security training, payroll verification.

The RAG answer is **specific**, **grounded**, and **deployable**. Now the natural next question is: *how* does the system actually find the right chunk? That is where vector search (from last session) re-enters the picture.

---

## How RAG Connects to Vector Search Systems

Most modern RAG systems use **vector search** as their retrieval engine. This is the direct bridge from Session 27 to today's topic.

**Why not just use keyword search?**

- Keyword search only matches exact words.
- It fails when the user's wording is different from the document's wording.
- It cannot understand *meaning*, only *letters*.
- Example: If the document says *"remote working is allowed two days per week"* but the user asks *"what is our work from home policy?"*, keyword search may find nothing.

### What is Vector Search (Quick Recap)

- **Official Definition:** **Vector search** converts text into numerical vectors called **embeddings** that capture semantic meaning, and then finds the most similar vectors to a query vector using a similarity metric (e.g. cosine similarity).
- **In Simple Words:** Every sentence is turned into a list of numbers. Sentences with similar *meaning* end up close to each other in that number space.
- **Real-Life Example:** Like organizing a library not by book title, but by *topic similarity*. Two books about "work from home" sit next to each other even if one is titled "Remote Work Policy" and the other is titled "WFH Guidelines."

### Why Vector Search is Useful for RAG

Vector search helps RAG retrieve context that is:

- **semantically relevant**, not just keyword-matched,
- **useful even when wording differs**,
- **ranked by similarity score**, so we can pick top-k.

### The Complete RAG + Vector Search Pipeline

![End-to-end RAG pipeline with chunking, embeddings, vector DB, top-k retrieval, and LLM](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session28/lecture-notes-images/session28-rag-vector-pipeline.png)

```text
Documents
    ↓
Convert into chunks (small readable pieces)
    ↓
Create embeddings for each chunk
    ↓
Store embeddings in a vector database (e.g. Chroma)
    ↓
User query → create query embedding
    ↓
Retrieve top-k similar chunks
    ↓
Pass chunks as context to the LLM
    ↓
LLM generates the grounded answer
```

This is basically the Session 27 pipeline with an LLM bolted on at the end. Now that the full mechanism is clear, let us look at where this is actually used in the real world.

---

## Real-World Use Cases of RAG

RAG shines whenever the correct answer *must* come from a specific, trusted knowledge source rather than general internet knowledge.

### Use Case 1: Enterprise Knowledge Assistants

Most companies have thousands of internal documents spread across tools:

- HR policies,
- engineering documentation,
- architecture notes,
- onboarding guides,
- compliance documents,
- internal FAQs.

Employees spend a lot of time *searching* instead of *working*. A RAG-based enterprise assistant can answer questions like:

- *"What is the reimbursement policy?"*
- *"How do I raise a production access request?"*
- *"Where is the deployment checklist documented?"*
- *"What is the leave carry-forward rule?"*

**Real-Life Example:** Microsoft internally uses an "Ask HR" style assistant that pulls answers from HR policy documents. The employee gets a direct answer with a source link instead of opening ten PDFs.

### Use Case 2: Document-Based Question Answering

Users often need answers from long documents: PDFs, contracts, research papers, invoices, manuals, legal agreements. Reading the whole document is painful.

A RAG system lets them just *ask*:

- *"What is the termination clause?"*
- *"What is the refund condition?"*
- *"What does this report conclude?"*
- *"What are the warranty terms?"*

**Real-Life Example:** A student uploads their lecture notes and asks *"What are the three main benefits of indexing mentioned in the notes?"* The system retrieves the relevant paragraph and answers directly, with the exact quote.

### Use Case 3: Domain-Specific Chat Systems

Some industries cannot afford generic LLM guesses — the answer must be domain-correct.

- **Banking:** "What is the eligibility for a credit card upgrade?" → retrieved from the bank's product policy.
- **Healthcare:** "What is the dosage guideline for this medicine in adults?" → retrieved from a medical reference.
- **Legal:** "What does Section 15 of this contract say about penalties?" → retrieved from the actual contract.
- **E-commerce support:** "Can I return this product after 15 days if it is defective?" → retrieved from the latest return policy.

**Common doubt:** *"Can't we just fine-tune the LLM on this data instead of using RAG?"* Fine-tuning is expensive, slow to update, and does not give you traceability. RAG lets you simply **update the knowledge base** whenever policy changes — no retraining needed.

These use cases already feel powerful, but RAG becomes *even* more important the moment we talk about **AI agents**.

---

## RAG in Agentic Systems

This course is called *Certification in Agentic Systems and Design*, so this connection is the most important one for us.

- **Official Definition:** An **AI agent** is a system that can understand a goal, reason about the steps, use tools and knowledge, and take actions to achieve that goal.
- **In Simple Words:** An agent is an LLM that can *act*, not just *chat*. It can fetch data, call APIs, and decide what to do next.
- **Real-Life Example:** A travel booking agent that takes your goal ("book a cheap flight to Delhi next Friday"), checks live flight data, compares prices, and books — instead of just suggesting what you could do.

### Why Agents Need Retrieval

Agents make **decisions** and take **actions**, often using the classic **Perceive → Reason → Act** loop. If their reasoning is based on stale or hallucinated information, the *action* they take will also be wrong — and actions have real consequences (booking a wrong flight, approving a wrong leave, sending a wrong email).

So agents need retrieval for the same reason a doctor needs a patient file — reasoning without facts is unsafe.

**Example:** A customer support agent receives:

> "Can a customer return a product after 15 days if the product is defective?"

If the agent first **retrieves** the latest return policy, then reasons over it, and only then responds, its decision is reliable. Without retrieval, the agent might confidently approve or deny a return based on a hallucinated rule.

### How RAG Improves Agent Decision-Making

When an agent uses retrieval before acting, it can:

- make **better decisions**,
- **reduce mistakes** and costly wrong actions,
- **justify** its responses with a source,
- **adapt** to domain-specific rules (banking vs healthcare vs e-commerce),
- work with **updated** information even after the LLM's training cutoff.

### The Agentic Flow with Retrieval

![Agent loop with RAG: perceive, retrieve, reason, then act or respond](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session28/lecture-notes-images/session28-agentic-rag-flow.png)

```text
User goal
    ↓
Agent decides it needs information
    ↓
Agent retrieves relevant knowledge (RAG)
    ↓
Agent reasons over the retrieved context
    ↓
Agent responds or takes an action (call API, raise ticket, book, reply, etc.)
```

**Example — Internal IT Helpdesk Agent:**

User: *"How do I request VPN access?"*

1. Agent retrieves the latest IT access SOP from the internal wiki.
2. Agent reasons over the SOP and identifies the exact form and approver.
3. Agent replies with correct steps, or even raises the request ticket directly.

Without retrieval, it might share an outdated process and send the user to the wrong team. This directly brings us to the last — and most practical — point of the session.

---

## Why Retrieval Quality is So Important

A RAG system is only as good as its retrieval. This is the single most important engineering lesson of RAG.

- **Official Definition:** **Retrieval quality** is how accurately the retrieval step returns the most relevant, complete, and up-to-date chunks for a given query.
- **In Simple Words:** If you fetch the wrong paragraph, even the smartest LLM will give the wrong answer.
- **Real-Life Example:** Imagine a lawyer who opens the *wrong* law book in court. It does not matter how well they argue — the argument is based on wrong evidence.

**Core rule of RAG:**

```text
Better retrieval → better context → better response quality
```

**If retrieval returns:** irrelevant chunks, incomplete chunks, outdated chunks, or no useful chunks — then the LLM may answer incorrectly, answer incompletely, **hallucinate**, or produce vague output.

### Example — "What is the approval process for travel reimbursement?"

- **Good retrieval:** The system fetches the latest travel policy and the reimbursement workflow. Result: **accurate, grounded** answer.
- **Poor retrieval:** The system fetches an unrelated finance document or an old version of the policy. Result: **confusing or incorrect** answer — even though the LLM is the same.

### What Affects Retrieval Quality

At a high level, retrieval quality depends on:

- how documents are **chunked** (too big = noisy, too small = missing context),
- how **embeddings** are created (which model, which dimensions),
- how **similarity search** is performed (cosine, dot product, etc.),
- how relevant chunks are **ranked** (top-k, re-ranking),
- whether **metadata filters** are used (department, date, doc type),
- whether the **knowledge base is kept updated**.

You do not need deep technical details for an introductory class — but you *must* internalize this: **retrieval quality directly decides answer quality.**

### Full Walk-Through Example — HR Leave Query

**Scenario:** A company has an HR policy document. The user asks: *"How many casual leaves can employees take in a year?"*

**Without RAG:**

> "Most companies allow 10 to 12 casual leaves per year."

This is a **generic guess** — may be wrong for *this* company.

**With RAG:**

- **Step 1 — Query:** User asks the question.
- **Step 2 — Retrieval:** The system searches the HR policy and retrieves this chunk: *"Full-time employees are entitled to 8 casual leave days per calendar year."*
- **Step 3 — Context to LLM:** The retrieved chunk is attached to the prompt.
- **Step 4 — Generation:** The LLM replies: *"According to the HR policy, full-time employees are entitled to 8 casual leave days per calendar year."*

This final answer is **specific**, **grounded**, and **reliable** — that is exactly the promise of RAG.

---

## Key Takeaways

- **LLMs answer from memory by default**, so they suffer from **static knowledge**, **no domain context**, **no live data**, and the risk of **hallucination**.
- **Grounding** means anchoring the answer to real external evidence — and **RAG (Retrieval-Augmented Generation)** is the standard way to do this: *query → retrieve → context → generate*.
- **Vector search** (from Session 27) is the engine that powers retrieval inside most RAG systems — it finds semantically similar chunks, not just keyword matches.
- RAG unlocks powerful real-world applications: **enterprise knowledge assistants**, **document Q&A**, and **domain-specific chatbots** in banking, healthcare, legal, and support.
- In **agentic systems**, RAG is what lets agents reason and act on **trusted, current information** instead of hallucinated memory — and the final answer quality is ultimately decided by **retrieval quality**.

In the upcoming sessions we will go one level deeper — we will study **chunking strategies**, **advanced retrieval techniques**, **prompt design for RAG**, and finally build a **complete RAG-powered agent** end-to-end.

---

## Important Commands, Libraries, and Terminologies

| Term / Tool                   | Category       | Meaning in Simple Words                                                                                  |
| ----------------------------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| **LLM**                       | Concept        | Large Language Model — a model that predicts the next word and generates natural text.                   |
| **Prompt**                    | Concept        | The input text (question + any context) sent to the LLM.                                                 |
| **Knowledge Cutoff**          | Concept        | The last date up to which the LLM saw training data; anything after that is unknown.                     |
| **Static Knowledge**          | Concept        | The LLM's fixed memory that does not auto-update.                                                        |
| **Hallucination**             | Concept        | A confident but fabricated/incorrect answer from an LLM.                                                 |
| **Grounding**                 | Concept        | Anchoring the LLM's answer in real, retrieved evidence.                                                  |
| **RAG**                       | Concept        | Retrieval-Augmented Generation — *retrieve first, then generate*.                                        |
| **Retrieval**                 | Pipeline step  | The step that fetches the most relevant chunks for a query.                                              |
| **Generation**                | Pipeline step  | The step where the LLM writes the final natural-language answer.                                         |
| **Context Window**            | Concept        | The amount of text the LLM can read at once (question + retrieved chunks + history).                     |
| **Knowledge Base (KB)**       | Concept        | The collection of documents/chunks the RAG system can search through.                                    |
| **Chunk / Chunking**          | Technique      | Splitting a long document into small readable pieces so retrieval can match them precisely.              |
| **Embedding**                 | Concept        | A numeric vector that captures the semantic meaning of a text chunk.                                     |
| **Vector Database**           | Tool type      | A database built to store embeddings and run fast similarity search (e.g. **Chroma**, Pinecone, FAISS).  |
| **Similarity Search**         | Technique      | Finding vectors closest in meaning to the query vector (e.g. using cosine similarity).                   |
| **Top-K Retrieval**           | Technique      | Returning the K most similar chunks for a query (typically K = 3 to 10).                                 |
| **Metadata Filter**           | Technique      | Narrowing search with tags like department, date, doc type before/after similarity search.              |
| **Citation / Traceability**   | Concept        | Pointing back to the exact document or chunk that produced an answer.                                    |
| **AI Agent**                  | Concept        | An LLM-based system that reasons, uses tools, and takes actions to achieve a goal.                       |
| **Perceive → Reason → Act**   | Concept        | The classic loop of an agent — observe input, think, then act.                                           |
| **Retrieval Quality**         | Concept        | How accurate and relevant the retrieved chunks are — directly decides final answer quality.              |
