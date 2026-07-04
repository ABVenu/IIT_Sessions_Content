# Embeddings & Vector Search

## Context of This Session

In the **previous** session you learned **RAG Foundations** — why LLMs need an external **library**, the five-step RAG flow, and a preview of **text → embeddings** with **Ollama**. You saw that meaning can be turned into numbers before any full retrieval app exists.

This session builds on that foundation: how **embeddings** work as semantic coordinates, how **similarity scores** help you judge matches, and how **Chroma** stores and searches vectors. You will **embed sample text**, **store** it, and run a **top-k semantic search** — the retrieve step a RAG pipeline reuses.

**In this session, you will:**

- Explain **embeddings** as semantic coordinates and **interpret similarity scores**
- **Create embeddings** for sample sentences using a standard library
- **Store vectors** in **Chroma** with minimal configuration
- Run a **top-k semantic search** and inspect retrieved chunks for relevance

Loading PDFs, **chunk-size tuning**, metadata on real policies, prompt assembly, and a full end-to-end RAG script are covered in later work on the same track.

---

## Embeddings as Semantic Coordinates

RAG needs a retriever that finds the right **chunks** before the LLM writes an answer. That retriever runs on **embeddings** — not on Ctrl+F keyword matching alone.

- **Official Definition:** An **embedding** is a dense vector (ordered list of numbers) produced by a model such that texts with **similar meaning** map to **nearby** points in vector space.
- **In Simple Words:** Embeddings are **meaning coordinates** — similar sentences get similar numbers; different topics sit farther apart.
- **Real-Life Example:** On a music app, every song has a **fingerprint vector**; humming a tune creates another vector; the app finds the **closest** stored song — same idea as matching a user question to the closest FAQ.

### Vectors — Ordered Lists of Numbers

- **Official Definition:** A **vector** is an ordered list of numbers, e.g. `[x₁, x₂, …, xₙ]`, representing a point in **n-dimensional space**.
- **In Simple Words:** A fixed-length row of numbers — embeddings often use **384** or **768** numbers for text.
- **Real-Life Example:** Two sentences about **refunds** should land near each other; a sentence about **weather** should be far away.
- Real embeddings use **384+ numbers** per sentence — you store and compare those lists, not individual words.
- **Common mistake:** Mixing vectors from **different models** — distances become meaningless.

### Granularity — Sentence vs Document Chunk

| Level | What gets embedded | Typical use |
|---|---|---|
| **Sentence** | One question or utterance | User **query** |
| **Document chunk** | Short FAQ line or paragraph slice | **Stored** knowledge |

- **Important rule:** Use the **same embedding model** for every stored chunk and every user query.
- **This lab** uses **short FAQ sentences**. Later work **chunks longer documents** before storing them.

---

## Text to Vectors and Similarity Scores

You do not train embedding models in this course — you **use** them. You **do** need the pipeline and how to **read** a similarity result.

### How Text Becomes a Vector

1. **Raw text** → 2. **Tokenization** → 3. **Encoding** (embedding model) → 4. **Store or compare**.

![How text becomes embeddings — raw text is tokenized, passed through an embedding model, and stored or compared as a fixed-size vector](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session16/session16-06-text-to-embedding-pipeline.png)

- **Official Definition:** An **embedding model** maps input text to a vector capturing semantic information.
- **In Simple Words:** A **meaning printer** — text in, list of numbers out.
- **Real-Life Example:** You previewed embeddings with **Ollama** earlier. The lab below uses **Sentence Transformers** (`all-MiniLM-L6-v2`) — same idea, different library.

**Full Code — Encode Two Sentences (Preview Before the Lab):**

```python
from sentence_transformers import SentenceTransformer  # Library for local embedding models

model = SentenceTransformer("all-MiniLM-L6-v2")  # Same model used in the Chroma lab below

sentence_a = "Refunds are processed within 5 to 7 business days"  # FAQ-style stored text
sentence_b = "When will I get my money back after returning the item?"  # User-style paraphrase

vector_a = model.encode(sentence_a, convert_to_numpy=True)  # Turn sentence_a into a numeric vector
vector_b = model.encode(sentence_b, convert_to_numpy=True)  # Turn sentence_b into a numeric vector

print("Vector length:", len(vector_a))  # Should be 384 for this model
print("First five numbers:", vector_a[:5])  # Peek at the coordinate list
```

**How the code works:**

