# RAG: Retrieval & Grounded Generation

## Context of This Session

In **previous work** on this track you **loaded** PDFs, **split** them into chunks, **embedded** them, and **stored** vectors in **Chroma** — including a large **Tesla annual report** demo with **LangChain**, **RecursiveCharacterTextSplitter**, and **GTE-large** embeddings (~351 chunks at 512 characters each).

This session completes the **retrieve → augment → generate** steps on that prepared index. You will **tune top-k retrieval**, **assemble context with delimiters**, and **generate grounded answers** with **Groq** — then **verify** answers against the source PDF.

**In this session, you will:**

- **Configure top-k retrieval** on your existing Chroma index using a **LangChain retriever**
- **Assemble retrieved chunks** into a prompt block with clear **`##context`** and **`##question`** delimiters
- **Generate grounded answers** with a **RAG-specific system message** and **Groq**
- Run an **informal grounding check** by comparing answers to retrieved chunks and the source document
- Walk through a **full end-to-end RAG pipeline** on the Tesla report and a smaller **HR policy PDF**

Automated RAG evaluation (for example **RAG triad** judges) and agent tooling are covered in **later work** on the same track.

![RAG flow — you built prepare in previous work; this session finishes retrieve, augment, and generate with grounded answers from your indexed chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-01-rag-five-steps-retrieve-generate.png)

---

## The Missing Steps — Retrieve, Augment, Generate

| Step | Name | Covered here |
|---|---|---|
| 1–2 | Ingest + Prepare | **Brief reuse** of loaders, chunking, and Chroma setup from previous labs |
| 3 | **Retrieve** | **Top-k** search via LangChain retriever |
| 4 | **Augment** | Join chunks + **delimiter** prompt template |
| 5 | **Generate** | **Groq** LLM with grounding rules |

- **Official Definition:** **Grounded generation** means the LLM answer should follow **retrieved context**, not invent facts when the document already has the answer.
- **In Simple Words:** **Search first, paste the notes, then speak** — open-book exam with rules.
- **Real-Life Example:** At a **railway enquiry counter**, the clerk reads the **display board** (retrieved chunks) before telling you the platform — not from memory alone.

**Common mistake:** Skipping grounding rules in the prompt — the model may still **sound confident** while guessing.

---

## Where RAG Can Fail — Check Upstream First

Before blaming the chat model, walk through these **failure points**:

| Stage | What goes wrong | Symptom |
|---|---|---|
| **Chunking** | Chunks too large or too small | Wrong or vague retrieval |
| **Embedding model** | Weak or mismatched model | Similar questions miss the right chunk |
| **Vector DB** | Index empty or wrong collection | No useful results |
| **Query encoding** | Different model at query time vs storage | Meaningless distances |
| **Top-k** | **k** too low or too high | Missing facts or noisy context |

- **Official Definition:** The **MTEB leaderboard** ranks embedding models on benchmark tasks — a quick way to compare model quality.
- **In Simple Words:** A **report card** for embedding models before you pick one for production.
- **Real-Life Example:** You would not use a **broken map** to navigate Delhi — a bad embedding model sends retrieval to the wrong “address” in vector space.

**Same-model rule:** Encode queries with the **same embedding model** used when chunks were stored (**GTE-large** in the Tesla demo).

---

## Top-k Retrieval — Configure Search Against Your Index

Retrieval is the **bridge** between your Chroma index and the LLM prompt.

- **Official Definition:** **Top-k retrieval** returns the **k** stored chunks whose embeddings are nearest to the query embedding.
- **In Simple Words:** *"Give me the **k** best paragraphs for this question."*
- **Real-Life Example:** A librarian brings **five** relevant folders, not the entire stack — enough detail without noise.

### Choosing k — Think in Extremes

| k value | Effect |
|---|---|
| **k = 1** | Fast — may miss a second relevant page |
| **k = 5** | **Demo default** on Tesla and HR notebooks |
| **k = 100** | Too much text — slow, noisy, defeats the purpose of RAG |

- **Latency trade-off:** Higher **k** means more chunks to retrieve and more tokens in the prompt — answers may improve slightly but the app feels **slower**.
- **Common doubt:** *Should k always be high?* No — start with a **middle value** (for example **5**), then tune if answers miss facts.

