# LangChain RAG Pipeline

## Context of This Session

In the **previous** class you extended **LangChain agents** with **conversational memory**: **`MessagesPlaceholder`**, **`chat_history`**, multi-turn demos, and **`RunnableWithMessageHistory`**. You saw how an agent remembers facts across turns when history is wired correctly.

Earlier you also built a **manual RAG pipeline** — load documents, chunk text, create embeddings, store in a vector database, retrieve similar chunks, and pass them to an LLM. That worked, but every step was written by hand.

This session re-expresses the same RAG idea using **LangChain** as a framework: **loaders**, **text splitters**, **Chroma**, a **retriever**, and an **LCEL RAG chain** for an e-commerce policy support bot.

**In this session, you will:**

- Build a small **policy document corpus** and ingest it with **LangChain loaders**
- **Split** documents into chunks with **`RecursiveCharacterTextSplitter`**
- **Embed** and **persist** vectors in **Chroma** for reuse across runs
- Create a **retriever** and a full **LCEL RAG chain** that answers from retrieved context only
- Test **grounded answers** (with source citation) and **honest “I don’t know”** when context is missing

![Why RAG exists — plain LLM lacks company policies; RAG retrieves from your vector database at query time](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-01-why-rag-exists.png)

---

## Why RAG Exists — LLM Limits and Company Data

- **Official Definition:** **Retrieval-Augmented Generation (RAG)** connects an LLM to an external knowledge store (often a vector database) so answers can use **your** documents at query time.
- **In Simple Words:** The model does not need to “memorise” your return policy during training — it **looks up** the right policy lines when a customer asks.
- **Real-Life Example:** A Swiggy or Amazon support bot must quote **your** refund rules, not generic internet advice.

**Plain LLM chatbot problems:**

- LLMs are trained on **public** data — they do not know your company’s internal policies by default.
- You **cannot** retrain models like GPT on your laptop — training costs months and millions of dollars.
- **Fine-tuning** changes behaviour with a **small** example set; it does **not** load 100 GB of policy PDFs into the model.
- **RAG** keeps large policy data in a **vector database** and retrieves only relevant chunks per question.

**Fine-tuning vs RAG (quick contrast):**

| Approach | Best for | Limit |
|---|---|---|
| **Fine-tuning** | Tone, format, small behaviour tweaks | Not for huge document stores |
| **RAG** | Large, changing policy / FAQ corpora | Needs good chunking and retrieval |

Both can coexist, but **RAG is not replaced by fine-tuning** for big internal knowledge bases.

---

## The Typical RAG Flow

- **Official Definition:** A RAG pipeline turns a user query into a grounded answer by **retrieving** relevant document chunks and **conditioning** generation on that context.
- **In Simple Words:** **Search first, speak second.**
- **Real-Life Example:** Before answering “Can I return headphones?”, the bot opens the **returns file**, finds the electronics section, then writes the reply.

**End-to-end flow:**

1. **User query** arrives.
2. **Retriever** searches the vector database for similar chunks.
3. **Top-k chunks** are passed into a **prompt template**.
4. **LLM** generates a user-friendly answer using only (or mainly) that context.

**Offline prepare path (done once, or when documents change):**

```
Create / load files → Document loader → Text splitter → Embeddings → Chroma (persist)
```

**Online answer path (every user question):**

```
User question → Retriever → Prompt + context → LLM → Final answer
```

![Typical RAG flow — offline prepare path (load, split, embed, persist) and online answer path (retrieve, prompt, generate)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-02-rag-flow-offline-online.png)

---

## Chunkification — Why Big Files Become Small Chunks

- **Official Definition:** **Chunking** splits long documents into smaller segments suitable for embedding and retrieval.
- **In Simple Words:** You cut a thick rulebook into **index cards**, not one giant card.
- **Real-Life Example:** Netflix does not stream a full movie as one block — it stores **one-minute chunks** and fetches the next chunk while you watch. YouTube and Instagram use the same idea.