- First run downloads the model (~80 MB).
- You will batch-encode **five FAQs** and later **queries** with this **same** `model` object.

### Semantic Similarity and Reading Scores

- **Official Definition:** **Semantic similarity** measures how close two texts are in **meaning**, often via distance or angle between vectors.
- **In Simple Words:** Similar meaning → vectors sit **close** on the map.
- **Real-Life Example:** *"Reset password"* and *"recover account access"* are close; *"weather forecast"* is far from both.

In **Chroma** results, **distance** often appears — **lower usually means closer** for distance-based metrics.

| What you see | How to read it |
|---|---|
| **Rank 1, 2, 3** | Best to third-best match by vector closeness |
| **Distance** | Smaller often = nearer in meaning |
| **No "100% correct"** | Scores are **relative** — inspect **top-k** text |

### Keyword Search vs Semantic Search

| Aspect | Keyword search | Semantic search |
|---|---|---|
| **Core idea** | Exact words or SQL filters | **Meaning** via embeddings |
| **Strength** | IDs, dates, statuses | Paraphrases, informal language |
| **Best when** | `WHERE user_id = 7` | FAQs, policies, RAG retrieval |

- **They work together:** SQL for structured facts; vector search for **what the user meant** in free text.

### Simple Activity — Predict the Top Match

Before the lab **query**, read these three lines:

1. `"Refunds are processed within 5 to 7 business days after the return is approved."`
2. `"Orders above 499 rupees qualify for free shipping."`
3. `"You can reset your password from the account settings page."`

User question: *"I want to return my shoes and get my money back."* Write which line should rank **#1** and why. Check after the lab.

---

## Why Vector Databases — Chroma at a Glance

You could compare vectors in a Python loop for **five** FAQs. At **thousands** of chunks, you need a **vector database**.

- **Official Definition:** A **vector database** stores embedding vectors and supports **similarity search** — finding nearest vectors efficiently.
- **In Simple Words:** A **library catalogue sorted by meaning**, not only by spelling.
- **Real-Life Example:** SQL finds a record by an **id** (exact key). Vector search finds complaints **like** this one (nearest meaning).

![SQL exact-key lookup versus vector similarity search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session17/session17-02-sql-vs-vector-search.png)

| Tool | Role in this course |
|---|---|
| **Chroma** | **Primary tool in this lab** — collections, upsert, query |

- **Common doubt:** Chroma is **not** the embedding model. **You** encode; Chroma **stores and searches**.

### The Pipeline You Will Run in Code

1. **Prepare** — Short chunks with **id** and **metadata**.
2. **Embed documents** — `model.encode()` on each FAQ.
3. **Store in Chroma** — `upsert` id, document, metadata, embedding.
4. **Verify** — `count()` (and optional `peek()`).
5. **Embed query** — Same model on the user question.
6. **Query** — Top-k nearest vectors.
7. **Read results** — Rank, text, distance.

![Chroma lab pipeline — prepare FAQ data, embed, upsert, verify, query top-k, read results](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session18/session18-01-chroma-lab-pipeline.png)

- **Official Definition:** **Top-k retrieval** returns the **k** stored items whose vectors are nearest to the query vector.
- **In Simple Words:** *"Give me the three best matches by meaning."*
- **Same model rule:** The **identical** model must encode stored documents and every query.

---

## Chroma Terminology — Learn the Vocabulary First

| Chroma term | What it holds | SQL analogy |
|---|---|---|
| **Client** | Connection (`PersistentClient` = disk) | Database **connection** |
| **Collection** | Named bucket of records | **Table** |
| **id** | Unique key | **Primary key** |
| **document** | Human-readable text | Text **column** |
| **metadata** | Tags e.g. `category` | Extra **columns** |
| **embedding** | Meaning vector | Vector column |
| **upsert** | Insert or replace by id | Upsert by key |
| **query** | Similarity search | Nearest meaning (no plain SQL equivalent) |
| **get** | Fetch by id | `WHERE id = ...` |

- **Official Definition:** A **Chroma collection** stores **id**, **document**, **metadata**, and **embedding** for similarity search.
- **In Simple Words:** One **shelf** of labelled **folders** — text, tags, and a hidden coordinate for search.
- **`PersistentClient`** saves `./chroma_store` across runs. **`embedding_function=None`** — you pass vectors on **upsert** and **query**.

### Key Methods for the Chroma Lab

