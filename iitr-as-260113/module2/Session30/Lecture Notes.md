# Building a RAG Pipeline

## What We Covered Before and Where We Are Now

In the previous session, we built the **foundation of a RAG system** for an e-commerce customer support assistant. We identified the key components — **retriever**, **generator**, and **knowledge sources** — and wired them together in a minimal end-to-end flow. We loaded a small set of policy snippets, retrieved relevant content using vector search, and generated grounded responses using an LLM. We also compared answers produced with and without retrieval to see how grounding improves quality.

Now we are ready to **scale that system into a real-world pipeline**. In this session, we will stop working with tiny sample snippets and start handling **actual documents** — PDFs, text files, and web pages. We will learn how to load documents, process them, split them into meaningful pieces, generate embeddings, store them in a vector database, and finally build a complete multi-document RAG assistant.

**What you will learn in this session:**
- How to load documents from various sources using **Document Loaders**
- How to break large documents into smaller chunks using a process called **Chunking**
- How to configure chunk size and overlap for better search results
- How to generate embeddings for document chunks and store them in a vector database
- How to build retrieval and generation layers on top of multiple documents
- How to update the knowledge base when documents change
- How to assemble a fully working **Multi-Document RAG System**

---

## From Snippets to Real Documents — Expanding the Knowledge Base

In the last session, we used a few handwritten policy paragraphs to simulate an e-commerce knowledge base. That was perfect for learning the concepts. But in real life, a company has many documents — return policy PDFs, shipping policy pages on their website, warranty documents, and more.

Think of it this way: earlier, we were cooking with just two or three pre-cut vegetables. Now we are going to the **actual market**, buying whole vegetables, cleaning them, cutting them into the right size, and then cooking. Each step in that process has a name in the RAG world.

**Why this matters:**
- Real documents are messy — they have headers, footers, extra whitespace, and irrelevant content.
- Documents can be in different formats — PDF, `.txt`, HTML, CSV.
- A single document can have thousands of words, which is too large to pass to an LLM at once.
- We need a **systematic pipeline** to handle all of this reliably.

**Our running example throughout this session:**
We are building a customer support assistant for an e-commerce company called **ShopEasy**. ShopEasy has the following policy documents:
- `returns_policy.pdf` — How customers can return products
- `shipping_policy.txt` — Delivery timelines and charges
- `warranty_policy.pdf` — Product warranty terms
- `refund_policy.txt` — Refund processing steps

By the end of this session, our RAG assistant will be able to answer any customer question by reading all four of these documents.

---

## Document Loaders — Bringing Documents Into Your Pipeline

Before we can search through a document, we need to **load it into our Python program**. This is the job of a **Document Loader**.

**Official Definition:** A Document Loader is a software component that reads content from a file or URL and converts it into a standard format that the rest of the pipeline can work with.

**In Simple Words:** Think of a document loader like a **scanner at an office**. You put in a paper document, and the scanner converts it into a digital file. Similarly, a document loader takes a PDF or text file and converts it into a Python object that holds the text content.

**Real-Life Example:** Imagine you have a bookshelf full of books in different languages. Before you can search through them, you first need someone to translate all of them into one common language. Document loaders do exactly that — they translate different file formats into one standard Python format.

**What a Document Loader gives you:**
- The raw **text content** of the document
- **Metadata** like the file name, page number, and source URL
- A clean, usable object that the rest of the pipeline can process

### Setting Up the Environment

Before writing any code, we need to install the required libraries. Open your terminal and run:

```bash
pip install langchain langchain-community pypdf openai chromadb tiktoken
```

- **`langchain`** — The main framework we use to build RAG pipelines
- **`langchain-community`** — Extra loaders and integrations
- **`pypdf`** — For reading PDF files
- **`openai`** — To access OpenAI's embedding and LLM models
- **`chromadb`** — A vector database that stores our embeddings
- **`tiktoken`** — For counting tokens in text

### Loading a PDF File

