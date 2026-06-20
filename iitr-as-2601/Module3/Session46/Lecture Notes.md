# Structured Outputs for Agents

## Introduction

Agents often sound fluent in plain English — but the **code**, **tools**, and **UI** behind them need **machine-readable JSON** they can parse on every call. Free-form paragraphs break dashboards, tool routers, and database inserts the moment wording shifts.

This session covers the full path from **contract** to **consumption**: **define a JSON schema** for agent responses, **prompt** the model to follow it, **parse** the raw text safely, and **validate** required fields before results reach a tool or dashboard.

**What you will learn:**

- **Define** a **JSON schema** that describes the exact agent response your application needs
- **Prompt** the model for **structured generation** so output conforms to that schema
- **Parse** model text into Python **dicts** and handle **malformed JSON** without crashing
- **Validate** **required fields** with a lightweight check before passing data to tools or UI

![Structured outputs for agents — free-form text breaks code; structured JSON with category, priority, and summary fields feeds dashboards and tools reliably](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session46/session46-01-structured-output-overview.png)

---

## Why Agents Need Structured Outputs

When an agent finishes a task, something else usually consumes the result — a **database row**, a **dashboard card**, or the **next tool call**. That consumer needs **predictable keys and types**, not free-form prose.

- **Official Definition:** **Structured output** is model text formatted as **JSON** (or another strict schema) so programs can **`parse`**, **`validate`**, and **`route`** it without guessing.
- **In Simple Words:** Instead of *"Your refund will take 5–7 days, probably"*, the agent returns `{"status": "approved", "days": 7}` — like a **filled government form**, not a handwritten essay.
- **Real-Life Example:** **IRCTC** needs `{ "from": "NDLS", "to": "BCT", "class": "SL" }` — not *"I think you want Mumbai next week."*

| Free-form reply | Structured JSON reply |
|---|---|
| Hard to auto-fill a UI table | Keys map directly to form fields |
| Regex breaks on wording changes | **`json.loads()`** gives a Python dict |
| Tool router cannot pick next step | **`"action": "refund"`** triggers the right function |

- **Common mistake:** Asking for JSON in the prompt but never **parsing** or **validating** — prose wrapped in `{` `}` still crashes production.
- **JSON refresher:** Agents speak **JSON** — objects `{}`, arrays `[]`, strings, numbers, booleans. Python's **`json`** module converts text ↔ **`dict`**. Always call **`json.loads()`** on model text; never treat a string as a dict by default.

---

## JSON Schema — The Application Contract

A **JSON Schema** is the **blueprint** your application owns — it declares **required keys**, **types**, and **allowed values**. The model fills the form; your schema defines the boxes.

- **Official Definition:** **JSON Schema** is a vocabulary for describing and validating JSON — **properties**, **types**, **required fields**, and **constraints** like **`enum`**.
- **In Simple Words:** The **instruction page** on a **board exam answer sheet** — fixed columns everyone must fill.
- **Real-Life Example:** A **passport form** marks required fields with a red asterisk — the schema does the same for JSON keys.

### ShopEasy Support Ticket Schema

Save as **`schemas/support_ticket_v1.json`** in your project folder:

```json
{
  "type": "object",
  "required": ["category", "priority", "summary", "needs_human", "suggested_reply"],
  "properties": {
    "category": { "type": "string", "enum": ["billing", "shipping", "product", "other"] },
    "priority": { "type": "string", "enum": ["low", "medium", "high"] },
    "summary": { "type": "string", "minLength": 5, "maxLength": 200 },
    "needs_human": { "type": "boolean" },
    "suggested_reply": { "type": "string" }
  },
  "additionalProperties": false
}
```

- **`required`** — keys that **must** appear; missing any one fails validation.
- **`enum`** — fixed menu of strings; stops `"super urgent!!!"` as a priority level.
- **`additionalProperties: false`** — reject surprise keys the UI does not expect.
- **Design habit:** Start from your **UI mock** or **tool signature** — work backwards to schema fields. Keep v1 **small** and testable.
- Store the schema as its own file alongside your system prompt (**`v1_system.txt`**) and config — one source of truth for output shape. Register the schema path in your agent config when you load prompt + settings together.

