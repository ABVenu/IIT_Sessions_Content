# Prompt Engineering

In the **previous** lesson you saw what an **LLM** is: text becomes **tokens**, a **Transformer** predicts the next token, and settings like **temperature** change tone. You called **Gemini** with **`fetch`** and watched the same sky question sound factual at low temperature and more creative at high temperature.

That engine does not read your mind. It reads **the words you send**. **Prompt engineering** is the skill of writing those words so the model gives **useful, checkable** answers—especially when you integrate AI beside **`campus_api`**, your docs page, and the review habits you already use in GenAI labs.

![Prompt parts flow into the model: role, context, task, format, and examples shape the answer you get back](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session39/session39-01-prompt-components.png?v=20261019)

## What you will learn in this lesson

- **Prompt structure** — role, context, task, format, constraints, and optional examples
- **Zero-shot**, **few-shot**, and **chain-of-thought** prompting
- **Role prompting** — personas that change depth and vocabulary
- **Structured output** — JSON and fixed shapes you can parse or compare to **`StudentOut`**
- **Hands-on** — one small **Gemini** script that swaps prompt **techniques** and prints results

Connecting idea: The LLM lesson explained **how the machine writes**; this lesson explains **what you type before it writes**.

---

## What is prompt engineering?

- **Official Definition:** **Prompt engineering** is the practice of designing, organising, and refining natural-language instructions to an LLM so outputs meet task, format, and safety requirements.
- **In Simple Words:** You learn to **ask clearly** so the model stops guessing what you meant.
- **Real-Life Example:** At a railway counter, “Ticket” gets a frown; “Two sleeper, Pune to Nagpur, tomorrow 6 am” gets a printout. Same clerk—better instruction slip.

| Without structure | With structure |
| --- | --- |
| “Fix my API” | “You are a FastAPI tutor. Here is my 404 on `GET /students/99`. List three checks in numbered steps. Do not invent routes.” |
| Vague, hallucination-prone | Scoped, easier to verify in `/docs` |

**Need:** Integration work fails when prompts are one-line wishes. Your backend still owns truth; the prompt **steers** the draft.

**Common mistake:** Blaming the model for a wrong field name when the prompt never listed **`hostel_name`** or said “use only these keys.”

---

## Anatomy of a well-structured prompt

Treat a strong prompt like a **form with labeled boxes**. Order can vary; missing boxes cause drift.

| Block | Purpose | Campus-flavoured hint |
| --- | --- | --- |
| **Role** | Who the model should act as | “Senior backend reviewer for FastAPI + SQLAlchemy” |
| **Context** | Facts you provide | Paste one real error line or one JSON row—not the whole repo |
| **Task** | One main job | “Explain this 404 in plain English” |
| **Format** | Shape of the answer | “Three bullets, max 12 words each” |
| **Constraints** | Must / must not | “Do not invent columns; say ‘unknown’ if missing” |
| **Examples** (optional) | Show the pattern | One mini Q→A pair (**few-shot**) |

![Zero-shot sends task only; few-shot adds example pairs; chain-of-thought asks for visible reasoning steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session39/session39-02-shot-and-cot.png?v=20261019)

**Weak vs strong (same intent)**

- **Weak:** “Explain StudentOut.”
- **Strong:** “**Role:** API docs writer. **Context:** Our list endpoint returns objects with `id`, `full_name`, `email`, `city`, `marks`, `hostel_id`, `hostel_name`. **Task:** Explain each field to a non-tech student. **Format:** Markdown table, two columns: Field, Meaning. **Constraints:** Do not add fields we did not list.”

**Delimiter pattern (keeps long context readable)**

When you paste logs or JSON, wrap them so the model knows what is data vs instruction:

```text
### CONTEXT START
(paste one traceback line or one StudentOut row)
### CONTEXT END

Task: ...
Format: ...
```

**Common doubt:** “Should I write in Hindi?” — Match the language you want **back**. For API field docs, English keys with simple English explanations reduce mixed-key bugs.

Connecting idea: Structure is independent of **technique**—you can use zero-shot or few-shot **inside** these blocks.

### Activity — label the blocks

Take the **strong** prompt above. On paper, underline which sentence belongs to role, context, task, format, and constraints.

---

## Zero-shot prompting

