# Retrieval & Grounding: Chunking & Metadata

## Introduction

In the **previous** lesson, you learnt that AI agents need **guardrails** because user text, retrieved text, and tool outputs can mislead the model.

Today we focus on another important RAG habit: retrieving the **right information**, answering only from that information, and **evaluating** whether a RAG system is trustworthy.

**RAG** means **Retrieval-Augmented Generation**.

- **Official Definition:** RAG is a method where an AI model retrieves useful documents before generating an answer.
- **In Simple Words:** The AI first checks notes, then answers.
- **Real-Life Example:** Before answering a college rule question, you open the rulebook instead of guessing.

**What you will learn:**

- Recap the **RAG pipeline** from documents to answers.
- Compare **fixed-size**, **recursive**, and **semantic** chunking.
- Use **metadata filters** for document type, product, date, and status.
- Add **source tags** for traceable citations.
- Evaluate answers with **LLM-as-judge** and the **RAG triad**.

![RAG retrieval and grounding overview showing an AI assistant retrieving trusted source pages before giving a cited answer while unsupported guesses are blocked](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session49/session49-01-retrieval-grounding-overview.png)

RAG quality depends on two things:

- The retriever must bring the right chunks.
- The model must answer only from those chunks.

If retrieval is weak, even a good prompt can give a wrong answer.

---

## RAG Architecture Recap

A RAG system follows a clear pipeline from raw documents to a final answer.

| Step | What happens |
|---|---|
| Documents | PDFs, manuals, policies, or reports enter the system |
| Chunking | A **chunker** splits documents into smaller text pieces |
| Embeddings | An **embedding model** converts each chunk into numbers |
| Vector DB | Chunks and embeddings are stored in a **vector database** |
| Retrieval | The user question finds similar chunks |
| Generation | An **LLM** writes an answer using retrieved context |

- **Official Definition:** A **vector database** stores unstructured data (text chunks and their embedding vectors) for similarity search.
- **In Simple Words:** It is a smart cupboard where each note has a number pattern so similar notes are easy to find.
- **Real-Life Example:** A library catalogue helps you reach the right shelf before you read the exact page.

In class we walked through this flow with an **ABB equipment user manual** — a real engineering document used to build a technician support RAG demo.

---

## Retrieval and Grounding

**Retrieval** is the step where the system searches stored knowledge and brings useful chunks.

- **Official Definition:** Retrieval means selecting relevant information from a stored collection based on a query.
- **In Simple Words:** It is like asking a librarian to bring the right page.
- **Real-Life Example:** If you ask for a laptop return rule, the staff should not bring a grocery return policy.

**Grounding** means the answer is supported by the retrieved sources.

- **Official Definition:** Grounding means making model outputs depend on verified context.
- **In Simple Words:** The AI should answer from the source, not from guesswork.
- **Real-Life Example:** In an exam, writing from the textbook is grounded; making up an answer is not grounded.

### Simple RAG Flow

| Step | What happens |
|---|---|
| User question | "Can I return a damaged laptop?" |
| Retrieval | Search stored policy chunks |
| Context | Bring laptop return policy |
| Generation | Model writes answer from that policy |
| Citation | Show the source file or section |

### Grounded vs Ungrounded

| Situation | Result |
|---|---|
| Retrieved text says "return within 10 days" | Grounded answer can say 10 days |
| No return policy is retrieved | Model should say information is not found |
| Old and new policies are both retrieved | Model may get confused |

**Important rule:**

> If the answer is not visible in the retrieved context, do not invent it.

### Activity — Check Grounding

For each answer, write **Grounded** or **Not Grounded**.

| Context | Answer |
|---|---|
| "Refunds take 7 working days." | "Refunds take 7 working days." |
| "Refunds take 7 working days." | "Refunds take 15 working days." |
| No context found | "Usually refunds take 10 days." |

---

## Chunks and Chunking

A RAG system usually does not store one full document as one searchable item.
It splits documents into smaller parts called **chunks**.

- **Official Definition:** A chunk is a smaller unit of text created from a larger document for indexing and retrieval.
- **In Simple Words:** A chunk is one useful piece from a big document.
- **Real-Life Example:** Instead of reading a full textbook, you read the exact page needed for your doubt.

![Chunking illustration showing a large course document split into focused knowledge pieces with a small overlap and a search beam selecting exact context](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session49/session49-02-chunking-document-pieces.png)

