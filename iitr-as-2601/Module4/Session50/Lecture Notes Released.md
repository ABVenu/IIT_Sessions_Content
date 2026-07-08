# Retrieval & Grounding: Hands-On Improvement

## Introduction

In the **previous** lesson you improved RAG reliability with **chunking choices**, **metadata filters**, **source tags**, and evaluation ideas such as the **RAG triad** and **LLM-as-judge**.

This session moves from building a RAG pipeline to **measuring** and **improving** retrieval quality. You practise framing evaluation questions, reading retrieval traces, and choosing fixes — without advanced search stacks or a full production eval platform.

**What you will learn:**

- Build a small set of **questions** with **expected supporting documents**
- Understand **informal hit rate** and **ranked-list** scoring for retrieval
- See how **top-k** and **chunk parameters** affect retrieval (conceptually)
- Use the **RAG triad** and **LLM-as-judge** to spot weak retrieval
- Diagnose misses and choose retrieval-side fixes (semantic chunking, embedding model, `k`)
- Connect RAG with agents through **agentic RAG** (SQL tool + policy retriever)

The skill is **measure → inspect traces → change one knob → measure again**. This lesson focuses on the measurement and diagnosis habits; you can run full before/after experiments in your own notebook later.

---

## Why a Fixed Eval Set Matters

If you only test with random questions each time, you cannot tell whether a change helped.

- **Official Definition:** A **fixed eval set** is a stable list of test questions and expected evidence used to compare RAG behaviour before and after a change.
- **In Simple Words:** Same exam paper every time — so scores can move for a real reason.
- **Real-Life Example:** A cricket coach uses the **same practice test** every week and tracks who improved.

Without a fixed set you may “fix” one question and break another without noticing. With a fixed set every experiment uses the **same questions**, you record **hit / miss** for retrieval, and you can tell a **before/after** story on specific failures.

**Common mistake:** Changing `k`, chunk size, and the prompt all at once. You will not know which change helped.

**Better habit:** Change **one parameter family at a time**, then re-run the same eval set.

---

## RAG Pipeline Recap

Before tuning, recall the full path from documents to answers:

| Step | What happens |
|---|---|
| Documents | Policies, manuals, or notices enter the system |
| Chunking | Text is split into searchable **chunks** |
| Embeddings | Each chunk becomes a numeric vector |
| Vector DB | Chunks and embeddings are stored |
| Retrieval | The user question finds similar chunks (often **top-k**) |
| Generation | The LLM writes an answer from retrieved context |

- **Official Definition:** **Retrieval-augmented generation** combines search over stored knowledge with language-model generation.
- **In Simple Words:** Look up the right notes first, then answer from those notes.
- **Real-Life Example:** A hostel notice board — you find the pinned policy before you explain the rule to a student.

Many **tuning knobs** sit in this pipeline: chunker type, chunk size, overlap, embedding model, retriever type, and **top-k** (how many chunks enter the prompt). The only way to tune them well is to **evaluate** retrieval and generation on a fixed question set.

---

## Build a Mini Knowledge Base for Evaluation

For this lesson we use a **small, fixed corpus** so every student can reason about the same hits and misses.

- **Official Definition:** A **corpus** is the collection of documents or chunks your retriever searches.
- **In Simple Words:** The notice board for these experiments.
- **Real-Life Example:** Five pinned hostel policies — small enough to check by hand.

### Sample corpus — CampusHelp policies

| Doc ID | Title | Short policy |
|---|---|---|
| `D1` | Attendance Policy | Minimum 75% attendance; below that, no end-term exam unless dean-approved medical certificate. |
| `D2` | Late Submission Policy | Up to 2 days late: 10% penalty per day; after 2 days, not accepted. |
| `D3` | Library Hours | Open Mon–Sat 8 AM–10 PM; closed Sundays and public holidays. |
| `D4` | Hostel Mess Refund | Refundable only if student applies at least 7 days before leaving; no same-day refunds. |
| `D5` | Wi-Fi Access | Enrolled students use college email login; guests need IT desk temporary pass. |

```python
# Mini corpus for retrieval evaluation
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
```

**How the code works:**

- Each item has a stable **`doc_id`** so the eval set can name expected evidence clearly.
- **`text`** is what gets chunked, embedded, and retrieved in a full stack.
- Keep this list **unchanged** while you compare tuning changes.

---

## Build Questions with Expected Supporting Documents

An eval item is not only a question. It also names **which document should support the answer**.

