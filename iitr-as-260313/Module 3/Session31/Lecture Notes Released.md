# LangChain RAG Pipeline

## Context of This Session

In **previous work** on this track you attached **rolling conversational memory** to a LangChain agent and explored the early **RAG prepare** steps — loading PDFs, **chunking**, **embedding**, and storing vectors in **Chroma**.

This session completes the **retrieve → augment → generate** path as a **LangChain** workflow. You will **load and chunk** PDF corpora, **build a Chroma index**, **tune top-k retrieval**, **assemble context with delimiters**, and **generate grounded answers** — then **verify** outputs against the source document.

**In this session, you will:**

- **Ingest and segment** PDF corpora with LangChain **loaders** and **RecursiveCharacterTextSplitter**
- **Embed and store** chunks in **Chroma** using **GTE-large** sentence-transformer embeddings
- **Configure top-k retrieval** and run an **imperative RAG pipeline** (retrieve → prompt → LLM)
- Apply **grounding rules** in the system message and run an **informal with-RAG vs without-RAG check**

Formal **LCEL pipe chains** and automated **RAG evaluation judges** are introduced in **later work** on the same track.

![RAG offline prepare path vs online answer path — documents become a vector filing cabinet; each question retrieves passages before the reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module3/session31/session31-rag-offline-online.png)

---

## Why RAG Belongs Next to Agent Memory

- **Official Definition:** **Retrieval-Augmented Generation (RAG)** connects an LLM to an external knowledge store so answers can use **your** documents at query time.
- **In Simple Words:** The model **looks up** the right policy lines before it writes the reply.
- **Real-Life Example:** An HR chatbot must quote **your** leave rule, not a generic internet guess.

| Need | Memory | RAG |
|---|---|---|
| Follow-up like *“What about that leave?”* | Helps — history carries context | Not enough by itself |
| *“What is the salary policy?”* | Does not load the PDF | Retrieves the relevant section |
| Trust / audit | Soft — depends on past chat | Stronger — tied to retrieved passages |

Both skills matter: **memory** for dialogue continuity, **RAG** for document truth.

![Why RAG looks up the handbook — memory alone may invent rules; RAG opens the policy file and answers from it](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module3/session31/session31-why-rag-handbook.png)

---

## The Five-Step RAG Workflow

| Step | Name | What happens |
|---|---|---|
| 1 | **Ingest** | Load raw files (PDF, Word, text) into LangChain **Document** objects |
| 2 | **Prepare** | **Chunk** text, **embed** chunks, **store** vectors in a vector DB |
| 3 | **Retrieve** | For each user question, fetch the **top-k** most similar chunks |
| 4 | **Augment** | Insert retrieved text into the **prompt** with clear delimiters |
| 5 | **Generate** | Call the LLM so the answer follows the **supplied context** |

- **Official Definition:** A **RAG pipeline** turns a user query into a grounded answer by **retrieving** relevant chunks and **conditioning** generation on that context.
- **In Simple Words:** **Search first, speak second.**
- **Real-Life Example:** Before answering a revenue question, the bot opens the annual report, finds the finance table, then replies.

**Offline prepare path** (once, or when documents change):

```
PDF files → Document loader → Text splitter → Embeddings → Chroma
```

**Online answer path** (every user question):

```
User question → Retriever → Prompt + context → LLM → Final answer
```

---

## Chunkification — Why Big PDFs Become Small Chunks

- **Official Definition:** **Chunking** splits long documents into smaller segments suitable for embedding and retrieval.
- **In Simple Words:** You cut a thick report into **index cards**, not one giant card.
- **Real-Life Example:** One embedding for an entire PDF blends finance tables with HR notes, so a revenue question may match the wrong page.

**Why chunk?** Large files are hard to search precisely; one vector for a whole PDF **mixes** topics; retrieval should return a **focused** passage.

| Setting | Tesla demo | Nestle / HR demo |
|---|---|---|
| `chunk_size` | **512** characters | **64** characters (small 8-page PDF) |
| `chunk_overlap` | **16** characters | Adjusted for short document |
| Result | ~**351** chunks | More, smaller sections |

