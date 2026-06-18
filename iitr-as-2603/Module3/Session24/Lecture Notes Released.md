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
| **Persona** | Who the AI is | *"You are an assistant to hospital administration."* |
| **Scope** | What it will and will not do | *"Extract age, gender, diagnosis, weight, and smoking status from medical notes only."* |
| **Tone & Rules** | How it should respond | *"Output JSON only. If a field is missing, write null — do not guess."* |

### Writing a System Prompt for a Bounded Task

The live demo used a **hospital medical-notes extractor** — a real-world case where doctors paste unstructured discharge notes and the model returns structured fields.

```text
SYSTEM (set once in Groq Playground):
You are an assistant to hospital administration.
Your job is to extract important information from medical notes.
Input: unstructured doctor's notes (discharge summary, prescriptions, reports).
Output: JSON with these fields — age (number), gender (string), diagnosis (string),
weight (number), smoking (yes/no).
Rules:
- Be specific; do not invent values not present in the notes.
- If a field is missing, use null.
- Output valid JSON only.

USER (this turn — pasted medical notes):
Patient discharged after 3-day stay. 45-year-old male, weight 72 kg.
Diagnosis: mild pneumonia. Current smoker. Prescribed antibiotics for 5 days.

ASSISTANT (shaped by both):
Returns JSON with age 45, gender male, diagnosis pneumonia, weight 72, smoking yes —
without the doctor repeating JSON rules on every paste.
```

**How this prompt works:**

- The **system** slot holds persona, input type, output schema, and guardrails — set once.
- The **user** slot holds only the changing medical notes each time a doctor submits.
- Explicit **output format** (JSON with named fields) lets another system consume the reply — not only a human reader.
- A **vague** alternative — *"Please read these notes"* — would produce inconsistent paragraphs instead of parseable data.

### A Second Bounded Example — Meeting Summarization

The same system/user split applies when summarizing meeting transcripts:

```text
SYSTEM:
You are a meeting summarization assistant.
Given a transcript, produce: meeting title, date, participants, key discussion points,
and action items with owners.
Do not invent attendees or decisions not in the transcript.

USER:
[paste transcript]

ASSISTANT:
Structured summary with labelled sections — because the system prompt defined the shape.
```

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

## Hands-On with Groq Playground

The live session used **Groq Console** — a free browser playground to test prompts before writing any code.

- **Official Definition:** A **playground** is a web UI where you type system and user messages, pick a model, and see the model reply instantly.
- **In Simple Words:** A practice kitchen before you cook the same recipe in your own app.
- **Real-Life Example:** Test-driving a car on the dealer lot before buying — same engine, no paperwork yet.

**Steps used in class:**

1. Open **console.groq.com** and sign in (e.g., with Google).
2. Click **Playground**.
3. Type your **system message** in the system slot.
4. Type your **user message** in the user slot (e.g., pasted medical notes).
5. Choose a model (e.g., **Llama 3.3**).
6. Hit **Submit** — read the assistant response.

- **Why Groq for learning:** Free tier models let you experiment without API billing during practice.
- **What you saw:** Three panels — **system message**, **user message**, and **assistant response** — matching the mental model from the previous section.
- **Next step:** The same prompts you tested here will later be sent programmatically through an API — the text stays the same; only the delivery method changes.

### Activity — Reproduce the Medical Notes Demo

1. Open Groq Playground.
2. Paste the medical-notes **system prompt** from the bounded-task example above.
3. Paste a short fake discharge note as the **user message**.
4. Submit and check whether the reply is valid JSON with the five fields.

Note whether missing fields come back as `null` or invented values — that tells you if your guardrails are strong enough.

---

## Zero-Shot vs Few-Shot Prompting

System and user roles tell the model *who it is*. **Zero-shot** and **few-shot** tell the model *what pattern to copy* inside a user message.

- **Official Definition:** **Zero-shot prompting** asks the model to perform a task with **no examples** — only the instruction. **Few-shot prompting** includes **one or more worked examples** before the real task so the model mirrors the pattern.
- **In Simple Words:** Zero-shot is *"Do it your way."* Few-shot is *"Do it exactly like these samples."*
- **Real-Life Example:** Zero-shot is a teacher saying *"Write a film review."* Few-shot is showing two sample reviews with a fixed structure, then saying *"Now review this film the same way."*

