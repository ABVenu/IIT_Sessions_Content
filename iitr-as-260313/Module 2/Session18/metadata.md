lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins

title: Implementing Vector Search Systems

objective: Understand how to store and query embeddings in vector databases

topics be covered: storing embeddings;querying vector DB


detailed subtopics to be covered:

- This session: hands-on implementation only (assume vector database concepts, indexing, and ANN were covered in the previous session — do not re-lecture theory)
- Bridge from Previous Session (5–10 mins) — Recall the conceptual similarity search process and name the tool used today (e.g. Chroma); open the lab pipeline checklist;
- Define the Objective of a Vector Search System — Establish the builder goal: given a user question, return the most semantically similar stored text chunks;
- Understand the End-to-End Implementation Workflow — Operational pipeline in code: sample data → embeddings → collection → store → embed query → top-k query → interpret results;
- Set Up the Development Environment — Install and configure a beginner-friendly vector database such as Chroma along with required Python libraries;
- Prepare Sample Data for Implementation — Structure a small dataset (documents/sentences) for embedding and retrieval; optional simple metadata fields (e.g. category);
- Generate Embeddings Using Pretrained Models — Convert sample text to vectors via API or local embedding model (same model for storage and queries);
- Initialize a Vector Database Collection — Create a collection (or index) to organize and store embeddings;
- Store Embeddings in the Vector Database — Insert vectors with identifiers and metadata; include a quick count/check that data is stored;
- Convert Query Input into Embedding — Transform a natural-language user query into an embedding using the same model as ingestion;
- Execute Similarity Search with Top-K Retrieval — Run vector similarity query; configure top-k (e.g. 3 results); read ranked output in one integrated step;
- Interpret Query Results — Understand returned text chunks, similarity scores, and ranking; discuss one wrong-result example as a class;
- Build a Minimal End-to-End Vector Search Application — Single script or notebook: query in → top-k relevant chunks out (capstone of the lab);
- Apply Basic Metadata Filtering in Queries (optional if time) — Combine similarity search with a simple filter (e.g. category tag) to refine results;
- Update the Vector Collection (optional if time) — Add new documents and embeddings to an existing collection;
- Relate Vector Databases to Agentic Systems — Explain how agents use vector databases for long-term memory, contextual retrieval, and knowledge access at scale (conceptual bridge after the lab; do not expand into a full agent architecture lesson);
