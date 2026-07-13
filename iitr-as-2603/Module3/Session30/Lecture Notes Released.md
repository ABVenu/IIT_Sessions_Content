# RAG: Chunking & Document Preparation

## Context of This Session

In the **previous** session you learned **embeddings** as semantic coordinates, read **similarity / distance** scores, and stored **five FAQ sentences** in **Chroma** (`support_knowledge_base`) with `all-MiniLM-L6-v2`. You ran **top-k semantic search** and inspected Rank 1 for relevance. Each FAQ was already one short **chunk**, with simple metadata such as `category`.

This session is the **prepare** step that session pointed to: **real policies and PDFs are longer than one FAQ line**. You will **load**, **split**, **label**, and **persist** them — then verify retrieval — using the same Chroma idea: embed → store → query.

The core skills are:

1. **Document loading** — bring plain text or PDFs into a consistent corpus  
2. **Chunking strategies** — choose **chunk size** and **overlap** and apply them on a sample dataset  
3. **Metadata** — attach **`source_id`** and **`page`** so every chunk is traceable  
4. **Chunk storage** — persist chunked rows into Chroma (manual upsert on short policies; LangChain `from_documents` on a large PDF)

**In this session, you will:**

- **Recap** the RAG prepare path: load → chunk → embed → store → retrieve (building on **embeddings** and **Chroma** from the previous session)  
- **Load** plain-text and PDF documents into a corpus (in-memory policies in the manual lab; folder PDF load via LangChain in the Tesla demo)  
- **Apply chunking** with justified **chunk size** and **overlap** on a sample dataset (fixed-size + overlap as the main strategy)  
- **Attach metadata** (`source_id`, `page`) to every chunk for traceability  
- **Persist** chunked documents into Chroma and **verify** with semantic search  
- **Preview** an end-to-end RAG answer on a real PDF (full grounded generation is covered in upcoming work)

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

Chunking sits **before embedding** and **before Chroma upsert** — a main skill of this session.

**Also remember top-k balance:** retrieving **too few** chunks can miss the answer; retrieving **too many** defeats the point of RAG and can leak unnecessary context. Choose a sensible middle value when you query.

![Why chunking matters — whole file blurs meaning, chunks too large return walls of text, chunks too small lose context like a lone date with no returns policy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-02-why-chunking-matters.png)

---

## Normal Generation vs RAG for Proprietary Data

Before diving into chunk code, connect this session to **why** RAG exists.

- **Official Definition:** **Normal generation** asks an LLM to answer from its training knowledge alone. **RAG** first **retrieves** relevant chunks from your documents, then asks the LLM to answer using that context.
- **In Simple Words:** Without RAG, the model only knows what it already “studied.” With RAG, it can open **your company’s manuals** first.
- **Real-Life Example:** Siemens builds MRI and CT machines. The **operating manuals** are confidential IP — not something a public chat model can be trusted to invent. A support chatbot for hospital staff must **consult the manual chunks**, not guess error codes.

**Key contrast:**

- **Normal generation** — question → LLM → answer (fails on private manuals and company data).  
- **Your lab path** — **chunked RAG**: load → split → label → embed → **upsert** → **query** → (later) generate with retrieved context.

---

## Chunking Strategies — Size, Overlap, and How to Choose

You will use a **fixed-size character splitter with overlap** — the most common starter strategy in RAG pipelines.

### Strategy 1 — Fixed size + overlap (this lab)

- Slide a window of **`chunk_size`** characters across the text.  
- Move forward by **`chunk_size − overlap`** so neighbouring chunks **share** a tail.  
- **Best for:** Policy PDFs, FAQs, notices — predictable and easy to debug in a notebook.

### One chunk per page (concept only — not the practice path)

- Early RAG diagrams sometimes say “each PDF page = one chunk” — that is only a **teaching picture**.  
- **In practice** you use **fixed-size character windows** (Strategy 1), because real pages can be long and still need splitting.  
- Other chunkers (for example **semantic chunking**) appear in **advanced** RAG work later.

**For this lab, Strategy 1 is enough** — you will justify the numbers, then code it.

