# Subjective Assignment: Policy Chunking and Vector Search

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

**Reuse note:** Reused from `iitr-as-2601` Module3 Session40 with difficulty labelled Medium. The task matches this cohort’s released notes (ShopEasy corpus, fixed-size chunking, metadata, MiniLM, Chroma `policy_chunks`, semantic query). LangChain / Tesla PDF / Groq generation are intentionally out of scope for this single-file task.

---

## Scenario

ShopEasy wants a small demo: split two short policies into chunks, store them in Chroma with file labels, and answer **one** customer question using semantic search.

You do **not** need LangChain or PDF loading for this task.

## Task

Create a single Python file named `policy_chunk_demo.py`.

### Step 1 — Copy the corpus and chunking helpers

Use the corpus and two functions below **as they are** (you may paste them directly). Do not change `chunk_size` or `overlap`.

```python
sample_corpus = [
    {
        "text": (
            "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
            "Items must be in original packaging. To start a return, open Orders and tap Request Return."
        ),
        "metadata": {"source_id": "returns_policy.txt", "page": 0},
    },
    {
        "text": (
            "ShopEasy Shipping Policy. Standard delivery takes 3 to 5 business days. "
            "Orders above 499 rupees qualify for free shipping."
        ),
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
    },
]


def chunk_text(text, chunk_size=500, overlap=75):
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be larger than overlap")
    chunks = []
    start = 0
    while start < len(text):
        piece = text[start : start + chunk_size].strip()
        if piece:
            chunks.append(piece)
        start += chunk_size - overlap
    return chunks


def create_chunks_from_corpus(corpus, chunk_size=500, overlap=75):
    all_chunks = []
    for record in corpus:
        source_id = record["metadata"]["source_id"]
        page = record["metadata"]["page"]
        for chunk_index, chunk_body in enumerate(chunk_text(record["text"], chunk_size, overlap)):
            all_chunks.append({
                "id": f"{source_id}__p{page}__c{chunk_index}",
                "text": chunk_body,
                "metadata": {
                    "source_id": source_id,
                    "page": page,
                    "chunk_index": chunk_index,
                },
            })
    return all_chunks
```

After calling `create_chunks_from_corpus(sample_corpus)`, print:

- total number of chunks  
- one example `id` and its `metadata`

### Step 2 — Store chunks in Chroma

1. `PersistentClient(path="./chroma_store")`  
2. Collection name: `policy_chunks`, with `embedding_function=None`  
3. Embed all chunk texts with `SentenceTransformer("all-MiniLM-L6-v2")`  
4. `upsert` with aligned `ids`, `documents`, `metadatas`, `embeddings`  
5. Print `collection.count()`

Add **one** short comment in your code: metadata is stored for labels, but only **text** is embedded.

### Step 3 — Run one semantic search

User question:

> How many days do I have to return a product?

1. Encode the question with the **same** model used for chunks.  
2. `query` with `n_results=2`.  
3. Print Rank 1: `id`, `document`, and `metadata` (include `source_id`).

### Expected output (minimum)

- Chroma `count()` matches your chunk list length.  
- Rank 1 `source_id` should be `returns_policy.txt`.

---

## Submission Instructions

- Code all steps in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. Paste the given corpus and chunking functions.  
2. Build chunks with metadata and stable ids.  
3. Encode chunk text only; upsert into `policy_chunks`.  
4. Encode the return-window question with the same model and read Rank 1 metadata.

### Complete Code

```python
import chromadb
from sentence_transformers import SentenceTransformer

sample_corpus = [
    {
        "text": (
            "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
            "Items must be in original packaging. To start a return, open Orders and tap Request Return."
        ),
        "metadata": {"source_id": "returns_policy.txt", "page": 0},
    },
    {
        "text": (
            "ShopEasy Shipping Policy. Standard delivery takes 3 to 5 business days. "
            "Orders above 499 rupees qualify for free shipping."
        ),
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
    },
]


def chunk_text(text, chunk_size=500, overlap=75):
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be larger than overlap")
    chunks = []
    start = 0
    while start < len(text):
        piece = text[start : start + chunk_size].strip()
        if piece:
            chunks.append(piece)
        start += chunk_size - overlap
    return chunks


def create_chunks_from_corpus(corpus, chunk_size=500, overlap=75):
    all_chunks = []
    for record in corpus:
        source_id = record["metadata"]["source_id"]
        page = record["metadata"]["page"]
        for chunk_index, chunk_body in enumerate(chunk_text(record["text"], chunk_size, overlap)):
            all_chunks.append({
                "id": f"{source_id}__p{page}__c{chunk_index}",
                "text": chunk_body,
                "metadata": {
                    "source_id": source_id,
                    "page": page,
                    "chunk_index": chunk_index,
                },
            })
    return all_chunks


chunks = create_chunks_from_corpus(sample_corpus)
print("Total chunks:", len(chunks))
print("Example id:", chunks[0]["id"])
print("Example metadata:", chunks[0]["metadata"])

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(
    name="policy_chunks",
    embedding_function=None,
)

model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [c["id"] for c in chunks]
documents = [c["text"] for c in chunks]
metadatas = [c["metadata"] for c in chunks]

# Only text is embedded; metadata is stored as labels for citation.
embeddings = model.encode(documents, convert_to_numpy=True).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings,
)

print("Rows stored:", collection.count())

user_query = "How many days do I have to return a product?"
query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()
results = collection.query(query_embeddings=query_embedding, n_results=2)

print("\nQuery:", user_query)
print("Rank 1 ID:", results["ids"][0][0])
print("Rank 1 Document:", results["documents"][0][0])
print("Rank 1 Metadata:", results["metadatas"][0][0])
```

### Notes for evaluation

- Accept working code that upserts all chunks and shows `returns_policy.txt` on Rank 1 for the return question.
- Small print-format differences are fine.
- Do not require `peek`, `get`, second query, LangChain, Tesla PDF, or a written traceability paragraph.
