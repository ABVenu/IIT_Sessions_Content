# Building a RAG Pipeline — From Basics to Production

---

## What You Will Learn in This Session

In the previous session, you built a **minimal RAG (Retrieval-Augmented Generation) system** from scratch. You learned the key components — the **Retriever** and the **Generator** — and built a small end-to-end flow where customer queries were matched against a few policy snippets stored as simple Python strings or lists. You also saw how injecting retrieved context into LLM prompts produces much more accurate, grounded answers compared to asking the LLM directly.

This session picks up from exactly that point and takes a big leap forward. Instead of a handful of hardcoded strings, you will work with **real PDF files** — just like companies do in the real world. By the end of this session, you will have built a complete, **production-style multi-document RAG pipeline** for an e-commerce customer support assistant.

**Here is what you will do step by step:**
- Load real policy PDF documents from a folder
- Parse and clean raw text from those documents
- Split documents into smart, overlapping chunks
- Convert chunks into embeddings and store them in ChromaDB
- Retrieve the most relevant chunks for any user query
- Build a prompt and generate a user-friendly final answer

---

## Why Strings Are Not Enough — The Real World Problem

In the last session, the policy data looked like this inside the Python program — a simple list of strings:

```python
policies = [
    "Return policy: Items can be returned within 30 days.",
    "Refund policy: Refunds are processed in 5-7 business days.",
    "Shipping policy: Free shipping on orders above Rs 500."
]
```

This works fine as a learning exercise. But think about how a real company stores its policies. **A company like Amazon or Flipkart does not type its policies into a Python list.** Its policies are written in documents — most commonly **PDF files** — that can be many pages long and are updated regularly.

- Real policy documents can be tens or hundreds of pages long.
- Companies usually have many separate documents — return policy, refund policy, shipping policy, warranty policy, and more.
- These documents are stored on servers, laptops, or cloud storage — **not inside Python code**.

So the goal of this session is to answer one big question: **How do you read real PDF documents and use them inside a RAG pipeline?**

![From company PDF bundles to ingestion in code — moving beyond toy string lists toward real documents](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-02-pdf-vs-strings-real-world.png)

---

## The Complete Production RAG Workflow

Before writing a single line of code, it is very important to understand the complete picture. Think of this as the **blueprint** of everything you are going to build.

Here is the full step-by-step workflow of a production RAG pipeline:

```
[PDF Documents in a Folder]
         ↓
  Step 1: Document Loading / Ingestion
         ↓
  Step 2: Parsing and Cleaning
         ↓
  Step 3: Chunking
         ↓
  Step 4: Generate Embeddings
         ↓
  Step 5: Store in Vector Database (ChromaDB)
         ↓
  --- Pre-processing is complete. System is ready. ---
         ↓
  Step 6: User sends a Query
         ↓
  Step 7: Convert Query to Embedding
         ↓
  Step 8: Similarity Search → Top-K Chunks
         ↓
  Step 9: Build Prompt (context + query)
         ↓
  Step 10: LLM Generates Final Answer
         ↓
  [User gets a helpful, grounded response]
```

![Visual overview — offline preprocessing (Steps 1–5) versus runtime querying (Steps 6–10) across a multi-document ecommerce RAG stack](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-01-rag-pipeline-overview.png)

**Steps 1 to 5** are the **pre-processing phase**. The user is not involved here at all. You are just preparing the system — loading, cleaning, chunking, embedding, and storing all the policy documents once.

**Steps 6 to 10** happen every time a user asks a question. This is the **runtime phase** — retrieve relevant content and generate a polished answer.

---

## Step 1 — Document Loading (Ingestion)

### What Is Document Ingestion?

- **Official Definition:** Document ingestion is the process of loading raw documents from an external source (like a file system or cloud) into your Python program so they can be processed.
- **In Simple Words:** Think of it like picking up physical files from a cabinet and bringing them to your desk so you can read them.
- **Real-Life Example:** A bank clerk who goes to a file room, picks up all the customer folders, and brings them to their desk to process — that is ingestion.

### The Most Common Document Format: PDF

In the real world, most company documents are stored as **PDF files**. PDFs are preferred because:
- They are universally readable on any device.
- They preserve formatting (fonts, tables, layouts).
- They can be secured with passwords.

To read PDF files in Python, you use a library called **pypdf**.

- **Official Definition:** `pypdf` is a Python library that allows you to open, read, and extract text from PDF files.
- **In Simple Words:** It is like a pair of glasses that helps your Python program read a PDF document, page by page.
- **Inside `pypdf`**, there is a class called **`PdfReader`** which reads the PDF and gives you access to each page.