![Top-k retrieval — encode the query, query Chroma, return k nearest chunks with metadata; k=5 is a practical demo default](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-02-top-k-retrieval.png)

### Reuse the Prepared Index and Instantiate a Retriever

Reopen the **Tesla Chroma index** built earlier, then create a retriever that returns the **top five** similar chunks:

```python
import os  # Read API keys from the environment
from langchain_community.document_loaders import PyPDFDirectoryLoader  # Load PDFs from a folder
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Split long documents into chunks
from langchain_community.vectorstores import Chroma  # LangChain wrapper around Chroma vector DB
from langchain_community.embeddings import HuggingFaceEmbeddings  # Embedding model via Hugging Face

PDF_FOLDER = "Tesla_Annual_Reports"  # Folder with Tesla PDF files (from the shared zip)
CHUNK_SIZE = 512  # Character window per chunk — same as the large-PDF prepare lab
CHUNK_OVERLAP = 16  # Small overlap so sentences on borders are not lost
TOP_K = 5  # Number of chunks to retrieve per question

# --- Load and chunk (reuse if index already built in your notebook) ---
loader = PyPDFDirectoryLoader(PDF_FOLDER)  # Read every PDF in the folder
documents = loader.load()  # List of LangChain Document objects with page_content + metadata

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)
chunks = splitter.split_documents(documents)  # ~351 chunks on the Tesla corpus in the demo

# --- Embed and store in Chroma ---
embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-large")  # GTE-large — same model as prepare lab

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="tesla_reports",  # Named collection for this corpus
)

retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})  # Top-k retriever wired to Chroma
```

**How the code works:**

- **`PyPDFDirectoryLoader`** — loads every PDF in a folder (use a single-file loader when you have only one PDF).
- **`RecursiveCharacterTextSplitter`** — fixed-size windows with overlap; chunk **metadata** keeps **source** and **page** for traceability.
- **`HuggingFaceEmbeddings` + GTE-large** — same encoder for storage and query inside LangChain.
- **`as_retriever(search_kwargs={"k": TOP_K})`** — the main **k** knob for this lesson.

### Simple Activity — Test the Retriever

Run a retrieval-only query before any LLM call:

```python
user_question = "What is the annual revenue in the year 2022?"  # Sample finance question

retrieved_docs = retriever.get_relevant_documents(user_question)  # Embed query + top-k search in one call

for i, doc in enumerate(retrieved_docs, start=1):
    print(f"\n--- Chunk {i} ---")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print("Text preview:", doc.page_content[:200], "...")
```

**Your task:** Confirm that at least one retrieved chunk contains the **2022 revenue figure** before you generate an answer. One sentence: what happens if you set **k = 1** for a question that needs facts from **two different pages**?

---

## Context Assembly — Delimiters and Joined Chunk Text

Raw chunk lists confuse the LLM. **Context assembly** wraps retrieved text in a **clear block** with **boundaries** and the **user question**.

- **Official Definition:** **Context assembly** (prompt augmentation) combines retrieved chunks, formatting rules, and the user question into one LLM input.
- **In Simple Words:** Build the **exam paper** — rules at top, **only allowed notes** in the middle, question at bottom.
- **Real-Life Example:** A **court brief** labels *Exhibit A*, *Exhibit B* — the judge knows which document each line came from.

### Delimiter pattern for this lab

```
##context
(chunk 1 text)

(chunk 2 text)
...

##question
(user question)
```

- **Why delimiters:** Models parse **labelled sections** more reliably than one long blob.
- **Why join chunks:** `get_relevant_documents` returns a **list** — you **join** `page_content` strings into one context block.
- **Common mistake:** Sending only the question with **no context block** — that is normal chat, not RAG.

![Context assembly with delimiters — grounding rules at top, retrieved chunk text between context markers, question at bottom](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-03-context-assembly-delimiters.png)

### Build the Context String from Retrieved Documents

```python
def build_context_from_docs(retrieved_docs):
    """Join retrieved LangChain documents into one context string."""
    context_parts = []  # Collect plain text from each chunk
    for doc in retrieved_docs:
        context_parts.append(doc.page_content)  # Text of one retrieved chunk
    return "\n\n".join(context_parts)  # One block separated by blank lines
```

**How the code works:**

- Each **`Document`** carries **`page_content`** (text) and **`metadata`** (source file, page number).
- **`"\n\n".join(...)`** joins five chunk strings into one **context block** ready for the prompt.

