# Objective Assignment — RAG Architecture and Pipeline

**Total Questions:** 10 | **MCQs:** 6 (4 Easy, 2 Moderate) | **MSQs:** 4 (2 Moderate, 2 Hard)

---

## Question 1 *(Easy | MCQ — Single Correct)*

An e-commerce startup is building an AI assistant that always answers customer questions using the company's actual rules — not guesses from the internet. The developers decide to implement an architecture where the AI first searches a knowledge base before generating a response. What is this architecture called?

- A) Recursive Attention Generation
- B) Retrieval-Augmented Generation
- C) Random Answer Generator
- D) Reinforcement-Aided Generation

**Correct Answer:** B) Retrieval-Augmented Generation

**Answer Explanation:**
RAG stands for **Retrieval-Augmented Generation**. It is an AI architecture where a retrieval system first fetches relevant documents from a knowledge base, and then passes that content to an LLM to generate a final answer grounded in real data — not model memory.
- A is incorrect — "Recursive Attention Generation" is a made-up term.
- C is incorrect — "Random Answer Generator" is not a real architecture.
- D is incorrect — "Reinforcement-Aided Generation" is not what RAG means.

---

## Question 2 *(Easy | MCQ — Single Correct)*

Aarav is designing a RAG pipeline. After the user types a question, he wants one specific component to convert that question into a vector and search the vector database to return the most relevant policy paragraphs. Which component of the RAG pipeline handles this job?

- A) Generator
- B) Prompt Builder
- C) Retriever
- D) Knowledge Source

**Correct Answer:** C) Retriever

**Answer Explanation:**
The **Retriever** is the component that converts the user query into an embedding vector and searches the vector database (e.g., ChromaDB) to return the top-K most similar document chunks. It does not generate an answer — that is the Generator's job. The Prompt Builder assembles the retrieved chunks into a structured prompt. Knowledge Sources are the raw documents stored in the system.

---

## Question 3 *(Easy | MCQ — Single Correct)*

ShopEasy has written five documents: a return policy, a refund policy, a shipping policy, a warranty policy, and a cancellation policy. They upload all five into their RAG system so the AI can consult them when answering customer queries. What are these five documents called in RAG terminology?

- A) Embeddings
- B) Vector Chunks
- C) Knowledge Sources
- D) Context Builders

**Correct Answer:** C) Knowledge Sources

**Answer Explanation:**
**Knowledge Sources** are the documents from which the retrieval system fetches relevant information to answer questions. They are the reference books handed to the LLM before the exam. In this case, the five policy documents are the knowledge sources of the RAG system.
- A is incorrect — Embeddings are the numerical vector representations of text, not the documents themselves.
- B is incorrect — "Vector Chunks" is not the correct term; chunks are pieces of knowledge sources.
- D is incorrect — "Context Builders" is not a RAG component.

---

## Question 4 *(Easy | MCQ — Single Correct)*

Meera runs her RAG script, indexes her policy documents, and then shuts down her laptop. The next day, she restarts the script and wants all the previously indexed embeddings to still be available without re-indexing. Which ChromaDB client mode should she have used when setting up the vector database?

- A) `EphemeralClient`
- B) `InMemoryClient`
- C) `TemporaryClient`
- D) `PersistentClient`

**Correct Answer:** D) `PersistentClient`

**Answer Explanation:**
`chromadb.PersistentClient(path=...)` saves data to disk at the specified path, so all stored embeddings and documents survive after the script stops running. This is the mode used in the session's e-commerce RAG implementation with `path="./chroma_policy_db"`.
- A, B, and C are either non-existent or in-memory modes that lose data when the process terminates.

---

## Question 5 *(Moderate | MCQ — Single Correct)*

A RAG-powered customer support bot is configured with `top_k = 1` for all queries. A customer asks: *"What is the express shipping timeline, and can I return an electronic item if I change my mind?"* What is the most likely problem with this configuration for this query?

