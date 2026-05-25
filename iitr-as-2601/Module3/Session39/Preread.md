# Pre-read: Embeddings & Vector Search

Imagine you open a shopping app and type, **"I want my money back for returned shoes."** You may not use the word **refund**, but the app should still connect your sentence to the refund policy.

This is the challenge many modern AI systems face. People ask questions in natural language, while documents, FAQs, policies, and notes may use different words for the same idea.

That is where **embeddings** and **vector search** become important.

In the previous session, you learned the foundation of **RAG**, where an AI system first retrieves useful information from an external source and then uses that information to answer. This session focuses on one of the most important parts of that retrieval step: how text is converted into numbers, stored, compared, and searched by meaning.

## Why Meaning-Based Search Matters

Let us take a simple example from daily life. Suppose you run an e-commerce support desk with FAQ lines about returns, refunds, shipping, passwords, and delivery. Now a customer asks, **"I returned my shoes. When will I get my money back?"**

The customer did not use the exact phrase **"refunds are processed"**, but any human can understand that the refund FAQ is the best match. The computer needs a way to reach the same conclusion. It needs to compare **meaning**, not just spelling.

Embeddings help with this.

An **embedding** is a list of numbers that represents the meaning of a piece of text. In simple words, it is like a **meaning fingerprint**. Similar meanings get similar number patterns, while unrelated meanings stay far apart.

## The Map Analogy

Think of embeddings like locations on a map. Nearby locations are easy to compare because their coordinates are close. In the same way, sentences about refunds sit near other refund-related sentences, while sentences about password reset sit near account-access sentences.

The computer does this using **vectors**, which are ordered lists of numbers. You do not manually create these numbers. A trained **embedding model** takes text and returns a vector that can be stored, compared, or searched.

## From Text to Searchable Meaning

The journey is simple. First, normal text such as an FAQ sentence is converted into a vector. Then the vector is stored along with the original text. When a user asks a question, the same model converts that question into another vector, and the system searches for stored vectors that are closest in meaning.

This is the core idea behind **semantic search**. The word **semantic** means related to meaning. Semantic search looks for what the user means, not only the exact words they typed.

This is why the **same embedding model** must be used for both stored content and user questions. If two different models create the vectors, the comparison may not make sense. It is like using two maps with different coordinate systems.

## Why We Need a Vector Database

For five FAQ lines, you could compare vectors one by one. But real systems may have thousands or lakhs of chunks from PDFs, support articles, policies, manuals, or internal documents. At that point, you need a **vector database**.

A vector database stores the original text, a unique ID, metadata such as category or source, and the embedding vector used for meaning-based search.

In this session, the main tool is **Chroma**. You will also hear about **FAISS**, another common tool. The exact tool can change, but the workflow remains the same: **embed, store, search, inspect**.

Think of Chroma like a library catalogue sorted by meaning. A normal catalogue may search by title, author, or keyword. A vector database can find content close to the user's question even when the wording is different.

## Understanding Similarity Scores

When the system searches, it does not simply say **"match"** or **"no match."** It gives a ranked list of results. If a user asks about money back after returning shoes, Rank 1 may be the refund policy and Rank 2 may be the return window.

Many vector search tools also show a **distance** or similarity value. In distance-based results, a smaller distance usually means the stored text is closer to the user question.

But these scores are not exam marks. Rank 1 is not automatically correct. You still need to inspect the returned text and check whether it answers the user's need.

If your knowledge base does not contain any payment FAQ, and a user asks, **"Can I pay with UPI?"**, the system may still return the closest available result. That does not mean the answer is correct. It means the database found the nearest meaning among the limited content it had.

Good search depends on good data.

## What You Will Learn

In this pre-read, you'll discover:

- How **embeddings** turn text into meaning-based number representations.
- How **vectors** help compare sentences that use different words but share similar meaning.
- Why tools like **Chroma** and **FAISS** are useful for storing and searching vectors.
- How **top-k semantic search** returns the best few matches instead of only one answer.

## What's Next

By the end of the session, you should be able to:

- Explain embeddings using a simple real-life analogy.
- Describe why semantic search is different from keyword search.
- Read top-k results and judge whether the retrieved chunks are relevant.
- Connect vector search to the larger RAG pipeline.

## Questions to Think About Before Class

- If two people ask the same question using totally different words, how can a computer know both questions mean the same thing?
- What should happen when the best available result is still not good enough to answer the user's question?
- If a support system returns three possible FAQ matches, how would you decide which one should be used in a final AI answer?

Keep these questions in mind. The session will turn this idea of **searching by meaning** into a working retrieval flow.
