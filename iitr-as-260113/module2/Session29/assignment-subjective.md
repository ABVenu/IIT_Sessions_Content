# Subjective Assignment — RAG Architecture and Pipeline

**Total Questions:** 1 | **Type:** Practical Coding Implementation | **Difficulty:** Medium

---

## Question 1 — Build a RAG-Powered HR Policy Assistant

### Background

Priya is the HR Manager at **InnoTech Solutions**, a 200-person startup. The company has written detailed internal HR policies, but employees constantly send Priya emails asking questions that are already answered in those documents. Priya spends hours every week answering the same repetitive questions.

She decides to build an **HR Policy Assistant** — a RAG-powered chatbot that lets employees type a question and instantly receive a policy-grounded answer. Rather than guessing or relying on generic AI responses, the assistant will retrieve the actual company policy and use it to generate the reply.

Your task is to build this assistant from scratch using Python, ChromaDB, and any LLM API of your choice — applying everything you learned about the RAG pipeline in this session.

---

### What You Must Build

Create a Python script called `hr_policy_rag.py` inside a project folder `hr-policy-rag`.

#### Step 1 — Define Your HR Policy Documents

Create **at least 4 HR policy documents** as Python dictionaries (similar to `POLICY_DOCUMENTS` in the session). Each document must have:
- A unique `id`
- A `text` field with 3–5 sentences of policy content
- A `metadata` field with `category` and `source` keys

Your 4 policies must cover these topics (write your own policy content — do not copy from the session):

| Policy | Example Topics to Cover |
| ------ | ----------------------- |
| **Leave Policy** | Annual leave days, sick leave rules, carry-forward rules |
| **Work From Home Policy** | WFH days per week, eligibility criteria, approval process |
| **Appraisal Policy** | Appraisal cycle timing, rating scale, increment linkage |
| **Code of Conduct** | Workplace behavior standards, data privacy rules, conflict of interest |

#### Step 2 — Build These Functions

Implement the following functions in your script:

| Function | What It Should Do |
| -------- | ----------------- |
| `create_embeddings(texts)` | Send text list to an embedding model of your choice and return embedding vectors |
| `setup_vector_database()` | Create a ChromaDB `PersistentClient` with a collection named `hr_policy_collection` using cosine similarity |
| `index_hr_documents(collection)` | Index your 4 HR policy documents into ChromaDB using `upsert` |
| `retrieve_hr_content(collection, query, top_k=3)` | Embed the query, search ChromaDB, and return top-K chunks with text, metadata, and distance |
| `build_grounded_prompt(query, chunks)` | Assemble a prompt that injects retrieved chunks as context and instructs the LLM to answer only from that context |
| `generate_answer(query, chunks)` | Call your chosen LLM with the grounded prompt and return the response text |
| `answer_with_rag(collection, query, top_k=3)` | The complete pipeline: retrieve → print chunks → generate answer |

#### Step 3 — Test With Employee Queries

Test your assistant with **at least 3 different employee queries**, one per policy area. Print the retrieved chunks and the final answer for each. Examples (you may write different ones):

- *"How many days of annual leave am I entitled to per year?"*
- *"Do I need manager approval before working from home?"*
- *"When is the appraisal cycle conducted and how is the increment decided?"*

#### Step 4 — Side-by-Side Comparison

For **one query of your choice**, print:
1. The answer generated **without RAG** (LLM answering from memory only, using a `generate_answer_without_retrieval(query)` function).
2. The answer generated **with RAG** (using your complete pipeline).

Label both outputs clearly in the terminal so the difference is visible.

---

### Constraints & Guidance

- Write your own HR policy text — do not copy the e-commerce policies from the session. The content must reflect a realistic HR context.
- You may use **any LLM API** for embeddings and generation — OpenAI, Google Gemini, or any other provider. **Gemini API has a free tier** and is a good option if you do not have OpenAI credits.
- Use `PersistentClient` so your ChromaDB data survives between runs.
- Use `upsert` (not `add`) when indexing documents.
- Your grounded prompt must include a fallback instruction: if the policy context does not answer the question, the LLM should say so instead of guessing.
- Store your API key as an environment variable — never hardcode it in the script. (e.g. `OPENAI_API_KEY` for OpenAI, `GEMINI_API_KEY` for Gemini, etc.)

---

### Submission Instructions

- Create a repo called `agentic-systems` in your GitHub account (if already created, use the same one) — clone it locally (skip if already cloned).
- Inside the repo, create a folder called `module2` (skip if it already exists).
- Inside `module2`, create a folder called `Session29`.
- Inside `Session29`, create your `hr-policy-rag` project folder containing:
  - `hr_policy_rag.py` — your complete implementation
  - `requirements.txt` — listing `chromadb` and the SDK for your chosen LLM provider (e.g. `openai`, `google-generativeai`, etc.)
  - `.gitignore` — ignoring `venv/`, `chroma_hr_policy_db/`, and `.env`
  - A brief `README.md` — 3–5 lines describing what the project does and how to run it
- Add, commit, and push all files to GitHub.
- Submit the GitHub link to the `Session29` folder (not the root repo link) as your submission.

---

### Answer Explanation (Model Solution)

**Approach Overview:**
The solution follows the same five-component RAG pattern taught in the session: Knowledge Sources → Embeddings → Vector Database → Retriever → Generator.

**Key implementation decisions:**
1. **Policy design:** Each policy document covers one specific HR area, keeping chunks focused so retrieval is precise.
2. **`upsert` over `add`:** Prevents duplicate-ID errors if the script is re-run after the ChromaDB folder already exists.
3. **Grounded prompt design:** The prompt must include the rule *"Answer only from the policy context below. If the answer is not in the context, say you do not have enough information."* — this prevents hallucination.
4. **Side-by-side comparison:** Calling the LLM without any retrieved context (just the raw employee question) produces a generic, company-unaware answer. With RAG, the answer reflects the exact policies written by the student — demonstrating the core value of grounding.
5. **`top_k=3`:** This balanced default ensures enough context for multi-aspect queries without adding noisy, irrelevant chunks.

**Example model output for query `"How many days of annual leave am I entitled to per year?"`:**

```
WITHOUT RAG:
Most companies provide between 12 to 24 days of paid annual leave per year, depending on company policy and local labor laws. Please check your HR handbook for specifics.

WITH RAG:
================================================================================
Customer Query: How many days of annual leave am I entitled to per year?
================================================================================
Result 1 | Source: leave_policy | Category: leave | Distance: 0.0812
...

Final RAG Answer:
As per InnoTech Solutions' Leave Policy, all full-time employees are entitled to 18 days of paid annual leave per calendar year. Unused leaves up to 5 days may be carried forward to the next year. Leaves beyond this limit will lapse.
```

**Alternative approaches:**
- Students may use any LLM provider — OpenAI (`gpt-4o-mini`, `gpt-4o`), Google Gemini (`gemini-1.5-flash`, `gemini-2.0-flash` — free tier available), or any other API. The RAG pipeline logic remains identical regardless of provider.
- Students may add metadata filtering (e.g., `where={"category": "leave"}`) to make retrieval more precise.
- More policy documents (5+) are acceptable and encouraged.
