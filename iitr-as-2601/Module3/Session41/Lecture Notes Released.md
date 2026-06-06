# RAG: Retrieval & Grounded Generation

## Context of This Session

In the **previous** session you **chunked** a Tesla annual report PDF (~130 pages → **351 chunks**), embedded them with **`all-MiniLM-L6-v2`**, and **persisted** them in a Chroma vector store using **LangChain**. You also practised the same prepare steps on a smaller **ShopEasy policy** corpus in a manual notebook.

This session completes the RAG loop on the **Tesla index**: **retrieve** top-k chunks, **assemble** them into a prompt, and **generate** grounded answers with **Groq**. You finish with an informal grounding audit and a **Gradio** chat UI.

**What you will learn:**

- Configure **top-k retrieval** with a LangChain retriever on the Tesla vector index  
- Build a **context block** using **`#context`** and **`#question`** delimiter tokens  
- Generate answers with **Groq** at **`temperature=0`** and verify claims against retrieved chunks  
- Run an **end-to-end RAG script** and wrap it in a **Gradio** mini app  

Agent orchestration and production eval tooling are covered in **later work** on the same track.

![RAG flow — you built prepare in the previous session; this session finishes retrieve, augment, and generate with grounded answers from the Tesla vector index](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-01-rag-five-steps-retrieve-generate.png)

---

## The Complete RAG Loop — Recap

| Step | Name | What happens |
|---|---|---|
| 1 | **Ingest** | Load PDFs (Tesla annual report folder) |
| 2 | **Prepare** | Chunk → embed → store in Chroma |
| 3 | **Retrieve** | Top-k similarity search on the vector index |
| 4 | **Augment** | Paste retrieved chunks into the LLM prompt |
| 5 | **Generate** | LLM writes the answer **only from context** |

- **Official Definition:** **Grounded generation** means the LLM answer should follow **retrieved context**, not invent facts when the library already has the answer.
- **In Simple Words:** **Search first, paste the notes, then speak** — open-book exam with rules.
- **Real-Life Example:** At a **railway enquiry counter**, the clerk reads the **display board** (retrieved chunks) before telling you the platform — not from memory alone.

**Common mistake:** Skipping grounding rules in the prompt — the model may still **sound confident** while guessing.

---

## Top-k Retrieval — LangChain Retriever on the Tesla Index

Retrieval is the **bridge** between your Chroma index and the LLM prompt. In class you **loaded** the Tesla vector DB built earlier and instantiated a **LangChain retriever**.

- **Official Definition:** **Top-k retrieval** returns the **k** stored chunks whose embeddings are nearest to the query embedding.
- **In Simple Words:** *"Give me the **k** best report paragraphs for this question."*
- **Real-Life Example:** A librarian brings **five** relevant folders, not the entire stack — enough detail without drowning in noise.

### Choosing k

| k value | Effect |
|---|---|
| **k = 1** | Fast, cheap — may miss a second relevant passage |
| **k = 3–4** | **Balanced default** — good starting point to experiment |
| **k = 5** | **Demo value in class** — more context; used for Tesla revenue queries |
| **k very high** | More tokens and **noise** — irrelevant chunks can confuse the LLM |

- **Same model rule:** Encode the query with **`all-MiniLM-L6-v2`** — the model used when chunks were stored.  
- **Search type:** **`similarity`** — nearest-neighbour match in embedding space (like a distance formula on meaning).  
- **Common doubt:** *Is there one correct k?* No — **experiment** on your corpus; low k misses facts, high k adds noise.

![Top-k retrieval — encode the query with all-MiniLM-L6-v2, query the Tesla Chroma index, return k nearest chunks with metadata; k=3–4 is a balanced default, k=5 used in the live demo](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-02-top-k-retrieval.png)

### Load the vector store and create the retriever

