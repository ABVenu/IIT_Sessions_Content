# Subjective Assignment — Medium Difficulty

## Practical Task: ClearCart Support — Token Budget Checker

**Difficulty:** Medium (guided mini-lab)  
**Type:** Coding implementation

---

## Scenario

**ClearCart**'s support desk will paste customer chats and policy excerpts into a **4,096-token** model API. Before going live, finish a small Python audit script that:

1. Counts **tokens** for two short customer messages (English + Hinglish).
2. Checks whether a **long policy draft** fits the **safe input budget** after reserving reply and buffer space.

No LLM API calls. No GitHub repo. One short `.py` file only.

---

## Setup

```bash
pip install tiktoken
```

Create: **`clearcart_token_audit.py`**

---

## Starter code

Copy this into **`clearcart_token_audit.py`**. Constants and sample texts are **already set** — do not change them.

```python
import tiktoken

MODEL_CONTEXT_LIMIT = 4096
RESERVED_FOR_REPLY = 600
SAFETY_BUFFER = 200
ENCODING_NAME = "cl100k_base"

SHORT_SAMPLES = {
    "Refund request (English)": "I want a refund on order #4421.",
    "Hinglish update": "Kal main office jaake meeting attend karunga.",
}

LONG_POLICY_DRAFT = "refund" * 4500  # concatenated with no separator


# ── TODO 1: YOU WRITE THIS FUNCTION ──────────────────────────────────────────
def print_token_audit(encoding, label, text):
  """Print header, token count, and the list of token pieces for one text."""
  pass


# ── TODO 2: YOU WRITE THIS FUNCTION ──────────────────────────────────────────
def check_context_fit(prompt_text, model_limit=MODEL_CONTEXT_LIMIT):
  """Return dict with input_tokens, usable_limit, fits, overflow_tokens."""
  pass


def main():
    encoding = tiktoken.get_encoding(ENCODING_NAME)

    print("=== Short message audit ===")
    for label, text in SHORT_SAMPLES.items():
        print_token_audit(encoding, label, text)
        print()

    print("=== Long draft context check ===")
    report = check_context_fit(LONG_POLICY_DRAFT)
    print("Input tokens:", report["input_tokens"])
    print("Usable limit:", report["usable_limit"])
    print("Fits safely:", report["fits"])
    if not report["fits"]:
        print("Overflow by:", report["overflow_tokens"], "tokens")

    # ── TODO 3: YOU WRITE THIS IF/ELSE ───────────────────────────────────────
    # Print exactly one recommendation line (see Requirements below)


if __name__ == "__main__":
    main()
```

---

## Your tasks (only these three)

### 1. Complete `print_token_audit`

For the given `encoding`, `label`, and `text`:

- Print `--- <label> ---`
- Print `Token count: <number>`
- Print `Tokens: <list>` where each piece comes from `encoding.decode([t])` for each token ID

Use this **only** for the two short samples in `SHORT_SAMPLES`.

### 2. Complete `check_context_fit`

Use `ENCODING_NAME` and the module constants. Logic:

- `input_tokens` = token count of `prompt_text`
- `usable_limit` = `model_limit - RESERVED_FOR_REPLY - SAFETY_BUFFER`
- `fits` = `input_tokens <= usable_limit`
- `overflow_tokens` = `max(0, input_tokens - usable_limit)`

Return a dictionary with keys: `input_tokens`, `usable_limit`, `fits`, `overflow_tokens`.

### 3. Complete the recommendation `if/else` in `main()`

Print **exactly one** line:

- If `fits` is `True`:  
  `Recommendation: SAFE TO SEND — trim not required for input budget.`
- If `fits` is `False`:  
  `Recommendation: OVERFLOW — split the draft or retrieve smaller sections before calling the API.`

---

## Expected output (key lines)

```
=== Short message audit ===
--- Refund request (English) ---
Token count: 10
Tokens: [...]

--- Hinglish update ---
Token count: 10
Tokens: [...]

=== Long draft context check ===
Input tokens: 4500
Usable limit: 3296
Fits safely: False
Overflow by: 1204 tokens
Recommendation: OVERFLOW — split the draft or retrieve smaller sections before calling the API.
```

*(Short-message token **pieces** may vary slightly by `tiktoken` version; counts should be **10** each. Long draft must be **4500** tokens, usable **3296**, overflow **1204**.)*

---

## Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

### Answer Explanation (Reference Approach)

#### Step-by-step solution walkthrough

1. In `print_token_audit`, call `encoding.encode(text)`, build the decoded piece list, and print the three lines.
2. In `check_context_fit`, load encoding, count tokens, subtract reply + buffer reserves, compute `fits` and `overflow_tokens`.
3. In `main()`, branch on `report["fits"]` to print the single recommendation line.
4. `usable_limit = 4096 − 600 − 200 = 3296`. `"refund" * 4500` → **4500** tokens → overflow **1204**.

#### Complete exact code (single-file reference solution)

```python
import tiktoken

MODEL_CONTEXT_LIMIT = 4096
RESERVED_FOR_REPLY = 600
SAFETY_BUFFER = 200
ENCODING_NAME = "cl100k_base"

SHORT_SAMPLES = {
    "Refund request (English)": "I want a refund on order #4421.",
    "Hinglish update": "Kal main office jaake meeting attend karunga.",
}

LONG_POLICY_DRAFT = "refund" * 4500


def print_token_audit(encoding, label, text):
    token_ids = encoding.encode(text)
    tokens_as_text = [encoding.decode([t]) for t in token_ids]
    print(f"--- {label} ---")
    print("Token count:", len(token_ids))
    print("Tokens:", tokens_as_text)


def check_context_fit(prompt_text, model_limit=MODEL_CONTEXT_LIMIT):
    encoding = tiktoken.get_encoding(ENCODING_NAME)
    input_tokens = len(encoding.encode(prompt_text))
    usable_limit = model_limit - RESERVED_FOR_REPLY - SAFETY_BUFFER
    fits = input_tokens <= usable_limit
    overflow = max(0, input_tokens - usable_limit)
    return {
        "input_tokens": input_tokens,
        "usable_limit": usable_limit,
        "fits": fits,
        "overflow_tokens": overflow,
    }


def main():
    encoding = tiktoken.get_encoding(ENCODING_NAME)

    print("=== Short message audit ===")
    for label, text in SHORT_SAMPLES.items():
        print_token_audit(encoding, label, text)
        print()

    print("=== Long draft context check ===")
    report = check_context_fit(LONG_POLICY_DRAFT)
    print("Input tokens:", report["input_tokens"])
    print("Usable limit:", report["usable_limit"])
    print("Fits safely:", report["fits"])
    if not report["fits"]:
        print("Overflow by:", report["overflow_tokens"], "tokens")

    if report["fits"]:
        print("Recommendation: SAFE TO SEND — trim not required for input budget.")
    else:
        print(
            "Recommendation: OVERFLOW — split the draft or retrieve "
            "smaller sections before calling the API."
        )


if __name__ == "__main__":
    main()
```

#### Alternative approaches

- Load `encoding` once in `main()` and pass it into `check_context_fit` to avoid calling `get_encoding` twice.
- Add a separate `print("Long policy draft token count:", ...)` line for readability — optional if context-check lines are correct.

#### Grading notes

- Full marks if both short audits show correct structure, context math is correct, and exactly one recommendation line prints.
- Deduct if constants are changed, `LONG_POLICY_DRAFT` is altered, or `usable_limit` formula is wrong.
- Do **not** require printing 4,500 individual token pieces for the long draft — only the two short messages need the full `Tokens:` list.
