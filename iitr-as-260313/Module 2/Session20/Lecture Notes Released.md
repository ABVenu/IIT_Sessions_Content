# RAG Architecture and Pipeline

## Context of This Session

In the previous session, you learned **why** **Retrieval-Augmented Generation (RAG)** matters for **ShopKart** customer support. You compared **ungrounded** LLM-style answers with **grounded** policy-backed replies, and you mapped the **retrieve** step to the **embedding + top-k vector search** pipeline you already built with **Chroma**.

That work answered the *theory* question: *"Why should we search first and generate second?"* Today's question is the *implementation* question: *"How do we wire retrieval and generation into one working loop?"*

**In this session, you will:**

- Frame **e-commerce customer support** as a **RAG problem** — purpose, users, knowledge boundaries, and policy documents
- Build **knowledge sources** as searchable policy chunks inside **Chroma**
- Use your **previous Chroma setup** as the **retriever** layer
- Add an **LLM generator** that answers only from retrieved evidence
- Run the full **retrieve → generate** loop on representative ShopKart support questions
- Inspect whether **semantic retrieval** matched the customer's **intent**

This session is **hands-on implementation**. You will write one complete Python script that turns ShopKart policy text into grounded support answers.

---

## The Running Example — ShopKart Support Assistant

You continue with **ShopKart**, the online store from the previous session. Customers ask about **returns**, **shipping**, **warranty**, and **refunds**. The assistant must answer from **official policy text**, not from the model's general memory.

### Who Uses This Assistant?

| Stakeholder | What they need |
|---|---|
| **Customer** | Clear, correct answers about eligibility, timelines, and exceptions |
| **Support team** | Fewer wrong promises that create escalations |
| **Business** | Answers traceable to live policy documents |

- **Official Definition:** A **knowledge boundary** is the set of topics and documents an AI system is allowed to use when answering — everything outside that boundary should be refused or escalated.
- **In Simple Words:** The bot is only allowed to speak from the **company rule book**, not from random internet guesses.
- **Real-Life Example:** A **bank phone line** agent who may only quote the bank's published loan brochure — not what they heard from a friend.

![ShopKart knowledge boundary — customers, support team, and business need answers traceable to the policy rule book; topics outside that boundary should be refused or escalated](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-01-knowledge-boundary.png)

### ShopKart Policy Knowledge Base

These four policy areas are your **knowledge sources** for today's lab. Each row becomes one stored chunk in Chroma.

| Policy area | Official text (source of truth) |
|---|---|
| **Returns** | Unopened items may be returned within **7 calendar days** of delivery. Opened or used items are not eligible unless defective. |
| **Shipping** | Standard delivery takes **3–5 business days** after dispatch. Express delivery (paid) arrives in **1–2 business days** in metro cities only. |
| **Warranty** | Electronics carry a **12-month manufacturer warranty** from the date of delivery. Warranty does not cover physical damage or liquid exposure. |
| **Refunds** | Refunds are credited within **5–7 business days** after the returned item passes warehouse verification. Cash-on-delivery orders are refunded to the original UPI or bank account only. |

- **Official Definition:** A **knowledge source** is a trusted document or text record that a RAG system may retrieve from when answering domain-specific questions.
- **In Simple Words:** The **reference material** the retriever is allowed to search — like the policy pages pinned behind a support desk.
- **Real-Life Example:** A coaching centre's **fee refund notice** posted on the office wall — not whatever the receptionist remembers from last year.

**Integrated learning point:** If a customer asks about **returns**, the assistant should pull **Returns** and sometimes **Refunds** text — not **Warranty** alone. Your retriever's job is to find the right shelf before the generator speaks.

![Four ShopKart policy areas indexed as Chroma chunks — Returns, Shipping, Warranty, and Refunds each become one row in shopkart_policy_kb for semantic retrieval](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-02-policy-chunks-chroma.png)

### Simple Activity — Map Questions to Policy Areas

In your notebook, match each customer line to the primary policy area (**Returns / Shipping / Warranty / Refunds**):

1. *"I opened the earphones — can I send them back?"*
2. *"Express delivery to Delhi — how fast?"*
3. *"My phone fell in water — is repair free under warranty?"*
4. *"COD order returned — when will money come to my UPI?"*

Write one sentence per line explaining **why** that policy area is the best starting search target.

---

## Three Components of a Minimal RAG Pipeline

Before you open your editor, see how today's code maps to three named roles you will hear in every RAG discussion: **ingestion**, **retrieval**, and **generation**.

```mermaid
flowchart LR
    Q[Customer question] --> R[Retriever]
    K[(Knowledge sources in Chroma)] --> R
    R --> C[Retrieved context]
    C --> G[Generator LLM]
    Q --> G
    G --> A[Grounded answer]
```