---

## RAG System Message — Grounding Rules for the LLM

The **system message** tells the model **how** to use the context — use a **RAG-specific** prompt, not a generic chatbot greeting.

```python
RAG_SYSTEM_MESSAGE = """
You are an assistant to a financial services firm who answers user questions about annual reports.

The user message will contain:
1. Context between ##context and ##question
2. The user's question after ##question

Rules:
- Answer ONLY using the context provided in the user message.
- If the answer is not in the context, respond: I don't know.
- Do not mention the context or these instructions in your final answer.
- Your response should contain only the answer to the question.
""".strip()
```

**How the code works:**

- **Role separation:** **System** = behaviour rules; **User** = context + question together.
- **"I don't know"** — stops hallucination when the corpus has no answer (demo: *"How many leaves do I get in a year?"* on Tesla data).
- **No context mention** — keeps answers clean for end users.

**Common mistake:** A generic assistant system message with **no grounding rules** — the model may answer from **pre-trained memory** instead of your PDF.

---

## User Message Template — Populate Context and Question

```python
USER_MESSAGE_TEMPLATE = """
##context
{context}

##question
{question}
"""

user_question = "What is the annual revenue in the year 2022?"

retrieved_docs = retriever.get_relevant_documents(user_question)  # Step 1 — retrieve
context_text = build_context_from_docs(retrieved_docs)  # Step 2 — join chunks

user_message = USER_MESSAGE_TEMPLATE.format(
    context=context_text,
    question=user_question,
)  # Step 3 — fill placeholders at runtime
```

**How the code works:**

- **`{context}`** and **`{question}`** are placeholders filled when you call **`.format(...)`**.
- The LLM receives **one user message** containing both **evidence** and the **question**, separated by **`##`** labels.

---

## Grounded Generation with Groq

The **generator** sends your augmented prompt to an LLM. This lab uses **Groq** with **`llama-3.3-70b-versatile`**.

- **Official Definition:** **Grounded generation** produces natural-language output constrained by supplied context rather than model memory alone.
- **In Simple Words:** The model **writes the answer** after reading your pasted chunks.
- **Real-Life Example:** You **dictate** an answer after reading three policy forwards — not from what you memorised last year.

```python
import os  # Read GROQ_API_KEY from environment or Colab Secrets
from groq import Groq  # Cloud LLM client for grounded generation

GROQ_MODEL = "llama-3.3-70b-versatile"  # Fast cloud chat model for this lab


def generate_grounded_answer(system_message, user_message):
    """Call Groq with temperature=0 for deterministic RAG answers."""
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Connect with your API key
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            temperature=0,  # Deterministic — same question should give the same answer
            messages=[
                {"role": "system", "content": system_message},  # Grounding rules
                {"role": "user", "content": user_message},  # Context + question block
            ],
        )
        return response.choices[0].message.content  # Final answer string
    except Exception as error:
        return f"Generation failed safely: {error}"  # try/except keeps the notebook from crashing
```

**How the code works:**

- **`temperature=0`** — keep RAG answers stable so repeated runs match.
- **`try/except`** — catches bad API keys, wrong model names, or network errors without breaking the whole notebook.
- **Two-message shape** — system rules + one user block with context and question.

![RAG pipeline in code — retrieve with LangChain, build delimited user message, generate with Groq](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-04-rag-pipeline-code.png)

### Simple Activity — Multi-Step Finance Question

1. Ask: *"What is the total annual revenue across both 2022 and 2023?"*
2. Print retrieved chunks, then the generated answer.
3. Open the source PDF and **add the two year figures manually** — confirm the model **summed** numbers from context (expect a combined total near **178.23 billion** when both year figures are present).
4. One sentence: why does this question need **k > 1**?

---

## Informal Grounding Check — Verify Against Retrieved Text

Production systems use automated evaluators; in this lab you **manually verify** that claims map back to retrieved text.

- **Official Definition:** An **informal grounding check** compares each factual claim in the LLM output to retrieved chunk text and source metadata.
- **In Simple Words:** **Fact-check the answer** against the paragraphs you pasted in.
- **Real-Life Example:** A **news fact-check desk** matches each headline claim to the **quoted paragraph** — same idea, done by you in a notebook.

### Checklist (run after every demo answer)