```python
# Import the PDF document loader from LangChain's community library
from langchain_community.document_loaders import PyPDFLoader

# Create a loader object and point it to the PDF file on your computer
loader = PyPDFLoader("returns_policy.pdf")

# Actually read the file — this gives us a list of pages
pages = loader.load()

# Print how many pages were found in the document
print(f"Number of pages loaded: {len(pages)}")

# Look at the content of the first page
print("Content of page 1:")
print(pages[0].page_content)

# Look at the metadata of the first page (source file name and page number)
print("Metadata of page 1:")
print(pages[0].metadata)
```

**How the code works:**
- `PyPDFLoader("returns_policy.pdf")` — Creates a loader that knows how to read PDF files. We give it the file path.
- `loader.load()` — This is when the actual reading happens. It returns a Python **list**, where each item is one page of the PDF.
- `pages[0].page_content` — Every page is a Python object. The `.page_content` attribute holds the actual text on that page.
- `pages[0].metadata` — This holds extra information like `{'source': 'returns_policy.pdf', 'page': 0}`.

**Common Doubt:** *What if the PDF has images or scanned text?*
- `PyPDFLoader` can only read **text-based PDFs**. If the PDF contains scanned images, you will need an OCR (Optical Character Recognition) tool. For most business documents like policies, the text is selectable, so `PyPDFLoader` works perfectly.

### Loading a Plain Text File

```python
# Import the text file loader
from langchain_community.document_loaders import TextLoader

# Create a loader for a .txt file
loader = TextLoader("shipping_policy.txt", encoding="utf-8")

# Load all the content — text files are treated as one single document
documents = loader.load()

# Print the number of documents loaded (usually 1 for a single text file)
print(f"Number of documents: {len(documents)}")

# Print the first 500 characters of the content
print(documents[0].page_content[:500])
```

**How the code works:**
- `TextLoader("shipping_policy.txt", encoding="utf-8")` — Points to the `.txt` file. The `encoding="utf-8"` ensures special characters (like ₹ or é) are read correctly.
- Unlike PDFs, a text file has no pages — so `loader.load()` returns a list with just **one document** that contains all the text.

### Loading Multiple Documents Together

In a real project, you will have several documents. Instead of loading them one by one, you can load all of them in a single step.

```python
# Import both loaders we need
from langchain_community.document_loaders import PyPDFLoader, TextLoader

# Create a list to store all loaded documents
all_documents = []

# Define the list of files and their formats
files_to_load = [
    ("returns_policy.pdf", "pdf"),
    ("shipping_policy.txt", "txt"),
    ("warranty_policy.pdf", "pdf"),
    ("refund_policy.txt", "txt"),
]

# Loop through each file and load it based on its type
for file_name, file_type in files_to_load:

    # Check if the file is a PDF
    if file_type == "pdf":
        loader = PyPDFLoader(file_name)

    # Otherwise, treat it as a plain text file
    else:
        loader = TextLoader(file_name, encoding="utf-8")

    # Load the documents and add them to our main list
    loaded_docs = loader.load()
    all_documents.extend(loaded_docs)

# Print the total number of pages/documents loaded across all files
print(f"Total documents loaded: {len(all_documents)}")
```

**How the code works:**
- We define a list of `(file_name, file_type)` pairs so we can handle multiple formats.
- The `for` loop goes through each file and picks the right loader.
- `.extend()` adds all pages from each file into the single `all_documents` list.
- After this loop, `all_documents` is a flat list of every page from every file — all in the same format.

---

## Processing and Organizing Document Data

Raw documents often have **noise** — extra spaces, page numbers, headers, footers, or repeated boilerplate text. Before we split the documents, it's good practice to inspect and lightly clean the content.

Think of this like washing vegetables before cutting them. You wouldn't start chopping an unwashed tomato.

**Inspecting your loaded documents:**