- A) The query will fail to embed correctly because it has two topics.
- B) ChromaDB will raise an error when a query spans multiple categories.
- C) Only one chunk will be retrieved, likely missing the relevant context for one of the two topics in the question.
- D) The LLM will refuse to answer unless exactly 3 chunks are provided.

**Correct Answer:** C) Only one chunk will be retrieved, likely missing the relevant context for one of the two topics in the question.

**Answer Explanation:**
`top_k = 1` tells the retriever to return only the single most similar chunk. When a customer asks a multi-topic question (shipping + returns), the retriever will return only the chunk closest in vector space — likely shipping or returns, but not both. This means the LLM will have incomplete context and may give an answer that addresses only one part of the question.
- A is incorrect — a multi-topic query embeds perfectly fine into a single vector.
- B is incorrect — ChromaDB does not raise errors for cross-category queries.
- D is incorrect — the LLM has no hard requirement on chunk count.

---

## Question 6 *(Moderate | MCQ — Single Correct)*

While inspecting the output of `retrieve_policy_content()`, Rohan notices a `distance` value of `0.08` for one chunk and `0.67` for another. Both were retrieved for the query: *"How long does standard shipping take?"* What does the lower distance value of `0.08` indicate?

- A) The chunk with `0.08` has fewer tokens and is cheaper to process.
- B) The chunk with `0.08` is less relevant because smaller numbers mean less overlap.
- C) The chunk with `0.08` is more semantically similar to the query — lower cosine distance means higher relevance.
- D) The distance represents the number of matching keywords, so `0.08` means very few matching words.

**Correct Answer:** C) The chunk with `0.08` is more semantically similar to the query — lower cosine distance means higher relevance.

**Answer Explanation:**
In ChromaDB with `"hnsw:space": "cosine"`, the **distance** is a cosine distance metric. A **lower distance** means the two vectors point in nearly the same direction — i.e., the chunk is semantically very close to the query. A distance of `0.08` means very high similarity; `0.67` means much lower similarity. This is not about keyword matching or token count — it is about semantic vector closeness.

---

## Question 7 *(Moderate | MSQ — Multiple Correct)*

The `index_policy_documents()` function in the e-commerce RAG system uses `collection.upsert(...)` instead of `collection.add(...)` to store policy chunks. Which of the following statements about `upsert` are correct? *(Select all that apply.)*

- A) It inserts a new record if the given ID does not already exist in the collection.
- B) It updates an existing record if the given ID already exists in the collection.
- C) It raises a `DuplicateIDError` if the same ID is added twice.
- D) It is safe to run multiple times without creating duplicate entries.
- E) It permanently deletes all existing embeddings before inserting new ones.

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct** — `upsert` inserts a new record when the ID is not found.
- **B is correct** — `upsert` updates the existing record when the ID is already present.
- **C is incorrect** — `add` raises a duplicate error, not `upsert`. That is precisely why `upsert` is preferred here.
- **D is correct** — Because `upsert` handles both insert and update cases, re-running the indexing script is safe and idempotent.
- **E is incorrect** — `upsert` does not delete unrelated embeddings; it only touches the records with the matching IDs.

---

## Question 8 *(Moderate | MSQ — Multiple Correct)*

A developer is deciding how to store a large warranty policy document in a RAG system. A colleague suggests storing the entire document as a single chunk. Which of the following statements about document chunking are correct, and support the case for breaking the document into smaller chunks instead? *(Select all that apply.)*