> **Note on OCR (Optical Character Recognition):** Sometimes PDFs contain images with text inside them (for example, scanned documents). Normal PDF readers cannot read text from images. OCR technology is used for this. Nowadays, you can pass an image directly to a powerful LLM (like GPT-4o) and ask it to read the text — this is one of the most modern approaches for image-based text extraction.

---

## Step 2 — Parsing and Cleaning

### Why Is Cleaning Needed?

Raw documents are **messy**. When you extract text from a PDF, you do not just get clean sentences. You get everything — company headers, footers, extra blank lines, page numbers, special characters, and random whitespace.

Think of it like this: **imagine photocopying a document that has sticky notes, highlighter marks, and scribbles all over it.** You only want the actual content, not all the noise around it.

**Common types of mess found in raw PDF text:**
- Company name and address repeated in the header of every page
- Page numbers like "Page 1 of 12" at the bottom of every page
- Extra blank lines between paragraphs
- Multiple spaces between words
- Strange characters from PDF encoding

### What Parsing and Cleaning Does

**Parsing** means reading the data and structuring it in a usable format. **Cleaning** means removing all the redundant, noisy data so only useful content remains.

- Removing extra spaces and newline characters (`\n`) is done using Python's `.replace()` and `.strip()` methods.
- Headers and footers can be identified by their position (first or last line of a page) and removed.

![Turning noisy PDF extracts into tidy text before chunking — parsing structures the data while cleaning strips headers, footers, and stray whitespace](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-03-text-cleaning-pipeline.png)

---

## Step 3 — Chunking: Splitting Documents into Pieces

### Why Can't You Store the Whole Document?

This is one of the most important concepts of this session. Suppose your return policy PDF has 200 pages. You store the entire 200-page document as one single item in the vector database.

Now, a user asks: *"What is the deadline for returning a product?"*

You find the 200-page document as the relevant match and send **all 200 pages** to the LLM as context. **Two serious problems happen:**
1. **The context window fills up immediately.** LLMs have a limit on how much text they can process at once. Sending 200 pages in one go will exceed that limit.
2. **The cost explodes.** You pay for LLM usage by the number of tokens (words). Sending hundreds of pages with every user query wastes enormous amounts of money.

Additionally, searching through one massive document to find relevant content is slow and imprecise. **The solution is to split every document into smaller, manageable pieces called chunks.**

- **Official Definition:** Chunking is the process of splitting a large document into smaller segments so that each segment can be stored, searched, and retrieved independently.
- **In Simple Words:** It is like dividing a thick textbook into separate chapters or topics — smaller pieces are easier to find and use.
- **Real-Life Example:** A dictionary is too big to read in one go to find one word. So you go to the correct alphabetical section. Chunking is the same idea — break the content so finding information is fast and targeted.

### Fixed-Size Chunking

The simplest and most widely-used chunking strategy is **fixed-size chunking**.

**How it works:**
- You decide a fixed number of words per chunk, for example, **120 words**.
- Words 1–120 go into Chunk 1.
- Words 121–240 go into Chunk 2.
- Words 241–360 go into Chunk 3, and so on.

**Advantages:**
- Very simple to implement.
- Predictable chunk sizes — easy to control storage and retrieval costs.

**Disadvantage:**
- A sentence might start in Chunk 1 and end in Chunk 2. When you split mid-sentence, you lose the **context** — the meaning is broken across two chunks.

### Chunk Overlap — The Fix for Lost Context

The solution to the mid-sentence problem is **chunk overlap**.

- **Official Definition:** Chunk overlap is a technique where the last N words of the previous chunk are repeated at the beginning of the next chunk, ensuring context is preserved across chunk boundaries.
- **In Simple Words:** Each new chunk "remembers" the last few words of the previous chunk so there is no abrupt break in meaning.

**Real-Life Analogy (from the session):**
> Imagine you are leaving your job at Microsoft. Your manager knows you have critical knowledge about a project. So, before you leave, your manager arranges for your replacement to work **alongside you for one week** — overlapping your last week. During that overlap, you share your knowledge. The replacement now has context about the previous work before taking over fully. This is exactly what chunk overlap does — the next chunk inherits context from the end of the previous one.

![Fixed-size chunks with overlapping tails so meaning is not abruptly cut mid-thought across chunk boundaries](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-04-chunk-overlap-explained.png)

