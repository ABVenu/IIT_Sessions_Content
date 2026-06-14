# Mastering Prompt Engineering

## Context of This Session

In the previous session, you learned how **LLMs** generate text token by token, what **context windows** limit, and why **hallucinations** happen. You also saw that fluent language does not mean the model stores verified facts — it predicts likely text.

This session answers the next question: **how do you instruct the model so answers stay useful and consistent** — especially when you are building **beginner agents** that must follow rules without you watching every reply.

**In this session, you will:**

- Distinguish **system** and **user** roles and write a clear **system prompt** for a bounded task
- Apply **zero-shot** and **few-shot** examples to improve answer format and consistency
- Use **chain-of-thought prompting** for multi-step reasoning on structured problems
- Assemble **reusable prompt templates** suitable for a single-agent workflow

---

## What Is Prompt Engineering?

- **Official Definition:** **Prompt Engineering** is designing, testing, and refining the text instructions you send to an LLM so outputs are accurate, consistent, and useful for your task.
- **In Simple Words:** Writing a clear brief for a smart intern who has read a lot but will guess when the brief is vague.
- **Real-Life Example:** A **wedding caterer** needs guest count, veg/non-veg split, budget, and serving time — not just *"make it nice."* Prompts need that same level of detail.

| Vague prompt | Specific prompt |
|---|---|
| *"Tell me about loans."* | *"You are a bank FAQ bot. Explain home loans in 3 bullet points for a first-time buyer. Do not quote interest rates."* |
| Output drifts, may invent numbers | Output stays on topic; format is predictable |

![Vague vs specific prompts — clear, detailed instructions get reliable outputs; fuzzy wishes do not](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-vague-vs-specific-prompt.png)

- **Common doubt:** *"Isn't the AI smart enough without instructions?"* — It is fluent, not psychic. It fills gaps with plausible-sounding guesses unless you close those gaps in the prompt.
- **Why it matters for agents:** An agent runs the same prompt pattern many times. Small weaknesses become repeated mistakes at scale.

---

## System Prompts vs User Prompts

Every chat with an LLM has two layers of instruction. Understanding the split is the foundation of reliable agent design.

- **Official Definition:** A **System Prompt** sets persistent background rules — role, scope, tone — for the whole conversation. A **User Prompt** is the live message the human or your app sends on each turn.
- **In Simple Words:** The **system prompt** is the staff briefing before the restaurant opens. The **user prompt** is what the customer orders at the table.
- **Real-Life Example:** A **college helpdesk bot** might have a system rule: *"Answer only admission and fee questions."* When a student types *"What is the last date for scholarship?"* — that question is the user prompt.

### How the Two Roles Work Together

- The **system prompt** is set **once** at the start — persona, boundaries, tone, and workflow rules live here.
- The **user prompt** changes **every turn** — questions, pasted documents, and follow-ups live here.
- The model **always reads both** — every user message is interpreted inside the frame the system prompt created.
- **Common mistake:** Putting long rules only in the first user message. In real APIs, stable rules belong in the **system** slot so they are not buried in chat history.

![System prompt vs user prompt — backstage rules set once shape every reply; the user message is the live question each turn](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session24/session24-01-system-vs-user-prompt.png)

| Role | Who sets it | What it controls |
|---|---|---|
| **System** | Developer / you (once) | Persona, scope, tone, step-by-step workflow |
| **User** | End user / your app (each turn) | The actual question or task for this moment |

### Three Ingredients of a Strong System Prompt

A bounded beginner agent system prompt usually has three parts:

| Ingredient | Purpose | Example line |
|---|---|---|
| **Persona** | Who the AI is | *"You are Meera, a calm campus library assistant."* |
| **Scope** | What it will and will not do | *"Only answer library timings, issue rules, and fines."* |
| **Tone & Rules** | How it should respond | *"Use short sentences. If unsure, escalate to the librarian."* |

### Writing a System Prompt for a Bounded Task

```python
# system_prompt.py — background rules for a bounded study helper

system_prompt = """
You are Arjun, a patient study buddy for first-year college students in India.

Scope:
- Only help with study planning, revision tips, and explaining pasted syllabus topics.
- Do not write full exam answers word-for-word. Guide the student to think.
- Off-topic (health, politics): "I focus on study help only — ask your counsellor."

Tone and rules:
- Use simple English. Explain jargon in one plain sentence.
- Keep replies under 150 words. End with one 10-minute action step.
"""

print(f"System prompt ready — {len(system_prompt)} characters")
```

