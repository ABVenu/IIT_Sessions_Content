# RAG: Chunking & Document Preparation

## Context of This Session

In the **previous** session you learned **embeddings** as semantic coordinates, read **similarity / distance** scores, and stored **five FAQ sentences** in **Chroma** (`support_knowledge_base`) with `all-MiniLM-L6-v2`. You ran **top-k semantic search** and inspected Rank 1 for relevance. Each FAQ was already one short **chunk**, with simple metadata such as `category`.

This session is the **prepare** step that session pointed to: **real policies are longer than one FAQ line**. You will **split**, **label**, and **persist** them with the **same Chroma path** — `PersistentClient` → `encode` → `upsert` → `query` — not build the perfect file loader.

The core skills are:

1. **Chunking strategies** — choosing **chunk size** and **overlap** and applying them on a sample dataset  
2. **Metadata** — attaching **`source_id`** and **`page`** so every chunk is traceable (richer than `category` alone)  
3. **Chunk storage** — persisting chunked rows into a new collection (`policy_chunks`) using the **same embed-and-upsert pattern** as the FAQ lab  

Loading `.txt` and PDF files into a corpus is **setup** you run once; it is covered briefly at the end.

**In this session, you will:**

- **Recap** the RAG prepare path: load → chunk → embed → store → retrieve (building on **embeddings** and **Chroma** from the previous session)  
- **Apply chunking** with justified **chunk size** and **overlap** on a sample dataset (fixed-size + overlap as the main strategy)  
- **Attach metadata** (`source_id`, `page`) to every chunk for traceability  
- **Persist** chunked documents into Chroma (`policy_chunks` collection)  
- **Load** plain-text and PDFs into a corpus (in-memory policies in the manual lab; folder PDF load via LangChain in the Tesla demo)  

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

---

## Document Upload in Chat Apps vs True RAG

- **Official Definition:** **Retrieval-Augmented Generation (RAG)** prepares documents offline: chunk, embed, store in a vector DB, then retrieve top matches at query time.
- **In Simple Words:** The model does **not** rely on one giant prompt that contains your whole PDF every time — it searches **pre-made chunk cards**.
- **Real-Life Example:** Uploading a very large file to a chat app often hits **token limits** because the system may treat the upload as **one user message**. A support bot instead **indexes** files once and pulls only **relevant chunks** per question.

**Key contrast:**

- **Chat-style document upload** — the file content can act like a **single zero-shot prompt** (not the same as your chunked Chroma lab).
- **In-memory RAG** (introduced briefly) — retrieval may happen inside a session without the persistent Chroma workflow you practised.
- **Your lab path** — **true chunked RAG**: split → label → embed → **upsert** → **query** (same pipeline idea as the FAQ flow, with more rows and richer metadata).

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

**For this lab, Strategy 1 is enough** — you will justify the numbers, then code it. Sentence-aware and page-based approaches were introduced as **alternatives**, not the main hands-on path.

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

### Ground rule for large PDFs (live demo)

For **long reports** (e.g. a multi-page SEC filing), a practical setting is **`chunk_size = 512`** and **`chunk_overlap = 16`** (~15% overlap).

- **Why 512?** A practical sweet spot on big files — not one vector for the whole PDF, not thousands of one-line fragments.  
- **Why ~15% overlap?** Keeps sentences on chunk borders from being lost between windows.  
- **Rule:** `overlap` must be **smaller than** `chunk_size` — if overlap equals size, the splitter **never advances**.