**Why chunk?**

- Very large documents are hard to search precisely.
- One embedding for an entire PDF **blends** many topics — refund questions may match shipping text.
- Retrieval should return **one focused idea**, not a 50-page wall.

**Common doubt:** *If one file is terabytes, do I load it all at once?*  
No — split into manageable pieces first, then load and index.

![Chunkification — split large policies into overlapping chunks for precise similarity search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-03-chunkification.png)

---

## LangChain Components You Will Implement

| # | Component | Role |
|---|---|---|
| 1 | **Document loader** | Read `.md` / PDF / text files into LangChain **Document** objects |
| 2 | **Text splitter** | Split documents into chunks (`chunk_size`, `chunk_overlap`) |
| 3 | **Embeddings** | Convert each chunk into a numeric vector |
| 4 | **Vector database (Chroma)** | Store vectors and run **similarity search** |
| 5 | **Retriever** | Wrapper that takes a query and returns top-k chunks |
| 6 | **LCEL RAG chain** | Pipe retriever → prompt → LLM → output parser |

**One-time vs every query:**

- **Ingest** (load → split → embed → store) is usually **one-time** until policies change.
- **RAG app** reloads persisted Chroma and answers questions **without** re-embedding every time.

![LangChain RAG components — document loader, text splitter, embeddings, Chroma, retriever, and LCEL chain](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-04-langchain-components.png)

---

## Production File Layout — Four Python Files

The class splits code across files (best practice for real projects):

| File | Purpose |
|---|---|
| `langchain_rag_create_corpus.py` | Write policy text from a dictionary into `.md` files |
| `langchain_rag_ingest.py` | Load, split, embed, and persist chunks in Chroma |
| `langchain_rag.py` | Optional: test retriever only (similarity search demo) |
| `langchain_rag_app.py` | Final LCEL RAG chain with LLM and prompt guardrails |

**Run order:**

1. `python3 langchain_rag_create_corpus.py`
2. `python3 langchain_rag_ingest.py` (needs `OPENAI_API_KEY`)
3. `python3 langchain_rag_app.py`

![Production file layout — four Python scripts from create_corpus through ingest to LCEL rag_app](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-05-four-file-layout.png)

---

## Step 1 — Create the Policy Corpus

- **Official Definition:** A **corpus** is the collection of source documents your RAG system will search.
- **In Simple Words:** The **folder of policy files** your bot is allowed to read.
- **Real-Life Example:** HR keeps separate files for leave policy, travel policy, and code of conduct — same idea here with return, refund, shipping, warranty, and cancellation policies.

In production, data often arrives as **API text** or a **dictionary**, not ready-made files. The first script **writes** Markdown files to disk.

### Install dependencies (once per environment)

```bash
pip install langchain langchain-openai langchain-community langchain-chroma langchain-text-splitters chromadb
```

### Full code — `langchain_rag_create_corpus.py`

```python
from pathlib import Path  # Helps build folder and file paths in a clean way

BASE_DIR = Path("documents")  # Folder where all policy .md files will live

# BASE_DIR.mkdir(parents=True, exist_ok=True)  # Uncomment if the folder does not exist yet

DOCUMENTS = {  # Dictionary: file name -> policy text (simulates data from an API or database)
    "return_policy.md": """
# Return Policy

Most products can be returned within 10 days of delivery if unused and in original packaging.

Electronic items such as headphones, keyboards, smart watches, and mobile accessories
can be returned only within 7 days of delivery.

Open the Orders section and tap Request Return to start a return.
""",
    "refund_policy.md": """
# Refund Policy

Approved returns are refunded to the original payment method within 5 to 7 business days.

Partial refunds may apply if the product is damaged or missing accessories.
""",
    "shipping_policy.md": """
# Shipping Policy

Standard delivery takes 3 to 5 business days.

Orders above 499 rupees qualify for free standard shipping in eligible pin codes.

Express delivery is available in select metro cities within 24 to 48 hours.
""",
    "warranty_policy.md": """
# Warranty Policy

Electronics include a 12-month manufacturer warranty from the delivery date.

Upload invoice and serial number photo in Support to raise a warranty claim.

Physical damage and liquid damage are not covered.
""",
    "cancellation_policy.md": """
# Cancellation Policy

Orders can be cancelled before they are shipped from the warehouse.

After dispatch, cancellation is not possible; you may need to refuse delivery or process a return.
""",
}

for file_name, content in DOCUMENTS.items():  # Loop over each policy file name and its text
    file_path = BASE_DIR / file_name  # Build full path like documents/return_policy.md
    file_path.write_text(content.strip(), encoding="utf-8")  # Write text to disk using UTF-8 encoding
    print(f"Created: {file_path}")  # Confirm which file was written
```