- **Official Definition:** An **expected supporting document** is the source that must appear in retrieval for a question to count as a retrieval success.
- **In Simple Words:** You write the question **and** the correct notice-board label.
- **Real-Life Example:** For “Is the library open on Sunday?”, expected support is **Library Hours** (`D3`) — not the Wi-Fi notice.

### Eval set design rules

| Rule | Why it matters |
|---|---|
| Keep the set small (5–8 questions) | Easy to score by hand |
| Mix easy and hard questions | Easy ones check the pipeline; hard ones expose tuning needs |
| Write **expected `doc_id`s** before you run retrieval | Avoids “this chunk looks fine” bias |
| Include at least one **no-answer** question | Checks honest handling when evidence is missing |
| Freeze the set before experiments | Otherwise scores are not comparable |

### Fixed eval set used in class

| Q ID | Question | Expected doc IDs |
|---|---|---|
| `Q1` | What is the minimum attendance required? | `D1` |
| `Q2` | Can I submit an assignment 1 day late? | `D2` |
| `Q3` | Is the library open on Sunday? | `D3` |
| `Q4` | How do I get a mess fee refund? | `D4` |
| `Q5` | Can a guest use campus Wi-Fi? | `D5` |
| `Q6` | What is the hostel room rent? | *(none)* |

```python
# Fixed eval set — freeze before tuning experiments
EVAL_SET = [
    {"qid": "Q1", "question": "What is the minimum attendance required?", "expected_docs": ["D1"]},
    {"qid": "Q2", "question": "Can I submit an assignment 1 day late?", "expected_docs": ["D2"]},
    {"qid": "Q3", "question": "Is the library open on Sunday?", "expected_docs": ["D3"]},
    {"qid": "Q4", "question": "How do I get a mess fee refund?", "expected_docs": ["D4"]},
    {"qid": "Q5", "question": "Can a guest use campus Wi-Fi?", "expected_docs": ["D5"]},
    {"qid": "Q6", "question": "What is the hostel room rent?", "expected_docs": []},
]
```

**How the code works:**

- **`expected_docs`** is the gold label for retrieval success on answerable questions.
- **`Q6`** has an empty list — success means the system does not invent a hostel-rent policy.
- You score retrieval against this list, not against “does the final sentence sound nice?”

---

## LLM-as-Judge and the RAG Triad

Automated evaluation helps when you have no single “correct answer” string for every question.

- **Official Definition:** **LLM-as-judge** uses a separate, usually stronger, model to score RAG outputs on quality dimensions.
- **In Simple Words:** A second examiner reads the first model’s answer and gives marks.
- **Real-Life Example:** In a debate, the speaker and the judge should not be the same person — that would be biased.

### Three judge dimensions (RAG triad)

| Dimension | What it checks | Typical low score means |
|---|---|---|
| **Groundedness** | Is the answer supported by retrieved context? | Generation invented facts |
| **Answer relevance** | Does the answer address the user question? | Right sources, wrong focus |
| **Context relevance** | Were the **right chunks** retrieved? | **Retrieval** problem |

- **Official Definition:** **Context relevance** measures whether retrieved chunks match what the question needs.
- **In Simple Words:** Did the librarian bring the right folder?
- **Real-Life Example:** Low groundedness with high context relevance → fix the prompt or generation step. Low context relevance → fix chunking, embeddings, or **top-k** first.

**Important rule:** Use a **different** model for judging than for answering. Same model judging itself tends to be lenient and biased.

When judge scores (groundedness, relevance, context relevance) are low, or when human/static eval shows misses, you know the RAG stack needs tuning.

---

## Semi-Manual Evaluation and Informal Hit Rate

Besides judges, you can run a **static, ground-truth** check: for each question, compare **retrieved chunk IDs** to **expected doc IDs**.

- **Official Definition:** **Retrieval hit rate** is the share of answerable questions where at least one expected document appears in the top-k retrieved results.
- **In Simple Words:** Out of five policy questions, how many times did the right notice land in the top results?
- **Real-Life Example:** If five chunks should match and three do, hit rate is **60%** (3 ÷ 5).

### Scoring rules

| Case | Hit? |
|---|---|
| Expected doc is in top-k | **Hit** |
| Expected doc is missing from top-k | **Miss** |
| Question has no expected docs (`Q6`) | Score separately — should not force a wrong policy |

For answerable questions (`Q1`–`Q5`):

**Hit rate = (number of hits) ÷ (number of answerable questions)**

