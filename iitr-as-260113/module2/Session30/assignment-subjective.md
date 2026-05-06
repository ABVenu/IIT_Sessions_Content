# Assignment Subjective: Build a Campus Policy RAG Assistant

---

Your institute has separate **PDF documents** for hostel rules, refund rules, library rules, and course withdrawal rules. Students keep asking repeated questions such as:

- *"Can I get a refund after dropping a course?"*
- *"What is the deadline for returning a library book?"*
- *"Are hostel visitors allowed on weekends?"*

Build a **Python-based RAG assistant** that reads multiple PDF policy documents and answers student questions using **only the retrieved policy context**.

---

### Requirements

Create a project named **`campus_policy_rag`** with the following structure:

```text
campus_policy_rag/
├── policy_documents/
│   ├── hostel_policy.pdf
│   ├── refund_policy.pdf
│   └── library_policy.pdf
├── requirements.txt
├── campus_policy_rag.py
└── chroma_db/              ← created automatically by ChromaDB
```

> You may create short sample PDFs yourself if real institute policy PDFs are not available. Each PDF should contain at least **2 to 3 short paragraphs** so the pipeline has enough content to retrieve from.

---

### Implementation Requirements

Your implementation must include:

1. A **`requirements.txt`** file containing the required libraries:
   - `openai`
   - `chromadb`
   - `pypdf`

2. A Python file named **`campus_policy_rag.py`**.

3. A function to **infer the policy type** from the PDF filename — e.g. `hostel`, `refund`, `library`, or `general`.

4. A function to **load all PDF files** from the `policy_documents/` folder using **`PdfReader`**.

5. A function to **clean extracted text** by removing extra newlines and repeated spaces.

6. A function to **split text into fixed-size overlapping chunks**:
   - Default **chunk size**: between **100 and 200 words**
   - **Overlap**: between **10% and 20%** of the chunk size

7. A function to **generate embeddings** using any LLM provider's embedding model — for example, OpenAI's **`text-embedding-3-small`**, Google Gemini, Groq, or any other provider you have API access to.

8. A **persistent ChromaDB collection** that stores for every chunk:
   - The **chunk text**
   - The **embedding vector**
   - **Metadata** — source file, page number, and policy type

9. A **retrieval function** that:
   - Converts the student query into an **embedding**
   - Retrieves the **top 3 relevant chunks** from ChromaDB

10. A **prompt-building function** that instructs the LLM to:
    - Answer **only** from the retrieved policy context
    - Say `"I don't have that information."` if the context does not contain the answer
    - Keep the response **simple and student-friendly**

11. A final **`answer_question()`** function that combines retrieval and generation end-to-end.

12. A **`main` block** that:
    - Builds the **knowledge base** (pre-processing phase)
    - Runs at least **3 test student queries**
    - Prints the retrieved answer for each query

---

### Expected Input

1. **PDF files** placed inside the `policy_documents/` folder.
2. **Student questions** written inside the test query list in the Python file.
3. Your **LLM provider API key** set as an environment variable in the terminal.

> You are free to use **any LLM provider** you have access to — OpenAI, Google Gemini, Groq, Mistral, Cohere, or any other. The logic remains the same regardless of which provider you choose.

```bash
# Example using OpenAI
export OPENAI_API_KEY="your-api-key-here"

# Example using Gemini
export GOOGLE_API_KEY="your-api-key-here"

# Example using Groq
export GROQ_API_KEY="your-api-key-here"

python3 campus_policy_rag.py
```

---

### Expected Output

Your output should confirm that the knowledge base was built and that each question was answered using retrieved context.

```text
Vector DB ready. Collection: campus_policies
Loaded 2 pages from: refund_policy.pdf
Loaded 2 pages from: library_policy.pdf
Loaded 1 page from: hostel_policy.pdf
Total chunks created: 8
Successfully stored 8 chunks in vector database.

User Query: Can I get a refund after dropping a course?
Retrieved 3 relevant chunks.
Answer: According to the refund policy, ...
```

---

### Important Constraints

- Do **not** hardcode policy content inside Python lists.
- Do **not** hardcode any API key (OpenAI, Gemini, Groq, or otherwise) in the Python file — always read it from an environment variable.
- Do **not** send the entire PDF text to the LLM for every query.
- The final answer must come **only from retrieved policy chunks** — not from general knowledge.
- Store **metadata** with every chunk so the source of each retrieved answer can be traced.

---

### Submission Instructions

