# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

Build a small **CampusHelp retrieval evaluator** in Python. You will define a fixed policy corpus, a frozen eval set with expected documents, run a simple **keyword retriever** at **top-k = 3**, and print an **informal hit rate**.

### Problem Statement

Create a single program that:

1. Defines the **CampusHelp `CORPUS`** with five documents (`D1`–`D5`): Attendance, Late Submission, Library Hours, Hostel Mess Refund, and Wi-Fi Access (use the policy text from the course notes).
2. Defines a frozen **`EVAL_SET`** with six items (`Q1`–`Q6`), each with:
   - `qid`
   - `question`
   - `expected_docs` (empty list for `Q6` — hostel room rent is not in the corpus)
3. Implements a simple **keyword retriever**:
   - `tokenize(text)` — lowercase word tokens
   - `score_doc(query, doc_text)` — count of shared query words
   - `retrieve_top_k(query, corpus, k)` — return top-k docs by score
4. Implements scoring helpers:
   - `is_hit(retrieved_doc_ids, expected_docs)` — `True` if any expected doc is in the retrieved list; return `None` when `expected_docs` is empty
   - `retrieval_hit_rate(rows)` — hits ÷ answerable questions only
5. Runs retrieval for every eval question with **`k = 3`** and prints:
   - `qid`, question, expected docs, retrieved doc IDs, hit/miss (or `N/A` for `Q6`)
   - overall **hit rate** for `Q1`–`Q5` as a decimal and percentage

### Expected Output (sample shape)

Your run should print one block per question and a final hit rate. Example:

```
Q1 hit=True
  question: What is the minimum attendance required?
  expected: ['D1']
  retrieved: ['D1', 'D3', 'D5']

Q6 hit=N/A
  question: What is the hostel room rent?
  expected: []
  retrieved: ['D1', 'D3', 'D4']

Hit rate: 1.00 (100%)
```

With this small corpus and keyword overlap, `Q1`–`Q5` should usually be **hits** if your retriever is implemented correctly. Retrieved **order** may differ; what matters is whether the **expected doc** appears anywhere in top-k.

### Submission Instruction

- code all the points mentioned in the VS Code in single `.py` file
- run the code and verify its working
- then submit the code in the code editor/answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Copy the five-policy `CORPUS` and six-item `EVAL_SET` from the lesson material.
2. Implement keyword overlap scoring — no vector DB or LLM required.
3. For each eval item, call `retrieve_top_k` with `k=3`.
4. Mark a **hit** when any `expected_docs` entry appears in the retrieved ID list.
5. Compute hit rate on answerable questions (`Q1`–`Q5`) only; skip `Q6` from the denominator.
6. Print a readable trace plus the final hit rate.

### Complete Reference Code (Single File)

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


def tokenize(text: str) -> list[str]:
    """Lowercase and split text into simple word tokens."""
    return re.findall(r"[a-z0-9]+", text.lower())


def score_doc(query: str, doc_text: str) -> int:
    """Count shared words between query and document."""
    query_tokens = set(tokenize(query))
    doc_tokens = set(tokenize(doc_text))
    return len(query_tokens & doc_tokens)


def retrieve_top_k(query: str, corpus: list[dict], k: int = 3) -> list[dict]:
    """Return top-k corpus items ranked by keyword overlap."""
    ranked = []
    for doc in corpus:
        ranked.append(
            {
                "doc_id": doc["doc_id"],
                "title": doc["title"],
                "text": doc["text"],
                "score": score_doc(query, doc["text"]),
            }
        )
    ranked.sort(key=lambda item: (-item["score"], item["doc_id"]))
    return ranked[:k]


def is_hit(retrieved_doc_ids: list[str], expected_docs: list[str]) -> bool | None:
    """True if any expected doc appears in retrieved ids; None if no gold labels."""
    if not expected_docs:
        return None
    return any(doc_id in retrieved_doc_ids for doc_id in expected_docs)


def retrieval_hit_rate(rows: list[dict]) -> float:
    """Hit rate for answerable questions only."""
    answerable = [row for row in rows if row["expected_docs"]]
    if not answerable:
        return 0.0
    hits = sum(1 for row in answerable if row["hit"])
    return hits / len(answerable)


def run_retrieval_eval(eval_set: list[dict], corpus: list[dict], k: int = 3) -> list[dict]:
    """Run retrieval for each eval question and return result rows."""
    rows = []
    for item in eval_set:
        retrieved = retrieve_top_k(item["question"], corpus, k=k)
        retrieved_ids = [doc["doc_id"] for doc in retrieved]
        rows.append(
            {
                "qid": item["qid"],
                "question": item["question"],
                "expected_docs": item["expected_docs"],
                "retrieved_doc_ids": retrieved_ids,
                "hit": is_hit(retrieved_ids, item["expected_docs"]),
            }
        )
    return rows


def main() -> None:
    rows = run_retrieval_eval(EVAL_SET, CORPUS, k=3)

    for row in rows:
        hit_label = "N/A" if row["hit"] is None else row["hit"]
        print(f"{row['qid']} hit={hit_label}")
        print(f"  question: {row['question']}")
        print(f"  expected: {row['expected_docs']}")
        print(f"  retrieved: {row['retrieved_doc_ids']}")
        print()

    rate = retrieval_hit_rate(rows)
    print(f"Hit rate: {rate:.2f} ({int(rate * 100)}%)")


if __name__ == "__main__":
    main()
```

### How the Code Works

- **`CORPUS`** and **`EVAL_SET`** freeze the knowledge base and gold labels before any scoring.
- **`retrieve_top_k`** ranks documents by shared words — a lightweight stand-in for vector search.
- **`is_hit`** uses **ranked-list** logic: success if the expected doc appears anywhere in top-k.
- **`retrieval_hit_rate`** ignores `Q6` so no-answer questions do not skew the score.
- Printing per-question traces makes it easy to spot retrieval misses (for example `Q2` or `Q4`) before tuning chunking or `k`.

### Alternative Valid Approaches

- Print `HIT` / `MISS` strings instead of booleans for readability.
- Add a second run with `k=5` and compare hit rates in the same file.
- Sort ties differently as long as hit/miss labels stay correct for gold docs.
