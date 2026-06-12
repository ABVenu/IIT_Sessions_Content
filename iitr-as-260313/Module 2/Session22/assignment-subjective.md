# Subjective Assignment: ShopKart RAG — Quick Evaluation Fix

## Practical Task

**Difficulty:** Medium (simplified)  
**Type:** Coding implementation

---

## Scenario

ShopKart’s QA team flagged one recurring bad answer: customers asking about **prepaid UPI refunds** get a confident reply even though policy files only describe **COD → UPI/bank** refunds.

You already have a **working file-based ShopKart RAG script** (policy folder, Chroma index, Groq answers). Your job is to add a small **improvement layer** and prove the fix on **two test queries**.

---

## Setup

Use your existing project folder:

```text
shopkart_rag_lab/
├── policy_documents/     # four policy .txt files
├── .env                  # GROQ_API_KEY=your-key-here
└── rag_pipeline.py       # your working script from the prior build
```

No need to rebuild the project from scratch. If `rag_pipeline.py` already loads policies and answers questions, **keep that code** and add only what is listed below.

---

## Task

Add the following to **`rag_pipeline.py`**.

### 1. Test queries (exactly two)

```python
TEST_QUERIES = [
    "Is UPI refund available for prepaid orders?",
    "I returned a defective kettle on COD last week. When will the refund reach my UPI?",
]
```

### 2. Copy these two functions into your file

```python
def guess_category(query):
    q = query.lower()
    if "return" in q or "opened" in q or "unopened" in q:
        return "returns"
    if "ship" in q or "express" in q or "metro" in q or "dispatch" in q or "deliver" in q:
        return "shipping"
    if "warranty" in q or "water" in q or "repair" in q or "liquid" in q:
        return "warranty"
    if "refund" in q or "cod" in q or "upi" in q or "money back" in q:
        return "refunds"
    return None


def retrieve_filtered(collection, model, user_query, top_k=3, category=None):
    embedding = model.encode([user_query], convert_to_numpy=True).tolist()
    args = {
        "query_embeddings": embedding,
        "n_results": top_k,
        "include": ["documents", "metadatas", "distances"],
    }
    if category:
        args["where"] = {"category": category}
    results = collection.query(**args)
    chunks = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        chunks.append({"text": doc, "metadata": meta, "distance": dist})
    return chunks
```

### 3. Write `generate_strict_answer` yourself

Create **`build_strict_prompt`** and **`generate_strict_answer`** that:

- use only retrieved excerpts  
- forbid inventing payment methods or policy rules  
- use this **exact refusal line** when evidence is missing:

  `"I do not have enough information in the provided policy excerpts."`

You may follow the same Groq call pattern as your existing `generate_grounded_answer`.

### 4. Add a simple runner in `main()`

After `build_knowledge_base(...)`, loop over `TEST_QUERIES` and for **each** query:

1. Call `guess_category(user_query)` and `retrieve_filtered(..., top_k=5, category=...)`
2. Print **Rank 1** category and a short snippet of Rank 1 text (reuse your existing print helper if you have one)
3. Call `generate_strict_answer(...)` and print the answer

Label the section in the terminal: `--- IMPROVED RUN ---`

---

## Expected behaviour

- Script runs without errors.
- Both test queries print retrieval output **before** the answer.
- Improved settings used: **`top_k=5`**, **category filter on**, **strict prompt**.
- For the **prepaid UPI** query, the answer should **refuse** or stay grounded — no invented prepaid UPI workflow.

---

## Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file (`rag_pipeline.py`).
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation (Reference Approach)

### Step-by-step solution walkthrough

1. Keep your existing ingestion and `build_knowledge_base` — do not rewrite loaders or chunking.
2. Paste `guess_category` and `retrieve_filtered` as given.
3. Add `build_strict_prompt` / `generate_strict_answer` with the fixed refusal sentence and **do not invent** rules.
4. In `main()`, run the improved loop on the two `TEST_QUERIES` only.
5. Read Rank 1 in the terminal to confirm **refunds** category for both queries before judging the answer.

### Reference — functions you write + improved `main()` loop

```python
REFUSAL = "I do not have enough information in the provided policy excerpts."

TEST_QUERIES = [
    "Is UPI refund available for prepaid orders?",
    "I returned a defective kettle on COD last week. When will the refund reach my UPI?",
]


def build_strict_prompt(user_query, retrieved_chunks):
    context = ""
    for i, chunk in enumerate(retrieved_chunks, start=1):
        src = chunk["metadata"].get("source", "unknown")
        cat = chunk["metadata"].get("category", "unknown")
        context += f"\nExcerpt {i} (source: {src}, category: {cat}):\n{chunk['text']}\n"
    return f"""You are ShopKart customer support.
Use ONLY the excerpts below.
Rules:
1. Do not invent numbers, payment methods, or rules not in the excerpts.
2. If the excerpts do not contain enough information, say exactly: "{REFUSAL}"
3. Keep the answer short and faithful to the excerpts.

Excerpts:
{context}

Question: {user_query}

Answer:"""


def generate_strict_answer(client, user_query, retrieved_chunks):
    prompt = build_strict_prompt(user_query, retrieved_chunks)
    response = client.chat.completions.create(
        model=GENERATION_MODEL_NAME,
        messages=[
            {"role": "system", "content": "Follow excerpts exactly. Never guess missing policy details."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()


# Inside main(), after build_knowledge_base:
print("\n--- IMPROVED RUN ---")
for user_query in TEST_QUERIES:
    category = guess_category(user_query)
    chunks = retrieve_filtered(collection, model, user_query, top_k=5, category=category)
    print_retrieved_chunks(user_query, chunks)  # your existing helper
    answer = generate_strict_answer(client, user_query, chunks)
    print("\nAnswer:", answer)
    print("-" * 72)
```

### Alternative approaches

- A single `run_queries(...)` helper is fine if it prints retrieval before answers.
- Baseline vs improved comparison is **not required** for this assignment — only the improved pass on two queries.
- LLM wording may vary slightly; graders check settings (`top_k=5`, filter, strict prompt) and grounded/refusal behaviour on prepaid UPI.

### Notes for evaluation

- Full credit: pasted router + filtered retriever, student-written strict answer with exact refusal, improved loop on both queries, Rank 1 printed before answer.
- Partial credit: missing category filter or strict prompt, or only one query implemented.
- Students may submit a full standalone file if they do not have the prior build — structure and behaviour matter more than file length.
