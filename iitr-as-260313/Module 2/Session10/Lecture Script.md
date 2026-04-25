# Lecture Script: Advanced Prompt Engineering for Agents

**Session duration:** 2 hours 15 minutes (instructor-led blocks: **127 minutes** of teaching, plus one **5–8 minute** break; blocks are designed to land on time)  
**Audience:** Indian learners; mixed backgrounds, including students with no prior tech experience.

**How to use this file:** This document is for *timing and facilitation only*. It is not a substitute for the Lecture Notes. Use it to pace the room, manage devices and screen share, and trigger engagement — read the full lecture notes in advance for definitions and examples.

**Break rule:** After roughly 60–75 minutes of instruction (after Block 6), take *one* break of 5–8 minutes. Do not list the break as a numbered teaching block; resume with Block 7 when the class is back.

---

## 1. Opening, recap, and learning outcomes (7 minutes)

- Welcome the batch; set a calm, practical tone: today is *hands-on* and about making AI outputs *reliable*, not more jargon.
- **Screen-share** the session title slide or first section of the notes: *Advanced Prompt Engineering for Agents*.
- In 1–2 minutes, **bridge from Session 9**: system prompts, role prompting, a glimpse of agent frameworks (LangChain, CrewAI, AutoGen) — today goes *deeper* on *how* to write prompts that make agents *think*.
- **Cold-call** one student: “In one line, what is one thing you still remember from last time about *system prompts* or *roles*?”
- **Read aloud** the “In this session, you will learn” bullets from the notes (or show them); ask for a **thumbs up** if the list matches what they hoped to get from the day.

**Bridge sentence:** “If that agenda works for you, we’ll start with what ‘advanced’ prompt engineering actually means — and a quick activity to wake up the room.”

---

## 2. Advanced prompt engineering + The Genie Test (10 minutes)

- **Screen-share** the “genie” analogy and the official vs simple definition; speak slowly; avoid assuming everyone codes.
- **Pair-share:** *The Genie Test* — each pair writes (1) a vague one-line ask and (2) a specific, detailed version for something they actually need; 3–4 minutes. **Circulate** and glance at 4–5 screens; pick **2–3 pairs** to share *before/after* (as in the instructor note).
- Debrief: point out *which* details changed the ask (context, goal, format).

**Bridge sentence:** “We’ve seen that vague asks get vague answers; next, we’ll look at a deliberately bad prompt and name exactly what’s missing so we can fix it with techniques you’ll use all day.”

---

## 3. Why basic prompts fail + Spot the Problem (8 minutes)

- **Screen-share** the example *“What should I do to grow my small business?”* and the generic list outcome; ask “Is this *wrong* or just *useless*?” — take 2 short answers.
- Run **Spot the Problem** on *“Tell me about AI.”* — give 90 seconds **solo**, then **cold-call 3–4 students** for what’s wrong or missing *before* you unpack the list.
- Connect to the line in the notes: **CoT, Structured, and Reasoning** each address part of the failure (no context, no thinking instruction, no format).

**Bridge sentence:** “The first big technique we add is: make the model *show its work* — that’s Chain-of-Thought, and it’s the backbone of better answers.”

---

## 4. Chain-of-Thought: concepts, research, and types (12 minutes)

- **Screen-share** the CoT definition, the math “show your working” analogy, and the doctor example — no rush.
- **Zero-shot CoT:** show the train problem with *“Let’s think step by step”*; explain *zero-shot* in plain language.
- **Few-shot CoT:** show the apple **Example 1** and the pen **follow-up**; ask “Why might showing one solved example help?” — **pair-share 60 seconds** then one pair reports.
- Briefly state the research line (40–50% on some tasks) without turning it into a stats lesson.

**Bridge sentence:** “You can put that same *step-by-step* discipline inside an agent’s *system* instructions — let’s look at a real snippet and then you’ll rewrite prompts yourselves.”

---

## 5. CoT in agent prompts + Trigger the Thinking activity (12 minutes)

- **Screen-share** the 4-step customer support `system_prompt` in Python; **read** the `How the code works` bullets — you don’t need to run it unless the room is strong on tools.
- **Check for understanding:** “Thumbs up if the *order* of the steps matters for a support agent; thumbs sideways if unsure.”
- **Activity — Trigger the Thinking:** *“Should I learn Python or SQL first for a data career?”* — **Part A** (zero-shot trigger only) 3 min; **Part B** (few-shot with one full example) 4 min. **Circulate**; **cold-call 2 students** to read *only* their Part A; comment on how different trigger phrases *feel* (as per instructor note).

**Bridge sentence:** “CoT is about *order of thought*; structured prompts are about *order of sections* in the message — like a form or an FIR, nothing leaves gaps.”

---

## 6. Structured prompts: five blocks + career walkthrough (10 minutes)

- **Screen-share** the five-component table (Role, Task, Instructions, Constraints, Output Format) — walk the room through one row at a time.
- **Build together** the career-counsellor example **step 1 through step 5**, then show the *full assembled* block in the notes; map each paragraph to a component.
- **Optional quick check:** “If you could only fix *one* of the five in a bad prompt first, which would you pick today?” — show of hands: Role / Output Format / other.

**Time check:** This block should land you in the **60–75 minute** window from session start. **Take the 5–8 minute break** (see break rule at top), then start Block 7.

**Bridge sentence (after break):** “We’ve defined structure on paper; now we see how teams **assemble** prompts in code so the same pattern works for every new user input.”

---

## 7. Python: `build_career_prompt` + Build your own structured prompt (10 minutes)