```python
# Go through every loaded document and print a summary
for i, doc in enumerate(all_documents):

    # Print a separator and the document number
    print(f"\n--- Document {i + 1} ---")

    # Print the source file name from metadata
    print(f"Source: {doc.metadata.get('source', 'Unknown')}")

    # Print the page number if available (PDFs have page numbers, text files don't)
    print(f"Page: {doc.metadata.get('page', 'N/A')}")

    # Print how many characters of text this document has
    print(f"Content length: {len(doc.page_content)} characters")

    # Print the first 200 characters as a preview
    print(f"Preview: {doc.page_content[:200]}")
```

**How the code works:**
- `enumerate(all_documents)` — Gives us both the index `i` and the document `doc` in each loop iteration.
- `doc.metadata.get('source', 'Unknown')` — Safely reads the `source` key from metadata. If it doesn't exist, it returns `'Unknown'` instead of crashing.
- This inspection step helps you catch problems early — for example, a PDF page that loaded as blank, or garbled text.

**Why metadata is important:**
- When our RAG system retrieves a chunk and answers a question, metadata tells us **which document and which page** that chunk came from.
- This is like how a textbook citation tells you the book name and page number — it makes the answer trustworthy and verifiable.

---

## Chunking — Splitting Documents into Meaningful Pieces

Now we have our documents loaded. But here is a problem: the **ShopEasy Returns Policy PDF** might be 10 pages long with 5,000 words. We cannot send all 5,000 words to the LLM for every question. It would be too slow and too expensive.

This is where **chunking** comes in.

**Official Definition:** Chunking is the process of splitting a large document into smaller, manageable pieces called **chunks**, each of which captures a self-contained unit of information.

**In Simple Words:** Imagine you have a very long newspaper article. Instead of reading the whole article to find the answer to one question, you cut the article into paragraphs. Each paragraph is now a searchable chunk. When someone asks a question, you only find and read the most relevant paragraph.

**Real-Life Example:** Think about how an index works in a book. The index doesn't contain the full content — it points you to **specific sections**. Chunking creates those sections so the system can point to the right piece at the right time.

### The Basic Text Splitter

LangChain provides a tool called `RecursiveCharacterTextSplitter` which is the most commonly used chunking tool.

**Official Definition:** `RecursiveCharacterTextSplitter` splits text by trying different separators in order — first by paragraphs, then by sentences, then by words — to keep chunks as semantically complete as possible.

**In Simple Words:** It's like a smart scissor that first tries to cut at paragraph breaks, then at sentence ends, and only cuts in the middle of a sentence if it has no other choice.

```python
# Import the text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure the splitter with chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter(

    # Each chunk should have at most 500 characters
    chunk_size=500,

    # The last 50 characters of each chunk will be repeated at the start of the next chunk
    chunk_overlap=50,

    # Count length in characters (not tokens)
    length_function=len,
)

# Apply the splitter to all loaded documents
chunks = text_splitter.split_documents(all_documents)

# Print how many chunks were created
print(f"Total chunks created: {len(chunks)}")

# Look at the first chunk's content and metadata
print("\nFirst chunk content:")
print(chunks[0].page_content)
print("\nFirst chunk metadata:")
print(chunks[0].metadata)
```

**How the code works:**
- `chunk_size=500` — Each chunk will have at most 500 characters. The splitter tries to cut at a natural break point (paragraph or sentence) before reaching 500.
- `chunk_overlap=50` — The last 50 characters of chunk #1 are repeated at the beginning of chunk #2. This prevents important information from being cut in half between two chunks.
- `split_documents(all_documents)` — Takes the list of Document objects and returns a new list of smaller Document objects. The metadata (source, page number) is **automatically carried over** to each chunk.

---

## Understanding Chunk Size and Overlap — Getting It Right

Choosing the right chunk size is one of the most important decisions in building a RAG pipeline. Get it wrong, and your system will give poor answers even with perfect documents.

