# Subjective Assignment: Build a ShopKart Policy RAG Assistant

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

ShopKart's support lead wants a small proof-of-concept assistant that answers customer questions **only** from official policy text. Your script must index four policy chunks in Chroma, retrieve the most relevant excerpts for each question, and generate grounded replies through Groq.

The support lead will review three specific customer tickets during the demo. Your program must show what was retrieved **before** each final answer so the team can judge retrieval intent.

## Task

Create a Python file named `shopkart_support_rag.py` that implements a minimal RAG workflow for ShopKart customer support.

### Functional Requirements

1. Import:
   - `chromadb`
   - `SentenceTransformer` from `sentence_transformers`
   - `Groq` from `groq`
   - `load_dotenv` from `dotenv`
   - `List`, `Dict`, `Any` from `typing`
2. Call `load_dotenv()` before creating the Groq client.
3. Store exactly four ShopKart policy records with these areas:
   - returns
   - shipping
   - warranty
   - refunds
4. Use this embedding model for both indexing and querying:
   - `BAAI/bge-small-en-v1.5`
5. Create a persistent Chroma client at:
   - `./chroma_store`
6. Create or open a collection named:
   - `shopkart_policy_kb`
   - with `embedding_function=None`
7. Implement these functions:
   - `create_embedding_model()`
   - `setup_chroma_collection()`
   - `index_policy_records(collection, model)`
   - `retrieve_policy_chunks(collection, model, user_query, top_k=2)`
   - `build_grounded_prompt(user_query, retrieved_chunks)`
   - `generate_grounded_answer(client, user_query, retrieved_chunks)`
   - `print_retrieved_chunks(user_query, retrieved_chunks)`
   - `answer_with_rag(client, collection, model, user_query, top_k=2)`
8. The grounded prompt must include rules that:
   - tell the model to answer using only the provided policy excerpts
   - forbid inventing numbers or eligibility rules not in the excerpts
   - ask for an honest insufficient-information reply when excerpts are not enough
9. Use this Groq generation model:
   - `llama-3.1-8b-instant`
10. In `main()`:
    - create the Groq client
    - load the embedding model
    - connect to Chroma
    - index the four policy records
    - run the full RAG loop on these three customer questions:
      - `"I opened the Bluetooth speaker and don't like the sound. Can I return it within two weeks?"`
      - `"How fast is express delivery to a metro city?"`
      - `"I returned a defective COD order last week. When will the refund reach my UPI?"`
11. For each question, print:
    - the question
    - Rank 1 and Rank 2 retrieved chunks with `category`, `distance`, and `text`
    - the final grounded answer
12. Add short comments explaining:
    - why the same embedding model is used for indexing and querying
    - why retrieval must happen before generation

### Expected Run Commands

```bash
pip install chromadb
pip install -U sentence-transformers
pip install groq
pip install python-dotenv
python shopkart_support_rag.py
```

Create a `.env` file in the same folder with:

```bash
GROQ_API_KEY=your-key-here
```

If your system uses `pip3` and `python3`, use those commands instead.

### Expected Behaviour

- The script should print that 4 policy records were indexed.
- For the opened-speaker return question, retrieval should surface **returns** near the top and the grounded answer should reflect that opened items are generally not eligible unless defective.
- For the express metro delivery question, retrieval should surface **shipping** near the top.
- For the COD refund question, retrieval should surface **refunds** and/or **returns** near the top, and the grounded answer should mention the **5–7 business day** refund window and COD refund path where supported by retrieved text.
- Every final answer should be preceded by printed retrieval output.

### Constraints

- Write the solution in one Python file only.
- Do not paste the API key inside the Python file.
- Do not use an automatic Chroma embedding function.
- Do not manually edit files inside `./chroma_store`.
- Do not add metadata filtering; use basic top-k similarity search only.
- Keep the code readable and beginner-friendly.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor or answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

A strong solution separates the RAG pipeline into clear stages. First, it defines four trusted ShopKart policy records and indexes them with `BAAI/bge-small-en-v1.5`, storing ids, documents, metadata, and embeddings through `collection.upsert(...)`. Because `embedding_function=None`, the script must call `model.encode(...)` manually for both policy text and user queries.

Next, `retrieve_policy_chunks(...)` embeds each customer question with the same model and runs `collection.query(...)` with `n_results=2`. The helper `print_retrieved_chunks(...)` makes retrieval visible so a human can inspect category, distance, and excerpt text before reading the final answer.

Then `build_grounded_prompt(...)` stitches the retrieved excerpts into a context block with strict evidence-only rules. `generate_grounded_answer(...)` sends that prompt to Groq using `llama-3.1-8b-instant`. Finally, `answer_with_rag(...)` enforces the correct order: retrieve first, print inspection output, then generate.

For the opened-speaker question, the returns policy should rank highly and the answer should not promise a casual two-week return for an opened item. For the express metro question, the shipping policy should rank highly. For the COD refund question, refunds and possibly returns should appear near the top, and the answer should stay tied to retrieved wording about refund timing and UPI/bank refund path.

### Complete Expected Code