- **Extreme cases:** If every chunk is **one character**, retrieval is useless noise. If the **entire PDF** is one chunk, RAG loses its purpose.
- **Common mistake:** Blaming the LLM when **chunk size** was wrong upstream — fix chunking before tuning the chat model.

![Chunkification — a thick document becomes overlapping index cards so each idea can be searched precisely](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module3/session31/session31-chunkification.png)

---

## Where RAG Can Fail — Check Upstream First

Before blaming the chat model, walk through these **failure points**:

| Stage | What goes wrong | Symptom |
|---|---|---|
| **Chunking** | Chunks too large or too small | Wrong or vague retrieval |
| **Embedding model** | Weak or mismatched model | Similar questions miss the right chunk |
| **Vector DB** | Index empty or wrong collection | No useful results |
| **Metadata** | Missing source / page tags | Hard to audit which file supported an answer |
| **Query encoding** | Different model at query time vs storage | Meaningless distances |
| **Top-k** | **k** too low or too high | Missing facts or noisy context |

- **Official Definition:** The **MTEB leaderboard** ranks embedding models on benchmark tasks — a quick way to compare model quality.
- **In Simple Words:** A **report card** for embedding models before you pick one for production.
- **Real-Life Example:** You would not use a **broken map** to navigate — a bad embedding model sends retrieval to the wrong “address” in vector space.

**Same-model rule:** Encode queries with the **same embedding model** used when chunks were stored (**GTE-large** in the live demos).

---

## LangChain Components Used in This Session

| # | Component | Role in this session |
|---|---|---|
| 1 | **`PyPDFDirectoryLoader`** | Load **all PDFs** from one folder |
| 2 | **`RecursiveCharacterTextSplitter`** | Split documents into chunks (`chunk_size`, `chunk_overlap`) |
| 3 | **`HuggingFaceEmbeddings` (GTE-large)** | Convert each chunk into a numeric vector |
| 4 | **`Chroma`** | Store vectors and run **similarity search** |
| 5 | **`as_retriever()`** | Accept a query and return **top-k** chunks |
| 6 | **Prompt + LLM call** | Join context, apply grounding rules, generate answer |

- **Official Definition:** A **document loader** reads external files and returns LangChain **Document** objects (text + metadata such as **source** and **page**).
- **In Simple Words:** A **file reader** that speaks LangChain’s language.
- **Real-Life Example:** A librarian scanning each report page into a standard catalogue card.

**Note:** LangChain also offers **`DirectoryLoader`**, **`TextLoader`**, and many other loaders — the live demo used **PDF folder loading** because the corpora were annual reports and HR policy PDFs.

---

## Step 1 — Load, Split, Embed, and Store in Chroma

This is the **prepare** step: turn PDFs into searchable vectors inside **Chroma**.

### Install dependencies (once per environment)

```bash
pip install langchain langchain-community langchain-text-splitters chromadb sentence-transformers
```

### Full code — prepare the Tesla index

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader  # Load every PDF in a folder
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Split long documents into chunks
from langchain_community.vectorstores import Chroma  # LangChain wrapper around Chroma vector DB
from langchain_community.embeddings import HuggingFaceEmbeddings  # Embedding model via Hugging Face

PDF_FOLDER = "Tesla_Annual_Reports"  # Folder with Tesla PDF files (from the shared zip)
CHUNK_SIZE = 512  # Character window per chunk — demo default on the large corpus
CHUNK_OVERLAP = 16  # Small overlap so sentences on borders are not lost
TOP_K = 5  # Number of chunks to retrieve per question (used later)

loader = PyPDFDirectoryLoader(PDF_FOLDER)  # Read every PDF in the folder
documents = loader.load()  # List of LangChain Document objects with page_content + metadata

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)
chunks = splitter.split_documents(documents)  # ~351 chunks on the Tesla corpus in the demo
print(f"Chunks generated: {len(chunks)}")

