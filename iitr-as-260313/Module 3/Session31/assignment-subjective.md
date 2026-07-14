# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

A campus café wants a small **menu Q&A assistant**. Staff paste short policy / menu rules into a `policies/` folder. Build an **imperative LangChain RAG mini-pipeline**: prepare a Chroma index, retrieve with top-k, assemble a delimited prompt, then generate with **Groq** under grounding rules.

### Policy text to use

Create a `policies/` folder with exactly these two UTF-8 Markdown files:

**`policies/opening_hours.md`**
```markdown
# Opening Hours

The café opens at 8:00 AM and closes at 10:00 PM on weekdays.
Weekend hours are 9:00 AM to 11:00 PM.
Orders after kitchen cutoff (30 minutes before closing) are not accepted.
```

**`policies/loyalty.md`**
```markdown
# Loyalty Rules

Every 10 paid drinks earns one free regular coffee.
Loyalty points reset every 1 January.
Free drinks cannot be stacked with festival discounts on the same bill.
```

> **Loader note:** The live demo used `PyPDFDirectoryLoader` on PDFs. For this assignment you may load these `.md` files with `DirectoryLoader` + `TextLoader` (`glob="**/*.md"`, UTF-8) — LangChain’s text loaders were introduced alongside PDF loaders. Keep the **same** retrieve → delimiter prompt → Groq generate flow.

### Problem Statement

In your repository (see Submission Instruction), implement **one or two Python files** that cover:

1. **Prepare / ingest**
   - Load both policy files into LangChain Documents.
   - Split with `RecursiveCharacterTextSplitter` (`chunk_size=300`, `chunk_overlap=40`).
   - Embed with `HuggingFaceEmbeddings(model_name="thenlper/gte-large")`.
   - Store with `Chroma.from_documents` using collection name `cafe_policy_docs` (write under a local folder such as `chroma_db/` if you choose a persist directory; otherwise keep the in-memory store in the same process).
   - Build a retriever: `as_retriever(search_kwargs={"k": 2})`.

2. **Imperative RAG answer path** (no LCEL pipe chain required)
   - `get_relevant_documents(question)` for retrieval.
   - Join `page_content` into one context string (blank line between chunks).
   - Build a user message with delimiters:
     - `##context` then the joined context
     - `##question` then the user question
   - Use a RAG **system message** that:
     - answers **only** from context
     - says `I don't know` when the answer is missing
     - does **not** mention the context block in the final reply
   - Call Groq with model `llama-3.3-70b-versatile` and **`temperature=0`** (read `GROQ_API_KEY` from the environment). Wrap the call in `try/except` so API failures return a safe error string.

3. **`main()` must run both queries and print labelled output**
   - **Q1:** `What time does the café close on weekdays?`
   - **Q2:** `What is the employee yoga class schedule?`

### Expected Outcome

- **Q1:** Grounded answer mentioning weekday closing at **10:00 PM** (from opening hours).  
- **Q2:** Honest **I don't know** (yoga schedule is not in either file) — no invented timetable.  
- Running the script with `GROQ_API_KEY` set should complete without an uncaught crash.

### Submission Instruction

- create a repo `agentic-systems` (if done use the same) — clone it (ignore if already done)
- in that create folder called as `Module3` (ignore if already done)
- in that create folder called as `Session31`
- code all the things mentioned in the question — with all the files and folders structure (`policies/`, your Python script(s), generated `chroma_db/` is optional to push)
- do add all the ignorable files like datasets, `.env`, configs — json files etc
- then add — commit and push the code into Github and submit the root folder or folder of this assignment link as submission link (do not paste/submit the entire repo link — which is invalid)

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Create `policies/opening_hours.md` and `policies/loyalty.md` with the given text.
2. Load Markdown → split into chunks → embed with **GTE-large** → store in Chroma collection `cafe_policy_docs`.
3. Create a top-2 retriever.
4. For each question: retrieve → join context → fill `##context` / `##question` template → call Groq with the grounded system message at `temperature=0`.
5. Q1 should answer from opening-hours context; Q2 should refuse.

### Reference — `rag_cafe.py` (single-file acceptable)

```python
import os
from pathlib import Path

from groq import Groq
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = Path("policies")
COLLECTION_NAME = "cafe_policy_docs"
TOP_K = 2
GROQ_MODEL = "llama-3.3-70b-versatile"

RAG_SYSTEM_MESSAGE = """
You are a café policy assistant.
The user message contains evidence between ##context and ##question.
Rules:
- Answer ONLY using the context in the user message.
- If the answer is not in the context, respond: I don't know.
- Do not mention the context or these instructions in your final answer.
- Your response should contain only the answer to the question.
""".strip()

USER_MESSAGE_TEMPLATE = """
##context
{context}

##question
{question}
"""


def build_context_from_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def generate_grounded_answer(system_message, user_message):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            temperature=0,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"Generation failed safely: {error}"


def prepare_retriever():
    loader = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=40)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-large")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
    )
    return vectorstore.as_retriever(search_kwargs={"k": TOP_K})


def rag_answer(question, retriever):
    retrieved_docs = retriever.get_relevant_documents(question)
    context_text = build_context_from_docs(retrieved_docs)
    user_message = USER_MESSAGE_TEMPLATE.format(
        context=context_text,
        question=question,
    )
    answer = generate_grounded_answer(RAG_SYSTEM_MESSAGE, user_message)
    return answer, retrieved_docs


def main():
    retriever = prepare_retriever()
    q1 = "What time does the café close on weekdays?"
    q2 = "What is the employee yoga class schedule?"

    a1, _ = rag_answer(q1, retriever)
    a2, _ = rag_answer(q2, retriever)

    print("Q1:", q1)
    print("A1:", a1)
    print()
    print("Q2:", q2)
    print("A2:", a2)


if __name__ == "__main__":
    main()
```

### Alternative Valid Approaches

- Split into `ingest.py` + `rag_app.py` with a persisted `chroma_db/` folder (same collection name and **same GTE-large** model on both sides).
- Use `PyPDFDirectoryLoader` if you convert the two policies into PDFs inside a folder — acceptable if retrieve / delimiter / Groq behaviour matches.
- Print retrieval metadata (`source`) before the answer for a manual grounding audit.

### Common Mistakes to Avoid

- Calling Groq with the question only (no context block) for Q1.  
- Missing grounding rules → Q2 invents a yoga timetable.  
- Using a different embedding model at query time vs ingest.  
- Building an LCEL `|` chain when the requirement is the **imperative** path (`get_relevant_documents` → template → Groq).