**How the code works:**

- **`Path("documents")`** — target folder for all policies.
- **`DOCUMENTS` dictionary** — mimics real data that is not already saved as files.
- **`write_text(..., encoding="utf-8")`** — standard encoding for English Markdown.
- After this step, you have five `.md` files ready for LangChain loaders.

### Simple Activity — Inspect Your Corpus

Open `documents/return_policy.md` in your editor. Underline the **7-day** rule for electronics and the **10-day** rule for most products. You will query these lines later in the RAG demo.

---

## Step 2 — Load, Split, Embed, and Persist in Chroma

This is the **ingest** step: turn files into searchable vectors saved on disk.

### Document loaders

- **Official Definition:** A **document loader** reads external files and returns LangChain **Document** objects (text + metadata).
- **In Simple Words:** A **file reader** that speaks LangChain’s language.
- **Real-Life Example:** A librarian scanning each policy booklet into a standard catalogue card format.

| Class | What it does |
|---|---|
| **`DirectoryLoader`** | Loads **many files** from one folder |
| **`TextLoader`** | Reads **plain text / Markdown** from each matched file |

**Glob pattern `**/*.md`:** load only Markdown files in the folder (ignore other types).

You do not need to memorise every loader argument — understand the **step** (load folder → filter `.md` → read as text) and use LangChain docs when formats change (PDF, CSV, etc.).

### Text splitter — `RecursiveCharacterTextSplitter`

- **Official Definition:** A **recursive character text splitter** breaks text into chunks using character boundaries, trying sensible separators before hard cuts.
- **In Simple Words:** Smart scissors that prefer breaking at paragraphs or sentences, not mid-word when possible.
- **Real-Life Example:** Cutting a notebook into revision cards — you try to keep one full rule per card.

**Key parameters (class demo values):**

| Parameter | Demo value | Meaning |
|---|---|---|
| `chunk_size` | `800` | Maximum characters per chunk |
| `chunk_overlap` | `120` | ~15% overlap so sentences split across chunks still appear whole somewhere |
| `add_start_index` | `True` | Tags each chunk with its start position in the source file |

**Rule of thumb:** overlap is often **10–20%** of `chunk_size`. Overlap must be **smaller than** chunk size.

In the live demo, five small policies each became **one chunk** because `chunk_size=800` was larger than each file. Try `chunk_size=100` or `200` on your own to see multiple chunks per file.

### Embeddings — OpenAI `text-embedding-3-small`

- **Official Definition:** **Embeddings** map text to fixed-length vectors so similar meaning → nearby vectors.
- **In Simple Words:** Each paragraph becomes a **list of numbers**; similar paragraphs get similar lists.
- **Real-Life Example:** Words like *refund* and *return* sit closer on a map than *refund* and *cricket score*.

| OpenAI model | Vector size (approx.) |
|---|---|
| **text-embedding-3-small** | 1,536 numbers |
| **text-embedding-3-large** | 3,072 numbers |

**Same model rule:** use the **same** embedding model at ingest time and at query time.

Set your API key before ingest:

```bash
export OPENAI_API_KEY="your-key-here"
```

### Chroma — collections and persist

