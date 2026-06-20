# Agent Build Workshop

## Introduction

This is the **final session of Module 3: Agentic Systems and Design** — a hands-on workshop where everything you practised across the module comes together in one build.

Across Module 3 you learned to **work with LLMs and prompts**, build **RAG** step by step (**embeddings**, **Chroma**, **chunking**, **retrieval**, **grounded generation**), and grow toward **agents** with **memory**, **tool use**, **structured JSON outputs**, and safe **API** habits. In the **previous** session you focused on **structured outputs** so agent answers parse reliably in code and UI.

Each earlier lab taught **one stage** of the pipeline. Today we close the module by building a **complete, end-to-end RAG application** — from document selection through ingest, search, and grounded answers — packaged as a script you can run and **demo to a peer**.

**What you will build in this capstone workshop:**

- **Choose** a small **document corpus** (ShopEasy policies from earlier labs, or your own short texts)
- **Ingest, chunk, embed, and store** in **Chroma**; **retrieve**, **assemble context**, and **generate grounded answers**
- **Package** as `shop_easy_rag_app.py` and **demo** with a peer-review checklist

---

## What Is a RAG Application?

A **RAG application** searches your documents first, then asks an LLM to write using **only what was found** — not from memory alone.

- **Official Definition:** **Retrieval-Augmented Generation (RAG)** combines a **retriever** (vector search over chunks) with a **generator** (LLM) so answers are **grounded** in supplied context.
- **In Simple Words:** **Open-book exam** — find the page, paste it, then write the answer.
- **Real-Life Example:** A **railway enquiry app** reads the **live display board** (retrieved chunks), not guesses from memory.

| Stage | Your job |
|---|---|
| **Select corpus** | 3–5 short policy or FAQ texts |
| **Ingest + chunk** | Split text; attach `source_id`, `page` |
| **Embed + store** | `all-MiniLM-L6-v2` → Chroma `upsert` |
| **Retrieve** | Top-k semantic search |
| **Augment** | Prompt with `=== CONTEXT ===` delimiters |
| **Generate** | Ollama or Groq — **only from context** |

- **Common mistake:** Calling the LLM without retrieval — that is a **chatbot**, not RAG.
- Every demo answer must show **which chunks** were retrieved **before** generation.

---

## Step 1 — Choose Your Document Corpus

- **Official Definition:** A **document corpus** is the set of source texts your RAG app may search and cite.
- **In Simple Words:** The **shelf of books** your assistant may read — nothing else.
- **Real-Life Example:** A **hostel** posts three PDFs — mess rules, curfew, laundry — not the entire university site.

### Option A — ShopEasy lab corpus (recommended)

| `source_id` | Topic |
|---|---|
| `returns_policy.txt` | 30-day returns, packaging, request flow |
| `shipping_policy.txt` | Delivery times, free shipping above ₹499 |
| `warranty_policy.pdf` | 12-month electronics warranty |

### Option B — Your own mini corpus

Pick **3–5 plain-text files**, each under ~1,000 characters — one idea per file, no secrets.

| Check | Why |
|---|---|
| Under ~5,000 chars total | Fast ingest; easy fact-check |
| Clear `source_id` | Clean citations |
| One not-in-corpus test question | Proves grounding (e.g. UPI) |

### Activity — Corpus map

Draw a table: **`source_id`**, **one key fact**, **sample question** — one row per document. Use it during the peer demo.

---

## Step 2 — Project Setup

```
shop_easy_rag_workshop/
├── shop_easy_rag_app.py
├── corpus/                    # optional .txt files
├── prompts/rag_system_v1.txt  # grounding rules
└── chroma_store/              # auto-created
```

```bash
pip install chromadb sentence-transformers groq ollama
ollama pull qwen2.5:0.5b   # if using local generation
```

- **Groq:** set `GROQ_API_KEY` in env or Colab Secrets.
- **Ollama:** keep the app running before you call `generate_answer`.
- Use **Python 3.10+** in a virtual environment.

### Activity — Smoke test