```python
import os  # Read API keys from environment
from langchain_community.embeddings import HuggingFaceEmbeddings  # Same encoder as index time
from langchain_community.vectorstores import Chroma  # Load persisted Tesla vector DB

EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Must match storage model
CHROMA_PATH = "./Tesla_db"  # Folder created when you built the index
TOP_K = 5  # Demo used k=5; try 3–4 for a tighter context window

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)  # Load once per session

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,  # Reopen existing index — no re-embed needed
    embedding_function=embeddings,
)

retriever = vectorstore.as_retriever(
    search_type="similarity",  # Nearest-neighbour semantic search
    search_kwargs={"k": TOP_K},  # Top-k knob — main retrieval config
)
```

**How the code works:**

- **`Chroma(persist_directory=...)`** reopens the Tesla index from the **previous** prepare lab.  
- **`as_retriever`** wraps the store with a standard **`.invoke(query)`** interface.  
- **`search_kwargs={"k": TOP_K}`** is where you tune how many chunks enter the prompt.

### Retrieve chunks for a query

```python
def retrieve_chunks(user_query, retriever):
    """Return top-k LangChain Document objects for the user question."""
    docs = retriever.invoke(user_query)  # Embed query + similarity search internally
    retrieved = []
    for i, doc in enumerate(docs, start=1):
        retrieved.append({
            "index": i,
            "text": doc.page_content,  # Chunk body text
            "metadata": doc.metadata,  # page, source file, etc. when present
        })
    return retrieved
```

**How the code works:**

- **`retriever.invoke`** handles query embedding and Chroma lookup in one call.  
- Each **`Document`** carries **`page_content`** (text) and **`metadata`** (for informal citations).  
- Print retrieved chunks **before** generation — essential for the grounding audit later.

### Simple Activity — Tune Top-k

Run `retrieve_chunks` on *"What is the annual revenue in the year 2022?"* with **k = 1**, then **k = 5**. Note which **page numbers** appear in metadata. One sentence: would **k = 1** ever miss a second mention of the same figure elsewhere in the report?

---

## Context Assembly — System Message and Delimiter Tokens

Raw chunk text pasted blindly confuses the LLM. **Context assembly** wraps retrieved text in a **clear block** with **boundaries** the model can parse.

- **Official Definition:** **Context assembly** (prompt augmentation) combines retrieved chunks, formatting rules, and the user question into one LLM input.
- **In Simple Words:** Build the **exam paper** — instructions at top, **only allowed notes** in the middle, question at bottom.
- **Real-Life Example:** A **court brief** separates exhibits with headers — the judge knows which document each line came from.

### Two-message pattern taught in class

| Message role | Contents |
|---|---|
| **System message** | Persona, grounding rules, delimiter explanation (`#context`, `#question`) |
| **User message** | Original **question** + **retrieved context** block |

Delimiter tokens tell the LLM where context ends and the question begins:

```
#context
[retrieved chunk 1 text]
[retrieved chunk 2 text]
...
#question
What is the annual revenue in the year 2022?
```

- **Why delimiters:** Models parse **labelled sections** more reliably than one long blob.  
- **Why a system message:** Grounding rules (*"say I don't know if not in context"*) live here — they apply to every query.  
- **Common mistake:** Dumping chunks **without** rules — the model treats them as optional background.

