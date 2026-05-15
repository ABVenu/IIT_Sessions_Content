# Assignment — Objective (Session: Prompt Engineering)

**Instructions:** Answer all questions. **MCQ** = exactly one correct option. **MSQ** = select *all* options that apply; partial marking may apply per platform rules.

---

## Section A — Easy (MCQ)

### Q1 (MCQ — Easy)

A banking chatbot always refuses non-banking questions and keeps a formal tone across every chat. According to how LLM-based apps are built, where are the long-lived rules that define that persona and boundary most likely defined?

- A) Inside each individual user message the customer types  
- B) In the system prompt (or equivalent persistent instruction sent before or with the conversation)  
- C) Only in the model’s random seed  
- D) In the customer’s browser cache  

---

### Q2 (MCQ — Easy)

You ask a model: *“Translate this sentence to French: The train leaves at 6 PM.”* You give no examples and no special format. This is best described as:

- A) Few-shot prompting  
- B) Zero-shot prompting  
- C) Few-shot chain-of-thought prompting  
- D) Iterative prompting  

---

### Q3 (MCQ — Easy)

You are briefing an AI assistant before it talks to any user. You write: *“You are Nisha, a calm career coach. Only discuss résumés and interviews. Never promise a job offer.”* Which three ingredients of a strong system prompt are you mainly covering?

- A) API key, temperature, and top-p  
- B) Persona, scope, and tone/rules  
- C) Dataset split, batch size, and learning rate  
- D) Retrieval index, embedding dimension, and chunk overlap  

---

### Q4 (MCQ — Easy)

**Few-shot prompting** is most useful when you need the model to:

- A) Always run faster with fewer input tokens  
- B) Match a non-standard format, tone, or pattern you demonstrate with examples in the prompt  
- C) Replace the need for any system prompt  
- D) Guarantee factually correct answers without checking  

---

## Section B — Moderate (MCQ)

### Q5 (MCQ — Moderate)

You want the model to solve a multi-step word problem and reduce “jumping to a guess.” You add: *“Let’s think step by step.”* You provide no worked examples. This is best described as:

- A) Few-shot prompting  
- B) Zero-shot chain-of-thought prompting  
- C) Self-correction prompting  
- D) Retrieval-augmented generation  

---

### Q6 (MCQ — Moderate)

A **structured prompt template** in the style taught in this module typically includes which five labeled components?

- A) Role, Task, Instructions, Constraints, Output Format  
- B) System, User, Assistant, Tool, Memory  
- C) Train, Validation, Test, Loss, Optimizer  
- D) Encoder, Decoder, Attention, LayerNorm, Dropout  

---

## Section C — Moderate (MSQ)

### Q7 (MSQ — Moderate)

Which statements about **self-correction prompts** are correct?

- A) They ask the model to critique and improve its own draft using explicit criteria  
- B) They always require three separate human reviewers before the model answers  
- C) A strong design often separates **Generate**, **Critique**, and **Rewrite** stages clearly  
- D) A vague line like “write a perfect answer” is equivalent to a reliable self-correction structure  

---

### Q8 (MSQ — Moderate)

Which practices match **iterative prompting** as described for refining model outputs?

- A) Sending one follow-up that targets the single most important gap you noticed  
- B) Sending “try again” with no specifics, repeatedly, hoping quality improves  
- C) Doing multiple rounds where each new prompt builds on the previous response  
- D) Expecting the first draft to be final without any review  

---

## Section D — Hard (MSQ)

### Q9 (MSQ — Hard)

An **agent prompt flow** meant to behave reliably “without you in the loop” should align with which ideas from this module?

- A) Combine role definition, the concrete task, measurable self-check criteria, and a defined output format  
- B) Rely only on the user’s latest message and ignore persistent instructions  
- C) Use reflection/feedback criteria so the agent can evaluate its output against a checklist and revise  
- D) Avoid constraints because they reduce creativity  

---

### Q10 (MSQ — Hard)

Pick **all** correct distinctions about LLM prompting and how real chat apps use instructions:

- A) **System prompt** sets persistent background behaviour; **user prompt** is the live message for each turn  
- B) **Self-correction** improves output within one structured prompt; **iterative prompting** improves output across multiple follow-up turns  
- C) **Zero-shot** always requires 3–5 examples inside the prompt  
- D) In production apps, the user-visible text box is often only part of what the application sends to the model  

---

## Answer Explanations (for Assess platform — paste per item)

### Q1 — Correct: **B**

**Reasoning:** Persistent persona, scope, and rules are associated with the system layer (or equivalent app-controlled system instructions), not each user utterance.

**Why others are wrong:** A) User messages are per-turn requests, not the persistent policy layer. C) Seed affects randomness, not business rules. D) Browser cache does not define model instructions.

---

### Q2 — Correct: **B**

**Reasoning:** No examples were provided—only an instruction—so this is zero-shot.

**Why others are wrong:** A) Few-shot requires examples in the prompt. C) No CoT trigger or exemplified reasoning shown. D) Iterative implies multiple rounds of prompts, not a single request.

---

### Q3 — Correct: **B**

**Reasoning:** Name/personality maps to persona; “only discuss…” maps to scope; “never promise…” maps to tone/rules guardrails.

**Why others are wrong:** A/C/D) These are unrelated ML/API mechanics not described as the three system-prompt ingredients in the notes.

---

### Q4 — Correct: **B**

**Reasoning:** Few-shot is used to teach a pattern/format/style via in-prompt examples.

**Why others are wrong:** A) Few-shot usually adds tokens/latency, not guaranteed speed. C) System prompts still matter. D) No prompting style guarantees factual correctness without verification.

---

### Q5 — Correct: **B**

**Reasoning:** A trigger phrase without exemplified reasoning is zero-shot CoT.

**Why others are wrong:** A) No examples → not few-shot. C) Self-correction needs critique/rewrite stages, not only a step-by-step trigger. D) RAG is document-grounding, not described here as the same thing.

---

### Q6 — Correct: **A**

**Reasoning:** The five-component structured template in the notes is Role, Task, Instructions, Constraints, Output Format.

**Why others are wrong:** B/C/D) These are chat roles, ML training, or model architecture terms—not the five prompt-template blocks taught.

---

### Q7 — Correct: **A, C**

**Reasoning:** Self-correction embeds evaluation/fixing in the prompt; explicit staged generate/critique/rewrite is the recommended structure.

**Why others are wrong:** B) Human reviewers are not required by definition. D) “Perfect answer” wording does not reliably enforce staged self-correction.

---

### Q8 — Correct: **A, C**

**Reasoning:** Iterative prompting is multi-round refinement; best practice is targeted fixes, often one key issue at a time.

**Why others are wrong:** B) Nonspecific retries are called out as a common mistake. D) That contradicts the draft/review/refine cycle.

---

### Q9 — Correct: **A, C**

**Reasoning:** Agent prompt flow combines role, task, reflection/feedback criteria, and output format; checklist-driven revision supports autonomy.

**Why others are wrong:** B) Ignoring persistent instructions contradicts system prompt design. D) Constraints are central guardrails, not something to avoid.

---

### Q10 — Correct: **A, B, D**

**Reasoning:** A/B are definitional in the notes; D matches “hidden system messages / institute context” behaviour of real apps.

**Why others are wrong:** C) Zero-shot means *no* examples; few-shot uses examples.

---

**End of objective assignment**
