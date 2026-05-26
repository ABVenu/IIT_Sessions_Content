# Subjective Assignment: Build a Local Chroma FAQ Search Script

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

A small e-commerce support team wants a local search demo for six FAQ answers. Users may ask questions in their own words, so exact keyword matching is not enough. Your task is to build a single Python script that stores FAQ records in Chroma, verifies the stored data, and retrieves the nearest records for user questions.

## Task

Create a Python file named `support_faq_search.py` that implements a local vector search workflow using Chroma and Sentence Transformers.

### Functional Requirements

1. Import:
   - `chromadb`
   - `SentenceTransformer` from `sentence_transformers`
   - `pprint` from `pprint`
2. Create a persistent Chroma client using:
   - path: `./chroma_store`
3. Create or open a collection named `support_knowledge_base` with:
   - `embedding_function=None`
4. Prepare exactly six FAQ records. Each record must contain:
   - `id`
   - `text`
   - `metadata`
5. Use records from this support domain:
   - returns
   - refunds
   - shipping
   - account/password
   - payments
6. Load the embedding model:
   - `all-MiniLM-L6-v2`
7. Build separate aligned lists for:
   - `ids`
   - `documents`
   - `metadatas`
   - `document_embeddings`
8. Use `collection.upsert(...)` to store all six FAQ records.
9. Verify storage by printing:
   - collection name
   - total count after upsert
   - output of `collection.peek()`
   - output of `collection.get(ids=["doc4"])`
10. Run two meaning-based queries using the same embedding model:
    - `"I returned my shoes and want my money back"`
    - `"How can I change my login password?"`
11. For the first query, return top 3 results.
12. For the second query, return top 2 results.
13. For every returned result, print:
    - rank
    - id
    - document
    - metadata
    - distance, if present
14. Add short comments in the code explaining:
    - why the same embedding model is used for documents and queries
    - why `get()` and `query()` are different

### Expected Run Commands

```bash
pip install chromadb
pip install -U sentence-transformers
python support_faq_search.py
```

If your system uses `pip3` and `python3`, use those commands instead.

### Expected Behaviour

- The script should create or reuse the local `./chroma_store` folder.
- The count after upsert should be `6`.
- The exact fetch for `doc4` should return the password/account FAQ.
- The return/refund query should return returns or refunds records near the top.
- The password query should return the account/password record near the top.
- Lower distance values should generally represent closer matches.

### Constraints

- Write the solution in one Python file only.
- Do not use an automatic Chroma embedding function.
- Do not manually edit files inside `./chroma_store`.
- Do not add metadata filtering; only use basic top-k similarity search.
- Keep the code readable and beginner-friendly.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor or answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

A strong solution first prepares clean FAQ records, then separates them into the parallel lists required by Chroma. The script uses `SentenceTransformer("all-MiniLM-L6-v2")` to create embeddings for all FAQ documents and stores them with `collection.upsert(...)`. After storage, it verifies the collection with `count()`, `peek()`, and `get(ids=["doc4"])`.

For retrieval, the same embedding model is used to encode each user query. This is important because distances are meaningful only when stored documents and user queries are represented in the same embedding space. `get()` is used for exact id lookup, while `query()` is used for meaning-based top-k retrieval.

### Complete Expected Code

```python
import chromadb
from pprint import pprint
from sentence_transformers import SentenceTransformer


def print_query_results(query_text, results):
    print("\nQuery:", query_text)
    print("Matches:\n")

    for index in range(len(results["ids"][0])):
        print(f"Rank {index + 1}")
        print("  ID:", results["ids"][0][index])
        print("  Document:", results["documents"][0][index])
        print("  Metadata:", results["metadatas"][0][index])
        if results.get("distances"):
            print("  Distance:", results["distances"][0][index])
        print()


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


client = chromadb.PersistentClient(path="./chroma_store")

collection = client.get_or_create_collection(
    name="support_knowledge_base",
    embedding_function=None,
)

print("Collection ready:", collection.name)

model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [record["id"] for record in records]
documents = [record["text"] for record in records]
metadatas = [record["metadata"] for record in records]
document_embeddings = model.encode(
    documents,
    convert_to_numpy=True,
).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("Upsert complete.")
print("Total records now:", collection.count())

print("\nPeek at stored data:")
pprint(collection.peek())

# get() is exact id lookup. It does not search by meaning.
print("\nExact fetch for doc4:")
pprint(collection.get(ids=["doc4"]))

queries = [
    ("I returned my shoes and want my money back", 3),
    ("How can I change my login password?", 2),
]

for query_text, top_k in queries:
    # Use the same model for queries and documents so distances are comparable.
    query_embedding = model.encode(
        [query_text],
        convert_to_numpy=True,
    ).tolist()

    # query() performs meaning-based top-k vector search.
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
    )

    print_query_results(query_text, results)
```

### Alternative Approaches

- The FAQ text can use a different support domain, such as course support or travel booking, as long as exactly six clean records are stored.
- The result printing can be written without a helper function, but a helper keeps both query outputs consistent.
- Learners may use `pip3` and `python3` depending on their local Python setup.