- **Official Definition:** **Zero-shot** prompting gives **instructions and context only**, with **no worked examples** of input→output in the prompt.
- **In Simple Words:** “Here is the job—figure it out from my words alone.”
- **Real-Life Example:** First day at a new shop: manager says “Stack milk bags, expiry forward”—no demo, but clear rules.

**When zero-shot works well**

- Simple definitions, short summaries, rephrasing text you paste
- Tasks the model saw often in training (explain HTTP 404, define ORM)

**When zero-shot struggles**

- Odd JSON shapes, strict key names, niche internal names like **`campus.log`**
- Multi-step debugging where you want the model to **show its work**

**Example zero-shot prompt (text you send to Gemini or Claude)**

```text
Task: In two sentences, explain what a 404 means on a GET /students/{id} route.
Format: Exactly two sentences, no bullet points.
Constraint: Do not mention databases by name unless needed.
```

**Common doubt:** “Is zero-shot the same as no system message?” — Not exactly. Apps may add a hidden system line; **zero-shot** here means **your visible prompt has no examples**.

---

## Few-shot prompting

- **Official Definition:** **Few-shot** prompting includes **one or more input–output examples** in the prompt so the model mimics the pattern.
- **In Simple Words:** Show one solved copybook sum before asking the next sum.
- **Real-Life Example:** Hostel warden shows a filled leave form, then asks you to fill yours the **same way**.

**Why it helps**

- Locks **tone**, **length**, and **field names**
- Reduces invented keys when examples use real **`StudentOut`** names

**Example few-shot fragment**

```text
Example 1
User: Field "marks" — meaning?
Assistant: Integer score for the student, used in filters like high-marks list.

Example 2
User: Field "hostel_name" — meaning?
Assistant: Read-only building label from the hostel relation, not sent on create.

Now answer for field "city".
```

**Guidelines**

- **Two or three** examples usually beat ten (context window cost)
- Examples must be **correct**—wrong examples teach wrong habits
- Match **format** you want in the final answer

**Common mistake:** Examples in casual Hindi while you demand English JSON—mixed signals produce mixed output.

### Activity — one-shot upgrade

Start from zero-shot “Explain `hostel_id`.” Add **one** example pair for another field. Compare answers for consistency of length and tone.

---

## Chain-of-thought prompting

- **Official Definition:** **Chain-of-thought (CoT)** prompting asks the model to produce **intermediate reasoning steps** before the final answer.
- **In Simple Words:** “Show your rough work, then give the final line.”
- **Real-Life Example:** Exam invigilator allows scratch work on the right side, final answer boxed on the left.

**Phrases that trigger CoT**

- “Think step by step.”
- “First list facts from the prompt, then conclude.”
- “Number your reasoning 1–3, then write **Answer:** on a new line.”

**When CoT helps**

- “Why might this query return empty when city filter is Pune?”
- Comparing two HTTP status choices (404 vs 422)

**When to skip CoT**

- You need **only** JSON for code to parse—reasoning adds noise unless you strip it in code
- Very short factual lookups

**Example CoT prompt**

```text
Context: GET /students?city=Pune returns [] but Pune rows exist in the database.
Task: Suggest three debugging checks for a FastAPI app.
Think step by step. After reasoning, end with "Checks:" and a numbered list of exactly three items.
Constraint: Do not invent middleware we never mentioned.
```

**Trade-off:** CoT uses more **tokens** (cost + context). Use when verification matters more than brevity.

Connecting idea: CoT can combine with **role** (“You are a backend tutor”) and **structured** final sections.

---

## Role prompting

- **Official Definition:** **Role prompting** assigns a **persona** (job, expertise, audience) so the model adopts matching vocabulary, depth, and priorities.
- **In Simple Words:** “Answer **as** this kind of professional.”
- **Real-Life Example:** Same health question to a friend vs a doctor—different words, same topic.

| Role angle | Effect on answer |
| --- | --- |
| “FastAPI instructor for beginners” | Short steps, less jargon |
| “Strict code reviewer” | Points out missing validation first |
| “Exam writer” | Adds edge-case questions |

**Role is not permission to invent facts.** A “database admin” role does not let the model see **`campus.db`**. You still pass **context** or query SQL yourself.

**Same question, different role (illustrative)**

