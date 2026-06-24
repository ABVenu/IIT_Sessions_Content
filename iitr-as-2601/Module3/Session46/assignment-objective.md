# Objective Assignment: Structured Outputs for Agents

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A **hospital notes** agent extracts patient data into a SQL table. The `weight` column is an **integer**, but the model returns `"80 KGs"` in free-form text.

What is the **core problem** this causes for the application?

A. The answer may be **factually correct in English** but **unusable** for a typed database column  
B. SQL tables cannot store numbers above 80  
C. The model hallucinated because medical notes were missing  
D. JSON Schema automatically converts `"80 KGs"` to integer 80

**Correct Answer:** A

**Answer Explanation:**  
A is correct — structured output exists so downstream systems receive **predictable types and keys**, not prose that breaks inserts.

B is incorrect — there is no 80 kg SQL limit; the issue is **format/type mismatch**. C is incorrect — the scenario is about **output shape**, not hallucination. D is incorrect — JSON Schema does not auto-cast strings with units into integers.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A developer receives this string from an LLM API: `'{"category": "billing", "priority": "low"}'`.

What is the **correct** way to turn it into a Python **`dict`** for further processing?

A. Call **`json.loads()`** on the string  
B. Assign the string to a variable named `dict`  
C. Wrap the string in **`eval()`** because it looks like a dictionary  
D. Split the string on spaces and hope keys appear

**Correct Answer:** A

**Answer Explanation:**  
A is correct — the standard library **`json.loads()`** safely parses JSON text into Python objects.

B is incorrect — a string variable is still a string, not a parsed dict. C is incorrect — **`eval()`** on model output is unsafe and can execute malicious code. D is incorrect — naive splitting cannot parse JSON structure reliably.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

In a ShopEasy support-ticket **JSON Schema**, the **`required`** array lists: `category`, `priority`, `summary`, `needs_human`, `suggested_reply`.

What does **`required`** enforce?

A. Those keys **must appear** in every valid model response — missing any one should fail validation  
B. The model may omit keys it does not know and still pass validation  
C. Only the first key in the list is mandatory  
D. Required fields are optional in the system prompt but mandatory in the UI only

**Correct Answer:** A

**Answer Explanation:**  
A is correct — **`required`** is the contract that every listed key must be present (use **`null`** if unknown, not omission).

B is incorrect — omitting required keys breaks schema validation. C is incorrect — **all** listed keys are mandatory. D is incorrect — validation applies to the **parsed dict**, not UI-only rules.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A team stores **`support_ticket_v1.json`** under **`schemas/`** and **`v1_system.txt`** under **`prompts/support_agent/`**.

Why keep these as **separate files**?

A. The **schema** is the application's validation blueprint; the **prompt** instructs the model — they serve different roles and should stay aligned but not merged  
B. Groq rejects API calls unless schema and prompt are in one file  
C. Python cannot load two files in one project  
D. JSON Schema files must be named `.txt` for Groq JSON mode

**Correct Answer:** A

**Answer Explanation:**  
A is correct — prompt text shapes generation; the schema file is what Python compares against after parsing.

B is incorrect — Groq has no single-file requirement. C is incorrect — projects routinely load multiple files. D is incorrect — schema files use **`.json`**, not `.txt`.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A ShopEasy engineer enables Groq **`response_format={"type": "json_object"}`** and lists every required key in the system prompt.

After deployment, some responses are **valid JSON** but use **`"priority": "HIGH"`** (wrong case) instead of **`"high"`**.

What is the **best explanation**?

A. JSON mode guarantees **syntax**, not full **schema semantics** — you still need a **Python validator** for enums and types  
B. JSON mode is broken and should never be used  
C. The fix is to remove the system prompt because JSON mode replaces it  
D. Raising **`temperature`** to 1.0 will fix enum casing

**Correct Answer:** A

**Answer Explanation:**  
A is correct — **`json_object`** mode helps produce parseable JSON; **enum casing** is enforced by your **`validate_ticket`** logic.

