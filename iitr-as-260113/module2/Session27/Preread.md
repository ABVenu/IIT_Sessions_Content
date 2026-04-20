# Pre-read: Implementing Vector Search Systems

## The hook

When someone searches your company’s FAQs or a support bot’s knowledge base, they rarely type the *exact* sentence that lives in your document. They say it their own way. If search only looks for matching words, good answers stay hidden—and everyone blames “bad search,” not the user. Learning how **meaning-based** search works is one of the most useful skills in modern AI systems: it is how assistants, plugins, and smart recommendations find the right thing without a perfect keyword.

## The problem

**What if** you had a few hundred short articles—policies, how-tos, product lines—and a user asked a question in plain English? Copy-paste **Find** on every page will miss answers that use different words for the same idea. Scaling that by hand is slow, brittle, and impossible to maintain every time you add new text.

The challenge is not “store more files.” It is: **how do we compare a question to many passages in a way that respects what the user meant—not only what they typed?**

## The solution preview

This session is about building a **small but real vector search pipeline**. You already know that text can be turned into **embeddings** (lists of numbers that capture meaning). Here we **save** those numbers in a **vector database** (we use **Chroma**—friendly for beginners), **ask** a new question, turn that question into numbers with the **same** model, and **retrieve** the closest matches.

You will go from “data on disk” to “top answers ranked by similarity,” including **top‑k** results and light **metadata** filters—then wire it into a **minimal end-to-end** flow you can run on a normal laptop.

## A simple analogy

In the notes we use a Kirana shop: you say *“Bhaiya, kuch thanda de do”* without naming a brand, and the shopkeeper still hands you a cold drink. That is **intent**, not exact wording. A vector search system is built on the same idea: it matches **meaning** in number-space, not only the same string as in a document.

## What you will be able to do after the session

- State a clear **goal** for a tiny search app (e.g. plain-English question → top similar sentences).
- Trace the **end-to-end path**: text → embeddings → storage → query embedding → retrieval.
- Set up **Python**, **Chroma**, and **sentence-transformers**, and prepare a **small** text dataset for practice.
- **Create a collection**, **store** vectors with IDs, text, and metadata, and **verify** what landed in the database.
- Run **similarity search**, read **distances / ranking**, and set **top‑k** retrieval.
- Apply **basic metadata filtering** (e.g. category) to narrow results.
- **Add** new items to an existing collection and connect the pieces into one **minimal working** pipeline.

## Questions we will answer in the live session

1. How does the same question get compared fairly to many stored passages—especially when the words do not match exactly?
2. Why must the **same embedding model** be used when storing and when querying—and what breaks if you mix models?
3. How do you go from “it returned three lines of text” to **trusting** the ranking—using distances, categories, and top‑k settings?

Bring your curiosity: we close the loop from sample data to a working search you can extend later.