### Why Chunks Are Needed

Large documents create problems:

- Search may find the document but not the exact section.
- The model may receive too much text.
- Important lines may get lost inside noise.
- Cost can increase because too much context is sent.

| Document | Better chunking idea |
|---|---|
| FAQ page | One or two FAQs per chunk |
| Policy document | One policy section per chunk |
| Product manual | One feature or heading per chunk |
| Course notes | One concept per chunk |

### Chunk Size and Overlap

**Chunk size** means how much text is kept inside one chunk.

- **Official Definition:** Chunk size is the approximate amount of text stored in each chunk.
- **In Simple Words:** It decides whether the search result is a small note or a long page.
- **Real-Life Example:** A sticky note may be too small, but ten pages may be too much.

**Chunk overlap** means repeating a small part of one chunk in the next chunk.

- **Official Definition:** Overlap is shared text between neighbouring chunks.
- **In Simple Words:** The next chunk carries a little memory of the previous chunk.
- **Real-Life Example:** A teacher repeats the last point before starting the next topic.

| Chunk size | Benefit | Risk |
|---|---|---|
| Small | Very focused | May miss surrounding meaning |
| Medium | Balanced | Usually best starting point |
| Large | More context | More noise |

Overlap helps when an answer sits between two chunk boundaries.

### Fixed-Size and Recursive Text Splitting

In earlier demos (for example, a **Tesla** financial dataset), we used a **fixed-size chunker**.

- Every **512 characters** became one chunk.
- The next 512 characters became the next chunk, and so on.

In class we also used a **recursive character text splitter** on an **ABB PDF manual**:

- It still creates fixed-size pieces (512 characters).
- It tries to split at natural boundaries like paragraphs when possible.
- This is a common starting point because it is fast and easy to set up.

- **Common mistake:** Assuming one chunk size works for every document type.
- **Better habit:** Test chunk size on real manuals and policy PDFs before production.

### Semantic Chunking

**Semantic chunking** groups text by **meaning**, not by character count.

- **Official Definition:** Semantic chunking splits a document into chunks where neighbouring sentences share similar meaning, often using embedding similarity.
- **In Simple Words:** Related ideas stay together in one chunk, even if the chunk length varies.
- **Real-Life Example:** In a recipe book, all steps for one dish stay in one chunk instead of cutting mid-step at a fixed line count.

How it works at a high level:

1. Take the document text.
2. Create embeddings for sentences or small text blocks.
3. Merge blocks that are semantically similar.
4. Each merged group becomes one chunk.

| Approach | Speed | Accuracy | Best for |
|---|---|---|---|
| Fixed-size / recursive | Fast | Good starting point | Large corpora, first prototype |
| Semantic | Slower (more compute) | Often better retrieval | Manuals, technical docs, precise answers |

**Cost and latency trade-off:**

- Semantic chunking is **computationally intensive** — it takes more time during indexing, not more money by itself.
- At **inference time** (when a user asks a question), semantic chunks can help you retrieve **fewer but better** chunks, which may speed up the final answer.

In code, a semantic chunker can often replace a recursive splitter with a small change — the idea is the same pipeline, only the splitting logic changes.

- **Common mistake:** Using semantic chunking on every project without measuring indexing time.
- **Better habit:** Start with recursive splitting; move to semantic chunking when retrieval quality is not good enough.

---

## Indexing Time vs Inference Time

RAG work happens in two different phases.

| Phase | When | What happens |
|---|---|---|
| **Indexing time** | Once (with occasional maintenance) | Chunking, embedding, storing in vector DB |
| **Inference time** | Every user question | Retrieve chunks → LLM generates answer |

- **Official Definition:** **Indexing** is the offline process of preparing and storing searchable chunks; **inference** is the online process of answering a live user query.
- **In Simple Words:** Indexing is cooking the meal in advance; inference is serving it when the customer orders.
- **Real-Life Example:** A restaurant preps ingredients in the morning (indexing) but plates food only when you order (inference).

In class we demoed inference through a small **Gradio** RAG app — the user types a question and gets an answer from the indexed manual.

Chunking, embedding, and vector DB setup are usually **one-time** (or periodic) work.
Users only wait during **inference** — so both **accuracy** and **speed** matter at answer time.

---

## Industry Use Cases — Why Latency Matters

