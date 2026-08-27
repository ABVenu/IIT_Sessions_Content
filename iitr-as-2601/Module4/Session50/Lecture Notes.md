# Retrieval & Grounding: Hands-On Improvement

## Introduction

In the **previous** session you improved RAG reliability with **chunking choices**, **metadata filters**, **source tags**, and evaluation ideas such as the **RAG triad** and **LLM-as-judge**.

You already know how to **retrieve** top-k chunks and **generate** grounded answers from context. This session is different: you practise **improving** retrieval quality on a **fixed eval set**, without advanced search stacks.

**What you will learn:**

- Build a small set of **questions** with **expected supporting documents**
- Experiment with **top-k** and **chunk parameters** and record **retrieval hit rate** informally
- Classify failures as **retrieval** vs **generation** and choose the right fix
- Show **measurable improvement** on at least two failing questions (before vs after)

Treat this lesson as a **tuning lab**, not a rebuild lab. The pipeline stays simple. The skill is **measure → change one knob → measure again**.

---

## Why a Fixed Eval Set Matters

If you only test with random questions each time, you cannot tell whether a change helped.

- **Official Definition:** A **fixed eval set** is a stable list of test questions and expected evidence used to compare RAG behaviour before and after a change.
- **In Simple Words:** Same exam paper every time — so marks can go up or down for a real reason.
- **Real-Life Example:** A cricket coach does not invent a new drill every day and claim the team improved. The coach uses the **same practice test** and tracks scores.

Without a fixed set:

- You may “fix” one question and break another without noticing
- You argue from memory instead of numbers
- You cannot show a **before/after** story to a teammate or interviewer

With a fixed set:

- Every experiment uses the **same questions**
- You record **hit / miss** for retrieval
- You can prove improvement on **specific failures**

**Common mistake:** Changing `k`, chunk size, and the prompt all at once. You will not know which change helped.

**Better habit:** Change **one parameter family at a time**, then re-run the same eval set.

---

## Build a Mini Knowledge Base for Tuning

For this lab we use a **small, fixed corpus** so every student can measure the same things. You do not need a large PDF or a production vector stack.

- **Official Definition:** A **corpus** is the collection of documents (or chunks) your retriever searches.
- **In Simple Words:** The notebook’s “library shelf” for these experiments.
- **Real-Life Example:** A hostel notice board with five pinned policies — small enough to check by hand.

### Sample corpus — CampusHelp policies

| Doc ID | Title | Full text (short) |
|---|---|---|
| `D1` | Attendance Policy | Students must maintain at least 75% attendance. Below 75%, the student cannot sit for the end-term exam unless a medical certificate is approved by the dean. |
| `D2` | Late Submission Policy | Assignments submitted up to 2 days late receive a 10% penalty per day. Submissions after 2 days are not accepted. |
| `D3` | Library Hours | The main library is open Monday to Saturday from 8 AM to 10 PM. It is closed on Sundays and public holidays. |
| `D4` | Hostel Mess Refund | Mess fees are refundable only if a student applies at least 7 days before leaving the hostel. Same-day refunds are not allowed. |
| `D5` | Wi-Fi Access | Campus Wi-Fi is available to enrolled students using college email login. Guests need a temporary pass from the IT desk. |

These five documents are enough to build questions, expected evidence, and failure cases.

```python
# Mini corpus for retrieval tuning experiments
CORPUS = [
    {
        "doc_id": "D1",  # Stable id used in the eval set
        "title": "Attendance Policy",
        "text": (
            "Students must maintain at least 75% attendance. "
            "Below 75%, the student cannot sit for the end-term exam "
            "unless a medical certificate is approved by the dean."
        ),
    },
    {
        "doc_id": "D2",
        "title": "Late Submission Policy",
        "text": (
            "Assignments submitted up to 2 days late receive a 10% penalty per day. "
            "Submissions after 2 days are not accepted."
        ),
    },
    {
        "doc_id": "D3",
        "title": "Library Hours",
        "text": (
            "The main library is open Monday to Saturday from 8 AM to 10 PM. "
            "It is closed on Sundays and public holidays."
        ),
    },
    {
        "doc_id": "D4",
        "title": "Hostel Mess Refund",
        "text": (
            "Mess fees are refundable only if a student applies at least 7 days "
            "before leaving the hostel. Same-day refunds are not allowed."
        ),
    },
    {
        "doc_id": "D5",
        "title": "Wi-Fi Access",
        "text": (
            "Campus Wi-Fi is available to enrolled students using college email login. "
            "Guests need a temporary pass from the IT desk."
        ),
    },
]
```