- **Task:** “What is dependency injection in FastAPI?”
- **Role A — peer student:** Short analogy, one `Depends` mention.
- **Role B — technical interviewer:** Definition plus “when would you inject `get_db`?”

**Common mistake:** Role without **constraints**—“senior architect” may hallucinate microservices you do not run.

![Role sets voice and depth; context and constraints still bound facts](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session39/session39-03-role-and-constraints.png?v=20261019)

### Activity — role swap

Pick one concept from your backend work (CORS, 422, or background log). Ask the same question twice with roles **beginner tutor** vs **strict reviewer**. Note which answer you would ship to a teammate.

---

## Structured output prompting

- **Official Definition:** **Structured output prompting** instructs the model to reply in a **machine-friendly shape** (JSON, YAML, fixed keys) so programs or humans can validate quickly.
- **In Simple Words:** “Fill this form exactly—no extra columns.”
- **Real-Life Example:** Board exam OMR sheet—bubbles in defined positions, not essay on the margin.

**Patterns that improve reliability**

- List **allowed keys** explicitly
- Say **“Return ONLY JSON, no markdown fence”** if your parser is strict
- Provide a **one-line schema** or tiny template
- Repeat **“If unknown, use null”** for optional fields

**Template example aligned with your API**

```text
Return ONLY a JSON object with keys:
  "field_name", "meaning", "in_create_body" (true/false)
One object for the field "email".
No markdown. No extra keys.
```

**Validation habit (developer-side)**

- Parse with `JSON.parse` in Node or `json.loads` in Python inside try/except
- Reject if unexpected keys appear before trusting text in production

**Hallucination guard:** Structured prompts **reduce** stray fields; they do **not** replace running **`GET /students/1`** in `/docs`.

![Structured prompt specifies keys; parser validates; API remains source of truth](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session39/session39-04-structured-json.png?v=20261019)

Connecting idea: Structured output is how backend routes later **consume** LLM text safely—today you practise the prompt side.

### Full code — validate structured JSON in Python

After a **structured** Gemini run, practise parsing like a FastAPI route would.

```python
# validate_llm_json.py — parse model JSON safely (run output pasted into SAMPLE)

import json  # Standard library JSON parser

SAMPLE = '{"status_code": 404, "meaning": "Row not found", "fix_hint": "Check id exists"}'  # Replace with your model text

def main():
    text = SAMPLE.strip()  # Remove accidental newlines
    if text.startswith("```"):  # Model sometimes adds fences despite instructions
        raise ValueError("Strip markdown fences before parsing")  # Fail in dev, fix prompt
    data = json.loads(text)  # Throws if not valid JSON
    allowed = {"status_code", "meaning", "fix_hint"}  # Keys you asked for
    extra = set(data.keys()) - allowed  # Detect hallucinated keys
    if extra:
        raise ValueError(f"Unexpected keys: {extra}")  # Reject before using in app
    print("OK:", data)  # Safe dict for downstream code


if __name__ == "__main__":
    main()  # Entry point
```

**How the code works:**

- **`json.loads`** is the gate—never trust raw strings in **`INSERT`** or response builders.
- **Allowed-key check** catches extra fields even when JSON is syntactically valid.
- If fences appear, tighten the prompt: **“No markdown, no backticks.”**

---

## System, user, and assistant turns (awareness)

Chat APIs often send three **roles**:

| Role | Typical content |
| --- | --- |
| **system** | Hidden product rules (tone, safety) |
| **user** | What you type—including your engineered prompt |
| **assistant** | Prior model replies in a multi-turn chat |

- **Official Definition:** A **system message** sets persistent behaviour for the thread; **user messages** carry tasks and context.
- **In Simple Words:** System = office policy poster; user = today’s form on the desk.
- **Real-Life Example:** Bank IVR says “English or Hindi” once (system); you ask balance (user).

In **`prompt_lab.mjs`** you send one combined **user** string. In products, split **role** into **system** and put **context + task** in **user** for clarity.

---

## Technique comparison (quick reference)

| Technique | You provide | Best for | Watch out |
| --- | --- | --- | --- |
| **Zero-shot** | Task + format only | Quick explain, rewrite | Invented field names |
| **Few-shot** | 1–3 examples | Tone, key names, tables | Bad examples copy errors |
| **Chain-of-thought** | “Step by step” | Debug reasoning | Long answers, extra tokens |
| **Role** | Persona line | Depth and audience | Overconfident fiction |
| **Structured** | Key list / schema | JSON for code | Invalid JSON, markdown wrappers |

---

## Hands-on — `prompt_lab.mjs` (Gemini, free tier)

Reuse **`llm_token_lab/.env`** with **`GEMINI_API_KEY`** from the previous lesson. One script switches **technique**; you read differences in the console.

```bash
cd llm_token_lab  # Same folder as gemini_ask.mjs
node prompt_lab.mjs  # Run after editing TECHNIQUE below
```

### Full code — `prompt_lab.mjs`

```javascript
// prompt_lab.mjs — compare prompt techniques with one Gemini call

