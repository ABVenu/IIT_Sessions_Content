# Hands-on RAG: LearnBridge Student Playbook Assistant

## What You Will Learn in This Session

In the previous part of the course, you moved from **embeddings and vector databases** through **vector search**, **introduction to RAG**, **building a full RAG pipeline**, and **evaluating and improving** retrieval quality. You practised loading knowledge, chunking text, storing vectors in ChromaDB, retrieving relevant snippets, and grounding LLM answers in real documents.

This masterclass brings those skills together in one realistic capstone. You will build a **student support assistant** for **LearnBridge Academy** — an EdTech company — that answers questions using only three official playbook policies: **attendance**, **assignment**, and **evaluation**.

By the end of this session, you will be able to:

- Download structured **JSON policy files** from the course S3 bucket into your local project in **VS Code**.
- Turn JSON sections into **searchable chunks** with metadata (`policy_type`, `section_id`).
- Build a complete **index → retrieve → generate** RAG pipeline on your laptop.
- Compare **grounded** answers with **LLM-only** answers on the same student question.
- Run a short **quality check**: tune **top-k**, test an out-of-scope question, and verify the fallback message.

---

## The LearnBridge Problem

**LearnBridge Academy** runs live cohort-based programs. Students constantly ask the support team the same questions:

- *"What is the minimum attendance to sit for the final exam?"*
- *"What happens if I submit an assignment two days late?"*
- *"How much of my grade comes from assignments versus the final evaluation?"*

Instead of copying answers from PDFs every time, LearnBridge wants a small **policy Q&A bot** that:

- Reads only from the official **student playbook** (three JSON policy files).
- Retrieves the right section before answering.
- Says **"I don't have that information."** when the playbook does not cover the topic (for example, hostel rules).

**Your job today:** Build that assistant in Python using **VS Code**, the same stack you used earlier: **OpenAI embeddings + ChromaDB + a grounded prompt**.

![Visual overview — offline preprocessing (Steps 1–5) versus runtime querying (Steps 6–10) across a multi-document RAG stack](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-01-rag-pipeline-overview.png)

---

## Module 2 RAG Skills — Quick Revision

This section is a **short checklist**, not new theory. Use it if you need a memory refresh before coding.

**Embeddings**
- **Official Definition:** Numeric vectors that represent the meaning of text so similar ideas sit close together in vector space.
- **In Simple Words:** A fingerprint of meaning — paraphrases get similar fingerprints.
- **Real-Life Example:** "Late fee" and "penalty for delay" should match even if the words differ.

**Vector database (ChromaDB)**
- **Official Definition:** A store that saves embedding vectors and returns the nearest matches to a query vector.
- **In Simple Words:** A smart filing cabinet sorted by meaning, not alphabet.
- **Real-Life Example:** You hum a tune; the app finds similar songs — not exact title match.

**RAG (Retrieval-Augmented Generation)**
- **Official Definition:** Retrieve relevant documents first, then pass them as context so the LLM generates a grounded answer.
- **In Simple Words:** Open the right notebook page, then write the answer from that page only.
- **Real-Life Example:** Exam open-book: you find the rule first, then explain it in your words.

**Retriever vs generator**
- **Retriever** = finds policy chunks.
- **Generator (LLM)** = writes the final answer from those chunks only.

![The retriever relies on embeddings and similarity math while the generator crafts natural language grounded in the retrieved snippets](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-07-retriever-generator-split.png)

**Activity:** In a text file or as a comment at the top of `learnbridge_rag.py`, write one sentence: *"If the retriever fetches the wrong policy section, the LLM answer will still sound confident but be wrong."* Keep that sentence visible while you test queries later.

---

## Policy Data on S3 — Download Links

LearnBridge stores policies as **JSON** files (structured text with sections). Each file has a `policy_type` and a list of `sections` with `heading` and `content`.

Download these three files into your project folder. They are hosted on the course S3 bucket:

| Policy | S3 URL |
|--------|--------|
| Attendance | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Masterclass/001/data/attendance_policy.json` |
| Assignment | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Masterclass/001/data/assignment_policy.json` |
| Evaluation | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Masterclass/001/data/evaluation_policy.json` |

**Common doubt:** Why JSON instead of PDF? **Answer:** JSON is easy to parse in code, keeps clear section boundaries for chunking, and matches how many companies store internal playbooks in databases. The RAG steps are the same as for PDFs — only the **loader** changes.

---

## Step 0 — Set Up VS Code and Your Project Folder

You will work locally in **Visual Studio Code**, not in Google Colab.

### Install and open VS Code

- Download **VS Code** from [https://code.visualstudio.com/](https://code.visualstudio.com/) if you do not have it.
- Install the **Python** extension (Microsoft) from the Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`).

### Create the project structure

In VS Code, use **File → Open Folder** and create this structure:

```text
learnbridge_playbook_rag/
├── policy_data/              ← JSON files will be saved here
├── chroma_playbook_db/       ← created automatically by ChromaDB
├── requirements.txt
└── learnbridge_rag.py
```

### Python virtual environment (Terminal in VS Code)

Open the integrated terminal: **Terminal → New Terminal**.

```bash
# Move into your project folder (change the path to where you created it)
cd learnbridge_playbook_rag

# Create an isolated Python environment
python3 -m venv venv

# Activate it — Mac/Linux
source venv/bin/activate

# Activate it — Windows (Command Prompt)
# venv\Scripts\activate

# Install libraries for embeddings, vector DB, and API calls
pip install openai chromadb
```

Create **`requirements.txt`** with exactly:

```text
openai
chromadb
```

### Set your OpenAI API key

- **Official Definition:** An API key is a secret token that lets your code call OpenAI services on your account.
- **In Simple Words:** Like a hostel ID card — without it, the gate will not open.
- **Real-Life Example:** Prepaid mobile recharge — no balance, no calls.

**Mac/Linux (same terminal session):**

```bash
export OPENAI_API_KEY="your-key-here"
```

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your-key-here"
```

**Activity:** Run `python -c "import os; print('Key set:', bool(os.getenv('OPENAI_API_KEY')))"`. You should see `Key set: True` before running the main script.

**Setup check:** Create `learnbridge_rag.py`, save it empty, and confirm the bottom-right of VS Code shows the Python interpreter from your `venv` folder.

---

## Step 1 — Download Policy JSON Files from S3

Run the download cell below once. It saves all three policies into `policy_data/` so you can open them in VS Code and read the rules offline.

```python
# =============================================================================
# STEP 1 — INGESTION: Download LearnBridge playbook JSON files from S3
# This is the "document loading" phase of the RAG pipeline (offline, run once).
# =============================================================================

import os          # Build folder paths relative to this script
import json        # Used in Step 2 when reading downloaded policies
import urllib.request  # Download public S3 files without installing extra packages

# Resolve the folder where learnbridge_rag.py is saved (works on any machine)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# All policy JSON files will live in policy_data/ next to the script
POLICY_DIR = os.path.join(BASE_DIR, "policy_data")
os.makedirs(POLICY_DIR, exist_ok=True)

# Map: local filename → course S3 URL (attendance, assignment, evaluation)
POLICY_URLS = {
    "attendance_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/attendance_policy.json"
    ),
    "assignment_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/assignment_policy.json"
    ),
    "evaluation_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/evaluation_policy.json"
    ),
}


def download_policy_files():
    """Download each playbook JSON from S3 into policy_data/ on your laptop."""
    for filename, url in POLICY_URLS.items():
        local_path = os.path.join(POLICY_DIR, filename)
        # urlretrieve fetches the file from the URL and saves it to local_path
        urllib.request.urlretrieve(url, local_path)
        print(f"Downloaded: {local_path}")


if __name__ == "__main__":
    download_policy_files()
