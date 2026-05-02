# RAG Architecture and Pipeline

## Context of the Session

In the previous session, we built a complete **vector search pipeline** from scratch. We learned how to convert text into **embeddings**, store those embeddings inside **ChromaDB**, run a **similarity search** using a query, and get back the most relevant document chunks with metadata filtering.

That pipeline gave us a powerful tool — given any question, we can now find the most relevant pieces of text from a knowledge base. But finding the right chunk is only half the job. A real user does not want a list of document snippets — they want a clean, natural language answer.

**This is exactly where today's session comes in.** We will now build a complete **RAG (Retrieval-Augmented Generation) pipeline** by connecting our retriever to an LLM. By the end of this session, we will have a working e-commerce customer support assistant that answers questions using real company policy documents.

**In this session, you will learn:**

- What **RAG** means and why it was invented.
- The **high-level architecture** of a RAG system.
- What **knowledge sources**, **document chunks**, **embeddings**, and **vector databases** do inside RAG.
- How the **Retriever** finds relevant policy content.
- How the **Generator (LLM)** uses that content to produce a grounded answer.
- How to build the **complete RAG pipeline** in Python using `openai` and `chromadb`.
- How to **compare responses with and without retrieval**.
- How **Top-K retrieval depth** affects answer quality.

---

## The Problem We Are Solving

Imagine you are building a customer support chatbot for an online shopping company. Customers ask questions like:

- "Can I return a product after 20 days?"
- "How long will my refund take?"
- "Is express delivery available?"
- "Does warranty cover accidental damage?"

If you simply pass these questions to a normal LLM, it will answer based on **general assumptions** — not based on the company's actual rules. Every company has different policies, so a generic answer is often wrong or misleading.

**For example:**

- One company allows returns within 7 days.
- Another allows returns within 30 days.
- Another may not allow returns on opened electronics at all.

So the assistant **must not guess**. It should look into the real company policy documents, find the relevant rule, and then answer. This is the exact problem that **RAG** solves.

---

## What Is RAG?

- **Official Definition:** **RAG** stands for **Retrieval-Augmented Generation**. It is an AI architecture where a retrieval system first fetches relevant documents from a knowledge base, and then passes that content to an LLM to generate a final answer.
- **In Simple Words:** RAG is like giving an open-book exam to the LLM. Instead of asking it to answer only from memory, we hand it the right pages from the textbook before it answers.
- **Real-Life Example:** Think of a new customer care executive at a company. Before they answer a customer's complaint, they quickly check the company's policy handbook and then reply using the real rules — not a guess.

The core formula of RAG is:

> **RAG = Search relevant company data + Generate answer using that data**

The key principle behind RAG is:

> **Do not depend only on the LLM's memory. Give the LLM the right context before asking it to answer.**

---

## Why Do We Need RAG?

Now that we know what RAG is, let us understand exactly what changes when we use it, by comparing two scenarios.

**Without RAG — Generic LLM Answer**

A user asks: *"Can I return headphones after 25 days?"*

The LLM may say: *"Most e-commerce companies allow returns within 7 to 30 days. Please check the seller policy."*

- This answer is **generic** and not based on real policy content.
- The LLM is **guessing** because it has no company-specific knowledge.
- This is called an **ungrounded response** — the answer floats in the air with no document backing it.

**With RAG — Grounded Answer**

The system first retrieves this policy chunk: *"Customers can return eligible products within 30 days of delivery. Products must be unused and in original packaging. Opened personal care items and digital products are not returnable."*

Then the LLM answers: *"Yes, you can return the headphones within 25 days if they are eligible, unused, and in original packaging. However, some categories may be excluded."*

- This answer is **grounded** — it is based on the real policy.
- The LLM is not guessing; it is using retrieved facts.
- This is the core power of RAG.

---

## High-Level RAG Architecture

Before we write any code, let us understand the overall structure of a RAG pipeline. Think of it as an assembly line in a factory where each station has a specific job.

```
User Query
    ↓
Retriever  (searches vector database for relevant chunks)
    ↓
Relevant Documents / Chunks
    ↓
Prompt Builder  (injects chunks as context into the prompt)
    ↓
LLM / Generator  (reads context + generates a natural language answer)
    ↓
Final Grounded Answer
```

**A real example walking through this pipeline:**