**The analogy of "too small" vs "too big":**
- If you cut an article into chunks of **5 words each**, each chunk is too small to make sense on its own. Searching for "What is the return window?" might return a chunk that just says "within 30 days" — with no context about what 30 days refers to.
- If your chunks are **5,000 characters each**, you are almost passing the entire document to the LLM every time. The search becomes inaccurate and expensive.

**Recommended starting points:**
| Use Case | Chunk Size | Overlap |
|---|---|---|
| Short policy documents | 300–500 characters | 30–50 characters |
| Long reports or manuals | 800–1200 characters | 100–150 characters |
| Code or structured data | 200–400 characters | 20–50 characters |

### Comparing Different Chunk Configurations

Let's see how different settings change our output:

```python
# Import the text splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configuration 1 — Small chunks, small overlap
splitter_small = RecursiveCharacterTextSplitter(
    chunk_size=200,    # Very small chunks — 200 characters each
    chunk_overlap=20,  # Small overlap — 20 characters
    length_function=len,
)

# Configuration 2 — Medium chunks, medium overlap
splitter_medium = RecursiveCharacterTextSplitter(
    chunk_size=500,    # Standard size — good for most policy docs
    chunk_overlap=50,  # Standard overlap — prevents context loss
    length_function=len,
)

# Configuration 3 — Large chunks, large overlap
splitter_large = RecursiveCharacterTextSplitter(
    chunk_size=1000,   # Large chunks — capture more context
    chunk_overlap=100, # Larger overlap — smooth transitions
    length_function=len,
)

# Apply each splitter to the same documents and compare
chunks_small  = splitter_small.split_documents(all_documents)
chunks_medium = splitter_medium.split_documents(all_documents)
chunks_large  = splitter_large.split_documents(all_documents)

# Print the number of chunks each configuration produces
print(f"Small config  → {len(chunks_small)} chunks")
print(f"Medium config → {len(chunks_medium)} chunks")
print(f"Large config  → {len(chunks_large)} chunks")
```

**How the code works:**
- We create three splitter objects with different settings.
- We apply each to the same `all_documents` list.
- Notice that smaller chunks = more chunks total, and larger chunks = fewer chunks.
- The right choice depends on your content — policy documents with short, self-contained rules work well with 300–500 character chunks.

**Common Doubt:** *Do I always need overlap?*
- Yes, in almost every case. Without overlap, if a sentence spans the boundary between two chunks, neither chunk will have the complete thought. Overlap ensures no key sentence is split without a safety net.

---

## Generating Embeddings for Policy Chunks

Now that our documents are split into chunks, we need to convert each chunk into a **numerical vector** (a list of numbers) that captures its meaning. This is called **embedding generation**.

**Official Definition:** An **embedding** is a mathematical representation of text as a fixed-length array of numbers, where similar meanings result in similar number patterns (vectors that are close together in space).

**In Simple Words:** Imagine you could rate every sentence by 1,000 different qualities — tone, topic, formality, sentiment, etc. Each sentence would get a score on every quality, giving it a unique "fingerprint" of 1,000 numbers. Two sentences about the same topic would have very similar fingerprints. That fingerprint is an embedding.

**Real-Life Example:** Think about how a music streaming app recommends songs. It secretly assigns every song a score on qualities like "energy," "tempo," and "mood." Songs with similar scores get recommended together. Embeddings do the same for text — chunks with similar meanings get similar scores and will be found together during search.

```python
# Import the OpenAI embedding model
from langchain_openai import OpenAIEmbeddings

# Import Chroma — our vector database
from langchain_community.vectorstores import Chroma

# Import os to read our API key from environment variables
import os

# Set your OpenAI API key — replace with your actual key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

# Create the embedding model — this will convert text to vectors
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Create a vector store from our chunks — this does two things:
# 1. Generates embeddings for every chunk
# 2. Stores both the chunk text and its embedding in Chroma
vectorstore = Chroma.from_documents(
    documents=chunks,            # Our list of chunked Document objects
    embedding=embedding_model,   # The model to use for embedding
    persist_directory="./shopeasy_db",  # Save the database to this folder on disk
    collection_name="shopeasy_policies"  # A name for this collection of documents
)

# Print confirmation
print("Vector store created and saved successfully.")
print(f"Total vectors stored: {vectorstore._collection.count()}")
```

