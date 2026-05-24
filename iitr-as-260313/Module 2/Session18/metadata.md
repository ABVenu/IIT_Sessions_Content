lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr 50 mins

title: Implementing Vector Search Systems

objective: Understand how to store and query embeddings in vector databases

topics be covered: storing embeddings;querying vector DB


detailed subtopics to be covered:

- This session: hands-on Chroma implementation only (assume vector database concepts, indexing, and ANN from the previous session — do not re-lecture theory)
- Bridge from Previous Session — Recall the embed → store → query → top-k pipeline; introduce Chroma as today's implementation tool
- Chroma Terminology and Setup — Map Chroma concepts (client, collection, id, document, metadata, embedding) to familiar **SQL** ideas (tables/rows); install and configure PersistentClient
- Add Data to a Chroma Collection — Prepare sample FAQ data, generate embeddings with a pretrained model, upsert vectors with ids, documents, and metadata; verify with count, peek, and get
- Retrieve Data from a Chroma Collection — Embed a user query with the same model, run top-k similarity search with query(), interpret returned chunks, ranks, and distance scores; discuss one wrong-result example at interpretation level only
- Bridge to Next Session — Brief note that the RAG track will reuse this Chroma collection as the retriever layer (metadata filtering, collection updates, and retrieval tuning deferred to later RAG sessions)