import "dotenv/config"; // Load GEMINI_API_KEY from .env

const TECHNIQUE = "zero_shot"; // Change to: few_shot | cot | role | structured

const key = process.env.GEMINI_API_KEY; // Never hard-code secrets
if (!key) {
  throw new Error("Missing GEMINI_API_KEY in .env"); // Stop early with clear fix
}

const PROMPTS = {
  zero_shot: [
    "Task: Explain what HTTP status 404 means on GET /students/{id}.",
    "Format: Two short bullet points.",
    "Constraint: Do not invent custom status codes.",
  ].join("\n"),
  few_shot: [
    "Copy the style of the examples.",
    "Example:",
    "Q: What does 422 mean on POST /students?",
    "A: Validation failed before DB write; fix body shape.",
    "Example:",
    "Q: What does 201 mean on POST /students?",
    "A: Row created; response includes id and hostel_name.",
    "Q: What does 404 mean on GET /students/{id}?",
    "A:",
  ].join("\n"),
  cot: [
    "Context: Client GET /students/9999 returns 404.",
    "Think step by step: list possible causes in FastAPI + SQLAlchemy.",
    "After reasoning, write Final: and one sentence for the user.",
    "Constraint: Do not claim rows exist without evidence.",
  ].join("\n"),
  role: [
    "Role: You are a patient FastAPI teaching assistant for first-year students.",
    "Task: Explain Depends(get_db) in plain English.",
    "Format: Three numbered lines, max 15 words each.",
    "Constraint: No advanced microservice architecture.",
  ].join("\n"),
  structured: [
    "Return ONLY JSON with keys: status_code, meaning, fix_hint.",
    "Topic: 404 on GET /students/{id} when id missing in campus.db.",
    "No markdown fences. No extra keys.",
  ].join("\n"),
};

const prompt = PROMPTS[TECHNIQUE]; // Pick block matching TECHNIQUE constant
if (!prompt) {
  throw new Error("Unknown TECHNIQUE — use zero_shot | few_shot | cot | role | structured"); // Guard typo
}

const url =
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" +
  key; // Same endpoint pattern as previous gemini_ask.mjs

const response = await fetch(url, {
  method: "POST", // JSON API call
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    contents: [{ parts: [{ text: prompt }] }], // Full prompt string
    generationConfig: { temperature: 0.2 }, // Low temp for teaching comparisons
  }),
});

const data = await response.json(); // Parse response
const text = data.candidates?.[0]?.content?.parts?.[0]?.text ?? JSON.stringify(data); // Printed answer