# Inspect one chunk — text plus metadata (source file, page number)
sample = chunks[0]
print("Text preview:", sample.page_content[:200])
print("Metadata:", sample.metadata)

embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-large")  # GTE-large — used in class

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="tesla_reports",  # Named collection for this corpus
)

retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})  # Top-k retriever wired to Chroma
print("Chroma index ready.")
```

**How the code works:**

- **`PyPDFDirectoryLoader`** — loads every PDF in a folder; if you have **multiple PDFs** in one directory, one loader call reads them all.
- **`RecursiveCharacterTextSplitter`** — fixed-size windows with overlap; chunk **metadata** keeps **source** and **page** for traceability.
- **`HuggingFaceEmbeddings` + GTE-large** — converts text to ~**1024**-dimension vectors; use the **same** model at ingest and query time.
- **`Chroma.from_documents`** — embeds each chunk and stores vectors for similarity search.
- **`as_retriever(search_kwargs={"k": TOP_K})`** — creates the searchable interface used in the answer path.

![Ingest into Chroma — load PDFs, split, embed as vectors, then store in a searchable index](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module3/session31/session31-ingest-chroma.png)

### Simple Activity — Inspect Chunks Before Retrieval

1. Print **`len(chunks)`** after splitting — confirm you see ~**351** on the Tesla corpus.
2. Print **metadata** for three random chunks — note **source** and **page** values.
3. One sentence: why is **page number** useful when you audit an answer later?

### Re-run on a smaller HR / Nestle PDF

Reuse the **same template** with a smaller policy PDF. Because the file was only **eight pages**, the instructor reduced **`chunk_size` to 64** so the splitter still produces enough sections. Same loader → splitter → embed → Chroma flow; only chunk settings and the system persona change.

---

## Step 2 — Top-k Retrieval

Retrieval is the **bridge** between your Chroma index and the LLM prompt.

- **Official Definition:** **Top-k retrieval** returns the **k** stored chunks whose embeddings are nearest to the query embedding.
- **In Simple Words:** *"Give me the **k** best paragraphs for this question."*
- **Real-Life Example:** A librarian brings **five** relevant folders, not the entire stack.

### Choosing k — Think in Extremes

| k value | Effect |
|---|---|
| **k = 1** | Fast — may miss a second relevant page |
| **k = 5** | **Demo default** on Tesla and HR notebooks |
| **k = 100** | Too much text — slow, noisy, defeats the purpose of RAG |

- **Latency trade-off:** Higher **k** means more chunks to retrieve and more tokens in the prompt — answers may improve slightly but the app feels **slower**.
- **Common doubt:** *Should k always be high?* No — start with a **middle value** (for example **5**), then tune if answers miss facts.

### Test the retriever before any LLM call

```python
user_question = "What is the annual revenue in the year 2022?"  # Sample finance question

retrieved_docs = retriever.get_relevant_documents(user_question)  # Embed query + top-k search in one call

for i, doc in enumerate(retrieved_docs, start=1):
    print(f"\n--- Chunk {i} ---")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print("Text preview:", doc.page_content[:200], "...")
```

**How the code works:**

- **`get_relevant_documents`** — LangChain handles **query embedding** and **similarity search** in one line.
- Each returned **`Document`** includes **`page_content`** and **`metadata`** for grounding audits.
- **Chunk distance** scores (when Chroma returns them) help you inspect **relevance** — useful for interpretability.

### Simple Activity — Retrieval-Only Check

Run the snippet above. Confirm at least one retrieved chunk contains the **2022 revenue figure** before you generate an answer. One sentence: what happens if you set **k = 1** for a question that needs facts from **two different pages**?

---

## Step 3 — Context Assembly with Delimiters

Raw chunk lists confuse the LLM. **Context assembly** wraps retrieved text in a **clear block** with **boundaries** and the **user question**.

- **Official Definition:** **Context assembly** (prompt augmentation) combines retrieved chunks, formatting rules, and the user question into one LLM input.
- **In Simple Words:** Build the **exam paper** — rules at top, **only allowed notes** in the middle, question at bottom.
- **Real-Life Example:** A **court brief** labels exhibits — the judge knows which document each line came from.

### Delimiter pattern used in class

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

### Build the context string

```python
def build_context_from_docs(retrieved_docs):
    """Join retrieved LangChain documents into one context string."""
    context_parts = []  # Collect plain text from each chunk
    for doc in retrieved_docs:
        context_parts.append(doc.page_content)  # Text of one retrieved chunk
    return "\n\n".join(context_parts)  # One block separated by blank lines


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

