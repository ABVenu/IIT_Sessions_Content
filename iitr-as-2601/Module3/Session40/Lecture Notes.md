# RAG: Chunking & Document Preparation

## Context of This Session

In the **previous** session you stored **five FAQ sentences** in Chroma (`support_knowledge_base`), embedded them with `all-MiniLM-L6-v2`, and ran **top-k semantic search**. Each FAQ was already one short **chunk**.

This session is about **preparing real knowledge for search** — not about building the perfect file loader. The core skills are:

1. **Chunking strategies** — choosing **chunk size** and **overlap** and applying them on a sample dataset  
2. **Metadata** — attaching **`source_id`** and **`page`** so every chunk is traceable  
3. **Chunk storage** — persisting chunked rows into the **same Chroma pattern** from the prior lab  

Loading `.txt` and PDF files into a corpus is **setup** you run once; it is covered briefly at the end.

**In this session, you will:**

- **Apply chunking** with justified **chunk size** and **overlap** on a sample dataset  
- **Attach metadata** (`source_id`, `page`) to every chunk for traceability  
- **Persist** chunked documents into Chroma (`policy_chunks` collection)  
- **Load** plain-text and PDF files into a consistent corpus *(lab setup — secondary)*  

Prompt assembly and a full RAG chatbot are covered in **later work** on the same track.

![Document preparation — RAG prepare stage: load files, chunk with overlap, attach metadata, embed with Sentence Transformers, upsert into Chroma](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-07-document-prep-pipeline.png)

---

## From One FAQ Line to Many Searchable Chunks

| Previous lab | This session |
|---|---|
| One FAQ sentence = one Chroma row | One **chunk** = one Chroma row |
| Metadata = `category` | Metadata = **`source_id`**, **`page`**, **`chunk_index`** |
| No splitting needed | Long policy text must be **split** before embed |

- **Official Definition:** **Document preparation** is the prepare stage of RAG — split text into chunks, tag them, then index for vector search.
- **In Simple Words:** Cut long policies into **small labelled cards**, then store each card in Chroma.
- **Real-Life Example:** A coaching institute does not photocopy a full **40-page module** for one doubt — you pull **one highlighted section** with the **page number** written on it.

**Common mistake:** Embedding a whole PDF as **one vector** — search returns vague matches because too many topics share one embedding.

![From one FAQ line to many searchable chunks — previous lab stored one sentence per row; this session splits long policies into labelled chunks with source_id and page](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-01-faq-to-chunks.png)

---

## Why Chunking Matters

- **Official Definition:** **Chunking** splits long text into segments sized for embedding and retrieval.
- **In Simple Words:** Each **search card** should hold roughly **one idea**.
- **Real-Life Example:** A food-delivery app’s terms page has separate cards for *refunds* and *delivery time* — not one card for the entire PDF.

| Without chunking | What goes wrong |
|---|---|
| Whole file → one vector | Meaning gets **averaged** — shipping questions may match returns text |
| Chunk too large | Rank 1 returns a **wall of text** — hard to use in a prompt |
| Chunk too small | Fragments like *"within 30 days"* lose **context** |

Chunking sits **before embedding** and **before Chroma upsert** — the main skill of this session.

![Why chunking matters — whole file blurs meaning, chunks too large return walls of text, chunks too small lose context like a lone date with no returns policy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-02-why-chunking-matters.png)

---

## Chunking Strategies — Size, Overlap, and How to Choose

You will use a **fixed-size character splitter with overlap** — the most common starter strategy in RAG pipelines. Other tools (sentence splitters, paragraph splitters) follow the same decisions: **how big** and **how much to repeat**.

### Strategy 1 — Fixed size + overlap (this lab)

- Slide a window of **`chunk_size`** characters across the text.  
- Move forward by **`chunk_size − overlap`** so neighbouring chunks **share** a tail.  
- **Best for:** Policy PDFs, FAQs, notices — predictable and easy to debug in a notebook.

### Strategy 2 — Sentence-aware (concept only)

- Split on `.` or `?` first, then pack sentences until a size limit.  
- **Best for:** Chatty prose where hard character cuts break mid-sentence.  
- **Trade-off:** More code; still need overlap at packed boundaries.

### Strategy 3 — One chunk per page (concept only)

- Each PDF page = one chunk — no overlap math.  
- **Best for:** Very short pages (one rule per page).  
- **Trade-off:** Long pages still need splitting inside the page.

**For this lab, Strategy 1 is enough** — you will justify the numbers, compare settings, then code it.

![Fixed size plus overlap — slide a chunk_size window across text and step forward by chunk_size minus overlap so neighbouring chunks share a margin at boundaries](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-03-sliding-window-overlap.png)