**Practical overlap guidelines:**
- Overlap is typically **10–20% of the chunk size**.
- If your chunk size is 120 words, an overlap of **20–30 words** is a good starting point.
- Overlap is a trade-off: it means a small amount of duplicate data, but the benefit of preserved context far outweighs this cost.

### How to Choose Chunk Size

There is **no single correct answer** for the ideal chunk size. It depends on your documents and your use case.

- **Very small chunks** (e.g., 50 words): Fast to search, but too little context per chunk → poor answer quality.
- **Very large chunks** (e.g., 1,000 words): Good context, but slow to search and expensive to send to LLM.
- **Sweet spot for small-to-medium documents:** **100 to 200 words** per chunk with an overlap of **10–20%**.

**The right approach is experimentation:**
1. Start with a reasonable guess (e.g., 120 words).
2. Run queries and check the quality of the answers.
3. If answers are poor, adjust the chunk size (increase or decrease) and try again.
4. Repeat until the answers are consistently good.

### Other Chunking Strategies (Brief Overview)

| Strategy | How It Works | Pros | Cons |
|---|---|---|---|
| **Fixed-Size Chunking** | Split by exact word count | Simple, fast to implement | Can break sentences mid-way |
| **Semantic Chunking** | Split based on meaning / sentence boundaries | Preserves context better | Very complex to implement |
| **Hierarchical Chunking** | Split by headings/topics/paragraphs | Natural document structure | Uneven chunk sizes |

**For this course, we use fixed-size chunking with overlap** — it is straightforward, effective, and the industry standard for most use cases.

---

## Step 4 — Generating Embeddings

After chunking, each chunk is a piece of plain text. But computers cannot directly compare two pieces of text to find out which one is most similar to a query. For that, you need to convert text into **numbers** — specifically into **vectors** called embeddings.

- **Official Definition:** An embedding is a list (vector) of numbers that represents the meaning of a piece of text in a mathematical space. Text with similar meanings will have embeddings that are close together in this space.
- **In Simple Words:** Think of it as giving each chunk a unique address on a map. Chunks that talk about similar topics will have addresses very close to each other.
- **Real-Life Example:** Imagine plotting cities on a map. Delhi and Noida will be very close. Mumbai and Delhi will be far apart. Embeddings do the same for text — "refund in 7 days" and "money back in a week" will be plotted very close together.

### Embedding Model Used

For this pipeline, you use OpenAI's **text-embedding-3-small** model.

| Model | Dimensions | Use Case |
|---|---|---|
| `text-embedding-3-small` | **1536** | Balanced — good quality, lower cost |
| `text-embedding-3-large` | **3072** | Higher quality, higher cost |

**Dimensions** simply means how many numbers are in the vector. More dimensions = more detailed representation of meaning = higher cost.

![Semantic neighbors in embedding space — paraphrases sit close together so similarity search surfaces the right snippets](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-05-embeddings-semantic-neighbors.png)

---

## Step 5 — Storing in Vector Database (ChromaDB)

Once you have embeddings, you store them in a **vector database**. For this project, you use **ChromaDB**.

- **Official Definition:** A vector database is a specialized database that stores embeddings (vectors) and allows extremely fast similarity searches — finding which stored vectors are most similar to a given query vector.
- **In Simple Words:** It is like a super-smart filing cabinet. You describe what you are looking for, and it instantly finds the files that are most similar to your description.

### What Gets Stored for Each Chunk?

For every chunk, three things are stored together:

| What is stored | Why it is stored |
|---|---|
| **The text of the chunk** | To return the actual content when retrieved |
| **The embedding vector** | To compare with the query embedding during search |
| **Metadata** | Extra information like file name, page number, policy type (refund / return / shipping) |

**Metadata** is very powerful — it lets you filter results. For example, if a user asks only about refund policies, you can filter the search to only look inside refund-related chunks.

![Vector databases like ChromaDB store each chunk with its embedding vector and metadata tags for lightning-fast similarity search plus optional filtering](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-06-chromadb-storage-retrieval.png)

---

## Setting Up the Project

### Project Structure

Before writing code, you set up the project folder like this:

```
advanced_rag/
│
├── policy_documents/
│   ├── return_policy.pdf
│   ├── refund_policy.pdf
│   └── shipping_policy.pdf
│
├── requirements.txt
├── advanced_ecommerce_rag.py
└── chroma_db/          ← (created automatically by ChromaDB)
```

### Installing Dependencies with requirements.txt