```

**How the code works:**

- **`POLICY_URLS`** holds the three public S3 links from the table above.
- **`urlretrieve`** downloads each JSON file into `policy_data/`.
- After running, open `attendance_policy.json` in VS Code and confirm you see `sections` with `heading` and `content`.

**Common doubt:** Download fails with SSL or network error. **Fix:** Check internet; try opening the URL in your browser. If it opens, copy the file manually into `policy_data/` with the same filename.

**Activity:** Open each JSON file in VS Code and find one rule you did not know before (for example, the 75% attendance rule or the 20% late penalty). Note it in a comment at the top of `learnbridge_rag.py`.

---

## Step 2 — Load JSON and Build Chunks for the Knowledge Base

Each **section** in the JSON becomes one **chunk** for ChromaDB. Metadata tags help filtering later (for example, only `evaluation` policy).

```python
# =============================================================================
# STEP 2 — CHUNKING: Turn each JSON section into one searchable RAG chunk
# One section = one chunk (heading + content). Expect ~15 chunks from 3 files.
# =============================================================================

from typing import List, Dict, Any
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_DIR = os.path.join(BASE_DIR, "policy_data")


def load_policy_chunks_from_json() -> List[Dict[str, Any]]:
    """Read all JSON policies and return a flat list of chunk dicts for ChromaDB."""
    all_chunks = []

    # --- Outer loop: one iteration per policy file (attendance, assignment, evaluation) ---
    for filename in os.listdir(POLICY_DIR):
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(POLICY_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            policy = json.load(file)

        # Tags used later for metadata filtering (e.g. only "evaluation" policy)
        policy_type = policy.get("policy_type", "general")
        policy_title = policy.get("policy_title", filename)

        # --- Inner loop: each section in this file becomes one chunk ---
        for section in policy.get("sections", []):
            chunk = {
                # Stable ID so re-running upsert updates the same row, not duplicates
                "id": f"{policy_type}_{section.get('section_id', 'unknown')}",
                # Embedding + retrieval use this text (heading helps semantic match)
                "text": (
                    f"{section.get('heading', '')}. "
                    f"{section.get('content', '')}"
                ).strip(),
                # Stored alongside the vector — used for filters and debugging prints
                "metadata": {
                    "policy_type": policy_type,
                    "policy_title": policy_title,
                    "section_id": section.get("section_id", ""),
                    "heading": section.get("heading", ""),
                    "source_file": filename,
                },
            }
            all_chunks.append(chunk)

    print(f"Loaded {len(all_chunks)} chunks from JSON policies.")
    return all_chunks
```

**How the code works:**

- One JSON **section** = one **chunk** — good size for retrieval (not too long, not too short).
- **`text`** combines heading + content so queries like "late submission" still match the right paragraph.
- **`metadata.policy_type`** lets you filter to attendance-only or evaluation-only search later.

**Activity:** After `load_policy_chunks_from_json()`, print the first chunk's `id` and first 80 characters of `text`. Confirm you see `attendance_minimum_attendance` or similar.

---

## Step 3 — Full RAG Pipeline Code (`learnbridge_rag.py`)

Copy the **entire** script below into `learnbridge_rag.py`. It includes download, indexing, retrieval, generation, comparison, and a small top-k experiment.

```python
# =============================================================================
# LearnBridge Playbook RAG — Full pipeline
#
# OFFLINE (run once per policy update):
#   A. Download JSON from S3  →  B. Parse into chunks  →  C. Embed  →  D–E. Store in Chroma
#
# RUNTIME (every student question):
#   F. Retrieve top-k chunks  →  H. Build grounded prompt  →  I. LLM answer
# =============================================================================

import os
import json
import urllib.request
from typing import List, Dict, Any
import chromadb
from openai import OpenAI

# =============================================================================
# CONFIGURATION — paths, models, and S3 URLs
# =============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_DIR = os.path.join(BASE_DIR, "policy_data")           # Downloaded JSON files
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_playbook_db")   # Vector DB on disk
COLLECTION_NAME = "learnbridge_playbook"

EMBEDDING_MODEL = "text-embedding-3-small"   # Converts text → vector for search
GENERATION_MODEL = "gpt-4.1-mini"            # Writes the final student-facing answer

POLICY_URLS = {
    "attendance_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/attendance_policy.json"
    ),
    "assignment_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/assignment_policy.json"
    ),
    "evaluation_policy.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-260113/module2/Masterclass/001/data/evaluation_policy.json"
    ),
}