![Context assembly with delimiters — system message defines #context and #question tokens; user message combines retrieved Tesla chunks and the original question](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-03-context-assembly-delimiters.png)

---

## Build the Prompt — System and User Messages

```python
SYSTEM_MESSAGE = """
You are an assistant for a financial services firm that answers user queries on annual reports.
User input will contain the context required to answer the question.
The context will begin with the token #context and contains portions of the source document.
The question will begin with the token #question.
Answer ONLY using the provided context.
If the answer is not found in the context, say: I don't know.
""".strip()


def build_context_block(retrieved_chunks):
    """Format retrieved chunks into a single context string."""
    parts = []
    for chunk in retrieved_chunks:
        parts.append(chunk["text"])
    return "\n\n".join(parts)


def build_user_message(user_query, retrieved_chunks):
    """Assemble #context and #question sections for the user message."""
    context_text = build_context_block(retrieved_chunks)
    return f"#context\n{context_text}\n#question\n{user_query}"
```

**How the code works:**

- **`SYSTEM_MESSAGE`** states persona, delimiter meaning, and the **I don't know** rule.  
- **`#context`** block holds all top-k chunk bodies joined with blank lines.  
- **`#question`** block holds the raw user query — same pattern as the live Tesla demo.

![RAG pipeline in code — retrieve_chunks, build_user_message, then generate_answer with Groq at temperature=0](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-04-rag-pipeline-code.png)

---

## Grounded Generation — Groq with temperature=0

The **generator** step sends your augmented messages to an LLM. Class used **Groq** (cloud API you already practised on this track).

- **Official Definition:** **Grounded generation** produces natural-language output constrained by supplied context rather than model memory alone.
- **In Simple Words:** The model **writes the answer** after reading your pasted report chunks.
- **Real-Life Example:** You **dictate** an answer after reading five PDF paragraphs — not from what you memorised last year.

### Why temperature=0 for RAG

- **Official Definition:** **Temperature** controls randomness in token sampling; **0** picks the most likely next token each step.
- **In Simple Words:** Same question + same context → **same answer** every run — important for factual Q&A.
- **Real-Life Example:** A **marks calculator** should not give 72 one time and 75 the next for the same inputs.

**Class rule:** Set **`temperature=0`** on RAG calls so answers stay **factual and repeatable**.

```python
import os  # Read GROQ_API_KEY from environment or Colab Secrets
from groq import Groq  # Cloud LLM client used in this session

GROQ_MODEL = "llama-3.3-70b-versatile"  # Fast model used on this track


def generate_answer(system_message, user_message):
    """Send system + user messages to Groq and return grounded assistant text."""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Your API key
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_message},  # Grounding rules + delimiter docs
            {"role": "user", "content": user_message},  # #context + #question block
        ],
        temperature=0,  # Factual, repeatable answers for RAG
    )
    return response.choices[0].message.content  # Final answer string
```

**How the code works:**

- **`messages`** uses **two roles** — system (rules) and user (context + question).  
- **`temperature=0`** reduces creative drift on financial facts.  
- **Common mistake:** Forgetting the API key or org quota — the cell fails before any answer is generated.

### Live demo result — revenue query

Question: *"What is the annual revenue in the year 2022?"*

- Retriever returned **five** relevant chunks.  
- Model answered **$96.77 billion** — matching language in the source report.  
- Instructor **manually verified** the figure against retrieved text on **page 51** and **page 57**.

### Simple Activity — Out-of-Context Refusal

Ask *"What is the weather in Delhi tomorrow?"* through the same RAG pipeline. The retriever may return **irrelevant** chunks, but the model should still reply **"I don't know"** because weather is not in the Tesla report. One sentence: why is the system message essential here?

---

## Informal Grounding Check — Map Claims to Chunks

Production systems use automated evaluators; in this lab you **manually verify** that claims map back to retrieved text.

- **Official Definition:** An **informal grounding check** compares each factual claim in the LLM output to retrieved chunk text and metadata.
- **In Simple Words:** **Fact-check the answer** against the paragraphs you pasted in.
- **Real-Life Example:** A **news fact-check desk** matches each headline claim to the **quoted paragraph** — same idea, done by you in a notebook.

### Checklist (run after every demo answer)

| Check | How |
|---|---|
| **Claim in context?** | Every number in the answer appears in **some retrieved chunk** |
| **Page trace** | Note **page** metadata (e.g. page 51, page 57) for each supporting chunk |
| **No-context case** | Off-topic questions → model should say **I don't know**, not invent |
| **Chunk ↔ claim map** | Write: *"$96.77B revenue → Chunk 2, page 51"* |

### Helper — print retrieval before generation

```python
def print_retrieval_trace(user_query, retrieved_chunks):
    """Print chunks before generation — use for manual grounding review."""
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for chunk in retrieved_chunks:
        meta = chunk.get("metadata", {})
        print(f"\nChunk {chunk['index']}")
        print(f"  metadata: {meta}")
        print(f"  text preview: {chunk['text'][:200]}...")
```

### Simple Activity — Grounding Audit

1. Query: *"What is the annual revenue in the year 2022?"*  
2. Print the **retrieval trace**, then the **generated answer**.  
3. Fill a two-column table: **Claim in answer** | **Which chunk + page supports it**.  
4. Repeat with a **weather** or **unrelated** question — confirm the model **refuses**.

![Informal grounding check — compare retrieval trace to the generated answer; map each claim to page metadata; verify no-context questions are refused](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-07-informal-grounding-check.png)

---

## Grounding Illusions — Fluent but Wrong Answers

Even with RAG, the model can **sound correct** while misreading nearby but **irrelevant** context.

- **Official Definition:** A **grounding illusion** is a confident answer that does not follow from the retrieved evidence.
- **In Simple Words:** The model **talks smoothly** but cites the wrong chunk or stretches a partial match.
- **Real-Life Example:** A student copies a **nearby paragraph** from the textbook that mentions a date but not the answer — looks cited, still wrong.

**Why manual audit matters:** Automated inline citations in model output were **not** the focus — you trace support yourself using the retrieval trace and page metadata.

![Without RAG vs with RAG — plain LLM call may hallucinate financial figures; RAG retrieves Tesla chunks first but you still audit claims against the trace](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-06-without-rag-vs-with-rag.png)

---

## End-to-End RAG Script — Tesla Annual Report

This script ties the full pipeline together: **load index → retrieve → prompt → answer**.

```python
import os
from groq import Groq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- Config ---
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CHROMA_PATH = "./Tesla_db"
TOP_K = 5
GROQ_MODEL = "llama-3.3-70b-versatile"

SYSTEM_MESSAGE = """
You are an assistant for a financial services firm that answers user queries on annual reports.
User input will contain the context required to answer the question.
The context will begin with the token #context and contains portions of the source document.
The question will begin with the token #question.
Answer ONLY using the provided context.
If the answer is not found in the context, say: I don't know.
""".strip()


def retrieve_chunks(user_query, retriever):
    docs = retriever.invoke(user_query)
    return [
        {"index": i, "text": d.page_content, "metadata": d.metadata}
        for i, d in enumerate(docs, start=1)
    ]


def build_user_message(user_query, retrieved_chunks):
    context_text = "\n\n".join(c["text"] for c in retrieved_chunks)
    return f"#context\n{context_text}\n#question\n{user_query}"


def generate_answer(system_message, user_message):
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
    """End-to-end: retrieve → build messages → generate → return audit bundle."""
    retrieved = retrieve_chunks(user_query, retriever)
    user_message = build_user_message(user_query, retrieved)
    answer = generate_answer(SYSTEM_MESSAGE, user_message)
    return {"answer": answer, "retrieved_chunks": retrieved, "user_message": user_message}


def main():
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)
    vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K},
    )

    question = "What is the annual revenue in the year 2022?"
    print("Question:", question)

    result = rag_answer(question, retriever)

    print("\n--- Retrieved chunks ---")
    for chunk in result["retrieved_chunks"]:
        print(f"Chunk {chunk['index']}: {chunk['metadata']}")

    print("\n--- Generated answer ---")
    print(result["answer"])

    print("\n--- Grounding audit (you fill in) ---")
    print("List each fact in the answer and the chunk page that supports it.")


if __name__ == "__main__":
    main()
```

**How the code works:**

- Assumes the **Tesla_db** folder already exists from the **previous** prepare lab (351 chunks).  
- **`rag_answer`** is the single function a chat UI or agent tool would call per message.  
- **`main()`** prints retrieval + answer + a reminder to **audit** claims against chunks.

![Mini end-to-end RAG script — load Tesla index, retrieve top-k, augment with #context/#question, generate via Groq, then audit claims against chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-08-end-to-end-mini-rag.png)

### Building the index (recap from previous lab)

If you need to recreate the vector store from the Tesla PDF folder:

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PDF_FOLDER = "Tesla_Annual_Reports"  # Folder with the annual report PDF(s)

loader = PyPDFDirectoryLoader(PDF_FOLDER)  # Load all PDFs in folder
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=16)
chunks = splitter.split_documents(documents)
print("Total chunks:", len(chunks))  # ~351 for the class PDF

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./Tesla_db",
)
```

**How the code works:**

- **`PyPDFDirectoryLoader`** scales to **many PDFs** in one folder — not just one file.  
- First-time vector DB creation can take **minutes to hours** at enterprise scale; the class PDF is small but the pattern is the same.  
- **Same embedding model** at index and query time — non-negotiable.

---

## ChatGPT Document Upload — In-Memory RAG

Before the hands-on block, class compared **ChatGPT file upload** to the Tesla pipeline you built.

- **Official Definition:** **In-memory / session RAG** builds a temporary vector index inside one chat session instead of a long-lived enterprise store.
- **In Simple Words:** Upload a PDF to ChatGPT → it chunks and searches **inside that chat** → answers with **source links**.
- **Real-Life Example:** Photocopying notes for **one exam prep session** — useful, but not the same as a company-wide library.

| Aspect | ChatGPT upload (session) | Enterprise RAG (Tesla lab pattern) |
|---|---|---|
| **Index lifetime** | Tied to the chat session | **Persistent** Chroma folder / cloud store |
| **Scale** | A few files per chat | **Millions** of documents |
| **Who manages data** | End user uploads | **Internal admins** — customers see only a chat UI |
| **What you built** | Scratch pipeline with LangChain + Chroma | Same story, fully under your control |

ChatGPT demonstrated **retrieval + citation** behind the scenes — the concepts match your lab, but you now control every step.

---

## Enterprise RAG — Scale, Sensitivity, and Updates

- **Official Definition:** **Enterprise RAG** serves many users against a **large, centrally managed** vector index with strict access controls.
- **In Simple Words:** A **massive internal library** that only **admins** curate; customers ask questions through a simple chat screen.
- **Real-Life Example:** A bank's **policy bot** — staff update PDFs on the backend; customers never touch the vector database.

**Key ideas from class:**

- Vector DBs are **highly sensitive** — end users should **not** manage upserts directly.  
- When source documents **change**, teams **re-chunk and re-embed** affected files (Chroma supports **upsert / update / delete**).  
- The **LLM itself** does not need to be organisation-specific — what is custom is the **data**, **retriever**, **prompts**, and **guardrails**.  
- **Latency** matters at scale — retrieval + generation time grows with index size and k.

---

## Code-Repository RAG — Extension Use Case

- **Official Definition:** **Code RAG** indexes source files (`.py`, `.ipynb`, etc.) so developers can query an internal codebase in natural language.
- **In Simple Words:** **GitHub Copilot-style** search — ask *"Where do we handle refunds?"* and get the right file chunk.
- **Real-Life Example:** A company with **thousands of Jupyter notebooks** builds RAG so any developer can ask how an internal API works.

**Suggested practice:** Take **five `.ipynb` notebooks**, chunk them like documents, embed into Chroma, and ask questions about functions defined inside — same pipeline as Tesla, different corpus.

---

## Gradio Mini RAG App — Chat-Style UI

The final demo wrapped the RAG logic in a **Python function** and exposed it with **Gradio** — a quick way to mock a ChatGPT-like interface.

- **Official Definition:** **Gradio** is a Python library that turns a function into a **web UI** with minimal frontend code.
- **In Simple Words:** Write **`answer(question)`** → Gradio shows a text box and return value — shareable demo URL.
- **Real-Life Example:** A **science fair prototype** — not a full production app, but enough to show investors the idea.

```python
import gradio as gr  # Simple UI wrapper for ML demos