Run `python -c "import chromadb; from sentence_transformers import SentenceTransformer; print('OK')"`. Fix any import error before continuing.

---

## Step 3 — Build the Pipeline (Concepts Before Code)

Work through these ideas **while** you type or paste the complete script in the next section.

### Ingest and chunk

- **Official Definition:** **Chunking** splits documents into segments for embedding, often with **overlap** so boundary sentences appear whole in at least one chunk.
- **In Simple Words:** Cut a policy into **index cards** labelled with file name and page.
- **Workshop defaults:** `chunk_size=500`, `overlap=75`, metadata keys `source_id`, `page`, `chunk_index`.
- **Common mistake:** `overlap >= chunk_size` — the splitter never advances.

### Embed and store

- **Official Definition:** An **embedding** is a numeric vector representing meaning; a **vector database** finds nearest neighbours efficiently.
- **In Simple Words:** Each chunk gets **GPS coordinates for meaning**; Chroma is the map.
- **Same model rule:** Use **`all-MiniLM-L6-v2`** for stored chunks **and** every query.
- Collection: **`workshop_policy_chunks`** in `./chroma_store`. Call `build_index(..., force_reingest=True)` after corpus changes.

### Retrieve

- **Official Definition:** **Top-k retrieval** returns the **k** chunks nearest to the query embedding.
- **In Simple Words:** *"Bring me the three best paragraphs for this question."*
- **`TOP_K = 3`** default — raise only if answers miss in-corpus facts.
- **`print_retrieval_trace`** prints evidence before generation — required for demo.

### Assemble context

- **Official Definition:** **Context assembly** combines grounding rules, retrieved chunks, and the user question into one LLM input.
- **In Simple Words:** **Exam paper** — rules on top, allowed notes in the middle, question at bottom.
- Save grounding rules in **`prompts/rag_system_v1.txt`**:

```
You are a helpful ShopEasy customer support assistant.
Answer ONLY using the Context between CONTEXT START and CONTEXT END.
If the answer is not in the Context, say: I could not find this in the provided policy documents.
At the end, add a line: Sources used: (list source_id and page for chunks you used).
```

- **`=== CONTEXT START/END ===`** delimiters mark the **only evidence** the model may use.

### Grounded generation

- **Official Definition:** **Grounded generation** constrains output to supplied context, not model memory alone.
- **In Simple Words:** The model **writes after reading** pasted policy chunks.
- Set **`GENERATOR_BACKEND = "ollama"`** or **`"groq"`** — retrieval and prompt stay identical; only the last call changes.
- **Common mistake:** Passing the raw user question to `generate_answer` — that bypasses RAG.

| Backend | Setup |
|---|---|
| **Ollama** | `ollama pull qwen2.5:0.5b` + app running |
| **Groq** | `GROQ_API_KEY` + `pip install groq` |

### Informal grounding check

| Check | How |
|---|---|
| Claim in context? | Every number/rule appears in a retrieved chunk |
| Sources line? | Answer ends with **Sources used:** |
| Not in corpus? | *"Can I pay with UPI?"* → polite refusal, no invention |
| Claim map | *"30 days → returns_policy.txt"* |

---

## Complete Runnable Script — `shop_easy_rag_app.py`

Save as **one file** and run `python shop_easy_rag_app.py`. Every function maps to a pipeline stage above.

