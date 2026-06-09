# Subjective Assignment: ShopKart File-Based RAG Pipeline

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

ShopKart wants a support script that reads policy rules from **text files** (not hardcoded strings), chunks them, stores them in Chroma, and answers customer questions with grounded Groq replies.

Print retrieved chunks **before** each final answer so you can check whether retrieval matched the question.

---

## Setup

Create this folder layout on your laptop:

```text
shopkart_rag_lab/
├── policy_documents/
├── .env                  # GROQ_API_KEY=your-key-here
└── rag_pipeline.py
```

Inside `policy_documents/`, add these four files:

**`returns_policy.txt`**
```text
ShopKart Returns Policy. Unopened items in original packaging may be returned within 7 calendar days of delivery.
Opened or used items are not eligible unless defective or damaged on arrival.
```

**`shipping_policy.txt`**
```text
ShopKart Shipping Policy. Standard delivery takes 3 to 5 business days after dispatch.
Express delivery arrives in 1 to 2 business days in metro cities only.
Orders placed after 6 PM dispatch on the next business day.
```

**`warranty_policy.txt`**
```text
ShopKart Warranty Policy. Electronics carry a 12-month manufacturer warranty from delivery date for manufacturing defects under normal use.
Warranty does not cover physical damage, liquid exposure, or misuse.
```

**`refunds_policy.txt`**
```text
ShopKart Refund Policy. Refunds are credited within 5 to 7 business days after the returned item passes warehouse verification.
Cash-on-delivery orders are refunded to the original UPI or bank account only.
```

Install packages and run:

```bash
pip install chromadb sentence-transformers groq python-dotenv
python rag_pipeline.py
```

Use `pip3` / `python3` if needed.

---

## Task

Write **`rag_pipeline.py`** that does the following.

### What your script must do

1. **Load** all `.txt` files from `./policy_documents`.
2. **Clean** text (collapse extra spaces/newlines) and **chunk** each file into ~100-word overlapping pieces.
3. **Index** chunks in Chroma:
   - model: `BAAI/bge-small-en-v1.5`
   - path: `./chroma_store`
   - collection: `shopkart_policy_kb_v2`
   - `embedding_function=None` (you call `model.encode(...)` yourself)
4. Store simple metadata per chunk: at least **`source`** (file name) and **`category`** (`returns`, `shipping`, `warranty`, or `refunds`).
5. For each customer question below:
   - retrieve **top 2** chunks
   - print rank, category, distance, and chunk text
   - generate a grounded answer with Groq (`llama-3.1-8b-instant`)
   - use a prompt that says **answer only from excerpts** and **do not invent policy numbers**

### Customer questions to run in `main()`

1. `"I bought earbuds yesterday. The box is still sealed. How many days do I have to return them?"`
2. `"My laptop charger stopped working after 8 months of normal use. Is repair covered under warranty?"`

### Expected output

- Four policy files loaded; total chunk count **greater than 4**.
- Question 1: Rank 1 should be **returns**; answer should mention **7 days** for unopened items.
- Question 2: Rank 1 should be **warranty**; answer should mention **12-month** coverage for manufacturing defects.
- Retrieval output printed before every final answer.

### Rules

- Put `GROQ_API_KEY` in `.env`, not inside the Python file.
- Do not use Chroma's automatic embedding function.
- Do not edit files inside `./chroma_store` by hand.

---

## Submission Instructions

- Code everything in a single **`rag_pipeline.py`** file in VS Code.
- Create `policy_documents/` and `.env` locally so the script runs.
- Run the code and verify it works.
- Submit **`rag_pipeline.py`** in the code editor or answer box in the LMS.

---

## Answer Explanation

### Ideal walkthrough