def rag_chat(user_query):
    """Gradio entry point — same retrieve → prompt → generate path."""
    result = rag_answer(user_query, retriever)  # retriever defined earlier in notebook
    return result["answer"]


demo = gr.Interface(
    fn=rag_chat,  # Function Gradio calls on each submit
    inputs=gr.Textbox(label="Ask about the Tesla annual report"),
    outputs=gr.Textbox(label="Answer"),
    title="Tesla Annual Report Q&A",
)

demo.launch(share=True)  # Opens local URL + optional public link for demos
```

**How the code works:**

- **`rag_chat`** reuses the same **`rag_answer`** pipeline — only the **packaging** changes.  
- **`gr.Interface`** needs one line of wiring — popular for **POCs**, not full-stack production.  
- Production UIs are usually built by **frontend teams**; Gradio is for **experimentation and demos**.

---

## When Answers Still Look Wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Invented financial figure | Weak grounding instruction or ignored context | Strengthen system message; verify `#context` block |
| "I don't know" but chunk exists | **k** too low or bad chunking | Raise **TOP_K**; revisit chunk size from prepare lab |
| Wrong page cited in your audit | Noisy retrieval | Lower **k** or improve chunk boundaries |
| Different answer each run | **temperature > 0** | Set **`temperature=0`** for factual RAG |
| Generic answer | Skipped retrieval step | Always call **`rag_answer`**, not raw Groq chat |

