# Objective Assignment: Embeddings & Vector Search

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

An e-commerce support team stores FAQ answers in a vector database. Each FAQ answer is converted into a list of numbers that capture its meaning.

What is this list of numbers called?

A. Token  
B. Embedding  
C. Prompt template  
D. Metadata tag

**Correct Answer:** B

**Answer Explanation:**  
B is correct because an embedding is a dense numeric vector that represents the semantic meaning of text. Similar meanings map to nearby points in vector space.

A is incorrect because a token is a smaller text unit produced during tokenization, not the final meaning vector. C is incorrect because a prompt template is text used to instruct a model, not a numeric representation. D is incorrect because metadata tags are extra labels such as category, not the meaning vector itself.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A developer uses the model `all-MiniLM-L6-v2` from Sentence Transformers to encode a sentence.

What vector length should they expect for each sentence?

A. 10  
B. 128  
C. 384  
D. 4096

**Correct Answer:** C

**Answer Explanation:**  
C is correct because `all-MiniLM-L6-v2` maps each sentence to a 384-dimensional embedding vector in the standard lab setup.

A and B are incorrect because they are far smaller than the model's output size. D is incorrect because 4096 is not the output dimension of this model.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A teammate says: "Chroma will automatically convert our FAQ text into embeddings when we call `query()`."

Why is this statement incorrect in the manual-embedding lab setup?

A. Because Chroma only works with image files  
B. Because with `embedding_function=None`, the developer must encode text before `upsert` and `query`  
C. Because Chroma cannot store more than one row  
D. Because similarity search is not supported in Chroma

**Correct Answer:** B

**Answer Explanation:**  
B is correct because when `embedding_function=None`, Chroma stores and searches vectors that you supply. You encode documents before `upsert` and encode the user question before `query`.

A is incorrect because Chroma is used for text embeddings in this workflow. C is incorrect because Chroma collections can store many rows. D is incorrect because `collection.query()` is specifically used for similarity search.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A team stores FAQ chunks in Chroma on Monday using `all-MiniLM-L6-v2`. On Tuesday, a new developer encodes user questions with a different embedding model before calling `query()`.

What is the main problem with this approach?

A. Chroma will automatically convert the new model's vectors to the old format  
B. Distances become meaningless when stored chunks and queries use different embedding models  
C. Metadata tags stop working  
D. The collection name must change every day

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the same embedding model must encode every stored chunk and every user query. Mixing models breaks semantic distance comparisons.

A is incorrect because Chroma does not auto-convert vectors between models. C is incorrect because metadata still works, but similarity results become unreliable. D is incorrect because the collection name does not need to change daily.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A Chroma query returns these distances for three results: `1.17`, `1.39`, `1.52`.

How should you read these values?

A. Higher distance always means a better business answer  
B. The result with distance `1.17` is usually the closest semantic match among the three  
C. Distance values are random and should be ignored  
D. All three distances prove the answer is 100% correct

**Correct Answer:** B

**Answer Explanation:**  
B is correct because in Chroma's distance-based results, a smaller distance usually means the stored chunk is nearer in meaning to the query vector.

A is incorrect because higher distance means farther away, not better. C is incorrect because distances help compare ranks within the same query. D is incorrect because similarity scores are relative; they do not guarantee business correctness.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

An administrator wants to fetch the exact FAQ row with id `doc4` from a Chroma collection for debugging.

Which Chroma method is the best fit?

A. `collection.query()`  
B. `collection.get(ids=["doc4"])`  
C. `collection.upsert()`  
D. `collection.peek()` only

**Correct Answer:** B

**Answer Explanation:**  
B is correct because `get()` fetches rows by exact id, similar to `WHERE id = ...` in SQL.

A is incorrect because `query()` searches by semantic similarity, not exact id lookup. C is incorrect because `upsert()` inserts or updates rows; it does not fetch one row by id for inspection. D is incorrect because `peek()` shows a sample of rows, not a guaranteed fetch of one specific id.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A support team is building a Chroma-based FAQ retriever with manual embeddings.

Which steps are part of the correct setup?

A. Encode stored documents with an embedding model  
B. Store ids, documents, metadata, and embeddings using `upsert`  
C. Use the same embedding model for stored chunks and user queries  
D. Use a different embedding model for every query to keep results fresh  
E. Pass `query_embeddings` to `query` when `embedding_function=None`

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because document text must be converted into vectors before storage. B is correct because `upsert` writes the parallel lists of ids, documents, metadata, and embeddings. C is correct because one encoder must be used for both ingest and search. E is correct because raw text cannot be passed directly to `query` in the manual-embedding setup.

D is incorrect because changing models between storage and query breaks similarity math.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A learner inspects embedding results for these sentences:

- `"Reset password from account settings."`
- `"Recover account access after login failure."`
- `"Today's weather forecast is rainy."`

Which statements are correct?

A. The first two sentences are likely closer in meaning than either is to the weather sentence  
B. Individual numbers like `0.7` or `0.8` in a vector are easy for humans to read as plain meaning  
C. Embeddings represent text as numeric vectors  
D. Semantic search can match paraphrases even when exact keywords differ  
E. Embeddings are used only for exact keyword matching

**Correct Answers:** A, C, D

**Answer Explanation:**  
A is correct because account-recovery sentences should sit nearer in vector space than a weather sentence. C is correct because embeddings are ordered lists of numbers representing meaning. D is correct because semantic search matches by meaning, not only shared keywords.

B is incorrect because individual dimensions are hidden neural features and are not human-interpretable one by one. E is incorrect because embeddings power semantic search, which is different from exact keyword matching.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A product team is choosing between SQL lookup and vector search for different tasks.

Which matches are correct?

A. `SELECT * FROM users WHERE user_id = 7` fits exact-key lookup  
B. `"I want my money back after returning shoes"` fits semantic FAQ retrieval better than exact keyword match alone  
C. Vector databases always return "I don't know" when no relevant chunk exists  
D. Metadata tags like `category: "returns"` can help narrow search on large collections  
E. Mixing embeddings from two different models in one distance comparison is a common mistake

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A is correct because SQL equality lookup is an exact-key search pattern. B is correct because informal user language can still match a refund FAQ by meaning. D is correct because metadata filtering can improve efficiency before similarity search. E is correct because vectors from different models cannot be compared reliably.

C is incorrect because vector databases return the mathematically closest vectors even when no chunk truly answers the question.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A support bot queries a Chroma collection with: `"Can I pay with UPI?"` The collection has FAQs only about returns, shipping, and account password reset — no payment FAQ.

Which statements are correct?

A. Chroma may still return the mathematically closest chunk even if none truly answers the UPI question  
B. Rank 1 always equals the business-correct answer  
C. Improving chunk coverage is a better fix than blaming the vector database tool  
D. In a full RAG pipeline, grounding helps the LLM answer from retrieved context or admit the answer is not found  
E. Using `top-k > 1` may still surface useful related chunks in some cases

**Correct Answers:** A, C, D, E

**Answer Explanation:**  
A is correct because vector search always returns nearest vectors by math, not by business completeness. C is correct because missing payment FAQs are a data problem. D is correct because grounding limits the generator to retrieved evidence. E is correct because retrieving more than one chunk can sometimes help when Rank 1 is weak.

B is incorrect because Rank 1 is the closest vector, not guaranteed to be the correct support answer.