Accuracy alone is not enough for enterprise RAG.

Companies like **ABB**, **Siemens**, and **Cisco** use RAG on large equipment manuals.
A field technician cannot wait 15 seconds when a machine has failed.

| Industry | Real need | RAG challenge |
|---|---|---|
| ABB / industrial equipment | Urgent repair steps from manuals | Fast, accurate retrieval |
| Siemens (MRI / CT scanners) | Help during live hospital operations | Zero tolerance for slow answers |
| Railway signalling (Siemens) | Instant fault guidance | Huge document corpus |

- **Official Definition:** **Latency** is the delay between a user query and the final response.
- **In Simple Words:** How long the user stares at a loading screen.
- **Real-Life Example:** A patient is inside an MRI scanner — the technician needs the fix now, not after a long search.

**Two goals for production RAG:**

1. **Accuracy** — is the answer correct and grounded?
2. **Efficiency** — is the answer fast enough to use?

Metadata filters (covered next) help reduce search space and improve latency.

---

## Metadata in RAG

**Metadata** is extra information attached to a document or chunk.

- **Official Definition:** Metadata is descriptive data that gives information about another piece of data.
- **In Simple Words:** Metadata is a label.
- **Real-Life Example:** A library book has title, author, subject, and shelf number.

Metadata helps retrieval search in the correct area.

### Common Metadata Fields

| Field | Example | Use |
|---|---|---|
| `doc_type` | `policy` | Search only policy documents |
| `product` | `laptop` | Search only laptop content |
| `department` | `support` | Avoid HR or finance documents |
| `status` | `active` | Exclude old or draft content |
| `version` | `v2` | Track document edition |
| `year` | `2022` | Filter financial reports by year |
| `company_name` | `Tesla` | Narrow company-specific chunks |
| `source_file` | `laptop_policy.md` | Show citation |
| `page_number` | `12` | Point to PDF page |

### Metadata vs Content

| Item | Content | Metadata |
|---|---|---|
| Actual refund rule | Yes | No |
| Product name | Sometimes | Yes |
| Source file | No | Yes |
| Version | Sometimes | Yes |
| Section heading | Yes | Often yes |

- **Common mistake:** Keeping all labels only inside the text.
- **Better habit:** Store important labels as metadata so filters can use them.

---

## Metadata Filters

**Metadata filters** restrict retrieval to chunks with selected labels.

- **Official Definition:** A metadata filter is a structured condition applied during retrieval using metadata fields.
- **In Simple Words:** It says, "Search only this shelf."
- **Real-Life Example:** On a shopping app, you filter by brand, price, and rating before choosing a product.

Similarity search alone can bring related but wrong documents.
For example, "return window" may appear in mobile, laptop, grocery, old policy, and training documents.
A filter like `product = laptop` and `status = active` makes retrieval cleaner.

![Metadata filters visual showing a search lens selecting only active laptop version-two policy documents while archived and wrong-product documents are dimmed](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session49/session49-03-metadata-filtering-shelves.png)

### Two-Layer Retrieval

In class we discussed a **two-step** retrieval pattern:

1. **Metadata filter first** — narrow the corpus (like a SQL `WHERE` clause).
2. **Similarity search second** — find the best match only inside the filtered set.

| User question | Layer 1 — metadata filter | Layer 2 — similarity |
|---|---|---|
| "Can I return a damaged laptop?" (Amazon care) | `product = laptop`, `status = active` | Search return-policy chunks |
| "What is Tesla's annual revenue in 2022?" | `year = 2022` | Search revenue-related chunks |

Without filters, every question scans the **entire** vector DB — millions of chunks — which is slow.
With filters, you might search only 10–20 chunks, then rank by similarity.

- **Common mistake:** Relying only on embedding similarity when metadata clearly narrows the intent.
- **Better habit:** Combine structured filters with vector search for both speed and precision.

### Useful Filter Examples

| Need | Filter |
|---|---|
| Search policies only | `doc_type = "policy"` |
| Search laptop content | `product = "laptop"` |
| Use current documents | `status = "active"` |
| Avoid drafts | `status != "draft"` |
| Use latest version | `version = "v2"` |
| Financial year filter | `year = "2022"` |

### Activity — Choose the Filter

Write a suitable metadata filter for each question.