| Check | How |
|---|---|
| **Claim in context?** | Every number or rule in the answer appears in **some retrieved chunk** |
| **Source traceable?** | Use chunk **metadata** (source PDF, **page** number) to locate the evidence |
| **No-context case** | Ask an **off-topic** question — model should say **I don't know**, not invent |
| **Chunk ↔ claim map** | Write: *"2022 revenue → Chunk 2, page 42"* in your notebook |

```python
def print_retrieval_trace(user_query, retrieved_docs):
    """Print chunks before generation — use for manual grounding review."""
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"\nChunk {i}")
        print("  source:", doc.metadata.get("source"))
        print("  page:", doc.metadata.get("page"))
        print("  text preview:", doc.page_content[:200], "...")
```

### Simple Activity — Grounding Audit

1. Query: *"What is the annual revenue in the year 2022?"*
2. Run **`print_retrieval_trace`**, then **`generate_grounded_answer`**.
3. Fill a two-column table: **Claim in answer** | **Which chunk + page supports it**.
4. Repeat with an **off-corpus** question — confirm the model **refuses** or says **I don't know**.

![Informal grounding check — compare retrieval trace to the generated answer; map each claim to source file and page](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-07-informal-grounding-check.png)

---

## Without RAG vs With RAG — Why Retrieval Matters

Same question, two paths:

| Path | What happens |
|---|---|
| **Without RAG** | Plain LLM call — question only, **no retrieved context** |
| **With RAG** | Retrieve chunks first, then generate from the **context block** |

- **Without RAG**, the model may invent a **plausible-sounding** return policy or revenue figure from **general training memory**.
- **With RAG**, the model must read **your PDF chunks** first — check numbers such as **81,462 million** against the source Tesla file after generation.

When you practise in your notebook, run the **same question** both ways and compare outputs.

![Without RAG vs with RAG — plain LLM call may hallucinate; RAG retrieves chunks first and answers from your corpus](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-06-without-rag-vs-with-rag.png)

---

## End-to-End RAG Function — Retrieve, Augment, Generate

Wrap the full pipeline in one callable function — reuse the same pattern on the **Tesla** report and on a smaller **HR policy PDF**.

```python
def rag_answer(user_query, retriever, system_message=RAG_SYSTEM_MESSAGE):
    """End-to-end: retrieve → build user message → generate → return answer + chunks."""
    retrieved_docs = retriever.get_relevant_documents(user_query)  # Retrieve top-k chunks
    context_text = build_context_from_docs(retrieved_docs)  # Join chunk text
    user_message = USER_MESSAGE_TEMPLATE.format(
        context=context_text,
        question=user_query,
    )  # Delimited user block
    answer = generate_grounded_answer(system_message, user_message)  # Groq generation
    return {
        "answer": answer,
        "retrieved_docs": retrieved_docs,
        "user_message": user_message,
    }


def demo_rag_question(question):
    """Print retrieval trace, answer, and a reminder to audit claims."""
    print("Question:", question)
    result = rag_answer(question, retriever)
    print_retrieval_trace(question, result["retrieved_docs"])
    print("\n--- Generated answer ---")
    print(result["answer"])
    print("\n--- Your grounding audit ---")
    print("List each fact in the answer and the chunk source/page that supports it.")


if __name__ == "__main__":
    demo_rag_question("What is the annual revenue in the year 2022?")
```

**How the code works:**

- **`rag_answer`** — one function an app can call per user message.
- **`retrieved_docs`** returned with the answer so you can **audit** without re-running retrieval.
- **HR demo:** Same template with a different system persona (*HR assistant*) and a **smaller PDF** — chunk size was reduced (for example **64** characters) because the document was only **eight pages**.

![Mini end-to-end RAG script — retrieve top-k, augment with delimiters, generate via Groq, then audit claims against chunks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session41/session41-08-end-to-end-mini-rag.png)

---

## Latency and Production Mindset

RAG is an **application** real users will wait on — not just a notebook exercise.

- **Retrieval time** grows when **k** is large — fetching **100 chunks** is slower than **5**.
- **Prompt size** grows with more chunks — the LLM takes longer to read a huge context block.
- **Trade-off:** You cannot always maximise **accuracy** and **speed** at the same time — tune **k** for your use case.

**Indexing vs retrieval layers:** Preparing chunks and embeddings is often called the **indexing** pipeline (can run ahead of time, including on your own machines). Finding the right chunks at question time is the **retrieval** layer — then you call the LLM.