**How the code works:**

- `system_prompt` is sent as the `system` message before the student's first turn.
- **Persona**, **scope**, and **tone** map to the three ingredients in the table above.
- `len(system_prompt)` checks size — long system prompts eat **context window** space.

### System + User in One Conversation

```text
SYSTEM (set once):
"You are a recipe assistant. Only suggest vegetarian Indian breakfast dishes.
List ingredients first, then numbered steps. Keep total cook time under 20 minutes."

USER (this turn):
"I have leftover poha and one onion. What can I make quickly?"

ASSISTANT (shaped by both):
Lists ingredients, numbered steps, 12-minute poha — without the user repeating
vegetarian, ingredients-first, or under-20-minutes rules.
```

### Practice — Draft Your Bounded System Prompt

Pick one narrow role: **fee-payment FAQ bot**, **metro route helper**, or **internship email polisher**.

Write 6–8 lines covering **Persona**, **Scope**, and **Tone & Rules**.

Include one **refusal rule** for off-topic requests and specify **response length** or **format**. Read your draft aloud — if you can predict the agent's behaviour from your text alone, it is clear enough.

---

## Zero-Shot vs Few-Shot Prompting

System and user roles tell the model *who it is*. **Zero-shot** and **few-shot** tell the model *what pattern to copy* inside a user message.

- **Official Definition:** **Zero-shot prompting** asks the model to perform a task with **no examples** — only the instruction. **Few-shot prompting** includes **one or more worked examples** before the real task so the model mirrors the pattern.
- **In Simple Words:** Zero-shot is *"Do it your way."* Few-shot is *"Do it exactly like these samples."*
- **Real-Life Example:** Zero-shot is a teacher saying *"Write a film review."* Few-shot is showing two sample reviews with a fixed structure, then saying *"Now review this film the same way."*

Zero-shot works for **common tasks** (translation, short Q&A) where format is flexible. It breaks down when you need **fixed JSON keys**, **brand tone**, or **repeatable labels** across many inputs — add **two** few-shot examples instead of blaming the model.

```text
ZERO-SHOT:
"Translate to Hindi: The library opens at 9 AM on weekdays."
→ "पुस्तकालय सप्ताह के दिनों में सुबह 9 बजे खुलता है।"
```

### Few-Shot — Teaching by Example

Few-shot puts **demonstrations inside the prompt**. The model infers the mapping from input to output.

```text
FEW-SHOT — product taglines:

Product: Reusable water bottle
Tagline: "Stay hydrated, stay kind — to yourself and the planet."

Product: Desk lamp with USB port
Tagline: "Light your late-night study sessions — and charge your phone too."

Product: Noise-cancelling headphones
Tagline:
```

The model is likely to return a short, two-part, brand-style line — because the examples set the pattern.

![Zero-shot vs few-shot — instruction only versus showing worked examples first so the model copies your format](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session24/session24-02-zero-shot-vs-few-shot.png)

### Zero-Shot vs Few-Shot — Quick Comparison

| Aspect | Zero-shot | Few-shot |
|---|---|---|
| **Examples in prompt** | None | Usually 1–5 |
| **Best for** | Standard language tasks | Custom format, tone, classification |
| **Consistency** | May vary run to run | Usually more stable |
| **Context cost** | Lower token use | Higher — examples consume window space |
| **Agent use case** | Simple lookups | Structured replies, routing labels |

- **Practical tip:** Start zero-shot. If format drifts, add **two** strong examples — not ten. Long few-shot blocks steal room from the user's actual document.

### Practice — Same Task, Two Styles

**Task:** Write a one-line **customer testimonial** for a fictional app called **StudyPath**.

Try zero-shot first, then few-shot with two sample testimonials. Note which output is easier to reuse in an automated workflow.

---

## Chain-of-Thought Prompting

Formatting examples help consistency. **Chain-of-thought (CoT)** helps **reasoning** — logic, maths, and multi-step decisions.