### Class demo trace (top-k retrieval)

| Q ID | Retrieved docs | Expected | Result |
|---|---|---|---|
| Q1 | D1 | D1 | Hit |
| Q2 | D5, D3, D1 | D2 | **Miss** |
| Q3 | D3 | D3 | Hit |
| Q4 | *(no D4 in top results)* | D4 | **Miss** |
| Q5 | D5 | D5 | Hit |

**Informal hit rate = 3 hits / 5 answerable questions = 0.60 (60%).**

This is **informal** on purpose — you are learning to **measure before you tune**, not building a full eval platform.

### Ranked-list evaluation

When you retrieve **top-k** chunks (for example 3 or 5), score against the **whole ranked list**, not only rank 1.

- **Official Definition:** **Ranked-list evaluation** checks whether the expected document appears anywhere in the top-k results.
- **In Simple Words:** The right policy counts if it is in the shortlist, even if it is not first.
- **Real-Life Example:** A librarian brings three folders; success if the correct policy is among them.

If multiple chunks can support one question, you can weight partial credit (for example 3 of 5 expected chunks retrieved → 60%).

---

## Top-k and Chunk Parameters (Tuning Knobs)

You practised choosing **top-k** when wiring retrieval into prompts. Here the focus is **what each knob does** when judge scores or hit rate are weak.

### Top-k

- **Official Definition:** **Top-k** is the number of highest-ranked chunks returned by the retriever.
- **In Simple Words:** How many notice cards the model may read.
- **Real-Life Example:** Bringing 1 folder vs 7 folders to answer a compound question.

| `k` | Possible benefit | Possible risk |
|---|---|---|
| 1 | Very focused context | Easy to miss the right chunk if ranking is imperfect |
| 3–5 | Balanced starting point | May still miss support if ranker is weak |
| 7–10 | Higher chance of including the right chunk | More noise for the generator |

In class we discussed: “Did you take **k = 1**? Should you use **k = 7** or **k = 10**?” Adjusting **k** is a common retrieval-side fix when expected chunks are ranked low but not absent.

### Chunk parameters

- **Official Definition:** **Chunk parameters** are settings such as **chunk size** and **overlap** that control how documents are split before embedding.
- **In Simple Words:** How big each note card is and whether neighbouring cards share a few lines.
- **Real-Life Example:** Cutting a long rulebook every 512 characters vs splitting at topic boundaries.

| Parameter | Role |
|---|---|
| **Chunk size** | Larger chunks keep more context; smaller chunks can be more precise |
| **Overlap** | Shared text between neighbours so a rule on a cut line is not lost |

When retrieval misses persist, try **one family of changes at a time** (only `k`, or only chunker settings) and re-run the **same** eval set.

---

## Failure Analysis — Retrieval vs Generation

A wrong final answer is not always a generation problem.

- **Official Definition:** **Failure analysis** is classifying why a RAG answer failed so you apply the correct fix.
- **In Simple Words:** Wrong page from the library, or right page but misread?
- **Real-Life Example:** If the clerk never opened the refund notice, that is **retrieval**. If the refund notice is on the desk but the clerk invents a rule, that is **generation**.

### Decision path

1. Look at **retrieved doc IDs** for the question.
2. If expected support is **missing** from top-k → treat as **retrieval failure** first.
3. If expected support is **present** but the answer is wrong or invented → **generation failure** (prompt, temperature, grounding rules).

In the class demo, **Q2** and **Q4** were clear **retrieval misses**: expected `D2` and `D4` never appeared in the retrieved set. Fixing only the answer prompt would not help — the model never saw the right evidence.

### Choose the right fix

| Failure signal | Good first fixes | Weak fix |
|---|---|---|
| Low **context relevance** / missing expected docs | Semantic chunking, stronger **embedding model**, higher **k**, better metadata | Only rewriting the answer prompt |
| Low **groundedness** with good retrieval | Stricter grounding prompt, lower temperature, “I don’t know” when unsupported | Blindly increasing **k** again |
| No-answer question (`Q6`) answered inventively | Refusal rule when retrieval is empty or irrelevant | Adding unrelated documents |

**Common mistake:** Treating every wrong answer as a prompt problem.

**Better habit:** Always print the **retrieval trace** before you edit generation settings.

---

## When Retrieval Misses — Fixes Discussed in Class

For **Q2** (late submission) the system retrieved `D5`, `D3`, `D1` but expected **`D2`**. For **Q4** (mess refund) the expected **`D4`** was a complete miss. The instructor walked through retrieval-side improvements to try next:

1. **Change chunking strategy** — especially **semantic chunking** instead of naive fixed-size splits.
2. **Swap or upgrade the embedding model** — for example a stronger model than your baseline (sessions used **GTE-large** as a reference).
3. **Adjust top-k** — retrieve more chunks when rank 1 is often wrong.
4. **Re-check judge scores** — groundedness, answer relevance, and context relevance should move after a real retrieval fix.

You would re-run the **same** eval questions after each change and compare hit rate and judge scores. That before/after loop is the improvement habit even when you do not automate every step in one script.

---

## Fixed-Size Chunking and Its Limits

Until now, many labs used **fixed-size chunking**: every N characters or tokens becomes one chunk (for example 512 characters, then the next 512).

- **Official Definition:** **Fixed-size chunking** splits text at fixed length boundaries regardless of meaning.
- **In Simple Words:** Scissors cut every fixed number of words, even mid-sentence.
- **Real-Life Example:** An HR leave policy where “maternity leave” and “12 weeks” land in **different** chunks because the cut fell in the middle — retrieval for “How long is maternity leave?” may miss both facts.

Problems with fixed-size-only chunking:

- Related sentences get **split apart**
- One chunk may lack enough context to answer
- Retrieval returns **partial** or **misleading** snippets

That is why teams move to **semantic chunking** when fixed-size hit rate or context-relevance scores stay low.

---

## Semantic Chunking

**Semantic chunking** splits text where **meaning** shifts, not only after a fixed character count.

- **Official Definition:** **Semantic chunking** groups sentences or passages that are semantically similar and splits where similarity drops.
- **In Simple Words:** New chunk when the topic changes, not when you hit character 512.
- **Real-Life Example:** One chunk for “late submission penalties” and a separate chunk for “exam attendance” — even if both sit in the same PDF page.

### How it works (high level)

1. Break the document into sentences or small units.
2. Embed each unit and measure **similarity** between neighbours.
3. **Merge** units that stay above a similarity threshold.
4. **Split** when similarity drops — a new topic starts.
5. Apply **guardrails**: minimum chunk size, maximum chunk size, so chunks are not tiny or huge.

Merge/split thresholds and size guardrails are often tuned **manually** by inspecting sample chunks — there is no single universal setting.

### Trade-offs

| Aspect | Semantic chunking | Fixed-size chunking |
|---|---|---|
| Retrieval quality on long policies | Often better topic coherence | Fast but can split mid-rule |
| Cost / latency | More embedding steps while building chunks | Cheaper to chunk |
| Tuning | Thresholds and min/max size need experimentation | Only size and overlap |

When class retrieval misses (like **Q2** and **Q4**) persist, switching chunker type is a standard next experiment on the same eval set.

---

## Embedding Model Choice

Retrieval quality depends heavily on the **embedding model** that maps text to vectors.

- **Official Definition:** An **embedding model** converts text into dense vectors so similar meaning sits nearby in vector space.
- **In Simple Words:** A “meaning printer” for chunks and queries.
- **Real-Life Example:** Two paraphrases of “mess refund rules” should land closer than a Wi-Fi policy.

Course labs often use **GTE-large** (or similar). If hit rate or context-relevance scores stay low after chunking fixes, trying a **more capable embedding model** is a valid experiment — always compare on the **same** frozen eval set.

---

## Agentic RAG — SQL Tool + Policy Retriever

The session connected retrieval tuning to **agents**: one top-level agent that picks among specialized tools.

- **Official Definition:** **Agentic RAG** is a pattern where an agent chooses between retrieval tools and other tools (for example database query tools) to answer user questions.
- **In Simple Words:** One smart router decides: “Should I search policies or query live order data?”
- **Real-Life Example:** An e-commerce support bot that checks **order status in SQL** and **return policy in a vector store**.

### E-commerce demo architecture

| Component | Role |
|---|---|
| **SQL database** | Live order and customer facts (structured) |
| **`create_sql_agent` tool** | LangChain built-in agent: English question → SQL → rows |
| **Vector store (Chroma)** | Policy documents chunked and embedded (unstructured) |
| **Custom RAG retriever tool** | Searches policy chunks for refund/shipping rules |
| **Top-level chat agent** | Picks SQL tool or RAG tool per question |

Flow in plain language:

1. User asks in natural language.
2. Top-level agent decides which tool fits.
3. **SQL tool** answers “Where is my order?” from the database.
4. **RAG tool** answers “What is your return policy?” from embedded policies.
5. Agent synthesizes a final reply from tool observations.

This is the same agent idea you have seen before (**LLM + tools**), now with **retrieval** as one of the tools instead of the only knowledge path.

**Safety note:** SQL agents need guardrails in the system prompt — for example **no DROP/DELETE** — because generated SQL can be dangerous if unchecked.

---

## Multimodal RAG (Preview)

A related direction is **multimodal RAG**: retrieving and reasoning over **images**, diagrams, or other media — not only text chunks.

- **Official Definition:** **Multimodal RAG** extends retrieval to non-text modalities (for example images paired with captions or OCR text).
- **In Simple Words:** The notice board can include pictures and charts, not only paragraphs.
- **Real-Life Example:** A technician manual where wiring diagrams and spec tables are both searchable.

This track covers multimodal models and vision-based RAG in an upcoming lesson. The same eval habits — fixed questions, trace inspection, judge scores — still apply when the “chunks” include visual content.

---

## Improvement Loop (Habit Summary)

| Step | Action |
|---|---|
| 1 | Freeze a small eval set with expected supporting docs |
| 2 | Run retrieval and record hit/miss per question (and judge scores if available) |
| 3 | Inspect misses — especially **context relevance** |
| 4 | Classify: missing evidence → retrieval fix; evidence present but wrong answer → generation fix |
| 5 | Change **one** knob (chunker, embedding model, or **k**) |
| 6 | Re-run the **same** eval set and compare |

Building the first RAG demo teaches the pipeline. This lesson teaches **controlled improvement** on that pipeline.

### Activity — One-Page Tuning Card

In your notebook, draft a one-page card with:

- Your eval questions (`qid` + expected docs)
- One sample hit-rate calculation (hits ÷ answerable questions)
- Two questions that **missed** in the class trace (`Q2`, `Q4`)
- One retrieval fix you would try first for each (chunker, embedding, or `k`)

Keep this card for future RAG projects. The tools may change; the loop stays useful.

---

## Key Takeaways

- A **fixed eval set** with **expected supporting documents** turns RAG tuning from guesswork into measurable work.
- **Informal hit rate** and **ranked-list** checks tell you whether the right evidence entered top-k before you judge the final answer.
- **LLM-as-judge** and the **RAG triad** separate **retrieval** weakness (context relevance) from **generation** weakness (groundedness, answer relevance).
- **Top-k**, **chunk size**, **overlap**, **chunker type**, and **embedding model** are the main retrieval-side knobs — change one family at a time.
- **Semantic chunking** often beats naive fixed-size splits on long policies; **GTE-large**-class models are a strong baseline to compare against.
- **Agentic RAG** combines a **SQL agent tool** and a **RAG retriever tool** under one top-level agent for mixed structured + unstructured support.

These measurement habits prepare you for stronger evaluation and production debugging later, where automated judges and richer search stacks build on the same improvement loop.

---

## Important Commands, Libraries, Terminologies Used

| Term or item | Meaning |
|---|---|
| **Fixed eval set** | Stable list of test questions for before/after comparison |
| **Expected supporting document** | Gold source that should appear in retrieval |
| **Retrieval hit rate** | Share of answerable questions where expected docs appear in top-k |
| **Ranked-list evaluation** | Score retrieval using the full top-k list, not only rank 1 |
| **Top-k** | Number of highest-ranked chunks returned to the generator |
| **Chunk size / overlap** | How documents are split and how much text is shared between chunks |
| **Fixed-size chunking** | Splits at fixed length boundaries |
| **Semantic chunking** | Splits where semantic similarity drops between units |
| **Context relevance** | Judge score: were the right chunks retrieved? |
| **Groundedness** | Judge score: is the answer supported by context? |
| **Answer relevance** | Judge score: does the answer address the question? |
| **RAG triad** | Groundedness, answer relevance, and context relevance together |
| **LLM-as-judge** | Separate model scores RAG outputs |
| **Retrieval failure** | Expected evidence missing from top-k |
| **Generation failure** | Evidence present but answer still wrong or invented |
| **GTE-large** | Example embedding model used in course labs |
| **Agentic RAG** | Agent routes between RAG retrieval and other tools (e.g. SQL) |
| **`create_sql_agent`** | LangChain helper that turns English questions into SQL |
| **Improvement loop** | Measure → classify → change one knob → measure again |
