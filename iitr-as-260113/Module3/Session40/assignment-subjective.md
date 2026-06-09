# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

A college hostel office wants a small **policy Q&A assistant**. They gave you two short rules (below). Build a **LangChain RAG mini-pipeline** that ingests these rules into **Chroma** and answers user questions with an **LCEL chain** and guardrail prompt.

### Policy text to use

Create a `documents/` folder with exactly these two files:

**`documents/quiet_hours.md`**
```markdown
# Quiet Hours Policy

Quiet hours are from 10:00 PM to 6:00 AM on all weekdays.
During quiet hours, loud music, group calls, and hallway gatherings are not allowed.
Violations may lead to a written warning.
```

**`documents/guest_policy.md`**
```markdown
# Guest Policy

Day guests are allowed only between 9:00 AM and 8:00 PM.
Overnight guests require prior warden approval at least 24 hours in advance.
Maximum two guests per room at any time.
```

### Problem Statement

In your repository (see Submission Instruction), implement:

1. **`ingest.py`**
   - Load both `.md` files using `DirectoryLoader` + `TextLoader` with `glob="**/*.md"` and UTF-8 encoding.
   - Split with `RecursiveCharacterTextSplitter` (`chunk_size=400`, `chunk_overlap=60`, `add_start_index=True`).
   - Embed with `OpenAIEmbeddings(model="text-embedding-3-small")`.
   - Persist to Chroma collection `hostel_policy_docs` under `chroma_db/` (delete old `chroma_db` with `shutil.rmtree` if it already exists before re-ingest).

2. **`rag_app.py`**
   - Reload the same Chroma collection and embedding model (no re-ingest in this file).
   - Build a retriever (`similarity`, `k=2`).
   - Build an LCEL RAG chain:
     - `context` = `retriever | format_docs` (join `page_content` with blank lines)
     - `question` = `RunnablePassthrough()`
     - prompt → `ChatOpenAI(model="gpt-4o-mini", temperature=0)` → `StrOutputParser()`
   - Prompt guardrails (include in your template):
     - Use only retrieved context
     - If missing, say: `I don't know based on the provided documents.`
     - Mention source file name when possible
   - In `main()`, run **both** queries and print labelled output:
     - **Q1:** `What are the quiet hours on weekdays?`
     - **Q2:** `What is the scholarship amount for hostel residents?`

### Expected Outcome

- **Q1:** Grounded answer mentioning quiet hours (10 PM–6 AM) and ideally citing `quiet_hours.md`.
- **Q2:** Honest refusal (scholarship is not in either policy file) — no invented amount.
- Running `python3 ingest.py` then `python3 rag_app.py` should succeed with `OPENAI_API_KEY` set.

### Submission Instruction

- create a repo `agentic-systems` (if done use the same) — clone it (ignore if already done)
- in that create folder called as `Module3` (ignore if already done)
- in that create folder called as `Session40`
- code all the things mentioned in the question — with all the files and folders structure (`documents/`, `ingest.py`, `rag_app.py`, generated `chroma_db/` is optional to push)
- do add all the ignorable files like datasets, `.env`, configs — json files etc
- then add — commit and push the code into Github and submit the root folder or folder of this assignment link as submission link (do not paste/submit the entire repo link — which is invalid)

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Create `documents/quiet_hours.md` and `documents/guest_policy.md` with the given text.
2. In `ingest.py`, optionally remove stale `chroma_db/` with `shutil.rmtree`.
3. Load Markdown files → split into chunks → embed with `text-embedding-3-small` → `add_documents` into Chroma collection `hostel_policy_docs`.
4. In `rag_app.py`, reload Chroma with the **same** collection name, persist path, and embedding model.
5. Define `format_docs` to join retrieved chunk text.
6. Build the LCEL dict chain with guardrail `ChatPromptTemplate`.
7. Run Q1 (in-corpus) and Q2 (out-of-corpus) and print results.

### Reference — `ingest.py`

```python
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = Path("documents")
CHROMA_DIR = Path("chroma_db")
COLLECTION_NAME = "hostel_policy_docs"
EMBEDDING_MODEL = "text-embedding-3-small"

if CHROMA_DIR.exists():
    shutil.rmtree(CHROMA_DIR)

loader = DirectoryLoader(
    str(DATA_DIR),
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=60,
    add_start_index=True,
)
chunks = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)
vector_store.add_documents(chunks)
print(f"Stored {len(chunks)} chunks in {COLLECTION_NAME}")
```

### Reference — `rag_app.py`

```python
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

CHROMA_DIR = Path("chroma_db")
COLLECTION_NAME = "hostel_policy_docs"
EMBEDDING_MODEL = "text-embedding-3-small"

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=str(CHROMA_DIR),
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2},
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


prompt = ChatPromptTemplate.from_template(
    """You are a hostel policy assistant.
Use only the retrieved context to answer.
If the answer is not present in the context, say: I don't know based on the provided documents.
Do not use outside knowledge.
Mention the source file name wherever possible.

Context:
{context}

Question:
{question}
"""
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)


def main():
    q1 = "What are the quiet hours on weekdays?"
    q2 = "What is the scholarship amount for hostel residents?"

    print("Q1:", q1)
    print("A1:", rag_chain.invoke(q1))
    print()
    print("Q2:", q2)
    print("A2:", rag_chain.invoke(q2))


if __name__ == "__main__":
    main()
```

### Alternative Valid Approaches

- Combine ingest + app in one script with a `--ingest` flag (acceptable if behaviour matches).
- Add a third in-corpus question about guest timing to strengthen manual testing.
- Print retrieved chunk metadata (`doc.metadata`) before generation for debugging.

### Common Mistakes to Avoid

- Running `rag_app.py` before `ingest.py` (empty Chroma).
- Mismatched `COLLECTION_NAME` or embedding model between ingest and app.
- Guardrail prompt missing → model hallucinates a scholarship amount for Q2.
- Forgetting `StrOutputParser()` parentheses in the LCEL chain.