```python
# shop_easy_rag_app.py — end-to-end RAG workshop application

import os  # Paths and environment variables
import chromadb  # Vector database client
from sentence_transformers import SentenceTransformer  # Local embedding model

# --- Config ---
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"  # Same model at index and query time
COLLECTION_NAME = "workshop_policy_chunks"
CHROMA_PATH = "./chroma_store"
CORPUS_DIR = "./corpus"
TOP_K = 3
GENERATOR_BACKEND = "ollama"  # Change to "groq" for cloud
OLLAMA_MODEL = "qwen2.5:0.5b"
GROQ_MODEL = "llama-3.3-70b-versatile"

DEFAULT_GROUNDING_RULES = (
    "You are a helpful ShopEasy customer support assistant.\n"
    "Answer ONLY using the Context between CONTEXT START and CONTEXT END.\n"
    "If the answer is not in the Context, say: I could not find this in the provided policy documents.\n"
    "At the end, add a line: Sources used: (list source_id and page for chunks you used)."
)

SAMPLE_CORPUS = [
    {
        "text": (
            "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
            "Items must be in original packaging. To start a return, open Orders and tap Request Return. "
            "Our team reviews requests within 24 hours on business days."
        ),
        "metadata": {"source_id": "returns_policy.txt", "page": 0},
    },
    {
        "text": (
            "ShopEasy Shipping Policy. Standard delivery takes 3 to 5 business days. "
            "Orders above 499 rupees qualify for free shipping. Express delivery arrives within 24 to 48 hours "
            "in eligible metro cities."
        ),
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
    },
    {
        "text": (
            "ShopEasy Warranty Policy. Electronics include a 12-month manufacturer warranty from delivery date. "
            "To claim warranty, upload invoice and serial number photo in Support. Physical damage is not covered."
        ),
        "metadata": {"source_id": "warranty_policy.pdf", "page": 0},
    },
]


def load_corpus_from_files(corpus_dir=CORPUS_DIR):
    """Read every .txt file; filename becomes source_id."""
    records = []
    if not os.path.isdir(corpus_dir):
        return records
    for filename in sorted(os.listdir(corpus_dir)):
        if not filename.endswith(".txt"):
            continue
        file_path = os.path.join(corpus_dir, filename)
        with open(file_path, "r", encoding="utf-8") as handle:
            text = handle.read().strip()
        if text:
            records.append({"text": text, "metadata": {"source_id": filename, "page": 0}})
    return records


def get_corpus():
    """Prefer disk files; fall back to SAMPLE_CORPUS."""
    from_disk = load_corpus_from_files()
    return from_disk if from_disk else SAMPLE_CORPUS


def chunk_text(text, chunk_size=500, overlap=75):
    """Fixed-size character windows with overlap."""
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
    """Split records; attach metadata and stable ids for Chroma upsert."""
    all_chunks = []
    for record in corpus:
        text = record["text"]
        if not text:
            continue
        source_id = record["metadata"]["source_id"]
        page = record["metadata"]["page"]
        for chunk_index, body in enumerate(chunk_text(text, chunk_size, overlap)):
            all_chunks.append({
                "id": f"{source_id}__p{page}__c{chunk_index}",
                "text": body,
                "metadata": {"source_id": source_id, "page": page, "chunk_index": chunk_index},
            })
    return all_chunks


def build_index(embed_model, collection, force_reingest=False):
    """Chunk, embed, upsert when index empty or force_reingest=True."""
    if collection.count() > 0 and not force_reingest:
        print(f"Index ready — {collection.count()} rows in {COLLECTION_NAME}")
        return
    chunks = create_chunks_from_corpus(get_corpus())
    if not chunks:
        raise RuntimeError("No chunks to ingest — add corpus files or check SAMPLE_CORPUS")
    texts = [c["text"] for c in chunks]
    vectors = embed_model.encode(texts, convert_to_numpy=True).tolist()
    collection.upsert(
        ids=[c["id"] for c in chunks],
        documents=texts,
        metadatas=[c["metadata"] for c in chunks],
        embeddings=vectors,
    )
    print(f"Ingest complete — {collection.count()} rows in {COLLECTION_NAME}")


def load_grounding_rules(path="./prompts/rag_system_v1.txt"):
    """Load versioned rules from disk; fall back to DEFAULT_GROUNDING_RULES."""
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read().strip()
        if text:
            return text
    return DEFAULT_GROUNDING_RULES


def retrieve_chunks(user_query, collection, embed_model, top_k=TOP_K):
    """Embed query; return top-k chunks with metadata and distance."""
    query_vector = embed_model.encode([user_query], convert_to_numpy=True).tolist()
    results = collection.query(query_embeddings=query_vector, n_results=top_k)
    retrieved = []
    for i in range(len(results["ids"][0])):
        retrieved.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i] if results.get("distances") else None,
        })
    return retrieved


def print_retrieval_trace(user_query, retrieved_chunks):
    """Print evidence before generation — required for demo and audit."""
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for i, chunk in enumerate(retrieved_chunks, start=1):
        meta = chunk["metadata"]
        print(f"\nChunk {i} | id={chunk['id']}")
        print(f"  source_id: {meta.get('source_id')} | page: {meta.get('page')}")
        if chunk.get("distance") is not None:
            print(f"  distance: {chunk['distance']:.4f}")
        preview = chunk["text"][:200]
        print(f"  text: {preview}{'...' if len(chunk['text']) > 200 else ''}")


def build_rag_prompt(user_query, retrieved_chunks, grounding_rules=None):
    """Assemble rules, delimited context blocks, and user question."""
    rules = grounding_rules or load_grounding_rules()
    lines = [rules, "", "=== CONTEXT START ==="]
    for index, chunk in enumerate(retrieved_chunks, start=1):
        meta = chunk["metadata"]
        lines.append(f"[Chunk {index} | source_id={meta.get('source_id')} | page={meta.get('page')}]")
        lines.append(chunk["text"])
        lines.append("")
    lines.extend(["=== CONTEXT END ===", "", "=== QUESTION ===", user_query])
    return "\n".join(lines)


def generate_answer_ollama(rag_prompt):
    """Generate with local Ollama."""
    from ollama import chat
    response = chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": rag_prompt}])
    return response["message"]["content"]


def generate_answer_groq(rag_prompt):
    """Generate with Groq cloud API."""
    from groq import Groq
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": rag_prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content


def generate_answer(rag_prompt):
    """Route to Ollama or Groq based on GENERATOR_BACKEND."""
    if GENERATOR_BACKEND == "ollama":
        return generate_answer_ollama(rag_prompt)
    if GENERATOR_BACKEND == "groq":
        return generate_answer_groq(rag_prompt)
    raise ValueError(f"Unknown GENERATOR_BACKEND: {GENERATOR_BACKEND}")


def rag_answer(user_query, collection, embed_model, top_k=TOP_K):
    """End-to-end: retrieve → build prompt → generate."""
    retrieved = retrieve_chunks(user_query, collection, embed_model, top_k=top_k)
    prompt = build_rag_prompt(user_query, retrieved)
    answer = generate_answer(prompt)
    return {"answer": answer, "retrieved_chunks": retrieved, "prompt": prompt}


def run_interactive_demo(collection, embed_model):
    """Type questions until you enter exit or quit."""
    print("ShopEasy RAG workshop — type a question (or 'exit'):")
    while True:
        user_query = input("\nYou: ").strip()
        if user_query.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not user_query:
            continue
        result = rag_answer(user_query, collection, embed_model, top_k=TOP_K)
        print_retrieval_trace(user_query, result["retrieved_chunks"])
        print("\n--- Assistant ---")
        print(result["answer"])


def main():
    """Build index, answer sample question, start interactive demo."""
    embed_model = SentenceTransformer(EMBED_MODEL_NAME)
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=None)
    build_index(embed_model, collection, force_reingest=False)
    sample_question = "How many days do I have to return a product?"
    print("Sample question:", sample_question)
    result = rag_answer(sample_question, collection, embed_model, top_k=TOP_K)
    print_retrieval_trace(sample_question, result["retrieved_chunks"])
    print("\n--- Generated answer ---")
    print(result["answer"])
    run_interactive_demo(collection, embed_model)


if __name__ == "__main__":
    main()
```

