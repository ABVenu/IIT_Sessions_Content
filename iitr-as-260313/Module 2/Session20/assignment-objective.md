# Objective Assignment: RAG Architecture and Pipeline

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A ShopKart support bot is allowed to answer only from official returns, shipping, warranty, and refund policy text. A customer asks about a product recall that is not in those documents. What should the assistant do within its **knowledge boundary**?

A. Guess the recall timeline from general e-commerce knowledge  
B. Refuse or escalate because the topic is outside allowed policy sources  
C. Search the internet and summarize the latest news article  
D. Answer confidently using the warranty policy alone

**Correct Answer:** B

**Answer Explanation:**  
B is correct because a knowledge boundary limits the bot to trusted policy documents. Topics outside that boundary should be refused or escalated.

A is incorrect because general knowledge breaks the knowledge boundary. C is incorrect because external web search is outside the allowed sources. D is incorrect because warranty text does not cover an unrelated recall question.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A team built Chroma top-k search that prints the best-matching policy chunks, but no LLM writes a customer reply yet. Which statement is most accurate?

A. They already have a complete RAG assistant  
B. They have retrieval only; generation is still missing for full RAG  
C. They have generation only; retrieval is still missing  
D. They have ingestion only; retrieval and generation are both finished

**Correct Answer:** B

**Answer Explanation:**  
B is correct because vector search returns chunks, but RAG also needs a generator that produces an answer conditioned on retrieved evidence.

A is incorrect because search alone is not a complete RAG loop. C is incorrect because retrieval is already working. D is incorrect because retrieval is present, not only ingestion.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

In a minimal ShopKart RAG pipeline, which component is mainly responsible for converting policy chunks into vectors and storing them in Chroma during the offline step?

A. Ingestion  
B. Generator  
C. Prompt tokenizer  
D. Browser cache

**Correct Answer:** A

**Answer Explanation:**  
A is correct because ingestion prepares trusted text, embeds it, and loads the vectors into the searchable store.

B is incorrect because the generator writes natural-language answers after retrieval. C is incorrect because a tokenizer is not the named ingestion component in this pipeline. D is incorrect because browser cache is unrelated to policy indexing.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A learner stores the Groq API key inside a `.env` file and loads it with `load_dotenv()` before creating the Groq client. What is the main security benefit of this pattern?

A. It makes the API key visible in Git history for easier sharing  
B. It keeps the secret out of the Python source file and out of version control when `.env` is ignored  
C. It removes the need for any API key during generation  
D. It forces Chroma to encrypt all stored embeddings automatically

**Correct Answer:** B

**Answer Explanation:**  
B is correct because `.env` keeps secrets local and separate from code, especially when `.env` is listed in `.gitignore`.

A is incorrect because committing secrets to Git is unsafe. C is incorrect because Groq generation still needs a valid API key. D is incorrect because `.env` does not change Chroma encryption behaviour.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A ShopKart script creates a collection like this:

```python
collection = client.get_or_create_collection(
    name="shopkart_policy_kb",
    embedding_function=None,
)
```

Later, the learner calls `collection.query(...)` for a customer question. What must happen before the query call in this setup?

A. The customer question must be converted into a query embedding using the same embedding model used for policy indexing  
B. Chroma will automatically embed the raw text even when `embedding_function=None`  
C. The learner must delete all metadata before every query  
D. The learner must retrain the Groq Llama model locally

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `embedding_function=None` means Chroma expects manually supplied embeddings, and the same model must be used for documents and queries.

B is incorrect because automatic embedding happens only when an embedding function is configured. C is incorrect because metadata does not need to be deleted before querying. D is incorrect because the Groq model is hosted remotely and is not retrained in this lab.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A developer accidentally calls the Groq generator before running `collection.query(...)`. Why does this break grounding for ShopKart support?

