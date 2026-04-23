# Subjective assignment — Vector search

## Problem statement

Build a **small HR policy search** tool in Python. You store short policy sentences in **Chroma**, create **embeddings** with **Sentence Transformers**, run **similarity search**, narrow results with a **category** filter, then **add or update** a policy and search again.

Use **local** embeddings only (`chromadb` + `sentence-transformers`). One `.py` file is enough.

---

## Tasks

1. Create a **persistent** Chroma client (e.g. `./hr_chroma_store`) and a collection with **`embedding_function=None`** (you will pass vectors yourself).

2. Invent at least **5** HR-style policy lines. Each row needs: **id**, **document** text, **metadata** with **`category`** (`"leave"` | `"benefits"` | `"conduct"`) and **`version`** (integer).

3. Embed all documents with Sentence Transformers (e.g. `all-MiniLM-L6-v2` — use the **same** model for every query). **Upsert** into Chroma with **`ids`**, **`documents`**, **`metadatas`**, **`embeddings`**.

4. Print **`collection.count()`** and one **`peek()`** (you may truncate long output).

5. **Search A:** one natural-language question; **`query`** using **`query_embeddings`**, no **`where`**, **`n_results=3`**. Print rank, id, snippet, metadata for each hit.

6. **Search B:** a different question; **`query`** with **`query_embeddings`** and **`where={"category": "..."}`** for one category only, **`n_results=2`**. Print the same kind of output.

7. **Update:** add a **new** document or **upsert** an existing id with new text; set or bump **`version`**. Run **one more filtered** **`query`** (with **`where`** on the right category and **`query_embeddings`**) so the new or updated line can show up in the results. Print the output.

---

## Submission instructions

1. Open **Visual Studio Code**, create your Python file, and install what you need (e.g. `chromadb`, `sentence-transformers`).
2. Run the script in VS Code until it works end-to-end with no errors.
3. Copy your **full** Python code and **paste it into the answer box** on the assessment platform.
4. At the **top of your code** (as comments), mention your Python version, the `pip install` commands you used, and how to run the file (e.g. `python hr_search.py`).

---

## Detailed solution (reference code)
```python
# Python 3.10+ recommended
# pip install chromadb sentence-transformers
# Run: python hr_policy_search.py

import chromadb
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
STORE_PATH = "./hr_chroma_store"
COLLECTION_NAME = "hr_policies"

records = [
    {
        "id": "doc1",
        "document": "Annual leave can be carried forward up to 10 days with manager approval.",
        "metadata": {"category": "leave", "version": 1},
    },
    {
        "id": "doc2",
        "document": "Sick leave requires a medical certificate for absences longer than two consecutive days.",
        "metadata": {"category": "leave", "version": 1},
    },
    {
        "id": "doc3",
        "document": "Health insurance enrollment window opens every April for dependent updates.",
        "metadata": {"category": "benefits", "version": 1},
    },
    {
        "id": "doc4",
        "document": "The company matches retirement contributions up to 6 percent of base salary.",
        "metadata": {"category": "benefits", "version": 1},
    },
    {
        "id": "doc5",
        "document": "Harassment complaints may be filed confidentially with People Operations.",
        "metadata": {"category": "conduct", "version": 1},
    },
]

model = SentenceTransformer(MODEL_NAME)
documents = [r["document"] for r in records]
ids = [r["id"] for r in records]
metadatas = [r["metadata"] for r in records]
document_embeddings = model.encode(documents, convert_to_numpy=True).tolist()

client = chromadb.PersistentClient(path=STORE_PATH)
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=None,
)

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=document_embeddings,
)

print("--- After ingest ---")
print("count:", collection.count())
print("peek (ids / documents / metadatas — embeddings omitted for readability):")
peeked = collection.peek()
for key in ("ids", "documents", "metadatas"):
    if key in peeked and peeked[key] is not None:
        print(key + ":", peeked[key])


def print_results(label, results):
    print(f"\n=== {label} ===")
    qids = results["ids"][0]
    qdocs = results["documents"][0]
    qmeta = results["metadatas"][0]
    for rank, (rid, text, meta) in enumerate(zip(qids, qdocs, qmeta), start=1):
        snippet = (text[:120] + "...") if text and len(text) > 120 else text
        print(f"Rank {rank} | id={rid} | snippet={snippet!r} | metadata={meta}")


# Search A — broad, top 3
query_a = "I was unwell for three days straight; what proof do I need for leave?"
q_emb_a = model.encode([query_a], convert_to_numpy=True).tolist()
res_a = collection.query(query_embeddings=q_emb_a, n_results=3)
print_results("Search A (no filter, n_results=3)", res_a)

# Search B — filtered to benefits, top 2
query_b = "When can I add my spouse to medical coverage?"
q_emb_b = model.encode([query_b], convert_to_numpy=True).tolist()
res_b = collection.query(
    query_embeddings=q_emb_b,
    n_results=2,
    where={"category": "benefits"},
)
print_results("Search B (where category=benefits, n_results=2)", res_b)

# Update — new policy document in benefits
new_record = {
    "id": "doc6",
    "document": "Dental and vision plans can be changed during open enrollment or within 30 days of a qualifying life event.",
    "metadata": {"category": "benefits", "version": 1},
}
new_emb = model.encode([new_record["document"]], convert_to_numpy=True).tolist()
collection.upsert(
    ids=[new_record["id"]],
    documents=[new_record["document"]],
    metadatas=[new_record["metadata"]],
    embeddings=new_emb,
)

print("\n--- After upsert new doc6 ---")
print("count:", collection.count())

# Search C — filtered query that should retrieve the new benefits line
query_c = "Can I switch my dental plan after my child is born?"
q_emb_c = model.encode([query_c], convert_to_numpy=True).tolist()
res_c = collection.query(
    query_embeddings=q_emb_c,
    n_results=2,
    where={"category": "benefits"},
)
print_results("Search C after update (where category=benefits, n_results=2)", res_c)
```

**Notes for graders:** Learners may use different HR text and ids; check that `embedding_function=None`, `upsert` includes `embeddings`, every `query` uses `query_embeddings`, Search A has no `where`, Search B and C use `where`, and an update step exists before Search C.
