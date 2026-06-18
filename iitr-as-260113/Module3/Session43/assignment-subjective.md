# Assignment Subjective

Total Questions: 1  
Difficulty: Easy  
Type: Practical Implementation

---

## Q1 (Practical, Easy)

**ShopEasy**'s support team keeps seeing the same RAG bug: with **small chunks**, the bot retrieves text about **electronics** but misses **seven days**, so it answers *"I don't know."*

Build a small Python script **`debug_helper.py`** that helps engineers **reproduce** and **triage** this locally — **no OpenAI key**, **no vector database**.

Your script must do two jobs when run:

1. **Chunk simulation** — split a fixed policy string into chunks and show whether a simulated top-1 retrieval would fail.  
2. **Remediation hints** — print the recommended fix for four common failure symptoms.

---

### What you must implement

Create one file: `debug_helper.py`

It must define and use these pieces:

#### A. Constants (use exactly)

```python
POLICY_TEXT = (
    "Electronics items including phones and laptops may be returned within "
    "seven days of delivery if unused. Open-box items follow the same window. "
    "Contact support with your order ID for defects."
)

QUERY_KEYWORD = "electronics"
ANSWER_KEYWORD = "seven days"
```

#### B. Function `split_into_chunks(text, chunk_size, overlap)`

- Split `text` into character chunks (same idea as a text splitter at ingest time).
- Each chunk has at most `chunk_size` characters.
- The next chunk starts at `previous_start + chunk_size - overlap`.
- Return a list of chunk strings until all of `text` is covered.

#### C. Function `diagnose_chunk_gap(chunks, query_keyword, answer_keyword)`

- Simulate **top-1 retrieval**: use the **first** chunk that contains `query_keyword` (case-insensitive).  
  If no chunk matches, use `chunks[0]` (or `""` if the list is empty).
- On **that one chunk only**, return a dict:

```python
{
    "query_hit": True or False,
    "answer_hit": True or False,
    "diagnosis": "ok_both_present" | "weak_retrieval_split" | "weak_retrieval_miss",
}
```

Rules for `diagnosis`:

| Condition | diagnosis |
|---|---|
| Both keywords found in retrieved chunk | `ok_both_present` |
| Query keyword found, answer keyword missing | `weak_retrieval_split` |
| Query keyword not found in retrieved chunk | `weak_retrieval_miss` |

#### D. Function `suggest_remediation(symptom_id)`

Return the exact remediation string for each id:

| `symptom_id` | return value |
|---|---|
| `gst_wrong_tool` | `tool_patch: sharpen calculate_gst description; add prompt examples` |
| `missing_calculator_call` | `prompt_patch: must call calculate_gst for math queries` |
| `tiny_chunk_miss` | `retrieval_tune: increase chunk_size / overlap and re-ingest` |
| `refusal_on_valid_refund` | `prompt_patch: relax over-strict guardrails for in-domain topics` |
| anything else | `unknown_symptom` |

#### E. `main()` behaviour

When the script runs, it must print output in this shape:

**Part 1 — chunk simulation** (loop over `(50, 10)` then `(150, 20)`):

```
=== Chunk simulation on POLICY_TEXT ===

chunk_size=50, overlap=10, chunks=5
  query_hit=True, answer_hit=False
  diagnosis=weak_retrieval_split

chunk_size=150, overlap=20, chunks=2
  query_hit=True, answer_hit=True
  diagnosis=ok_both_present
```

**Part 2 — remediation hints** (print these four lines in order):

```
=== Symptom → remediation hints ===
gst_wrong_tool: tool_patch: sharpen calculate_gst description; add prompt examples
missing_calculator_call: prompt_patch: must call calculate_gst for math queries
tiny_chunk_miss: retrieval_tune: increase chunk_size / overlap and re-ingest
refusal_on_valid_refund: prompt_patch: relax over-strict guardrails for in-domain topics
```

---

### How to run and verify

```bash
python3 debug_helper.py
```

Check that your printed numbers and diagnosis labels match the expected output above.

---

### Submission Instruction

- implement everything in a single `debug_helper.py` file in VS Code  
- run the code and verify the output matches the expected format  
- submit the full `debug_helper.py` in the code editor / answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Walkthrough

1. **`split_into_chunks`** — walk `start` from 0; slice `text[start : start + chunk_size]`; advance by `chunk_size - overlap` until the end of the string.  
2. **`diagnose_chunk_gap`** — find the first chunk containing the query keyword; test both keywords only on that chunk; set the diagnosis label from the table.  
3. **`suggest_remediation`** — use a dictionary mapping the four symptom ids to the exact strings.  
4. **`main`** — call the chunk demo for both size/overlap pairs, then print the four remediation lines.

### Reference implementation

```python
POLICY_TEXT = (
    "Electronics items including phones and laptops may be returned within "
    "seven days of delivery if unused. Open-box items follow the same window. "
    "Contact support with your order ID for defects."
)

QUERY_KEYWORD = "electronics"
ANSWER_KEYWORD = "seven days"


def split_into_chunks(text, chunk_size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start += chunk_size - overlap
    return chunks


def diagnose_chunk_gap(chunks, query_keyword, answer_keyword):
    q = query_keyword.lower()
    a = answer_keyword.lower()
    retrieved = next((c for c in chunks if q in c.lower()), chunks[0] if chunks else "")
    query_hit = q in retrieved.lower()
    answer_hit = a in retrieved.lower()

    if query_hit and answer_hit:
        diagnosis = "ok_both_present"
    elif query_hit:
        diagnosis = "weak_retrieval_split"
    else:
        diagnosis = "weak_retrieval_miss"

    return {
        "query_hit": query_hit,
        "answer_hit": answer_hit,
        "diagnosis": diagnosis,
    }


def suggest_remediation(symptom_id):
    mapping = {
        "gst_wrong_tool": "tool_patch: sharpen calculate_gst description; add prompt examples",
        "missing_calculator_call": "prompt_patch: must call calculate_gst for math queries",
        "tiny_chunk_miss": "retrieval_tune: increase chunk_size / overlap and re-ingest",
        "refusal_on_valid_refund": "prompt_patch: relax over-strict guardrails for in-domain topics",
    }
    return mapping.get(symptom_id, "unknown_symptom")


def main():
    print("=== Chunk simulation on POLICY_TEXT ===")
    for size, overlap in [(50, 10), (150, 20)]:
        chunks = split_into_chunks(POLICY_TEXT, size, overlap)
        result = diagnose_chunk_gap(chunks, QUERY_KEYWORD, ANSWER_KEYWORD)
        print(f"\nchunk_size={size}, overlap={overlap}, chunks={len(chunks)}")
        print(f"  query_hit={result['query_hit']}, answer_hit={result['answer_hit']}")
        print(f"  diagnosis={result['diagnosis']}")

    print("\n=== Symptom → remediation hints ===")
    for symptom_id in [
        "gst_wrong_tool",
        "missing_calculator_call",
        "tiny_chunk_miss",
        "refusal_on_valid_refund",
    ]:
        print(f"{symptom_id}: {suggest_remediation(symptom_id)}")


if __name__ == "__main__":
    main()
```

### Alternative valid approaches

- Helper functions like `run_chunk_demo()` and `run_triage_demo()` are fine if `main()` produces the same output.  
- You may print each chunk index for your own debugging — grading uses the summary lines only.

### Common mistakes

- Testing keywords across **all** chunks instead of the **top-1 retrieved** chunk.  
- Wrong slide step (`start += chunk_size` without subtracting overlap).  
- Typos in remediation strings — match the table exactly.
