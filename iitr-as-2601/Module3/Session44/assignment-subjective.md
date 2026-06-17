# Subjective Assignment: GreenCart Token Counter

## Practical Task

**Difficulty:** Easy  
**Type:** Coding implementation

---

## Scenario

**GreenCart** wants a quick check before sending prompts to Groq: **how many tokens** does a prompt use, and **which old chat messages** would be left out if only the last few turns are sent?

You will complete a short script — **no LLM API key** needed.

---

## Task

Create one file: `prompt_budget_checker.py`

Most of the file is already written below. **Copy it** and complete only the **two marked sections**.

### Starter code (complete the `# TODO` parts)

```python
# pip install tiktoken
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

SAMPLE_PROMPT = """
You are a GreenCart FAQ assistant.
Answer ONLY from the context below.

=== CONTEXT START ===
Refunds are processed within 7 business days for eligible orders.
=== CONTEXT END ===

Question: What is the refund timeline?
"""

FULL_HISTORY = [
    {"role": "user", "content": "Use only GreenCart policy FAQ facts."},
    {"role": "assistant", "content": "Understood — grounded answers only."},
    {"role": "user", "content": "What is standard shipping time?"},
    {"role": "assistant", "content": "5-7 days in metro cities per FAQ."},
    {"role": "user", "content": "And refund timeline?"},
    {"role": "assistant", "content": "7 business days for eligible orders."},
    {"role": "user", "content": "What about warranty on electronics?"},
]

MAX_MESSAGES = 4


# TODO 1 — Write count_tokens(text) using encoding.encode(text)
def count_tokens(text: str) -> int:
    pass


# TODO 2 — Return (kept, dropped). If history fits, dropped = [].
#          kept = last max_messages items; dropped = everything before that.
def windowed_history(history: list, max_messages: int) -> tuple[list, list]:
    pass


def main():
    word_count = len(SAMPLE_PROMPT.split())
    token_count = count_tokens(SAMPLE_PROMPT)

    print("=== Token check ===")
    print("Word count:", word_count)
    print("Token count:", token_count)

    kept, dropped = windowed_history(FULL_HISTORY, MAX_MESSAGES)

    print("\n=== Windowed history (max 4 messages) ===")
    print("Messages sent to model:", len(kept))
    print("Messages dropped:", len(dropped))
    if dropped:
        print("First dropped message:", dropped[0]["content"])


if __name__ == "__main__":
    main()
```

---

## What you must implement

1. **`count_tokens`** — return `len(encoding.encode(text))`.
2. **`windowed_history`** — when history is longer than `max_messages`, keep the **last** `max_messages` messages and put the rest in **dropped**.

Do **not** change `SAMPLE_PROMPT`, `FULL_HISTORY`, `MAX_MESSAGES`, or the `print` lines in `main()`.

---

## Expected behaviour

When you run `python prompt_budget_checker.py`:

```text
=== Token check ===
Word count: <number>
Token count: <number>

=== Windowed history (max 4 messages) ===
Messages sent to model: 4
Messages dropped: 3
First dropped message: Use only GreenCart policy FAQ facts.
```

- **Token count** should be **greater than** word count (tokens ≠ words).
- **4** messages kept, **3** dropped.
- The first dropped line is the early **grounding rule**.

---

## Submission Instructions

- Complete the two `TODO` functions in a single `.py` file named `prompt_budget_checker.py`.
- Run the script and check the output matches the pattern above.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. **`count_tokens`** — `encoding.encode(text)` turns text into token IDs; `len(...)` is the count used for billing and context limits.
2. **`windowed_history`** — `kept = history[-max_messages:]` and `dropped = history[:-max_messages]` when the list is too long. This shows **silent forgetting**: rules from early turns may not reach the model.

### Reference Solution

```python
# pip install tiktoken
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

SAMPLE_PROMPT = """
You are a GreenCart FAQ assistant.
Answer ONLY from the context below.

=== CONTEXT START ===
Refunds are processed within 7 business days for eligible orders.
=== CONTEXT END ===

Question: What is the refund timeline?
"""

FULL_HISTORY = [
    {"role": "user", "content": "Use only GreenCart policy FAQ facts."},
    {"role": "assistant", "content": "Understood — grounded answers only."},
    {"role": "user", "content": "What is standard shipping time?"},
    {"role": "assistant", "content": "5-7 days in metro cities per FAQ."},
    {"role": "user", "content": "And refund timeline?"},
    {"role": "assistant", "content": "7 business days for eligible orders."},
    {"role": "user", "content": "What about warranty on electronics?"},
]

MAX_MESSAGES = 4


def count_tokens(text: str) -> int:
    return len(encoding.encode(text))


def windowed_history(history: list, max_messages: int) -> tuple[list, list]:
    if len(history) <= max_messages:
        return history, []
    kept = history[-max_messages:]
    dropped = history[:-max_messages]
    return kept, dropped


def main():
    word_count = len(SAMPLE_PROMPT.split())
    token_count = count_tokens(SAMPLE_PROMPT)

    print("=== Token check ===")
    print("Word count:", word_count)
    print("Token count:", token_count)

    kept, dropped = windowed_history(FULL_HISTORY, MAX_MESSAGES)

    print("\n=== Windowed history (max 4 messages) ===")
    print("Messages sent to model:", len(kept))
    print("Messages dropped:", len(dropped))
    if dropped:
        print("First dropped message:", dropped[0]["content"])


if __name__ == "__main__":
    main()
```

### Alternative approaches

- Add `print("Tokens > words:", token_count > word_count)` for a quick sanity check.
- Loop over `dropped` to print every dropped message (optional).

### Notes for evaluation

- Full credit if both functions are correct and output shows 4 kept, 3 dropped, with the grounding rule as first dropped message.
- Token count should exceed word count for the given prompt.
- No API key or RAG loop logic required.
