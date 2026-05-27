# Objective Assignment: Embeddings & Vector Search

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A music app stores a numeric **fingerprint vector** for every song. When a user hums a tune, the app converts the hum into another vector and finds the **closest** stored song.

Which concept from text search does this example best illustrate?

A. Embeddings place similar meaning closer in vector space  
B. Keyword search matches exact spelling only  
C. SQL `WHERE id = 5` finds records by primary key only  
D. Fine-tuning retrains the model on every new song

**Correct Answer:** A

**Answer Explanation:**  
A is correct because embeddings map items (songs or sentences) to numeric coordinates so that similar items sit near each other; the app picks the nearest stored vector to the hum vector.

B is incorrect because the example is about meaning similarity via vectors, not exact word matching. C is incorrect because SQL id lookup is exact key search, not nearest-neighbour meaning search. D is incorrect because the scenario describes comparing vectors at query time, not retraining a model for each song.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A learner encodes two FAQ lines with `SentenceTransformer("all-MiniLM-L6-v2")` and prints `len(vector_a)`.

What vector length should they expect for each sentence?

A. 384  
B. 2  
C. 76800  
D. The length changes randomly on every run for the same sentence

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `all-MiniLM-L6-v2` produces a fixed-size embedding of 384 numbers per input sentence in this lab setup.

B is incorrect because embeddings are dense vectors with hundreds of dimensions, not length 2. C is incorrect because 76800 is not the output size of this model. D is incorrect because the same model and same sentence produce a stable vector length; only the exact float values might vary slightly by environment, not the dimension count.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A team stored FAQ chunks last week using `all-MiniLM-L6-v2`. Today they embed user questions with a **different** embedding model before querying Chroma.

What is the most likely problem?

A. Distance scores become unreliable because vectors live in different spaces  
B. Chroma will automatically re-encode old rows with the new model  
C. The collection count will always become zero  
D. Semantic search will work better because two models mean double the meaning

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the same embedding model must encode both stored documents and queries; mixing models breaks the meaning of distance comparisons.

B is incorrect because Chroma does not silently replace stored embeddings when you change models. C is incorrect because the row count is unrelated to which encoder you use. D is incorrect because mixing models does not improve search; it makes similarity scores meaningless.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

In a Chroma setup, a developer runs `model.encode(...)` in Python and passes the resulting lists to `collection.upsert(...)` and `collection.query(query_embeddings=...)`.

What role does **Chroma** play in this workflow?

A. It stores vectors and runs similarity search; it is not the embedding model  
B. It trains a new embedding model from scratch on every upsert  
C. It tokenizes raw text into subwords automatically in every setup  
D. It replaces the need for any embedding step

**Correct Answer:** A

**Answer Explanation:**  
A is correct because in this lab you encode text with Sentence Transformers and Chroma handles persistence and nearest-neighbour retrieval.

B is incorrect because Chroma is a vector database client, not a model trainer. C is incorrect because tokenization and encoding happen in the embedding model library, not inside Chroma by default here. D is incorrect because you still must create embeddings before upsert and query when `embedding_function=None`.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

An e-commerce helpdesk has these three stored FAQ lines:

1. `"Refunds are processed within 5 to 7 business days after the return is approved."`  
2. `"Orders above 499 rupees qualify for free shipping."`  
3. `"You can reset your password from the account settings page."`

A user asks: *"I want to return my shoes and get my money back."*

Which line should rank **#1** in a semantic search over this collection?

A. Line 1  
B. Line 2  
C. Line 3  
D. All three must tie with distance 0

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the user question is about returning an item and getting money back, which is closest in meaning to the refund-processing FAQ, not shipping or password reset.

B is incorrect because free shipping is a different topic from returns and refunds. C is incorrect because password reset is unrelated to returning shoes. D is incorrect because distances are relative scores; paraphrases rarely produce identical vectors for unrelated lines.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A script uses:

```python
collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)
```

Later the developer calls `collection.query(...)` for a user question.

What must they pass for a meaning-based search in this setup?

