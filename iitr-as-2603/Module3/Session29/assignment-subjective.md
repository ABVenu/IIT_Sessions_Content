# Subjective Assignment: Mini Support Vector Search Lab

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

An e-commerce support lead wants a **local demo** that shows how FAQ text becomes vectors, lands in Chroma, and answers informal customer questions by **meaning** rather than exact keywords. Your script will store a small knowledge base, verify it, run semantic searches, and briefly interpret one “weak” match when the collection has no perfect answer.

## Task

Create a single Python file named `support_vector_search.py` that implements the workflow below.

### Setup and data

1. Use `chromadb`, `SentenceTransformer` from `sentence_transformers`, and `pprint`.
2. Create `chromadb.PersistentClient(path="./chroma_store")`.
3. Open or create collection `support_knowledge_base` with `embedding_function=None`.
4. Store **exactly** these five records (same `id`, `text`, and `metadata`):

| id   | text | metadata |
|------|------|----------|
| doc1 | Customers can return products within 30 days of delivery. | `{"category": "returns"}` |
| doc2 | Refunds are processed within 5 to 7 business days after the return is approved. | `{"category": "returns"}` |
| doc3 | Orders above 499 rupees qualify for free shipping. | `{"category": "shipping"}` |
| doc4 | You can reset your password from the account settings page. | `{"category": "account"}` |
| doc5 | Express delivery orders usually arrive within 24 to 48 hours. | `{"category": "shipping"}` |

5. Load `SentenceTransformer("all-MiniLM-L6-v2")`.
6. Build aligned lists for `ids`, `documents`, `metadatas`, and `document_embeddings` (use `.tolist()` after `model.encode`).
7. `upsert` all five rows, then print collection name and `count()` (expect **5**).
8. Print `peek()` and the result of `get(ids=["doc4"])`.

### Semantic searches

Run **three** meaning-based queries with the **same** model. For each query, use the `n_results` shown and print rank, id, document, metadata, and distance (if present).

| # | User query | n_results |
|---|------------|-----------|
| 1 | I want to return my shoes and get my money back | 3 |
| 2 | How do I change my login password? | 2 |
| 3 | Can I pay with UPI? | 3 |

### Interpretation block (required prints)

After query 3 only, print a short block titled `--- Gap analysis ---` with **two sentences**:

- Sentence 1: State which `id` ranked first and its `category`.
- Sentence 2: Explain why rank 1 might still be a **weak business answer** even though it is the closest vector in this tiny store (hint: no payment FAQ exists).

### Code comments (minimum two)

Add inline comments explaining:

1. Why the **same** embedding model must encode stored FAQs and every user query.
2. The difference between `get()` and `query()` in one line each.

### Expected behaviour

- `./chroma_store` is created or reused on disk.
- Count after upsert is `5`.
- Query 1 should rank **doc1** or **doc2** near the top (returns/refunds).
- Query 2 should rank **doc4** first (password/account).
- Query 3 may rank shipping or returns lines first; your gap analysis should reflect missing payment content.

### Constraints

- One `.py` file only; no automatic Chroma embedding function.
- Do not hand-edit files inside `./chroma_store`.
- No metadata filtering—basic top-k search only.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor/answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

The script prepares five parallel lists, encodes all FAQ strings once with `all-MiniLM-L6-v2`, and upserts ids, documents, metadatas, and embeddings together. Verification uses `count()`, `peek()`, and `get(ids=["doc4"])` to confirm storage and exact id lookup.

Each user question is encoded with the **same** model into `query_embeddings`, then passed to `collection.query(..., n_results=...)`. Query 1 should surface returns/refund FAQs; query 2 should surface doc4; query 3 demonstrates that vector search returns the **nearest** stored vectors even when no UPI FAQ exists—learners explain that rank 1 is not always the support answer they would write.

### Complete Code

```python
import chromadb
from pprint import pprint
from sentence_transformers import SentenceTransformer


def print_query_results(query_text, results):
    print("\nQuery:", query_text)
    print("Matches:\n")
    for i in range(len(results["ids"][0])):
        print(f"Rank {i + 1}")
        print("  ID:", results["ids"][0][i])
        print("  Document:", results["documents"][0][i])
        print("  Metadata:", results["metadatas"][0][i])
        if results.get("distances"):
            print("  Distance:", results["distances"][0][i])
        print()


records = [
    {
        "id": "doc1",
        "text": "Customers can return products within 30 days of delivery.",
        "metadata": {"category": "returns"},
    },
    {
        "id": "doc2",
        "text": "Refunds are processed within 5 to 7 business days after the return is approved.",
        "metadata": {"category": "returns"},
    },
    {
        "id": "doc3",
        "text": "Orders above 499 rupees qualify for free shipping.",
        "metadata": {"category": "shipping"},
    },
    {
        "id": "doc4",
        "text": "You can reset your password from the account settings page.",
        "metadata": {"category": "account"},
    },
    {
        "id": "doc5",
        "text": "Express delivery orders usually arrive within 24 to 48 hours.",
        "metadata": {"category": "shipping"},
    },
]

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)

# Same model for stored FAQs and queries so distances stay comparable.
model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [r["id"] for r in records]
documents = [r["text"] for r in records]
metadatas = [r["metadata"] for r in records]
document_embeddings = model.encode(documents, convert_to_numpy=True).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("Collection:", collection.name)
print("Count after upsert:", collection.count())

print("\nPeek sample:")
pprint(collection.peek())

# get(): exact fetch by primary key — not meaning search.
print("\nExact get for doc4:")
pprint(collection.get(ids=["doc4"]))

searches = [
    ("I want to return my shoes and get my money back", 3),
    ("How do I change my login password?", 2),
    ("Can I pay with UPI?", 3),
]

for query_text, k in searches:
    query_embedding = model.encode([query_text], convert_to_numpy=True).tolist()
    # query(): top-k nearest vectors by meaning.
    results = collection.query(query_embeddings=query_embedding, n_results=k)
    print_query_results(query_text, results)

    if query_text == "Can I pay with UPI?":
        top_id = results["ids"][0][0]
        top_category = results["metadatas"][0][0]["category"]
        print("--- Gap analysis ---")
        print(
            f"Rank 1 is {top_id} with category '{top_category}' because it is the closest stored vector to the UPI question."
        )
        print(
            "It is still a weak business answer because this collection has no payment or UPI FAQ, so Chroma only returns the nearest available meaning, not a true UPI policy."
        )
```

### Alternative Approaches

- Result printing can use a helper function (as above) or inline loops; both are acceptable.
- Exact rank-1 id for the UPI query may vary slightly by environment, but the gap analysis should name the actual top id printed and note missing payment content.
- Learners may use `pip3` / `python3` if their system requires it.
