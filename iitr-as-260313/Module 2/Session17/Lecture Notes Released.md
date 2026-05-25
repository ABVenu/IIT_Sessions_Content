# Introduction to Vector Databases

## Context of This Session

In the previous session, you learned how **embeddings** turn text into vectors so that similar meanings sit close together in **vector space**. You also saw why the **same embedding model** must be used for stored documents and user queries.

This session is about what happens after embeddings are created. If your app has thousands or millions of chunks, you need a system that can **store**, **index**, and **retrieve** the nearest vectors quickly.

**In this session, you will:**

- Briefly recall how **embeddings** support similarity-based retrieval.
- Understand why traditional databases are not enough for fast vector similarity search at scale.
- Define **vector databases** and their role in storing, indexing, and retrieving embeddings.
- Build intuition for **similarity search**, **top-k retrieval**, and **similarity measurement**.
- Understand why brute-force search becomes slow and how **vector indexing** plus **ANN** search help.
- Compare **exact match** search with **similarity search**.
- Prepare for the next session, where the pipeline will be implemented in code with **Chroma**.

This session is **conceptual only**. There is no Chroma setup or full live coding lab here; implementation comes next.

---

## Bridge: Embeddings and Semantic Search

Before learning vector databases, recall the workflow that brings embeddings into retrieval.

### What You Already Know

- **Embeddings** are fixed-size lists of numbers that represent the meaning of text.
- **Semantic search** finds content by meaning, not only by exact words.
- The **same embedding model** must convert both document chunks and user queries into vectors.
- If documents and queries use different models, their vectors may not live in the same meaning space.

### Semantic Search Workflow

Think of a course support bot:

1. **Store** policy PDFs and FAQs as smaller chunks.
2. **Embed documents** by converting each chunk into a vector.
3. **Embed the query** when a student asks a question.
4. **Compare vectors** to find the closest chunks.
5. **Return top matches** to the user or pass them into an LLM for a grounded answer.

![Semantic search workflow — store chunks, embed documents and the query with the same model, compare vectors, return the nearest matches for RAG](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-01-semantic-search-workflow.png)

The big question is: if step 4 must search across lakhs or millions of chunks, how can it still be fast?

### Simple Activity: Trace One Query

- Write three short chunks in your notebook: one about refunds, one about login issues, and one about hostel rules.
- Use this query: `refund for cancelled workshop`.
- Pick the chunk closest in meaning, even if exact words do not match.
- Write one sentence explaining that this human nearest-meaning step is what vector search automates with numbers.

---

## Recall the Role of Embeddings in AI Systems

**Official Definition:** An **embedding** is a dense vector representation of data, often text, produced by a trained model so that semantically similar inputs map to nearby points in a high-dimensional space.

**In Simple Words:** Embeddings are a **coordinate system for meaning**. Similar sentences receive similar coordinates.

**Real-Life Example:** "Work from home" and "remote work" may use different words, but their meaning is close. Embeddings help a system treat them as related.

![Embeddings as a meaning map — semantically similar chunks sit close together; retrieval finds the nearest neighbours to the query vector](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-04-embeddings-meaning-map.png)

### How Embeddings Enable Retrieval

- The model converts text into vectors.
- The system compares a query vector with stored document vectors.
- The closest vectors are returned as candidate answers or context.
- These returned chunks can later be passed to an LLM in a RAG-style flow.

**Common doubt:** Does the embedding understand like a human?  
No. It has learned statistical patterns from large training data. For retrieval, that is often enough when chunks, models, and metadata are chosen carefully.

---

## Limitations of Traditional Databases for Vector Data

Relational databases such as PostgreSQL and MySQL are excellent for exact structured facts. They are not designed, by default, to quickly answer: "Which five paragraphs are closest in meaning to this question?"

### Exact-Key Lookup vs Nearest-Meaning Search