> **Customer asks:** "How long does a refund take?"
>
> **Retriever finds:** "Refunds are processed within 5–7 business days after quality check."
>
> **Prompt Builder** sends this context to the LLM along with the question.
>
> **LLM answers:** "Your refund will usually be processed within 5–7 business days after the returned item passes quality check."

![High-level RAG architecture: user query, retriever, relevant chunks, prompt builder, LLM, and grounded answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session29/rag-notes-image2-architecture.png)

---

## Main Components of a RAG System

A RAG pipeline is made up of five key components. Let us understand each one before we start coding.

### Knowledge Sources

- **Official Definition:** **Knowledge sources** are the documents from which the retrieval system fetches relevant information to answer questions.
- **In Simple Words:** These are the reference books we give to the LLM before the exam.
- **Real-Life Example:** A bank's RAG system would use its loan policy, interest rate guide, and account opening rules as knowledge sources.

For our e-commerce use case, the knowledge sources are:

| Document | Example Content |
| -------- | --------------- |
| Return Policy | Return window, eligibility, exceptions |
| Refund Policy | Refund timeline, refund method, failed refund cases |
| Shipping Policy | Delivery time, express shipping, shipping charges |
| Warranty Policy | Warranty duration, coverage, exclusions |
| Cancellation Policy | When you can cancel, what happens post-shipment |

### Document Chunks

- **Official Definition:** **Document chunking** is the process of breaking large documents into smaller, independent pieces of text called **chunks**.
- **In Simple Words:** Instead of handing the entire policy book to the LLM, we cut it into short paragraphs so the retriever can find the exact relevant paragraph.
- **Real-Life Example:** A recipe book is easier to use when chapters are separated by dish type. Similarly, a policy document is easier to search when split by topic.

**Example — chunking a refund policy:**

- **Chunk 1:** Refunds are initiated after the returned product passes quality check.
- **Chunk 2:** Refunds to UPI/cards take 5–7 business days.
- **Chunk 3:** COD refunds require bank account details and may take 7–10 business days.

**Why chunking is important:**

- Smaller chunks are easier for the retriever to match accurately.
- The LLM receives clean, focused context instead of a large noisy document.
- It reduces irrelevant information in the prompt, which improves answer quality.
- If you store the entire document as one chunk, the retriever may return it even when only one line is relevant — this wastes tokens and confuses the LLM.

### Embeddings

- **Official Definition:** **Embeddings** are dense numerical vector representations of text, generated by a neural network, that capture the semantic meaning of the text.
- **In Simple Words:** Embeddings are the way a computer "understands" the meaning of a sentence — by converting it into a list of numbers.
- **Real-Life Example:** Think of a map where similar places are kept close together. Embeddings do the same thing with words and sentences — sentences that mean similar things end up very close to each other in the vector space.

**How embeddings work in RAG:**

- The customer query — *"How long does refund take?"* — is converted into a vector like `[0.12, -0.45, 0.88, ...]`.
- Every policy chunk is also stored as a vector.
- The system then finds which policy chunk vector is **closest** to the query vector.
- Closest vectors = most similar meaning = most relevant chunk.

![Embeddings map text to vectors so the retriever can find semantically similar policy chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session29/rag-notes-image1-embeddings.png)

### Vector Database

- **Official Definition:** A **vector database** is a specialised database that stores text, embeddings, and metadata together and supports fast similarity-based search using vector distances.
- **In Simple Words:** A vector database is like a library where books are arranged not by title, but by topic — so when you ask for "something about shipping," it brings you the shelf closest in meaning to "shipping."
- **Real-Life Example:** Google Photos groups your photos by face, location, and object without you labelling them. It does this using vector similarity — the same concept our vector database uses.

A single record in a vector database looks like this:

```json
{
  "id": "refund_policy_1",
  "text": "Refunds are processed within 5-7 business days after quality check.",
  "metadata": {
    "category": "refund",
    "source": "refund_policy"
  },
  "embedding": [0.12, -0.45, 0.88]
}
```

For this session, we will use **ChromaDB** as our vector database. ChromaDB supports a **PersistentClient** that saves data locally — meaning even after we stop the script, the stored embeddings are still available.

### Retriever

- **Official Definition:** The **retriever** is the component that converts a user query into an embedding and searches the vector database to return the most relevant document chunks.
- **In Simple Words:** The retriever is like a smart search engine that understands meaning, not just keywords.
- **Real-Life Example:** When you search "delay in delivery" on an e-commerce site, it shows you the shipping policy even if those exact words do not appear in the policy — because the meaning matches.