**How the code works:**

- Each item has a **`doc_id`** so the eval set can name the expected document clearly.
- **`text`** is the searchable content — later we will also split it into chunks for parameter experiments.
- Keep this list **unchanged** while you tune retrieval settings.

---

## Build Questions with Expected Supporting Documents

An eval item is not only a question. It also names **which document should support the answer**.

- **Official Definition:** An **expected supporting document** is the source (or sources) that must appear in retrieval for a question to count as a retrieval success.
- **In Simple Words:** You write the question **and** the correct library shelf label.
- **Real-Life Example:** For “What time does the library close?”, the expected support is the **Library Hours** notice — not the Wi-Fi notice.

### Eval set design rules

| Rule | Why it matters |
|---|---|
| Keep the set small (5–8 questions) | Easy to score by hand in class |
| Mix easy and hard questions | Easy ones check the pipeline; hard ones expose tuning needs |
| Write **expected `doc_id`s** before you run retrieval | Avoids “I think this chunk is fine” bias |
| Include at least one **no-answer** question | Checks that missing evidence is handled honestly |
| Freeze the set before experiments | Otherwise scores are not comparable |

### Sample fixed eval set

| Q ID | Question | Expected doc IDs | Notes |
|---|---|---|---|
| `Q1` | What is the minimum attendance required? | `D1` | Direct fact |
| `Q2` | Can I submit an assignment 1 day late? | `D2` | Needs penalty rule |
| `Q3` | Is the library open on Sunday? | `D3` | Closed-day rule |
| `Q4` | How do I get a mess fee refund? | `D4` | 7-day rule |
| `Q5` | Can a guest use campus Wi-Fi? | `D5` | Temporary pass rule |
| `Q6` | What is the hostel room rent? | *(none)* | Not in corpus — should miss retrieval support |

```python
# Fixed eval set — do not edit during experiments
EVAL_SET = [
    {
        "qid": "Q1",
        "question": "What is the minimum attendance required?",
        "expected_docs": ["D1"],  # Must retrieve attendance policy
    },
    {
        "qid": "Q2",
        "question": "Can I submit an assignment 1 day late?",
        "expected_docs": ["D2"],
    },
    {
        "qid": "Q3",
        "question": "Is the library open on Sunday?",
        "expected_docs": ["D3"],
    },
    {
        "qid": "Q4",
        "question": "How do I get a mess fee refund?",
        "expected_docs": ["D4"],
    },
    {
        "qid": "Q5",
        "question": "Can a guest use campus Wi-Fi?",
        "expected_docs": ["D5"],
    },
    {
        "qid": "Q6",
        "question": "What is the hostel room rent?",
        "expected_docs": [],  # No supporting doc in corpus
    },
]
```

**How the code works:**

- **`expected_docs`** is the gold label for retrieval success.
- **`Q6`** has an empty list — success means **not** pretending a policy exists.
- You will score retrieval against this list, not against “does the answer sound nice?”

### Activity — Write Two Extra Eval Items

Add two more questions for CampusHelp in your notebook:

1. One **easy** question with a clear expected `doc_id`
2. One **tricky** question where wording differs from the document title

Write them in this format:

| Q ID | Question | Expected doc IDs |
|---|---|---|
| `Q7` | | |
| `Q8` | | |

Do not change `Q1`–`Q6` after you start experiments.

---

## Informal Retrieval Hit Rate

Before you tune anything, you need a simple score for retrieval quality.

- **Official Definition:** **Retrieval hit rate** is the share of eval questions where at least one expected supporting document appears in the top-k retrieved results.
- **In Simple Words:** “Out of 5 answerable questions, how many times did the right note land in the top results?”
- **Real-Life Example:** If a librarian brings five folders and the correct policy is among them, that question is a **hit**. If not, it is a **miss**.

### Scoring rules used in this lab

| Case | Hit? |
|---|---|
| Expected doc is in top-k | **Hit** |
| Expected doc is missing from top-k | **Miss** |
| Question has no expected docs (`Q6`) | Score separately as **correct miss** if no policy-like doc is forced into an answer later |

For answerable questions (`Q1`–`Q5`):

**Hit rate = (number of hits) / (number of answerable questions)**

Example: 3 hits out of 5 → hit rate = **0.60 (60%)**.

This is **informal** on purpose. You are not building a full evaluation platform. You are learning to **measure before you tune**.