# Reads OPENAI_API_KEY from your terminal environment (set before running)
openai_client = OpenAI()


# =============================================================================
# PHASE 1 — OFFLINE: INGESTION (Step A)
# Load knowledge sources from S3 into policy_data/
# =============================================================================
def download_policy_files():
    """Document loader: fetch all playbook JSON files from the course S3 bucket."""
    os.makedirs(POLICY_DIR, exist_ok=True)
    for filename, url in POLICY_URLS.items():
        local_path = os.path.join(POLICY_DIR, filename)
        urllib.request.urlretrieve(url, local_path)
        print(f"Downloaded: {local_path}")


# =============================================================================
# PHASE 1 — OFFLINE: CHUNKING (Step B)
# Each JSON "section" becomes one chunk with id, text, and metadata
# =============================================================================
def load_policy_chunks_from_json() -> List[Dict[str, Any]]:
    """Parse JSON policies into a list of chunks ready for embedding."""
    all_chunks = []
    for filename in os.listdir(POLICY_DIR):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(POLICY_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            policy = json.load(file)

        policy_type = policy.get("policy_type", "general")
        policy_title = policy.get("policy_title", filename)

        for section in policy.get("sections", []):
            all_chunks.append(
                {
                    "id": f"{policy_type}_{section.get('section_id', 'unknown')}",
                    "text": (
                        f"{section.get('heading', '')}. "
                        f"{section.get('content', '')}"
                    ).strip(),
                    "metadata": {
                        "policy_type": policy_type,
                        "policy_title": policy_title,
                        "section_id": section.get("section_id", ""),
                        "heading": section.get("heading", ""),
                        "source_file": filename,
                    },
                }
            )
    print(f"Loaded {len(all_chunks)} chunks from JSON policies.")
    return all_chunks


# =============================================================================
# PHASE 1 — OFFLINE: EMBEDDINGS (Step C)
# Turn text into vectors so Chroma can measure semantic similarity
# =============================================================================
def create_embeddings(texts: List[str]) -> List[List[float]]:
    """Call OpenAI embedding API — used for both chunks (indexing) and queries (search)."""
    response = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]


# =============================================================================
# PHASE 1 — OFFLINE: VECTOR DATABASE (Step D)
# Chroma persists to disk — survives after you close VS Code
# =============================================================================
def setup_vector_database():
    """Create or reconnect to the local Chroma collection (cosine similarity)."""
    os.makedirs(CHROMA_PATH, exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},  # Compare vectors by angle, not raw distance
    )
    return collection


# =============================================================================
# PHASE 1 — OFFLINE: INDEXING (Step E)
# Store chunk text + metadata + embedding vectors in Chroma (upsert = safe re-run)
# =============================================================================
def index_policy_chunks(collection, chunks: List[Dict[str, Any]]):
    """Embed all chunks and write them into the vector database (knowledge base build)."""
    ids = [c["id"] for c in chunks]
    texts = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]

    # Batch embed all chunk texts in one API call
    embeddings = create_embeddings(texts)

    # upsert: insert new chunks or update existing ones with the same id
    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    print(f"Indexed {len(chunks)} chunks into ChromaDB.")


