# Objective Assignment: Implementing Vector Search Systems

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A support team wants to save FAQ records in Chroma so users can search by meaning. Which Chroma object should hold the FAQ records with ids, documents, metadata, and embeddings?

A. Collection  
B. Python virtual environment  
C. SQLite Viewer extension  
D. Terminal command history

**Correct Answer:** A

**Answer Explanation:**  
A is correct because a Chroma collection is the named container that stores records with ids, documents, metadata, and embeddings.

B is incorrect because a virtual environment manages Python packages, not Chroma records. C is incorrect because SQLite Viewer is only an inspection tool. D is incorrect because terminal history does not store searchable vector records.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A learner creates a Chroma client using:

```python
client = chromadb.PersistentClient(path="./chroma_store")
```

What is the main purpose of using `PersistentClient` here?

A. It saves Chroma data in a local folder so it remains after the Python program ends.  
B. It forces Chroma to delete all records after every query.  
C. It converts plain text into embeddings automatically in every setup.  
D. It opens a browser page for viewing search results.

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `PersistentClient(path="./chroma_store")` stores Chroma data on disk inside the specified folder.

B is incorrect because persistence is the opposite of deleting data after the program ends. C is incorrect because automatic embedding requires an embedding function, and this lab passes embeddings manually. D is incorrect because `PersistentClient` does not open a browser page.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

In a Chroma FAQ record, which field should contain human-readable text such as `"Refunds are processed within 5 to 7 business days"`?

A. `document`  
B. `id`  
C. `embedding`  
D. `collection.name`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the document field stores the readable text that can be returned in search results.

B is incorrect because `id` is the unique key for the record. C is incorrect because an embedding is a numeric vector. D is incorrect because `collection.name` is the name of the collection, not the text inside one record.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A script stores six FAQ records in Chroma and then runs:

```python
print(collection.count())
```

What should `count()` help the learner verify?

A. The number of records currently stored in the collection  
B. The exact wording of every user query  
C. The model's total training dataset size  
D. The number of CPU cores available on the laptop

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `collection.count()` returns how many records exist in the collection. It is a useful storage verification step after upsert.

B is incorrect because `count()` does not inspect user query text. C is incorrect because Chroma count does not reveal model training data. D is incorrect because it does not inspect hardware details.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A learner writes:

```python
collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)
```

Later, the learner wants to run a meaning-based query. What must the learner provide to `collection.query(...)` in this setup?

A. A query embedding created manually using the same embedding model  
B. Only a raw text query string, because Chroma will always embed it automatically  
C. A SQL `SELECT` statement with a `WHERE` clause  
D. A screenshot of the FAQ table

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `embedding_function=None` means Chroma will not embed raw text automatically. The query text must first be converted into an embedding, and the same model used for stored documents should be used.

B is incorrect because raw text works only when an embedding function is configured. C is incorrect because `query` performs vector similarity search, not SQL. D is incorrect because screenshots are not valid query inputs.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A FAQ collection contains an item with id `doc4` and document text about password reset. Which method should be used to fetch exactly that record by id, without running meaning-based search?

A. `collection.get(ids=["doc4"])`  
B. `collection.query(query_embeddings=..., n_results=3)`  
C. `collection.peek()`  
D. `model.encode(["doc4"])`

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `get(ids=[...])` fetches records by exact id, similar to a SQL lookup by primary key.

B is incorrect because `query` performs similarity search using vectors. C is incorrect because `peek()` only shows a sample of stored rows. D is incorrect because encoding the id string creates a vector but does not fetch the stored record by id.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A learner is preparing FAQ data before calling `collection.upsert(...)`. Which lists should stay aligned so each position belongs to the same Chroma record?

A. `ids`  
B. `documents`  
C. `metadatas`  
D. `embeddings`  
E. Browser bookmark names

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A, B, C, and D are correct because `upsert` receives parallel lists. The item at each index across `ids`, `documents`, `metadatas`, and `embeddings` should describe the same record.

E is incorrect because browser bookmark names are unrelated to Chroma's stored record structure.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A team wants to verify that FAQ data was stored correctly before demonstrating similarity search. Which actions are appropriate verification steps?

A. Use `collection.count()` to confirm the expected number of records.  
B. Use `collection.peek()` to inspect a small sample of stored rows.  
C. Use `collection.get(ids=["doc1"])` to fetch one known record by exact id.  
D. Manually edit Chroma's internal SQLite files to make results look correct.  
E. Check that stored documents and metadata are not empty or mismatched.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because `count()` confirms how many records are stored. B is correct because `peek()` helps inspect sample stored data. C is correct because `get()` confirms exact id lookup works. E is correct because mismatched text and metadata can damage result quality.

D is incorrect because Chroma's SQLite files are internal storage and should not be edited manually.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A learner builds a search script with `SentenceTransformer("all-MiniLM-L6-v2")`, manually stores document embeddings, and then queries Chroma. Which statements are technically correct?

A. The stored documents and user queries should be embedded with the same model.  
B. The model produces 384-dimensional embeddings in this lab setup.  
C. A larger embedding model may be slower or heavier than a smaller one.  
D. Mixing embeddings from unrelated models in the same collection can make distances unreliable.  
E. Chroma distances are guaranteed to be identical even if the query is embedded with a different model.

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A is correct because vector distances are meaningful only when documents and queries are encoded in the same embedding space. B is correct because `all-MiniLM-L6-v2` creates 384-dimensional embeddings. C is correct because larger models can require more compute. D is correct because mixing model outputs can make similarity scores unreliable.

E is incorrect because distances are not reliable when embeddings come from different models or incompatible vector spaces.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A query for `"How do I change my login password?"` is run with `n_results=2` on a tiny six-record FAQ collection. Chroma returns the password reset row first and another weaker row second. Which interpretations are correct?

A. Rank 1 is the closest vector match among the stored records.  
B. Rank 2 can be weak because top-k returns the nearest available records, not only perfect answers.  
C. Lower distance usually indicates a closer semantic match.  
D. The second result proves that Chroma ignored the query embedding.  
E. If only one stored record is clearly relevant, asking for two results may still return a less useful second result.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because Chroma ranks returned items by vector closeness. B is correct because top-k retrieval returns the requested number of nearest available records, even when later ranks are only partly useful. C is correct because lower distance usually means a closer match. E is correct because a small collection may not contain multiple strongly relevant records for one query.

D is incorrect because a weak lower-ranked result does not mean Chroma ignored the query. It can simply be the next nearest vector available in the collection.