A. `query_embeddings` built with the same model used at upsert time  
B. Only the raw question string, with no embedding step  
C. A SQL `JOIN` between two tables  
D. The collection name repeated three times

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `embedding_function=None` means Chroma will not embed text automatically; you must supply `query_embeddings` from the same encoder used for stored documents.

B is incorrect because raw text query works only when an embedding function is configured on the collection. C is incorrect because Chroma `query` performs vector similarity search, not SQL joins. D is incorrect because the collection name is not a valid query input.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A product team compares **keyword search** and **semantic search** for a support bot.

Which statements correctly describe when each approach fits?

A. Keyword search is strong for exact filters such as `WHERE user_id = 7`  
B. Semantic search helps when users paraphrase FAQs in informal language  
C. Semantic search replaces every SQL use case in all databases  
D. The two approaches can work together: SQL for structured facts, vectors for free-text meaning  
E. Keyword search always understands that "get my money back" means "refund"

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because structured exact filters are a strength of keyword/SQL-style lookup. B is correct because embeddings capture meaning beyond exact word overlap. D is correct because real systems often combine SQL for structured data with vector search for natural-language questions.

C is incorrect because semantic search does not replace all SQL scenarios. E is incorrect because keyword search misses paraphrases unless the exact words appear.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

Before demoing similarity search, a learner finishes `collection.upsert(...)` on five FAQ rows.

Which checks are sensible verification steps?

A. `collection.count()` should match the number of FAQs upserted  
B. `collection.peek()` helps spot empty or obviously wrong stored text  
C. `collection.get(ids=["doc4"])` fetches one row by exact id for debugging  
D. Manually editing files inside `./chroma_store` is the recommended way to fix bad rows  
E. `ids`, `documents`, `metadatas`, and `embeddings` lists should stay index-aligned during upsert

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because count confirms all rows landed. B is correct because peek gives a quick sample without writing a search query. C is correct because `get` is exact id lookup, useful to verify one known row. E is correct because misaligned parallel lists attach the wrong metadata or vector to a document.

D is incorrect because internal Chroma storage files should not be hand-edited; fix data in code and upsert again.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A learner inspects Chroma query output:

| Rank | id   | distance |
|------|------|----------|
| 1    | doc2 | 0.41     |
| 2    | doc1 | 0.52     |
| 3    | doc3 | 0.89     |

Which interpretations are correct?

A. Rank 1 is the closest vector match among stored records for this query  
B. Smaller distance often means nearer meaning for distance-based metrics  
C. A low distance always proves the answer is legally correct for every business case  
D. Scores are relative; inspecting the returned **text** of top-k rows still matters  
E. If no FAQ on the topic exists, rank 1 may still be the nearest available vector, not a perfect answer

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A is correct because Chroma orders results by vector proximity. B is correct because, for distance-based metrics in this lab, smaller distance usually means closer meaning. D is correct because teams must read retrieved document text, not only the number. E is correct because missing topics (e.g. no UPI FAQ) can still produce a rank-1 neighbour that is only the least-bad match in a small store.

C is incorrect because vector closeness does not guarantee business or policy correctness.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A developer builds a tiny FAQ retriever with Chroma and `all-MiniLM-L6-v2`. They set `embedding_function=None`, upsert five rows, and run `n_results=3`.

Which technical choices are correct for this design?

A. Call `model.encode` on FAQ strings before `upsert`, passing `embeddings=` explicitly  
B. Encode each user question with the **same** `model` object used for documents  
C. Use `collection.query(query_embeddings=..., n_results=3)` for top-k semantic retrieval  
D. Use `collection.get(ids=[...])` when they need exact fetch by primary key, not nearest meaning  
E. Pass raw user text directly to `query` without embeddings because Chroma always embeds queries internally in this setup

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A is correct because manual embeddings are required when `embedding_function=None`. B is correct because the same model rule keeps distances meaningful. C is correct because `query` with `query_embeddings` performs top-k similarity search. D is correct because `get` is id-based lookup, distinct from meaning search.

E is incorrect because with `embedding_function=None`, raw text cannot be passed alone to `query`; you must supply embeddings.