**Real-world examples:**

- **Amazon Rufus** on product pages retrieves specs before answering feature questions — the same **retrieve-then-generate** pattern at ecommerce scale.
- **Product manuals** (AC, washing machine, refrigerator PDFs) can power a support assistant: scrape or load manuals into Chroma, then answer button / cycle questions from retrieved pages.

### Image embeddings (concept)

Pages can hold **figures** as well as text. **Image embeddings** turn a picture into a vector the same way text embeddings turn a paragraph into numbers. The **MTEB** space also lists image embedding models — multimodal RAG is a natural extension once text RAG is solid.

---

## When Answers Still Look Wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Invented detail | Weak grounding instruction or no context | Strengthen system rules; check delimiters |
| "I don't know" but chunk exists | **k** too low or bad chunking | Raise **TOP_K**; revisit chunk size |
| Wrong page cited | Noisy retrieval | Lower **k** or improve chunks |
| Generic answer | Called LLM **without** context block | Use full **`rag_answer`** path |
| Slow responses | **k** too high | Lower **k** or filter metadata |

Fix **retrieval and prompt** before blaming the chat model.

---

## What Comes Next

- **Agents** — call **`rag_answer`** as a **tool** inside a larger agent loop.
- **Automated evaluation** — grounding judges and **RAG triad** metrics instead of manual audit only.
- **Advanced retrieval** — metadata filters, reranking, and semantic chunking.

---

## Key Takeaways

- **Top-k retrieval** via **`retriever.get_relevant_documents`** connects your prepared **Chroma** index to the user question — **k = 5** is a sensible starting point; tune using **extreme cases** (k = 1 vs k = 100).
- **Context assembly** uses **`##context`** / **`##question`** delimiters and a **joined chunk block** so the LLM knows which evidence it may use.
- **Grounded generation** with a **RAG system message**, **`temperature=0`**, and **Groq** keeps answers tied to retrieved text — use an **informal grounding check** (claim ↔ chunk map) after every run.
- The **`rag_answer`** pattern runs **retrieve → augment → generate** in one flow — reuse it on **Tesla**-scale PDFs and short **HR** manuals.
- **Without-RAG** calls show why retrieval matters — the model guesses; **with-RAG** it reads your library first.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `TOP_K` / `search_kwargs={"k": ...}` | Config | Number of chunks retrieved per query |
| `retriever.get_relevant_documents` | Code | LangChain one-line retrieve (embed query + search) |
| `build_context_from_docs` | Code | Join retrieved chunk text into one block |
| `USER_MESSAGE_TEMPLATE` | Code | Delimited context + question template |
| `RAG_SYSTEM_MESSAGE` | Code | Grounding rules for the LLM |
| `generate_grounded_answer` | Code | Groq call with `temperature=0` |
| `rag_answer` | Code | End-to-end retrieve → prompt → generate |
| `##context` / `##question` | Pattern | Delimiters marking evidence vs question |
| **Context assembly / Augment** | Concept | Insert retrieved text into LLM prompt |
| **Grounded generation** | Concept | Answer from supplied context, not memory alone |
| **Informal grounding check** | Practice | Manually map claims to chunk sources |
| **Top-k retrieval** | Concept | Return k nearest chunks by embedding distance |
| `PyPDFDirectoryLoader` | Code | Load all PDFs from a folder |
| `RecursiveCharacterTextSplitter` | Code | Fixed-size chunking with overlap |
| `HuggingFaceEmbeddings` + GTE-large | Code | Embedding model used in Tesla demo |
| `Chroma.from_documents` | Code | Build LangChain vector store from chunks |
| `vectorstore.as_retriever` | Code | Create searchable retriever from store |
| `GROQ_API_KEY` | Config | API key for Groq (env / Colab Secrets) |
| `pip install groq` | Setup | Groq Python client |
| **MTEB leaderboard** | Reference | Benchmark ranking for embedding models (text and image) |
| **Chunk distance** | Concept | Similarity score — useful for relevance inspection |
| **Latency trade-off** | Concept | Higher k → more context vs slower responses |
| **Indexing vs retrieval** | Concept | Prepare/store ahead of time; search at question time |
| **Image embeddings** | Concept | Encode pictures as vectors for multimodal search |