Zero-shot works for **common tasks** (translation, short Q&A, information extraction) where format is flexible. It breaks down when you need **fixed JSON keys**, **brand tone**, or **repeatable labels** across many inputs — add **two** few-shot examples instead of blaming the model.

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

### When Zero-Shot Fails — Proprietary Domain Example

A **Cisco device error-code** lookup shows where zero-shot breaks:

```text
ZERO-SHOT (fails):
User: "Red light on my Cisco router — what is error code XYZ-442?"
→ Model may guess or say it does not know — ChatGPT was never trained on Cisco's internal codes.

FEW-SHOT (works):
If issue: "Link down on port 3" → Error code: ERR-LINK-03
If issue: "Fan failure detected" → Error code: ERR-FAN-09
If issue: "Red light on router, port 5 blinking" → Error code: ???
→ Model maps the new issue to the pattern learned from examples.
```

- **Security note:** Embedding proprietary examples in prompts exposes that data to the model provider — use only with approved data-handling policies.
- **Practical tip:** Few-shot is how you teach **custom labels** the model never saw during public training.

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

LLMs predict **one token at a time** — direct *"Answer: ___"* often picks a shallow completion. **Step-by-step text** creates checkpoints on symptoms, eligibility, and diagnosis. In production, the model can reason internally and only print the final formatted answer.

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

### CoT for Medical Diagnosis — Why Few-Shot Alone Fails

Few-shot *symptom → disease* pairs fail because one symptom maps to many diseases. **Chain-of-thought** fixes this by teaching the **process**:

```text
SYSTEM — Medical diagnosis assistant:

When a patient describes symptoms, follow these steps:
Step 1: List all key symptoms mentioned.
Step 2: Group symptoms that point to related conditions.
Step 3: Rule out conditions that do not fit the full symptom set.
Step 4: Ask yourself what follow-up question a doctor would ask next.
Step 5: State the most likely diagnosis and one reason it fits.

Do not jump from fever → influenza without checking other possibilities.
Output: Symptoms found / Ruled out / Likely diagnosis / Suggested follow-up question

USER:
"I have had fever, cough, and sore throat for 3 days, plus fatigue."

ASSISTANT:
Walks through steps 1–5 before naming a diagnosis — like a real consultation.
```

- **When CoT is unnecessary:** Simple extraction (age, gender from notes) — the model already knows those fields; extra steps waste tokens.
- **When CoT shines:** Multi-step logic, eligibility checks, troubleshooting workflows.

Embed numbered CoT steps in the **system prompt** so every user turn follows the same process.

### Practice — Upgrade a Weak Prompt with CoT

Take *"Should I learn Python or SQL first for a data career?"* — rewrite once with a **zero-shot CoT** trigger, once with one **few-shot CoT** solved example. Compare which advice feels more transparent.

---

## Choosing the Right Prompting Technique

Not every task needs the heaviest prompt. Pick the **smallest technique that works**.

| Task type | Start with | Escalate to |
|---|---|---|
| Translation, summarization, general Q&A | **Zero-shot** | Few-shot if format drifts |
| Custom labels, brand tone, proprietary codes | **Few-shot** | — |
| Multi-step reasoning, diagnosis, troubleshooting | **Chain-of-thought** | Few-shot CoT if still weak |
| Many similar inputs daily | **Template** with five building blocks | — |

- **Gradient-boosting analogy:** Do not use a heavy model when a simple one suffices — if zero-shot works, do not add few-shot or CoT just because it looks impressive.
- **Token awareness:** Zero-shot uses the **fewest** tokens; few-shot adds example cost; chain-of-thought uses the **most**. Longer prompts leave less room in the **context window** for user documents.
- **Cost example (flagship APIs):** Pricing is often per **million tokens** — input and output priced separately. A medical-notes pipeline processing thousands of pages can add up quickly if every prompt is unnecessarily long.

### Activity — Classify Three Tasks

For each task, write which technique you would try first and why:

1. Translate a paragraph to Hindi.
2. Classify internal support tickets into five company-specific categories.
3. Help a student decide between two career paths with pros and cons.

**Suggested answers:** (1) Zero-shot. (2) Few-shot with 2–3 labelled examples. (3) Chain-of-thought with numbered comparison steps.

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

The live **career counsellor** demo used all five blocks:

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
- Do not use jargon without a one-line explanation.

[OUTPUT FORMAT]
Path 1: <name> / daily work / why it fits / 30-day skill step
Path 2: ...
Path 3: ...