- A) Smaller chunks allow the retriever to pinpoint the exact paragraph relevant to the query, rather than returning the entire document.
- B) Storing the entire document as one chunk ensures complete context is always available and improves answer quality.
- C) Smaller chunks reduce the amount of irrelevant information injected into the LLM prompt.
- D) Proper chunking improves retrieval accuracy because each chunk focuses on one specific topic.
- E) The LLM automatically breaks large chunks into smaller pieces before generating an answer.

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A is correct** — Smaller chunks are more precise retrieval targets; the retriever can find the exact relevant paragraph.
- **B is incorrect** — Storing the whole document as one chunk means it may be returned even when only one line is relevant, wasting tokens and confusing the LLM.
- **C is correct** — Focused chunks mean the prompt contains only the relevant content, reducing noise.
- **D is correct** — One-topic-per-chunk makes similarity search more accurate since the chunk's embedding captures a specific concept.
- **E is incorrect** — The LLM does not perform chunking; chunking is done as a pre-processing step before indexing.

---

## Question 9 *(Hard | MSQ — Multiple Correct)*

Sneha is debugging her RAG system. For the query *"Will I get a refund if my product arrived damaged?"*, she expects the refund policy and warranty policy chunks to be retrieved. However, the system keeps retrieving the shipping policy chunk as one of the top results. Which of the following could be valid reasons for this problem? *(Select all that apply.)*

- A) The `top_k` value is set to 1, so only the single most similar chunk is returned, and the shipping chunk happens to be closest in vector space due to surface-level semantic overlap.
- B) The refund and warranty policy chunks were never indexed into the ChromaDB collection, so they are not searchable.
- C) The embedding model generated poor-quality vectors for the refund and warranty chunks, causing their vectors to be far from the query vector even though they are topically relevant.
- D) ChromaDB's cosine similarity always ranks shipping-related content higher than refund content regardless of the query.
- E) The query phrasing ("arrived damaged") does not closely match the language in the refund/warranty chunks, leading to lower similarity scores for those chunks.

**Correct Answers:** A, B, C, E

**Answer Explanation:**
- **A is correct** — A `top_k=1` setting returns only one result. If the shipping chunk has any linguistic overlap with "arrived" (delivery-related), it may edge out the refund chunk.
- **B is correct** — If the policy chunks were not indexed via `collection.upsert(...)`, they cannot be retrieved at all.
- **C is correct** — Embedding quality matters. If the model generated poor vectors, semantic similarity search will not work correctly even for topically relevant chunks.
- **D is incorrect** — ChromaDB does not have any category preference; it ranks purely by vector distance. Shipping content is not inherently ranked higher.
- **E is correct** — Retrieval is based on semantic similarity of vectors. If the query phrasing is very different from the language in the policy chunks, their vector distances will be higher, causing them to rank lower.

---

## Question 10 *(Hard | MSQ — Multiple Correct)*

In the e-commerce RAG pipeline built in this session, the `build_grounded_prompt(query, chunks)` function is a critical step. Which of the following statements correctly describe what this function does and why it matters? *(Select all that apply.)*

- A) It converts the customer's natural language query into an embedding vector for ChromaDB search.
- B) It assembles all retrieved policy chunks into a structured, labeled context block that the LLM can read.
- C) It instructs the LLM via the prompt to answer only using the provided policy context and not from general knowledge.
- D) It labels each retrieved chunk with its source document name so the LLM knows which policy it came from.
- E) It directly calls the OpenAI API to get the LLM's final response.
- F) It includes a fallback rule instructing the LLM to say it does not have enough information if the answer is not present in the retrieved context.

**Correct Answers:** B, C, D, F

**Answer Explanation:**
- **A is incorrect** — Embedding creation is done by `create_embeddings()`, not the prompt builder.
- **B is correct** — The function loops through all retrieved chunks and combines them into a labeled `context` string injected into the prompt.
- **C is correct** — The prompt explicitly says: *"Answer the customer's question using ONLY the policy context provided below."* This is what grounds the LLM.
- **D is correct** — Each chunk is labeled with `Policy Chunk {index} | Source: {source}` so the LLM has transparent attribution.
- **E is incorrect** — Calling the OpenAI API is handled by `generate_answer_from_context()`, not the prompt builder.
- **F is correct** — The prompt includes the rule: *"If the answer is not present in the context, say: 'I do not have enough information in the provided policy documents.'"* — this is the LLM's fallback instruction.