---

## Chunk Size — Justify Your Number

- **Official Definition:** **Chunk size** is the maximum length of one segment before the splitter starts the next chunk.
- **In Simple Words:** The **maximum size of one search card**.
- **Real-Life Example:** Cutting a **samosa** — too small loses filling; too large is not bite-sized.

| Size | Trade-off |
|---|---|
| **Too small** (~80 chars) | Loses context — *"within 30 days"* alone does not say *returns* |
| **Too large** (~4,000 chars) | Few chunks, **blurry** embeddings, heavy prompts |
| **Lab default** (**500 chars**) | ~2–4 policy sentences; works well with `all-MiniLM-L6-v2` |

**Why 500 characters for the sample dataset:**

- Matches **short e-commerce policies** (same theme as the FAQ lab).  
- Easy to inspect with `len()` in a notebook — no token counter required.  
- In production you may switch to **token limits**; the **thinking** (one idea per chunk) stays the same.

![Chunk size trade-offs — too small loses context, lab default 500 chars balances policy sentences, too large creates blurry embeddings and heavy prompts](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-04-chunk-size-tradeoffs.png)

---

## Chunk Overlap — Justify Your Margin

- **Official Definition:** **Chunk overlap** repeats characters from the end of chunk *n* at the start of chunk *n + 1*.
- **In Simple Words:** A **shared margin** so a sentence split across two cuts still appears **whole** in at least one chunk.
- **Real-Life Example:** A newspaper repeats the **last line** at the top of the next column — overlap does that for search.

| Setting | Chunk size | Overlap | When to use |
|---|---|---|---|
| **Lab default** | 500 | **75** (~15%) | Balanced policies — **recommended** |
| Tighter | 500 | 50 (~10%) | Smaller index; slightly higher boundary risk |
| Safer | 500 | 100 (~20%) | Long sentences; rules split across lines |

- **Rule of thumb:** Overlap ≈ **10–20%** of chunk size.  
- **Cost:** More overlap → more rows in Chroma → slightly more embed time — usually fine for small corpora.  
- **Common mistake:** `overlap >= chunk_size` — the splitter **never advances** (the lab code guards against this).

---

## Sample Dataset for Chunking Practice

Use this **in-memory corpus** to learn chunking and metadata **before** worrying about file loaders. Each record has `text` plus `source_id` and `page`.

```python
sample_corpus = [  # Three policy slices — same e-commerce theme as the FAQ lab
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
            "To claim warranty, upload invoice and serial number photo in Support. "
            "Physical damage is not covered."
        ),
        "metadata": {"source_id": "warranty_policy.pdf", "page": 0},
    },
]
```

All chunking and metadata activities below use `sample_corpus`. The **Load sample files** section at the end rebuilds the same shape from disk.

---

## Implement Chunking — Code and Metadata Together

Chunking and metadata are **one step** — every chunk must carry **where it came from**.

```python
def chunk_text(text, chunk_size=500, overlap=75):
    """Strategy 1: fixed character windows with overlap."""
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
    """Split every record; attach source_id, page, chunk_index; build stable ids."""
    all_chunks = []

    for record in corpus:
        text = record["text"]
        if not text:
            continue

        source_id = record["metadata"]["source_id"]
        page = record["metadata"]["page"]

        for chunk_index, chunk_body in enumerate(chunk_text(text, chunk_size, overlap)):
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


chunks = create_chunks_from_corpus(sample_corpus, chunk_size=500, overlap=75)
print("Total chunks:", len(chunks))
print("Example id:", chunks[0]["id"])
print("Example metadata:", chunks[0]["metadata"])
print("Example text preview:", chunks[0]["text"][:180])
```

**How the code works:**

- **`chunk_text`** — sliding window; step = `chunk_size - overlap`.  
- **`create_chunks_from_corpus`** — copies **`source_id`** and **`page`** from the parent record; adds **`chunk_index`** per page.  
- **`id`** — `{source_id}__p{page}__c{index}` — unique Chroma primary key.  
- **Embedding uses `text` only** — metadata is **not** embedded; it is stored for **citation and filters**.

---

## Simple Activity — Compare Chunking Strategies (Numbers)

On `sample_corpus`, run `create_chunks_from_corpus` three times and record **total chunk count**:

| Run | chunk_size | overlap | Total chunks (you fill in) |
|---|---|---|---|
| A | 300 | 30 | |
| B | 500 | 75 | |
| C | 800 | 80 | |

Write **two sentences** choosing the best setting for ShopEasy support docs — mention **context per chunk** and **number of rows**. Run **B** for the rest of the lab.