```python
from typing import List, Dict, Any
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

POLICY_RECORDS = [
    {
        "id": "shopkart_returns_1",
        "text": (
            "Unopened items may be returned within 7 calendar days of delivery. "
            "Opened or used items are not eligible unless defective."
        ),
        "metadata": {"category": "returns", "source": "returns_policy"},
    },
    {
        "id": "shopkart_shipping_1",
        "text": (
            "Standard delivery takes 3 to 5 business days after dispatch. "
            "Express delivery (paid) arrives in 1 to 2 business days in metro cities only."
        ),
        "metadata": {"category": "shipping", "source": "shipping_policy"},
    },
    {
        "id": "shopkart_warranty_1",
        "text": (
            "Electronics carry a 12-month manufacturer warranty from the date of delivery. "
            "Warranty does not cover physical damage or liquid exposure."
        ),
        "metadata": {"category": "warranty", "source": "warranty_policy"},
    },
    {
        "id": "shopkart_refunds_1",
        "text": (
            "Refunds are credited within 5 to 7 business days after the returned item "
            "passes warehouse verification. Cash-on-delivery orders are refunded to the "
            "original UPI or bank account only."
        ),
        "metadata": {"category": "refunds", "source": "refunds_policy"},
    },
]

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
GENERATION_MODEL_NAME = "llama-3.1-8b-instant"


def create_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def setup_chroma_collection():
    client = chromadb.PersistentClient(path="./chroma_store")
    collection = client.get_or_create_collection(
        name="shopkart_policy_kb",
        embedding_function=None,
    )
    return collection


def index_policy_records(collection, model: SentenceTransformer) -> None:
    ids = [row["id"] for row in POLICY_RECORDS]
    documents = [row["text"] for row in POLICY_RECORDS]
    metadatas = [row["metadata"] for row in POLICY_RECORDS]
    embeddings = model.encode(documents, convert_to_numpy=True).tolist()

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings,
    )

    print(f"Indexed {collection.count()} ShopKart policy records.")


def retrieve_policy_chunks(
    collection,
    model: SentenceTransformer,
    user_query: str,
    top_k: int = 2,
) -> List[Dict[str, Any]]:
    query_embedding = model.encode([user_query], convert_to_numpy=True).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    retrieved = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        retrieved.append(
            {
                "text": doc,
                "metadata": meta,
                "distance": dist,
            }
        )

    return retrieved


def build_grounded_prompt(user_query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    context_block = ""
    for index, chunk in enumerate(retrieved_chunks, start=1):
        source_name = chunk["metadata"].get("source", "unknown")
        context_block += f"\nExcerpt {index} (source: {source_name}):\n{chunk['text']}\n"

    prompt = f"""You are ShopKart customer support.
Answer the customer's question using ONLY the policy excerpts below.
Rules:
1. Do not invent numbers, timelines, or eligibility rules not present in the excerpts.
2. If the excerpts do not contain enough information, say:
   "I do not have enough information in the provided policy excerpts."
3. Keep the answer short, polite, and clear.
4. Mention important conditions when they appear in the excerpts.

Policy excerpts:
{context_block}

Customer question:
{user_query}

Final answer:"""

    return prompt


def generate_grounded_answer(
    client: Groq,
    user_query: str,
    retrieved_chunks: List[Dict[str, Any]],
) -> str:
    prompt = build_grounded_prompt(user_query, retrieved_chunks)

    response = client.chat.completions.create(
        model=GENERATION_MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a precise ShopKart support assistant. Follow the policy excerpts exactly.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()


def print_retrieved_chunks(user_query: str, retrieved_chunks: List[Dict[str, Any]]) -> None:
    print("\n" + "=" * 72)
    print(f"Customer question: {user_query}")
    print("=" * 72)

    for rank, chunk in enumerate(retrieved_chunks, start=1):
        print(f"\nRank {rank}")
        print(f"  Source   : {chunk['metadata'].get('source')}")
        print(f"  Category : {chunk['metadata'].get('category')}")
        print(f"  Distance : {chunk['distance']:.4f}")
        print(f"  Text     : {chunk['text']}")


def answer_with_rag(
    client: Groq,
    collection,
    model: SentenceTransformer,
    user_query: str,
    top_k: int = 2,
) -> str:
    retrieved_chunks = retrieve_policy_chunks(
        collection=collection,
        model=model,
        user_query=user_query,
        top_k=top_k,
    )

    print_retrieved_chunks(user_query, retrieved_chunks)

    return generate_grounded_answer(
        client=client,
        user_query=user_query,
        retrieved_chunks=retrieved_chunks,
    )


def main():
    client = Groq()
    model = create_embedding_model()
    collection = setup_chroma_collection()

    index_policy_records(collection, model)

    demo_queries = [
        "I opened the Bluetooth speaker and don't like the sound. Can I return it within two weeks?",
        "How fast is express delivery to a metro city?",
        "I returned a defective COD order last week. When will the refund reach my UPI?",
    ]

    for user_query in demo_queries:
        print("\n\n" + "#" * 72)
        print("QUESTION:", user_query)
        print("\n--- RAG (retrieve + generate) ---")

        grounded_answer = answer_with_rag(
            client=client,
            collection=collection,
            model=model,
            user_query=user_query,
            top_k=2,
        )

        print("\nFinal grounded answer:")
        print(grounded_answer)


if __name__ == "__main__":
    main()
```

### Alternative Approaches

- The file may be named `rag.py` instead of `shopkart_support_rag.py` if the learner already uses that name locally, as long as all required functions and behaviour are present.
- Learners may use `pip3` and `python3` depending on their local Python setup.
- The exact wording of grounded answers may vary slightly with the LLM, but every number and eligibility rule in the answer should still be traceable to retrieved excerpts.