console.log("TECHNIQUE:", TECHNIQUE); // Which pattern you ran
console.log("--- PROMPT SENT ---\n", prompt); // Audit what the model saw
console.log("--- MODEL OUTPUT ---\n", text); // Compare techniques across runs
```

**How the code works:**

- **`TECHNIQUE`** selects a pre-written prompt block—change it, rerun, compare output shape.
- **`temperature: 0.2`** keeps comparisons stable; style differences come mostly from **prompt**, not randomness.
- **`structured`** run should be checked: valid JSON? extra keys? markdown fences?
- Same **key hygiene** as before: local Node only, not browser **`fetch`**.

### Lab flow

Run **`zero_shot`**, then **`few_shot`**, **`cot`**, **`role`**, and **`structured`**—one line in your notes per technique on tone, length, and parseability.

---

## Prompting for your existing GenAI lab workflow

You already wrap Claude with **stack rules** and **one TASK** when editing **`campus_api`**. That wrapper **is** prompt engineering:

| Lab habit | Prompt block it maps to |
| --- | --- |
| “Do not drop CORS or upload” | **Constraints** |
| “Return only the new route function” | **Format** |
| “Use StudentOut” | **Context** + **structured** key names |
| “SQLAlchemy 2 select()” | **Examples** or **constraints** |

**Logic:** Better prompts reduce rewrite loops; they do **not** remove **`uvicorn`** testing.

**Common errors in backend AI drafts (prompt fixes)**

| Draft problem | Prompt fix |
| --- | --- |
| In-memory list instead of DB | Constraint: “No Python list as database.” |
| Missing `hostel_name` in example | Few-shot example with full JSON keys |
| Whole-file rewrite | Format: “Return one function only.” |

---

## Responsible prompting (integrated)

- Never paste **`.env`**, API keys, or real student PII into prompts.
- Say **“use only the context below”** when you paste snippets—reduces invented routes.
- For production, log **prompt + model version**, not just the answer.
- **Temperature:** Use **low** values for structured JSON; higher for brainstorming copy.

**Hallucination vs bad prompt (examples)**

| Situation | Likely cause | Prompt fix |
| --- | --- | --- |
| Model adds `gpa` field | No schema in prompt | Structured keys list + few-shot without `gpa` |
| Long essay when you wanted JSON | Missing format block | “JSON only, no prose” |
| Wrong HTTP verb for your app | Vague task | Context: “We use GET list with ?city=” |
| Confident student count | No data provided | Constraint: “Do not guess counts; say unknown” |

---

## If output is weak — tune in this order

Clarify **task** → add **format** → add **constraints** → add one **few-shot** → add **CoT** only if needed → **lower temperature** if wording drifts. Same order you already use when refining Claude drafts on **`campus_api`**.

---

## Hands-on checklist

1. Write one **structured** prompt for a single **`StudentOut`** field without opening the lab script.
2. Run **`prompt_lab.mjs`** for all five **`TECHNIQUE`** values; keep a one-line note per output.
3. Rewrite a weak one-line prompt from your own project using **role + task + format + constraints**.
4. Combine **CoT** with **role** in a single prompt on paper—check it is not contradictory (short final JSON + long reasoning needs clear separators).
5. Paste one **structured** model reply into **`validate_llm_json.py`**; fix prompt if fences or extra keys appear.

---

## Key Takeaways

- **Prompt engineering** turns the LLM from a guessing machine into a **directed** tool—structure matters as much as model choice.
- **Zero-shot**, **few-shot**, and **CoT** trade simplicity against control and token cost; pick per task.
- **Role** shapes voice; **context** and **constraints** shape facts—roles do not replace **`/docs`** or SQL.
- **Structured output** prompts prepare you to wire LLM replies into FastAPI routes with parsing and validation.
- Next work in the course will **use** these patterns inside features and agents—today you built the vocabulary and a repeatable Gemini lab.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **Prompt engineering** | Designing instructions to get reliable LLM outputs |
| **Zero-shot** | Prompt with no in-prompt examples |
| **Few-shot** | Prompt with one or more input–output examples |
| **Chain-of-thought (CoT)** | Ask for visible reasoning before the final answer |
| **Role prompting** | Persona that sets expertise and tone |
| **Structured output** | JSON or fixed keys for machine validation |
| **Context block** | Facts you supply (errors, schema, sample row) |
| **Constraints** | Must-not rules and boundaries |
| **Format block** | Bullets, tables, JSON-only, length limits |
| **prompt_lab.mjs** | Script switching five technique prompts |
| **TECHNIQUE** | Constant selecting which prompt block runs |
| **temperature 0.2** | Low randomness for technique comparison |
| **Hallucination** | Confident text not grounded in your data |
| **StudentOut** | Reference schema for structured examples |
| **GEMINI_API_KEY** | Loaded from `.env` for local lab calls |
| **System message** | Persistent behaviour instructions in chat APIs |
| **User message** | Task + context you send each turn |
| **Delimiter blocks** | CONTEXT START/END around pasted data |
| **validate_llm_json.py** | Parse and key-check structured model output |
| **json.loads** | Python parse step before trusting LLM JSON |