Instead of installing libraries one by one, you create a **`requirements.txt`** file listing all your dependencies. Then you install everything in one command.

```
# requirements.txt
openai
chromadb
pypdf
```

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all dependencies at once
pip3 install -r requirements.txt
```

**Why `requirements.txt` matters:**
- Saves time — one command installs everything.
- Makes your project shareable — anyone who clones your project can set it up instantly.
- Industry standard practice in all Python projects.

### Setting the API Key as an Environment Variable

**Never hardcode your API key inside your Python file.** Anyone who reads your code will see your key.

```bash
# Set the API key as an environment variable in your terminal
export OPENAI_API_KEY="your-api-key-here"
```

When you create the OpenAI client without passing a key, it **automatically reads** the `OPENAI_API_KEY` variable from your environment.

```python
from openai import OpenAI

# OpenAI client automatically picks up the API key from the environment variable
client = OpenAI()
```

---

## The Full Code — Advanced E-Commerce RAG Pipeline

Below is the complete, fully-commented code for the production-style RAG pipeline built in this session.

```python
# =====================================================================
# Advanced E-Commerce RAG Pipeline
# Handles multiple PDF policy documents end-to-end
# =====================================================================

import os                  # to work with file paths and folders
import re                  # for text cleaning using regular expressions
import random              # for generating unique chunk IDs
from openai import OpenAI  # OpenAI client for embeddings and chat
from pypdf import PdfReader  # library to read PDF files page by page
import chromadb            # vector database for storing and searching embeddings

# ---- Setup: Create the OpenAI client ----
# The client automatically reads OPENAI_API_KEY from environment variables
client = OpenAI()

# ---- Constants: Define model names in one place ----
# Change the model name here once if you ever need to switch models
LLM_MODEL = "gpt-4o"
EMBEDDING_MODEL = "text-embedding-3-small"

# =====================================================================
# SECTION 1: DOCUMENT LOADING AND CLEANING
# =====================================================================

def infer_policy_type(filename):
    """
    Figures out the type of policy from the file name.
    For example: 'refund_policy.pdf' → 'refund'
    """
    name = filename.lower()  # convert filename to lowercase for easy matching
    
    if "return" in name:
        return "return"          # file talks about return policy
    elif "refund" in name:
        return "refund"          # file talks about refund policy
    elif "shipping" in name:
        return "shipping"        # file talks about shipping policy
    elif "warranty" in name:
        return "warranty"        # file talks about warranty policy
    elif "cancel" in name:
        return "cancellation"    # file talks about cancellation policy
    else:
        return "general"         # default type if none of the above match


def clean_text(raw_text):
    """
    Cleans raw text extracted from a PDF by removing noise.
    - Replaces newline characters with spaces
    - Removes extra/multiple spaces
    """
    # Step 1: Replace all newline characters (\n) with a single space
    text = raw_text.replace("\n", " ")
    
    # Step 2: Use regex to replace multiple consecutive spaces with one space
    text = re.sub(r'\s+', ' ', text)
    
    # Step 3: Strip leading and trailing whitespace
    text = text.strip()
    
    return text  # return the cleaned, single-line text


def make_document(text, metadata):
    """
    Creates a standard document dictionary for every page.
    Having a consistent structure makes it easy to handle thousands of documents.
    """
    return {
        "text": text,          # the actual cleaned text of this page
        "metadata": metadata   # extra info like file path, page number, policy type
    }


def load_pdf_file(file_path):
    """
    Loads a single PDF file and returns a list of documents (one per page).
    Each document contains the page's text and metadata.
    """
    documents = []          # empty list to collect all page documents
    policy_type = infer_policy_type(os.path.basename(file_path))  # get policy type from filename
    
    # Open and read the PDF file using PdfReader
    reader = PdfReader(file_path)
    
    # Iterate through every page of the PDF (enumerate gives index + value)
    for page_num, page in enumerate(reader.pages, start=1):
        
        raw_text = page.extract_text()  # extract raw text from this page
        
        if not raw_text:
            continue  # skip empty pages (some PDFs have blank pages)
        
        clean = clean_text(raw_text)  # remove noise from the extracted text
        
        if clean:  # only add the document if there is actual content
            metadata = {
                "source": file_path,         # full path of the source PDF file
                "page": page_num,            # page number within the PDF
                "policy_type": policy_type   # type of policy (refund/return/shipping)
            }
            documents.append(make_document(clean, metadata))  # add to list
    
    return documents  # return all page-documents from this PDF


