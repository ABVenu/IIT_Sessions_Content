# Subjective Assignment: ShopEasy Ticket Validator

## Practical Task

**Difficulty:** Easy  
**Type:** Coding implementation (complete the missing parts)

---

## Scenario

**ShopEasy** saves raw LLM responses before they reach the support dashboard. Your teammate already wrote the **parsing helpers** — they turn messy text into a Python **`dict`**. Your job is to add the **validator** so bad tickets (like wrong priority spelling) are caught **before** the UI updates.

No live Groq API calls are needed for this exercise.

---

## Task

Create **`shopeasy_ticket_parser.py`** using the **starter code** below. You only need to complete the parts marked **`# TODO`**.

### What you must implement

1. **`validate_ticket(data: dict) -> tuple[bool, str]`**
   - Return **`(True, "ok")`** if the ticket passes all checks.
   - Return **`(False, reason)`** on the **first** failure.
   - Checks (in this order):
     1. Every key in **`REQUIRED_KEYS`** must be present in **`data`**.
     2. **`data["category"]`** must be in **`ALLOWED_CATEGORIES`**.
     3. **`data["priority"]`** must be in **`ALLOWED_PRIORITIES`**.

2. **`validate_or_raise(data: dict) -> dict`**
   - Call **`validate_ticket(data)`**.
   - If validation fails, raise **`ValueError(message)`**.
   - If validation passes, return **`data`**.

3. **`main()`**
   - Loop over **`TEST_CASES`** (already defined in the starter).
   - For each raw string:
     - Call **`safe_parse_model_json(raw)`** then **`validate_or_raise(parsed)`**.
     - On success, print: **`SUCCESS: <the dict>`**
     - On **`ValueError`**, print: **`FAILED: <error message>`**

Do **not** change the parsing helpers or the **`TEST_CASES`** values.

### Starter code (copy this into your file)

```python
import json
import re

REQUIRED_KEYS = ["category", "priority", "summary", "needs_human", "suggested_reply"]
ALLOWED_CATEGORIES = {"billing", "shipping", "product", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def strip_markdown_fences(text: str) -> str:
    cleaned = text.strip()
    match = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", cleaned, flags=re.IGNORECASE)
    return match.group(1).strip() if match else cleaned


def extract_json_object(text: str) -> str:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object braces found in model output.")
    return text[start : end + 1]


def safe_parse_model_json(raw: str) -> dict:
    step1 = strip_markdown_fences(raw)
    step2 = extract_json_object(step1)
    data = json.loads(step2)
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON must be an object (dict).")
    return data


# TODO: Implement validate_ticket
def validate_ticket(data: dict) -> tuple[bool, str]:
  pass


# TODO: Implement validate_or_raise
def validate_or_raise(data: dict) -> dict:
  pass


TEST_CASES = [
    # Case 1 — valid ticket (should print SUCCESS)
    '{"category": "shipping", "priority": "medium", "summary": "Order 4412 arrived late", '
    '"needs_human": false, "suggested_reply": "We are tracking your parcel."}',
    # Case 2 — wrong priority casing (should print FAILED)
    '{"category": "billing", "priority": "HIGH", "summary": "Duplicate charge", '
    '"needs_human": false, "suggested_reply": "Refund initiated."}',
]


# TODO: Implement main
def main() -> None:
  pass


if __name__ == "__main__":
    main()
```

---

## Expected behaviour

When you run `python shopeasy_ticket_parser.py`:

```text
SUCCESS: {'category': 'shipping', 'priority': 'medium', 'summary': 'Order 4412 arrived late', 'needs_human': False, 'suggested_reply': 'We are tracking your parcel.'}
FAILED: Invalid priority: 'HIGH'
```

- **Case 1** must print **`SUCCESS:`** with the parsed dict.
- **Case 2** must print **`FAILED: Invalid priority: 'HIGH'`** (use this exact message format for the priority check).

---

## Submission Instructions

- Complete the **`# TODO`** sections in a single `.py` file named `shopeasy_ticket_parser.py` in VS Code.
- Run the script and verify both output lines match the expected behaviour above.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. **`safe_parse_model_json`** (already provided) turns each raw string into a Python **`dict`**.
2. **`validate_ticket`** is where you enforce the schema rules — required keys plus allowed **`category`** and **`priority`** values.
3. **Case 2** parses fine as JSON, but **`"HIGH"`** is not in **`ALLOWED_PRIORITIES`** — validation must block it before the dashboard updates.
4. **`main()`** ties parse → validate → print into a simple loop over **`TEST_CASES`**.

### Reference Solution

```python
import json
import re

REQUIRED_KEYS = ["category", "priority", "summary", "needs_human", "suggested_reply"]
ALLOWED_CATEGORIES = {"billing", "shipping", "product", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def strip_markdown_fences(text: str) -> str:
    cleaned = text.strip()
    match = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", cleaned, flags=re.IGNORECASE)
    return match.group(1).strip() if match else cleaned


def extract_json_object(text: str) -> str:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object braces found in model output.")
    return text[start : end + 1]


def safe_parse_model_json(raw: str) -> dict:
    step1 = strip_markdown_fences(raw)
    step2 = extract_json_object(step1)
    data = json.loads(step2)
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON must be an object (dict).")
    return data


def validate_ticket(data: dict) -> tuple[bool, str]:
    for key in REQUIRED_KEYS:
        if key not in data:
            return False, f"Missing required field: {key}"
    if data["category"] not in ALLOWED_CATEGORIES:
        return False, f"Invalid category: {data['category']!r}"
    if data["priority"] not in ALLOWED_PRIORITIES:
        return False, f"Invalid priority: {data['priority']!r}"
    return True, "ok"


def validate_or_raise(data: dict) -> dict:
    ok, message = validate_ticket(data)
    if not ok:
        raise ValueError(message)
    return data


TEST_CASES = [
    '{"category": "shipping", "priority": "medium", "summary": "Order 4412 arrived late", '
    '"needs_human": false, "suggested_reply": "We are tracking your parcel."}',
    '{"category": "billing", "priority": "HIGH", "summary": "Duplicate charge", '
    '"needs_human": false, "suggested_reply": "Refund initiated."}',
]


def main() -> None:
    for raw in TEST_CASES:
        try:
            parsed = safe_parse_model_json(raw)
            validated = validate_or_raise(parsed)
            print("SUCCESS:", validated)
        except ValueError as exc:
            print("FAILED:", str(exc))


if __name__ == "__main__":
    main()
```

### Notes for evaluation

- Full credit: Case 1 prints **`SUCCESS:`**; Case 2 prints **`FAILED: Invalid priority: 'HIGH'`**; parsing helpers left unchanged.
- Partial credit: validation logic works but error message format differs — note which check failed.
- No Groq API key required.