| Method | Job |
|---|---|
| `get_or_create_collection(...)` | Open or create a collection |
| `collection.upsert(...)` | Add or update rows with vectors |
| `collection.count()` | How many rows stored? |
| `collection.peek()` | Sample a few rows |
| `collection.query(...)` | Top-k search by meaning |

---

## Set Up Your Development Environment

```bash
pip install chromadb  # Chroma vector database client
pip install -U sentence-transformers  # Local embedding models
```

**How the code works:**

- Use **Python 3.10+** in a **virtual environment** when possible.
- Run all lab code from **one folder** — `PersistentClient(path="./chroma_store")` creates storage there.

```bash
mkdir vector_search_lab  # One folder for this lab
cd vector_search_lab
```

## Prepare Sample Data

Run the code blocks **in order** from here through **Retrieve Data** in one notebook (or Colab). Each block assumes variables from the previous block — e.g. **upsert** needs `records` and `collection`; **query** needs `model` and `collection` after upsert.

Good retrieval starts with **clean, small chunks** — one idea per row.

| Field | Purpose | Example |
|---|---|---|
| **id** | Unique key | `"doc2"` |
| **text** | Returned in search results | Refund FAQ sentence |
| **metadata** | Tags with the row | `{"category": "returns"}` |

Our example is an **e-commerce support knowledge base** — **five** short FAQs, each covering one clear idea.

```python
records = [  # Each dict = one Chroma row (id, text, metadata)
    {"id": "doc1", "text": "Customers can return products within 30 days of delivery.", "metadata": {"category": "returns"}},
    {"id": "doc2", "text": "Refunds are processed within 5 to 7 business days after the return is approved.", "metadata": {"category": "returns"}},
    {"id": "doc3", "text": "Orders above 499 rupees qualify for free shipping.", "metadata": {"category": "shipping"}},
    {"id": "doc4", "text": "You can reset your password from the account settings page.", "metadata": {"category": "account"}},
    {"id": "doc5", "text": "Express delivery orders usually arrive within 24 to 48 hours.", "metadata": {"category": "shipping"}},
]
```

**How the code works:**

- Each dict is one **record** — like one SQL **row**.
- Lists built from this master list must stay **index-aligned** (same index = same FAQ).

---

## Create the Chroma Client and Collection

```python
import chromadb  # Vector database client
from sentence_transformers import SentenceTransformer  # Embedding model loader
from pprint import pprint  # Readable output for peek()

client = chromadb.PersistentClient(path="./chroma_store")  # Local disk — survives restarts

collection = client.get_or_create_collection(
    name="support_knowledge_base",  # Collection name — like a table
    embedding_function=None,  # We pass embeddings manually
)

print("Collection:", collection.name)
print("Count before upsert:", collection.count())  # Expect 0 on first run
```

**How the code works:**

- **`embedding_function=None`** → you pass `embeddings=` on upsert and `query_embeddings=` on query.
- **Common mistake:** Running from different folders creates a **different** empty `chroma_store`.

---

## Add Data to Your Chroma Collection

```python
model = SentenceTransformer("all-MiniLM-L6-v2")  # Same model for store and query

documents = [record["text"] for record in records]
ids = [record["id"] for record in records]
metadatas = [record["metadata"] for record in records]

document_embeddings = model.encode(
    documents, convert_to_numpy=True
).tolist()  # Chroma expects Python lists

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("Upsert complete. Total rows:", collection.count())  # Expect 5
```

**How the code works:**

- **`model.encode(documents)`** → one vector per FAQ string.
- **`upsert`** writes all four parallel lists — index `2` in each list is the **same** row.
- If `count()` is not **5**, fix storage before any **query**.

---

## Verify What You Stored

Never demo search without confirming **add** worked.

```python
print("Total records:", collection.count())  # Expect 5

print("\nPeek sample:")
pprint(collection.peek())  # Eyeball ids, text, metadata
```

**How the code works:**

- **`count()`** answers *"Did all rows land?"*
- **`peek()`** catches empty or wrong text without writing a search query.

**get vs query (one line each):**

- **`get(ids=["doc4"])`** — exact fetch by id (debugging one row).
- **`query(query_embeddings=...)`** — search by **meaning** (what RAG retrieval uses).

![get vs query — exact id lookup versus nearest-meaning search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session18/session18-04-get-vs-query.png)

---

## Retrieve Data with Similarity Search