**The retriever's job is limited and specific:**

- It does **not** generate the answer.
- It only finds and returns the most relevant content.
- The answer generation is handled separately by the LLM.

**Example:**

- Input: *"How many days does delivery take?"*
- Retriever output:
  - Standard delivery takes 3–5 business days.
  - Express delivery takes 1–2 business days.
  - Remote pin codes may take 5–8 business days.

### Generator

- **Official Definition:** The **generator** is the LLM component that takes the user query and retrieved policy chunks as input and produces a natural language answer.
- **In Simple Words:** The generator is the LLM that reads the retrieved paragraphs and writes a proper, helpful reply for the customer.
- **Real-Life Example:** Think of a well-trained human agent who reads the policy paragraph you hand them, and then writes a polite, clear reply to the customer — that is the generator's job.

**What the generator receives:**

- The customer's question
- Retrieved policy content (as context)
- Instructions on how to behave (system prompt)

**Example prompt sent to the generator:**

```
You are a customer support assistant.
Use only the policy context below to answer the question.

Policy Context:
Refunds are processed within 5–7 business days after quality check.

Customer Question:
How long will my refund take?
```

**Generated answer:**
*Your refund will usually be processed within 5–7 business days after the returned product passes quality check.*

---

## Building the E-Commerce RAG System

Now that we understand every component, it is time to build the full pipeline. We will use two libraries — `openai` for embeddings and LLM generation, and `chromadb` for the vector database.

### Sample Policy Documents We Will Use

| Customer Query | Relevant Policy |
| -------------- | --------------- |
| Can I return shoes after 15 days? | Return Policy |
| When will I get my refund? | Refund Policy |
| Is express shipping available? | Shipping Policy |
| Does warranty cover water damage? | Warranty Policy |
| Can I cancel my order after shipping? | Cancellation Policy |

The five policy documents we will store in our RAG system:

> **Return Policy:** Customers can return eligible products within 30 days of delivery. Products must be unused, undamaged, and in original packaging. Digital products, opened personal care items, and perishable goods are not eligible for return.

> **Refund Policy:** Refunds are processed after the returned product passes quality check. Refunds to cards, UPI, and net banking usually take 5–7 business days. COD refunds require bank details and may take 7–10 business days.

> **Shipping Policy:** Standard shipping takes 3–5 business days. Express shipping takes 1–2 business days and may include additional charges. Orders above ₹999 are eligible for free standard shipping. Remote pin codes may take 5–8 business days.

> **Warranty Policy:** Electronics come with a 1-year manufacturer warranty. Warranty covers manufacturing defects only. Accidental damage, liquid damage, and physical breakage are not covered. Dead-on-arrival products must be reported within 7 days of delivery.

> **Cancellation Policy:** Customers can cancel an order before it is shipped. Once the order has been shipped, cancellation is not allowed. Customers may refuse delivery or request a return after delivery if the product is eligible under the return policy.

### Environment Setup

Create a project folder and set up the environment:

```bash
# Create a new folder for the project
mkdir ecommerce-rag-demo

# Navigate into the folder
cd ecommerce-rag-demo

# Create a virtual environment to keep dependencies isolated
python3 -m venv venv

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate

# Install the required libraries
pip install openai chromadb
```

Create a new file called `ecommerce_rag.py` inside the folder.

### The Complete Code