- **Official Definition:** **Chroma** is a vector database that stores embeddings and supports **similarity search**, with optional **local persistence**.
- **In Simple Words:** A **searchable filing cabinet** for chunk vectors on your laptop.
- **Real-Life Example:** Like tables in SQL — Chroma uses **collections** to group related vectors (here: `e_commerce_policy_docs`).

| Term | Meaning |
|---|---|
| **`persist_directory`** | Folder where Chroma **saves** vectors locally (`chroma_db`) |
| **`collection_name`** | Named bucket inside the database |
| **Persist** | **Save** so the next script can reload without re-embedding |

**Optional cleanup:** before re-ingest, delete old `chroma_db` with `shutil.rmtree` so stale vectors do not answer from outdated policy text.

![Ingest pipeline — DirectoryLoader, RecursiveCharacterTextSplitter, OpenAIEmbeddings, and persisted Chroma](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-06-ingest-pipeline.png)

### Full code — `langchain_rag_ingest.py`

```python
import shutil  # Used to optionally delete an old Chroma folder before re-ingest
from pathlib import Path  # Builds paths to documents and chroma_db folders

from langchain_chroma import Chroma  # LangChain wrapper around Chroma vector database
from langchain_community.document_loaders import DirectoryLoader, TextLoader  # Load many .md files from a folder
from langchain_openai import OpenAIEmbeddings  # OpenAI embedding model wrapper
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Splits long text into chunks

DATA_DIR = Path("documents")  # Folder containing policy .md files
CHROMA_DIR = Path("chroma_db")  # Local folder where Chroma will persist vectors
COLLECTION_NAME = "e_commerce_policy_docs"  # Collection name inside Chroma (like a table name)

EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI embedding model used in class

# --- Optional: remove old persisted data so re-ingest starts fresh ---
if CHROMA_DIR.exists():  # Only run cleanup if chroma_db already exists
    shutil.rmtree(CHROMA_DIR)  # Delete old vectors (use when policy files changed)

# --- 1) Load documents from folder ---
loader = DirectoryLoader(  # Reads every matching file in DATA_DIR
    str(DATA_DIR),  # Path to documents folder as a string
    glob="**/*.md",  # Load only Markdown files
    loader_cls=TextLoader,  # Treat each file as plain text / Markdown
    loader_kwargs={"encoding": "utf-8"},  # Read English text with UTF-8 encoding
)
documents = loader.load()  # Returns a list of LangChain Document objects
print(f"Original documents loaded: {len(documents)}")  # Usually 5 policy files

# --- 2) Split into chunks ---
text_splitter = RecursiveCharacterTextSplitter(  # Standard LangChain splitter
    chunk_size=800,  # Max characters per chunk (demo value from class)
    chunk_overlap=120,  # Shared tail between neighbouring chunks (~15%)
    add_start_index=True,  # Store where each chunk began in the source file
)
chunks = text_splitter.split_documents(documents)  # Apply splitting to loaded documents
print(f"Chunks generated: {len(chunks)}")  # May equal 5 if each policy is shorter than 800 chars

# --- 3) Create embedding model object ---
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)  # Wrapper that calls OpenAI embeddings API

# --- 4) Create Chroma vector store and add chunks ---
vector_store = Chroma(  # Connect to (or create) a persisted Chroma database
    collection_name=COLLECTION_NAME,  # Name of the collection for these policy chunks
    embedding_function=embeddings,  # Model used to embed chunks and later queries
    persist_directory=str(CHROMA_DIR),  # Save vectors under chroma_db/ for reuse
)
vector_store.add_documents(chunks)  # Embed each chunk and store in Chroma
print(f"Stored chunks in collection '{COLLECTION_NAME}' at '{CHROMA_DIR}'")
```

**How the code works:**

- **`DirectoryLoader`** — batch-loads all `*.md` policies.
- **`split_documents`** — turns each file into one or more chunks.
- **`OpenAIEmbeddings`** — converts text to vectors via API.
- **`Chroma(...)` + `add_documents`** — embeds and persists chunks locally.
- Re-running ingest after editing `return_policy.md` is required — raw file edits do **not** update vectors automatically.