# =============================================================================
# PHASE 2 — RUNTIME: RETRIEVER (Step F)
# Given a student question, find the most similar playbook chunks
# =============================================================================
def retrieve_chunks(
    collection,
    query: str,
    top_k: int = 3,
    policy_type_filter: str = None,
) -> List[Dict[str, Any]]:
    """
    RETRIEVER component of RAG.
    1) Embed the question  2) Similarity search in Chroma  3) Return top_k chunks
  Optional policy_type_filter narrows search to one policy (e.g. only 'evaluation').
    """
    # Convert student question to the same vector space as stored chunks
    query_embedding = create_embeddings([query])[0]

    query_kwargs = {
        "query_embeddings": [query_embedding],
        "n_results": top_k,  # How many chunks to send to the LLM (tune for quality)
        "include": ["documents", "metadatas", "distances"],
    }

    # Metadata filter — e.g. search only inside evaluation_policy.json content
    if policy_type_filter:
        query_kwargs["where"] = {"policy_type": policy_type_filter}

    results = collection.query(**query_kwargs)

    # Package results into a simple list of dicts for the generator
    retrieved = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        retrieved.append({"text": doc, "metadata": meta, "distance": dist})
    return retrieved


# =============================================================================
# DEBUG HELPER (Step G) — Inspect what the retriever found before trusting the answer
# =============================================================================
def print_retrieved_chunks(query: str, chunks: List[Dict[str, Any]]):
    """Print retrieved chunks so you can verify retrieval quality (garbage in → garbage out)."""
    print("\n" + "=" * 72)
    print(f"Student question: {query}")
    print("=" * 72)
    for i, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {i}")
        print(f"  Policy type : {chunk['metadata'].get('policy_type')}")
        print(f"  Heading     : {chunk['metadata'].get('heading')}")
        print(f"  Distance    : {chunk['distance']:.4f}")  # Lower = closer match (cosine)
        print(f"  Text        : {chunk['text'][:200]}...")


# =============================================================================
# PHASE 2 — RUNTIME: PROMPT BUILDER (Step H)
# Inject retrieved playbook text into the LLM prompt (grounding)
# =============================================================================
def build_grounded_prompt(query: str, chunks: List[Dict[str, Any]]) -> str:
    """
    Combine retrieved excerpts + strict rules.
    Rule 2 forces a fixed fallback when the playbook has no answer (e.g. hostel curfew).
    """
    context = ""
    for i, chunk in enumerate(chunks, start=1):
        meta = chunk["metadata"]
        context += (
            f"\nPlaybook excerpt {i} | "
            f"Policy: {meta.get('policy_title')} | "
            f"Section: {meta.get('heading')}\n"
            f"{chunk['text']}\n"
        )

    prompt = f"""You are a helpful student support assistant for LearnBridge Academy.
Answer using ONLY the playbook excerpts below.
Rules:
1. Do not invent rules that are not in the excerpts.
2. If the answer is not in the excerpts, reply exactly:
   I don't have that information in the LearnBridge student playbook.
3. Use simple, friendly language suitable for students.
4. Mention numbers, penalties, and deadlines exactly as written in the excerpts.

Playbook excerpts:
{context}

Student question:
{query}

Final answer:"""
    return prompt


# =============================================================================
# PHASE 2 — RUNTIME: GENERATOR (Step I)
# LLM writes the answer using ONLY the retrieved context
# =============================================================================
def generate_grounded_answer(query: str, chunks: List[Dict[str, Any]]) -> str:
    """GENERATOR component of RAG — chat completion with grounded prompt."""
    prompt = build_grounded_prompt(query, chunks)
    response = openai_client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise LearnBridge Academy student support assistant."
                ),
            },
            {"role": "user", "content": prompt},  # Prompt already contains excerpts + question
        ],
    )
    return response.choices[0].message.content.strip()


# =============================================================================
# BASELINE COMPARISON (Step J) — Same question WITHOUT retrieval (often hallucinates)
# =============================================================================
def generate_answer_without_retrieval(query: str) -> str:
    """LLM-only answer for contrast — no playbook context injected."""
    response = openai_client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Answer from general knowledge only."
                ),
            },
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content.strip()


# =============================================================================
# END-TO-END RAG (Step K) — Retrieve → inspect → generate
# =============================================================================
def answer_with_rag(
    collection,
    query: str,
    top_k: int = 3,
    policy_type_filter: str = None,
) -> str:
    """Full RAG path: retriever + generator wired together."""
    chunks = retrieve_chunks(
        collection, query, top_k=top_k, policy_type_filter=policy_type_filter
    )
    print_retrieved_chunks(query, chunks)
    return generate_grounded_answer(query, chunks)