```python
def is_hit(retrieved_doc_ids, expected_docs):
    """Return True if any expected doc appears in retrieved ids."""
    if not expected_docs:  # No-answer questions are scored separately
        return None  # Do not count them in the main hit-rate formula
    return any(doc_id in retrieved_doc_ids for doc_id in expected_docs)  # Hit if any gold doc is present


def retrieval_hit_rate(results):
    """Return hit rate for answerable questions only."""
    answerable = [r for r in results if r["expected_docs"]]  # Keep only questions with gold docs
    if not answerable:  # Guard against empty eval sets
        return 0.0  # No answerable questions means no rate to report
    hits = sum(  # Count successful retrievals
        1  # Add one for each hit
        for r in answerable  # Walk every answerable row
        if is_hit(r["retrieved_doc_ids"], r["expected_docs"])  # Check gold overlap
    )
    return hits / len(answerable)  # Informal hit rate between 0 and 1
```

**How the code works:**

- **`is_hit`** checks overlap between retrieved ids and expected ids.
- **`retrieval_hit_rate`** ignores no-answer questions so they do not inflate or deflate the main score.
- Print both the **rate** and the **per-question hit/miss table** — the table is what you debug from.

### Activity — Score a Manual Trace

Suppose top-3 retrieval for five questions returned:

| Q ID | Retrieved docs | Expected | Hit? |
|---|---|---|---|
| Q1 | D1, D5, D3 | D1 | |
| Q2 | D5, D3, D1 | D2 | |
| Q3 | D3, D1, D5 | D3 | |
| Q4 | D2, D5, D1 | D4 | |
| Q5 | D5, D1, D3 | D5 | |

Fill **Hit?** for each row, then compute hit rate.

---

## Simple Retriever for Experiments

You already practised vector retrieval and grounded generation earlier on this track. Here we use a **lightweight keyword retriever** so you can focus on the improvement loop without advanced search stacks.

- **Official Definition:** A **keyword retriever** ranks documents by how many query words appear in the document text.
- **In Simple Words:** Count overlapping words and pick the top matches.
- **Real-Life Example:** Searching a notice board for the word “refund” and reading the notices that mention it most.

This is enough to practise **top-k**, **chunking parameters**, **hit rate**, and **failure classification**.

```python
import re  # Split text into simple word tokens


def tokenize(text):
    """Lowercase and split text into word tokens."""
    return re.findall(r"[a-z0-9]+", text.lower())  # Keep only letters and digits


def score_doc(query, doc_text):
    """Count how many query tokens appear in the document text."""
    query_tokens = set(tokenize(query))  # Unique words from the question
    doc_tokens = set(tokenize(doc_text))  # Unique words from the document
    if not query_tokens:  # Empty query cannot match anything
        return 0  # Lowest possible score
    return len(query_tokens & doc_tokens)  # Shared-word count as relevance score


def retrieve_top_k(query, corpus, k=3):
    """Return top-k corpus items ranked by keyword overlap."""
    ranked = []  # Collector for scored documents
    for doc in corpus:  # Score every document in the corpus
        ranked.append(  # Store id, text, and score together
            {
                "doc_id": doc["doc_id"],  # Parent document id for hit scoring
                "title": doc["title"],  # Human-readable label for debugging
                "text": doc["text"],  # Text that may enter the answer context
                "score": score_doc(query, doc["text"]),  # Keyword overlap score
            }
        )
    ranked.sort(key=lambda item: item["score"], reverse=True)  # Highest score first
    return ranked[:k]  # Keep only the top-k results
```

**How the code works:**

- **`tokenize`** removes punctuation and lowercases text so `"Sunday?"` matches `"sunday"`.
- **`score_doc`** counts shared words — a simple relevance signal.
- **`retrieve_top_k`** sorts by score and keeps only the top **`k`** results.

You can later swap this function for a vector retriever. The **eval set and hit-rate method stay the same**.

---

## Baseline Run — Record Before Scores

Improvement needs a **baseline**. Run the fixed eval set once with default settings and write the numbers down.

Default settings for the first run:

| Knob | Baseline value |
|---|---|
| `k` | `3` |
| Chunking | Off (whole document as one unit) |
| Prompt | Simple grounded prompt |