def load_all_documents(folder_path):
    """
    Loads ALL PDF files from a given folder automatically.
    You just point it to a folder — it finds every PDF and loads all pages.
    No need to call load_pdf_file manually for each file.
    """
    all_documents = []  # master list to collect documents from all PDFs
    
    # Walk through every file in the given folder
    for filename in os.listdir(folder_path):
        
        if filename.endswith(".pdf"):  # only process PDF files, ignore others
            
            file_path = os.path.join(folder_path, filename)  # build full path
            docs = load_pdf_file(file_path)                  # load that PDF
            all_documents.extend(docs)  # add all pages from this PDF to master list
            print(f"Loaded {len(docs)} pages from: {filename}")
    
    print(f"\nTotal documents loaded: {len(all_documents)}")
    return all_documents  # return all documents from all PDFs in the folder


# =====================================================================
# SECTION 2: CHUNKING
# =====================================================================

def chunk_text(text, chunk_size=120, overlap=30):
    """
    Splits a single piece of text into overlapping word-based chunks.
    
    chunk_size = 120 → each chunk has up to 120 words
    overlap = 30    → each new chunk starts 30 words before the previous chunk ended
    
    Example with chunk_size=120, overlap=30:
    - Chunk 1: words 1 to 120
    - Chunk 2: words 91 to 210  (starts at 120 - 30 = 90, i.e. index 90)
    - Chunk 3: words 181 to 300 (starts at 210 - 30 = 180, i.e. index 180)
    """
    words = text.split()  # split the text into individual words using spaces
    chunks = []           # list to store all created chunks
    
    start = 0  # pointer for the starting position of the current chunk
    
    # Keep creating chunks until we reach the end of the word list
    while start < len(words):
        end = start + chunk_size  # calculate where this chunk should end
        
        # Slice the words list to get only this chunk's words
        chunk_words = words[start:end]
        
        # Join the words back into a string with spaces
        chunk = " ".join(chunk_words)
        
        chunks.append(chunk)  # add this chunk to our list
        
        # Move the start pointer forward, but go back by 'overlap' words
        # This ensures the next chunk starts slightly before this one ended
        start += chunk_size - overlap
    
    return chunks  # return all chunks created from this text


def create_chunks(documents, chunk_size=120, overlap=30):
    """
    Creates chunks for ALL documents in the pipeline.
    For each document (page), it calls chunk_text to split that page into chunks.
    Each chunk also carries the original document's metadata.
    """
    all_chunks = []  # master list to hold every chunk from every document
    
    for doc in documents:  # go through each document (page)
        
        text_chunks = chunk_text(doc["text"], chunk_size, overlap)  # split text into chunks
        
        for i, chunk_text_content in enumerate(text_chunks):  # go through each chunk
            
            chunk_id = str(random.randint(100000, 999999))  # generate a random unique ID for this chunk
            
            all_chunks.append({
                "id": chunk_id,                       # unique identifier for this chunk
                "text": chunk_text_content,           # the actual text of this chunk
                "metadata": doc["metadata"],          # carry forward the original document's metadata
                "chunk_index": i                      # which chunk number this is within the document
            })
    
    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks  # return all chunks ready for embedding


# =====================================================================
# SECTION 3: EMBEDDINGS AND VECTOR DATABASE
# =====================================================================