| Component | Job in ShopKart | Today's tool |
|---|---|---|
| **Ingestion** | Prepare policy text, embed it, and store vectors in Chroma | Python list → **BGE** embeddings → **`collection.upsert`** |
| **Retriever** | Find top-k chunks whose **meaning** matches the question | **Sentence Transformers** + **`collection.query`** |
| **Generator** | Turn retrieved text + question into a polite reply | **Groq** chat API with a **Llama** model |

- **Official Definition:** A **retriever** converts a user query into a search request and returns the most relevant passages from a knowledge store.
- **In Simple Words:** The **smart search** step — it finds policy paragraphs before anyone writes an answer.
- **Real-Life Example:** A **library assistant** who runs a catalog search and places three relevant books on the desk before you read them.

- **Official Definition:** A **generator** is the language model component that produces natural-language output conditioned on the user query and supplied context.
- **In Simple Words:** The **writer** that explains the policy in friendly sentences — but only after the retriever hands over the facts.
- **Real-Life Example:** A trained **support executive** who reads the highlighted policy clause and then types the reply to the customer.

**Connecting sentence:** You already built the **retriever engine** in the previous hands-on session (Chroma + embeddings). Today you **reuse that pattern**, complete the **ingestion → retrieval → generation** loop, and add the **generator** so retrieved chunks become full answers — not just ranked text in a terminal.

### Ingestion — From Raw Policy Text to Stored Vectors

In production, ingestion often starts with raw HTML or PDFs, then cleaning, chunking, embedding, and storage. In today's minimal lab, your policy text is **already chunked** in `POLICY_RECORDS` — so ingestion focuses on **embed → upsert into Chroma**.

- **Official Definition:** **Ingestion** is the offline pipeline that prepares trusted documents, converts them into embeddings, and loads them into a searchable vector store.
- **In Simple Words:** The **filing step** — you sort policy pages into labelled folders and index them before anyone asks a question.
- **Real-Life Example:** A coaching centre scanning fee-refund notices, typing them into short paragraphs, and pinning them behind the reception desk before opening for admissions.

**Common doubt:** *"Is vector search alone the same as RAG?"* — No. Search returns chunks; **RAG** also **generates** an answer that should follow those chunks. Until generation happens with clear **use-this-evidence** instructions, you have retrieval — not a complete assistant.

![Three components of a minimal RAG pipeline — knowledge sources in Chroma, retriever with embeddings and top-k query, and generator LLM that writes only from retrieved evidence](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-03-three-rag-components.png)

---

## Project Setup

Create a dedicated folder for today's lab. You need the same two libraries from your vector search lab, plus the **Groq** client and **python-dotenv** for secure API key loading.

### Install Commands

```bash
mkdir shopcart_rag  # Create a folder for today's RAG script and Chroma data
cd shopcart_rag  # Work inside this folder so chroma_store path stays consistent
pip install chromadb  # Vector database client — same library as the previous lab
pip install -U sentence-transformers  # Local embedding model for retriever (BGE)
pip install groq  # Groq Python client for the generator step
pip install python-dotenv  # Load API keys safely from a .env file
```

**How the code works:**

- **`chromadb`** provides **`PersistentClient`**, **`get_or_create_collection`**, **`upsert`**, and **`query`** — your retriever storage layer.
- **`sentence-transformers`** loads the **BGE** embedding model so you embed policy text and customer questions on your laptop without a separate embedding API.
- **`groq`** sends the grounded prompt to a hosted **Llama** model and returns the final answer text.
- **`python-dotenv`** reads secrets from a **`.env`** file so keys never sit inside your Python source.

![Lab stack — chromadb for persistent vectors, sentence-transformers for local BGE embeddings, and Groq for the generator; API key stays in .env, not in Git](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-04-lab-stack.png)

### Groq API Key and `.env` Setup

The **retriever** runs locally. The **generator** calls a hosted LLM through the **Groq** API.