```python
def run_retrieval_eval(eval_set, corpus, k=3):
    """Run retrieval for every eval question and return detailed rows."""
    rows = []
    for item in eval_set:
        retrieved = retrieve_top_k(item["question"], corpus, k=k)
        retrieved_ids = [r["doc_id"] for r in retrieved]
        hit = is_hit(retrieved_ids, item["expected_docs"])
        rows.append(
            {
                "qid": item["qid"],
                "question": item["question"],
                "expected_docs": item["expected_docs"],
                "retrieved_doc_ids": retrieved_ids,
                "hit": hit,
            }
        )
    return rows


baseline_rows = run_retrieval_eval(EVAL_SET, CORPUS, k=3)
baseline_hit_rate = retrieval_hit_rate(baseline_rows)

print("Baseline hit rate:", round(baseline_hit_rate, 2))
for row in baseline_rows:
    print(row["qid"], "hit=", row["hit"], "retrieved=", row["retrieved_doc_ids"])
```

**How the code works:**

- One function runs the **whole eval set** so experiments stay consistent.
- You print **per-question** results, not only the average.
- Save this output as **Before** in your notebook or a small table.

### Baseline log template

| Setting | Value |
|---|---|
| `k` | 3 |
| Chunk size | whole doc |
| Hit rate (Q1–Q5) | |
| Missed questions | |

---

## Top-k Experiments

**Top-k** controls how many documents enter the context window.

- **Official Definition:** **Top-k** is the number of highest-ranked items returned by the retriever.
- **In Simple Words:** How many notes you allow the model to read.
- **Real-Life Example:** Bringing 1 folder vs 5 folders to a meeting.

You practised choosing `k` when you first wired retrieval into prompts. Today you **measure** what each `k` does on the same eval set.

| `k` | Possible benefit | Possible risk |
|---|---|---|
| 1 | Very focused | Easy to miss the right doc if ranking is imperfect |
| 3 | Balanced starting point | May still miss a lower-ranked support doc |
| 5 | Higher chance of a hit on small corpora | More noise for generation |

```python
def compare_k_values(eval_set, corpus, k_values):
    """Compare informal hit rate across several k settings."""
    report = []
    for k in k_values:
        rows = run_retrieval_eval(eval_set, corpus, k=k)
        report.append(
            {
                "k": k,
                "hit_rate": retrieval_hit_rate(rows),
                "rows": rows,
            }
        )
    return report


k_report = compare_k_values(EVAL_SET, CORPUS, k_values=[1, 3, 5])
for item in k_report:
    print("k=", item["k"], "hit_rate=", round(item["hit_rate"], 2))
```

**How the code works:**

- The same **`EVAL_SET`** is reused for every `k`.
- You compare **hit rates**, then inspect which questions flipped from miss to hit.
- Pick the smallest `k` that keeps the hits you need — larger is not always better for generation quality.

### Activity — Top-k Table

Fill this table from your notebook run:

| `k` | Hit rate | Questions that still miss |
|---|---|---|
| 1 | | |
| 3 | | |
| 5 | | |

Write one sentence: which `k` would you keep for CampusHelp and why?

---

## Chunk Parameter Experiments

Whole documents are easy when texts are short. Real policies are longer, so you split them into **chunks** and tune **chunk size** and **overlap**.

You already compared chunking styles earlier. Here the new skill is **measuring** chunk settings with hit rate on a fixed set.

- **Official Definition:** **Chunk parameters** are settings such as chunk size and overlap that control how documents are split before retrieval.
- **In Simple Words:** How big each note card is, and whether neighbouring cards share a few lines.
- **Real-Life Example:** Cutting a long hostel rulebook into page-sized cards; if a rule sits on the cut line, a little overlap keeps the full rule on at least one card.

### Create chunks from the corpus

```python
def chunk_text(text, chunk_size=40, overlap=10):
    """Split text into overlapping word windows for this lab."""
    words = text.split()  # Work in words so sizes are easy to reason about
    if chunk_size <= 0:  # Invalid size would create an infinite loop risk
        raise ValueError("chunk_size must be positive")  # Fail fast with a clear message
    if overlap >= chunk_size:  # Overlap must leave the window moving forward
        raise ValueError("overlap must be smaller than chunk_size")  # Prevent stuck starts

    chunks = []  # Collector for chunk strings
    start = 0  # Start index of the current window
    while start < len(words):  # Keep slicing until the document ends
        end = start + chunk_size  # End index of the current window
        piece = " ".join(words[start:end])  # Rebuild one chunk as text
        chunks.append(piece)  # Store the chunk
        if end >= len(words):  # Stop when the last words are included
            break  # No more windows needed
        start = end - overlap  # Move forward but keep shared words
    return chunks  # List of overlapping text pieces


def build_chunk_corpus(corpus, chunk_size=40, overlap=10):
    """Turn documents into searchable chunks with parent doc ids."""
    chunk_corpus = []  # New searchable collection built from chunks
    for doc in corpus:  # Process every parent document
        pieces = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)  # Split one doc
        for i, piece in enumerate(pieces, start=1):  # Number chunks inside the parent doc
            chunk_corpus.append(  # Each chunk becomes one retrieval unit
                {
                    "doc_id": doc["doc_id"],  # Parent document id for hit scoring
                    "chunk_id": f"{doc['doc_id']}-C{i}",  # Unique chunk label for debugging
                    "title": doc["title"],  # Keep the policy title for traces
                    "text": piece,  # Searchable chunk body
                }
            )
    return chunk_corpus  # Ready for retrieve_top_k and hit-rate scoring
```

