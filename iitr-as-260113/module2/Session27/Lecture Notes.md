# Implementing Vector Search Systems

**Session focus:** Build a minimal pipeline that **stores** document embeddings in a vector database and **queries** them for semantically similar matches.

**Learning objective:** Understand how to store and query embeddings in vector databases (using Chroma and embeddings from a local model or an API).

### What you will cover

| Theme | What you will do |
| --- | --- |
| Objective & workflow | See why vector search beats keyword-only search; follow data → embeddings → storage → query → retrieval. |
| Environment & data | Install Chroma and Sentence Transformers; structure ids, text, and metadata. |
| Embeddings & storage | Generate vectors with a pretrained model; create a collection; `upsert` and verify with `count` / `peek`. |
| Query & retrieval | Embed the user query; run similarity search; interpret ranks and distances; set **top‑k**; filter with **where**. |
| Growth | Add new documents to the same collection and query again. |

The objective of a vector search system is to retrieve semantically similar data rather than relying only on exact keyword matching.

In traditional search, if a user searches for:

> “How do I get my money back?”

the system may miss a document that says:

> “Refund policy for returned items”

because the exact words are different.

A vector search system solves this problem by converting both the stored text and the user query into embeddings (numerical vectors). Then it finds the stored items whose vectors are closest to the query vector in semantic space.

### Simple intuition

Think of vector search like this:

- **Traditional search asks:** “Do the words match?”
- **Vector search asks:** “Do the meanings match?”

This is why vector search is useful in:

- semantic search
- recommendation systems
- document retrieval
- RAG systems
- support chatbots
- FAQ matching
- product search

![Traditional keyword search vs semantic vector search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session27/session27-traditional-vs-vector-search.png)

**Let’s take one practical example and use it across all steps:**

**Use case:** E-commerce support knowledge base

Suppose an online shopping company has help documents like:

- “Products can be returned within 30 days”
- “Refunds are processed in 5–7 business days”
- “Orders above ₹499 get free delivery”
- “You can reset your password from account settings”

Now the user asks:

> “I want to send back my shoes and get a refund”

Even if the query does not exactly match any stored sentence, the vector search system should understand that this query is most related to:

- return policy
- refund process

That is the real goal of a vector search system.

## End-to-end implementation workflow

A vector search system usually follows this pipeline:

**Step 1: Data**

Start with text data such as:

- product descriptions
- support documents
- FAQs
- blog chunks
- notes
- transcripts

**Step 2: Embeddings**

Convert each text item into a numerical vector using an embedding model.

**Step 3: Storage**

Store:

- original text
- unique ID
- metadata
- embedding vector

inside a vector database.

**Step 4: Query**

When a user asks a question, convert the query text into an embedding.

**Step 5: Retrieval**

Search the vector database for the top-k nearest neighbors.

**Step 6: Interpretation**

Return the most relevant results, optionally with metadata and similarity information.

**Pipeline summary**

```text
data → embeddings → vector DB → query embedding → similarity search → top-k results
```

![End-to-end vector search pipeline](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session27/session27-vector-search-pipeline.png)

This is also the same pattern used in many RAG pipelines. Chroma supports collections for storage, add/upsert for ingestion, and query/get for retrieval; when a collection has no embedding function attached, you pass embeddings directly during both ingest and query.

## Development environment setup

For a local implementation, `Chroma` is a good choice. In Python, Chroma supports:

- an in-memory client via `chromadb.Client()`
- a persistent local client via `chromadb.PersistentClient(path=...)`
- an HTTP client when connecting to a separate Chroma server

The docs note that the in-memory client is convenient for experimentation, while `PersistentClient` stores data on disk and is intended for local development/testing.

For generating embeddings locally, Sentence Transformers is a simple option. Its docs recommend installing with `pip install -U sentence-transformers` and note Python 3.10+ as the recommended version baseline.

![Local stack: Chroma persistent client and Sentence Transformers embeddings](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session27/session27-chroma-sentence-transformers.png)

### Install commands

```bash
pip install chromadb
pip install -U sentence-transformers
```

Use a recent Python (3.10+ is recommended for Sentence Transformers). In a virtual environment, run both commands once.

### What are we going to build?

We will build a minimal vector search application that does the following:

- creates sample support documents
- generates embeddings
- stores them in Chroma
- verifies storage
- converts a user query into an embedding
- performs similarity search
- applies top-k retrieval
- applies metadata filtering
- updates the collection with new records

## Sample dataset for implementation

We will use a small dataset of support documents.

Each record will have:

- id
- document
- metadata

**Why is metadata useful?**

Metadata helps us filter results later.

Examples:

- `category = returns`
- `category = shipping`
- `category = account`

Chroma supports storing metadata with records. Metadata values can be strings, integers, floats, booleans, and arrays of those types. Both `query` and `get` support metadata filtering through the `where` parameter.

## Full working code: end-to-end implementation