- **`build_context_from_docs`** — turns five chunk objects into one **context block**.
- **`{context}`** and **`{question}`** placeholders are filled at runtime with **`.format(...)`**.
- The LLM receives **one user message** containing both **evidence** and the **question**, separated by **`##`** labels.

---

## Step 4 — RAG System Message and Grounded Generation

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
- **Grounded generation** means the answer must come from **supplied context**, not the model’s general memory alone.

**Common mistake:** A generic assistant system message with **no grounding rules** — the model may answer from **pre-trained memory** instead of your PDF.

### Generate with Groq (Llama 3.3)

The live demo used **Groq** with **`llama-3.3-70b-versatile`** and **`temperature=0`** for deterministic RAG answers.

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

### Simple Activity — Multi-Step Finance Question

1. Ask: *"What is the total annual revenue across both 2022 and 2023?"*
2. Print retrieved chunks, then the generated answer.
3. Open the source PDF and **add the two year figures manually** — confirm the model **summed** numbers from context.
4. One sentence: why does this question need **k > 1**?

---

## Step 5 — End-to-End RAG Function

Wrap the full pipeline in one callable function — reuse the same pattern on the **Tesla** report and on the smaller **HR / Nestle** PDF.

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


def print_retrieval_trace(user_query, retrieved_docs):
    """Print chunks before generation — use for manual grounding review."""
    print("\n--- Retrieval trace ---")
    print("Query:", user_query)
    for i, doc in enumerate(retrieved_docs, start=1):
        print(f"\nChunk {i}")
        print("  source:", doc.metadata.get("source"))
        print("  page:", doc.metadata.get("page"))
        print("  text preview:", doc.page_content[:200], "...")


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
- **HR demo:** Same template with a different system persona (*Nestle / HR assistant*) and a **smaller PDF** — chunk size was reduced because the document was short.

---

## Informal Grounding Check — Verify Against Retrieved Text

Production systems use automated evaluators; in this session you **manually verify** that claims map back to retrieved text.

- **Official Definition:** An **informal grounding check** compares each factual claim in the LLM output to retrieved chunk text and source metadata.
- **In Simple Words:** **Fact-check the answer** against the paragraphs you pasted in.
- **Real-Life Example:** A **news fact-check desk** matches each headline claim to the **quoted paragraph**.

### Checklist (run after every demo answer)

| Check | How |
|---|---|
| **Claim in context?** | Every number or rule in the answer appears in **some retrieved chunk** |
| **Source traceable?** | Use chunk **metadata** (source PDF, **page** number) to locate the evidence |
| **No-context case** | Ask an **off-topic** question — model should say **I don't know**, not invent |
| **Chunk ↔ claim map** | Write: *"2022 revenue → Chunk 2, page 42"* in your notebook |

### Simple Activity — Grounding Audit

1. Query: *"What is the annual revenue in the year 2022?"*
2. Run **`print_retrieval_trace`**, then **`demo_rag_question`**.
3. Fill a two-column table: **Claim in answer** | **Which chunk + page supports it**.
4. Repeat with an **off-corpus** question — confirm the model **refuses** or says **I don't know**.

Formal scoring criteria (source fidelity, citation, refusal honesty, hallucination risk) and automated **RAG triad** judges are covered in **advanced work** later on the track.

---

## Without RAG vs With RAG — Why Retrieval Matters

Same question, two paths:

| Path | What happens |
|---|---|
| **Without RAG** | Plain LLM call — question only, **no retrieved context** |
| **With RAG** | Retrieve chunks first, then generate from the **context block** |