**How the code works:**

- **`chunk_text`** walks through words with a sliding window.
- **`overlap`** keeps shared words between neighbours so a rule is less likely to be split badly.
- **`doc_id`** stays on every chunk so hit rate still checks the **parent document**.

### Compare chunk settings

```python
def compare_chunk_settings(eval_set, corpus, settings, k=3):
    """Compare hit rate for different chunk_size and overlap values."""
    report = []
    for setting in settings:
        chunk_corpus = build_chunk_corpus(
            corpus,
            chunk_size=setting["chunk_size"],
            overlap=setting["overlap"],
        )
        rows = run_retrieval_eval(eval_set, chunk_corpus, k=k)
        report.append(
            {
                "chunk_size": setting["chunk_size"],
                "overlap": setting["overlap"],
                "num_chunks": len(chunk_corpus),
                "hit_rate": retrieval_hit_rate(rows),
                "rows": rows,
            }
        )
    return report


chunk_settings = [
    {"chunk_size": 12, "overlap": 2},   # Small chunks
    {"chunk_size": 20, "overlap": 5},   # Medium chunks
    {"chunk_size": 40, "overlap": 10},  # Larger chunks
]

chunk_report = compare_chunk_settings(EVAL_SET, CORPUS, chunk_settings, k=3)
for item in chunk_report:
    print(
        "size=", item["chunk_size"],
        "overlap=", item["overlap"],
        "chunks=", item["num_chunks"],
        "hit_rate=", round(item["hit_rate"], 2),
    )
```

**How the code works:**

- Each setting rebuilds the searchable units, then reuses the **same eval set**.
- You record **hit rate** and **number of chunks** — more chunks are not automatically better.
- Keep `k` fixed while you change chunk settings so you isolate one variable family.

### Activity — Chunk Setting Log

| Chunk size | Overlap | Number of chunks | Hit rate | Notes |
|---|---|---|---|---|
| 12 | 2 | | | |
| 20 | 5 | | | |
| 40 | 10 | | | |

Circle the setting you will use as your **improved retrieval config**.

---

## Failure Analysis — Retrieval vs Generation

A wrong final answer is not always a generation problem.

- **Official Definition:** **Failure analysis** is the process of classifying why a RAG answer failed so you apply the correct fix.
- **In Simple Words:** Decide whether the library brought the wrong page, or the writer misread the right page.
- **Real-Life Example:** If a clerk quotes the wrong notice, that is a retrieval problem. If the clerk has the right notice but still invents a rule, that is a generation problem.

### Two failure types

| Failure type | What you observe | What it means |
|---|---|---|
| **Retrieval failure** | Expected doc is missing from top-k | The model never saw the evidence |
| **Generation failure** | Expected doc is present, but answer is wrong, incomplete, or invented | Evidence was available; writing step failed |

Use this decision tree:

1. Look at **retrieved ids** for the question.
2. If expected support is missing → **retrieval failure**.
3. If expected support is present → check the answer against that text.
4. If the answer is unsupported or wrong → **generation failure**.

```python
def classify_failure(expected_docs, retrieved_doc_ids, answer_text, source_texts):
    """
    Classify one failing question.
    source_texts: list of retrieved texts joined for a simple support check.
    """
    if expected_docs and not is_hit(retrieved_doc_ids, expected_docs):
        return "retrieval_failure"

    # Very simple support check for the lab:
    # if answer claims a number/word that never appears in retrieved text, flag generation.
    answer_tokens = set(tokenize(answer_text))
    source_tokens = set(tokenize(" ".join(source_texts)))
    unsupported = answer_tokens - source_tokens

    # Ignore tiny grammar words for this informal check
    stopwords = {"the", "a", "an", "is", "are", "to", "of", "and", "or", "in", "for"}
    unsupported = {token for token in unsupported if token not in stopwords and len(token) > 2}

    if unsupported:
        return "generation_failure"

    return "needs_manual_review"
```

