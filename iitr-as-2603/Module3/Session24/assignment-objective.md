# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A **college admission helpdesk** bot is configured once with the rule: *"Answer only admission, fee, and scholarship questions."* Every afternoon, students type new questions like *"What is the hostel fee deadline?"*

Which statement correctly maps **system prompt** vs **user prompt** in this setup?

A. The daily student question is the **system prompt**; the admission rule is the **user prompt**  
B. The admission rule is the **system prompt**; each student question is the **user prompt**  
C. Both are user prompts because students type the messages  
D. The model generates the system prompt automatically on each turn

**Correct Answer:** B

**Answer Explanation:**  
The **system prompt** sets persistent background rules (scope, persona, tone) **once**. The **user prompt** is the live input that changes every turn.

**Why other options are wrong:**  
- A: Reverses the roles — stable rules belong in system, not user.  
- C: Students type user messages; developers set system rules.  
- D: System prompts are written by the builder, not auto-generated each turn.

---

## Q2 (MCQ, Easy)

Ravi is building a **medical-notes JSON extractor** in Groq Playground. He wants the model to always output the same five fields (`age`, `gender`, `diagnosis`, `weight`, `smoking`) and never invent missing values.

Where should he place the JSON schema and *"use null if missing — do not guess"* rule?

A. Only in the first user message, then hope the model remembers  
B. In the **system prompt**, so rules persist for every pasted note  
C. In the assistant response panel before submitting  
D. In a separate PDF the model cannot read

**Correct Answer:** B

**Answer Explanation:**  
Stable **output format** and **guardrails** belong in the **system prompt** so they are not buried in chat history and apply to every user turn.

**Why other options are wrong:**  
- A: Rules in the first user message get lost in long chats — a common mistake.  
- C: You cannot pre-fill the assistant slot as instructions.  
- D: The model only reads what you put in system/user slots.

---

## Q3 (MCQ, Easy)

Meera runs a travel blog and asks an LLM: *"Translate to Hindi: The library opens at 9 AM on weekdays."* She gives **no examples** — only the instruction and the English sentence.

Which prompting style is she using?

A. Few-shot prompting  
B. Chain-of-thought prompting  
C. Zero-shot prompting  
D. Prompt template with five building blocks only

**Correct Answer:** C

**Answer Explanation:**  
**Zero-shot** means the task instruction has **no worked examples** — the model relies on patterns learned during training (translation is a common zero-shot task).

**Why other options are wrong:**  
- A: Few-shot requires demonstration examples before the real task.  
- B: CoT requires step-by-step reasoning instructions, not just translation.  
- D: Templates are reusable patterns; this is a single direct instruction.

---

## Q4 (MCQ, Easy)

A network team at a company needs an assistant to map **internal router error descriptions** to **company-specific error codes** that never appeared in public training data. Zero-shot guesses are wrong or empty.

What is the **best first upgrade**?

A. Add **few-shot examples** in the prompt showing issue → error code pairs  
B. Remove the system prompt entirely  
C. Switch to chain-of-thought only, with no examples  
D. Ask the model to guess faster by shortening the prompt to one word

**Correct Answer:** A

**Answer Explanation:**  
**Few-shot prompting** teaches **custom labels** the model never saw publicly — by showing issue → code demonstrations inside the prompt.

**Why other options are wrong:**  
- B: Removing system rules makes format and scope worse.  
- C: CoT helps reasoning steps, not proprietary label mapping without examples.  
- D: Shorter prompts do not teach unknown code mappings.

---

## Q5 (MCQ, Moderate)

A health-tech startup tries **few-shot prompting** for a diagnosis assistant: *fever + cough → influenza*, *chest pain → heart issue*, then asks about a new patient with fever and fatigue.

Why does this approach **fail** for diagnosis?

A. Few-shot always uses too many tokens for any task  
B. One symptom can map to **many diseases** — examples cannot teach the full **reasoning process**  
C. LLMs cannot read the word "fever"  
D. System prompts are illegal for medical apps

**Correct Answer:** B

**Answer Explanation:**  
Medical diagnosis needs **multi-step reasoning** (list symptoms → rule out → follow-up). Few-shot input→output pairs skip that process — **chain-of-thought** is the better fit.

**Why other options are wrong:**  
- A: Token cost is a trade-off, not why few-shot fails logically here.  
- C: Models understand common symptom words.  
- D: System prompts are standard; the issue is technique choice, not legality.

---

## Q6 (MCQ, Moderate)

An engineering lead compares three prompt styles for the **same task volume** on a paid API billed per **million tokens**:

- Style A: zero-shot instruction only  
- Style B: zero-shot + two few-shot examples  
- Style C: chain-of-thought with five numbered steps in the system prompt  

Which ordering correctly ranks **typical token usage** from **lowest to highest**?

A. A → B → C  
B. C → B → A  
C. B → A → C  
D. A → C → B

**Correct Answer:** A

**Answer Explanation:**  
**Zero-shot** uses the fewest tokens; **few-shot** adds example cost; **chain-of-thought** with long step lists uses the **most**. Pick the lightest technique that still works.

**Why other options are wrong:**  
- B, C, D: Reverse or scramble the ordering — CoT is not cheaper than zero-shot.

---

## Q7 (MSQ, Moderate)

Divya is assembling a **reusable prompt template** for a campus career counsellor agent. Which items are among the **five standard building blocks**?

A. **Role** — persona and expertise  
B. **Task** — what must be delivered this run  
C. **Instructions** — ordered steps to follow  
D. **API key** — provider authentication string  
E. **Constraints** — guardrails and limits  
F. **Output format** — exact structure of the answer

**Correct Answers:** A, B, C, E, F

**Answer Explanation:**  
The five blocks are **Role**, **Task**, **Instructions**, **Constraints**, and **Output format**. Only the variable input (e.g. student background) changes each run.

**Why other options are wrong:**  
- D: API keys are deployment config, not a prompt template block.

---

## Q8 (MSQ, Moderate)

A **meeting summarizer agent** must not invent attendees or decisions. Which prompt constraints are **effective hallucination guardrails** for this agent?

A. *"Answer only from the provided transcript. Do not invent facts."*  
B. *"Do not add attendees or decisions not present in the transcript."*  
C. *"Always guess missing names so the summary looks complete."*  
D. *"If a field is unknown, write 'not stated' instead of fabricating."*  
E. *"Use longer chain-of-thought steps on every task, including simple word counts."*

**Correct Answers:** A, B, D

**Answer Explanation:**  
**Hallucination guardrails** ground the model in **provided context** and forbid fabrication — steering toward *"not stated"* or null when data is missing.

**Why other options are wrong:**  
- C: Explicitly encourages fabrication.  
- E: CoT on trivial tasks wastes tokens without reducing hallucination risk.

---

## Q9 (MSQ, Hard)

Match each **real task** to the **best first prompting technique** (before escalating to heavier methods):

| Task | Best first technique |
|---|---|
| 1. Translate a product manual paragraph to Tamil | ? |
| 2. Route support tickets into five **company-internal** category codes | ? |
| 3. Help a student compare two career paths with pros, cons, and a recommendation | ? |
| 4. Extract `age` and `gender` from a short medical note into JSON | ? |

Which **task → technique** pairings are **correct**?

A. Task 1 → **Zero-shot**  
B. Task 2 → **Few-shot** with labelled examples  
C. Task 3 → **Chain-of-thought** with numbered comparison steps  
D. Task 4 → **Few-shot with twenty tagline examples** before extraction  
E. Task 4 → **Strong system prompt** with JSON output format (zero-shot extraction)

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
Translation is a standard **zero-shot** task. Internal labels need **few-shot**. Career comparison needs **reasoning steps** (**CoT**). Simple field **extraction** needs a clear **system prompt** and schema — not unrelated few-shot demos.

**Why other options are wrong:**  
- D: Twenty tagline examples do not help structured medical field extraction and waste context.

---

## Q10 (MSQ, Hard)

Ankit is shipping a **beginner single-agent workflow** in Groq Playground for a bounded **fee-payment FAQ bot**. Which design choices follow **sound prompt engineering**?

A. Put **persona, scope, and refusal rules** in the **system prompt**  
B. Define a predictable **output format** (e.g. labelled sections) for every reply  
C. Add **fifteen few-shot examples** to every prompt to be safe  
D. Include a **grounding rule**: answer only from the FAQ text provided in the user message  
E. Use a **long chain-of-thought workflow** to extract a single fee amount from one sentence  
F. Keep the system prompt short enough to leave room for FAQ text in the **context window**

**Correct Answers:** A, B, D, F

**Answer Explanation:**  
Reliable beginner agents use **system-layer** rules, **bounded scope**, **parseable output**, **grounding**, and **token-aware** prompt length. Escalate technique only when needed.

**Why other options are wrong:**  
- C: Too many examples steal context window space — two strong ones usually suffice.  
- E: CoT is unnecessary for simple single-field extraction.