- **Official Definition:** **Chain-of-Thought (CoT) prompting** instructs the model to show **intermediate reasoning steps** before giving a final answer, instead of jumping straight to a conclusion.
- **In Simple Words:** Asking the student to **show working** in the exam — not only write the final number.
- **Real-Life Example:** A **doctor** who lists symptoms, rules out causes, then recommends treatment is using chain-of-thought. A doctor who blurts one medicine name with no reasoning is risky.

![Chain-of-Thought prompting — step-by-step reasoning keeps the model on track instead of jumping to a shallow answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-chain-of-thought-flow.png)

LLMs predict **one token at a time** — direct *"Answer: ___"* often picks a shallow completion. **Step-by-step text** creates checkpoints on budgets, scheduling, and eligibility checks. In production, the model can reason internally and only print the final formatted answer.

### Zero-Shot CoT vs Few-Shot CoT

| Style | How you trigger reasoning |
|---|---|
| **Zero-shot CoT** | Add a phrase like *"Let's think step by step."* — no solved examples |
| **Few-shot CoT** | Show 1–2 solved problems with visible Reasoning + Answer, then your question |

```text
ZERO-SHOT CoT:
A train leaves Delhi at 7 AM at 60 km/h. Another leaves Agra (200 km away)
at 9 AM at 80 km/h toward Delhi. When do they meet? Let's think step by step.

FEW-SHOT CoT:
Q: A shopkeeper buys 20 pens at ₹5 each and sells at ₹8 each. Profit?
Reasoning: Cost = 20 × 5 = ₹100. Revenue = 20 × 8 = ₹160. Profit = ₹60.
A: ₹60

Now solve:
Q: A vendor buys 30 notebooks at ₹12 each, sells at ₹18 each. Profit?
Reasoning: [work step by step]
A:
```

Embed numbered CoT steps in the **system prompt** so every user turn follows the same process.

```python
# cot_in_system.py — bookstore support agent with embedded reasoning workflow

support_system = """
You are a support triage assistant for an online bookstore.

Before every reply:
Step 1: Quote the customer's problem in one sentence.
Step 2: Classify as DELIVERY, PRODUCT_QUALITY, PAYMENT, or OTHER.
Step 3: Branch — tracking steps for DELIVERY; photo request for PRODUCT_QUALITY.
Step 4: Draft a polite reply under 120 words with one next action.

Do not invent refund amounts or delivery dates the customer did not mention.
"""
```

**How the code works:**

- Steps 1–2 force **understanding before action** — fewer generic apologies.
- Step 2 produces a **label** you can log or route to tools later.
- Steps 3–4 are **conditional CoT** — different paths for different problem types.
- The last line is a **hallucination guardrail** tied to facts the user actually provided.

The full FAQ agent demo later combines this CoT pattern with a user template.

### Practice — Upgrade a Weak Prompt with CoT

Take *"Should I learn Python or SQL first for a data career?"* — rewrite once with a **zero-shot CoT** trigger, once with one **few-shot CoT** solved example. Compare which advice feels more transparent.

---

## Reusable Prompt Templates

CoT improves thinking. **Prompt templates** improve **repeatability** — the same slots filled with different data each run.

- **Official Definition:** A **prompt template** is a reusable text pattern with **placeholders** for variable inputs, so you can generate consistent prompts without rewriting from scratch.
- **In Simple Words:** A **mad libs** form for AI — fixed instructions, blank spaces for the changing details.
- **Real-Life Example:** A **railway reservation form** always asks name, age, train number, and class — only the values change. A template does that for prompts.

### The Five Building Blocks

| Block | What it does | Example |
|---|---|---|
| **Role** | Persona and expertise | *"You are a senior career counsellor."* |
| **Task** | The job for this run | *"Recommend three career paths for this student."* |
| **Instructions** | Ordered steps to follow | *"Read background → match interests → explain in plain language."* |
| **Constraints** | Guardrails and limits | *"No jargon without explanation. Max 100 words per path."* |
| **Output format** | Exact structure of the answer | *"Career 1: name / Why it fits: … / First step: …"* |

![The five building blocks of a structured prompt — Role, Task, Instructions, Constraints, and Output Format](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-structured-prompt-five-components.png)

### A Complete Structured Template (Plain Text)