**How the code works:**
- `OpenAIEmbeddings(model="text-embedding-3-small")` — Creates an embedding model. The model `text-embedding-3-small` is affordable and accurate for most use cases.
- `Chroma.from_documents(...)` — This single function call does a lot of heavy lifting. It loops through every chunk, calls the embedding model to convert it to a vector, and stores the (chunk text + vector + metadata) trio in the Chroma database.
- `persist_directory="./shopeasy_db"` — Saves the database to your hard drive so you don't have to regenerate embeddings every time you restart your program.
- After this step, your knowledge base is ready to be searched.

**Cost Awareness:** Generating embeddings costs money (fractions of a cent per 1,000 characters with OpenAI). Always persist your vector store to disk so you only pay for embedding generation once.

---

## Building the Retrieval Layer for User Queries

We now have all our policy chunks stored as searchable vectors. The next step is to build the **retrieval layer** — the component that accepts a user's question, converts it to a vector, and finds the most relevant chunks.

**Official Definition:** The **retrieval layer** is the part of the RAG pipeline responsible for taking a query as input and returning the most semantically relevant document chunks from the vector store.

**In Simple Words:** It is the smart search engine of our system. When a customer asks "Can I return a broken phone?", the retrieval layer converts that question into a vector and finds the chunks from our policy documents that are most similar in meaning.

```python
# Load the existing vector store from disk (no need to re-embed documents)
vectorstore = Chroma(
    persist_directory="./shopeasy_db",         # Folder where the DB is saved
    embedding_function=embedding_model,        # Same model used during creation
    collection_name="shopeasy_policies"        # Same collection name
)

# Create a retriever object — this is a simple interface for searching
retriever = vectorstore.as_retriever(
    search_type="similarity",   # Find chunks by semantic similarity
    search_kwargs={"k": 4}      # Return the top 4 most relevant chunks
)

# Test the retriever with a sample customer question
query = "What is the return window for electronics?"

# Retrieve relevant chunks
relevant_chunks = retriever.invoke(query)

# Print how many chunks were retrieved
print(f"Number of retrieved chunks: {len(relevant_chunks)}")

# Print each retrieved chunk with its source
for i, chunk in enumerate(relevant_chunks):
    print(f"\n--- Retrieved Chunk {i + 1} ---")
    print(f"Source: {chunk.metadata.get('source', 'Unknown')}")
    print(f"Content: {chunk.page_content}")
```

**How the code works:**
- `Chroma(persist_directory=...)` — Loads the database we saved earlier. This is much faster than recreating it from scratch.
- `vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})` — Wraps the vector store in a retriever interface. `k=4` means it will return the 4 chunks whose vectors are closest to the query vector.
- `retriever.invoke(query)` — Converts the query string to a vector and searches for the top-k matches. Returns a list of Document objects.

**Tuning `k` (Top-K):**
- **`k=2`** — Very focused. Good when documents are precise and questions are specific. Risk: might miss relevant context.
- **`k=4`** — A balanced default for most use cases.
- **`k=8`** — Broader context. Good for complex, multi-part questions. Risk: may introduce irrelevant content that confuses the LLM.

---

## Constructing Prompt Templates for Response Generation

We have retrieved the relevant chunks. Now we need to **give those chunks to the LLM** along with the user's question. But we don't just paste everything randomly — we use a structured **prompt template** to tell the LLM exactly what role it plays and how to use the context.

**Official Definition:** A **prompt template** is a pre-written instruction structure with placeholders for dynamic inputs like the user's question and the retrieved document context.