[STUDENT INPUT]
Degree: BCom, 2 years sales experience. Interests: talking to people, spreadsheets.
```

Only `[STUDENT INPUT]` changes each time. The agent behaviour stays stable.

- **Output format matters for pipelines:** In many apps, the model's reply feeds **another system** — predictable JSON or labelled sections make that handoff reliable.
- **Constraints in action:** The live demo showed the model refusing to guarantee salaries because the constraint explicitly forbade it.

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

### Agents Built in This Session

The class framed each Groq exercise as a **simple agent** — an automated app that repeats the same prompt pattern:

| Agent | System prompt carries | User message carries |
|---|---|---|
| **Medical notes extractor** | Role, JSON schema, extraction rules | Pasted doctor's notes |
| **Meeting summarizer** | Summary sections, no-hallucination rule | Meeting transcript |
| **Career counsellor** | Five-block template with constraints | Student background |
| **Medical diagnosis assistant** | CoT steps for symptom analysis | Patient symptom description |

- **Customer support angle:** Banks transcribe call audio to text, then run extraction and sentiment agents on the transcript — the same template idea at enterprise scale.
- **Key insight:** You were already building agents in Playground — the system prompt is the agent's permanent job description; the user message is today's input.

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

### Hallucinations and Constraint Guardrails

- **Official Definition:** A **hallucination** is when the model generates confident text that is **not grounded** in facts or provided context.
- **In Simple Words:** The model invents a story that sounds true — like making up events from 1957 when it was never given a source.
- **Real-Life Example:** A student cites a research paper the model invented — the title sounds academic but the paper does not exist.

**How prompts reduce hallucinations:**

- Add an explicit constraint: *"Answer only from the provided context. Do not invent facts."*
- For medical notes: *"If a field is not in the notes, return null — do not guess."*
- For meeting summaries: *"Do not add attendees or decisions not in the transcript."*

- **Why it works:** The model still predicts likely text — but strong guardrails steer it toward *"I don't know"* instead of fabrication.
- **Common mistake:** Assuming a fluent answer is a correct answer — always check against the source document.

### Ship Checklist

- **Bounded scope** — can you state what the agent does *not* do in one sentence?
- **Numbered workflow** — are CoT steps visible in the system prompt?
- **Output format** — will every reply look similar enough to display or parse?
- **Grounding rule** — does the prompt forbid facts outside provided context?
- **Token budget** — is the system prompt short enough to leave room for user documents?

### Capstone Practice

Design one **complete system prompt** for a daily-life helper — study planner, mock interviewer, caption writer, or fitness habit coach.

Include **named persona**, **scope with refusal line**, **3+ CoT steps**, **2 constraints**, and **labelled output format**. Test with one on-topic and one off-topic user message in Groq Playground.

---

## Key Takeaways

- **Prompt engineering** turns a fluent LLM into a dependable tool — clear instructions beat clever one-liners.
- **System prompts** carry persona, scope, and workflow; **user prompts** carry the live task. Split them correctly for stable agent behaviour.
- **Zero-shot** suits standard tasks; **few-shot** locks custom format and tone when the model cannot infer your pattern alone.
- **Chain-of-thought** step lists reduce reasoning errors on multi-step problems — especially when embedded in the system prompt.
- **Reusable templates** with Role, Task, Instructions, Constraints, and Output format let one beginner agent handle many inputs without prompt drift.
- **Token cost** rises from zero-shot → few-shot → chain-of-thought — choose the lightest technique that still works.
- **Hallucination guardrails** in constraints keep agents honest when answers must come only from provided context.

In upcoming work you will connect these prompt designs to **programmatic API calls and agent frameworks**, where the system prompt remains the main lever for how your agent thinks and responds.

---

## Quick Reference — Important Commands, Libraries, and Terminologies

| Term / Tool | What It Means |
|---|---|
| **Prompt Engineering** | Designing and refining LLM inputs for reliable, useful outputs |
| **System Prompt** | Persistent background instruction — persona, scope, rules for the whole chat |
| **User Prompt** | Each live message or task input from the human or application |
| **Groq Playground** | Free browser UI at console.groq.com to test system + user prompts |
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
| **Context window** | Token limit for system + user + model reply in one API call |
| **Hallucination** | Model-generated text not grounded in facts or provided context |
| **Hallucination guardrail** | Prompt rule forbidding invented facts outside provided context |
