# RAG: Retrieval & Grounded Generation

## Context of This Session

In the **previous** session you **chunked** ShopEasy policy text, attached **`source_id`** and **`page`** metadata, and **stored** rows in Chroma (`policy_chunks`) using `all-MiniLM-L6-v2`. You also ran **top-k search** and read Rank 1 metadata.

Before that, in an **earlier lab on the same track**, you learned **embeddings**, **Chroma**, and semantic search on short FAQs (`support_knowledge_base`).

Even **earlier**, you saw the **five-step RAG flow** — ingest, prepare, retrieve, augment, generate — as a concept with **Ollama**. You have since built the **prepare** side (chunk, embed, store). Here you finish **retrieve → augment → generate** in code.

**What you will learn:**

- Tune and run **top-k retrieval** on `policy_chunks`  
- Build a **context block** with labelled delimiters and source tags  
- Call **Ollama** (local) or **Groq** (cloud) to generate answers **only from context**  
- Wire **ingest → retrieve → generate** in one script  

Agent workflows and production RAG tooling are covered in **later work** on the same track.

![RAG flow — you built prepare in the previous session; this session finishes retrieve, augment, and generate with grounded answers from policy_chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-01-rag-five-steps-retrieve-generate.png)

---

## The Missing Steps — Retrieve, Augment, Generate

| Step | Name | Covered here |
|---|---|---|
| 1–2 | Ingest + Prepare | Brief **ingest** helper in the final script (or reuse existing `policy_chunks`) |
| 3 | **Retrieve** | Top-k query on Chroma |
| 4 | **Augment** | Paste chunks into prompt with **delimiters** |
| 5 | **Generate** | **Ollama** (local) or **Groq** (cloud) writes the answer |

- **Official Definition:** **Grounded generation** means the LLM answer should follow **retrieved context**, not invent facts when the library already has the answer.
- **In Simple Words:** **Search first, paste the notes, then speak** — open-book exam with rules.
- **Real-Life Example:** At a **railway enquiry counter**, the clerk reads the **display board** (retrieved chunks) before telling you the platform — not from memory alone.

**Common mistake:** Skipping grounding rules in the prompt — the model may still **sound confident** while guessing.

![Top-k retrieval — encode the query with all-MiniLM-L6-v2, query policy_chunks in Chroma, return k nearest chunks with metadata; k=3 is the lab default](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-02-top-k-retrieval.png)

---

## Top-k Retrieval — Configure Search Against Your Index

Retrieval is the **bridge** between your Chroma index and the LLM prompt.

- **Official Definition:** **Top-k retrieval** returns the **k** stored chunks whose embeddings are nearest to the query embedding.
- **In Simple Words:** *"Give me the **k** best policy paragraphs for this question."*
- **Real-Life Example:** A librarian brings **three** relevant folders, not the entire stack — enough detail without noise.

### Choosing k

| k value | Effect |
|---|---|
| **k = 1** | Fast, cheap — may miss a second relevant rule |
| **k = 3** | **Lab default** — balanced for short policies |
| **k = 5+** | More context — risk of irrelevant chunks confusing the LLM |

- **Same model rule:** Encode the query with **`all-MiniLM-L6-v2`** — the model used when chunks were stored.  
- **Index:** Use collection **`policy_chunks`** in `./chroma_store` (from the **previous** chunking lab).  
- **Common doubt:** *Should k always be high?* No — extra chunks add **noise** and **tokens**; start at **3**, tune if answers miss facts.

### Connect to Chroma and the embedding model

```python
import chromadb  # Vector database client
from sentence_transformers import SentenceTransformer  # Same encoder as prior labs

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"  # Must match the model used at index time
COLLECTION_NAME = "policy_chunks"  # Collection from the chunking lab
TOP_K = 3  # Number of chunks to retrieve per question

client = chromadb.PersistentClient(path="./chroma_store")  # Same folder as prior labs

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=None,  # You pass query vectors manually
)

embed_model = SentenceTransformer(EMBED_MODEL_NAME)  # Load once; reuse for every query
```