**How the code works:**

- **`rag_answer`** wraps retrieve → prompt → generate; **`main()`** runs sample Q&A then interactive demo.

### Activity — Tune top-k and backends

Run *"How many days do I have to return a product?"* with `top_k=1` then `top_k=3`. Run *"Is delivery free on a 600 rupee order?"* with Ollama then Groq — compare **Sources used** lines.

---

## Step 4 — Test Matrix and Peer Review Demo

Run these **before** your live demo. This is your quality gate.

| Test type | Example question | Expected behaviour |
|---|---|---|
| **Direct fact** | *"How many days to return a product?"* | Cites returns; mentions **30 days** |
| **Paraphrase** | *"I want my money back for shoes"* | Semantic search still hits returns |
| **Cross-topic** | *"Is shipping free on a 600 rupee order?"* | Cites shipping; mentions **499** |
| **Not in corpus** | *"Can I pay with UPI?"* | **Refusal** — no invented policy |
| **Without RAG** | Row 1 but skip retrieval | Generic or wrong — proves why RAG matters |

For **without-RAG** contrast, call `generate_answer(f"Answer as ShopEasy support: {question}")` once and compare to `rag_answer`.

### Peer demo script

1. Show folder layout — `corpus/`, `prompts/`, `shop_easy_rag_app.py`, `chroma_store/`
2. Run `python shop_easy_rag_app.py` — sample question shows retrieval trace + answer
3. Peer asks one **in-corpus** question — show trace and answer
4. Peer asks one **not-in-corpus** question — show polite refusal
5. Explain one design choice — chunk size, `TOP_K`, or Ollama vs Groq