**How the code works:**

- Missing expected docs are labelled **`retrieval_failure`** immediately.
- If docs are present, a lightweight token check looks for answer words absent from context.
- **`needs_manual_review`** is honest — informal checks cannot catch every subtle error.

### Choose the right fix

| Failure type | Good first fix | Weak fix |
|---|---|---|
| Retrieval failure | Change `k`, chunk size/overlap, or query wording used for search | Only rewriting the answer prompt |
| Generation failure | Strengthen grounding rules, lower temperature, require “I don’t know” when unsupported | Only increasing `k` again and again |
| No-answer question answered inventively | Improve refusal rule in the prompt | Adding unrelated documents |

**Common mistake:** Treating every wrong answer as a prompt problem.

**Better habit:** Always print the **retrieval trace** before you edit the prompt.

### Activity — Classify Four Failures

Classify by the **evidence path**, not by whether the final sentence happens to sound right. If the expected document never entered top-k, label it **Retrieval** even when the answer text looks correct.

For each case, write **Retrieval** or **Generation**:

| Case | Retrieved | Answer | Type |
|---|---|---|---|
| Q: attendance minimum? Expected D1 | D5, D3, D2 | “Minimum attendance is 75%.” | |
| Q: library open Sunday? Expected D3 | D3, D1 | “Yes, open 24 hours on Sunday.” | |
| Q: mess refund? Expected D4 | D4 | “Apply 7 days before leaving.” | *(not a failure)* |
| Q: hostel room rent? Expected none | D5, D1 | “Room rent is ₹8,000 per month.” | |

---

## Grounded Answer Step for Before/After Demos

To show improvement on failing questions, you need both retrieval and a simple grounded answer step.

```python
def build_context(retrieved_items):
    """Join retrieved texts into one context block."""
    parts = []
    for item in retrieved_items:
        parts.append(f"[{item['doc_id']}] {item['text']}")
    return "\n".join(parts)


def grounded_answer(question, retrieved_items):
    """
    Tiny rule-based generator for the lab.
    It answers only with sentences that share tokens with the question,
    otherwise it refuses.
    """
    if not retrieved_items:
        return "I don't know."

    context = build_context(retrieved_items)
    question_tokens = set(tokenize(question))

    # Prefer the top retrieved item that shares tokens with the question
    for item in retrieved_items:
        item_tokens = set(tokenize(item["text"]))
        if question_tokens & item_tokens:
            return item["text"]

    # If nothing overlaps meaningfully, refuse instead of inventing
    return "I don't know."
```

**How the code works:**

- Context is labelled with **`doc_id`** so you can audit support quickly.
- The function returns source text or **`I don't know`** — it does not invent hostel rent or other missing facts.
- In a full stack you would call an LLM with `temperature=0` and the same refusal rule; the measurement method stays identical.

---

## Demonstrate Measurable Improvement on Two Failing Questions

The goal is not “the bot feels better.” The goal is: **at least two questions move from fail to pass**, with numbers written down.

### Improvement protocol

1. Run baseline (`k=1`, small/no overlap chunks if you want a weak start).
2. List failing questions and classify each failure.
3. Apply **one retrieval fix** (for example raise `k`, or use better chunk settings).
4. Re-run the **same** eval questions.
5. Record **before** and **after** for those two questions and for overall hit rate.

### Full improvement script