| Idea | Relational / SQL style | Vector / semantic style |
|---|---|---|
| Question | "Give me `user_id = 7`" | "Which passages are like this question?" |
| Match rule | Equality on keys and filters | Closeness between vectors |
| Index use | B-tree indexes on ids, dates, statuses | Vector indexes for similarity |
| Typical strength | Orders, users, payments, statuses | Docs, chats, policies, memories |

**Official Definition:** **Exact-key lookup** retrieves rows where a column equals a specific value. **Nearest-neighbour search** retrieves vectors closest to a query vector under a similarity measure.

**In Simple Words:** SQL answers "which row has this exact ID?" Vector search answers "which chunks feel most related?"

**Real-Life Example:** Finding a train ticket by **PNR number** is exact lookup. Finding old support complaints similar to "I cannot access MFA" is nearest-meaning search.

![SQL exact-key lookup versus vector similarity search — equality on IDs and filters vs nearest meaning in embedding space](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-02-sql-vs-vector-search.png)

### Why SQL Alone Struggles at Scale for Vectors

- **High dimensionality:** One embedding can contain hundreds or thousands of numbers.
- **No ordinary nearest-meaning index:** Normal SQL indexes help with `city = 'Mumbai'`, not with "smallest angle to this 768-number vector."
- **Slow brute-force loops:** Pulling every vector into Python and comparing one by one works for demos, not for production.
- **Keyword mismatch:** A keyword search may miss "remote work" when the user types "work from home."

Extensions like **pgvector** add vector support inside PostgreSQL. Dedicated vector databases such as **Chroma**, **Pinecone**, **FAISS-backed systems**, **Qdrant**, **Weaviate**, and **Milvus** focus more directly on embedding storage and similarity search.

**Common mistake:** "We stored embeddings in a JSON column, so vector search is solved." Storage is only one part. You also need efficient similarity indexing and retrieval.

---

## Introduce Vector Databases

**Official Definition:** A **vector database** is a storage and retrieval system optimised for embedding vectors, similarity search, metadata filtering, and scalable nearest-neighbour queries.

**In Simple Words:** It is a **library catalogue sorted by meaning**, not only by alphabetical title.

**Real-Life Example:** Imagine every FAQ answer in a coaching centre is pinned on a giant meaning map. A student asks a new question; the system walks to the nearest pins instead of reading every note on the wall.

### Three Main Jobs

1. **Store:** Save vectors with original text and metadata.
2. **Index:** Organise vectors so search avoids scanning every point.
3. **Retrieve:** Given a query vector, return **top-k** nearest matches.

![A vector database’s three jobs — store embeddings with text and metadata, index for fast search, retrieve top-k nearest neighbours](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-03-vector-database-three-jobs.png)

### Example Tools at a High Level

| Tool | One-line role |
|---|---|
| **Chroma** | Lightweight vector database for learning and prototypes |
| **Pinecone** | Managed cloud vector database service |
| **pgvector** | PostgreSQL extension for vector search inside SQL systems |
| **FAISS** | Facebook AI Similarity Search library for fast vector similarity search |
| **Qdrant / Weaviate / Milvus** | Production-grade vector database options |

You do not need to memorise vendors yet. Focus on the pattern: **embed -> store -> index -> query -> retrieve top-k results**.

### Metadata Alongside Vectors

Vector databases often store more than numbers:

- Original document or chunk text
- Source file, page, URL, or ticket id
- Category, date, user id, product name, or policy year

Example: "Search support articles similar to this question, but only from the Billing category." That combines **semantic similarity** with a **metadata filter**.

---

## Understand Similarity-Based Retrieval

**Official Definition:** **Similarity-based retrieval** returns items whose embedding vectors are closest to a query embedding, rather than matching exact strings or primary keys.

**In Simple Words:** You ask, "What is closest in meaning to this question?" instead of "Which row has exactly this word?"

**Real-Life Example:** Amazon recommendations are not only exact category matches. Products with similar descriptions, usage, or behaviour signals may appear together.