# =============================================================================
# TUNING LAB (Step L) — See how top_k changes retrieval breadth and answer quality
# =============================================================================
def top_k_experiment(collection, query: str):
    """Try top_k = 1, 2, 3 on the same question to feel precision vs recall trade-off."""
    print("\n" + "#" * 72)
    print("TOP-K EXPERIMENT")
    print("#" * 72)
    for k in [1, 2, 3]:
        print(f"\n--- top_k = {k} ---")
        chunks = retrieve_chunks(collection, query, top_k=k)
        answer = generate_grounded_answer(query, chunks)
        print(answer)


# =============================================================================
# MAIN — Run offline build once, then demo runtime Q&A and improvements
# =============================================================================
def main():
    print("=== LearnBridge Playbook RAG ===\n")

    # ----- OFFLINE: build the knowledge base (Steps A–E) -----
    download_policy_files()
    chunks = load_policy_chunks_from_json()
    collection = setup_vector_database()
    index_policy_chunks(collection, chunks)

    # ----- RUNTIME: test questions students might ask -----
    test_questions = [
        "What is the minimum attendance required for the final evaluation?",
        "What is the penalty if I submit an assignment 1 day late?",
        "What percentage of my grade comes from assignments?",
        "What is the hostel curfew time?",  # Out of scope — should trigger fallback (Rule 2)
    ]

    print("\n\n=== GROUNDED RAG ANSWERS ===")
    for question in test_questions:
        print("\n" + "*" * 72)
        answer = answer_with_rag(collection, question, top_k=3)
        print("\nFinal answer:\n", answer)

    # ----- Compare grounded vs LLM-only on one question -----
    print("\n\n=== COMPARISON: WITH vs WITHOUT RETRIEVAL ===")
    compare_q = "Can I resubmit an assignment if I scored 35%?"
    print(f"\nQuestion: {compare_q}")
    rag_chunks = retrieve_chunks(collection, compare_q, top_k=2)
    print("\n--- With RAG (grounded) ---")
    print(generate_grounded_answer(compare_q, rag_chunks))
    print("\n--- Without RAG (LLM only) ---")
    print(generate_answer_without_retrieval(compare_q))

    # ----- Metadata filter demo: search only evaluation policy -----
    print("\n\n=== METADATA FILTER: evaluation policy only ===")
    eval_q = "What is the passing mark for the final proctored evaluation?"
    answer_filtered = answer_with_rag(
        collection, eval_q, top_k=2, policy_type_filter="evaluation"
    )
    print("\nFiltered answer:\n", answer_filtered)

    # ----- Top-k tuning experiment -----
    print("\n\n=== TOP-K EXPERIMENT ===")
    top_k_experiment(
        collection,
        "How many days of approved leave can I take per module?",
    )


if __name__ == "__main__":
    main()