![Fixed size plus overlap — slide a chunk_size window across text and step forward by chunk_size minus overlap so neighbouring chunks share a margin at boundaries](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-03-sliding-window-overlap.png)

---

## Chunk Size — Justify Your Number

- **Official Definition:** **Chunk size** is the maximum length of one segment before the splitter starts the next chunk.
- **In Simple Words:** The **maximum size of one search card**.
- **Real-Life Example:** Cutting a **samosa** — too small loses filling; too large is not bite-sized.

| Size | Trade-off |
|---|---|
| **Too small** (e.g. 1–50 chars) | Loses meaning — a single character or half a sentence is useless as a chunk |
| **Too large** (e.g. ~10,000 chars / whole file) | Few chunks, **blurry** embeddings — RAG becomes pointless |
| **Lab default** (**500 chars**) | ~2–4 policy sentences; easy to inspect with `len()` |
| **Large PDF practice** (**512 chars**) | Practical sweet spot used on long reports |

**Why 500 characters for the short policy corpus:**

- Matches **short e-commerce policies** (same theme as the FAQ lab).  
- Easy to inspect with `len()` in a notebook — no token counter required.  
- In production you may switch to **token limits**; the **thinking** (one idea per chunk) stays the same.

### Ground rule for large PDFs

For **long reports** (e.g. a multi-page financial PDF), a practical setting is **`chunk_size = 512`** and **`chunk_overlap = 16`**.

- **Why 512?** A practical sweet spot on big files — not one vector for the whole PDF, not thousands of one-line fragments.  
- **Why a small overlap?** Keeps sentences on chunk borders from being lost between windows.  
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
| **Large PDF demo** | 512 | **16** | Short shared bridge between windows |

- **Rule of thumb:** Overlap ≈ **10–20%** of chunk size on short corpora; large demos may use a smaller absolute overlap (e.g. 16).  
- **Cost:** More overlap → more rows in Chroma → slightly more embed time — usually fine for small corpora.  
- **Common mistake:** `overlap >= chunk_size` — the splitter **never advances** (the lab code guards against this).

---

## Sample Dataset for Chunking Practice

Use this **in-memory corpus** to learn chunking and metadata **before** file loaders. Each record has `text` plus `source_id` and `page`. The short policy walkthrough focuses on **returns** and **shipping** text; a third warranty policy is included here for extra practice in the same shape.

```python
sample_corpus = [  # Longer policies — same e-commerce support theme as the FAQ lab
    {
        "text": (  # Returns policy paragraph
            "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
            "Items must be in original packaging. To start a return, open Orders and tap Request Return. "
            "Our team reviews requests within 24 hours on business days."
        ),
        "metadata": {"source_id": "returns_policy.txt", "page": 0},  # page 0 for plain text
    },
    {
        "text": (  # Shipping policy paragraph
            "ShopEasy Shipping Policy. Standard delivery takes 3 to 5 business days. "
            "Orders above 499 rupees qualify for free shipping. Express delivery arrives within 24 to 48 hours "
            "in eligible metro cities."
        ),
        "metadata": {"source_id": "shipping_policy.txt", "page": 0},
    },
    {
        "text": (  # Extra practice policy — same metadata pattern
            "ShopEasy Warranty Policy. Electronics include a 12-month manufacturer warranty from delivery date. "
            "To claim warranty, upload invoice and serial number photo in Support. "
            "Physical damage is not covered."
        ),
        "metadata": {"source_id": "warranty_policy.pdf", "page": 0},
    },
]
```

**ShopEasy** is the brand name for these longer policy texts. The ideas match the previous FAQ lab — **30-day returns**, **free shipping above 499 rupees**, **express delivery in 24–48 hours** — but each policy is now a **paragraph**, not a one-line FAQ.

All chunking and metadata activities below use `sample_corpus`. The **Tesla PDF demo** later loads real files from disk with LangChain.

---

## Implement Chunking — Code and Metadata Together

Chunking and metadata are **one step** — every chunk must carry **where it came from**.