```python
import re


CORPUS = [
    {
        "doc_id": "D1",
        "title": "Attendance Policy",
        "text": (
            "Students must maintain at least 75% attendance. "
            "Below 75%, the student cannot sit for the end-term exam "
            "unless a medical certificate is approved by the dean."
        ),
    },
    {
        "doc_id": "D2",
        "title": "Late Submission Policy",
        "text": (
            "Assignments submitted up to 2 days late receive a 10% penalty per day. "
            "Submissions after 2 days are not accepted."
        ),
    },
    {
        "doc_id": "D3",
        "title": "Library Hours",
        "text": (
            "The main library is open Monday to Saturday from 8 AM to 10 PM. "
            "It is closed on Sundays and public holidays."
        ),
    },
    {
        "doc_id": "D4",
        "title": "Hostel Mess Refund",
        "text": (
            "Mess fees are refundable only if a student applies at least 7 days "
            "before leaving the hostel. Same-day refunds are not allowed."
        ),
    },
    {
        "doc_id": "D5",
        "title": "Wi-Fi Access",
        "text": (
            "Campus Wi-Fi is available to enrolled students using college email login. "
            "Guests need a temporary pass from the IT desk."
        ),
    },
]


EVAL_SET = [
    {"qid": "Q1", "question": "What is the minimum attendance required?", "expected_docs": ["D1"]},
    {"qid": "Q2", "question": "Can I submit an assignment 1 day late?", "expected_docs": ["D2"]},
    {"qid": "Q3", "question": "Is the library open on Sunday?", "expected_docs": ["D3"]},
    {"qid": "Q4", "question": "How do I get a mess fee refund?", "expected_docs": ["D4"]},
    {"qid": "Q5", "question": "Can a guest use campus Wi-Fi?", "expected_docs": ["D5"]},
    {"qid": "Q6", "question": "What is the hostel room rent?", "expected_docs": []},
]


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def score_doc(query, doc_text):
    query_tokens = set(tokenize(query))
    doc_tokens = set(tokenize(doc_text))
    return len(query_tokens & doc_tokens)


def retrieve_top_k(query, corpus, k=3):
    ranked = []
    for doc in corpus:
        ranked.append(
            {
                "doc_id": doc["doc_id"],
                "title": doc.get("title", ""),
                "text": doc["text"],
                "score": score_doc(query, doc["text"]),
            }
        )
    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked[:k]


def is_hit(retrieved_doc_ids, expected_docs):
    if not expected_docs:
        return None
    return any(doc_id in retrieved_doc_ids for doc_id in expected_docs)


def retrieval_hit_rate(rows):
    answerable = [r for r in rows if r["expected_docs"]]
    if not answerable:
        return 0.0
    hits = sum(1 for r in answerable if r["hit"])
    return hits / len(answerable)


def chunk_text(text, chunk_size=40, overlap=10):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start = end - overlap
    return chunks


def build_chunk_corpus(corpus, chunk_size=40, overlap=10):
    chunk_corpus = []
    for doc in corpus:
        pieces = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for i, piece in enumerate(pieces, start=1):
            chunk_corpus.append(
                {
                    "doc_id": doc["doc_id"],
                    "chunk_id": f"{doc['doc_id']}-C{i}",
                    "title": doc["title"],
                    "text": piece,
                }
            )
    return chunk_corpus


def grounded_answer(question, retrieved_items):
    if not retrieved_items:
        return "I don't know."
    question_tokens = set(tokenize(question))
    for item in retrieved_items:
        if question_tokens & set(tokenize(item["text"])):
            return item["text"]
    return "I don't know."


def evaluate_config(eval_set, corpus, k):
    rows = []
    for item in eval_set:
        retrieved = retrieve_top_k(item["question"], corpus, k=k)
        retrieved_ids = [r["doc_id"] for r in retrieved]
        answer = grounded_answer(item["question"], retrieved)
        hit = is_hit(retrieved_ids, item["expected_docs"])
        rows.append(
            {
                "qid": item["qid"],
                "question": item["question"],
                "expected_docs": item["expected_docs"],
                "retrieved_doc_ids": retrieved_ids,
                "hit": hit,
                "answer": answer,
            }
        )
    return {
        "hit_rate": retrieval_hit_rate(rows),
        "rows": rows,
    }


# --- Before: intentionally weak settings ---
before_corpus = build_chunk_corpus(CORPUS, chunk_size=8, overlap=0)
before = evaluate_config(EVAL_SET, before_corpus, k=1)

# --- After: improved retrieval settings ---
after_corpus = build_chunk_corpus(CORPUS, chunk_size=20, overlap=5)
after = evaluate_config(EVAL_SET, after_corpus, k=3)

print("BEFORE hit rate:", round(before["hit_rate"], 2))
print("AFTER hit rate:", round(after["hit_rate"], 2))

# Focus on two questions that failed before and should improve
focus_qids = ["Q2", "Q4"]
for qid in focus_qids:
    before_row = next(r for r in before["rows"] if r["qid"] == qid)
    after_row = next(r for r in after["rows"] if r["qid"] == qid)
    print("\n", qid)
    print(" before hit:", before_row["hit"], "retrieved:", before_row["retrieved_doc_ids"])
    print(" after hit:", after_row["hit"], "retrieved:", after_row["retrieved_doc_ids"])
    print(" before answer:", before_row["answer"])
    print(" after answer:", after_row["answer"])
```