Use **500 / 75** on the **short ShopEasy policy corpus** in the manual notebook; use **512 / 16** when you mirror the **Tesla-scale** LangChain demo.

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
sample_corpus = [  # Longer policies — same e-commerce support theme as the FAQ lab (returns, shipping, 499 rupees)
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

**ShopEasy** is the brand name for these longer policy texts. The ideas match the previous FAQ lab — **30-day returns**, **free shipping above 499 rupees**, **express delivery in 24–48 hours** — but each policy is now a **paragraph**, not a one-line FAQ.

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
| **`year`**, **`category`** (optional) | Optional tags | Useful later for **metadata filters** (e.g. only 2023 reports) |

### How metadata flows

1. **Parent record** (corpus row) holds `source_id` + `page`.  
2. **Chunk step** copies them onto every child chunk.  
3. **Chroma upsert** stores them in `metadatas=`.  
4. **Query results** return them in `results["metadatas"]` — read Rank 1 before trusting the answer.

![Metadata for traceability — parent record supplies source_id and page; each chunk gets chunk_index and a stable id; only text is embedded, metadata is stored for citation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-05-metadata-traceability.png)

| Previous FAQ lab (`support_knowledge_base`) | This session (`policy_chunks`) |
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
pip install langchain-community langchain  # For the Tesla-style folder PDF demo
```

Run the blocks below **in order** after `chunks` is built from `sample_corpus` (or from a loaded corpus).

```python
import chromadb
from sentence_transformers import SentenceTransformer
from pprint import pprint

client = chromadb.PersistentClient(path="./chroma_store")  # Same on-disk store pattern as the FAQ lab

collection = client.get_or_create_collection(
    name="policy_chunks",  # New collection — do not overwrite support_knowledge_base
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

## Real-World PDF Demo — LangChain (Folder Load and Chunk)

After the **manual** `policy_chunks` lab, you can run a **Tesla annual report** PDF set (~130 pages) with **LangChain** — same concepts, shorter code.

**What the demo showed:**

- **Load** every PDF in a folder in one step.  
- **Chunk** with **`chunk_size=512`**, **`chunk_overlap=16`** → **351 chunks** for that dataset.  
- **Persist** with `Chroma.from_documents` and **`all-MiniLM-L6-v2`**.  
- **Metadata was omitted** in this shortcut to keep the notebook light — in real projects, still attach **`source_id`** and **`page`** as in the manual lab.

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PDF_FOLDER = "Tesla_Annual_Reports"

loader = PyPDFDirectoryLoader(PDF_FOLDER)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=16)
chunks = splitter.split_documents(documents)
print("Total chunks:", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="tesla_financial_chunks",
)
```

**How the code works:**

- **`PyPDFDirectoryLoader`** — loads all PDFs in the folder (each page becomes part of the document list).  
- **`RecursiveCharacterTextSplitter`** — fixed-size windows with overlap (Strategy 1 via a library).  
- **`Chroma.from_documents`** — embeds and upserts in one call instead of manual list alignment.  
- **Same pipeline** as the manual lab — only the API surface is shorter.

**End-of-session recap:** load plain text and PDF → chunk (fixed-width focus) → attach metadata (manual path) → persist in Chroma → retrieve for questions (full prompt assembly comes next).

---

## Semantic Chunking — Advanced Alternative

- **Official Definition:** **Semantic chunking** groups text by **embedding similarity** between sentences, not fixed character windows.
- **In Simple Words:** Sentences about the **same topic** stay in one chunk even when lengths differ.
- **Real-Life Example:** A fixed 500-character cut through a story can split mid-topic; semantic grouping keeps **one complete idea** together.

**Typical steps:**

1. Split into **sentences**.  
2. **Embed** each sentence.  
3. **Merge** neighbours while similarity stays high; start a new chunk when the topic shifts.

**Trade-offs:**

- **Pros** — Chunks follow **meaning**; fewer broken policy rules at boundaries.  
- **Cons** — **More compute**; not usually the **first** move for a small FAQ or policy bot.  
- Production systems often use **hybrid** or **hierarchical** approaches (e.g. code indexed by file/class/function).

**For this module, Strategy 1 (fixed size + overlap) is the primary skill.**

---

## Vector Stores and Similarity Indexes

- **Official Definition:** **Similarity indexes** (e.g. HNSW, IVF) accelerate **nearest-neighbour search** over embedding vectors.
- **In Simple Words:** Like a database index — without it, every query might scan **all** vectors.
- **Real-Life Example:** You use a **shop map** to find the right aisle instead of walking every shelf for every question.

Vector DBs still need **admin-style care** (index choice, rebuilds) like traditional DBAs, but lookups are **semantic**, not exact-key SQL filters.

---

## What Comes Next

- **Prompt assembly** — top-k chunk text becomes LLM context.  
- **Metadata filters** — search only `source_id="shipping_policy.txt"`.  
- **Full RAG** — retrieve → augment → generate.

---

## Key Takeaways

- **RAG prepare stage** — load → chunk → embed → store → retrieve; today went deep on **chunking**, **metadata**, and **storage**.  
- **Chunking strategies** — **fixed size + overlap** is primary; justify **500 / 75** on short policies and **512 / 16** on large PDFs (~15% overlap).  
- **Metadata** (`source_id`, `page`, `chunk_index`) makes chunks **traceable** — only **text** is embedded; tags are for citation.  
- **Chunk storage** — manual `encode` + `upsert` on `policy_chunks`, or **LangChain** `Chroma.from_documents` on large folders (same embedding model rule).  
- **Chat upload ≠ chunked RAG** — whole-file prompts hit limits; persistent vector search needs prepared chunks.  
- **Semantic chunking** and **similarity indexes** matter in advanced systems; fixed-width chunking is your core lab skill.  
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
| `PyPDFDirectoryLoader` / `RecursiveCharacterTextSplitter` | Code | LangChain load + chunk (Tesla-style demo) |
| `Chroma.from_documents` | Code | One-step embed + upsert for many chunks |
| **Semantic chunking** | Concept | Sentence-similarity grouping (advanced) |
| **HNSW / IVF** | Concept | Similarity indexes inside vector DBs |
| **Same model rule** | Concept | One encoder for all chunks and queries |