```python
def chunk_text(text, chunk_size=500, overlap=75):
    """Strategy 1: fixed character windows with overlap."""
    if chunk_size <= overlap:  # Guard: overlap must be smaller than size
        raise ValueError("chunk_size must be larger than overlap")

    chunks = []  # Collect plain text pieces
    start = 0  # Sliding-window start index
    while start < len(text):  # Walk until the end of the string
        piece = text[start : start + chunk_size].strip()  # Take one window
        if piece:  # Skip empty pieces after strip
            chunks.append(piece)
        start += chunk_size - overlap  # Advance by size minus overlap
    return chunks


def create_chunks_from_corpus(corpus, chunk_size=500, overlap=75):
    """Split every record; attach source_id, page, chunk_index; build stable ids."""
    all_chunks = []  # Final list of chunk dicts

    for record in corpus:  # One parent document at a time
        text = record["text"]
        if not text:
            continue

        source_id = record["metadata"]["source_id"]  # File name for citation
        page = record["metadata"]["page"]  # Page index (0 for .txt)

        for chunk_index, chunk_body in enumerate(chunk_text(text, chunk_size, overlap)):
            all_chunks.append({
                "id": f"{source_id}__p{page}__c{chunk_index}",  # Stable Chroma primary key
                "text": chunk_body,  # Only this field is embedded
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

| Field | Required | Role |
|---|---|---|
| **`source_id`** | Yes | File name — which document answered |
| **`page`** | Yes | PDF page index; use **`0`** for plain `.txt` |
| **`chunk_index`** | Lab extra | Order when one page becomes many chunks |

**Why it matters:** When Rank 1 is wrong, metadata helps you **debug** — you can see which file and page came back. Citations for users (“see page 125”) also need these tags.

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
- *Can I search by page?* Chroma supports **metadata filters** in later work; in this lab you **read** tags from results.  
- *Wrong page in results?* Usually a **loading** bug — fix `page` at corpus time, not at query time.

### Simple Activity — Metadata Check on Chunks

Pick **three** items from `chunks`. For each, write **`source_id`**, **`page`**, **`chunk_index`**, and one sentence of **chunk text**. Confirm the text still makes sense **without** reading the full parent file.

---

## Persist Chunked Documents in Chroma

**Chunk storage** is the third core skill — same pipeline as the FAQ lab, more rows, richer metadata.

![Persist chunked documents in Chroma — corpus to chunks, encode with all-MiniLM-L6-v2, upsert into policy_chunks, then query top-k and read metadata on results](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session40/session40-06-chroma-chunk-pipeline.png)

```bash
pip install chromadb sentence-transformers  # Manual policy lab
pip install langchain langchain-community  # Tesla-style folder PDF demo
```

Run the blocks below **in order** after `chunks` is built from `sample_corpus`.

```python
import chromadb  # Persistent vector store client
from sentence_transformers import SentenceTransformer  # Embedding model
from pprint import pprint  # Pretty-print peek results

client = chromadb.PersistentClient(path="./chroma_store")  # Same on-disk pattern as FAQ lab

collection = client.get_or_create_collection(
    name="policy_chunks",  # New collection — do not overwrite support_knowledge_base
    embedding_function=None,  # We pass embeddings ourselves
)

model = SentenceTransformer("all-MiniLM-L6-v2")  # Same encoder as previous lab

ids = [c["id"] for c in chunks]  # Primary keys
documents = [c["text"] for c in chunks]  # Text to embed and store
metadatas = [c["metadata"] for c in chunks]  # Traceability tags

embeddings = model.encode(documents, convert_to_numpy=True).tolist()  # Vectors for each chunk

collection.upsert(  # Insert or update all rows
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings,
)

