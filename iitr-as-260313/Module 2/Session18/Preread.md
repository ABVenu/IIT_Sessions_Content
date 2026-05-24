# Pre-read: Implementing Vector Search Systems

When someone searches your company’s FAQs or a support bot’s knowledge base, they rarely type the *exact* sentence stored in your document. They say it their own way. If search only hunts for matching words, good answers stay hidden—and everyone blames “bad search,” not the user. **Meaning-based** retrieval is how modern assistants, plugins, and smart recommendations find the right passage without a perfect keyword.

In the **previous session**, you learned *why* vector databases exist: embeddings, similarity instead of exact keys, indexing, and fast **approximate nearest neighbour** search at scale. You drew the pipeline on paper — **chunk → embed → store → query → top-k**. Today you **run** that pipeline in code.

---

**What if** you had a few hundred short articles—policies, how-tos, product lines—and a user asked in plain English: *“I want my money back after sending the shoes back”*? A spreadsheet **Find** misses *“Refunds are processed in 5–7 business days”* because the words differ. Maintaining keyword rules by hand breaks every time you add new text.

**What if** you embedded documents with one model and questions with another? Distances stop meaning anything — like mixing units on the same ruler.

**What if** leadership asks for a demo tomorrow — three relevant paragraphs for one student question — and you have never **created a collection**, **stored vectors**, or **read ranked results** from a real tool?

The challenge is not “store more files.” It is: **build a small but real system** that compares a question to many passages by **meaning**, then returns the **top matches** you can show and defend.

---

This session is **hands-on implementation only**. We assume vector-database **concepts** from the **previous session** — we will **not** re-teach indexing theory or ANN in depth. You will use **Chroma** (beginner-friendly) and a **pretrained embedding model** (local or API) on a normal laptop.

**Builder goal:** Plain-English question in → **top-k** semantically similar text chunks out, with ids, optional **metadata** (e.g. category), and interpretable **ranking**.

You will go from sample sentences on disk to **upsert → verify → query → interpret**, then wire one **minimal end-to-end** script you can extend for **RAG** and **agent retrieval** later.

---

## A simple analogy

Think of a **Kirana shop**: you say *“Bhaiya, kuch thanda de do”* without naming a brand, and the shopkeeper still hands you a cold drink. That is **intent**, not exact wording. Vector search matches **meaning in number-space**, not only the same string as in a stored document. The **previous session** explained the warehouse layout; **today** you stock the shelves and use the counter yourself.

---

**In this pre-read, you'll discover:**

- The **end-to-end path** you will code: text → embeddings → **collection** → store → query embedding → **top-k** retrieval  
- How to **set up** Chroma and embedding libraries, prepare a **small** dataset with ids and metadata, and **verify** what landed (`count`, `peek`)  
- Why the **same embedding model** must index documents and queries — and how to read **ranking** and one **wrong-result** example in class  
- How this minimal pipeline connects to **agents** that retrieve knowledge before the LLM answers  

**Session objective:** Understand how to store and query embeddings in vector databases.

---

## The pipeline you will build (overview)

```text
sample texts + metadata → embed → collection.upsert() → verify
       → user query → embed query → collection.query(n_results=k) → ranked chunks
```

| Stage | What you do |
| --- | --- |
| **Prepare data** | Short FAQ-style sentences; unique **ids**; optional **category** in metadata |
| **Embed & store** | One model encodes all documents; vectors go into a **collection** |
| **Verify** | Confirm count and peek at stored rows |
| **Query** | Encode the user question with the **same** model |
| **Retrieve** | Request **top-k** (e.g. 3) nearest neighbours |
| **Interpret** | Read rank, distances, and discuss one misleading match |
| **Extend (if time)** | Filter by metadata; **upsert** new documents and query again |

Details and full syntax are for the **live lab** — arrive with Python ready (Colab or local **venv**).

---

## Ideas worth knowing before class

**Chroma** — A lightweight vector database for learning: collections, persistent storage on disk, and similarity **query** APIs.

**Collection** — Named bucket holding documents, embeddings, ids, and metadata together.

**Upsert** — Insert or update by id when FAQs change.

**Top-k** — *“Give me the three best matches”* (`n_results=3`), not the entire database ranked.

**Metadata filter** — Narrow search: *similar meaning, but only `category = returns`*.

**Same model rule** — Document and query vectors must come from the **identical** embedding model and version.

**Verify before demo** — If `count()` is wrong, every query result is untrustworthy.

---

## Questions to explore in the live session

1. How does the same question get compared fairly to many stored passages when the **words do not match** exactly?  
2. Why must the **same embedding model** be used when storing and when querying — and what breaks if you mix models?  
3. How do you move from *“it returned three lines”* to **trusting** the ranking — using distances, categories, and **top-k**?  
4. Rank 1 is about **password reset** but the user asked about **delivery** — what failed: data, metadata filter, or missing chunks?

---

## After this session, you should be able to

- State a clear **goal** for a tiny search app (question → top similar sentences).  
- Trace and **run** the full path: embed → store → query → top-k in Chroma.  
- **Verify** storage, apply **basic metadata filtering**, and **add** new items to a collection.  
- Explain one case where similarity ranking **misleading** looks right.  
- Describe how this **retrieve** step fits **RAG** and **agent tools** without rebuilding the whole agent stack in one day.  

---

## Before class — checklist

- [ ] **Previous session** notes handy: embeddings, similarity vs SQL, top-k, indexing/ANN (conceptual only)  
- [ ] Python environment working; stable connection if using API embeddings  
- [ ] Mindset: **lab session** — you will type code, not only listen to theory  

Bring curiosity and one real domain in mind (coaching FAQs, shop policies, internal wiki). We close the loop from sample data to a **working search** you can show — the step that turns *“I understand vectors”* into *“I can ship retrieval.”*