```python
# Import the List, Dict, and Any types for type hints — helps with code readability
from typing import List, Dict, Any

# Import chromadb — this is our vector database library
import chromadb

# Import the OpenAI client to use embeddings and text generation
from openai import OpenAI

# -----------------------------------------------------------------------
# Step 1: Initialize the OpenAI client
# Make sure OPENAI_API_KEY is set as an environment variable before running
# -----------------------------------------------------------------------
openai_client = OpenAI()

# -----------------------------------------------------------------------
# Step 2: Set the model names we will use throughout the code
# EMBEDDING_MODEL converts text into vectors (numerical representations)
# GENERATION_MODEL is the LLM that will generate the final answer
# -----------------------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI embedding model
GENERATION_MODEL = "gpt-5.2"               # OpenAI LLM for text generation

# -----------------------------------------------------------------------
# Step 3: Define the sample e-commerce policy documents
# Each document has an id, the text content, and metadata (category + source)
# These five documents are our entire "knowledge base" for this demo
# -----------------------------------------------------------------------
POLICY_DOCUMENTS = [
    {
        "id": "return_policy_1",                  # Unique ID for this chunk
        "text": (
            "Customers can return eligible products within 30 days of delivery. "   # Core rule
            "Products must be unused, undamaged, and in original packaging. "       # Condition
            "Digital products, opened personal care items, and perishable goods "   # Exceptions
            "are not eligible for return."
        ),
        "metadata": {
            "category": "returns",                # Category tag for filtering
            "source": "return_policy"             # Which document this chunk came from
        }
    },
    {
        "id": "refund_policy_1",                  # Unique ID for refund chunk
        "text": (
            "Refunds are processed after the returned product passes quality check. "    # Step 1
            "Refunds to cards, UPI, and net banking usually take 5 to 7 business days. "# Timeline
            "COD refunds require bank details and may take 7 to 10 business days."      # COD case
        ),
        "metadata": {
            "category": "refunds",                # Category for filtering
            "source": "refund_policy"             # Source document name
        }
    },
    {
        "id": "shipping_policy_1",                # Unique ID for shipping chunk
        "text": (
            "Standard shipping takes 3 to 5 business days. "                            # Standard
            "Express shipping takes 1 to 2 business days and may include additional charges. "  # Express
            "Orders above 999 rupees are eligible for free standard shipping. "         # Free shipping rule
            "Remote pin codes may take 5 to 8 business days."                           # Remote areas
        ),
        "metadata": {
            "category": "shipping",               # Category for filtering
            "source": "shipping_policy"           # Source document name
        }
    },
    {
        "id": "warranty_policy_1",                # Unique ID for warranty chunk
        "text": (
            "Electronics come with a 1-year manufacturer warranty. "                    # Coverage period
            "Warranty covers manufacturing defects only. "                              # What is covered
            "Accidental damage, liquid damage, and physical breakage are not covered. " # Exclusions
            "Dead-on-arrival products must be reported within 7 days of delivery."      # DOA rule
        ),
        "metadata": {
            "category": "warranty",               # Category for filtering
            "source": "warranty_policy"           # Source document name
        }
    },
    {
        "id": "cancellation_policy_1",            # Unique ID for cancellation chunk
        "text": (
            "Customers can cancel an order before it is shipped. "                      # Before shipment
            "Once the order has been shipped, cancellation is not allowed. "            # After shipment rule
            "Customers may refuse delivery or request a return after delivery "         # Post-delivery option
            "if the product is eligible under the return policy."
        ),
        "metadata": {
            "category": "cancellation",           # Category for filtering
            "source": "cancellation_policy"       # Source document name
        }
    }
]


# -----------------------------------------------------------------------
# Step 4: Function to create embeddings for a list of text strings
# Sends the texts to OpenAI and gets back a list of float vectors
# -----------------------------------------------------------------------
def create_embeddings(texts: List[str]) -> List[List[float]]:
    # Call OpenAI's embeddings API with the chosen embedding model
    response = openai_client.embeddings.create(
        model=EMBEDDING_MODEL,   # Use the embedding model we defined above
        input=texts              # Pass the list of text strings
    )
    # Extract only the embedding vectors from the response object
    embeddings = [item.embedding for item in response.data]
    # Return the list of embedding vectors
    return embeddings


# -----------------------------------------------------------------------
# Step 5: Function to create and connect to the ChromaDB vector database
# PersistentClient saves data to disk so we don't lose data on restart
# -----------------------------------------------------------------------
def setup_vector_database():
    # Create a persistent ChromaDB client that stores data in "./chroma_policy_db" folder
    chroma_client = chromadb.PersistentClient(path="./chroma_policy_db")

    # Get an existing collection or create a new one if it does not exist
    # "cosine" distance means we measure similarity by angle, not raw distance
    collection = chroma_client.get_or_create_collection(
        name="ecommerce_policy_collection",   # Name of the collection
        metadata={"hnsw:space": "cosine"}     # Use cosine similarity for search
    )

    # Return the collection object so other functions can use it
    return collection


# -----------------------------------------------------------------------
# Step 6: Function to index (store) all policy documents into ChromaDB
# We store the text, metadata, and embeddings together for each document
# -----------------------------------------------------------------------
def index_policy_documents(collection):
    # Extract the "id" field from each policy document into a list
    ids = [doc["id"] for doc in POLICY_DOCUMENTS]

    # Extract the "text" field from each policy document into a list
    texts = [doc["text"] for doc in POLICY_DOCUMENTS]

    # Extract the "metadata" field from each policy document into a list
    metadatas = [doc["metadata"] for doc in POLICY_DOCUMENTS]

    # Generate embeddings for all policy texts in one API call
    embeddings = create_embeddings(texts)

    # Store everything in ChromaDB using upsert
    # upsert = update if ID exists, insert if it does not — safe to run multiple times
    collection.upsert(
        ids=ids,               # Unique IDs for each chunk
        documents=texts,       # Raw text content of each chunk
        metadatas=metadatas,   # Category and source metadata
        embeddings=embeddings  # Vector representations of each chunk
    )

    # Print a confirmation message once all documents are stored
    print(f"Indexed {len(POLICY_DOCUMENTS)} policy documents successfully.")


# -----------------------------------------------------------------------
# Step 7: Retriever function — finds most relevant policy chunks
# Converts the user query to an embedding and searches ChromaDB
# -----------------------------------------------------------------------
def retrieve_policy_content(
    collection,
    query: str,
    top_k: int = 3    # top_k controls how many chunks to retrieve
) -> List[Dict[str, Any]]:

    # Convert the user query into an embedding vector using OpenAI
    query_embedding = create_embeddings([query])[0]  # [0] because we only sent one query

    # Search ChromaDB for the top_k most similar policy chunks
    results = collection.query(
        query_embeddings=[query_embedding],                      # Query vector
        n_results=top_k,                                         # Number of results to fetch
        include=["documents", "metadatas", "distances"]          # What to include in response
    )

    # Build a clean list of retrieved chunks with text, metadata, and distance
    retrieved_chunks = []
    documents = results["documents"][0]   # List of matching text strings
    metadatas = results["metadatas"][0]   # List of matching metadata dicts
    distances = results["distances"][0]   # List of similarity distances (lower = more similar)

    # Loop through results and combine them into one dictionary per chunk
    for document, metadata, distance in zip(documents, metadatas, distances):
        retrieved_chunks.append({
            "text": document,       # The policy text
            "metadata": metadata,   # Category and source info
            "distance": distance    # How close this chunk is to the query
        })

    # Return the list of retrieved chunks
    return retrieved_chunks


# -----------------------------------------------------------------------
# Step 8: Helper function to print retrieved chunks so we can inspect them
# This helps students see what the retriever found before the LLM answers
# -----------------------------------------------------------------------
def print_retrieved_chunks(query: str, chunks: List[Dict[str, Any]]):
    # Print a divider and the customer query
    print("\n" + "=" * 80)
    print(f"Customer Query: {query}")
    print("=" * 80)

    # Loop through each retrieved chunk and print its details
    for index, chunk in enumerate(chunks, start=1):
        print(f"\nResult {index}")
        print(f"Source   : {chunk['metadata']['source']}")    # Which policy document
        print(f"Category : {chunk['metadata']['category']}")  # Which category
        print(f"Distance : {chunk['distance']:.4f}")          # Similarity score (lower = closer)
        print(f"Content  : {chunk['text']}")                  # The actual policy text


# -----------------------------------------------------------------------
# Step 9: Prompt builder — injects retrieved policy chunks into the prompt
# This is the most important step in RAG: grounding the LLM with real data
# -----------------------------------------------------------------------
def build_grounded_prompt(query: str, chunks: List[Dict[str, Any]]) -> str:
    # Build the context string by combining all retrieved chunks
    context = ""
    for index, chunk in enumerate(chunks, start=1):
        source = chunk["metadata"]["source"]  # Get source name for the chunk
        text = chunk["text"]                  # Get the chunk text
        # Append each chunk with its source label
        context += f"\nPolicy Chunk {index} | Source: {source}\n{text}\n"

    # Build the full prompt with instructions, context, and the customer question
    prompt = f"""You are a helpful customer support assistant for an e-commerce company.
Answer the customer's question using ONLY the policy context provided below.
Rules:
1. Do not make up policy details.
2. If the answer is not present in the context, say:
   "I do not have enough information in the provided policy documents."
3. Keep the answer simple, clear, and customer-friendly.
4. Mention important conditions or exceptions if they are present in the context.

Policy Context:
{context}

Customer Question:
{query}

Final Answer:"""

    # Return the fully assembled prompt
    return prompt


# -----------------------------------------------------------------------
# Step 10: Generator function — uses the LLM to answer based on context
# This is the "Generation" part of Retrieval-Augmented Generation
# -----------------------------------------------------------------------
def generate_answer_from_context(query: str, chunks: List[Dict[str, Any]]) -> str:
    # Build the grounded prompt by injecting retrieved policy chunks
    prompt = build_grounded_prompt(query, chunks)

    # Call the OpenAI LLM with the grounded prompt
    response = openai_client.responses.create(
        model=GENERATION_MODEL,    # Use the generation model we defined
        instructions=(
            "You are a precise and helpful e-commerce customer support assistant."  # System instruction
        ),
        input=prompt               # The grounded prompt with policy context
    )

    # Return the generated text from the LLM response
    return response.output_text


# -----------------------------------------------------------------------
# Step 11: Standalone LLM function — answers WITHOUT any retrieval
# This is for comparison: shows how the LLM answers from memory alone
# -----------------------------------------------------------------------
def generate_answer_without_retrieval(query: str) -> str:
    # Call the OpenAI LLM without any retrieved policy context
    response = openai_client.responses.create(
        model=GENERATION_MODEL,    # Same generation model
        instructions=(
            "You are a helpful e-commerce customer support assistant. "
            "Answer based on your general knowledge."  # No company policy given
        ),
        input=query                # Only the raw customer question — no context
    )

    # Return the generated text from the LLM
    return response.output_text


# -----------------------------------------------------------------------
# Step 12: Complete RAG pipeline — ties retrieval and generation together
# This is the main function students will call for production-style usage
# -----------------------------------------------------------------------
def answer_with_rag(collection, query: str, top_k: int = 3) -> str:
    # Step A: Retrieve the top_k most relevant policy chunks
    retrieved_chunks = retrieve_policy_content(
        collection=collection,   # The ChromaDB collection
        query=query,             # Customer's question
        top_k=top_k              # How many chunks to retrieve
    )

    # Step B: Print the retrieved chunks so we can inspect what was found
    print_retrieved_chunks(query, retrieved_chunks)

    # Step C: Generate the final grounded answer using retrieved context
    answer = generate_answer_from_context(query, retrieved_chunks)

    # Return the final answer
    return answer


# -----------------------------------------------------------------------
# Step 13: Top-K experiment — shows how retrieval depth affects answers
# Runs the same query with different top_k values so students can compare
# -----------------------------------------------------------------------
def top_k_experiment(collection, query: str):
    # Print a section header for the experiment
    print("\n" + "#" * 80)
    print("TOP-K EXPERIMENT")
    print("#" * 80)

    # Try top_k values of 1, 2, 3, and 5 one by one
    for top_k in [1, 2, 3, 5]:
        print(f"\n\n--- Answer with Top-K = {top_k} ---")

        # Retrieve chunks using the current top_k value
        chunks = retrieve_policy_content(
            collection=collection,   # ChromaDB collection
            query=query,             # The experiment query
            top_k=top_k              # Current depth we are testing
        )

        # Generate an answer using the retrieved chunks
        answer = generate_answer_from_context(query, chunks)

        # Print the generated answer for this top_k level
        print(answer)


# -----------------------------------------------------------------------
# Step 14: Main function — runs the full demo from start to finish
# -----------------------------------------------------------------------
def main():
    # Step A: Set up the ChromaDB vector database (creates or reuses the collection)
    collection = setup_vector_database()

    # Step B: Index all five policy documents into the vector database
    index_policy_documents(collection)

    # Step C: Define a sample customer query for the demo
    sample_query = "How long will it take to get my refund for a COD order?"

    # Step D: First, answer WITHOUT retrieval (LLM from memory only)
    print("\n\nWITHOUT RETRIEVAL:")
    print("-" * 80)
    answer_without_rag = generate_answer_without_retrieval(sample_query)
    print(answer_without_rag)

    # Step E: Now answer WITH RAG (retrieval + LLM)
    print("\n\nWITH RAG:")
    print("-" * 80)
    answer_with_retrieval = answer_with_rag(
        collection=collection,   # ChromaDB collection
        query=sample_query,      # Customer's question
        top_k=3                  # Retrieve top 3 most relevant chunks
    )
    print("\nFinal RAG Answer:")
    print(answer_with_retrieval)

    # Step F: Run the top-K experiment to show how depth affects answers
    top_k_experiment(
        collection=collection,
        query="Can I return an electronic item if it has liquid damage?"
    )


# Standard Python entry point — runs main() only when script is executed directly
if __name__ == "__main__":
    main()
```