- **Screen-share** the `build_career_prompt` function; trace **role, task, instructions, constraints, output_format** variables and the final `f-string`; run `print(prompt)` only if the batch is following.
- **Activity — Build Your Own:** each learner drafts **all five** components for a *real* task (2–4 lines each) — 5 minutes. **Pair swap** and ask: “Can you tell exactly what the AI should *produce*?” **Circulate.**
- **Spotlight:** **2–3 students** read **Role + Output Format** only; praise strong alignment between them.

**Bridge sentence:** “Structure gives you predictable *shape*; reasoning prompts add *comparisons, causes, and decisions* — the same mental moves you use in a job or a debate.”

---

## 8. Reasoning prompts + combined power example (10 minutes)

- **Screen-share** **Comparison** (Python vs JavaScript for agents, criteria + table + recommendation), **Causal** (chatbot + satisfaction), **Decision** (startup budget) — one minute each; don’t read every line.
- **Screen-share** the `advanced_agent_prompt` BI analyst example; point out **where CoT, structure, and reasoning** appear in *one* string.
- **Check:** “Name one *decision* prompt from your own life in one sentence” — 2 **cold-calls**.

**Bridge sentence:** “You’ll now try one reasoning type for yourself, then we’ll play *technique match* so you know when to stop piling on structure.”

---

## 9. Make the AI reason + when to use + Technique Match (9 minutes)

- **Solo 4–5 min:** *Make the AI Reason* — each student writes **one** reasoning prompt (comparison, causal, or decision) for a *real* situation, with scenario + criteria + final recommendation.
- **Technique match:** read the **five scenarios** from the notes **one at a time**; students **write** Basic / CoT / Structured / Reasoning / **Combined** (or call out if your room is small). **Debate briefly** before you confirm answers; emphasise the **golden rule** (minimum structure for reliable output).
- If time is tight, do scenarios **1, 3, 4, 5** only.

**Bridge sentence:** “You can feel when a prompt is *weak*; next we use a small checklist — CICO — to say *why* it’s weak and how to fix it.”

---

## 10. CICO + fix the broken prompt + run the CICO check (7 minutes)

- **Screen-share** the CICO letters (Clarity, Intent, Constraints, Output); relate each to a **fail mode**.
- **Walk through** the *broken* “Tell me about AI agents and their benefits” → **Fixed** structured version in the notes.
- **Run the CICO check** on *“You are a helpful assistant. Help the user plan their week.”* — **2–3 minutes solo**, fill Pass/Fail; one student **reads a rewrite**; **facilitate** the class to score it against CICO **live**.

**Bridge sentence:** “A checklist catches errors once; in real projects you **iterate** — test, break one thing, fix one thing, test again.”

---

## 11. Iterative refinement + One fix at a time (6 minutes)

- **Screen-share** the 4-step loop (Write → Test → Diagnose → Fix) and the rule: **one change** between tests.
- **Activity:** the *“Give me tips to be more productive”* example — **1 minute** discuss with neighbour: *what is the most critical single missing component?* Then **one fix only** in writing.
- **Reinforce** instructor note: “add more detail” is not a diagnosis; name *Role, Constraints*, etc.

**Bridge sentence:** “To close the design loop, here are a few *agent-level* habits pros use every day — and we’ll read one ‘bad’ prompt and fix it together.”

---

## 12. Best practices + Spot the violations (6 minutes)

- **Rapidly list** 1–2 practices from the notes (positive vs negative instructions; anchor persona) with **one** example each.
- **Activity — Spot the violations:** the *“You are an AI. Don’t be rude. Don’t…”* prompt — **1 minute** list **2** violations; **pair** for rewrite **2 min**; **one** student shares; map to best practices #2 and #3.

**Bridge sentence:** “Everything today lands in a single capstone: a *full* system prompt for a study assistant, then *your* mini-agent — the prompt you could actually ship to an API next week.”

---

## 13. Study agent demo + Build your mini agent (16 minutes)

- **Screen-share** the *Study Assistant* `study_agent_system_prompt` (skim: name **Arya**, steps 1–5, constraints, edge case) — `print` and `len()` optional; mention *tokens* only if the room asks.
- **Capstone — Build Your Mini Agent:** must include **Role (with name/traits)**, **≥3 CoT steps**, **≥2 constraints**, **output format** — **10 minutes**; **you circulate**; help people stuck on **role** or **steps** first.
- **Last 4–5 minutes:** **2–3 students** read **Role + Constraints**; **quick class vote** — “Does this agent feel reliable?” (hands or chat).

**Bridge sentence:** “We’ll land the session with a tight recap you can photograph or copy — the techniques you’ll wire into LangChain and CrewAI soon.”

---

## 14. Key takeaways and close (4 minutes)

- **Screen-share** or read the **Key Takeaways** bullets; **one** cold-call: “Which single technique will you use first *this* week?”
- Point forward: next sessions connect these prompts to **frameworks** (LangChain, CrewAI).
- Thank the batch; point to the terminology table for self-study; handle **1–2 questions** or post in forum.

---

## Timing flex (if the session is running long)

- **Shorten first:** Truncate long **pair shares** to “one pair only” in Blocks 2, 4, 5, and 7. Run **Technique Match** (Block 9) with **3 scenarios** instead of 5. In Block 10, do **CICO table orally** for the weak prompt (no full table write-up).
- **Capstone (Block 13):** If behind by more than 10 minutes, set **7 minutes** for mini-agent and **1 minute** share per volunteer (max two); or assign capstone as **take-home** with a clear submission line.
- **Do not cut:** The **break** (unless policy forbids) — if late, cut **Block 6** follow-up by showing the *assembled* career prompt only, without step-by-step build live.
- **If ahead by 5+ minutes:** Add **2 extra cold-calls** in Block 3 or 8; or let pairs **read their** reasoning prompt to each other in Block 9.

---

*End of script.*