```text
[ROLE]
You are a campus placement coach helping non-engineering graduates explore tech roles.

[TASK]
Suggest three realistic entry-level tech career paths for the student below.

[INSTRUCTIONS]
1. Read the student's degree and interests.
2. Pick paths that do not require heavy coding on day one.
3. For each path, name one skill to build in the next 30 days.

[CONSTRAINTS]
- Do not promise specific salaries as guarantees.
- Keep language simple enough for a first-year student.

[OUTPUT FORMAT]
Path 1: <name> / daily work / why it fits / 30-day skill step
Path 2: ...
Path 3: ...

[STUDENT INPUT]
Degree: BCom, 2 years sales experience. Interests: talking to people, spreadsheets.
```

Only `[STUDENT INPUT]` changes each time. The agent behaviour stays stable.

### Prompt Template in Python

```python
# template_demo.py — system rules fixed; user message built from a template

from string import Template

system_prompt = "You are a note-summariser. Max 5 bullets. No facts outside the notes."

user_template = Template("""
[TASK] Summarise these lecture notes.
[OUTPUT FORMAT] Bullet 1 … Bullet 2 … Exam tip: …
[LECTURE NOTES]
$notes_text
""")

notes = "Tokens are text chunks. Context window caps tokens per call."
user_prompt = user_template.substitute(notes_text=notes)
print(user_prompt)  # Same structure every run — only $notes_text changes
```

**How the code works:**

- `system_prompt` stays fixed; `user_template` injects new content via `$notes_text`.
- `substitute()` returns the filled user message ready for an API call.

### Practice — Build Your Own Five-Block Template

Choose a real task: **summarise a news article**, **draft a polite email to a professor**, or **turn meeting bullets into action items**.

Write all five blocks: **Role**, **Task**, **Instructions**, **Constraints**, **Output format**. Leave one placeholder — e.g. `[PASTE ARTICLE HERE]`.

Re-read your template. Could you fill the blank and know exactly what shape the answer must take?

---

## Designing a Beginner Single-Agent Prompt

You now have the core tools: **system vs user**, **zero-shot / few-shot**, **CoT**, and **templates**. A **beginner agent** wires these into one dependable **system prompt** plus a **user template** for incoming tasks.

- **Official Definition:** An **agent prompt** is the combined instruction design — system rules, reasoning workflow, output format, and guardrails — that steers one AI worker through a repeated task without constant human editing.
- **In Simple Words:** A **job description + checklist + answer format** posted on the agent's desk before customers arrive.
- **Real-Life Example:** A **DMV counter clerk** follows the same script: verify ID, check form section, stamp approval, hand receipt. Your agent script is that process in text form.

### Four Pieces of a Reliable Beginner Agent Prompt

| Piece | Source technique | What it prevents |
|---|---|---|
| **Role & scope** | System prompt | Off-topic answers, wrong persona |
| **Reasoning steps** | Chain-of-thought | Shallow guesses on multi-step tasks |
| **Format & constraints** | Structured template | Messy or unsafe outputs |
| **Optional few-shot** | Examples in system or first turn | Inconsistent labels or tone |

![The four parts of a beginner agent prompt — role and scope, reasoning steps, format constraints, and optional few-shot examples](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-agent-prompt-flow-four-components.png)

One well-written **system prompt** and one **user template** are enough for a single-agent workflow — no complex framework required to practise.

### Complete Demo — Campus Tech Fest FAQ Agent

One script combines **system prompt**, **user template**, and **CoT workflow**. No paid API — it prints prompts you can paste into any chat tool.

```python
# prompt_agent_demo.py — single-agent prompt design

from string import Template

system_prompt = """
You are Kiran, FAQ assistant for college Tech Fest 2026.
Scope: dates, venue, registration, schedule only.
Off-topic: "I can help with Tech Fest 2026 details only."

Workflow: (1) Restate question (2) Check FAQ context (3) Answer from context
or say what is missing (4) Reply under 100 words with one next step.

Constraints: Never invent guests, prizes, or dates. No passwords or Aadhaar.
Output: Question understood / Answer / Next step
"""

user_template = Template("[FAQ CONTEXT]\n$faq_context\n\n[QUESTION]\n$student_question")

faq_context = "Tech Fest 2026: 12–14 March, Main Auditorium. Registration closes 1 March. Day 1 keynote: 10:00 AM."

for q in ["What time is the keynote on day 1?", "Who is performing at the IPL final?"]:
    print("Q:", q)
    print(user_template.substitute(faq_context=faq_context, student_question=q))
    print("---")
```