### How the Code Works

- **`POLICY_DOCUMENTS`** is a list of five dictionaries. Each dictionary holds the policy text, a unique ID, and metadata (category + source name) — this is our entire knowledge base.
- **`create_embeddings(texts)`** sends a list of text strings to OpenAI's `text-embedding-3-small` model and gets back a list of float vectors — one vector per text.
- **`setup_vector_database()`** creates a local ChromaDB collection stored on disk. Using `PersistentClient` means the data survives after the script stops.
- **`index_policy_documents(collection)`** stores all five policy chunks — along with their embeddings and metadata — into ChromaDB using `upsert`. Using `upsert` instead of `add` ensures no duplicate errors if we run the script again.
- **`retrieve_policy_content(collection, query, top_k)`** converts the user's question into an embedding and asks ChromaDB to return the `top_k` most similar policy chunks. The `distance` tells us how close or far the match is — lower distance means more similar.
- **`print_retrieved_chunks(query, chunks)`** is a debug helper that prints each retrieved chunk with its source, category, distance, and text. This lets students verify that the retriever is finding the right content.
- **`build_grounded_prompt(query, chunks)`** assembles the final prompt by injecting all retrieved policy chunks as context. This is the core RAG step — we are giving the LLM its open book before asking it to answer.
- **`generate_answer_from_context(query, chunks)`** calls the LLM with the grounded prompt and returns the final answer. The LLM must answer only from the provided context.
- **`generate_answer_without_retrieval(query)`** calls the LLM with no context — just the raw question. This produces a generic, ungrounded answer, useful for comparison.
- **`answer_with_rag(collection, query, top_k)`** is the complete pipeline: retrieve → print → generate. This is the function students would call in a real application.
- **`top_k_experiment(collection, query)`** runs the same query with `top_k` values of 1, 2, 3, and 5 so students can see how retrieval depth changes the final answer quality.