print("Rows stored:", collection.count())
pprint(collection.peek())  # Spot-check stored rows
```

**How the code works:**

- **`policy_chunks`** — new collection; FAQ rows stay in **`support_knowledge_base`**.  
- **`embedding_function=None`** — you pass vectors on upsert and query (same as previous lab).  
- **Index-aligned lists** — `ids[i]`, `documents[i]`, `metadatas[i]`, `embeddings[i]` are the **same chunk**.  
- **Same model rule** — `all-MiniLM-L6-v2` for every chunk and every query in this manual lab.

---

## Verify Storage and Run Semantic Search

Confirm **metadata** survived the upsert, then search.

```python
row = collection.get(ids=[ids[0]], include=["documents", "metadatas"])  # Exact lookup by id
print("Spot-check metadata:", row["metadatas"][0])
print("Spot-check text:", row["documents"][0][:160])

user_query = "How many days do I have to return a product?"

query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()  # Same model as chunks

results = collection.query(query_embeddings=query_embedding, n_results=3)  # Top-3 similar chunks

print("\nQuery:", user_query)
for i in range(len(results["ids"][0])):
    print(f"\nRank {i + 1}")
    print("  ID:", results["ids"][0][i])
    print("  Document:", results["documents"][0][i])
    print("  Metadata:", results["metadatas"][0][i])  # Trace source_id and page
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

## Real-World PDF Demo — LangChain (Tesla Report)

After the **manual** `policy_chunks` lab, run a **Tesla annual report** PDF (~130 pages) with **LangChain** — same concepts, much shorter code.

**What this demo shows:**

- **Load** every PDF in a folder with `PyPDFDirectoryLoader` (backed by **PyPDF**).  
- **Chunk** with `RecursiveCharacterTextSplitter` — **`chunk_size=512`**, **`chunk_overlap=16`** → **351 chunks** for that dataset.  
- **Metadata auto-attached** — LangChain adds **`source`** (file path) and **`page`** (e.g. page 125) without hand-written tags.  
- **Embed** with **GTE Large** (contrasted with MiniLM from the short policy lab).  
- **Persist** with `Chroma.from_documents` and a **persist directory**.  
- **Retrieve** top-k chunks, then **preview** a grounded LLM answer (full generation flow is covered in upcoming work).

**Why LangChain here:** Manual chunking can take ~20–30 lines. With LangChain helpers, load / chunk / embed / store each become roughly **one call**.

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader  # Load all PDFs in a folder
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Fixed-size windows with overlap
from langchain_community.embeddings import HuggingFaceEmbeddings  # Sentence-Transformers wrapper
from langchain_community.vectorstores import Chroma  # Persist embeddings

PDF_FOLDER = "Tesla_Annual_Reports"  # Folder after unzipping the shared zip

loader = PyPDFDirectoryLoader(PDF_FOLDER)  # Uses PyPDF under the hood
documents = loader.load()  # One Document object per page (with source + page metadata)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,  # Practical size for long reports
    chunk_overlap=16,  # Shared bridge between neighbouring chunks
)
chunks = splitter.split_documents(documents)  # ~351 chunks on the Tesla file
print("Total chunks:", len(chunks))
print("Sample metadata:", chunks[0].metadata)  # source + page already present

embeddings = HuggingFaceEmbeddings(
    model_name="thenlper/gte-large"  # GTE Large — larger than MiniLM for this demo
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="tesla_financial_chunks",
    persist_directory="./tesla_chroma_store",  # On-disk Chroma folder
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5},  # Top-5 similar chunks
)
```

**How the code works:**

- **`PyPDFDirectoryLoader`** — loads all PDFs in the folder; each page becomes a document with metadata.  
- **`RecursiveCharacterTextSplitter`** — fixed-size windows with overlap (Strategy 1 via a library).  
- **`HuggingFaceEmbeddings` + GTE Large** — embeds chunks for this large-PDF demo (MiniLM stays correct for the short policy lab).  
- **`Chroma.from_documents`** — embeds and upserts in one call instead of manual list alignment.  
- **`as_retriever`** — similarity search helper for later query steps.

### Preview — retrieve context and ask the LLM

This is a **preview** of the full RAG answer path. Upcoming work goes deeper on prompt assembly and generation quality.

```python
from groq import Groq  # Cloud LLM client for the answer preview

client = Groq()  # Uses your GROQ API key from the environment

user_query = "What is the annual revenue in the year 2020?"