**How the code works:**

- Reopens the **existing** index — Chroma setup was covered in a **previous** lab.  
- **`TOP_K`** is the main knob you configure in this lesson.  
- If `collection.count()` is **0**, run the **ingest** section in the end-to-end script first.

---

## Retrieve Function — Top-k with Metadata

Package Chroma results into a clean list the prompt builder can read.

```python
def retrieve_chunks(user_query, collection, embed_model, top_k=TOP_K):
    """Embed the query and return top-k chunks with text, metadata, and distance."""
    query_vector = embed_model.encode([user_query], convert_to_numpy=True).tolist()  # Same model as storage

    results = collection.query(
        query_embeddings=query_vector,
        n_results=top_k,  # Top-k semantic search
    )

    retrieved = []  # List of dicts for prompt building
    for i in range(len(results["ids"][0])):
        retrieved.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i] if results.get("distances") else None,
        })

    return retrieved
```

**How the code works:**

- **`n_results=top_k`** — configure k here or pass a different value per call.  
- Each item keeps **`metadata`** (`source_id`, `page`) for **citations** in the final answer.  
- **Lower distance** usually means **closer meaning** — same reading as the FAQ lab.

### Simple Activity — Tune Top-k

Run `retrieve_chunks` on *"How many days do I have to return a product?"* with **k = 1**, then **k = 3**. Note which **`source_id`** values appear. One sentence: would **k = 1** ever miss the shipping policy for a mixed question?

---

## Context Assembly — Delimiters and Source Labels

Raw chunk text pasted blindly confuses the LLM. **Context assembly** wraps retrieved text in a **clear block** with **boundaries** and **labels**.

- **Official Definition:** **Context assembly** (prompt augmentation) combines retrieved chunks, formatting rules, and the user question into one LLM input.
- **In Simple Words:** Build the **exam paper** — instructions at top, **only allowed notes** in the middle, question at bottom.
- **Real-Life Example:** A **court brief** separates *"Exhibit A"*, *"Exhibit B"* with headers — the judge knows which document each line came from.

### Delimiter pattern for this lab

```
=== INSTRUCTIONS ===
(grounding rules)

=== CONTEXT START ===
[Chunk 1 | source_id=... | page=...]
(chunk text)

[Chunk 2 | ...]
...
=== CONTEXT END ===

=== QUESTION ===
(user question)
```

- **Why delimiters:** Models parse **sections** more reliably than one long blob.  
- **Why source labels:** Enables **informal citations** — *"According to returns_policy.txt…"*  
- **Common mistake:** Dumping chunks **without** rules — the model treats them as optional background.

![Context assembly with delimiters — instructions at top, labelled chunks with source_id and page between CONTEXT START and CONTEXT END, question at bottom](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-03-context-assembly-delimiters.png)

---

## Build the Prompt — Full Function

```python
def build_rag_prompt(user_query, retrieved_chunks):
    """Assemble retrieved chunks into a grounded prompt with clear delimiters."""
    lines = [
        "You are a helpful ShopEasy customer support assistant.",
        "Answer ONLY using the Context between CONTEXT START and CONTEXT END.",
        "If the answer is not in the Context, say: I could not find this in the provided policy documents.",
        "At the end, add a line: Sources used: (list source_id and page for chunks you used).",
        "",
        "=== CONTEXT START ===",
    ]

    for index, chunk in enumerate(retrieved_chunks, start=1):
        meta = chunk["metadata"]  # Dict with source_id, page, chunk_index
        source_id = meta.get("source_id", "unknown")
        page = meta.get("page", "unknown")
        lines.append(f"[Chunk {index} | source_id={source_id} | page={page}]")
        lines.append(chunk["text"])
        lines.append("")

    lines.extend([
        "=== CONTEXT END ===",
        "",
        "=== QUESTION ===",
        user_query,
    ])

    return "\n".join(lines)  # Single string for the LLM
```

**How the code works:**