def create_embeddings(texts):
    """
    Converts a list of text strings into embedding vectors using OpenAI.
    Returns a list of embedding vectors (one per text input).
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,  # use the text-embedding-3-small model
        input=texts             # pass the list of texts to embed
    )
    
    # Extract just the embedding vectors from the API response
    embeddings = [item.embedding for item in response.data]
    
    return embeddings  # return list of vectors


def setup_vector_db(db_path="./chroma_db", collection_name="ecommerce_policies"):
    """
    Sets up a persistent ChromaDB client and creates (or opens) a collection.
    'Persistent' means the data is saved to disk — it survives program restarts.
    """
    # Create a persistent ChromaDB client at the given path
    chroma_client = chromadb.PersistentClient(path=db_path)
    
    # Get or create a collection with the given name
    # If the collection already exists, it opens it; if not, it creates it
    collection = chroma_client.get_or_create_collection(name=collection_name)
    
    print(f"Vector DB ready. Collection: '{collection_name}'")
    return collection  # return the collection object


def index_chunks(chunks, collection):
    """
    Generates embeddings for all chunks and stores them in the vector database.
    This is the step where your knowledge base actually gets built.
    """
    # Extract just the text from each chunk to send to the embedding model
    texts = [chunk["text"] for chunk in chunks]
    
    print("Generating embeddings for all chunks...")
    embeddings = create_embeddings(texts)  # convert all chunk texts to vectors
    
    # Extract IDs, texts, metadatas, and embeddings in parallel lists
    ids = [chunk["id"] for chunk in chunks]                # list of all chunk IDs
    metadatas = [chunk["metadata"] for chunk in chunks]    # list of all metadata dicts
    
    # Store everything in ChromaDB in one batch operation
    # upsert = insert if new, update if ID already exists
    collection.upsert(
        ids=ids,              # unique IDs for each entry
        documents=texts,      # the actual text of each chunk
        embeddings=embeddings, # the vector representation of each chunk
        metadatas=metadatas   # the metadata (policy type, page, source file)
    )
    
    print(f"Successfully stored {len(chunks)} chunks in vector database.")


# =====================================================================
# SECTION 4: BUILDING THE KNOWLEDGE BASE (PRE-PROCESSING PHASE)
# =====================================================================

def build_knowledge_base(folder_path, collection, chunk_size=120, overlap=30):
    """
    Runs the entire pre-processing pipeline:
    1. Load all PDF documents from the folder
    2. Clean the text
    3. Create chunks with overlap
    4. Generate embeddings
    5. Store everything in the vector database
    
    Call this function ONCE to prepare your system before handling user queries.
    """
    print("=== Building Knowledge Base ===")
    print(f"Loading documents from: {folder_path}")
    
    # Step 1 & 2: Load and clean all documents
    documents = load_all_documents(folder_path)
    
    # Step 3: Split documents into overlapping chunks
    chunks = create_chunks(documents, chunk_size, overlap)
    
    # Steps 4 & 5: Generate embeddings and store in vector DB
    index_chunks(chunks, collection)
    
    print("=== Knowledge Base Ready ===\n")


# =====================================================================
# SECTION 5: RETRIEVAL AND GENERATION (RUNTIME PHASE)
# =====================================================================

def retrieve_chunks(query, collection, top_k=3, policy_filter=None):
    """
    Given a user query, finds the most relevant chunks from the database.
    
    top_k = 3 means: return the 3 most similar chunks to the query
    policy_filter = optional filter, e.g., only search refund-related chunks
    """
    # Step 1: Convert the user query into an embedding vector
    query_embedding = create_embeddings([query])[0]  # embed only one text (the query)
    
    # Step 2: Build optional filter for metadata (e.g., only refund policy chunks)
    where_filter = None
    if policy_filter:
        where_filter = {"policy_type": {"$eq": policy_filter}}  # ChromaDB filter syntax
    
    # Step 3: Perform similarity search in the vector database
    results = collection.query(
        query_embeddings=[query_embedding],  # the query's vector
        n_results=top_k,                     # how many top results to return
        where=where_filter                   # optional metadata filter
    )
    
    # Step 4: Package the results into a clean list of retrieved chunks
    retrieved = []
    if results["documents"] and results["documents"][0]:
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            retrieved.append({
                "text": doc,        # the chunk text
                "metadata": meta    # the chunk's metadata
            })
    
    return retrieved  # return the top-k most relevant chunks


def build_prompt(query, retrieved_chunks):
    """
    Combines retrieved policy chunks and the user's query into a structured prompt.
    The LLM will use this prompt to generate a helpful, grounded answer.
    """
    # Combine all retrieved chunk texts into one context block
    context = "\n\n".join([chunk["text"] for chunk in retrieved_chunks])
    
    # Build the full prompt with system instructions + context + user question
    prompt = f"""You are a helpful customer support assistant for an e-commerce company.
    
Answer the customer's question using ONLY the policy information provided below.
Do NOT make up any details. If the answer is not in the context, say: "I don't have that information."
Keep your answer simple, clear, and customer-friendly.

--- POLICY CONTEXT ---
{context}
--- END OF CONTEXT ---

Customer Question: {query}