| User question | Metadata filter |
|---|---|
| "What is the billing rule for premium users?" | |
| "Show active return policy for mobiles." | |
| "What does the employee handbook say about leave?" | |
| "Find warranty steps from manuals only." | |

---

## Python Demo: Metadata Filtering

This simple code shows how metadata filtering works before ranking results.
Save as **`metadata_filter_demo.py`**:

```python
chunks = [  # Create a list to store searchable chunks.
    {  # Start the first chunk.
        "text": "Mobiles can be returned within 7 days if damaged.",  # Store mobile policy text.
        "metadata": {  # Store labels for this chunk.
            "doc_type": "policy",  # Mark this as a policy document.
            "product": "mobile",  # Mark this chunk as mobile-related.
            "status": "active",  # Mark this policy as active.
            "source_file": "mobile_policy.md",  # Store the source file name.
        },  # End metadata.
    },  # End first chunk.
    {  # Start the second chunk.
        "text": "Laptops can be returned within 10 days for defects.",  # Store laptop policy text.
        "metadata": {  # Store labels for this chunk.
            "doc_type": "policy",  # Mark this as a policy document.
            "product": "laptop",  # Mark this chunk as laptop-related.
            "status": "active",  # Mark this policy as active.
            "source_file": "laptop_policy.md",  # Store the source file name.
        },  # End metadata.
    },  # End second chunk.
    {  # Start the third chunk.
        "text": "Laptops were earlier returnable within 30 days.",  # Store old policy text.
        "metadata": {  # Store labels for this old chunk.
            "doc_type": "policy",  # Mark this as a policy document.
            "product": "laptop",  # Mark this chunk as laptop-related.
            "status": "archived",  # Mark this policy as old.
            "source_file": "old_laptop_policy.md",  # Store the old source file name.
        },  # End metadata.
    },  # End third chunk.
]  # End chunks list.


def matches_filters(metadata, filters):  # Define a function to check metadata filters.
    for key, value in filters.items():  # Loop through every filter condition.
        if metadata.get(key) != value:  # Compare chunk metadata with expected value.
            return False  # Reject the chunk when one condition fails.
    return True  # Accept the chunk when all conditions match.


def retrieve(filters):  # Define a simple retrieval function.
    results = []  # Create an empty list for matching chunks.
    for chunk in chunks:  # Check every stored chunk.
        if matches_filters(chunk["metadata"], filters):  # Apply metadata filters first.
            results.append(chunk)  # Add the matching chunk to results.
    return results  # Return filtered results.


filters = {"doc_type": "policy", "product": "laptop", "status": "active"}  # Choose safe filters.
retrieved_chunks = retrieve(filters)  # Retrieve chunks using filters.

for chunk in retrieved_chunks:  # Loop through retrieved chunks.
    print(chunk["text"])  # Print the answer context.
    print("Source:", chunk["metadata"]["source_file"])  # Print the source for citation.
```

### How the Code Works

- `chunks` is a small sample knowledge base.
- Every chunk has `text` and `metadata`.
- `matches_filters()` checks all filter conditions.
- `retrieve()` searches only chunks that pass the filters.
- The archived laptop policy is ignored because `status` must be `active`.

In real apps, the same filter idea is used with vector databases.

---

## Source Tagging and Citations

**Source tagging** means storing source details with each chunk.

- **Official Definition:** Source tagging is the practice of attaching source identifiers to chunks for traceability and citations.
- **In Simple Words:** Every answer should know where it came from.
- **Real-Life Example:** In an assignment, you mention the textbook or website used.

Source tags help users trust the answer and help developers debug wrong answers.
In class we discussed storing **file name**, **page number**, **topic**, and a **reference back to the original document** in the vector DB.

### Useful Source Tags

| Field | Example | Use |
|---|---|---|
| `source_file` | `refund_policy.md` | Shows original file |
| `source_url` | `https://example.com/policy` | Shows link |
| `section_title` | `Refund Timeline` | Shows exact section |
| `page_number` | `12` | Helps for PDFs |
| `topic` | `Motor Control Mode` | Groups manual sections |

### Simple Citation Format

```text
Answer: Laptops can be returned within 10 days for manufacturing defects.
Source: laptop_policy.md - Return Rules
```

- **Common mistake:** Letting the model invent citations.
- **Better habit:** Show citations from stored metadata only.

---

## Vector DB Maintenance and Version Control