B is incorrect — JSON mode is useful when paired with validation. C is incorrect — strong prompt text plus JSON mode is the recommended combo. D is incorrect — higher temperature increases randomness and worsens consistency.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A support dashboard auto-fills ticket fields from model output. The team calls **`json.loads()`** on the raw string and immediately updates the UI. On some runs, tickets show **`"Billing"`** in a dropdown that only accepts **`billing`**, **`shipping`**, **`product`**, **`other`**.

Which step was **skipped**?

A. **Validation** against the schema (required keys, enums, types) before routing to the UI  
B. Training a new embedding model  
C. Increasing **`max_tokens`** on every request  
D. Converting the prompt file from `.txt` to `.yaml`

**Correct Answer:** A

**Answer Explanation:**  
A is correct — parsing proves **syntax**; **validation** proves the dict is **usable** before side effects like UI updates.

B is irrelevant to output-shape enforcement. C might help truncated JSON but does not fix wrong enum values. D is unrelated to enum validation.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

You are designing the ShopEasy **`support_ticket_v1.json`** schema file.

Which items belong in the **JSON Schema file** (not just the system prompt)?

A. **`"required"`** array listing mandatory keys  
B. **`"properties"`** with per-field **`type`** and **`enum`** constraints  
C. The customer's raw chat message text  
D. **`"type": "object"`** declaring a single JSON object output  
E. Instructions like *"You are ShopEasy Support Classifier"*

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D are schema vocabulary — contract structure, field definitions, and top-level object type.

C is incorrect — user messages are runtime inputs, not schema content. E is incorrect — persona instructions belong in the **system prompt**, not the schema blueprint.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A model returns messy text:

```text
Sure, here is the ticket JSON:

```json
{"category": "shipping", "priority": "medium", "summary": "Late delivery", "needs_human": false, "suggested_reply": "We are tracking your parcel."}
```
```

Which **defensive parsing** steps are **appropriate** before **`json.loads()`**?

A. **`strip_markdown_fences`** to remove triple-backtick wrappers  
B. **`extract_json_object`** to slice from the first **`{`** to the last **`}`**  
C. **`eval()`** on the raw string because it starts with `{`  
D. Raise a clear **`ValueError`** with a short snippet if parsing still fails  
E. Delete the schema file so validation cannot fail

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D match the taught clean → extract → parse → clear-error pipeline.

C is incorrect — never use **`eval()`** on model output. E is incorrect — removing the schema removes safety; it does not fix parsing.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

ShopEasy runs this pipeline for each customer message:

**Groq call (JSON mode)** → **`safe_parse_model_json`** → **`validate_or_raise`** → **`route_to_ui`**

Which statements about this design are **correct**?

A. **`safe_parse_model_json`** should run **before** **`validate_or_raise`** because validation needs a Python **`dict`**, not a raw string  
B. **`route_to_ui`** should run **only after** validation passes  
C. If parsing fails, the app should still write to the database so no data is lost  
D. **`validate_or_raise`** can raise **`ValueError`** so callers use one **`try`/`except`** path for parse and validation failures  
E. Groq JSON mode removes the need for **`validate_or_raise`** entirely

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D describe the correct order: parse → validate → route, with unified error handling.

C is incorrect — invalid output must **not** reach side effects; that is the gate/checkpoint pattern. E is incorrect — JSON mode does not replace semantic validation.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A ShopEasy staging agent intermittently returns truncated or malformed JSON. The system prompt and schema file already match.

Which **debugging actions** are **sound**?

A. Print the **`raw`** model string before parsing and compare with a known-good saved response  
B. Confirm **`response_format={"type": "json_object"}`** is set **and** the system prompt **mentions JSON**  
C. Check whether **`max_tokens`** is too low, causing JSON cut off mid-string  
D. Remove all **`required`** keys from the schema so validation always passes  
E. Run the same message twice at **`temperature: 0.0`** to see if output shape still drifts

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are the practical debugging checklist items for syntax and shape drift.

D is incorrect — weakening the schema hides bugs instead of fixing generation or parsing issues.