- **Without RAG**, the model may invent a **plausible-sounding** policy or revenue figure from **general training memory**.
- **With RAG**, the model must read **your PDF chunks** first — check numbers against the source file after generation.

When you practise, run the **same question** both ways and compare outputs. The live session used an **informal** check (open the PDF and verify) rather than a scripted dual-chain comparison loop.

![Grounding comparison — with retrieval cites the document correctly; without retrieval may invent a fluent wrong answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module3/session31/session31-grounding-comparison.png)

---

## Latency and Production Mindset

RAG is an **application** real users will wait on — not just a notebook exercise.

- **Retrieval time** grows when **k** is large — fetching **100 chunks** is slower than **5**.
- **Prompt size** grows with more chunks — the LLM takes longer to read a huge context block.
- **Trade-off:** You cannot always maximise **accuracy** and **speed** at the same time — tune **k** for your use case.

**Real-world examples discussed in class:**

- **Amazon Rufus** on product pages retrieves specs before answering feature questions — the same **retrieve-then-generate** pattern at ecommerce scale.
- **Product manuals** (AC, washing machine, refrigerator PDFs) can power a support assistant: load manuals into Chroma, then answer button / cycle questions from retrieved pages.
- **Bank statements** or personal PDFs — same template, but handle **sensitive data** carefully in production.

### Image embeddings (concept)

Pages can hold **figures** as well as text. **Image embeddings** turn a picture into a vector the same way text embeddings turn a paragraph into numbers. The text-only demos in this session do **not** load images — **multimodal RAG** is a natural extension once text RAG is solid.

---

## Common Mistakes and Fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Invented detail | Weak grounding instruction or no context | Strengthen system rules; check delimiters |
| "I don't know" but chunk exists | **k** too low or bad chunking | Raise **TOP_K**; revisit chunk size |
| Wrong page cited | Noisy retrieval | Lower **k** or improve chunks |
| Generic answer | Called LLM **without** context block | Use full **`rag_answer`** path |
| Slow responses | **k** too high | Lower **k** or filter metadata |
| Wrong matches | Different embedding model at query time | Use the **same GTE-large** model everywhere |

Fix **retrieval and prompt** before blaming the chat model.

---

## Key Takeaways

- **LangChain loaders and splitters** turn PDF folders into chunked **Document** objects with **metadata** — Tesla (~351 chunks at 512 chars) and a short HR PDF (64-char chunks) used the **same template**.
- **GTE-large embeddings + Chroma** store searchable vectors; **`get_relevant_documents`** connects the index to each user question with **top-k** retrieval (**k = 5** is a sensible start).
- **Delimiter-based context assembly** (`##context` / `##question`) and a **RAG system message** keep generation **grounded**; use **`temperature=0`** for stable answers.
- The **`rag_answer`** pattern runs **retrieve → augment → generate** imperatively — formal **LCEL pipe chains** are the next composition style on the track.
- **Informal grounding checks** (claim ↔ chunk map) and **without-RAG vs with-RAG** thinking prepare you for automated evaluation later.

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
| `PyPDFDirectoryLoader` | Class | Load all PDFs from a folder |
| `RecursiveCharacterTextSplitter` | Class | Split documents into overlapping chunks |
| `chunk_size` / `chunk_overlap` | Params | Max chunk length; shared margin between chunks |
| `HuggingFaceEmbeddings` + GTE-large | Embeddings | Sentence-transformer model used in live demos |
| `Chroma.from_documents` | Code | Build LangChain vector store from chunks |
| `vectorstore.as_retriever` | Code | Create searchable retriever from store |
| `GROQ_API_KEY` | Config | API key for Groq (env / Colab Secrets) |
| **MTEB leaderboard** | Reference | Benchmark ranking for embedding models |
| **Chunk distance** | Concept | Similarity score — useful for relevance inspection |
| **Latency trade-off** | Concept | Higher k → more context vs slower responses |
| **Image embeddings** | Concept | Encode pictures as vectors for multimodal search |