When source documents change, the vector DB must stay in sync.
This is usually an **administration task** handled by database or platform teams.

| Document change | Typical action |
|---|---|
| New document added | Add new chunks to the vector DB |
| Document updated | Re-chunk and re-index affected content |
| Document removed | Delete related chunks from the vector DB |

Vector DBs often store a **reference** to the original document in chunk metadata.
If the source file disappears but chunks remain, the bot may answer from stale text.

### Git and Persisted Vector DB Files

If you persist a local vector DB folder in a project, Git may show files as modified even when content did not meaningfully change — internal index metadata and timestamps can update on read.

- **Better habit:** Add the persisted vector DB directory to **`.gitignore`** unless you intentionally version database files.
- **In Simple Words:** Do not commit a live database folder like normal source code.

---

## Evaluating RAG Quality — LLM as Judge

Building a RAG demo is easy.
Knowing whether answers are **correct and reliable** is the hard part.

**LLM-as-judge** uses a **second LLM** to rate the first LLM's RAG answer.

- **Official Definition:** LLM-as-judge is an evaluation method where one language model scores another model's output against defined quality metrics.
- **In Simple Words:** Like a dance competition — one performer, one judge with a scorecard.
- **Real-Life Example:** A teacher marks an answer sheet using a fixed rubric, not personal guesswork.

### Two Judges Used in Class

| Judge | What it checks | Example |
|---|---|---|
| **Groundedness judge** | Is the answer supported by retrieved context? | Answer must come from the manual, not general knowledge |
| **Relevance judge** | Is the answer relevant to the question given the context? | If you ask for **revenue**, the answer should not discuss **profit** only |

### How the Judge Works

1. User asks a question.
2. RAG retrieves context and generates an answer (first LLM).
3. Judge LLM receives **question + context + answer**.
4. Judge returns a **star rating** (1–5) and short reasoning.

| Star rating | Meaning (groundedness) |
|---|---|
| 1 | Answer ignores or contradicts context |
| 5 | Answer is fully derived from context |

- **Common mistake:** Using the same small model as both answer generator and judge.
- **Better habit:** Use a **stronger judge model** than the main RAG model when possible.

### Judge System Message Pattern

The judge is briefed through a **system message** — like instructions given to a competition judge.

Key rule in the groundedness prompt:

> The answer should be derived **only** from the information present in the context.

In the ABB manual demo, both judges gave **5-star** ratings when retrieval and generation aligned — a sign the pipeline was working for that test question.

---

## RAG Triad

In interviews and production debugging, teams often discuss three linked metrics — the **RAG triad**.

| Metric | Direction | Question it answers |
|---|---|---|
| **Context relevance** | Query → Context | Did retrieval bring the **right** chunks for this question? |
| **Groundedness** | Context → Response | Is the answer **supported** by those chunks? |
| **Answer relevance** | Query → Response | Is the answer **on-topic** for what was asked? |

- **Official Definition:** The **RAG triad** is a framework that evaluates retrieval quality, grounding fidelity, and answer relevance as separate checks.
- **In Simple Words:** Three doors — if the wrong context enters, nothing downstream can be fully trusted.
- **Real-Life Example:** In an exam, you must pick the right textbook page (context relevance), copy facts from it (groundedness), and answer the exact question asked (relevance).

**Why context relevance matters:**

- Low groundedness may mean bad generation **or** bad retrieval.
- Low context relevance points to **chunking**, **embeddings**, **filters**, or **search** — fix retrieval before blaming the prompt.

When a judge score drops, ask which leg of the triad failed.

---

## Human Evaluation Workflow

Automated judges scale well, but companies still use **human evaluators** for edge cases.

A workflow similar to **ChatGPT** internal quality checks:

1. RAG (or chat) model generates a response.
2. Judge LLM scores the response (1–5 stars).
3. Low scores (1–2) may be sent to **human experts** for review.
4. User **thumbs up / thumbs down** can provide extra feedback signals.

- **Official Definition:** **Human evaluation** is manual review of model outputs by trained reviewers against quality guidelines.
- **In Simple Words:** A senior teacher rechecks answers the auto-grader was unsure about.
- **Real-Life Example:** Customer support escalates only the tickets the bot could not handle confidently.

Human review is slower but catches subtle errors automated judges miss.

---

## Debugging Retrieval Problems