1. Create a free account at [groq.com](https://groq.com) and click **Create API Key**.
2. Copy the key once — treat it like a password. Do not share it in chat or commit it to Git.
3. In the same folder as `rag.py`, create a file named **`.env`**:

```bash
GROQ_API_KEY=your-key-here
```

4. Add **`.env`** to **`.gitignore`** so Git never uploads your secret.
5. Optionally add a **`.env.example`** file (without the real key) so teammates know which variable name to use:

```bash
GROQ_API_KEY=
```

- **Official Definition:** An **API key** is a secret token that proves your code is allowed to call a provider's hosted model.
- **In Simple Words:** The **password** your script uses to talk to Groq's servers.
- **Real-Life Example:** A **metro smart card** — without it, the gate will not open even if you know which train to take.

**Common mistake:** Pasting the API key inside `rag.py`. Always keep it in **`.env`** and load it with **`load_dotenv()`**.

### Simple Activity — Environment Checklist

In your notebook, tick each item after you verify it:

- [ ] Python 3.10+ running
- [ ] `import chromadb` succeeds
- [ ] `from sentence_transformers import SentenceTransformer` succeeds
- [ ] `from groq import Groq` succeeds
- [ ] `from dotenv import load_dotenv` succeeds
- [ ] `.env` file exists with `GROQ_API_KEY` set

---

## Step 1 — Define Knowledge Sources as Policy Records

Good RAG starts with **clean, small chunks** — one main idea per row. For ShopKart, four policy paragraphs are enough for a **minimal** pipeline.

Create a file named `rag.py` and start with the master policy list:

```python
# rag.py — minimal RAG loop for ShopKart customer support

from typing import List, Dict, Any  # Type hints for readable function signatures
import os  # Read environment variables like GROQ_API_KEY
import chromadb  # Vector database for storing and searching policy chunks
from sentence_transformers import SentenceTransformer  # Local BGE embedding model for retriever
from groq import Groq  # Client for Groq LLM generation API calls
from dotenv import load_dotenv  # Load secrets from .env file safely

load_dotenv()  # Read GROQ_API_KEY from .env before any API call

# ---------------------------------------------------------------------------
# ShopKart policy records — these are our knowledge sources for this lab
# Each dict becomes one row in Chroma: id, text, metadata
# ---------------------------------------------------------------------------
POLICY_RECORDS = [
    {  # Returns policy chunk
        "id": "shopkart_returns_1",  # Unique primary key for this policy row
        "text": (
            "Unopened items may be returned within 7 calendar days of delivery. "
            "Opened or used items are not eligible unless defective."
        ),  # Human-readable returns rule — source of truth for return questions
        "metadata": {"category": "returns", "source": "returns_policy"},  # Tags for display and later filtering
    },
    {  # Shipping policy chunk
        "id": "shopkart_shipping_1",  # Unique id for shipping row
        "text": (
            "Standard delivery takes 3 to 5 business days after dispatch. "
            "Express delivery (paid) arrives in 1 to 2 business days in metro cities only."
        ),  # Shipping timelines customers ask about often
        "metadata": {"category": "shipping", "source": "shipping_policy"},  # Shipping category tag
    },
    {  # Warranty policy chunk
        "id": "shopkart_warranty_1",  # Unique id for warranty row
        "text": (
            "Electronics carry a 12-month manufacturer warranty from the date of delivery. "
            "Warranty does not cover physical damage or liquid exposure."
        ),  # Warranty coverage and exclusions
        "metadata": {"category": "warranty", "source": "warranty_policy"},  # Warranty category tag
    },
    {  # Refund policy chunk
        "id": "shopkart_refunds_1",  # Unique id for refund row
        "text": (
            "Refunds are credited within 5 to 7 business days after the returned item "
            "passes warehouse verification. Cash-on-delivery orders are refunded to the "
            "original UPI or bank account only."
        ),  # Refund timing and COD path
        "metadata": {"category": "refunds", "source": "refunds_policy"},  # Refunds category tag
    },
]

# BGE embedding model — MUST stay the same for documents and every query
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"  # BGE model from Beijing Academy of AI — 384-dim vectors

# Llama model on Groq for generation — course-friendly default; your org may allow a different name
GENERATION_MODEL_NAME = "llama-3.1-8b-instant"  # Groq-hosted Llama model used as the generator
```

**How the code works:**

- **`POLICY_RECORDS`** is the **knowledge base** — four trusted chunks covering ShopKart's main support topics.
- Each **`id`** must be unique so **`upsert`** can insert or update rows safely.
- **`metadata`** stores **`category`** and **`source`** labels — useful for debugging retrieval today; advanced **metadata filtering** comes in a **later** session.
- **`EMBEDDING_MODEL_NAME`** points to a **BGE** model that outputs **384-dimensional** vectors — each policy sentence becomes a list of 384 numbers.
- **`load_dotenv()`** must run before creating the Groq client so **`GROQ_API_KEY`** is available from your **`.env`** file.

**Integrated learning point:** Outdated or wrong policy text in this list produces "grounded" wrong answers with extra confidence. Production teams version and update knowledge sources; today you focus on **architecture**, not document management.

### Simple Activity — Trace One Record

Pick **`shopkart_refunds_1`**. In your notebook, write: (1) the full policy text, (2) the **`category`** metadata value, (3) one customer question that should retrieve this row before the others.

---

## Step 2 — Connect to Chroma and Index Policy Chunks

This step reuses the **PersistentClient → collection → embed → upsert** pattern from your previous vector search lab. The collection becomes the **physical home** of ShopKart's knowledge sources.

```python
def create_embedding_model() -> SentenceTransformer:
    # Load the local embedding model once — reuse for all encode calls in this script
    return SentenceTransformer(EMBEDDING_MODEL_NAME)  # Downloads ~80MB on first run


def setup_chroma_collection():
    # Connect to on-disk Chroma storage in ./chroma_store (survives after script ends)
    client = chromadb.PersistentClient(path="./chroma_store")  # Local persistent database folder

    # Open or create the ShopKart policy collection — separate name from older demo collections
    collection = client.get_or_create_collection(
        name="shopkart_policy_kb",  # Named bucket for ShopKart policy rows
        embedding_function=None,  # We pass embeddings manually — same teaching pattern as before
    )

    return collection  # Return collection handle for upsert and query


def index_policy_records(collection, model: SentenceTransformer) -> None:
    # Build parallel lists from POLICY_RECORDS — index alignment matters for upsert
    ids = [row["id"] for row in POLICY_RECORDS]  # One unique id per policy chunk
    documents = [row["text"] for row in POLICY_RECORDS]  # Plain text stored and returned in search
    metadatas = [row["metadata"] for row in POLICY_RECORDS]  # Category and source tags per row

    # Encode all policy texts to vectors in one batch — same model as queries later
    embeddings = model.encode(documents, convert_to_numpy=True).tolist()  # Chroma expects Python lists

    # Write all rows into Chroma — upsert is safe to rerun (updates by id if already present)
    collection.upsert(
        ids=ids,  # Primary keys
        documents=documents,  # Readable policy sentences
        metadatas=metadatas,  # Tags stored alongside each row
        embeddings=embeddings,  # Meaning vectors used for similarity search
    )

    print(f"Indexed {collection.count()} ShopKart policy records.")  # Expect 4 after first successful run
```

**How the code works:**

- **`setup_chroma_collection`** mirrors your previous lab — only the **collection name** changes to **`shopkart_policy_kb`**.
- **`embedding_function=None`** means **you** call **`model.encode`** — no hidden embedding inside Chroma.
- **`index_policy_records`** is an **offline** step: run it once (or again when policy text changes) before answering live customer questions.
- After upsert, **`collection.count()`** should print **4**. If not, fix indexing before building the retriever.

![Index policy records in Chroma — offline batch embed of POLICY_RECORDS, then upsert ids, documents, metadata, and embeddings into shopkart_policy_kb](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-05-index-chroma.png)

### BGE Embeddings and 384 Dimensions

The **BGE** (Beijing General Embedding) model converts each policy sentence into a fixed-length list of numbers called an **embedding**.

- **Official Definition:** An **embedding** is a numeric vector that represents the meaning of a text passage in a form suitable for similarity search.
- **In Simple Words:** A **fingerprint of meaning** — similar sentences get similar number patterns.
- **Real-Life Example:** Two different customers asking *"refund delay"* and *"when will money come back"* should produce vectors close enough for Chroma to surface the **Refunds** chunk.

The BGE small model used here creates **384-dimensional** embeddings. That means every policy chunk becomes a list of **384** numbers stored in Chroma.

**Common doubt:** *"Will my distance numbers match the instructor's exactly?"* — Not always. Embedding models are predictive; distances can vary slightly between runs or machines even for the same sentence. Focus on **which policy area ranks first**, not on matching every decimal place.

**Common mistake:** Running the script from two different folders creates two different **`./chroma_store`** paths. Always **`cd`** into **`shopcart_rag`** before executing.

### Simple Activity — Verify the Index

After running the index function once, add these lines temporarily and record the output in your notebook:

```python
print("Count:", collection.count())  # Should be 4
print("Peek sample:", collection.peek())  # Eyeball ids and document text
```

Note one **`id`**, one **`category`** from metadata, and confirm all four policy areas appear.

---

## Step 3 — Build the Retriever

The **retriever** is the bridge between a customer's words and the stored policy chunks. It embeds the question, runs **top-k** similarity search, and returns ranked evidence.

- **Official Definition:** **Top-k retrieval** returns the **k** stored items whose embedding vectors are nearest to the query vector.
- **In Simple Words:** *"Bring me the **k** best-matching policy paragraphs by meaning."*
- **Real-Life Example:** Asking a shopkeeper for the **two most relevant** FAQ printouts for *"refund delay"* — not the entire filing cabinet.

For today's minimal pipeline, **`top_k=2`** is a reasonable starting point with only four chunks. **Tuning** how many chunks to fetch — and **filtering** by metadata — is covered in a **later** session.

```python
def retrieve_policy_chunks(
    collection,
    model: SentenceTransformer,
    user_query: str,
    top_k: int = 2,
) -> List[Dict[str, Any]]:
    # Convert the customer's question into an embedding vector using the SAME model as indexing
    query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()  # Batch of one query

    # Ask Chroma for the nearest stored policy vectors to this question vector
    results = collection.query(
        query_embeddings=query_embedding,  # Query as numbers — not raw string
        n_results=top_k,  # How many chunks to return (top-k)
        include=["documents", "metadatas", "distances"],  # Ask for text, tags, and scores
    )

    retrieved = []  # Clean list we will pass to the generator

    # Loop through each rank in the top-k result lists — index 0 is best match
    for doc, meta, dist in zip(
        results["documents"][0],  # Matched policy text strings
        results["metadatas"][0],  # Metadata dicts aligned with each match
        results["distances"][0],  # Distance scores — lower usually means closer meaning
    ):
        retrieved.append(
            {
                "text": doc,  # Policy excerpt text
                "metadata": meta,  # Source and category labels
                "distance": dist,  # Similarity score for inspection
            }
        )

    return retrieved  # List of dicts — retriever output for this query
```

**How the code works:**

- **`model.encode([user_query], ...)`** applies the **same model rule** — never swap embedding models between index and query.
- **`collection.query`** is exactly the skill from your previous lab — now wrapped inside a named **`retrieve_policy_chunks`** function.
- **`distance`** helps you **inspect** retrieval quality; it does not go to the customer directly.
- The retriever **does not** call the LLM — it only returns evidence.

![Retriever step — embed the customer question, run Chroma top-k query, return ranked policy excerpts with category metadata and distance scores for inspection](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-06-retriever-topk.png)

### Simple Activity — Inspect Retrieval Intent

Run the retriever alone with this question: *"I want my money back after returning a COD order."*

Print each result's **`metadata["category"]`**, **`text`**, and **`distance`**. Answer in your notebook:

- Did **refunds** (or **returns**) rank first?
- Would a human support agent agree this is the right policy area?
- If the wrong chunk ranked first, note the wording that may have confused the search — you will tune this in a **later** session.

---

## Step 4 — Build the Grounded Prompt and Generator

The **generator** receives the customer question plus **retrieved context**. Your prompt must tell the model to **stick to the evidence**.

```python
def build_grounded_prompt(user_query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    # Stitch retrieved policy excerpts into one context block the LLM can read
    context_block = ""  # Start empty — append each chunk with a label
    for index, chunk in enumerate(retrieved_chunks, start=1):  # Number chunks for clarity
        source_name = chunk["metadata"].get("source", "unknown")  # Which policy file this came from
        context_block += f"\nExcerpt {index} (source: {source_name}):\n{chunk['text']}\n"  # One labeled paragraph

    # Full instruction prompt — rules + evidence + question
    prompt = f"""You are ShopKart customer support.
Answer the customer's question using ONLY the policy excerpts below.
Rules:
1. Do not invent numbers, timelines, or eligibility rules not present in the excerpts.
2. If the excerpts do not contain enough information, say:
   "I do not have enough information in the provided policy excerpts."
3. Keep the answer short, polite, and clear.
4. Mention important conditions (opened vs unopened, metro-only express, COD refund path) when they appear in the excerpts.

Policy excerpts:
{context_block}

Customer question:
{user_query}

Final answer:"""

    return prompt  # String ready to send to the LLM API


def generate_grounded_answer(client: Groq, user_query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    # Build the grounded prompt from retrieved evidence
    prompt = build_grounded_prompt(user_query, retrieved_chunks)  # Context + question + rules

    # Call the hosted LLM — generator step of RAG
    response = client.chat.completions.create(
        model=GENERATION_MODEL_NAME,  # Which LLM writes the final reply
        messages=[
            {
                "role": "system",  # High-level behavior instruction
                "content": "You are a precise ShopKart support assistant. Follow the policy excerpts exactly.",
            },
            {"role": "user", "content": prompt},  # Grounded prompt with evidence block
        ],
    )

    # Extract assistant text from the API response object
    return response.choices[0].message.content.strip()  # Final grounded answer string
```

**How the code works:**

- **`build_grounded_prompt`** is the **context injection** step — retrieved chunks become the **evidence block** from the previous session's diagrams.
- System + user **messages** follow the chat API pattern you saw when learning how LLMs are accessed remotely — Groq uses the same style as other hosted chat APIs.
- Rule **2** reduces guessing when retrieval misses — a honest *"I don't know from policy"* beats a fluent invention.
- **`generate_grounded_answer`** is the **generator** — it never searches; it only **writes** from supplied context.

**Common doubt:** *"What if the LLM ignores the excerpts?"* — It can happen. That is a **generation discipline** problem. Today you inspect answers side by side with retrieved text; a **later** session covers evaluation when the model adds extra "facts."

![Grounded prompt and generator — stitch retrieved excerpts with strict use-only-evidence rules, then call the chat API to produce a policy-backed ShopKart reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-07-grounded-generator.png)

### Simple Activity — Evidence Audit

After one grounded answer, copy the **retrieved excerpts** and the **final answer** into two columns. Underline every **number** and **eligibility rule** in the answer. Each underlined fact should appear verbatim or clearly paraphrased from an excerpt. Circle any line with no excerpt support.

---

## Step 5 — Wire the Full RAG Loop

One function ties **retriever + generator** into the pipeline you diagrammed earlier: **query → retrieve → context → generate**.

```python
def print_retrieved_chunks(user_query: str, retrieved_chunks: List[Dict[str, Any]]) -> None:
    # Debug helper — show what the retriever found before reading the LLM answer
    print("\n" + "=" * 72)  # Visual divider in terminal output
    print(f"Customer question: {user_query}")  # Echo the query
    print("=" * 72)  # Closing divider line

    for rank, chunk in enumerate(retrieved_chunks, start=1):  # Rank 1 = best match
        print(f"\nRank {rank}")  # Human-friendly rank label
        print(f"  Source   : {chunk['metadata'].get('source')}")  # Policy source tag
        print(f"  Category : {chunk['metadata'].get('category')}")  # Returns/shipping/etc.
        print(f"  Distance : {chunk['distance']:.4f}")  # Lower usually = closer vector match
        print(f"  Text     : {chunk['text']}")  # Actual policy excerpt retrieved


def answer_with_rag(
    client: Groq,
    collection,
    model: SentenceTransformer,
    user_query: str,
    top_k: int = 2,
) -> str:
    # Step A — Retrieve relevant ShopKart policy excerpts
    retrieved_chunks = retrieve_policy_chunks(
        collection=collection,  # Chroma collection holding policy rows
        model=model,  # Shared embedding model
        user_query=user_query,  # Customer's natural-language question
        top_k=top_k,  # How many excerpts to fetch
    )

    # Step B — Print retrieval results so you can judge intent match before generation
    print_retrieved_chunks(user_query, retrieved_chunks)  # Inspection step — not optional in learning

    # Step C — Generate grounded natural-language answer from retrieved evidence
    grounded_answer = generate_grounded_answer(
        client=client,  # Groq client
        user_query=user_query,  # Original question
        retrieved_chunks=retrieved_chunks,  # Evidence from retriever
    )

    return grounded_answer  # Final reply to show the customer
```

**How the code works:**

- **`answer_with_rag`** is the **minimal RAG loop** — the function you would call from a chat UI in a real app.
- **`print_retrieved_chunks`** makes retrieval **visible** — you judge whether search matched **intent** before trusting the answer.
- Order matters: **retrieve first**, **generate second** — swapping them would break grounding.

![answer_with_rag minimal loop — retrieve top-k chunks, print ranks for inspection, then generate the grounded answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-09-answer-with-rag-loop.png)

---

## Step 6 — Complete Script and Demo Queries

Add a **`main`** block that indexes policies and runs the full RAG loop on representative ShopKart questions.

```python
def main():
    # Create Groq client — reads GROQ_API_KEY from .env via load_dotenv()
    client = Groq()  # Generator API handle

    # Load embedding model and connect to Chroma collection
    model = create_embedding_model()  # SentenceTransformer (BGE) for retriever
    collection = setup_chroma_collection()  # Persistent Chroma collection

    # Index (or refresh) ShopKart policy knowledge sources
    index_policy_records(collection, model)  # Offline ingestion step

    # Representative customer questions spanning returns, shipping, warranty, refunds
    demo_queries = [
        "I received my phone case yesterday unopened. How many days do I have to return it?",
        "Will express shipping reach my address in a metro city by tomorrow?",
        "My wireless earphones stopped working after 10 months. Is repair covered?",
        "I returned a defective kettle on COD last week. When will the refund reach my UPI?",
    ]

    # Run each demo query through the full RAG loop
    for user_query in demo_queries:
        print("\n\n" + "#" * 72)  # Section header per question
        print("QUESTION:", user_query)  # Show current test question

        print("\n--- RAG (retrieve + generate) ---")  # Grounded pipeline label
        rag_answer = answer_with_rag(
            client=client,  # Groq generator client
            collection=collection,  # Retriever storage
            model=model,  # BGE embedding model
            user_query=user_query,  # Customer question
            top_k=2,  # Fetch two nearest policy chunks
        )
        print("\nFinal grounded answer:")  # Label final output
        print(rag_answer)  # Print grounded answer


# Standard Python entry — run main only when executing this file directly
if __name__ == "__main__":
    main()  # Start the ShopKart RAG demo
```

**How the code works:**

- **`demo_queries`** cover all four **knowledge source** areas — returns window, express shipping, warranty term, COD refund timing.
- For each question, you print **retrieval inspection** first, then the **RAG answer** — easy reading in the terminal.
- **`top_k=2`** may return both **returns** and **refunds** for return/refund wording — that is acceptable for a minimal demo; the instructor also discussed trying **top_k=3** or **top_k=5**; advanced tuning waits for a **later** session.

### How to Run

```bash
cd shopcart_rag  # Same folder where chroma_store and .env will live
python rag.py  # Execute the full demo — GROQ_API_KEY loads from .env
```

**Expected flow in the terminal:**

1. **`Indexed 4 ShopKart policy records.`**
2. For each demo question — **Rank 1 / Rank 2** retrieved excerpts with **category**, **distance**, and policy **text**.
3. A **final grounded answer** citing ShopKart's **7-day**, **3–5 day**, **12-month**, or **5–7 business day** rules where relevant.

### Simple Activity — Retrieval and Answer Scorecard

For each of the four demo queries, fill a table with columns: **Question**, **Rank 1 policy area**, **Key claim in grounded answer**, **Matches ShopKart policy?**. Write one sentence explaining how retrieved context shaped the answer on at least two rows.

---

## Validate Semantic Retrieval and Grounded Generation

A working pipeline needs two separate checks — **did we fetch the right policy?** and **did the answer follow that policy?**

### Checklist — Retrieval Intent Match

| Question | Did top rank hit the expected policy area? | Notes |
|---|---|---|
| Unopened return window | **Returns** | Customer rarely says "7 calendar days" verbatim |
| Express metro delivery | **Shipping** | "Tomorrow" may be unrealistic even with express rules |
| 10-month electronics repair | **Warranty** | Watch for liquid/damage exclusions in answer |
| COD refund to UPI | **Refunds** | May also surface **Returns** — both can be useful context |

- **Official Definition:** **Semantic retrieval** finds passages whose **meaning** is similar to the query, even when exact keywords differ.
- **In Simple Words:** Search by **intent**, not by copy-pasting policy words.
- **Real-Life Example:** Searching *"paise wapas kab aayenge"* should still find **refund timeline** text even if the policy never uses that Hindi phrase.

**Integrated learning point:** If retrieval fails, generation may still look polished. Always read **Rank 1 text** before trusting the final reply — the retriever is the first gate.

### Cosine Similarity — How Chroma Finds Nearest Chunks

Chroma's built-in similarity search uses **cosine similarity** to compare the query vector with stored policy vectors.

- **Official Definition:** **Cosine similarity** measures how close two vectors point in the same direction, regardless of their length.
- **In Simple Words:** It checks whether two meaning-fingerprints **face the same way** — higher similarity means closer meaning match.
- **Real-Life Example:** Two compass needles pointing north-east are "similar" even if one arrow is longer — direction matters more than size.

**Common doubt:** *"Can I change the distance function?"* — Yes, in advanced setups you can override Chroma's default. A **later** session covers retrieval tuning in more depth; today you inspect the **distance** values Chroma prints and judge intent match.

### Checklist — Generation Follows Evidence

When auditing a RAG answer, ask:

- Does every **number** in the reply appear in a retrieved excerpt?
- Does the reply respect **eligibility** language (unopened, metro-only, liquid damage excluded)?
- If excerpts were empty or wrong, did the model admit insufficient policy information?

### Example — One Refund Question

**Customer question:** *"I returned a defective kettle on COD last week. When will the refund reach my UPI?"*

| Check | What to look for |
|---|---|
| **Rank 1 policy area** | **Refunds** (may also surface **Returns**) |
| **Grounded answer claim** | *"5–7 business days after warehouse verification; COD to original UPI/bank"* |
| **Uses ShopKart policy numbers?** | Yes — if retrieval surfaced **refunds** chunk |
| **Traceable to excerpt?** | Yes — compare printed Rank 1 **text** |

### Simple Activity — Two-Stage Debug

Pick one demo query where the RAG answer felt wrong. Split the bug:

1. **Retrieval stage** — Was the wrong policy area Rank 1? Write the distance and category.
2. **Generation stage** — If retrieval looked correct, did the LLM add facts not in the excerpt?

One sentence: *"The main failure was in ___ stage because ___."*

---

## End-to-End Flow — Full Picture

```mermaid
flowchart TB
    A[Customer asks in natural language] --> B[Embed question with SentenceTransformer]
    B --> C[Chroma top-k query on shopkart_policy_kb]
    C --> D[Retrieved policy excerpts + metadata]
    D --> E[Build grounded prompt with rules]
    E --> F[LLM generates answer]
    F --> G[Grounded reply to customer]
    H[Knowledge sources indexed offline] --> C
```

Step-by-step in one breath:

1. **Offline** — Policy paragraphs live in **`POLICY_RECORDS`** and are embedded into **Chroma**.
2. **Online** — Customer question arrives.
3. **Retrieve** — Embed question → **`collection.query`** → top-k excerpts.
4. **Ground** — Excerpts pasted into prompt with **use-only-this-evidence** rules.
5. **Generate** — LLM writes the final support reply.
6. **Inspect** — You compare retrieval ranks and the grounded answer against ShopKart policy text.

![End-to-end RAG pipeline — offline policy indexing into Chroma, then per-question embed, top-k retrieve, grounded prompt, and LLM reply; validate both retrieval intent and evidence-following generation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session20/session20-10-end-to-end-pipeline.png)

**Common doubt:** *"Should I always trust Rank 1?"* — Rank 1 means **closest vector**, not guaranteed **business-correct** in every edge case. Human review of retrieval output remains part of responsible RAG design.

---

## Further Exploration — Real-Life RAG Projects

The minimal `rag.py` lab uses four short policy chunks. Production RAG systems often ingest **raw HTML or PDFs**, clean and chunk large documents, and serve thousands of queries.

- **Official Definition:** A **customized RAG application** combines domain-specific ingestion, retrieval tuning, and generation prompts for one business use case.
- **In Simple Words:** The same **search-then-write** pattern you built today — scaled up for a real company's documents.
- **Real-Life Example:** A legal firm indexing contract clauses so junior staff can ask *"What is the notice period?"* and get answers tied to the signed agreement text.

Your instructor shared links to larger **customized RAG demos** as extended learning references. Explore them after you can run today's script end to end — they show how ingestion, retrieval, and generation grow beyond a four-row policy table.

---

## Key Takeaways

- **Customer support** is a natural RAG use case: users need **organization-specific**, **current**, **verifiable** answers from **returns, shipping, warranty, and refund** policies — not generic LLM memory.
- A **minimal RAG pipeline** has three roles: **ingestion** (embed and store policy chunks in Chroma), **retrieval** (BGE embedding + top-k search), and **generation** (Groq Llama model that writes from retrieved context).
- Your **previous Chroma lab** becomes the retriever layer; today's new work is **`.env`-secured Groq integration**, **prompt grounding**, and **generation** wired after **`collection.query`**.
- **BGE embeddings** turn policy text into **384-dimensional** vectors; Chroma uses **cosine similarity** internally to find nearest matches — inspect **distance** and **category** before trusting the final answer.
- **Inspect retrieval before trusting answers** — semantic search can miss or mis-rank; generation can ignore good excerpts. A **later** session scales this pipeline to real policy files and deeper retrieval tuning.

---

## Important Commands, Libraries, and Terminologies used

| Term / Command | Meaning in one line |
|---|---|
| **RAG (Retrieval-Augmented Generation)** | Retrieve trusted chunks first, then generate an answer conditioned on that context |
| **Ingestion** | Offline step: prepare policy text, embed it, and load vectors into Chroma |
| **Knowledge source** | Trusted policy or document text the system may search (ShopKart returns/shipping/warranty/refunds) |
| **Knowledge boundary** | Topics and sources the assistant is allowed to use when answering |
| **Retriever** | Component that embeds the query and returns top-k relevant chunks from Chroma |
| **Generator** | LLM that turns retrieved excerpts + question into a natural-language reply |
| **Grounded prompt** | User message that includes policy excerpts and strict use-the-evidence rules |
| **Semantic retrieval** | Search by meaning similarity, not exact keyword match |
| **Cosine similarity** | Chroma's default way to compare query and stored vectors by direction |
| **Top-k (`n_results`)** | Number of nearest chunks the retriever returns per query |
| **Context / evidence block** | Retrieved policy text injected into the prompt before generation |
| **BGE embedding model** | Beijing General Embedding model that converts text into meaning vectors |
| **384 dimensions** | Number of numeric values in each BGE small embedding vector |
| **Chroma `PersistentClient`** | Local on-disk vector store — survives between script runs |
| **`shopkart_policy_kb`** | Collection name holding ShopKart policy rows in today's lab |
| **`embedding_function=None`** | You supply embeddings manually with Sentence Transformers |
| **`BAAI/bge-small-en-v1.5`** | BGE model used for indexing and query embeddings in this lab |
| **`collection.upsert(...)`** | Insert or update policy rows with ids, documents, metadata, embeddings |
| **`collection.query(...)`** | Top-k similarity search used inside the retriever |
| **`build_grounded_prompt`** | Assembles excerpts + rules + customer question for the LLM |
| **`answer_with_rag`** | Full minimal loop: retrieve → inspect → generate |
| **`groq.Groq()`** | Client for Groq-hosted Llama generation API calls |
| **`chat.completions.create`** | Chat API pattern for sending system + user messages to the generator |
| **`llama-3.1-8b-instant`** | Example Llama model name on Groq used in the lab script |
| **`GROQ_API_KEY`** | Secret token stored in `.env` for Groq API access |
| **`.env` / `python-dotenv`** | Safe local file + loader for API secrets — never commit to Git |
| **`print_retrieved_chunks`** | Debug helper to verify retrieval intent before reading the final answer |