| Application step | Schema decision |
|---|---|
| Route to billing team | **`"category": "billing"`** |
| Show red badge | **`"priority": "high"`** |
| Display ticket title | **`"summary"`** string |
| Skip auto-reply | **`"needs_human": true`** |

![JSON schema as application contract — support_ticket_v1.json blueprint maps to required fields category, priority, summary, needs_human, and suggested_reply for ShopEasy support](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session46/session46-02-json-schema-contract.png)

---

## Structured Generation — Prompting for JSON

**Structured generation** constrains the model — through **prompt text** and **API settings** — to emit JSON matching your schema.

- **Official Definition:** **Structured generation** uses **prompt instructions** and **`response_format`** API flags to force a predefined output shape.
- **In Simple Words:** Tell the chef: *"Serve only in the standard steel tiffin, compartments labelled."*
- **Real-Life Example:** A **CBSE exam** says *"Write answers in the box only"* — same idea for JSON keys.

Add this block to **`v1_system.txt`**:

```
You are ShopEasy Support Classifier.
Return ONE JSON object only — no markdown, no text before or after.

REQUIRED SHAPE (all keys mandatory):
{
  "category": "billing" | "shipping" | "product" | "other",
  "priority": "low" | "medium" | "high",
  "summary": "one sentence, max 200 characters",
  "needs_human": true or false,
  "suggested_reply": "draft reply, or "" if needs_human is true"
}

RULES:
- Use lowercase enum values exactly as shown.
- Refunds, legal threats, or abuse → needs_human: true, suggested_reply: "".
```

- List **every required key** in the prompt — *"respond in JSON"* alone causes random omissions.
- Set **`temperature: 0.0`** in your config for stable classification output.

### Groq JSON Mode

Groq supports **`response_format={"type": "json_object"}`** on chat completions.

- Your messages must **mention JSON** — Groq rejects JSON mode otherwise.
- JSON mode guarantees **valid syntax**, not perfect **schema** adherence — you still **validate** fields in Python.
- Best beginner combo: **explicit schema in system prompt** + **JSON mode** on the API call.

![Structured generation — system prompt with required JSON shape plus Groq response_format json_object and temperature 0.0 for stable ShopEasy classifier output](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session46/session46-03-structured-generation.png)

---

## Parsing Model Output Safely

**Output parsing** turns the model's raw string into a Python **`dict`**. Models sometimes add markdown fences, preamble text, or truncate mid-brace — production code must **clean first**, then parse.

- **Official Definition:** **Defensive parsing** cleans raw text, attempts **`json.loads()`**, and returns clear errors when output is unusable.
- **In Simple Words:** Check the **SIM card** is inserted correctly before blaming the network.
- **Real-Life Example:** A failed **UPI payment** shows *"Could not read bank response"* — not a white-screen crash.