### Keyword Search vs Similarity Search

- **Keyword search:** "password" must appear, or a close spelling/stem must appear.
- **Similarity search:** "I forgot my login" can match "account recovery steps" even without the word password.
- **Exact match still wins:** SQL is better for payment totals, shipped orders, exact ids, and compliance reports.

### Top-k Retrieval

**Official Definition:** **Top-k retrieval** returns the `k` best matching vectors according to similarity or distance.

**In Simple Words:** Instead of returning the whole database, the system returns the best few matches, such as top 3, top 5, or top 10.

**Real-Life Example:** Search engines show the first page of results because users need the most useful matches, not every possible match.

**Common doubt:** What if the correct answer is rank 50?  
Then improve chunking, embeddings, filters, or increase `k` carefully. Retrieval quality is tuned; it is not magic.

---

## Develop Intuition for Similarity Search in Production

Production systems repeat the same story: **embed query -> search collection -> return nearest items -> downstream application uses them**.

### Coaching Centre Notice Board Analogy

Imagine thousands of sticky notes on a wall. Notes about fees are in one area, notes about placements in another, and notes about hostel rules somewhere else.

A student asks, "Can I pay fees in instalments?" You do not read every note. You walk toward the fee cluster and read the nearest notes.

Vector search automates that "walk to the right neighbourhood" step using numbers.

### Other Useful Analogies

- **Ola/Uber nearby cabs:** The system does not rank every driver in India; it narrows to nearby drivers quickly.
- **Post office PIN codes:** Letters are sorted by region before the exact address is checked.
- **Product recommendations:** Similar products may be found by behaviour or meaning, not exact title spelling.

### Simple Activity: Human Top-k

- Write 10 short sentences on mixed topics in your notebook.
- Pick one query sentence.
- Select the **top 3** sentences closest in meaning.
- Write why your third pick may be debatable. Similar ambiguity appears when real vector results have close scores.

---

## Understand Similarity Measurement Conceptually

**Official Definition:** **Similarity measurement** quantifies how alike two vectors are, commonly through distance or angle-based measures such as **cosine similarity**.

**In Simple Words:** Distance asks "how far apart are the points?" Cosine asks "are they pointing in a similar direction?"

**Real-Life Example:** Two friends may walk in the same direction from the college gate. One may stop earlier, but the direction still says they are heading toward a similar place.

### Distance vs Angle

- **Euclidean distance:** Straight-line gap between two points.
- **Cosine similarity:** Angle-based comparison, common for text embeddings.
- **API difference:** Some tools return similarity where higher is better; some return distance where lower is better.

### Toy Code: Direction Intuition

```python
vec_refund_policy = [0.9, 0.1, 0.0]  # Create a tiny toy vector mostly about refunds.
vec_cancel_course = [0.85, 0.15, 0.0]  # Create a second toy vector pointing in a similar direction.
vec_hostel_rules = [0.1, 0.1, 0.9]  # Create a third toy vector pointing toward a different topic.

def simple_dot(a, b):  # Define a helper that gives a higher score when values align.
    return sum(x * y for x, y in zip(a, b))  # Multiply matching positions and add them.

score_near = simple_dot(vec_refund_policy, vec_cancel_course)  # Score two similar-topic vectors.
score_far = simple_dot(vec_refund_policy, vec_hostel_rules)  # Score two different-topic vectors.

print("Refund vs cancel:", score_near)  # Print the similar-topic score.
print("Refund vs hostel:", score_far)  # Print the different-topic score.
```

**How the code works:**

- Real embeddings have hundreds or thousands of dimensions; this toy example uses only 3.
- The refund and cancellation vectors align more strongly, so their score should be higher.
- Production systems use optimised similarity functions and indexes; you usually call the tool API.

---

## Understand the Need for Scalable Search

Brute force means comparing the query vector with **every** stored vector and then sorting the scores. It is accurate, but it becomes slow as data grows.

### Why Brute Force Breaks