```python
user_query = "I want to return my shoes and get my money back"

query_embedding = model.encode(
    [user_query], convert_to_numpy=True
).tolist()  # MUST be same model as document ingest

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,  # Top-3 matches by meaning
)

print("\nQuery:", user_query)
print("Top matches:\n")

for i in range(len(results["ids"][0])):
    print(f"Rank {i + 1}")
    print("  ID:", results["ids"][0][i])
    print("  Document:", results["documents"][0][i])
    print("  Metadata:", results["metadatas"][0][i])
    if results.get("distances"):
        print("  Distance:", results["distances"][0][i])
    print()
```

**How the code works:**

- With `embedding_function=None`, you **cannot** pass raw text to `query` — only **`query_embeddings`**.
- **`n_results=3`** is **top-k** — three best matches, not the whole collection.
- **`distances`** — smaller values usually mean closer meaning.

**Optional extension:** Change `user_query` to *"How do I change my login password?"* and confirm **doc4** ranks first — same `model`, same `collection`, new query vector only.

---

## Interpret Query Results — Ranks, Distances, and One Wrong Match

| Field | Meaning |
|---|---|
| **Rank order** | Index 0 = best semantic match |
| **documents** | Text for display or a future RAG prompt |
| **metadatas** | Tags from upsert |
| **distances** | Closeness — **lower often = nearer** |

![Top-k query results with ranks and distance scores](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session18/session18-06-top-k-results.png)

- **Official Definition:** **Similarity search** ranks stored vectors by proximity to the query vector.
- **In Simple Words:** Chroma finds the closest **meaning-coordinates** to your question.

**Rank 1 ≠ always the business-correct answer** — it is the **closest vector** in the collection.

### When Ranking Looks Wrong

**User query:** *"Can I pay with UPI?"*

There is **no payment FAQ** in this collection. Rank 1 might still be **doc3** (free shipping / orders) or **doc2** (refunds) — the **nearest vector** in the store, not the answer support would write for UPI. **doc5** covers delivery timing, not payment methods — so even a delivery FAQ can rank above a missing topic if it is semantically closer than password or returns lines.

- Fix with **better chunks**, not by blaming the tool.
- **top-k > 1** helps — Rank 2 or 3 may still help.

Metadata filtering and tuning **k** are covered in later RAG work on the same track.

### Simple Activity — Results Check

For the shoe-return query: note Rank 1 **id**, **category**, and **distance**. Was your earlier prediction correct? One sentence on **get** vs **query**.

---

## What Comes Next — From Vector Search to Full RAG

| Later focus | How this session connects |
|---|---|
| **Chunking and document preparation** | Longer policies than one FAQ line — **chunk size**, **overlap**, **`source_id` / `page`**, persist with the **same Chroma path** |
| **Retrieval and grounded generation** | **top-k** text becomes prompt **context**; LLM answers from chunks |
| **Agent track** | Retrieval for memory and tools |

The workflow here is the **retriever** half of RAG — storing and searching vectors — not a full chatbot yet.

---

## Key Takeaways

- **Embeddings** are semantic coordinates; **rank** and **distance** judge matches — not exact word overlap.
- **Same model rule:** One encoder for all stored chunks and every query.
- **Chroma path:** `PersistentClient` → `get_or_create_collection(embedding_function=None)` → `encode` → `upsert` → `count`/`peek` → `query`.
- **`query`** is meaning-based search; **`get`** is exact id lookup.
- Weak or missing chunks cause weak Rank 1 — improve **data**, not only the tool.

Later work **chunks real documents**, attaches richer metadata, and persists them in a new collection using the same embed-and-upsert pattern.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `pip install chromadb` | Setup | Install Chroma client |
| `pip install -U sentence-transformers` | Setup | Install embedding library |
| `SentenceTransformer("all-MiniLM-L6-v2")` | Code | Small local embedding model |
| `model.encode(texts, convert_to_numpy=True).tolist()` | Code | Text → vectors for Chroma |
| `chromadb.PersistentClient(path="./chroma_store")` | Code | On-disk Chroma storage |
| `get_or_create_collection(..., embedding_function=None)` | Code | Open collection; you supply vectors |
| `collection.upsert` / `count` / `peek` / `query` | Code | Store, verify, top-k search |
| **Embedding / Top-k / Same model rule** | Concept | Meaning vectors; k matches; one encoder |
| **Chroma** | Tool | Vector store used in this lab |
| **get vs query** | Concept | Exact id vs meaning search |

