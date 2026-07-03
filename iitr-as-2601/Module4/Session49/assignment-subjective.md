# Subjective Assignment: Metadata-First Policy Retrieval

## Practical Task (Medium)

**ShopSphere** runs a product-support knowledge base for mobiles, laptops, and manuals. Before adding vector similarity search, the team wants a **metadata-first retrieval layer** that filters chunks safely and prints traceable citations — the same pattern used in the class demo.

Your task is to build a **single Python file** named `policy_retrieval.py` that simulates filter-first retrieval **without** calling any LLM or vector database API.

### Knowledge base to use

Start with this exact `chunks` list in your file:

```python
chunks = [
    {
        "text": "Mobiles can be returned within 7 days if damaged.",
        "metadata": {
            "doc_type": "policy",
            "product": "mobile",
            "status": "active",
            "source_file": "mobile_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops can be returned within 10 days for manufacturing defects.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops were earlier returnable within 30 days.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "archived",
            "source_file": "old_laptop_policy.md",
            "section_title": "Old Return Rules",
        },
    },
    {
        "text": "For laptop battery drain, run diagnostics mode before replacing parts.",
        "metadata": {
            "doc_type": "manual",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_service_manual.pdf",
            "section_title": "Battery Diagnostics",
        },
    },
    {
        "text": "Premium users get billing support within 24 hours.",
        "metadata": {
            "doc_type": "policy",
            "product": "billing",
            "status": "active",
            "source_file": "billing_policy.md",
            "section_title": "Premium Support",
        },
    },
]
```

### What you must implement

Create these functions in `policy_retrieval.py`:

#### 1. `matches_filters(metadata: dict, filters: dict) -> bool`

- Return `True` only when **every** key in `filters` matches the same key in `metadata`.
- Use `metadata.get(key)` for comparison.
- Return `False` if any filter condition fails.

#### 2. `retrieve(filters: dict) -> list`

- Loop through `chunks`.
- Return a list of chunks whose metadata passes `matches_filters`.
- Preserve the original chunk dictionaries.

#### 3. `format_citation(chunk: dict) -> str`

Return a citation string in this exact format:

```text
Source: <source_file> - <section_title>
```

Example:

```text
Source: laptop_policy.md - Return Rules
```

Read `source_file` and `section_title` from `chunk["metadata"]`.

#### 4. `print_retrieval_results(filters: dict) -> None`

For every chunk returned by `retrieve(filters)`:

1. Print the chunk `text` on one line  
2. Print the citation from `format_citation(chunk)` on the next line  
3. Print one blank line after each chunk  

If no chunk matches, print exactly:

```text
No matching chunks found.
```

#### 5. Demo block

At the bottom of the file, add:

```python
if __name__ == "__main__":
    ...
```

Run **exactly these three filter tests** in order by calling `print_retrieval_results(...)`:

| Test | Filters |
|---|---|
| 1 | `{"doc_type": "policy", "product": "laptop", "status": "active"}` |
| 2 | `{"doc_type": "policy", "product": "mobile", "status": "active"}` |
| 3 | `{"doc_type": "manual", "product": "laptop", "status": "active"}` |

### Expected sample output

```text
Laptops can be returned within 10 days for manufacturing defects.
Source: laptop_policy.md - Return Rules

Mobiles can be returned within 7 days if damaged.
Source: mobile_policy.md - Return Rules

For laptop battery drain, run diagnostics mode before replacing parts.
Source: laptop_service_manual.pdf - Battery Diagnostics

```

### Constraints

- **One file only:** `policy_retrieval.py`  
- **No LLM API calls** and **no vector database libraries**  
- Use only Python standard library  
- Code must run with: `python policy_retrieval.py`  
- The archived laptop policy must **not** appear in Test 1 because `status` must be `active`

### Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file  
- Run the code and verify it is working  
- Then submit the code in the code editor / answer box in the LMS  

---

## Answer Explanation

### Ideal Solution Walkthrough

A complete solution mirrors the class **metadata filter first** pattern:

1. Store chunks with both `text` and `metadata`.  
2. Use `matches_filters()` to apply every filter condition.  
3. Use `retrieve()` to collect only matching chunks.  
4. Print grounded context plus a citation built only from stored metadata — never invented by the model.

Test 1 should return only the active laptop policy. The archived 30-day laptop policy is excluded because its `status` is `archived`. Test 2 returns the mobile policy. Test 3 returns the laptop manual chunk.

### Complete Reference Solution

```python
# policy_retrieval.py — metadata-first retrieval demo (offline)

chunks = [
    {
        "text": "Mobiles can be returned within 7 days if damaged.",
        "metadata": {
            "doc_type": "policy",
            "product": "mobile",
            "status": "active",
            "source_file": "mobile_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops can be returned within 10 days for manufacturing defects.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_policy.md",
            "section_title": "Return Rules",
        },
    },
    {
        "text": "Laptops were earlier returnable within 30 days.",
        "metadata": {
            "doc_type": "policy",
            "product": "laptop",
            "status": "archived",
            "source_file": "old_laptop_policy.md",
            "section_title": "Old Return Rules",
        },
    },
    {
        "text": "For laptop battery drain, run diagnostics mode before replacing parts.",
        "metadata": {
            "doc_type": "manual",
            "product": "laptop",
            "status": "active",
            "source_file": "laptop_service_manual.pdf",
            "section_title": "Battery Diagnostics",
        },
    },
    {
        "text": "Premium users get billing support within 24 hours.",
        "metadata": {
            "doc_type": "policy",
            "product": "billing",
            "status": "active",
            "source_file": "billing_policy.md",
            "section_title": "Premium Support",
        },
    },
]


def matches_filters(metadata: dict, filters: dict) -> bool:
  # Return True only when every filter key matches metadata
  for key, value in filters.items():
    if metadata.get(key) != value:
      return False
  return True


def retrieve(filters: dict) -> list:
  # Collect chunks that pass all metadata filters
  results = []
  for chunk in chunks:
    if matches_filters(chunk["metadata"], filters):
      results.append(chunk)
  return results


def format_citation(chunk: dict) -> str:
  # Build a traceable citation from stored metadata only
  source_file = chunk["metadata"]["source_file"]
  section_title = chunk["metadata"]["section_title"]
  return f"Source: {source_file} - {section_title}"


def print_retrieval_results(filters: dict) -> None:
  # Print filtered chunk text plus citation for each match
  results = retrieve(filters)
  if not results:
    print("No matching chunks found.")
    return

  for chunk in results:
    print(chunk["text"])
    print(format_citation(chunk))
    print()


if __name__ == "__main__":
  print_retrieval_results(
    {"doc_type": "policy", "product": "laptop", "status": "active"}
  )
  print_retrieval_results(
    {"doc_type": "policy", "product": "mobile", "status": "active"}
  )
  print_retrieval_results(
    {"doc_type": "manual", "product": "laptop", "status": "active"}
  )
```

### Alternative Approaches

- **List comprehension in `retrieve`:** `[chunk for chunk in chunks if matches_filters(chunk["metadata"], filters)]` — shorter and equally valid.  
- **Helper for empty checks:** Raise a custom message per test case if you later add logging, but keep the required exact no-match string for grading.  
- **Next step after this task:** Add a simple keyword ranking function as a second layer before generation — that would extend the two-layer retrieval idea from the notes.

### Why this matches the session

The task applies **metadata filters**, **filter-first retrieval**, **source tagging / citations**, and the **offline indexing vs online inference** mindset — without requiring embeddings, Gradio, or LLM-as-judge APIs that were only introduced at overview level in the notes.