- **Grounding rules** at the top reduce hallucination when context is missing.  
- Each chunk is **numbered** and tagged with **`source_id`** / **`page`** from Chroma metadata.  
- **`=== ... ===`** delimiters mark the **allowed evidence** block.  
- The **Sources used** instruction sets up the **informal grounding check** in the model reply.

![RAG pipeline in code — retrieve_chunks, build_rag_prompt, then generate_answer; only GENERATOR_BACKEND switches between Ollama and Groq](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-04-rag-pipeline-code.png)

---

## Grounded Generation — Ollama or Groq

The **generator** step sends your augmented prompt to an LLM. On this track you already used **Ollama** locally and **Groq** in the cloud — **both work for RAG**. Retrieval and prompt building stay **identical**; only the **last call** changes.

- **Official Definition:** **Grounded generation** produces natural-language output constrained by supplied context rather than model memory alone.
- **In Simple Words:** The model **writes the answer** after reading your pasted policy chunks.
- **Real-Life Example:** You **dictate** an answer after reading three WhatsApp policy forwards — not from what you memorised last year.

### Pick your generator backend

| Backend | Best for | Setup |
|---|---|---|
| **Ollama** | Local laptop, privacy, offline practice | `ollama pull qwen2.5:0.5b` + Ollama app running |
| **Groq** | Colab, weak laptop, faster large models | `GROQ_API_KEY` in env / Colab Secrets + `pip install groq` |

- **Retrieval is unchanged** — always Chroma + `all-MiniLM-L6-v2`.  
- **Prompt is unchanged** — same `build_rag_prompt` output for both backends.  
- **Try both** on the same question — answers should be similarly grounded; wording may differ.

![Same RAG path for two backends — identical build_rag_prompt output routes to Ollama locally or Groq in the cloud via GENERATOR_BACKEND](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-05-ollama-vs-groq-same-rag.png)

Set one switch for the whole lab:

```python
GENERATOR_BACKEND = "ollama"  # Change to "groq" for cloud generation
```

---

### Option A — Generate with Ollama (local)

```bash
ollama pull qwen2.5:0.5b  # Small local chat model for the lab
```

```python
from ollama import chat  # Local LLM client — same library as prior Ollama labs

OLLAMA_MODEL = "qwen2.5:0.5b"  # Light model — swap if you use another pulled model


def generate_answer_ollama(rag_prompt):
    """Send augmented prompt to Ollama and return assistant text."""
    response = chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": rag_prompt}],  # One user message with full prompt
    )
    return response["message"]["content"]  # Final answer string
```

**How the code works:**

- **`chat`** — same pattern as terminal Ollama; the **entire** RAG prompt is one user message.  
- **Ollama must be running** — start the Ollama app or `ollama serve` before calling.

---

### Option B — Generate with Groq (cloud)

```bash
pip install groq  # Groq Python client — run once in Colab or local venv
```