```python
import chromadb
from sentence_transformers import SentenceTransformer
from pprint import pprint

# 1. Prepare sample data
records = [
    {
        "id": "doc1",
        "text": "Customers can return products within 30 days of delivery.",
        "metadata": {"category": "returns", "source": "policy"},
    },
    {
        "id": "doc2",
        "text": "Refunds are processed within 5 to 7 business days after the return is approved.",
        "metadata": {"category": "returns", "source": "policy"},
    },
    {
        "id": "doc3",
        "text": "Orders above 499 rupees qualify for free shipping.",
        "metadata": {"category": "shipping", "source": "faq"},
    },
    {
        "id": "doc4",
        "text": "You can reset your password from the account settings page.",
        "metadata": {"category": "account", "source": "help_center"},
    },
    {
        "id": "doc5",
        "text": "Express delivery orders usually arrive within 24 to 48 hours.",
        "metadata": {"category": "shipping", "source": "faq"},
    },
    {
        "id": "doc6",
        "text": "If your payment fails, try another card or use UPI.",
        "metadata": {"category": "payments", "source": "help_center"},
    },
]

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Convert documents into embeddings
documents = [record["text"] for record in records]
ids = [record["id"] for record in records]
metadatas = [record["metadata"] for record in records]

document_embeddings = model.encode(documents, convert_to_numpy=True).tolist()

# 4. Create persistent Chroma client
client = chromadb.PersistentClient(path="./chroma_store")

# We are passing embeddings ourselves,
# so we keep embedding_function=None
collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)

# 5. Store data in Chroma
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("Data inserted successfully.")

# 6. Verify stored data
print("\nTotal records in collection:", collection.count())

print("\nSample stored records:")
pprint(collection.peek())

# 7. Query: convert user query into embedding
user_query = "I want to return my shoes and get my money back"

query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()

# 8. Similarity search (Top-K retrieval)
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
)

print("\nTop 3 results for query:")
print("Query:", user_query)

for i in range(len(results["ids"][0])):
    print(f"\nRank {i + 1}")
    print("ID:", results["ids"][0][i])
    print("Document:", results["documents"][0][i])
    print("Metadata:", results["metadatas"][0][i])

    # distances may be returned depending on the include/output behavior
    if "distances" in results and results["distances"] is not None:
        print("Distance:", results["distances"][0][i])

# 9. Metadata filtering
shipping_query = "How fast will my order arrive?"

shipping_query_embedding = model.encode(
    [shipping_query], convert_to_numpy=True
).tolist()

filtered_results = collection.query(
    query_embeddings=shipping_query_embedding,
    n_results=2,
    where={"category": "shipping"},
)

print("\nFiltered results (category = shipping):")
print("Query:", shipping_query)

for i in range(len(filtered_results["ids"][0])):
    print(f"\nRank {i + 1}")
    print("ID:", filtered_results["ids"][0][i])
    print("Document:", filtered_results["documents"][0][i])
    print("Metadata:", filtered_results["metadatas"][0][i])

# 10. Update the collection with new data
new_record = {
    "id": "doc7",
    "text": "Cancelled orders are refunded to the original payment method.",
    "metadata": {"category": "payments", "source": "policy"},
}

new_embedding = model.encode([new_record["text"]], convert_to_numpy=True).tolist()

collection.upsert(
    ids=[new_record["id"]],
    documents=[new_record["text"]],
    metadatas=[new_record["metadata"]],
    embeddings=new_embedding,
)

print("\nNew record added.")
print("Updated total records in collection:", collection.count())

# 11. Query again after update
payment_query = "How will I get refund for a cancelled order?"

payment_query_embedding = model.encode(
    [payment_query], convert_to_numpy=True
).tolist()

payment_results = collection.query(
    query_embeddings=payment_query_embedding,
    n_results=2,
    where={"category": "payments"},
)

print("\nResults after update:")
print("Query:", payment_query)

for i in range(len(payment_results["ids"][0])):
    print(f"\nRank {i + 1}")
    print("ID:", payment_results["ids"][0][i])
    print("Document:", payment_results["documents"][0][i])
    print("Metadata:", payment_results["metadatas"][0][i])
```

## Explanation of the code, step by step

**Step A: Prepare sample data**

We create a small list of records.

Each record contains:

- a unique ID
- text content
- metadata

**Step B: Generate embeddings**

We load a pretrained embedding model and call:

```python
model.encode(documents, convert_to_numpy=True)
```

This converts human language into vectors.

The vector itself is not human-readable.

For example:

```text
"refund for returned item"
"money back after return"
```

will likely produce vectors that are close to each other even though the words differ.

`Sentence Transformers` exposes a simple `SentenceTransformer(...)` interface for turning text into dense embeddings.

**Step C: Initialize the vector database collection**

We create a persistent Chroma client:

```python
client = chromadb.PersistentClient(path="./chroma_store")
```

Then we create or load a collection:

```python
collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)
```

Why `embedding_function=None`?