A. Groq cannot generate text without a system prompt  
B. The model answers without retrieved policy evidence, so the reply is not grounded in ShopKart rules  
C. Chroma deletes the collection when generation happens first  
D. BGE embeddings become 768-dimensional when generation runs first

**Correct Answer:** B

**Answer Explanation:**  
B is correct because RAG requires retrieve-first, generate-second. Without retrieved excerpts, the model falls back to general knowledge instead of policy evidence.

A is incorrect because Groq can still generate text, but it will not be evidence-backed. C is incorrect because call order does not delete the collection. D is incorrect because embedding dimensionality does not change based on call order.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A quality analyst is checking whether semantic retrieval matched a customer's intent. Which inspection steps are appropriate right after `retrieve_policy_chunks(...)` runs?

A. Check whether Rank 1 `metadata["category"]` matches the expected policy area  
B. Read Rank 1 `text` and confirm it is relevant to the question  
C. Ignore distances completely because they are never useful  
D. Compare the customer wording with the retrieved excerpt meaning, not just exact keywords  
E. Assume Rank 1 is always business-correct without reading the text

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because category tags help confirm the policy area surfaced first. B is correct because the retrieved text must be read before trusting the answer. D is correct because semantic retrieval is about intent, not exact keyword overlap.

C is incorrect because distance values are useful for inspection even if they may vary slightly across runs. E is incorrect because Rank 1 means closest vector, not guaranteed business correctness in every edge case.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A grounded ShopKart prompt includes retrieved policy excerpts and strict answer rules. Which prompt rules directly reduce unsupported guessing?

A. "Answer using ONLY the policy excerpts below."  
B. "If excerpts do not contain enough information, say you do not have enough information in the provided policy excerpts."  
C. "Invent friendly timelines when the excerpts are incomplete."  
D. "Do not invent numbers, timelines, or eligibility rules not present in the excerpts."  
E. "Ignore the excerpts if the customer sounds upset."

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because it restricts the model to supplied evidence. B is correct because it encourages an honest insufficient-information response instead of guessing. D is correct because it blocks fabricated policy numbers and eligibility rules.

C is incorrect because inventing timelines is exactly the behaviour grounding tries to prevent. E is incorrect because customer tone must not override evidence rules.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A learner builds ShopKart RAG with `SentenceTransformer("BAAI/bge-small-en-v1.5")`, stores four policy embeddings in Chroma, and later queries with the same model. Which statements are technically correct?

A. The stored policy chunks and user queries should be embedded with the same model.  
B. This BGE small model produces 384-dimensional embeddings in this lab setup.  
C. Mixing embeddings from a different model in the same collection can make distances unreliable.  
D. Distance values must match exactly on every laptop for the same sentence.  
E. The retriever should use `model.encode(...)` for both indexing and querying.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because vector distances are meaningful only in the same embedding space. B is correct because the BGE small model used here creates 384-dimensional vectors. C is correct because mixed model outputs make similarity scores unreliable. E is correct because manual embedding is required when `embedding_function=None`.

D is incorrect because embedding models are predictive; distances can vary slightly across runs or machines even for the same sentence.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A ShopKart RAG answer sounds polite but cites a 30-day return window, while the stored returns policy says 7 calendar days for unopened items. Which failure explanations are plausible in a minimal RAG pipeline?

A. Retrieval surfaced the wrong policy chunk first  
B. Retrieval was correct, but the generator ignored or altered the excerpt  
C. The indexed policy text itself was outdated or wrong in `POLICY_RECORDS`  
D. Hallucination becomes impossible once any retrieval step exists  
E. The evidence audit should compare every number in the final answer with retrieved excerpt text

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because wrong Rank 1 retrieval can send bad evidence to the generator. B is correct because generation can still drift even when retrieval looks fine. C is correct because garbage-in produces confidently wrong grounded answers. E is correct because number-level evidence auditing is a core validation step.

D is incorrect because RAG reduces hallucination risk but does not make it impossible by design.
