lecture ID: 153007

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins

title: Introduction to Vector Databases

objective: Learn how vector databases store and retrieve embeddings

topics be covered: vector indexing;similarity search


detailed subtopics to be covered:

- This session: conceptual only (no Chroma setup or live coding lab — that is the next session)
- Bridge from Previous Session (10–15 mins) — Recap embeddings, same embedding model for documents and queries, and semantic search workflow; confirm readiness before vector database concepts;
- Recall the Role of Embeddings in AI Systems — Short revisit only; how embeddings enable similarity-based retrieval (do not re-teach full embedding theory from the previous session);
- Identify Limitations of Traditional Databases for Vector Data — Explain why relational databases are not suitable for efficient vector similarity search at scale; contrast exact-key SQL lookup vs nearest-meaning search;
- Introduce Vector Databases — Define vector databases and their role in storing, indexing, and retrieving embeddings; mention example tools at a high level (e.g. Chroma, Pinecone, pgvector) without hands-on setup;
- Understand Similarity-Based Retrieval — Explain how vector databases return results based on semantic closeness (nearest vectors) rather than exact text or key matches;
- Develop Intuition for Similarity Search — Use real-world analogies to explain how similarity-driven retrieval works in production systems;
- Understand Similarity Measurement (Conceptual) — Reinforce only (~5 mins); closeness via distance/angle (e.g. cosine similarity) without formulas — do not repeat the full lesson from two sessions ago;
- Understand the Need for Scalable Search — Explain why brute-force comparison across all vectors is inefficient as data grows;
- Introduce Vector Indexing — Explain how indexing structures organize vectors to enable faster search than full scans;
- Understand Approximate Nearest Neighbor (ANN) Search — Explain how systems balance speed and accuracy by retrieving near-optimal results at scale;
- Understand the Similarity Search Process — Conceptual end-to-end: query embedding → search indexed collection → return nearest vectors (diagram/story level; implementation is next session);
- Differentiate Exact Match vs Similarity Search — Brief recap only (~5 mins); when keyword/SQL exact match wins vs semantic vector search — do not repeat the full comparison taught previously;
- Bridge to Next Session — Next session implements the pipeline in code (Chroma): embed, store, query, top-k, and a minimal end-to-end script;