**How the code works:**

- **Before** uses tiny chunks, no overlap, and `k=1` — a weak but realistic failure setup.
- **After** uses medium chunks, overlap, and `k=3` — one clear retrieval improvement package.
- The script prints overall hit rate and a **zoom-in** on two focus questions.
- Your success criteria: those two questions move from **miss → hit**, and answers become supported.

### Before/after report template

| Item | Before | After |
|---|---|---|
| `k` | 1 | 3 |
| Chunk size | 8 | 20 |
| Overlap | 0 | 5 |
| Overall hit rate | | |
| Q2 hit? | | |
| Q4 hit? | | |
| Failure type for Q2 (before) | | |
| Failure type for Q4 (before) | | |
| Fix applied | | |

### Activity — Prove Two Improvements

Run the full script (or your own variant) and complete:

1. Name **two** questions that failed in the before run.
2. Classify each as **retrieval** or **generation**.
3. State the **one main fix** you applied.
4. Show the after result: hit status and short supported answer.

If a question still fails, do not hide it. Write the remaining failure type and the next fix you would try.

---

## Putting the Improvement Loop Together

Use this loop whenever you tune RAG quality:

| Step | Action |
|---|---|
| 1 | Freeze a small eval set with expected supporting docs |
| 2 | Run baseline and record hit rate |
| 3 | Inspect misses with a retrieval trace |
| 4 | Classify each miss as retrieval vs generation |
| 5 | Change one parameter family |
| 6 | Re-run the same eval set |
| 7 | Keep the change only if the target failures improve and overall hit rate does not collapse |

This loop is the new habit from this lesson. Building the first RAG demo teaches the pipeline. This lab teaches **controlled improvement**.

### Activity — One-Page Tuning Card

Create a one-page card in your notes with:

- Your eval questions (`qid` + expected docs)
- Baseline hit rate
- Best `k`
- Best chunk size / overlap
- Two improved questions with before/after status

Keep this card for future RAG projects. The tools may change; the loop stays useful.

---

## Key Takeaways

- A **fixed eval set** with **expected supporting documents** turns RAG tuning from guesswork into measurable work.
- **Informal retrieval hit rate** tells you whether the right evidence entered top-k before you judge the final answer.
- **Top-k** and **chunk parameters** should be compared on the same questions, changing one family of settings at a time.
- Wrong answers need **failure analysis**: fix retrieval when evidence is missing; fix generation when evidence is present but the answer is still wrong.
- A credible improvement story shows **before/after** results on at least two failing questions, not only a nicer demo answer.

These measurement habits prepare you for stronger evaluation and production debugging later, where automated judges and richer search stacks build on the same improvement loop.

---

## Important Commands, Libraries, Terminologies Used

| Term or item | Meaning |
|---|---|
| **Fixed eval set** | Stable list of test questions used for before/after comparison |
| **Expected supporting document** | Gold source that should appear in retrieval for a question |
| **Retrieval hit rate** | Share of answerable questions where expected docs appear in top-k |
| **Top-k** | Number of highest-ranked results returned by the retriever |
| **Chunk size** | How much text goes into one searchable chunk |
| **Chunk overlap** | Shared text between neighbouring chunks |
| **Baseline** | First measured result before any tuning change |
| **Before/after comparison** | Same eval set scored under old and new settings |
| **Retrieval failure** | Expected evidence never entered the retrieved set |
| **Generation failure** | Evidence was retrieved, but the answer is still wrong or invented |
| **Failure analysis** | Classifying the failure type before choosing a fix |
| **Keyword retriever** | Simple ranker based on shared words between query and text |
| **Corpus** | Collection of documents or chunks searched by the retriever |
| **`doc_id`** | Stable document identifier used in scoring |
| **`tokenize`** | Split text into lowercase word tokens |
| **`retrieve_top_k`** | Function that returns the top-k ranked items |
| **`is_hit`** | Checks whether expected docs appear in retrieved ids |
| **`retrieval_hit_rate`** | Computes informal hit rate for answerable questions |
| **`build_chunk_corpus`** | Splits documents into chunks while keeping parent `doc_id` |
| **`grounded_answer`** | Answers only from retrieved text or says “I don’t know” |
| **`evaluate_config`** | Runs the full eval set for one retrieval configuration |
| **No-answer question** | Eval item with no supporting document in the corpus |
| **Improvement loop** | Measure → classify → change one knob → measure again |