### How to Run the Code

Run the script from your terminal:

```bash
python ecommerce_rag.py
```

**Expected output flow:**

```
Indexed 5 policy documents successfully.
```

Then the terminal prints:

```
WITHOUT RETRIEVAL:
--------------------------------------------------------------------------------
Most e-commerce companies process refunds within 7-10 business days...
(generic LLM answer with no company-specific detail)
```

Then:

```
WITH RAG:
================================================================================
Customer Query: How long will it take to get my refund for a COD order?
================================================================================

Result 1
Source   : refund_policy
Category : refunds
Distance : 0.1234
Content  : Refunds are processed after the returned product passes quality check...

Final RAG Answer:
For a COD order, your refund will be processed after the returned product
passes quality check and may take 7 to 10 business days. Please keep your
bank account details ready for the refund transfer.
```

![Example terminal output when running the ecommerce RAG script (indexing, retrieval, and answers)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session29/rag-notes-image3-run-output.png)

---

## End-to-End RAG Flow — Full Picture

Now that we have seen the code, let us look at the complete flow in one diagram so the whole picture is clear:

```
Customer asks a question.
    ↓
System converts question into an embedding vector.
    ↓
Vector database (ChromaDB) finds policy chunks with similar vectors.
    ↓
Retrieved chunks are inserted into the LLM prompt as context.
    ↓
LLM reads context and generates a grounded, accurate answer.
    ↓
Customer receives a policy-backed response.
```