Add your API key as **`GROQ_API_KEY`** (Colab Secrets or shell export). Create a key at [console.groq.com](https://console.groq.com) if you do not have one.

```python
import os  # Read API key from environment
from groq import Groq  # Cloud LLM client — same pattern as prior Groq labs

GROQ_MODEL = "llama-3.3-70b-versatile"  # Fast cloud model used on this track


def generate_answer_groq(rag_prompt):
    """Send augmented prompt to Groq and return assistant text."""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Connect with your secret key
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": rag_prompt}],  # Same message shape as Ollama path
    )
    return response.choices[0].message.content  # Final answer string
```

**How the code works:**

- **`Groq(api_key=...)`** — same client pattern from **earlier** cloud API work on this track.  
- **`chat.completions.create`** — OpenAI-style call; only the **client and model name** differ from other providers.  
- **Common mistake:** Typo in `GROQ_API_KEY` or secret not enabled in Colab — cell fails with key-not-found.

---

### One wrapper — switch backends with a single variable

```python
GENERATOR_BACKEND = "ollama"  # or "groq"


def generate_answer(rag_prompt):
    """Route to Ollama or Groq based on GENERATOR_BACKEND."""
    if GENERATOR_BACKEND == "ollama":
        return generate_answer_ollama(rag_prompt)
    if GENERATOR_BACKEND == "groq":
        return generate_answer_groq(rag_prompt)
    raise ValueError(f"Unknown GENERATOR_BACKEND: {GENERATOR_BACKEND}")
```

**How the code works:**

- **`build_rag_prompt`** output is **backend-neutral** — swap `GENERATOR_BACKEND` without touching retrieval.  
- **Common mistake:** Calling `generate_answer` **before** building the prompt with retrieved chunks — that is **not RAG**, just a plain chatbot.

### Simple Activity — Same RAG, Two Generators

1. Run the full pipeline with **`GENERATOR_BACKEND = "ollama"`** on *"Is delivery free for a 600 rupee order?"*  
2. Change to **`"groq"`** and run again (same retrieved chunks if you print them first).  
3. Note: do **Sources used** lines match the same **`source_id`** values? One sentence on any wording difference.

---

## Informal Grounding Check — Cite Supporting Chunks

Production systems use automated evaluators; in this lab you **manually verify** that claims map back to retrieved text.

- **Official Definition:** An **informal grounding check** compares each factual claim in the LLM output to retrieved chunk text and metadata.
- **In Simple Words:** **Fact-check the answer** against the three paragraphs you pasted in.
- **Real-Life Example:** A **news fact-check desk** matches each headline claim to the **quoted paragraph** — same idea, done by you in a notebook.

### Checklist (run after every demo answer)

| Check | How |
|---|---|
| **Claim in context?** | Every number/rule in the answer appears in **some retrieved chunk** |
| **Source line present?** | Answer ends with **Sources used:** listing `source_id` / `page` |
| **No-context case** | Ask about **UPI payments** (not in corpus) — model should **refuse**, not invent |
| **Chunk ↔ claim map** | Write: *"30 days → Chunk 1, returns_policy.txt"* |

### Simple helper — print retrieval for side-by-side review

```python
def print_retrieval_trace(user_query, retrieved_chunks):
    """Print chunks before generation — use for manual grounding review."""
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for i, chunk in enumerate(retrieved_chunks, start=1):
        meta = chunk["metadata"]
        print(f"\nChunk {i} | id={chunk['id']}")
        print(f"  source_id: {meta.get('source_id')} | page: {meta.get('page')}")
        if chunk.get("distance") is not None:
            print(f"  distance: {chunk['distance']:.4f}")
        print(f"  text: {chunk['text'][:200]}...")
```

### Simple Activity — Grounding Audit

1. Query: *"How many days do I have to return a product?"*  
2. Print the **retrieval trace**, then the **generated answer**.  
3. Fill a two-column table: **Claim in answer** | **Which chunk + source_id supports it**.  
4. Repeat with *"Can I pay with UPI?"* — confirm the model **refuses** or says **not found**.

![Informal grounding check — compare retrieval trace to the generated answer; map each claim to source_id and page; verify no-context questions are refused](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-07-informal-grounding-check.png)

---

## Without RAG vs With RAG — Quick Contrast

Same question, two paths — compare both outputs in your notebook.

```python
def generate_without_rag(user_query):
    """Plain LLM call — no retrieved context (shows hallucination risk)."""
    if GENERATOR_BACKEND == "ollama":
        from ollama import chat
        response = chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": user_query}])
        return response["message"]["content"]
    from groq import Groq
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": user_query}],
    )
    return response.choices[0].message.content
```

- Run **`generate_without_rag`** and **`generate_answer(build_rag_prompt(...))`** on the **same** ShopEasy question.  
- The without-RAG path may invent a **generic** return policy; the RAG path should cite **your** stored chunks.

![Without RAG vs with RAG — plain LLM call may hallucinate policy details; rag_answer retrieves chunks first and cites Sources used from your corpus](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-06-without-rag-vs-with-rag.png)

---

## Mini End-to-End RAG Script — Ingest, Retrieve, Answer

This script ties the full pipeline together. **Ingest** rebuilds the index if empty; otherwise it reuses `policy_chunks`.

```python
import os
import chromadb
from sentence_transformers import SentenceTransformer

# --- Config ---
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "policy_chunks"
CHROMA_PATH = "./chroma_store"
TOP_K = 3
GENERATOR_BACKEND = "ollama"  # or "groq" — swap for cloud generation
OLLAMA_MODEL = "qwen2.5:0.5b"
GROQ_MODEL = "llama-3.3-70b-versatile"

# --- Sample corpus (same ShopEasy policies as the chunking lab) ---
SAMPLE_CORPUS = [
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
            "Orders above 499 rupees qualify for free shipping. Express delivery arrives within 24 to 48 hours "
            "in eligible metro cities."
        ),
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
    },
    {
        "text": (
            "ShopEasy Warranty Policy. Electronics include a 12-month manufacturer warranty from delivery date. "
            "Physical damage is not covered."
        ),
        "metadata": {"source_id": "warranty_policy.pdf", "page": 0},
    },
]


def chunk_text(text, chunk_size=500, overlap=75):
    """Fixed-size character splitter with overlap."""
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
    """Split corpus records and attach metadata + stable ids."""
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


def ingest_sample_policies(collection, embed_model):
    """Ingest step: chunk sample corpus, embed, upsert into Chroma."""
    chunks = create_chunks_from_corpus(SAMPLE_CORPUS)
    collection.upsert(
        ids=[c["id"] for c in chunks],
        documents=[c["text"] for c in chunks],
        metadatas=[c["metadata"] for c in chunks],
        embeddings=embed_model.encode([c["text"] for c in chunks], convert_to_numpy=True).tolist(),
    )
    print(f"Ingest complete — {collection.count()} rows in {COLLECTION_NAME}")


def retrieve_chunks(user_query, collection, embed_model, top_k=TOP_K):
    """Retrieve step: top-k semantic search."""
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


def build_rag_prompt(user_query, retrieved_chunks):
    """Augment step: context block with delimiters and source labels."""
    lines = [
        "You are a helpful ShopEasy customer support assistant.",
        "Answer ONLY using the Context between CONTEXT START and CONTEXT END.",
        "If the answer is not in the Context, say: I could not find this in the provided policy documents.",
        "End with: Sources used: (list source_id and page for chunks you used).",
        "",
        "=== CONTEXT START ===",
    ]
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
    )
    return response.choices[0].message.content


def generate_answer(rag_prompt):
    """Generate step — route to Ollama or Groq."""
    if GENERATOR_BACKEND == "ollama":
        return generate_answer_ollama(rag_prompt)
    if GENERATOR_BACKEND == "groq":
        return generate_answer_groq(rag_prompt)
    raise ValueError(f"Unknown GENERATOR_BACKEND: {GENERATOR_BACKEND}")


def rag_answer(user_query, collection, embed_model, top_k=TOP_K):
    """End-to-end: retrieve → build prompt → generate → return answer + chunks for audit."""
    retrieved = retrieve_chunks(user_query, collection, embed_model, top_k=top_k)
    prompt = build_rag_prompt(user_query, retrieved)
    answer = generate_answer(prompt)
    return {"answer": answer, "retrieved_chunks": retrieved, "prompt": prompt}


def main():
    """Run ingest (if needed), then answer a sample question with full trace."""
    embed_model = SentenceTransformer(EMBED_MODEL_NAME)
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=None)

    if collection.count() == 0:
        ingest_sample_policies(collection, embed_model)  # Ingest only when index is empty

    question = "How many days do I have to return a product?"
    print("Question:", question)

    result = rag_answer(question, collection, embed_model, top_k=TOP_K)

    print("\n--- Retrieved chunks ---")
    for i, chunk in enumerate(result["retrieved_chunks"], start=1):
        print(f"Chunk {i}: {chunk['metadata']}")

    print("\n--- Generated answer ---")
    print(result["answer"])

    print("\n--- Grounding audit (you fill in) ---")
    print("List each fact in the answer and the chunk source_id that supports it.")


if __name__ == "__main__":
    main()
```

**How the code works:**

- **`ingest_sample_policies`** — **ingest + prepare** when the index is empty; skips if **`policy_chunks`** already exists from the **previous** chunking lab.  
- **`retrieve_chunks`** — **top-k** on `policy_chunks` with **`TOP_K = 3`**.  
- **`build_rag_prompt`** — **context assembly** with **`===` delimiters** and **source_id / page** labels.  
- **`generate_answer`** — **Ollama** or **Groq** via **`GENERATOR_BACKEND`** — retrieval and prompt unchanged.  
- **`rag_answer`** — one function your app can call per user message.  
- **`main()`** — prints retrieval + answer + reminder to **audit** claims against chunks.

![Mini end-to-end RAG script — ingest if index empty, retrieve top-k, augment with delimiters, generate via Ollama or Groq, then audit claims against chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-08-end-to-end-mini-rag.png)

Save as `mini_rag_app.py` and run: `python mini_rag_app.py`

---

## When Answers Still Look Wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Invented policy detail | Weak grounding instruction or no context | Strengthen rules; check delimiters |
| "Not found" but chunk exists | **k** too low or bad chunking | Raise **TOP_K**; revisit chunk size |
| Wrong document cited | Noisy retrieval | Lower **k** or improve chunks |
| Generic answer | Called LLM **without** context block | Use full `rag_answer` path |

Fix **retrieval and prompt** before blaming the chat model.

---

## What Comes Next

- **Agents** — call `rag_answer` as a **tool** inside a larger agent loop.  
- **Metadata filters** — retrieve only from `shipping_policy.txt`.  
- **Production eval** — automated grounding scores instead of manual audit.

---

## Key Takeaways

- **Top-k retrieval** on `policy_chunks` with **`all-MiniLM-L6-v2`** connects your prepared index to the user question — **k = 3** is a sensible default.  
- **Context assembly** uses **delimiters** and **source_id / page labels** so the LLM knows which evidence it may use.  
- **Grounded generation** via **Ollama** or **Groq** plus an **informal grounding check** (claim ↔ chunk map) keeps answers tied to stored policies.  
- The **mini RAG script** runs **ingest → retrieve → augment → generate** in one flow — the same pattern every RAG app uses.  
- **Without-RAG** calls show why retrieval matters — the model guesses; **with-RAG** it reads your library first.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `TOP_K` / `n_results` | Config | Number of chunks retrieved per query |
| `retrieve_chunks` | Code | Embed query + Chroma top-k search |
| `build_rag_prompt` | Code | Context assembly with delimiters |
| `GENERATOR_BACKEND` | Config | `"ollama"` (local) or `"groq"` (cloud) |
| `generate_answer_ollama` / `generate_answer_groq` | Code | Backend-specific generator calls |
| `generate_answer` | Code | Wrapper — routes to Ollama or Groq |
| `rag_answer` | Code | End-to-end retrieve → prompt → generate |
| `ingest_sample_policies` | Code | Chunk, embed, upsert if index empty |
| `=== CONTEXT START/END ===` | Pattern | Delimiters for evidence block |
| **Context assembly / Augment** | Concept | Insert retrieved text into LLM prompt |
| **Grounded generation** | Concept | Answer from supplied context |
| **Informal grounding check** | Practice | Manually map claims to chunk sources |
| `policy_chunks` | Code | Chroma collection from chunking lab |
| `ollama pull qwen2.5:0.5b` | CLI | Pull local chat model |
| `pip install groq` | Setup | Groq client for cloud generation |
| `GROQ_API_KEY` | Config | API key for Groq (env / Colab Secrets) |
| `from ollama import chat` | Code | Local LLM generator |
| `from groq import Groq` | Code | Cloud LLM generator |
| **Same model rule** | Concept | Same embed model for index and query |
