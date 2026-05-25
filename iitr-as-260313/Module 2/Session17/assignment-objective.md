# Objective Assignment: Introduction to Vector Databases

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A course support bot stores policy documents as embeddings. A student asks, "Can I get a refund for a cancelled workshop?"

What should the system do before comparing this question with stored document vectors?

A. Convert the question into an embedding using the same embedding model used for documents.  
B. Convert the question into a SQL table name.  
C. Delete all old document vectors and start again.  
D. Translate the question into every Indian language before searching.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because semantic search compares vectors. The user question must be converted into an embedding using the same embedding model as the stored document chunks, otherwise vector closeness is not meaningful.

B is incorrect because SQL table names are unrelated to semantic comparison. C is incorrect because existing document vectors do not need to be deleted for every query. D is incorrect because translation into every language is not required for the vector search workflow described here.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A database query asks: "Find order where `order_id = 5721`."

Which search style is best suited for this task?

A. Exact-key lookup  
B. Similarity search  
C. ANN search over document chunks  
D. Product recommendation search

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the query asks for an exact id match. Relational databases and SQL-style exact lookup are excellent for ids, statuses, dates, and structured fields.

B is incorrect because similarity search is useful when the user asks by meaning, not by exact id. C is incorrect because ANN over document chunks is unnecessary for one exact order id. D is incorrect because this is not a recommendation problem.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A vector database is used in a FAQ assistant. Which option best describes its main role?

A. It stores, indexes, and retrieves embeddings by similarity.  
B. It permanently changes the weights of the LLM.  
C. It replaces every relational database in a company.  
D. It writes the final natural-language answer by itself in all cases.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because a vector database is designed to store embedding vectors, organise them with indexes, and retrieve nearest vectors for a query.

B is incorrect because changing model weights is fine-tuning, not vector database usage. C is incorrect because SQL databases are still useful for exact structured data. D is incorrect because a vector database retrieves relevant items; another application or LLM may use those results to write the final answer.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A shopping app receives the query "comfortable shoes for daily walking" and wants to find products with similar meaning, even if product descriptions do not contain the exact same words.

Which approach best matches this need?

A. Semantic similarity search using embeddings  
B. Exact lookup by product id only  
C. Sorting all products alphabetically  
D. Checking whether the word "comfortable" appears in every product title only

**Correct Answer:** A

**Answer Explanation:**  
A is correct because embeddings and similarity search can find items close in meaning, even when exact words differ.

B is incorrect because there is no exact product id in the user query. C is incorrect because alphabetical sorting does not capture meaning. D is incorrect because keyword-only search may miss related descriptions that use different wording.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A vector search system has 20 lakh stored vectors. For every user question, it compares the query vector with all 20 lakh vectors before sorting the results.

What is the biggest problem with this design?

A. It is brute-force search and can become too slow at scale.  
B. It is ANN search and always returns random results.  
C. It is exact-key lookup and cannot store vectors.  
D. It is metadata filtering and removes all useful results.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because comparing the query with every stored vector is brute-force nearest-neighbour search. It may be accurate, but it becomes slow as the collection grows.

B is incorrect because ANN search is designed to avoid scanning everything and does not mean random results. C is incorrect because the described process is vector comparison, not exact-key SQL lookup. D is incorrect because metadata filtering is about narrowing results using tags, not scanning every vector.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A vector database returns the five nearest policy chunks for a user question instead of returning the entire ranked list of all chunks.

Which concept is being used?

A. Top-k retrieval  
B. Full table deletion  
C. Model fine-tuning  
D. Primary-key indexing only

**Correct Answer:** A

**Answer Explanation:**  
A is correct because top-k retrieval returns the best `k` matches, such as top 3, top 5, or top 10, instead of returning the full database.

B is incorrect because no data is deleted. C is incorrect because fine-tuning changes model weights, while this is retrieval. D is incorrect because primary-key indexing is for exact id lookup, not nearest-vector retrieval.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A support team is designing a vector database for internal help articles. Each article chunk will be stored with its embedding.

Which additional information is useful to store as metadata?

A. Source file or URL  
B. Category such as Billing or Account  
C. Policy year or last updated date  
D. Random emojis unrelated to the document  
E. Ticket id or page number when available

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because source information helps trace where a result came from. B is correct because category metadata can filter results. C is correct because policy year or update date can avoid returning outdated information. E is correct because ticket id or page number can help locate the original context.

D is incorrect because unrelated random emojis do not help filtering, tracing, or retrieval quality.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A company has both SQL tables and a vector database. Which decisions are appropriate?

A. Use SQL to calculate total revenue for March.  
B. Use vector similarity search to find policy paragraphs related to "remote work" when documents say "work from home."  
C. Use SQL exact lookup to fetch `user_id = 42`.  
D. Use vector search as a complete replacement for all exact payment reports.  
E. Use both SQL filters and vector similarity when the query needs structured filtering plus meaning search.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because revenue totals are structured aggregate queries suited for SQL. B is correct because vector similarity can match related meanings with different words. C is correct because exact id lookup is a SQL strength. E is correct because real systems often combine structured filters with semantic search.

D is incorrect because vector search should not replace SQL for exact financial reports, counts, or compliance facts.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A vector database uses ANN search for a large collection. Which statements correctly describe ANN?

A. ANN returns very good nearest-neighbour results faster than scanning every vector.  
B. ANN may trade a small amount of exact ranking accuracy for much better speed.  
C. ANN guarantees the mathematically perfect top-k in every case.  
D. ANN can use index structures such as graph-style or partitioning-style indexes.  
E. ANN is useful only when the collection has exactly five vectors.

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because ANN is designed to retrieve near-optimal neighbours quickly at scale. B is correct because ANN commonly trades perfect exhaustive accuracy for speed. D is correct because vector systems may use index structures such as HNSW-style graphs or IVF-style partitions.

C is incorrect because exact mathematical top-k is not guaranteed by approximate search. E is incorrect because ANN matters mainly when data grows large; tiny collections can often use exact search.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A team is building a conceptual retrieval pipeline for a policy assistant. The planned flow is:

`documents -> chunks -> embeddings -> vector DB with index -> query embedding -> top-k chunks -> application uses returned text`

Which statements are correct?

A. The same embedding model should be used for document chunks and user queries.  
B. The vector database should store only numbers and never store original text or metadata.  
C. Vector indexing helps avoid scanning every stored vector for every query.  
D. K-means and KNN are related to the idea of closeness, but they are not complete vector database products by themselves.  
E. FAISS is an example of a library used for fast vector similarity search.

**Correct Answers:** A, C, D, E

**Answer Explanation:**  
A is correct because document and query vectors must share the same embedding space. C is correct because indexing helps skip unlikely regions and improves search speed. D is correct because K-means and KNN are related algorithmic ideas, not full vector database products. E is correct because FAISS stands for Facebook AI Similarity Search and is used for fast vector search.

B is incorrect because practical vector databases often store vectors along with original text and metadata for filtering, traceability, and downstream use.