![End-to-end RAG flow from customer question to embedding, chunk retrieval, prompt assembly, and grounded response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session29/rag-notes-image4-end-to-end-flow.png)

**A concrete example of the full flow:**

- **Query:** "Can I cancel my order after shipping?"
- **Retrieved Context:** "Customers can cancel an order before it is shipped. Once the order has been shipped, cancellation is not allowed."
- **Answer:** "You can cancel an order only before it is shipped. Once it has been shipped, cancellation is not allowed."

---

## Experimenting With Retrieval Depth: Top-K

Now that the full pipeline works, let us explore one important tuning parameter — **Top-K**.

- **Official Definition:** **Top-K** is the parameter that controls how many document chunks the retriever fetches for each query. Setting `top_k = 3` means retrieve the 3 most similar chunks.
- **In Simple Words:** Top-K is like asking a librarian to bring you 1 book, 3 books, or 5 books on the same topic. Bringing too few means you might miss important details. Bringing too many means you get extra, irrelevant pages.
- **Real-Life Example:** If you search "best phone under 20000" and the results show only 1 phone, you might miss a better option. But if results show 50 phones, you get confused. The right number is somewhere in between.

| Top-K Value | What Happens |
| ----------- | ------------ |
| Too low (1) | May miss important context; answer is incomplete |
| Balanced (3) | Gives enough relevant context; answer is accurate |
| Too high (5+) | May include irrelevant chunks; LLM gets confused |

