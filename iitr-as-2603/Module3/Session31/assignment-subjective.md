# Subjective Assignment: Grounded Mini RAG Q&A

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

**FinSight Analytics** helps analysts query a small set of annual-report excerpts. The excerpts are already prepared as text snippets (no PDF loading required). Your job is to wire the **retrieve → augment → generate** path: build a tiny Chroma index, retrieve top-k chunks with LangChain, assemble a `##context` / `##question` user message, and answer with **Groq** at **`temperature=0`**.

You do **not** need Gradio or a full Tesla PDF for this task.

---

## Provided corpus

Use this corpus **exactly** in your script:

```python
CORPUS = [
    {
        "text": (
            "NovaTech Annual Report 2022 — Financial Highlights. "
            "Total revenue for fiscal year 2022 was 48.2 billion dollars, "
            "representing 19 percent year-over-year growth."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 12},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Operating Income. "
            "Operating income reached 6.1 billion dollars in 2022. "
            "Cloud services contributed the largest share of margin improvement."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 18},
    },
    {
        "text": (
            "NovaTech Annual Report 2023 — Outlook. "
            "Management expects continued investment in AI infrastructure through 2024. "
            "No weather or macro-forecast data is included in this document."
        ),
        "metadata": {"source_id": "novatech_2023.pdf", "page": 4},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Employee Count. "
            "NovaTech employed 124000 people worldwide at the end of 2022."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 31},
    },
]
```

---

## Task

Create a single Python file named `mini_grounded_rag.py`.

### Step 1 — Build a mini vector index

1. Convert each `CORPUS` record into a LangChain `Document` (`page_content` + `metadata`).  
2. Use `HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")` for this small corpus (keep the **same** model for indexing and querying).  
3. Build the store with `Chroma.from_documents(...)`.  
4. Print total documents stored.

### Step 2 — Configure retrieval

1. Create a retriever with `vectorstore.as_retriever(...)`.  
2. Use `search_kwargs={"k": 3}` (you may also pass `search_type="similarity"` if your LangChain version supports it).  
3. Retrieve with `retriever.get_relevant_documents(user_query)`.

### Step 3 — Prompt assembly

Implement:

- `SYSTEM_MESSAGE` that:
  - States the assistant answers from annual-report context only  
  - Explains `##context` and `##question` delimiter tokens  
  - Instructs the model to say **"I don't know"** if the answer is not in context  
- `build_user_message(user_query, retrieved_docs)` that joins `page_content` and returns:

```
##context
<joined chunk texts>

##question
<user query>
```

### Step 4 — Grounded generation

Implement `generate_grounded_answer(system_message, user_message)` using **Groq**:

- Model: `llama-3.3-70b-versatile` (or another Groq chat model you have access to)  
- `temperature=0`  
- Read `GROQ_API_KEY` from the environment

Implement `rag_answer(user_query, retriever)` that returns a dict with keys: `answer`, `retrieved_docs`, `user_message`.

### Step 5 — Run two test queries in `main()`

**Query A (in corpus):**

> What was NovaTech's total revenue in 2022?

**Query B (out of corpus):**

> What is the weather in Mumbai tomorrow?

For **each** query, print:

1. A short **retrieval trace** (chunk index + `metadata` + first 120 characters of chunk text)  
2. The **generated answer**

### Expected behaviour

- Query A should mention **48.2 billion dollars** (or clearly grounded equivalent wording from retrieved text).  
- Query B should **refuse** or say **I don't know** — not invent a weather forecast.  
- Both runs use the full `rag_answer` path (not a raw Groq call without retrieval).

---

## Submission Instructions

- Code all steps in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. Build `Document` objects from `CORPUS` and create a small Chroma index with the same embedding model used at query time.  
2. Configure a similarity retriever with `k=3` and call `get_relevant_documents`.  
3. Assemble system + user messages using `##context` / `##question` delimiters and grounding rules.  
4. Call Groq at `temperature=0` inside `rag_answer`.  
5. Print retrieval traces and answers for one in-corpus and one out-of-corpus query to demonstrate grounding and refusal.

### Complete Code

```python
import os
from groq import Groq
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CORPUS = [
    {
        "text": (
            "NovaTech Annual Report 2022 — Financial Highlights. "
            "Total revenue for fiscal year 2022 was 48.2 billion dollars, "
            "representing 19 percent year-over-year growth."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 12},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Operating Income. "
            "Operating income reached 6.1 billion dollars in 2022. "
            "Cloud services contributed the largest share of margin improvement."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 18},
    },
    {
        "text": (
            "NovaTech Annual Report 2023 — Outlook. "
            "Management expects continued investment in AI infrastructure through 2024. "
            "No weather or macro-forecast data is included in this document."
        ),
        "metadata": {"source_id": "novatech_2023.pdf", "page": 4},
    },
    {
        "text": (
            "NovaTech Annual Report 2022 — Employee Count. "
            "NovaTech employed 124000 people worldwide at the end of 2022."
        ),
        "metadata": {"source_id": "novatech_2022.pdf", "page": 31},
    },
]

EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3
GROQ_MODEL = "llama-3.3-70b-versatile"

SYSTEM_MESSAGE = """
You are an assistant that answers user queries on annual report excerpts.
User input will contain the context required to answer the question.
The context will begin with the token ##context.
The question will begin with the token ##question.
Answer ONLY using the provided context.
If the answer is not found in the context, say: I don't know.
""".strip()


def build_documents(corpus):
    return [
        Document(page_content=item["text"], metadata=item["metadata"])
        for item in corpus
    ]


def build_user_message(user_query, retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return f"##context\n{context_text}\n\n##question\n{user_query}"


def print_retrieval_trace(user_query, retrieved_docs):
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"Chunk {i} | metadata: {doc.metadata}")
        print(f"  preview: {doc.page_content[:120]}...")


def generate_grounded_answer(system_message, user_message):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def rag_answer(user_query, retriever):
    retrieved_docs = retriever.get_relevant_documents(user_query)
    user_message = build_user_message(user_query, retrieved_docs)
    answer = generate_grounded_answer(SYSTEM_MESSAGE, user_message)
    return {
        "answer": answer,
        "retrieved_docs": retrieved_docs,
        "user_message": user_message,
    }


def run_query(label, question, retriever):
    print(f"\n===== {label} =====")
    result = rag_answer(question, retriever)
    print_retrieval_trace(question, result["retrieved_docs"])
    print("\n--- Generated answer ---")
    print(result["answer"])


def main():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)
    documents = build_documents(CORPUS)

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
    )
    print("Documents stored:", len(documents))

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K},
    )

    run_query(
        "Query A — in corpus",
        "What was NovaTech's total revenue in 2022?",
        retriever,
    )
    run_query(
        "Query B — out of corpus",
        "What is the weather in Mumbai tomorrow?",
        retriever,
    )


if __name__ == "__main__":
    main()
```

### Alternative approaches

- Use `thenlper/gte-large` instead of MiniLM if you want to mirror the Tesla notebook encoder — keep the **same** model for index and query.  
- Add a printed two-column grounding table mapping claims to `source_id` / `page` for Query A.  
- Wrap the Groq call in `try/except` so bad API keys fail safely.

### Notes for evaluation

- Accept working code that uses the full RAG path and shows grounded revenue text for Query A.  
- Query B should refuse or say **I don't know**; minor wording differences are fine.  
- Do not require Gradio, Tesla PDFs, or automated inline citations in model output.