```

**How the code works:**

- **Pre-processing (run once):** download JSON → parse sections → embed → store in Chroma under `chroma_playbook_db/`.
- **Runtime (each question):** embed query → `query` top-k chunks → build prompt with excerpts → `chat.completions` for the final answer.
- **`policy_type_filter`** uses Chroma metadata `where` — narrows search to one policy when you already know the topic.
- The **hostel curfew** question tests the fallback — no hostel policy exists in the playbook.

**Common doubt:** Chroma errors after you change chunk text. **Fix:** Delete the `chroma_playbook_db` folder and run `main()` again to rebuild the index.

---

## Step 4 — Run the Assistant in VS Code

1. Save `learnbridge_rag.py`.
2. In the terminal (venv activated), run:

```bash
python learnbridge_rag.py
```

3. Watch the terminal: downloads → chunk count (expect **15** sections across 3 files) → indexed message → four test Q&A blocks.
4. For the **hostel curfew** question, confirm the answer uses the exact fallback line from the prompt.

**Activity:** Change `top_k` from `3` to `1` for the attendance question only. Re-run and note whether the answer still mentions **75%**. If it misses details, that shows why **top-k** matters.

---

## Step 5 — Improve Retrieval (15 Minutes)

Use this checklist on your own machine after the first successful run.

| Issue | What to try |
|-------|-------------|
| Answer mixes assignment and evaluation rules | Set `policy_type_filter="evaluation"` (or the right type) |
| Answer is too vague | Increase `top_k` from 1 to 3 |
| Answer includes unrelated sections | Decrease `top_k` or tighten the student question |
| Wrong numbers in answer | Check retrieved chunks — fix retrieval before blaming the LLM |
| Out-of-scope question answered confidently | Strengthen prompt rule 2; verify no irrelevant chunks retrieved |

![Four-step RAG evaluation checklist: document → chunk → answer correctness → grounding](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-04-evaluation-four-steps.png)

**Mini evaluation table:** Fill this for three questions you ask yourself:

| Student question | Correct policy type retrieved? | Answer grounded? (yes/no) |
|------------------|----------------------------------|---------------------------|
| Minimum attendance? | | |
| Late assignment penalty? | | |
| Hostel curfew? (should fallback) | | |

**Activity:** Add one **your own** question about certificate eligibility. Run `answer_with_rag` and paste the retrieved chunk headings into a comment — prove the answer came from `evaluation` policy text.

---

## Sample Student Questions for Practice

Use these during the session or for homework drill:

**Attendance**
- What counts as a live session for attendance?
- Can watching a recording within 24 hours count fully toward attendance?

**Assignment**
- What is the maximum score cap on a resubmission?
- What happens on a first plagiarism offence?

**Evaluation**
- What are the four components of the module grade weightage?
- How long is the final proctored exam?

**Out of scope (expect fallback)**
- What is the Wi-Fi password in the hostel?
- Can I get a scholarship based on sports?

---

## Key Takeaways

- A **production-style RAG assistant** loads official documents (here, JSON from S3), chunks them, embeds them, and stores them in **ChromaDB** before any student question is asked.
- The **retriever** decides which playbook excerpts the LLM sees — weak retrieval causes confident wrong answers even with a strong model.
- **Grounding** means every fact should trace to a retrieved section; your prompt must force a clear fallback when context is missing.
- **Top-k** and **metadata filters** are practical levers you can tune without rewriting the whole system.
- The same pipeline extends to **PDF loaders**, **user feedback loops**, and **agent tools** in upcoming work — only the data source and evaluation layer change.

---

## Important Commands, Libraries, and Terminologies

| Item | Meaning |
|------|---------|
| `python3 -m venv venv` | Creates an isolated Python environment for the project |
| `source venv/bin/activate` | Activates the virtual environment (Mac/Linux) |
| `pip install openai chromadb` | Installs embedding, LLM, and vector DB libraries |
| `export OPENAI_API_KEY="..."` | Sets your API key for the terminal session |
| `python learnbridge_rag.py` | Runs the full download → index → Q&A pipeline |
| `urllib.request.urlretrieve` | Downloads a file from a public URL (S3) to your laptop |
| `json.load` | Parses a JSON policy file into a Python dictionary |
| `chromadb.PersistentClient(path=...)` | Local vector database that survives after you close VS Code |
| `collection.upsert(...)` | Inserts or updates chunks + embeddings in Chroma |
| `collection.query(...)` | Similarity search — returns nearest chunks to the query embedding |
| `where={"policy_type": "evaluation"}` | Metadata filter — search only inside one policy |
| `top_k` | Number of chunks retrieved per question |
| **Embedding** | Vector representation of text meaning |
| **RAG** | Retrieve context first, then generate the answer |
| **Grounding** | Answer supported only by retrieved playbook text |
| **Hallucination** | Model states facts not present in the context |
| **Fallback response** | Fixed message when the playbook has no answer |