**In Simple Words:** Think of a prompt template like a **fill-in-the-blank form** at a hospital. The form structure is always the same — "Patient Name: ___, Symptoms: ___, Doctor: ___" — but the actual content is filled in for each new patient. Our prompt template has blanks for "context" (retrieved chunks) and "question" (user's query).

```python
# Import the prompt template tool
from langchain.prompts import PromptTemplate

# Define our prompt template as a string with placeholders
template_string = """
You are a helpful customer support assistant for ShopEasy, an e-commerce company.
Use ONLY the information provided in the context below to answer the customer's question.
If the answer is not in the context, say "I'm sorry, I don't have that information in our policy documents."

Context from ShopEasy Policy Documents:
{context}

Customer Question:
{question}

Your Answer:
"""

# Create a PromptTemplate object with the placeholders defined
prompt_template = PromptTemplate(
    template=template_string,   # The template string we wrote above
    input_variables=["context", "question"]  # The two placeholders we will fill in
)

# Test the template by filling in sample values
sample_context = "Electronics can be returned within 30 days of purchase."
sample_question = "How long do I have to return a phone?"

# Format the prompt with actual values
formatted_prompt = prompt_template.format(
    context=sample_context,
    question=sample_question
)

# Print the fully formatted prompt that would be sent to the LLM
print("Formatted Prompt:")
print(formatted_prompt)
```

**How the code works:**
- The `{context}` and `{question}` in the template string are **placeholders**. They will be replaced with real values when we call `.format(...)`.
- The instruction "Use ONLY the information provided in the context" is critical — it tells the LLM not to use its general knowledge and only rely on our policy documents. This is what makes RAG **grounded** and reliable.
- The fallback instruction ("I'm sorry, I don't have that information") prevents the LLM from making up answers when no relevant chunk is found.

---

## Building the End-to-End Multi-Document RAG System

We now have all the individual pieces. Let's assemble them into a complete, working pipeline that a customer can use to ask any question about ShopEasy's policies.

```python
# Import all necessary libraries
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# ─── STEP 1: Set up API key ───────────────────────────────────────────────────
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

# ─── STEP 2: Load all ShopEasy policy documents ───────────────────────────────

# List all policy files with their types
policy_files = [
    ("returns_policy.pdf", "pdf"),
    ("shipping_policy.txt", "txt"),
    ("warranty_policy.pdf", "pdf"),
    ("refund_policy.txt", "txt"),
]

# Empty list to hold all loaded document pages
all_documents = []

# Loop and load each file with the right loader
for file_name, file_type in policy_files:
    if file_type == "pdf":
        loader = PyPDFLoader(file_name)
    else:
        loader = TextLoader(file_name, encoding="utf-8")
    all_documents.extend(loader.load())

# ─── STEP 3: Split documents into chunks ──────────────────────────────────────

# Create the text splitter with our chosen settings
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # Each chunk: maximum 500 characters
    chunk_overlap=50,  # Last 50 chars of each chunk repeated in the next
    length_function=len,
)

# Split all documents into chunks
chunks = text_splitter.split_documents(all_documents)

# ─── STEP 4: Create embeddings and vector store ───────────────────────────────

# Set up the embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

# Build vector store from chunks (generates and stores embeddings)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./shopeasy_db",
    collection_name="shopeasy_policies"
)

# ─── STEP 5: Create the retriever ─────────────────────────────────────────────

# Set up the retriever to return top 4 relevant chunks
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# ─── STEP 6: Set up the LLM ───────────────────────────────────────────────────

# Create an OpenAI chat model for generating answers
llm = ChatOpenAI(
    model="gpt-3.5-turbo",    # The model to use for text generation
    temperature=0,             # 0 = no creativity, strictly factual answers
)

# ─── STEP 7: Create the prompt template ───────────────────────────────────────

# Write the prompt with placeholders
prompt_template = PromptTemplate(
    template="""You are a helpful customer support assistant for ShopEasy.
Use ONLY the context below to answer the customer's question.
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: {question}

Answer:""",
    input_variables=["context", "question"]
)

# ─── STEP 8: Define the full RAG function ─────────────────────────────────────

def ask_shopeasy(question):
    """Takes a customer question and returns a grounded answer from policy docs."""

    # Retrieve the top 4 relevant chunks for this question
    retrieved_docs = retriever.invoke(question)

    # Join all retrieved chunk texts into a single context string
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Fill in the prompt template with context and question
    formatted_prompt = prompt_template.format(
        context=context,
        question=question
    )

    # Send the formatted prompt to the LLM and get the response
    response = llm.invoke(formatted_prompt)

    # Return the text content of the LLM's response
    return response.content

# ─── STEP 9: Test the system ──────────────────────────────────────────────────

# Sample customer questions to test the system
test_questions = [
    "What is the return window for electronics?",
    "How long does standard shipping take?",
    "Is my product covered under warranty for manufacturing defects?",
    "How do I get a refund for a cancelled order?",
]

# Loop through each question and print the answer
for question in test_questions:
    print(f"\n{'='*60}")
    print(f"Customer: {question}")
    print(f"ShopEasy Bot: {ask_shopeasy(question)}")
```

**How the code works:**
- **Step 1–4** runs once to build and save the knowledge base. After the first run, you skip straight to Step 5.
- `"\n\n".join([doc.page_content for doc in retrieved_docs])` — Takes the list of retrieved chunks and joins them into one long string, with two line breaks between each chunk. This becomes the `{context}` in our prompt.
- `temperature=0` — Setting this to zero ensures the LLM gives consistent, factual answers instead of creative variations each time.
- `ask_shopeasy(question)` — This is our complete RAG pipeline in one function. You call it with any question and it returns a grounded answer.

---

## Handling Updates to Policy Documents

Policies change. ShopEasy might extend their return window from 30 days to 45 days. When this happens, we need to update our knowledge base. There are two approaches.

**Approach 1 — Full Rebuild (Simple but slow)**
Delete the old database and rebuild it completely from scratch with the new documents. This is the safest approach for small knowledge bases.

```python
# Import the shutil library to delete folders
import shutil

# Delete the existing vector store folder from disk
shutil.rmtree("./shopeasy_db")

# Now re-run the full pipeline from Step 2 onwards with updated documents
print("Old vector store deleted. Ready to rebuild.")
```

**How the code works:**
- `shutil.rmtree("./shopeasy_db")` — Deletes the entire `shopeasy_db` folder and everything inside it.
- After this, you run the full pipeline again from Step 2. Chroma will create a fresh database.

**Approach 2 — Incremental Update (Efficient for large knowledge bases)**
Add only the new or changed document to the existing database without touching the rest.

```python
# Load only the updated document
updated_loader = TextLoader("returns_policy_v2.txt", encoding="utf-8")
updated_docs = updated_loader.load()

# Split the updated document into chunks
updated_chunks = text_splitter.split_documents(updated_docs)

# Load the existing vector store from disk
vectorstore = Chroma(
    persist_directory="./shopeasy_db",
    embedding_function=embedding_model,
    collection_name="shopeasy_policies"
)

# Add the new chunks to the existing store (old chunks remain untouched)
vectorstore.add_documents(updated_chunks)

# Print confirmation
print(f"Added {len(updated_chunks)} new chunks to the knowledge base.")
```

**How the code works:**
- We only load and split the updated file — not all four files.
- `vectorstore.add_documents(updated_chunks)` — Appends the new chunks to the existing Chroma collection without deleting the old ones.
- **Important:** If you just updated an existing policy (not a completely new one), you may want to delete the old chunks for that file first to avoid having both old and new versions in the database at the same time. For production systems, a full rebuild is often simpler to manage correctly.

---

## Putting It All Together — What Our Complete Pipeline Looks Like

At this point, we have built a full production-style RAG pipeline. Here is a clear summary of every stage and what it does:

| Stage | Tool Used | What It Does |
|---|---|---|
| **Load** | `PyPDFLoader`, `TextLoader` | Reads documents from files |
| **Process** | Inspect metadata, preview | Checks quality of loaded content |
| **Chunk** | `RecursiveCharacterTextSplitter` | Splits documents into small pieces |
| **Embed** | `OpenAIEmbeddings` | Converts chunks to numerical vectors |
| **Store** | `Chroma` | Saves chunks + vectors to disk |
| **Retrieve** | `Chroma.as_retriever()` | Finds relevant chunks for a query |
| **Generate** | `ChatOpenAI` + `PromptTemplate` | Produces a grounded answer |

**The data flow for every customer question:**

1. Customer types a question.
2. The question is converted to a vector.
3. Chroma finds the top-k chunks with the closest vectors.
4. The chunks are formatted into a prompt.
5. The LLM reads the prompt and generates an answer.
6. The answer is returned to the customer.

---

## Key Takeaways

- **Document Loaders** (`PyPDFLoader`, `TextLoader`) are the entry points of any RAG pipeline — they convert files into a standard Python format that the rest of the system can process.
- **Chunking** (`RecursiveCharacterTextSplitter`) breaks large documents into small, searchable pieces. `chunk_size` controls how big each piece is, and `chunk_overlap` ensures no important sentence is cut off at a boundary.
- **Embeddings** convert text chunks into vectors (numbers), and **Chroma** stores those vectors on disk so the system can search through them quickly and cost-effectively.
- The complete RAG pipeline follows a clear, sequential flow: **Load → Chunk → Embed → Store → Retrieve → Generate** — and each step has a specific, replaceable component.
- In the upcoming sessions, we will go further by adding **memory** to our RAG assistant (so it remembers previous questions in a conversation) and building a **chat interface** so real users can interact with it.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Description |
|---|---|
| `PyPDFLoader` | LangChain loader to read PDF files page by page |
| `TextLoader` | LangChain loader to read plain `.txt` files |
| `loader.load()` | Reads the file and returns a list of Document objects |
| `Document` | A LangChain object with `.page_content` (text) and `.metadata` (source info) |
| `RecursiveCharacterTextSplitter` | Splits text into chunks using paragraph/sentence/word boundaries in order |
| `chunk_size` | Maximum number of characters in a single chunk |
| `chunk_overlap` | Number of characters repeated between consecutive chunks to avoid context loss |
| `text_splitter.split_documents()` | Applies chunking to a list of Document objects |
| `OpenAIEmbeddings` | Converts text to numerical vectors using OpenAI's embedding model |
| `text-embedding-3-small` | OpenAI's cost-efficient embedding model suitable for RAG |
| `Chroma` | An open-source vector database for storing and searching embeddings |
| `Chroma.from_documents()` | Creates a new vector store from a list of documents (embeds + stores) |
| `persist_directory` | Folder path where Chroma saves the database on disk |
| `vectorstore.as_retriever()` | Creates a retriever interface from the vector store |
| `search_kwargs={"k": 4}` | Tells the retriever to return the top 4 most relevant chunks |
| `retriever.invoke(query)` | Searches the vector store and returns relevant chunks for the query |
| `PromptTemplate` | A reusable template with `{placeholders}` for dynamic content |
| `prompt_template.format(...)` | Fills in the placeholders with actual values |
| `ChatOpenAI` | LangChain wrapper for OpenAI's chat models (GPT-3.5-Turbo, GPT-4, etc.) |
| `temperature=0` | LLM setting that makes responses consistent and factual (no randomness) |
| `llm.invoke(prompt)` | Sends the formatted prompt to the LLM and returns the response |
| `vectorstore.add_documents()` | Adds new chunks to an existing Chroma vector store (incremental update) |
| `shutil.rmtree(path)` | Deletes a folder and all its contents (used for full database rebuild) |
| `pip install langchain langchain-community pypdf openai chromadb tiktoken` | Installs all required libraries for this pipeline |