| Collection size | Rough feel |
|---|---|
| 1,000 vectors | Fine for class demos |
| 100,000 vectors | Noticeable delay if done naively every request |
| 10,000,000 vectors | Too slow for real-time apps without indexing |

**Official Definition:** **Brute-force nearest-neighbour search** compares a query vector with every vector in a collection before selecting the top results.

**In Simple Words:** It is like reading every book in the library before choosing five useful books.

**Real-Life Example:** Finding your friend in a stadium by checking every seat one by one is possible, but using section maps is much faster.

![Brute-force compares the query to every vector; indexing and ANN skip large regions so search stays fast at millions of vectors](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-05-brute-force-vs-indexing.png)

### Big O, Linear Search, and Binary Search Intuition

- **O(n) linear search:** If there are `n` vectors, a brute-force search may compare against all `n` vectors.
- **Binary-search intuition:** Sorted/indexed structures can reduce the search area step by step instead of checking everything.
- **Vector search difference:** Vectors are high-dimensional, so vector databases use specialised indexes rather than normal sorted-list binary search.

The key intuition is simple: good indexing helps the system **skip large regions** that are unlikely to contain the best match.

### Toy Code: Brute Force Top-k

```python
stored = {  # Create a small dictionary of chunk names and toy vectors.
    "chunk_A": [1.0, 0.0],  # Store the first toy vector.
    "chunk_B": [0.9, 0.1],  # Store a vector close to the query.
    "chunk_C": [0.0, 1.0],  # Store a vector pointing elsewhere.
    "chunk_D": [0.2, 0.8],  # Store another less similar vector.
    "chunk_E": [0.95, 0.05],  # Store another close vector.
}  # End the dictionary of stored vectors.

query = [0.92, 0.08]  # Create the user question as a toy query vector.

def l2_distance(a, b):  # Define straight-line distance between two vectors.
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5  # Calculate square root of summed squared differences.

scores = []  # Create an empty list to store distance results.
for name, vector in stored.items():  # Visit every stored vector one by one.
    distance = l2_distance(query, vector)  # Compare the query with this stored vector.
    scores.append((name, distance))  # Save the chunk name and its distance.

scores.sort(key=lambda item: item[1])  # Sort by distance, where smaller means closer.
top_k = scores[:2]  # Keep the two nearest chunks.
print("Brute-force top-2:", top_k)  # Print the nearest chunks.
```

**How the code works:**

- The loop visits every entry, so this is **O(n)** per query.
- Sorting gives the nearest results, but doing this over millions of vectors is expensive.
- A vector database replaces this naked loop with indexes and ANN search.

---

## Introduce Vector Indexing

**Official Definition:** **Vector indexing** builds data structures over embeddings so nearest-neighbour queries can skip large parts of the collection.

**In Simple Words:** Instead of checking every sticky note, you build a map of neighbourhoods and start searching in the most promising area.

**Real-Life Example:** A post office sorts PIN codes by region, so it does not open every bag in India for one letter.

### What an Index Does

- Groups or connects vectors that are close in meaning.
- Guides search toward promising regions first.
- Helps avoid scanning every stored vector.
- Uses extra memory and tuning parameters to gain speed.

You do not implement these structures by hand in this course. You choose a vector database or library and use the index support it provides.

### Common Indexing Names

- **HNSW:** A graph-style ANN index used by many vector systems.
- **IVF:** A partitioning/clustering-style family of indexes.
- **FAISS:** A library that provides fast similarity search and indexing methods.

The exact math is not needed here. The important idea is that indexes organise vectors so search becomes faster than full scanning.

---

## Understand Approximate Nearest Neighbor (ANN) Search

**Official Definition:** **Approximate Nearest Neighbor (ANN) search** returns vectors that are very likely to be among the true nearest neighbours, without always guaranteeing the exact mathematical top-k, in exchange for much faster search.

**In Simple Words:** You may not always get the absolute perfect match, but you get a very good match much faster.