- `system_prompt` holds persona, scope, CoT workflow, constraints, and output format.
- `user_template` injects new FAQ text and questions each turn.
- The IPL question tests **scope refusal** without inventing performers.
- In a real app, send `system_prompt` once and the filled `user_template` on each turn.

### Common Prompt Mistakes to Avoid

- **Empty system prompt** — all rules crammed into the first user message get lost in long chats.
- **No output format** — the model improvises structure every time; agents need predictable shape.
- **Too many few-shot examples** — ten examples eat the context window; two strong ones usually suffice.
- **No grounding rule** — without *"answer only from provided context"*, hallucinations return on factual tasks.

**Layering tip:** Start with zero-shot + strong system prompt → add few-shot when format drifts → add CoT when logic fails → wrap in a template for many similar inputs.

| Layer | Technique | Agent job |
|---|---|---|
| 1 | **System prompt** | Permanent persona and boundaries |
| 2 | **Few-shot** (if needed) | Locks output style or labels |
| 3 | **CoT steps** | Better multi-step reasoning |
| 4 | **Template placeholders** | New user data without rewriting rules |

Move stable rules into the **system** layer — not the user message. Keep the system prompt short enough to leave room for user documents in the **context window**.

### Ship Checklist

- **Bounded scope** — can you state what the agent does *not* do in one sentence?
- **Numbered workflow** — are CoT steps visible in the system prompt?
- **Output format** — will every reply look similar enough to display or parse?
- **Grounding rule** — does the prompt forbid facts outside provided context?
- **Token budget** — is the system prompt short enough to leave room for user documents?

### Capstone Practice

Design one **complete system prompt** for a daily-life helper — study planner, mock interviewer, caption writer, or fitness habit coach.

Include **named persona**, **scope with refusal line**, **3+ CoT steps**, **2 constraints**, and **labelled output format**. Test with one on-topic and one off-topic user message.

---

## Key Takeaways

- **Prompt engineering** turns a fluent LLM into a dependable tool — clear instructions beat clever one-liners.
- **System prompts** carry persona, scope, and workflow; **user prompts** carry the live task. Split them correctly for stable agent behaviour.
- **Zero-shot** suits standard tasks; **few-shot** locks custom format and tone when the model cannot infer your pattern alone.
- **Chain-of-thought** step lists reduce reasoning errors on multi-step problems — especially when embedded in the system prompt.
- **Reusable templates** with Role, Task, Instructions, Constraints, and Output format let one beginner agent handle many inputs without prompt drift.

In upcoming work you will connect these prompt designs to **agent frameworks and tool-using workflows**, where the system prompt remains the main lever for how your agent thinks and responds.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / Tool | What It Means |
|---|---|
| **Prompt Engineering** | Designing and refining LLM inputs for reliable, useful outputs |
| **System Prompt** | Persistent background instruction — persona, scope, rules for the whole chat |
| **User Prompt** | Each live message or task input from the human or application |
| **Zero-Shot Prompting** | Task instruction with no examples — model relies on training patterns |
| **Few-Shot Prompting** | Task instruction with 1–5 worked examples before the real input |
| **Chain-of-Thought (CoT)** | Intermediate reasoning steps before the final answer |
| **Zero-Shot CoT** | CoT triggered by a phrase like *"Let's think step by step"* — no examples |
| **Few-Shot CoT** | Solved examples include visible reasoning; model copies that pattern |
| **Prompt Template** | Reusable prompt pattern with placeholders for variable content |
| **Role** | Template block defining persona and expertise |
| **Task** | Template block stating what must be delivered |
| **Instructions** | Template block listing ordered steps to complete the task |
| **Constraints** | Template block listing limits and forbidden behaviours |
| **Output Format** | Template block defining structure, length, and sections of the reply |
| **Agent Prompt** | Combined system design — role, workflow, format, and guardrails for one agent |
| **`string.Template`** | Python helper for `$placeholder` substitution in prompt strings |
| **`Template.substitute(...)`** | Fills placeholders and returns the final prompt text |
| **Context window** | Token limit for system + user + model reply in one API call |
| **Hallucination guardrail** | Prompt rule forbidding invented facts outside provided context |