### Simple Activity — Re-Ingest After a Policy Change

1. Change **7 days** to **70 days** for electronics in `return_policy.md`.
2. Run ingest again (with optional `shutil.rmtree`).
3. Ask the same electronics return question in the RAG app.
4. Notice the answer still says **7 days** until you re-ingest — this proves vectors lag behind raw files.

---

## Step 3 — Retriever Demo (Similarity Search Only)

- **Official Definition:** A **retriever** is an interface that accepts a query string and returns the most relevant document chunks from a vector store.
- **In Simple Words:** A **search button** for your policy database.
- **Real-Life Example:** Typing “return headphones” into an internal wiki search and getting the top three policy paragraphs.

**Retriever settings from class:**

- **`search_type="similarity"`** — rank by embedding distance.
- **`search_kwargs={"k": 3}`** — return **top 3** chunks.

### Full code — `langchain_rag.py` (optional retriever test)

```python
from pathlib import Path  # For chroma_db path

from langchain_chroma import Chroma  # Reload persisted Chroma store
from langchain_openai import OpenAIEmbeddings  # Same embedding model as ingest

CHROMA_DIR = Path("chroma_db")  # Must match ingest script
COLLECTION_NAME = "e_commerce_policy_docs"  # Must match ingest script
EMBEDDING_MODEL = "text-embedding-3-small"  # Must match ingest script

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)  # Same model as ingest (required)

vector_store = Chroma(  # Attach to existing persisted database (no re-embedding here)
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)

retriever = vector_store.as_retriever(  # Turn vector store into a retriever object
    search_type="similarity",  # Standard semantic similarity search
    search_kwargs={"k": 3},  # Return top 3 matching chunks
)

query = "What is the return window for electronics items?"  # Example user question
retrieved_docs = retriever.invoke(query)  # Run similarity search

print("User query:", query)  # Show what we searched for
print("Retrieved chunks:", len(retrieved_docs))  # Should print 3 (or fewer if corpus is tiny)
for i, doc in enumerate(retrieved_docs, start=1):  # Print a preview of each chunk
    print(f"\n--- Rank {i} ---")
    print(doc.page_content[:300])  # First 300 characters of chunk text
```

**How the code works:**

- Reloads **existing** Chroma data — no `add_documents` here.
- **`as_retriever()`** — LangChain helper so the same store plugs into LCEL chains.
- **`invoke(query)`** — embeds the query and fetches nearest chunk vectors.

---

## Step 4 — LCEL RAG Chain (Retrieve → Prompt → LLM → Answer)

### LangChain Expression Language (LCEL)

- **Official Definition:** **LCEL** composes LangChain components with the **pipe (`|`)** operator into a single runnable chain.
- **In Simple Words:** Connect blocks like LEGO: **output of step 1 → input of step 2**.
- **Real-Life Example:** Assembly line — washing, drying, packing happen in fixed order.

**RAG chain shape from class:**

```
{ context: retriever → format_docs, question: RunnablePassthrough() }
    → ChatPromptTemplate
    → ChatOpenAI
    → StrOutputParser()
```

![LCEL RAG chain — RunnablePassthrough, retriever context, ChatPromptTemplate, LLM, and StrOutputParser](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-07-lcel-rag-chain.png)

### `RunnablePassthrough`

- **Official Definition:** **`RunnablePassthrough`** forwards the input unchanged to the next step in the chain.
- **In Simple Words:** Pass the **original question as-is** to the prompt while the retriever fetches context in parallel.
- **Real-Life Example:** You ask a shopkeeper a question verbatim while they simultaneously pull the right policy file.

### Prompt guardrails (grounding behaviour)

The support prompt used in class:

- Answer **only** from retrieved context.
- If the answer is missing, say: **“I don’t know based on the provided documents.”**
- Do **not** use outside / general world knowledge.
- Mention **source file name** when possible.