Because we are generating embeddings ourselves using Sentence Transformers.

When a collection does not have an embedding function attached, Chroma expects you to provide embeddings directly during insertion and querying. Chroma’s client API supports `get_or_create_collection(...)`, and the query docs note that if a collection lacks an embedding function, you should pass `query_embeddings` directly.

**Step D: Store embeddings**

We insert the data using:

```python
collection.upsert(...)
```

This stores:

- ids
- documents
- metadata
- embeddings

**Why use upsert instead of add?**

Upsert is safer because it inserts new records or updates existing ones.

Chroma’s docs note that `add` inserts records and that if an ID already exists, that record is ignored rather than overwritten; for overwrite/update behavior, use `update` or `upsert`.

**Step E: Verify stored data**

We verify the collection using:

```python
collection.count()
collection.peek()
```

From the above code we can confirm:

- how many records exist
- whether documents are actually stored
- whether metadata is present

Chroma exposes convenience methods like `count()` and `peek()` for exactly this purpose.

**Step F: Convert query into embedding**

When the user types a query, we convert it into an embedding:

```python
query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()
```

Now the query and stored documents live in the same embedding space, so similarity search becomes possible.

**Step G: Execute similarity search**

We use:

```python
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
)
```

This retrieves the most similar items.

### Top-k retrieval

Here, `n_results=3` means:

return the top 3 most relevant matches

Chroma’s query API performs nearest-neighbor similarity search, and the docs note that `n_results` controls how many matches are returned; if omitted, the default is 10.

**Step H: Interpret the results**

The result object usually contains aligned arrays such as:

- ids
- documents
- metadata
- optionally distances

This means:

```python
results["ids"][0][0]
results["documents"][0][0]
results["metadatas"][0][0]
```

all refer to the same top-ranked match.

We can interpret the output like this:

- Rank 1 = most relevant
- Rank 2 = next relevant
- Rank 3 = third relevant

Chroma’s docs show query results as grouped arrays and describe query responses as ranked nearest-neighbor results.

**About distances / similarity score**

If distances are returned, they help indicate closeness under the collection’s search metric.

- smaller distance = closer meaning
- higher-ranked result = better semantic match

**Step I: Apply metadata filtering**

Now suppose the query is:

**“How fast will my order arrive?”**

We do not want payment or account documents.  
We want only shipping-related documents.

So we use:

```python
where={"category": "shipping"}
```

This combines:

- semantic similarity
- metadata filtering

This is a very important real-world feature because production systems almost never rely on vector similarity alone.

Examples:

- search only finance docs
- search only current year data
- search only a specific product category
- search only a specific user’s files

Chroma supports `where` filters in both `query` and `get`, and its metadata docs show filter patterns like:

```python
where={"page": 10}
```

**Step J: Update the vector collection**

We add a new document:

“Cancelled orders are refunded to the original payment method.”

Then we create its embedding and upsert it into the same collection.

This demonstrates that vector databases are not static. We can continue adding fresh content as the knowledge base grows.

This is exactly what happens in real systems:

- new FAQ entries are added
- new product descriptions are inserted
- new support articles are indexed
- newly uploaded files are embedded and stored

## Why top-k retrieval matters

If we return only one result:

we may miss a useful supporting document

If we return too many:

we may include noise

So top-k retrieval is a balance between:

- relevance
- diversity
- context size

### Practical choices

For most of the cases:

**k = 2 or k = 3 is enough**

For RAG systems:

**often k = 3, 5, or 10, depending on chunk size and model context window**

## Why does metadata filtering matter in real systems?

Vector search alone may retrieve semantically related but operationally irrelevant results.

### Example

Query:

“How do I get a refund?”

Possible semantically similar results:

- refund policy
- failed payment retry
- cashback offer

But if the user is currently on the returns screen, we may want to search only:

`category = returns`

So production retrieval is often:

semantic similarity + filters + ranking logic

This is a major point because many people think vector search means only “store embeddings and search nearest neighbors”.

That is incomplete.

## Alternative approach: using an API for embeddings

In the main example above, we used a local embedding model through Sentence Transformers.

Another option is to generate embeddings using an API. OpenAI’s embeddings API accepts text input and returns embedding vectors as arrays of floats; current embedding model names in the reference include `text-embedding-3-small` and `text-embedding-3-large`.

**Example Python snippet with OpenAI embeddings**

```python
from openai import OpenAI

client = OpenAI()

texts = [
    "Customers can return products within 30 days of delivery.",
    "Refunds are processed within 5 to 7 business days after the return is approved.",
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts,
)

embeddings = [item.embedding for item in response.data]

print("Number of vectors:", len(embeddings))
print("Length of first vector:", len(embeddings[0]))
```

### When to use API embeddings?

**Use API-based embeddings when:**

- you want managed infrastructure
- you want a hosted model
- you do not want to run embedding models locally

**Use local embeddings when:**

- you want low recurring cost for demos
- you want offline/local experimentation