**Common doubt:** *"Should I always use the highest top-K to be safe?"*

- No. A higher top-K means more tokens in the prompt, which increases cost.
- It also risks adding noise — unrelated chunks that mislead the LLM.
- A balanced top-K of 3 to 5 is the standard starting point for most RAG systems.

---

## Key Takeaways

- **RAG solves the grounding problem** — instead of letting an LLM guess, we retrieve real policy documents and inject them into the prompt so the answer is always fact-based.
- **The pipeline has three main jobs** — Retrieve (find the right chunks from ChromaDB), Build Prompt (inject those chunks as context), and Generate (ask the LLM to answer using only that context).
- **Chunking and embeddings are the foundation** — without proper chunking, the retriever returns noisy results; without good embeddings, semantic similarity search does not work.
- **Top-K is a balance** — too few retrieved chunks means incomplete answers; too many chunks adds noise and increases cost; 3 to 5 is the practical sweet spot.
- **Grounded vs. ungrounded answers are very different** — comparing the two outputs side by side is the clearest proof of why RAG matters in any real-world application.

In the next session, we will go deeper into **advanced RAG patterns** — including how to handle multi-document queries, how to add metadata filtering to make retrieval more precise, and how a RAG system fits inside a larger **agentic workflow** where the AI decides when to retrieve and when to answer from memory.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Meaning |
| -------------- | ------- |
| **RAG** | Retrieval-Augmented Generation — search relevant data + generate answer using that data |
| **Retriever** | Component that converts query to embedding and fetches relevant chunks from vector DB |
| **Generator** | The LLM that reads retrieved context and produces the final natural language answer |
| **Grounding** | Basing an LLM answer on real retrieved documents instead of model memory |
| **Hallucination** | When an LLM confidently generates false information from memory |
| **Knowledge Source** | The document(s) used as the knowledge base (e.g., return policy, shipping policy) |
| **Document Chunk** | A small piece of a larger document stored individually for precise retrieval |
| **Embedding** | A list of numbers that captures the meaning of a piece of text |
| **Vector Database** | A database that stores embeddings and supports fast similarity-based search |
| **ChromaDB** | An open-source vector database used to store and search policy chunk embeddings |
| **Top-K** | Parameter controlling how many chunks the retriever returns per query |
| **Cosine Similarity** | A distance metric measuring how similar two vectors are by the angle between them |
| **upsert** | A database operation that inserts a record if it does not exist, or updates it if it does |
| **PersistentClient** | ChromaDB mode that saves data to disk so embeddings survive across script runs |
| `pip install openai chromadb` | Command to install the required libraries |
| `chromadb.PersistentClient(path=...)` | Creates or connects to a local ChromaDB database stored at the given path |
| `get_or_create_collection(name=...)` | Gets existing ChromaDB collection by name, or creates it if not present |
| `collection.upsert(...)` | Stores documents, embeddings, and metadata into ChromaDB |
| `collection.query(query_embeddings=..., n_results=...)` | Searches ChromaDB and returns the top n most similar chunks |
| `openai_client.embeddings.create(model=..., input=...)` | Converts text strings into embedding vectors using OpenAI |
| `openai_client.responses.create(model=..., instructions=..., input=...)` | Calls the OpenAI LLM to generate a text response |
| `text-embedding-3-small` | OpenAI embedding model used to convert text into vectors |
| `gpt-5.2` | OpenAI LLM model used for generating grounded answers |