This is a form of **prompt-level guardrailing** — like Amazon’s bot refusing random “latest AI news” questions.

**Citation / sourcing:** when the model cites `return_policy.md`, users trust the answer because it is tied to a real document, not a guess.

![Grounding and citations — electronics query returns cited answer; baby-items query returns honest refusal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session40/session40-08-grounding-citations.png)

### Full code — `langchain_rag_app.py`

```python
from pathlib import Path  # Path helper (optional for constants)

from langchain_chroma import Chroma  # Load persisted vector store
from langchain_core.output_parsers import StrOutputParser  # Convert LLM message to plain string
from langchain_core.prompts import ChatPromptTemplate  # Build chat-style prompt with variables
from langchain_core.runnables import RunnablePassthrough  # Pass question through unchanged
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # Chat model + embeddings

CHROMA_DIR = Path("chroma_db")  # Same folder as ingest
COLLECTION_NAME = "e_commerce_policy_docs"  # Same collection name as ingest
EMBEDDING_MODEL = "text-embedding-3-small"  # Same embedding model as ingest

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)  # Needed to query Chroma with same vectors

vector_store = Chroma(  # Reload persisted Chroma (no re-ingest in this file)
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)

retriever = vector_store.as_retriever(  # Retriever used inside the LCEL chain
    search_type="similarity",
    search_kwargs={"k": 3},
)

def format_docs(docs):  # Join retrieved Document objects into one context string
    return "\n\n".join(doc.page_content for doc in docs)  # Newline between chunks for readability

prompt = ChatPromptTemplate.from_template(  # Prompt with placeholders for context and question
    """You are a helpful customer support assistant for an e-commerce company.
Use only the retrieved context to answer the user's question.
If the answer is present in the context, answer clearly.
If the answer is not present in the context, say: I don't know based on the provided documents.
Do not use outside knowledge.
Mention the source file name wherever possible.

Context:
{context}

Question:
{question}
"""
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)  # Low temperature for factual policy answers

rag_chain = (  # Full LCEL RAG pipeline
    {
        "context": retriever | format_docs,  # Retrieve chunks and format as one string
        "question": RunnablePassthrough(),  # Forward user question unchanged
    }
    | prompt  # Insert context + question into template
    | llm  # Generate answer
    | StrOutputParser()  # Return plain string (note the parentheses)
)

question_1 = "What is the return window for electronics items?"  # Grounded query (in corpus)
answer_1 = rag_chain.invoke(question_1)  # Run retrieve + generate
print("\nQ:", question_1)
print("A:", answer_1)  # Expect 7-day electronics rule + source mention (return_policy.md)

question_2 = "What is the return window for baby items?"  # Out-of-corpus category
answer_2 = rag_chain.invoke(question_2)  # Run again with different query
print("\nQ:", question_2)
print("A:", answer_2)  # Expect honest uncertainty — baby items not defined in policies
```

**How the code works:**

- **`retriever | format_docs`** — fetch top-k chunks, merge into one context block.
- **`RunnablePassthrough()`** — same question string flows to `{question}` in the template.
- **Guardrail prompt** — blocks hallucinated baby-item rules when policy text is silent.
- **`StrOutputParser()`** — must be called with `()` (common syntax mistake in live demo).
- Changing policy files requires **re-running ingest**, not only the app.

### Simple Activity — Grounding Check (Two Queries)

Run the app with the two hard-coded questions above.

| Query | Expected behaviour |
|---|---|
| Electronics return window | Grounded answer (**7 days**), cites **`return_policy.md`** |
| Baby items return window | Does **not** invent a policy; admits information is missing |

Write one sentence for each: *Did the answer stick to retrieved context?*

### Grounding comparison — what class demonstrated

The session showed **grounded vs unanswerable** behaviour on **different** queries:

- **With relevant context** → correct, cited answer.
- **Without relevant context** → safe refusal phrase from the prompt.