When a RAG answer is wrong, first inspect retrieval.
Do not immediately blame the final prompt.

### Debugging Questions

- What chunks were retrieved?
- Which metadata filters were applied?
- Were archived chunks included?
- Did the top chunk contain the answer?
- Was the source document recently updated?
- Did citations come from metadata?
- What did the **groundedness** and **relevance** judges score?
- Is **context relevance** low — pointing to a retrieval problem?

### Common Symptoms

| Symptom | Likely cause | First fix |
|---|---|---|
| Old answer | Stale chunks in vector DB | Re-index with admin team |
| Wrong product | Missing product filter | Add product metadata |
| No citation | Missing source tags | Store source metadata |
| Guessing | Weak prompt | Add no-context fallback |
| Mixed answer | Conflicting chunks | Improve filters and chunking |
| Slow answers | Full-corpus search | Add metadata filters first |

Retrieval debugging is like checking ingredients before blaming the cook.
Wrong context usually creates wrong answers.

---

## Mini Project

Design a grounded RAG plan for ecommerce, college policy, HR, banking, or healthcare.
Fill this table:

| Item | Your plan |
|---|---|
| Bot use case | |
| Source documents | |
| Chunking approach | |
| Metadata fields | |
| Filters needed | |
| Citation format | |
| Evaluation metrics (RAG triad) | |

Example:

| Item | Example |
|---|---|
| Bot use case | College course policy bot |
| Source documents | Attendance policy, grading policy |
| Chunking approach | Recursive 512-char chunks or semantic for long PDFs |
| Metadata fields | `doc_type`, `status`, `version`, `source_file` |
| Filters needed | `doc_type = policy`, `status = active` |
| Citation format | `Source: grading_policy.md - Late Submissions` |
| Evaluation metrics | Context relevance, groundedness, answer relevance |

---

## Key Takeaways

- **Grounding** means the answer should be supported by retrieved source material — never invent facts missing from context.
- **Chunking** choices (fixed-size, recursive, semantic) affect retrieval quality, indexing time, and answer latency.
- **Metadata filters** narrow the search space before similarity search — like a SQL `WHERE` clause plus vector ranking.
- **Source tagging** makes citations traceable and helps debug wrong answers.
- **LLM-as-judge** and the **RAG triad** help you measure whether retrieval, grounding, and relevance are working before you trust a production bot.

In the next learning step, these habits will help you build RAG systems that are easier to test, explain, and improve.

---

## Important Commands, Libraries, Terminologies Used

| Term or item | Meaning |
|---|---|
| **RAG** | Retrieval-Augmented Generation |
| **Retrieval** | Searching stored information for useful context |
| **Grounding** | Answering only from verified retrieved sources |
| **Chunk** | Smaller searchable part of a document |
| **Chunk size** | Amount of text in one chunk |
| **Chunk overlap** | Shared text between nearby chunks |
| **Recursive text splitter** | Chunker that splits at natural boundaries when possible |
| **Semantic chunking** | Chunking by meaning similarity using embeddings |
| **Indexing time** | Offline phase — chunk, embed, store |
| **Inference time** | Online phase — retrieve and generate answer |
| **Latency** | Delay between user question and final answer |
| **Metadata** | Labels attached to chunks |
| **Metadata filter** | Condition used to search selected chunks |
| **Two-layer retrieval** | Metadata filter first, then similarity search |
| **Source tagging** | Storing source details with chunks |
| **Citation** | Visible source reference for an answer |
| **Vector DB** | Database storing chunks and embedding vectors |
| **LLM-as-judge** | Second LLM that scores RAG answer quality |
| **Groundedness** | Whether answer is supported by retrieved context |
| **Answer relevance** | Whether answer matches the user question |
| **Context relevance** | Whether retrieved chunks match the query |
| **RAG triad** | Context relevance + groundedness + answer relevance |
| **Human evaluation** | Manual review of low-scoring model outputs |
| **Gradio** | Python library for quick RAG UI demos |
| `.gitignore` | File list telling Git which folders not to track |
| `doc_type` | Metadata field for document type |
| `product` | Metadata field for product category |
| `status` | Metadata field for active, draft, or archived state |
| `version` | Metadata field for document edition |
| `source_file` | Metadata field for original file name |
| `metadata_filter_demo.py` | Demo for filter-first retrieval |