- Create a GitHub repository named **`agentic-systems`** (if already created, use the same) — clone it locally (ignore if already cloned).
- Inside the repository, create a folder called **`module2`** (ignore if already present).
- Inside `module2`, create a folder called **`Session30`**.
- Place the complete **`campus_policy_rag`** project folder (with all files and the folder structure shown above) inside `Session30`.
- Add ignorable files (`.env`, API key configs) to **`.gitignore`** — do **not** commit them.
- Run `git add`, `git commit`, and `git push` to publish your code.
- Submit the link to the **`Session30`** folder (or the `campus_policy_rag` sub-folder) on GitHub — **not** the root repository link.

---

### Answer Explanation

An ideal solution follows the **production RAG pipeline** covered in this session. The pipeline has two distinct phases — a one-time **pre-processing phase** that prepares the knowledge base, and a **runtime phase** that runs every time a student asks a question.

---

#### Phase 1 — Pre-Processing (Run Once)

**Step 1 — Document Loading (Ingestion)**

The first task is to scan the `policy_documents/` folder and load every PDF file found inside it. The program should not be written for one specific file — it must automatically discover all PDFs in the folder. For each PDF, the `PdfReader` class from the `pypdf` library is used to open the file and read it **page by page**. Each page's raw text is extracted and paired with **metadata** — the source file path, the page number within the PDF, and the inferred policy type (e.g. `hostel`, `refund`, `library`). The policy type is inferred from the filename itself so no manual tagging is needed.

```python
import os
from pypdf import PdfReader

def infer_policy_type(filename):
    name = filename.lower()
    if "hostel" in name:
        return "hostel"
    elif "refund" in name:
        return "refund"
    elif "library" in name:
        return "library"
    else:
        return "general"

def load_pdf_file(file_path):
    documents = []
    policy_type = infer_policy_type(os.path.basename(file_path))
    reader = PdfReader(file_path)
    for page_num, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text()
        if not raw_text:
            continue
        clean = clean_text(raw_text)
        if clean:
            metadata = {
                "source": file_path,
                "page": page_num,
                "policy_type": policy_type
            }
            documents.append({"text": clean, "metadata": metadata})
    return documents

def load_all_documents(folder_path):
    all_documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            docs = load_pdf_file(file_path)
            all_documents.extend(docs)
            print(f"Loaded {len(docs)} pages from: {filename}")
    print(f"Total documents loaded: {len(all_documents)}")
    return all_documents
```

---

**Step 2 — Cleaning**

Raw text extracted from PDFs is messy. It contains extra blank lines, repeated spaces, stray newline characters (`\n`), and sometimes page headers or footers. Before storing anything, this noise must be removed. The cleaning step replaces all newline characters with spaces and collapses multiple consecutive spaces into a single space. The result is a clean, single-line block of text for each page — ready to be chunked.

```python
import re

def clean_text(raw_text):
    text = raw_text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text
```

---

**Step 3 — Chunking with Overlap**

Storing an entire PDF page as one unit is impractical. If a page has 500 words and a student asks a very specific question, the retriever would return 500 words of context for that one match — far more than needed. Instead, each page is split into **fixed-size overlapping chunks**.

A good chunk size for this task is between **100 and 200 words**. The overlap — typically **10% to 20% of the chunk size** — means the last few words of one chunk are repeated at the beginning of the next. This ensures that sentences which fall across a chunk boundary are not cut off and stripped of meaning. Think of it like a handover between shifts — the incoming shift repeats the last few minutes of the previous shift to avoid missing anything critical.

Each chunk is stored as a dictionary containing its text, its metadata (inherited from the parent document), and a unique ID.

```python
import random

def chunk_text(text, chunk_size=120, overlap=30):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def create_chunks(documents, chunk_size=120, overlap=30):
    all_chunks = []
    for doc in documents:
        text_chunks = chunk_text(doc["text"], chunk_size, overlap)
        for i, chunk_content in enumerate(text_chunks):
            chunk_id = str(random.randint(100000, 999999))
            all_chunks.append({
                "id": chunk_id,
                "text": chunk_content,
                "metadata": doc["metadata"],
                "chunk_index": i
            })
    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks
```

---

**Step 4 — Generating Embeddings**

Plain text cannot be compared mathematically. To find which chunk is most similar to a student's question, both the chunks and the question must be converted into **vectors** — lists of numbers that represent meaning in a mathematical space. This is done using OpenAI's **`text-embedding-3-small`** model, which produces a **1536-dimensional vector** for each piece of text. Chunks that talk about similar topics will produce vectors that are mathematically close to each other.

```python
from openai import OpenAI

client = OpenAI()
EMBEDDING_MODEL = "text-embedding-3-small"

def create_embeddings(texts):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]
```

---

**Step 5 — Storing in ChromaDB**