Fix **retrieval and prompt** before blaming the chat model.

---

## What Comes Next

- **Agents** — call `rag_answer` as a **tool** inside a larger agent loop.  
- **Metadata filters** — retrieve only from specific report sections or file names.  
- **Production eval** — automated grounding scores instead of manual audit.

---

## Key Takeaways

- **Top-k retrieval** on the Tesla Chroma index via a LangChain **`similarity`** retriever connects your prepared embeddings to each user question — start around **k = 3–4**, demo used **k = 5**.  
- **Context assembly** uses a **system message** plus **`#context` / `#question`** tokens in the user message so the LLM knows which evidence it may use.  
- **Grounded generation** with **Groq** at **`temperature=0`** plus an **informal grounding check** (claim ↔ chunk/page map) keeps answers tied to the annual report.  
- The **end-to-end script** runs **load index → retrieve → augment → generate** — the same pattern every RAG app uses, extendable to **code repos** or **enterprise** corpora.  
- **ChatGPT upload** is **session-scale RAG**; your lab builds the **persistent, controllable** version. **Gradio** wraps the pipeline into a quick Q&A demo UI.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `TOP_K` / `search_kwargs={"k": ...}` | Config | Number of chunks retrieved per query |
| `vectorstore.as_retriever` | Code | LangChain retriever on Chroma |
| `search_type="similarity"` | Config | Nearest-neighbour semantic search |
| `retrieve_chunks` | Code | Embed query + top-k via retriever |
| `SYSTEM_MESSAGE` | Pattern | Grounding rules + delimiter documentation |
| `#context` / `#question` | Pattern | Delimiter tokens in user message |
| `build_user_message` | Code | Assemble context + question block |
| `temperature=0` | Config | Deterministic, factual generation |
| `Groq` / `GROQ_API_KEY` | Code / Config | Cloud LLM client and API key |
| `rag_answer` | Code | End-to-end retrieve → prompt → generate |
| `Chroma(persist_directory=...)` | Code | Load persisted Tesla vector index |
| `HuggingFaceEmbeddings` | Code | Same `all-MiniLM-L6-v2` encoder |
| `gr.Interface` | Code | Gradio one-function web UI |
| **Context assembly / Augment** | Concept | Insert retrieved text into LLM prompt |
| **Grounded generation** | Concept | Answer from supplied context only |
| **Informal grounding check** | Practice | Manually map claims to chunk sources |
| **Grounding illusion** | Concept | Fluent answer not supported by evidence |
| **Enterprise RAG** | Concept | Large persistent index, admin-managed |
| **In-memory / session RAG** | Concept | Temporary index (e.g. ChatGPT upload) |
| **Code-repository RAG** | Concept | RAG over internal `.py` / `.ipynb` files |
| **Same model rule** | Concept | Same embed model for index and query |
| `pip install langchain langchain-community groq gradio` | Setup | Packages used in the Tesla demo |