Answer:"""
    
    return prompt  # return the complete prompt string


def generate_answer(query, retrieved_chunks):
    """
    Sends the constructed prompt to the LLM and returns the final answer.
    This is the Generator component of RAG.
    """
    # Build the prompt by combining context and query
    prompt = build_prompt(query, retrieved_chunks)
    
    # Call the LLM (GPT-4o) with the constructed prompt
    response = client.chat.completions.create(
        model=LLM_MODEL,  # use the configured LLM model
        messages=[
            {
                "role": "system",
                "content": "You are a helpful e-commerce customer support assistant."
            },
            {
                "role": "user",
                "content": prompt  # pass the full prompt (context + query)
            }
        ],
        temperature=0.2  # low temperature = more factual, less creative answers
    )
    
    # Extract and return just the text of the answer
    return response.choices[0].message.content


def answer_question(query, collection, top_k=3):
    """
    The main function that handles end-to-end question answering.
    1. Retrieve relevant chunks for the query
    2. Generate a polished answer using the LLM
    """
    print(f"\nUser Query: {query}")
    print("-" * 50)
    
    # Step 1: Retrieve the most relevant policy chunks
    retrieved = retrieve_chunks(query, collection, top_k=top_k)
    
    if not retrieved:
        return "I'm sorry, I couldn't find relevant information to answer your question."
    
    print(f"Retrieved {len(retrieved)} relevant chunks.")
    
    # Step 2: Generate the final answer using the LLM
    answer = generate_answer(query, retrieved)
    
    return answer  # return the final customer-friendly answer


# =====================================================================
# MAIN: Run the full pipeline
# =====================================================================

if __name__ == "__main__":
    
    # ----- PRE-PROCESSING PHASE (run once) -----
    collection = setup_vector_db()  # set up ChromaDB
    
    POLICY_FOLDER = "./policy_documents"  # path to your folder of PDF files
    build_knowledge_base(POLICY_FOLDER, collection)  # load, chunk, embed, store
    
    # ----- RUNTIME PHASE (for every user query) -----
    test_queries = [
        "What is the return window for products?",
        "How long does a refund take?",
        "Is there free shipping available?"
    ]
    
    for query in test_queries:
        answer = answer_question(query, collection)
        print(f"\nAnswer: {answer}")
        print("=" * 60)
```

---

## How the Code Works — Section by Section

### Section 1: Loading and Cleaning

- **`infer_policy_type(filename)`** — reads the filename and guesses the policy type. "refund_policy.pdf" → `"refund"`. This becomes part of the metadata stored with every chunk.
- **`clean_text(raw_text)`** — takes messy PDF text and strips out newlines and extra spaces so you get one clean block of text.
- **`make_document(text, metadata)`** — wraps text and metadata into a consistent dictionary format. Every page of every PDF becomes one document dictionary.
- **`load_pdf_file(file_path)`** — opens a PDF using `PdfReader`, goes through each page, cleans it, and returns a list of document dictionaries.
- **`load_all_documents(folder_path)`** — scans a folder, finds every `.pdf` file, and calls `load_pdf_file` on each one. You get all pages from all PDFs in one master list.

### Section 2: Chunking

- **`chunk_text(text, chunk_size, overlap)`** — splits one page's text into overlapping word-based chunks. With `chunk_size=120` and `overlap=30`: Chunk 1 = words 1–120, Chunk 2 = words 91–210, Chunk 3 = words 181–300.
- **`create_chunks(documents)`** — applies `chunk_text` to every document (page) and returns all chunks with their metadata and unique IDs.

### Section 3: Embeddings and Vector DB

- **`create_embeddings(texts)`** — sends a list of texts to OpenAI's `text-embedding-3-small` model and gets back a list of 1536-dimensional vectors.
- **`setup_vector_db()`** — creates a persistent ChromaDB client and opens/creates a collection named `"ecommerce_policies"`.
- **`index_chunks(chunks, collection)`** — the heart of the storage phase. Gets embeddings for all chunks and stores text + embeddings + metadata in ChromaDB using `.upsert()`.

### Section 4: Build Knowledge Base

- **`build_knowledge_base()`** — the master pre-processing function that calls Steps 1 through 5 in order. Run this once before your system is ready.

### Section 5: Retrieval and Generation

- **`retrieve_chunks(query, collection, top_k)`** — embeds the user query and performs similarity search in ChromaDB. Returns the top 3 most relevant chunks.
- **`build_prompt(query, retrieved_chunks)`** — stitches retrieved chunks into a context block and writes the final prompt telling the LLM what to do.
- **`generate_answer(query, retrieved_chunks)`** — calls GPT-4o with the built prompt and returns the polished, customer-friendly answer.
- **`answer_question(query, collection)`** — the top-level function: retrieve + generate in one call.

---

## Understanding the Retriever vs Generator Split

It helps to see the pipeline split clearly into its two halves:

![The retriever relies on embeddings and similarity math while the generator crafts natural language grounded in the retrieved snippets](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session30/session30-07-retriever-generator-split.png)

```
RAG = Retriever  +  Generator
```

| Component | What It Does | Tools Used |
|---|---|---|
| **Retriever** | Embeds query → searches ChromaDB → returns top-K chunks | `create_embeddings`, `collection.query` |
| **Generator** | Takes chunks + query → builds prompt → calls LLM → returns answer | `build_prompt`, `client.chat.completions.create` |

The **Retriever** does not understand language — it works with math (vector similarity). The **Generator** understands language and turns raw chunk text into a polished, helpful response. Together they make RAG powerful.

---

## Handling Policy Document Updates

One important production consideration is: **what happens when a policy changes?**

For example, the company changes the return window from 30 days to 45 days. The old chunks in ChromaDB are now outdated and will give wrong answers.

**The correct approach:**
1. **Delete** all chunks from ChromaDB that belong to the updated document (using chunk IDs and metadata filters).
2. **Re-load and re-chunk** the updated PDF file.
3. **Re-embed and re-store** the new chunks.

This ensures the knowledge base stays current. The session covered this concept and additional handling details are in the supplementary notes.

---

## Key Takeaways

- **Production RAG uses real documents** (PDFs) instead of hardcoded strings. The `pypdf` library with its `PdfReader` class is the standard tool for reading PDFs page by page in Python.
- **Chunking is essential** because storing entire documents is expensive and slow. Fixed-size chunking with overlap (10–20% overlap) balances context preservation and retrieval efficiency. A chunk size of 100–200 words is a good starting range for most use cases.
- **Metadata is a superpower** — storing policy type, page number, and source file alongside each chunk lets you filter searches and trace the origin of every answer.
- **The pipeline has two distinct phases:** a one-time **pre-processing phase** (load → clean → chunk → embed → store) and a **runtime phase** (query → embed → retrieve → generate) that runs for every user question.
- **Next up:** Now that you can build a multi-document RAG system, upcoming sessions will explore how to make these systems more autonomous, add memory, and eventually build full-fledged agents that can use RAG as one of many tools.

---

## Quick Reference — Commands, Libraries, and Terminology

| Term / Command | What It Means |
|---|---|
| `pypdf` | Python library for reading PDF files |
| `PdfReader` | Class inside `pypdf` that opens and reads a PDF page by page |
| `page.extract_text()` | Method to get raw text from one page of a PDF |
| `chromadb.PersistentClient(path)` | Creates a ChromaDB instance that saves data to disk |
| `collection.get_or_create_collection(name)` | Opens an existing collection or creates a new one |
| `collection.upsert(ids, documents, embeddings, metadatas)` | Stores or updates chunks in ChromaDB |
| `collection.query(query_embeddings, n_results)` | Searches for the top-N most similar chunks |
| `client.embeddings.create(model, input)` | Converts text(s) into embedding vectors using OpenAI |
| `text-embedding-3-small` | OpenAI embedding model — 1536 dimensions |
| `text-embedding-3-large` | OpenAI embedding model — 3072 dimensions (higher cost) |
| `pip3 install -r requirements.txt` | Installs all dependencies listed in requirements.txt at once |
| `export OPENAI_API_KEY="..."` | Sets the OpenAI API key as a terminal environment variable |
| **Document Ingestion** | Loading raw documents into the pipeline |
| **Parsing** | Reading and extracting structured data from a raw document |
| **Cleaning** | Removing noise (headers, footers, extra spaces) from text |
| **Fixed-Size Chunking** | Splitting text into equal-sized word groups |
| **Chunk Overlap** | Repeating the last N words of one chunk at the start of the next |
| **Embedding** | A list of numbers (vector) representing the meaning of a text |
| **Vector Database** | A database optimized for storing and searching embedding vectors |
| **Similarity Search** | Finding stored vectors that are mathematically closest to a query vector |
| **Top-K Retrieval** | Returning the K most relevant results from a similarity search |
| **RAG Prompt** | A structured prompt combining retrieved context + user query for the LLM |
| **OCR** | Optical Character Recognition — reading text from images |
| **Metadata** | Extra descriptive information stored alongside each chunk (e.g., policy type, page number) |
| **Knowledge Base** | The vector database loaded with all your document chunks and embeddings |
| **Pre-processing Phase** | One-time setup: load → clean → chunk → embed → store |
| **Runtime Phase** | Per-query flow: embed query → similarity search → generate answer |