A formal **same-question with-retrieval vs without-retrieval** side-by-side benchmark was **not** run in class. On your own, you can temporarily replace `{context}` with an empty string in the prompt and compare answers for the **same** question — that highlights how retrieval changes quality.

---

## Common Mistakes and Fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| `OpenAI API key is missing` | Key not exported | `export OPENAI_API_KEY=...` before ingest / app |
| Answer ignores edited `.md` file | Vectors not rebuilt | Re-run **ingest** after policy changes |
| `StrOutputParser` type error | Missing `()` | Use `StrOutputParser()` in the chain |
| Only 5 chunks for 5 files | `chunk_size` larger than files | Lower `chunk_size` (e.g. 100–200) to practise multi-chunk splits |
| Wrong or vague matches | Chunks too large / no overlap | Tune `chunk_size` and `chunk_overlap` |
| Retrieval quality poor | Different embedding model at query time | Use the **same** `EMBEDDING_MODEL` everywhere |

---

## How This Connects Forward

- **Agents + RAG:** upcoming work can attach a **retrieval tool** so agents fetch policies before answering.
- **Guardrails module:** prompt rules today are a light version of broader safety and routing controls.
- **Evaluation:** compare answers with retrieval on vs off, and score citation accuracy on fixed test questions.

---

## Key Takeaways

- **RAG** lets an LLM answer from **your** policies via retrieve-then-generate, not by retraining on gigabytes of data.
- **LangChain** packages loaders, splitters, embeddings, Chroma, retrievers, and **LCEL** chains into a repeatable pipeline.
- **Ingest once, query many times** — persist Chroma locally; re-ingest when source documents change.
- **Chunk size and overlap** control retrieval quality; demo used **800 / 120** on a small corpus.
- **Prompt guardrails** plus **citations** produce trustworthy support answers and honest “I don’t know” when context is missing.
- **Four-file layout** (`create_corpus` → `ingest` → optional retriever test → `rag_app`) mirrors production structure.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `langchain_rag_create_corpus.py` | File | Writes policy `.md` files from a dictionary |
| `langchain_rag_ingest.py` | File | Load → split → embed → persist in Chroma |
| `langchain_rag_app.py` | File | LCEL RAG chain with LLM + guardrail prompt |
| `DirectoryLoader` | Class | Load many files from a folder |
| `TextLoader` | Class | Read plain text / Markdown files |
| `glob="**/*.md"` | Config | Only ingest Markdown files |
| `RecursiveCharacterTextSplitter` | Class | Split documents into overlapping chunks |
| `chunk_size` / `chunk_overlap` | Params | Max chunk length; repeated margin between chunks |
| `add_start_index=True` | Param | Track chunk position in source file |
| `OpenAIEmbeddings` | Class | OpenAI embedding wrapper |
| `text-embedding-3-small` | Model | 1,536-dim embedding model used in demo |
| `Chroma` | Class | LangChain vector store with local persist |
| `persist_directory` | Param | Folder where Chroma saves vectors |
| `collection_name` | Param | Named collection inside Chroma |
| `vector_store.add_documents` | Method | Embed and store chunks |
| `as_retriever()` | Method | Expose similarity search on the store |
| `search_kwargs={"k": 3}` | Config | Return top 3 chunks |
| **LCEL** | Concept | Chain components with `\|` pipe operator |
| `RunnablePassthrough` | Class | Forward input unchanged (user question) |
| `ChatPromptTemplate` | Class | Prompt with `{context}` and `{question}` slots |
| `StrOutputParser()` | Class | LLM output → plain string |
| **RAG** | Concept | Retrieval-Augmented Generation |
| **Citation / sourcing** | Concept | Name the policy file behind an answer |
| **Guardrail (prompt-level)** | Concept | “Use only retrieved context” rules |
| `export OPENAI_API_KEY=...` | Shell | Authenticate OpenAI calls |
| `shutil.rmtree(chroma_db)` | Code | Optional full reset before re-ingest |