| Symptom | First fix |
|---|---|
| Wrapped in ` ```json ` | Strip code fences |
| Text before `{` | Slice from first `{` to last `}` |
| Truncated mid-key | Raise **`max_tokens`** |
| Single quotes `'key'` | Re-prompt — never use **`eval()`** |

```python
# safe_parse.py — defensive JSON parse for model output

import json  # Standard JSON parser
import re  # Match markdown fences

def strip_markdown_fences(text: str) -> str:
    """Remove ```json ... ``` wrappers if the model added them."""
    cleaned = text.strip()  # Trim outer whitespace
    match = re.match(r"^```(?:json)?\s*([\s\S]*?)\s*```$", cleaned, flags=re.IGNORECASE)
    return match.group(1).strip() if match else cleaned  # Inner JSON or original text


def extract_json_object(text: str) -> str:
    """If prose surrounds JSON, slice from first { to last }."""
    start, end = text.find("{"), text.rfind("}")  # Brace positions
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object braces found in model output.")
    return text[start : end + 1]  # Substring that should be one object


def safe_parse_model_json(raw: str) -> dict:
    """Strip fences, extract object, parse, type-check — one policy for all callers."""
    step1 = strip_markdown_fences(raw)  # Remove ``` fences
    step2 = extract_json_object(step1)  # Cut to {...} region
    try:
        data = json.loads(step2)  # String → Python values
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON parse failed: {exc}\nSnippet: {step2[:200]}") from exc
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON must be an object (dict).")
    return data  # Ready for validation
```

**How the code works:**

- **`strip_markdown_fences`** handles the most common demo mistake — triple-backtick wrappers.
- **`extract_json_object`** salvages *"Here is the JSON:"* preambles without unsafe **`eval()`**.
- **`ValueError`** with a **snippet** aids debugging without logging full customer text in production.

![Defensive parsing — strip markdown fences, extract JSON braces, json.loads to dict; clear errors instead of crashes like a failed UPI payment message](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session46/session46-04-defensive-parsing.png)

---

## Validation Before Tools or UI

Parsing proves **syntax**. **Validation** proves the dict is **usable** — right keys, types, enums, and business rules — before routing or tool calls.

- **Official Definition:** **Validation** checks data against rules before side effects like database writes or tool execution.
- **In Simple Words:** A **bouncer checking ID** — JSON shape is the ticket; validation confirms the name is on the list.
- **Real-Life Example:** An **Aadhaar form** won't submit with an empty PIN — block empty **`summary`** the same way.

```python
# validate_ticket.py — hand-written checks against schema (no extra library)

from typing import Tuple

ALLOWED_CATEGORIES = {"billing", "shipping", "product", "other"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}


def validate_ticket(data: dict, schema: dict) -> Tuple[bool, str]:
    """Return (True, 'ok') or (False, reason) on first failure."""
    for key in schema.get("required", []):
        if key not in data:
            return False, f"Missing required field: {key}"
    if data["category"] not in ALLOWED_CATEGORIES:
        return False, f"Invalid category: {data['category']!r}"
    if data["priority"] not in ALLOWED_PRIORITIES:
        return False, f"Invalid priority: {data['priority']!r}"
    if not isinstance(data["summary"], str) or len(data["summary"].strip()) < 5:
        return False, "summary must be a non-empty string (min 5 chars)."
    if not isinstance(data["needs_human"], bool):
        return False, "needs_human must be boolean."
    if data["needs_human"] and data["suggested_reply"].strip() != "":
        return False, "suggested_reply must be empty when needs_human is true."
    if schema.get("additionalProperties") is False:
        allowed = set(schema.get("properties", {}).keys())
        extra = set(data.keys()) - allowed
        if extra:
            return False, f"Unexpected fields: {sorted(extra)}"
    return True, "ok"


def validate_or_raise(data: dict, schema: dict) -> dict:
    """Raise ValueError on failure — uniform error handling for callers."""
    ok, message = validate_ticket(data, schema)
    if not ok:
        raise ValueError(message)
    return data


def route_to_ui(ticket: dict) -> dict:
    """Map validated dict to UI props — frontend never parses raw model text."""
    return {
        "title": ticket["summary"],
        "badge": ticket["priority"].upper(),
        "team": ticket["category"],
        "show_draft": not ticket["needs_human"],
        "draft_text": ticket["suggested_reply"],
    }
```

**How the code works:**

- **`required` from schema** is the single source of truth for mandatory keys.
- **Enum sets** catch typos like **`"Billing"`** or **`"HIGH"`** (wrong case).
- **Business rule** linking **`needs_human`** and **`suggested_reply`** catches logic errors parsing alone misses.
- **`route_to_ui`** runs only after validation — inner functions trust the dict shape.

### Gating Tool Calls After Validation

Structured output does not replace safety policy — tools should check **`needs_human`** and **`category`** even after validation passes.

```python
def maybe_call_refund_tool(ticket: dict, order_id: str) -> None:
    """Only draft a refund tool call when schema + business policy allow."""
    if ticket["category"] != "billing":
        return  # Wrong queue — skip tool
    if ticket["needs_human"]:
        return  # Human must approve refunds
    if ticket["priority"] != "high":
        return  # Policy: instant draft only for high-priority billing
    print(f"TOOL: create_refund_draft(order_id={order_id})")  # Placeholder for real call
```

- Validation guarantees **shape**; tool gates enforce **policy** — both layers stay separate.
- **Common mistake:** Auto-calling a refund tool because JSON parsed successfully — always read **`needs_human`** first.

![Validate before tools or UI — required fields, enums, and business rules gate; validated JSON routes to dashboard card and conditional refund tool](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session46/session46-05-validation-gate.png)

---

## Complete Pipeline — Classify, Parse, Validate, Route

The full path: **customer message** → **Groq with JSON mode** → **`safe_parse_model_json`** → **`validate_or_raise`** → **`route_to_ui` / tools**. If any step fails, stop before side effects.

```python
# pipeline_support_classifier.py — full structured output pipeline

import json  # Load schema file
import os  # GROQ_API_KEY from environment
from pathlib import Path  # File paths for schema and prompt files

from groq import Groq  # Groq chat API

from safe_parse import safe_parse_model_json  # Defensive parse
from validate_ticket import validate_or_raise, route_to_ui  # Validate + UI map

SCHEMA_PATH = Path("schemas/support_ticket_v1.json")  # Output contract on disk
PROMPT_PATH = Path("prompts/support_agent/v1_system.txt")  # System prompt with JSON rules
MODEL_NAME = "llama-3.3-70b-versatile"  # Model name from your config file


def classify_message(customer_text: str) -> dict:
    """Call model, parse JSON, validate — return trusted dict or raise ValueError."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))  # Load schema once per call
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8").strip()  # System prompt text from disk
    client = Groq(api_key=os.environ["GROQ_API_KEY"])  # Key from env, never hard-coded

    response = client.chat.completions.create(
        model=MODEL_NAME,  # Fixed model for consistent output during testing
        messages=[
            {"role": "system", "content": system_prompt},  # JSON contract + behaviour rules
            {"role": "user", "content": customer_text},  # Raw customer message to classify
        ],
        temperature=0.0,  # Low randomness for stable classification
        max_tokens=512,  # Enough room for JSON object
        response_format={"type": "json_object"},  # Groq JSON syntax mode
    )

    raw = response.choices[0].message.content  # Untrusted string until parsed + validated
    parsed = safe_parse_model_json(raw)  # dict or ValueError
    return validate_or_raise(parsed, schema)  # Trusted dict or ValueError


if __name__ == "__main__":
    samples = [
        "Where is my order 4412? It was supposed to arrive yesterday.",
        "I was charged twice for order 8821. Please refund the duplicate.",
    ]
    for msg in samples:
        print(f"\n--- {msg[:40]}... ---")
        ticket = classify_message(msg)  # Full pipeline
        print("Validated:", json.dumps(ticket, indent=2))
        print("UI payload:", route_to_ui(ticket))
```

**How the code works:**

- **`classify_message`** is the **single front door** — every caller gets the same parse + validate policy.
- **`response_format={"type": "json_object"}`** plus a strong system prompt gives reliable beginner results.
- Errors surface as **`ValueError`** — log them and optionally retry the API call with backoff when failures are transient.
- When you change a prompt or schema, track **schema pass rate** (% of test inputs that parse and validate) beside human review of answer quality.

### Checking Structured Output Quality

When you test an agent on a **fixed set of sample messages**, add programmatic checks beside reading the answers yourself.

| Check | Question |
|---|---|
| Parse success | Does every test row produce valid JSON? |
| Required fields | Any missing keys after parse? |
| Enum compliance | Any `"Priority": "High"` capitalization failures? |
| Business rules | Any **`needs_human: true`** with non-empty **`suggested_reply`**? |

- **Pass rate** = rows where **`safe_parse_model_json`** + **`validate_or_raise`** both succeed.
- **Regression signal:** If a new prompt reads nicer but pass rate drops, it is not ready to ship — JSON reliability beats clever prose.
- Log **`PIPELINE ERROR`** lines with a **timestamp** and **schema filename** so failures are visible during development.

---

## Activity 1 — Design a Schema on Paper

Read: *"The blue kettle I ordered arrived cracked. I want a replacement, not a refund."*

Write a JSON Schema with four **required** keys — **`issue_type`** (`damage`, `wrong_item`, `late_delivery`, `other`), **`resolution`** (`replace`, `refund`, `info_only`), **`priority`** (`low`, `medium`, `high`), **`summary`** (one sentence). Then write the JSON object you expect the model to return. Confirm every required key is present and enums are lowercase.

---

## Activity 2 — Break the Parser, Then Fix Validation

**Part A:** Save and run this snippet — confirm fence stripping recovers valid JSON:

```python
# test_parser.py — messy model output with markdown fences

from safe_parse import safe_parse_model_json

bad_output = (
    "Here is the classification:\n\n"
    "```json\n"
    '{"category": "product", "priority": "medium", "summary": "Kettle arrived cracked", '
    '"needs_human": false, "suggested_reply": "We will send a replacement."}\n'
    "```"
)
print(safe_parse_model_json(bad_output))  # Should parse after cleanup
```

Try a second string with **no closing brace** — confirm you get a clear **`ValueError`**, not an unhandled crash.

**Part B:** Run **`validate_ticket`** on this dict:

```python
sample = {"category": "billing", "priority": "HIGH", "summary": "Dup charge",
          "needs_human": False, "suggested_reply": "Refund initiated."}
```

List every validation error. Fix the dict until all checks pass, then call **`route_to_ui`** and note which UI fields change.

---

## Debugging When JSON Fails

- Confirm **`response_format={"type": "json_object"}`** is set and the system prompt **mentions JSON**.
- Print **`raw`** before parsing — compare with a known-good saved response from an earlier successful run.
- Check **`max_tokens`** — truncated JSON often ends mid-string.
- Ensure **`required`** keys in the prompt match the schema file exactly.
- Run the same message twice at **`temperature=0.0`** — if shape still drifts, tighten enum wording.

---

## Key Takeaways

- **Structured outputs** turn agent answers into **JSON objects** your code, tools, and UI consume without regex on free text.
- A **JSON schema** is the **application contract** — define **`required`** keys, **types**, and **enums** in a dedicated file stored alongside your system prompt.
- **Structured generation** pairs **explicit schema instructions** with Groq **`json_object`** mode — syntax reliability still needs your **validator** for semantics.
- **Defensive parsing** strips fences, extracts `{...}`, and raises clear errors — never **`eval()`** raw model text.
- **Validate before side effects** — routing, auto-reply, and tool calls run only after required fields and business rules pass.

These patterns are the foundation for any agent that must hand results to **code**, **tools**, or a **UI** — not just display text to a user.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Structured output** | Concept | Model response in strict JSON for programs to parse |
| **JSON Schema** | Specification | Blueprint: properties, types, required, enums |
| **`required`** | Schema keyword | Keys that must exist in every valid response |
| **`enum`** | Schema keyword | Allowed string values for a field |
| **`additionalProperties: false`** | Schema keyword | Reject unknown extra keys |
| **Structured generation** | Practice | Constrain output via prompt + API format flags |
| **`response_format={"type": "json_object"}`** | Groq API | Request JSON-syntax assistant message |
| **`json.loads()`** | Function | Parse JSON string → Python object |
| **`safe_parse_model_json()`** | Code pattern | Clean + parse + type-check in one function |
| **`validate_or_raise()`** | Code pattern | Return dict or raise **`ValueError`** |
| **Schema pass rate** | Metric | % of test inputs that parse and validate |
| **`pathlib.Path`** | Library | Load schema and prompt files safely |
| **`GROQ_API_KEY`** | Env var | API key from environment, not source code |
