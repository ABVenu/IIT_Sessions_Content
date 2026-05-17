# Pre-read: Introduction to Vector Databases

Imagine you built a support bot for a large online coaching platform. Last week, you learned how **embeddings** turn questions and FAQ chunks into numbers so that *similar meaning* sits close together on a hidden map. A student types *"I cannot log in"* — and your demo finds the right **password reset** article even when the words do not match.

It works beautifully with **ten** FAQ chunks in class. Then your company uploads **five lakh** policy pages, old tickets, and wiki updates. Every new question must be compared against every stored chunk — in under a second, while hundreds of students ask at once. Suddenly the clever idea feels like searching a national stadium **seat by seat** for one friend.

That gap — *meaning search that still feels instant at real scale* — is what today's session is about.

---

## When the Right Answer Is Not a Row ID

You already know two kinds of questions.

> **Exact questions:** *"Show order `ORD-8842`"* or *"All users where `city = Mumbai`."*  
> A normal database table with IDs and filters is perfect. You are looking for a **specific key**, not a feeling.

> **Meaning questions:** *"Find help articles **like** this complaint about two-factor login."*  
> The article might say **MFA recovery** while the user never used those words. You need **nearest meaning**, not `WHERE text LIKE '%login%'`.

**Embeddings** gave you the meaning map. The new puzzle is **where** you store millions of coordinates and **how** you find the closest pins without reading every pin on every query.

---

## The Specialised Warehouse for Meaning

Picture a giant notice board at a coaching centre. Thousands of sticky notes — each one a small FAQ chunk. Notes about **fees** cluster on the left; **placements** in the middle; **hostel rules** at the back.

A student walks in and asks aloud: *"Can I pay fees in instalments?"* You do not read every note word by word. You walk to the **fee corner** and read the **nearest** notes. A **vector database** is the system that holds those notes as numbers, builds a **map of neighbourhoods**, and returns the **top few** best matches in milliseconds — even when the board has millions of stickies.

That is the hero of today: not a replacement for your normal SQL tables, but a **specialised store** for embedding vectors with three jobs — **store**, **index**, and **retrieve**.

---

## In this pre-read, you'll discover:

- Why **relational databases** excel at exact facts but struggle with fast **nearest-meaning** search over huge collections of embeddings
- What a **vector database** does, how **similarity-based retrieval** and **top-k** results work, and why **brute-force** comparison breaks at scale
- How **vector indexing** and **approximate nearest neighbour (ANN)** search trade a little perfect accuracy for speed users actually feel
- Where vector stores fit in **RAG**, **semantic search**, **recommendations**, and **agent memory** — and how that connects to hands-on **Chroma** in the next session

---

## Ideas Worth Knowing Before We Go Live

**Vector database** — Storage built for embedding vectors: save text + metadata + numbers, search by **closeness**, not by matching spelling.

**Similarity-based retrieval** — Return chunks whose vectors are **nearest** to the query vector. Same **embedding model** for documents and queries — still non-negotiable.

**Top-k** — *"Give me the five best matches,"* not the whole database ranked. Like Google showing one page of results, not rank 10,000.

**Brute-force search** — Compare the query to **every** stored vector, then sort. Fine for classroom demos; too slow for production traffic on lakhs of chunks.

**Vector indexing** — Extra structures (like a PIN-code map at the post office) so search **skips** huge regions instead of opening every bag.

**ANN (Approximate Nearest Neighbor)** — *Good enough, fast enough* neighbours — like ride apps showing **nearby** drivers, not every driver in India ranked to the millimetre. Teams tune this when chatbots must answer in sub-seconds.

**Metadata filter** — Combine meaning with rules: *"Similar to this question, but **only** Billing articles from 2025."*

**SQL + vectors together** — SQL for **who** the customer is and **what** they bought; vector search for **what they mean** in free text. Agents often call **both** tools before the LLM speaks.

**Upsert** — Save or refresh a chunk by id when documents change, without duplicate rows piling up.

---

## Questions We Will Answer in the Live Session

1. **The tool picker:** For each question — total March revenue, wiki pages related to *"reset two-factor auth"* when articles say *"MFA recovery"*, and all orders with `status = shipped` — do you need **SQL**, **vector similarity**, or **both**?

2. **The scale shock:** Your collection grows from 1,000 to 10 million embedding vectors. Why does a simple loop that compares **every** vector to every query stop being acceptable — and what do **indexing** and **ANN** change?

3. **The agent blueprint:** Design a tool called `find_similar_support_tickets(description)`. What gets embedded, what does the vector database return, and how should an **agent** use those snippets without treating the store as its entire "brain"?

---

## After This Session, You Will Be Able To

- Explain why **embeddings alone** are not enough — you need the right **storage and search layer** at scale  
- Contrast **exact-key lookup** vs **nearest-meaning search** and pick the right tool for a business question  
- Walk through the end-to-end story: **chunk → embed → store → query → top-k → use in UI, RAG, or agent tools**  
- Describe **indexing** and **ANN** in plain language — speed vs perfect rank — without fear of the jargon  
- Place vector databases in **semantic search**, the **retrieve** step of **RAG**, and **long-term agent memory**  
- Arrive ready for the **next** session, where you will run that pipeline in real **Chroma** code

Today's session is **conceptual only** — no live Chroma lab yet. Come with your **Python environment** from earlier weeks, your notebook sketch of the semantic search workflow from last time, and curiosity about what happens when ten classroom chunks become ten million company documents.

See you in class. The step from *"I know what embeddings are"* to *"I know where and how fast to search them"* is what separates a demo from a system your users can trust.