**Real-Life Example:** Ola shows nearby drivers quickly. It does not calculate and rank every possible driver with perfect global precision before showing results.

![Approximate nearest neighbour (ANN) search uses an index to reach very good top-k matches quickly instead of scanning the entire collection](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-06-ann-search.png)

### Speed vs Accuracy

| Approach | Accuracy | Speed at huge scale |
|---|---|---|
| Exact brute force | Perfect ranking | Slow |
| ANN with index | Usually excellent top-k | Fast |

**Common mistake:** ANN is not "wrong search." It is a practical engineering trade-off used when full scanning is too slow.

**Evaluation habit:** Measure real answer quality with real questions, not only theoretical neighbour rank.

---

## K-Means and KNN: Brief Clarification

These ideas came up as related terms, but they are not the main implementation focus here.

- **K-means:** A clustering technique that groups data points into `k` clusters.
- **KNN (K-nearest neighbours):** A method that looks at the nearest `k` points for classification or retrieval-style reasoning.
- **Connection to vector search:** They share the intuition of closeness and neighbourhoods in a space.
- **Difference:** A vector database is a production storage and retrieval system; K-means and KNN are algorithms or modelling ideas, not complete vector database products by themselves.

Keep this as vocabulary-level awareness. The full focus remains vector databases, indexing, ANN, and top-k retrieval.

---

## Understand the Similarity Search Process End to End

The full conceptual pipeline is:

```text
[Documents] -> chunk -> embed -> store in Vector DB with index
                                     ^
[User question] -> embed with same model
                                     |
                         ANN / similarity search -> top-k chunks
                                     |
                         Application uses returned text + metadata
```

![End-to-end similarity search — chunk and embed documents, store in a vector DB, embed each query with the same model, ANN search returns top-k matches for your application](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-07-end-to-end-pipeline.png)

### Step-by-Step

1. **Ingest:** Collect sources such as PDFs, tickets, web pages, or wiki pages.
2. **Chunk:** Split long files into smaller passages.
3. **Embed:** Convert each chunk into a vector using the embedding model.
4. **Upsert into vector DB:** Save vector, text, and metadata.
5. **Query time:** Embed the user question with the same model.
6. **Search:** Use similarity search or ANN to return top-k neighbours.
7. **Use results:** Display the text or pass it to an LLM as context.

**Official Definition:** **Upsert** means insert a new record or update it if the same id already exists.

**In Simple Words:** "Save or refresh this chunk" without creating duplicate copies.

### Pseudocode Pipeline

```python
chunks = [  # Create sample chunks before storing them.
    {"id": "faq_1", "text": "How to reset your password", "topic": "account"},  # Create an account FAQ chunk.
    {"id": "faq_2", "text": "Track your shipment status", "topic": "shipping"},  # Create a shipping FAQ chunk.
]  # End the sample chunk list.

for chunk in chunks:  # Process every chunk in the knowledge base.
    vector = embedding_model.encode(chunk["text"])  # Convert the chunk text into an embedding.
    vector_db.upsert(  # Save or update the chunk in the vector database.
        id=chunk["id"],  # Store a unique id for the chunk.
        embedding=vector,  # Store the embedding vector.
        document=chunk["text"],  # Store the original text.
        metadata={"topic": chunk["topic"]},  # Store metadata for filtering.
    )  # End the upsert call.

user_question = "I forgot my login password"  # Capture the user's query.
query_vector = embedding_model.encode(user_question)  # Convert the query with the same embedding model.

results = vector_db.query(  # Ask the vector database for nearest neighbours.
    embedding=query_vector,  # Search using the query vector.
    top_k=2,  # Return the two best matches.
    filter={"topic": "account"},  # Restrict results using metadata.
)  # End the query call.

for hit in results:  # Loop through the returned matches.
    print(hit.id, hit.document, hit.score)  # Print each match and its score.
```

**How the code works:**