relevant_docs = retriever.get_relevant_documents(user_query)  # Top-k chunks from Chroma
context = "\n\n".join(doc.page_content for doc in relevant_docs)  # Join chunk text into one context block

prompt = (  # Build a grounded prompt from retrieved text only
    f"Answer using only the context below.\n\n"
    f"Context:\n{context}\n\n"
    f"Question: {user_query}"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Example Groq model — match your notebook if different
    messages=[{"role": "user", "content": prompt}],  # Single user turn with context + question
)
print(response.choices[0].message.content)  # Print the grounded answer
```

**How the code works:**

- **Retriever** pulls the most similar Tesla chunks for the question.  
- **Context string** is built from those chunks only.  
- **LLM** answers from context — useful for confidential PDFs the model never trained on.  
- **Evaluate carefully** — checking whether answers are always correct is a later **evaluation** topic.

Other loaders exist too (text, Excel, JSON). This session’s focus is **plain text / PDF** into a consistent corpus.

---

## Semantic Chunking — Brief Look Ahead

- **Official Definition:** **Semantic chunking** groups text by **embedding similarity** between sentences, not fixed character windows.
- **In Simple Words:** Sentences about the **same topic** stay in one chunk even when lengths differ.
- **Real-Life Example:** A fixed 500-character cut can split mid-topic; semantic grouping keeps **one complete idea** together.

**For this module, Strategy 1 (fixed size + overlap) is the primary skill.** Semantic and other advanced chunkers belong to **advanced RAG** work later.

---

## What Comes Next

- **Prompt assembly** — top-k chunk text becomes LLM context in more detail.  
- **Metadata filters** — search only `source_id="shipping_policy.txt"`.  
- **Full RAG generation** — retrieve → augment → generate as the main focus.  
- **Evaluation** — systematic checks that answers are correct, not only manual spot checks.  
- **Advanced chunking** — semantic and hybrid approaches on larger systems.

---

## Key Takeaways

- **RAG prepare stage** — load → chunk → embed → store → retrieve; this session went deep on **loading**, **chunking**, **metadata**, and **storage**.  
- **Chunking** — **fixed size + overlap** is primary; justify **500 / 75** on short policies and **512 / 16** on large PDFs. Page-as-one-chunk is only a teaching picture.  
- **Metadata** (`source_id`, `page`, `chunk_index`) makes chunks **traceable** — only **text** is embedded; tags are for citation and debugging.  
- **Storage options** — manual MiniLM `upsert` on `policy_chunks`, or LangChain `Chroma.from_documents` with **GTE Large** on large PDFs. Weak retrieval is often a **chunking or metadata** problem.  
- **Next** — deepen **grounded generation**, prompt assembly, evaluation, and advanced chunkers on the same Tesla-style pipeline.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `chunk_text` / `create_chunks_from_corpus` | Code | Fixed-size splitter; chunks + metadata |
| `chunk_size` / `chunk_overlap` | Concept | Max length; repeated tail between chunks |
| **Fixed-size + overlap strategy** | Concept | Primary chunking approach in this lab |
| `source_id` / `page` | Metadata | File name; page index (0 for `.txt`) |
| `chunk_index` | Metadata | Order of chunk within a page |
| `SentenceTransformer("all-MiniLM-L6-v2")` | Code | Encoder for the short policy lab |
| `thenlper/gte-large` (GTE Large) | Code | Encoder used in the Tesla PDF demo |
| `policy_chunks` | Code | Chroma collection for file-based chunks |
| `collection.upsert` / `query` / `get` | Code | Store chunks; search; verify one row |
| `PyPDFDirectoryLoader` / `RecursiveCharacterTextSplitter` | Code | LangChain load + chunk (Tesla-style demo) |
| `Chroma.from_documents` / `as_retriever` | Code | One-step embed + upsert; similarity retriever |
| **Semantic chunking** | Concept | Sentence-similarity grouping (advanced / later) |
| **Same model rule** | Concept | One encoder for all chunks and queries in a given index |
| Groq + retrieved context | Preview | End-to-end answer preview; full generation next |