1. **Offline ingestion:** Scan `policy_documents/`, read each TXT file, clean text, split into word chunks (100 words, 20 overlap), embed with BGE, and `upsert` into `shopkart_policy_kb_v2`.
2. **Online loop:** For each question, embed the query with the **same** BGE model, run `collection.query(..., n_results=2)`, print ranks, then send retrieved excerpts to Groq with strict grounding rules.
3. **Earbuds question:** Returns chunks should rank first; the answer should cite the **7 calendar day** window for unopened items.
4. **Charger question:** Warranty chunks should rank first; the answer should reference **12-month** manufacturing-defect coverage.

### Core logic (reference)

```python
import os
import re
from typing import List, Dict, Any
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
GENERATION_MODEL = "llama-3.1-8b-instant"
POLICY_FOLDER = "./policy_documents"
CHUNK_SIZE, OVERLAP = 100, 20


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\n", " ")).strip()


def infer_category(filename: str) -> str:
    name = filename.lower()
    if "return" in name:
        return "returns"
    if "shipping" in name:
        return "shipping"
    if "warranty" in name:
        return "warranty"
    if "refund" in name:
        return "refunds"
    return "general"


def load_policies(folder: str) -> List[Dict[str, Any]]:
    docs = []
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".txt"):
            continue
        with open(os.path.join(folder, fname), encoding="utf-8") as f:
            text = clean_text(f.read())
        docs.append({"text": text, "metadata": {"source": fname, "category": infer_category(fname)}})
    return docs


def chunk_words(text: str) -> List[str]:
    words = text.split()
    chunks, start = [], 0
    while start < len(words):
        end = start + CHUNK_SIZE
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start += CHUNK_SIZE - OVERLAP
    return chunks


def build_index(collection, model, folder: str) -> None:
    rows = []
    for i, doc in enumerate(load_policies(folder)):
        for j, piece in enumerate(chunk_words(doc["text"])):
            meta = dict(doc["metadata"])
            meta["chunk_index"] = j
            rows.append({
                "id": f"{meta['category']}_{i}_{j}",
                "text": piece,
                "metadata": meta,
            })
    embeddings = model.encode([r["text"] for r in rows], convert_to_numpy=True).tolist()
    collection.upsert(
        ids=[r["id"] for r in rows],
        documents=[r["text"] for r in rows],
        metadatas=[r["metadata"] for r in rows],
        embeddings=embeddings,
    )


def answer_question(client, collection, model, question: str) -> None:
    q_emb = model.encode([question], convert_to_numpy=True).tolist()
    hits = collection.query(query_embeddings=q_emb, n_results=2, include=["documents", "metadatas", "distances"])
    retrieved = [
        {"text": d, "metadata": m, "distance": dist}
        for d, m, dist in zip(hits["documents"][0], hits["metadatas"][0], hits["distances"][0])
    ]
    for rank, ch in enumerate(retrieved, 1):
        print(f"Rank {rank} | {ch['metadata']['category']} | {ch['distance']:.4f} | {ch['text'][:80]}...")
    context = "\n".join(ch["text"] for ch in retrieved)
    prompt = f"Answer ONLY from:\n{context}\n\nQuestion: {question}\nAnswer:"
    reply = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[{"role": "user", "content": prompt}],
    ).choices[0].message.content
    print("Answer:", reply)


def main():
    model = SentenceTransformer(EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path="./chroma_store")
    collection = client.get_or_create_collection("shopkart_policy_kb_v2", embedding_function=None)
    build_index(collection, model, POLICY_FOLDER)
    groq_client = Groq()
    for q in [
        "I bought earbuds yesterday. The box is still sealed. How many days do I have to return them?",
        "My laptop charger stopped working after 8 months of normal use. Is repair covered under warranty?",
    ]:
        print("\n" + "=" * 60 + f"\n{q}\n" + "=" * 60)
        answer_question(groq_client, collection, model, q)


if __name__ == "__main__":
    main()
```

### Alternative approaches

- Function names may differ (`load_all_policy_documents`, `build_knowledge_base`, etc.) as long as behaviour matches.
- `top_k=3` is acceptable if retrieval and printing still work correctly.
- Exact Groq wording may vary; policy numbers in the answer must still match retrieved text.