- The offline part prepares and stores chunks.
- The online part embeds each new user question.
- `vector_db.query()` is where the vector DB handles indexing and ANN internally.
- The `filter` shows how metadata and semantic search can work together.

---

## Differentiate Exact Match vs Similarity Search

| When to use | Exact match / SQL / keyword | Similarity / vector DB |
|---|---|---|
| Data type | Structured ids, statuses, dates | Unstructured or semi-structured text |
| Question style | "status = shipped" | "something like this meaning" |
| Best for | Payments, orders, counts, compliance facts | Policies, FAQs, support chats, recommendations |
| Risk | Wrong row if key is wrong | Loosely related chunk if data is noisy |

Use them together. SQL can fetch the customer profile and order history; vector search can fetch the policy paragraph related to the customer's free-text question.

**Do not replace SQL** for exact totals, inventory counts, or legal reports. Use vector search where meaning-based retrieval is needed.

### Simple Activity: Traffic Light

- Write six user questions for a course portal or shopping app.
- Mark each question as **SQL**, **vector similarity**, or **both**.
- For any doubtful case, write one sentence explaining your reasoning.

---

## Bridge to the Next Session: From Concepts to Chroma

Today you built the mental model:

- Embeddings turn language into points on a meaning map.
- SQL is excellent for exact structured facts.
- Vector databases are built for nearest-meaning search over embeddings.
- Indexing and ANN make large-scale search practical.
- The end-to-end story is **chunk -> embed -> store -> query -> top-k -> use returned text**.

In the next session, this pipeline becomes runnable code with **Chroma**: create a collection, embed sample documents, run queries, set **top-k**, and inspect results.

---

## Key Takeaways

- **Embeddings** enable similarity-based retrieval when documents and queries use the same embedding model.
- **Traditional SQL** is strong for exact keys and structured filters, but not enough for fast nearest-meaning search over millions of high-dimensional vectors.
- A **vector database** stores, indexes, and retrieves embeddings, often with metadata filters.
- **Brute-force search** is accurate but slow at scale; **vector indexing** and **ANN** make retrieval fast enough for production.
- **Exact match** and **similarity search** complement each other in real applications.

---

## Important Commands, Libraries, and Terminologies

| Term / Tool | Type | Meaning |
|---|---|---|
| Embedding | Concept | Vector representation of text capturing semantic meaning |
| Semantic search | Concept | Retrieval by nearest meaning, not exact string match |
| Vector database | System | Store optimised for embeddings and fast similarity search |
| Similarity-based retrieval | Concept | Return items closest to a query vector |
| Top-k | Concept | Return the k best matches |
| Brute-force search | Concept | Compare the query with every stored vector |
| Big O | Concept | Way to describe how work grows as input size grows |
| O(n) | Concept | Linear work; scanning all n items |
| Vector indexing | Concept | Structures that speed up nearest-neighbour search |
| ANN | Concept | Approximate Nearest Neighbor search for fast near-optimal results |
| Cosine similarity | Concept | Similarity based on angle between vectors |
| Euclidean distance | Concept | Straight-line distance between points |
| Metadata filter | Concept | Restrict vector search by tags such as topic, date, or user id |
| Upsert | Concept | Insert or update a record by id |
| Chunking | Concept | Split long documents before embedding |
| Chroma | Tool | Vector database used in the next implementation session |
| Pinecone | Tool | Managed cloud vector database service |
| pgvector | Extension | Vector search support inside PostgreSQL |
| FAISS | Library | Facebook AI Similarity Search for fast vector search |
| HNSW / IVF | Index names | Common ANN/indexing families used by vector systems |
| K-means | Algorithm | Groups points into clusters |
| KNN | Algorithm | Uses nearest k neighbours for classification or retrieval-style reasoning |
| `embedding_model.encode()` | API pattern | Converts text to vectors |
| `vector_db.query()` | API pattern | Searches the vector DB using query vector and top_k |