---

## Metadata for Traceability

Metadata is the **second core skill** — without it, Rank 1 text is anonymous.

- **Official Definition:** **Metadata** is key–value data attached to each chunk (file, page, index) for citations, debugging, and filters.
- **In Simple Words:** The **label on the folder**, not the paragraph itself.
- **Real-Life Example:** A court citation lists **case, year, page** — your bot should say *"According to returns_policy.txt…"* not *"According to some text…"*.

### Required fields (metadata basics)

| Field | Required by syllabus | Role |
|---|---|---|
| **`source_id`** | Yes | File name — which document answered |
| **`page`** | Yes | PDF page index; use **`0`** for plain `.txt` |
| **`chunk_index`** | Lab extra | Order when one page becomes many chunks |

### How metadata flows

1. **Parent record** (corpus row) holds `source_id` + `page`.  
2. **Chunk step** copies them onto every child chunk.  
3. **Chroma upsert** stores them in `metadatas=`.  
4. **Query results** return them in `results["metadatas"]` — read Rank 1 before trusting the answer.

![Metadata for traceability — parent record supplies source_id and page; each chunk gets chunk_index and a stable id; only text is embedded, metadata is stored for citation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-05-metadata-traceability.png)

| FAQ lab metadata | This session |
|---|---|
| `{"category": "returns"}` | `{"source_id": "returns_policy.txt", "page": 0, "chunk_index": 1}` |

**Common doubts:**

- *Is metadata embedded?* **No** — only **`text`** becomes a vector.  
- *Can I search by page?* Chroma supports **metadata filters** in later work; today you **read** tags from results.  
- *Wrong page in results?* Usually a **loading** bug — fix `page` at corpus time, not at query time.

### Simple Activity — Metadata Check on Chunks

Pick **three** items from `chunks`. For each, write **`source_id`**, **`page`**, **`chunk_index`**, and one sentence of **chunk text**. Confirm the text still makes sense **without** reading the full parent file.

---

## Persist Chunked Documents in Chroma

**Chunk storage** is the third core skill — same pipeline as the FAQ lab, more rows, richer metadata.

![Persist chunked documents in Chroma — corpus to chunks, encode with all-MiniLM-L6-v2, upsert into policy_chunks, then query top-k and read metadata on results](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-06-chroma-chunk-pipeline.png)

```bash
pip install chromadb sentence-transformers  # Same as previous lab
pip install pypdf  # Only if you run the optional file-load section at the end
```

Run the blocks below **in order** after `chunks` is built from `sample_corpus` (or from a loaded corpus).

```python
import chromadb
from sentence_transformers import SentenceTransformer
from pprint import pprint

client = chromadb.PersistentClient(path="./chroma_store")

collection = client.get_or_create_collection(
    name="policy_chunks",
    embedding_function=None,
)

model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [c["id"] for c in chunks]
documents = [c["text"] for c in chunks]
metadatas = [c["metadata"] for c in chunks]

embeddings = model.encode(documents, convert_to_numpy=True).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings,
)

print("Rows stored:", collection.count())
pprint(collection.peek())
```

**How the code works:**

- **`policy_chunks`** — new collection; FAQ rows stay in **`support_knowledge_base`**.  
- **`embedding_function=None`** — you pass vectors on upsert and query (same as previous lab).  
- **Index-aligned lists** — `ids[i]`, `documents[i]`, `metadatas[i]`, `embeddings[i]` are the **same chunk**.  
- **Same model rule** — `all-MiniLM-L6-v2` for every chunk and every query.

---

## Verify Storage and Run Semantic Search

Confirm **metadata** survived the upsert, then search.

```python
row = collection.get(ids=[ids[0]], include=["documents", "metadatas"])
print("Spot-check metadata:", row["metadatas"][0])
print("Spot-check text:", row["documents"][0][:160])

user_query = "How many days do I have to return a product?"

query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()

results = collection.query(query_embeddings=query_embedding, n_results=3)

print("\nQuery:", user_query)
for i in range(len(results["ids"][0])):
    print(f"\nRank {i + 1}")
    print("  ID:", results["ids"][0][i])
    print("  Document:", results["documents"][0][i])
    print("  Metadata:", results["metadatas"][0][i])
    if results.get("distances"):
        print("  Distance:", results["distances"][0][i])
```

**How the code works:**

- **`get`** — exact row by id; use to verify **metadata** after upsert.  
- **`query`** — meaning search; **`n_results=3`** returns top chunks, not whole files.  
- **Read `metadata` on Rank 1** — cite **`source_id`** and **`page`** in your answer notes.