### Peer review checklist

| Item | Yes / No |
|---|---|
| Retrieval trace printed **before** answer | |
| Facts match retrieved chunk text | |
| **Sources used** lists correct `source_id` | |
| Not-in-corpus question **not** invented | |
| App runs from **one command** | |

### Activity — Fill the test matrix

Run all four in-corpus test types plus one not-in-corpus row. Mark **Pass** or **Fail** and note one fix (e.g. raised `TOP_K`, tightened `rag_system_v1.txt`).

**Submit:** `shop_easy_rag_app.py`, optional `rag_system_v1.txt`, one in-corpus + one not-in-corpus log, one-sentence design note.

---

## When Something Breaks

| Symptom | Fix |
|---|---|
| `collection.count()` is 0 | `build_index(..., force_reingest=True)` |
| Invented policy detail | Strengthen `rag_system_v1.txt`; check delimiters |
| "Not found" but chunk exists | Raise `TOP_K` to 4–5 |
| Groq key error | Set `GROQ_API_KEY` or switch to Ollama |
| Ollama connection error | Start Ollama app or `ollama serve` |
| Generic answer | Always call `rag_answer`, not bare `generate_answer` |

Fix **retrieval and prompt** before blaming the chat model.

---

## Key Takeaways

- **`shop_easy_rag_app.py`** runs the full pipeline: corpus → chunk → embed → store → retrieve → augment → generate.
- **Small corpora** + `source_id` metadata make peer review and grounding checks practical.
- **Delimiters** and **versioned grounding rules** tie answers to retrieved evidence; `TOP_K` and backend are config only.
- **Test matrix + peer demo** prove grounding on in-corpus and not-in-corpus questions.

This capstone build closes **Module 3** — you now have a runnable RAG app plus the agent skills (tools, memory, structured outputs) to extend it further.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Document corpus** | Concept | Source texts the RAG app may search and cite |
| `get_corpus()` | Code | Load `.txt` files or `SAMPLE_CORPUS` |
| `create_chunks_from_corpus` | Code | Split text; attach `source_id`, `page` |
| `all-MiniLM-L6-v2` | Model | Embedding model — same at index and query |
| `build_index` | Code | Chunk, embed, upsert into Chroma |
| `TOP_K` | Config | Chunks retrieved per question (default 3) |
| `retrieve_chunks` | Code | Embed query + Chroma top-k search |
| `print_retrieval_trace` | Code | Print evidence before generation |
| `build_rag_prompt` | Code | Context assembly with delimiters |
| `GENERATOR_BACKEND` | Config | `"ollama"` or `"groq"` |
| `rag_answer` | Code | End-to-end retrieve → prompt → generate |
| **Grounded generation** | Concept | Answer from retrieved context only |
| **Same model rule** | Concept | Identical embed model for storage and queries |