Once embeddings are generated, everything is stored together in a **persistent ChromaDB collection**. For each chunk, three things are stored: the **chunk text** (so it can be shown to the LLM later), the **embedding vector** (so similarity search can work), and the **metadata** (so the source of any retrieved chunk can be traced back to its original PDF and page). Using a persistent client means this data survives program restarts — you do not need to re-embed the documents every time a student asks a question.

```python
import chromadb

def setup_vector_db(db_path="./chroma_db", collection_name="campus_policies"):
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name=collection_name)
    print(f"Vector DB ready. Collection: {collection_name}")
    return collection

def index_chunks(chunks, collection):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = create_embeddings(texts)
    ids = [chunk["id"] for chunk in chunks]
    metadatas = [chunk["metadata"] for chunk in chunks]
    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )
    print(f"Successfully stored {len(chunks)} chunks in vector database.")
```

---

#### Phase 2 — Runtime (Runs for Every Student Query)

**Step 6 — Query Embedding and Retrieval**

When a student types a question, the question is first converted into an embedding using the same `text-embedding-3-small` model. This query vector is then compared against all stored chunk vectors in ChromaDB using **similarity search**. ChromaDB returns the **top 3 chunks** whose vectors are closest to the query vector — meaning they are the most semantically relevant to the student's question.

```python
def retrieve_chunks(query, collection, top_k=3):
    query_embedding = create_embeddings([query])[0]
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    retrieved = []
    if results["documents"] and results["documents"][0]:
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            retrieved.append({"text": doc, "metadata": meta})
    return retrieved
```

---

**Step 7 — Prompt Construction**

The three retrieved chunks are combined into a single **context block**. A structured prompt is then built that contains: a system instruction telling the LLM to answer only from the provided context, the context block itself, and the student's original question. The prompt also explicitly instructs the LLM to say *"I don't have that information."* if the answer cannot be found in the context — preventing hallucination.

```python
def build_prompt(query, retrieved_chunks):
    context = "\n\n".join([chunk["text"] for chunk in retrieved_chunks])
    prompt = f"""You are a helpful student support assistant for a college.

Answer the student's question using ONLY the policy information provided below.
Do NOT make up any details. If the answer is not in the context, say: "I don't have that information."
Keep your answer simple, clear, and student-friendly.

--- POLICY CONTEXT ---
{context}
--- END OF CONTEXT ---

Student Question: {query}

Answer:"""
    return prompt
```

---

**Step 8 — Answer Generation**

The constructed prompt is sent to the LLM (e.g. `gpt-4o`). The LLM reads the retrieved context and generates a clear, student-friendly answer. It does not draw on general knowledge — it is constrained to the policy content that was retrieved. The final answer is printed to the screen.

```python
LLM_MODEL = "gpt-4o"

def generate_answer(query, retrieved_chunks):
    prompt = build_prompt(query, retrieved_chunks)
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful college student support assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content

def answer_question(query, collection, top_k=3):
    print(f"\nUser Query: {query}")
    print("-" * 50)
    retrieved = retrieve_chunks(query, collection, top_k=top_k)
    if not retrieved:
        return "I'm sorry, I couldn't find relevant information to answer your question."
    print(f"Retrieved {len(retrieved)} relevant chunks.")
    return generate_answer(query, retrieved)
```

---

**Putting It All Together — The `main` Block**

```python
if __name__ == "__main__":
    # Pre-processing phase — run once
    collection = setup_vector_db()
    documents = load_all_documents("./policy_documents")
    chunks = create_chunks(documents)
    index_chunks(chunks, collection)

    # Runtime phase — one call per student query
    test_queries = [
        "Can I get a refund after dropping a course?",
        "What is the deadline for returning a library book?",
        "Are hostel visitors allowed on weekends?"
    ]

    for query in test_queries:
        answer = answer_question(query, collection)
        print(f"\nAnswer: {answer}")
        print("=" * 60)
```

---

#### Retriever vs Generator — The Key Separation

A strong submission will clearly separate the pipeline into two components:

| Component | Responsibility |
|---|---|
| **Retriever** | Embeds the query → searches ChromaDB → returns top-K relevant chunks |
| **Generator** | Takes chunks + query → builds prompt → calls the LLM → returns the final answer |

The **Retriever** works purely with math — it does not understand language, it compares vectors. The **Generator** works purely with language — it does not search databases, it reads context and writes a response. Keeping these two responsibilities separated makes the system modular and easy to debug or improve.

Alternative valid approaches may use slightly different function names or chunk sizes, as long as the implementation follows the same **RAG workflow** and stays within the taught tools and concepts.