### Simple Activity — Trace Rank 1

For the return-window query, copy **Rank 1**: full **chunk text**, **`source_id`**, **`page`**, and **distance**. One sentence: did **overlap** help keep the full return rule in one chunk?

Try: *"Is delivery free for a 600 rupee order?"* — confirm **`shipping_policy.txt`** appears in metadata.

---

## When Rank 1 Looks Wrong — Tune Chunking First

| Symptom | Likely cause | Fix |
|---|---|---|
| Vague match | Chunk too large | Lower **chunk_size** |
| Half a rule missing | Bad boundary cut | Raise **overlap** |
| Duplicate rows | Overlap too high on tiny text | Lower overlap |

Improve **chunk size / overlap / metadata**, not only the vector DB tool.

---

## Lab Setup — Load Files into a Corpus (Secondary)

Use this section to **replace** `sample_corpus` with files from disk. Same record shape: `text` + `metadata.source_id` + `metadata.page`.

```python
import os
from pypdf import PdfReader

CORPUS_DIR = "corpus"
os.makedirs(CORPUS_DIR, exist_ok=True)

# Write two .txt policies (or use files your instructor provides)
returns_text = (
    "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
    "Items must be in original packaging. To start a return, open Orders and tap Request Return."
)
shipping_text = (
    "ShopEasy Shipping Policy. Orders above 499 rupees qualify for free shipping. "
    "Express delivery arrives within 24 to 48 hours in eligible metro cities."
)
with open(os.path.join(CORPUS_DIR, "returns_policy.txt"), "w", encoding="utf-8") as f:
    f.write(returns_text)
with open(os.path.join(CORPUS_DIR, "shipping_policy.txt"), "w", encoding="utf-8") as f:
    f.write(shipping_text)


def load_text_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().strip()
    return [{"text": text, "metadata": {"source_id": os.path.basename(path), "page": 0}}]


def load_pdf_file(path):
    reader = PdfReader(path)
    source_id = os.path.basename(path)
    out = []
    for page_index, page in enumerate(reader.pages):
        text = " ".join((page.extract_text() or "").split())
        out.append({"text": text, "metadata": {"source_id": source_id, "page": page_index}})
    return out


def load_corpus_from_folder(folder):
    corpus = []
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if name.endswith(".txt"):
            corpus.extend(load_text_file(path))
        elif name.endswith(".pdf"):
            corpus.extend(load_pdf_file(path))
    return corpus


# corpus = load_corpus_from_folder(CORPUS_DIR)
# chunks = create_chunks_from_corpus(corpus, chunk_size=500, overlap=75)
```

**How the code works:**

- **`.txt`** → one record, **`page: 0`**. **PDF** → one record per page with **`page`** index.  
- Optional: `json.dump(corpus, open("corpus.json","w"))` for a **file-based** copy of the in-memory list.  
- **Notebook order:** load (this section) → `create_chunks_from_corpus` → Chroma upsert above.

---

## What Comes Next

- **Prompt assembly** — top-k chunk text becomes LLM context.  
- **Metadata filters** — search only `source_id="shipping_policy.txt"`.  
- **Full RAG** — retrieve → augment → generate.

---

## Key Takeaways

- **Chunking strategies** start with **fixed size + overlap**; justify **500 / 75** (or your comparison pick) using chunk count and Rank 1 text quality.  
- **Metadata** (`source_id`, `page`, `chunk_index`) makes chunks **traceable** — store on upsert, read on query.  
- **Chunk storage** reuses the prior Chroma path: `encode` → `upsert` → `peek` / `get` → `query` with the **same embedding model**.  
- **Loading** produces a uniform corpus list — important in production, but **secondary** to how you split and tag text.  
- Weak retrieval is often a **chunking or metadata** problem, not a Chroma problem.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `chunk_text` / `create_chunks_from_corpus` | Code | Fixed-size splitter; chunks + metadata |
| `chunk_size` / `chunk_overlap` | Concept | Max length; repeated tail between chunks |
| **Fixed-size + overlap strategy** | Concept | Primary chunking approach in this lab |
| `source_id` / `page` | Metadata | File name; page index (0 for `.txt`) |
| `chunk_index` | Metadata | Order of chunk within a page |
| `SentenceTransformer("all-MiniLM-L6-v2")` | Code | Same model as previous lab |
| `policy_chunks` | Code | Chroma collection for file-based chunks |
| `collection.upsert` / `query` / `get` | Code | Store chunks; search; verify one row |
| `load_corpus_from_folder` | Code | Optional — build corpus from `.txt` / `.pdf` |
| **Same model rule** | Concept | One encoder for all chunks and queries |
