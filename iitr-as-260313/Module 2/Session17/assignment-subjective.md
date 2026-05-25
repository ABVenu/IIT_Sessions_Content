# Subjective Assignment: Design a Vector Search Plan for a Support Assistant

## Practical Task

**Difficulty:** Medium

A coaching institute wants to build a support assistant for student questions. The institute has:

- 500 FAQ articles about fees, refunds, login issues, placements, and certificates.
- A SQL database with student profiles, payments, and order/status records.
- A future plan to use a vector database for meaning-based retrieval.

Create a clear design plan for how the institute should use **SQL**, **embeddings**, and a **vector database** together.

### Your Answer Must Include

Write your answer in 6 short sections:

1. **Which data should stay in SQL**  
   Mention at least 3 examples, such as payment totals, student ids, order status, or exact filters.

2. **Which data should go into the vector database**  
   Mention what should be chunked and embedded from the FAQ articles.

3. **Metadata to store with each vector**  
   Mention at least 4 useful metadata fields.

4. **Query-time flow**  
   Explain the steps from user question -> query embedding -> vector search -> top-k chunks -> final application use.

5. **Why brute force is not enough at scale**  
   Explain why comparing every query with every stored vector becomes slow, and how indexing or ANN helps.

6. **One exact-match example and one similarity-search example**  
   Give one user question that SQL should handle and one user question that vector similarity search should handle.

### Constraints

- Do not write code.
- Do not describe a full Chroma implementation.
- Keep the answer between 350 and 600 words.
- Use simple language and bullet points wherever helpful.

### Submission Instructions

- Type the answer in the answer box.

---

## Answer Explanation

### Ideal Solution Walkthrough

A strong answer should separate exact structured data from meaning-based document retrieval. SQL should handle exact ids, payment status, order status, totals, and structured filters. The vector database should handle FAQ chunks and other unstructured support text where users may ask the same meaning in different words.

The answer should also mention that FAQ articles need to be chunked, embedded with one embedding model, and stored in a vector database with useful metadata. At query time, the user question is embedded using the same model, the vector database returns top-k nearest chunks, and the application uses those chunks to show an answer or pass context to an LLM.

### Sample Ideal Answer

1. **Which data should stay in SQL**

- Student id, email, and profile details should stay in SQL because they need exact lookup.
- Payment totals and refund transaction status should stay in SQL because these require accurate structured records.
- Order or ticket status such as `open`, `resolved`, or `shipped` should stay in SQL because these are exact fields.

2. **Which data should go into the vector database**

- FAQ article text about fees, refunds, login issues, placements, and certificates should be split into chunks.
- Each chunk should be converted into an embedding.
- These embeddings should be stored in the vector database so student questions can retrieve the nearest matching chunks by meaning.

3. **Metadata to store with each vector**

- FAQ article id
- Topic or category, such as Fees or Login
- Source file or URL
- Last updated date or policy year
- Page number or section name if available

4. **Query-time flow**

- A student asks a question such as "Can I pay my course fee in parts?"
- The system converts the question into an embedding using the same embedding model used for FAQ chunks.
- The vector database searches the indexed collection.
- It returns top-k chunks closest in meaning.
- The application displays those chunks or passes them to an LLM as context for a grounded answer.

5. **Why brute force is not enough at scale**

- Brute force compares the query vector with every stored vector.
- With a small number of chunks, this may work.
- With thousands or millions of chunks, this becomes slow because every query does O(n) comparisons.
- Vector indexing and ANN help the system skip unlikely regions and return good matches faster.

6. **One exact-match example and one similarity-search example**

- SQL example: "Show payment status for student id 1042."
- Similarity-search example: "Can I pay fees in instalments?" This may match an FAQ chunk that says "Students can choose a monthly payment plan," even though the exact words differ.

### Alternative Approaches

- The vector database can be a dedicated system such as Chroma or Pinecone, or vector support inside PostgreSQL through pgvector.
- The final application may directly display retrieved FAQ chunks or pass them into an LLM for a fuller answer.
- The team can combine SQL filters with vector search, for example searching only the Refund category or only documents updated in the current policy year.
