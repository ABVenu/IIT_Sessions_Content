# Lecture Script: Mastering Prompt Engineering

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian learners who may have no formal tech background; goal is usable AI prompting, not jargon for its own sake.

---

**How to use this document**  
This file is **for timing and facilitation only**. It does not replace the lecture notes or student handouts; it tells you *what to do in the room*, where to circulate, how to demo, and when to pause for checks. Lean on Lecture Notes.md for definitions, examples, and code.

**Break rule**  
After **approximately 65–72 minutes from session start**, take **one pause of 5–8 minutes**. Do **not** count the break as a numbered block below; resume afterward with Chain-of-Thought.

---

## 1. Opening, Recap Bridge & Today's Map (11 minutes)

- Screen-share agenda slide or first section of Lecture Notes.md; skim "What We Covered So Far & What's Coming Next" — LLMs recap in **one minute max** ("We know tokens, windows, hallucinations — today we steer the model").
- Flash the vague vs specific prompts image briefly; tie it to today's theme: **brief** beats perfect on the thumbnail.
- Read aloud the bullet list of outcomes (system vs user, zero/few-shot, CoT, templates, self-correction, iterative, agent flow); ask for **thumbs up** if terminology from last session is still fuzzy ("We'll replay anything you're unsure about in examples").
- **Cold-call** one learner: "In one sentence, what is prompt engineering?"
- Normalize: messy first prompts are OK; today is about repeatable patterns.

**Bridge sentence:** "Now we'll split the backstage rules from what you actually type each time — system prompt versus user prompt."

---

## 2. System Prompts vs User Prompts — Teach & Live Walkthrough (16 minutes)

- Use the restaurant analogy (owner briefing vs customer order); reinforce with banking chatbot boundary — **pause** ask "Who writes the rule that says banking only?"
- Screen-share the three-ingredient table (Persona | Scope | Tone & Rules); annotate one row live.
- Open the **`system_prompt`** Python block (Arjun / academic mentor): scroll slowly — point to **`"""..."""`** and where this would attach in an API/UI; optionally show `len()` line as "length awareness" teaser for tokens later.
- Recite side-by-side box (recipe assistant + leftover rice user prompt) — **pair-share 30 seconds:** "What's one behaviour that came only from system, not user?"

**Bridge sentence:** "You’ve seen the backstage script; next you’ll draft your own backstage script in your own words."

---

## 3. Student Activity — Write Your First System Prompt (11 minutes)

- Post instructions from Lecture Notes: pick a real-life assistant role; **Persona + Scope + Tone & Rules**; 5–8 lines; swap with neighbour "Can they say what you'll always/never do?"
- **Circulate** — check laptops: common gap is missing **scope**; nudge students to add "If asked outside X, say…"
- **Cold-call** 2–3 students to read aloud; label each aloud: persona / scope / tone.
- If running ahead, ask one learner to paste into a chat tool optionally (offline policy permitting); do not insist.

**Bridge sentence:** "That's who the model is forever; next we tune how much *example data* we paste into a single question — zero-shot versus few-shot."

---

## 4. Zero-Shot vs Few-Shot Prompting (12 minutes)

- Two definitions briefly; exam-essay analogy.
- Screen two zero-shot snippets (translate; list benefits); then few-shot taglines block — underline **pattern imitation** without explicit format rules.
- Show comparison table quickly; emphasize **risk** rows (format drift vs prompt length).

**Bridge sentence:** "Same tool, same model — let's run the same assignment twice so you feel the delta in your own hands."

---

## 5. Student Activity — Same Task, Two Approaches (13 minutes)

- Task clear on screen: fictional **StudyPath** testimonial; Round 1 zero-shot only; Round 2 prepend two stylistic exemplars — compare outputs.
- **Timer visible** (~4–5 min rounds + compare); circulate — point out constrained tone and structure after few-shot.
- **Check for thumbs:** "Who got a visibly different tone between rounds?"
- Quick debrief tying to agents: predictable format is why few-shot survives in production workflows.

> If Block 5 ends **before ~65 minutes elapsed**, stretch lightly—another pair-share, one cold-call, or a preview question—until you cross the **65–72 minute** window, then pause. If you overrun, trim post-break Blocks 11 or 10 per Timing flex instead of cutting the pause.

---

**Break:** 5–8 minutes (**target**: immediately after Block 5, ~63 minutes in). Students refresh, hydrate; defer long questions until closing if tight on time.

---

## 6. Chain-of-Thought (CoT) Prompting — Teach & Connection to Agents (10 minutes)

- Motivate with mental math + doctor analogy; show optional CoT flow image.
- Explain **why** CoT lifts accuracy (surface answer vs committed steps — avoid over-claiming exact percentages unless you cite).
- Contrasts: zero-shot phrase triggers vs few-shot reasoning exemplar; skim train/Pune problem and shopkeeper Few-Shot CoT snippet.
- Show **embedded CoT** in customer complaint `system_prompt` code — numbered steps internalized before reply.

**Bridge sentence:** "Phrases aren't magic — consistency is; now you'll wire your own reasoning trigger."

---

## 7. Student Activity — Trigger the Thinking (6 minutes)

- On screen: base question "Should I learn Python or SQL first for a data career?"
- Part A: add zero-shot CoT triggers only (**pair-share** naming different trigger phrases).
- Part B (**fast track if short on time:** demo one strong few-shot reasoning pair as instructor-led): one solved chain + main question — optional pair build.
- **Cold-call** two Part A readings; narrate stylistic variance.

**Bridge sentence:** "Thinking steps help truth; labelled boxes help hygiene — structured templates are how teams ship reliably."

---

## 8. Prompt Templates — Five Components & Build Activity (11 minutes)

- Form / FIR analogy; show five-component graphic if bandwidth allows.
- Walk the fully assembled **[ROLE]**…**Student Interests:** block — annotate Role + Output Format first (strongest QA signal).

**Integrated activity (~6–8 min)** — shorten lecture if boxed in time:
- Silent draft: learners pick personal task → write **five** headings with 2–4 lines each; swap neighbour — clarity test.
- **Circulate**, flag missing **constraints** or **output format**.
- **Cold-call** Role + Output Format from 2 students.

**Bridge sentence:** "Good structure reduces waste; reflection and rework handle the leftovers — self-correction and iteration."

---

## 9. Self-Correction & Iterative Prompting — Compact Double Feature (10 minutes)

**Self-correction (~5–6 min)**
- Narrate vague morning routine contrast; three stages **Generate → Critique → Rewrite** with labels imperative.
- Optionally flash without-vs-with-reflection graphic; one tip bullet: vague "make it perfect" fails.

**Iterative (~4–5 min)**
- Sculptor analogy; cycle **Draft → Review → Refine one thing → Repeat**.
- Rapid walkthrough ATM three-round story — underline Round 2 as **specific** fix (vocabulary ladder).
- **Check for thumbs:** "Who has reopened a chat to fix only one complaint — that's iteration."

**Bridge sentence:** "Production agents fuse role, steps, and checks into one repeatable flow."

---

## 10. Agent Prompt Flow, Feedback Loops & Capstone Build (17 minutes)

**Lecture (~7–9 min)**  
- Four components slide: Role, Task, Reflection/Feedback Criteria, Output Format.
- Scroll `study_agent_system_prompt`: name + traits, numbered teaching path (**CoT baked in**), constraints, confusion branch; mention tokens/cost casually via `len` line — **pairs discuss 30 seconds** "Which line prevents sloppy replies?"

**Feedback loop (~2–3 min)**  
- Distinction internal vs human; verbalize checklist disclaimer example (~30 words checklist).

**Capstone (~6–9 min)**  
- Silence + **circulate**: build **their** agent system prompt with **four must-haves**: named Role (+traits), ≥3 numbered CoT steps, ≥2 constraints, explicit Output Format outline.
- Last 120 seconds: votes or **two shout-outs** ("reliable? useful?").
- Honour instructor notes: help stuck groups on Role/CoT first.

**Bridge sentence:** "Take these patterns forward when we plug prompts into frameworks like LangChain and CrewAI."

---

## 11. Key Takeaways, Terminology Sweep & Close (9 minutes)

- Rapid recap bullets matching lecture endings; skim glossary table verbally — spotlight **few vs zero**, **CoT**, **structured prompt**, **self-correction vs iterative**, **feedback loop**.
- **Exit ticket (optional verbal):** "Name one trick you'll use tonight in a personal chat."
- Homework previews / logistics if course requires; reminders about API keys if next lab touches code.

---

## Timing flex — if you are behind schedule

Cut in this **order** (fastest wins first):

1. Shorten Blocks **1**, **11** narrative; glossary table → "read asynchronously."
2. In Block **10**, truncate `study_agent` code to Role + numbered steps only; demo feedback loop verbally without full read.
3. Merge Block **9** iterative story to **ATM Round 1 + Round 2** only; skip Round 3 detail.
4. Block **8** swap activity → instructor shows one anonymous student-safe example instead of pairs.
5. Block **7** → Part B instructor demo only.

If you are **ahead**, extend Block **10** capstone shares or redo Block **5** with volunteer screen-share of outputs — always prioritize **hands-on prompting** over extra theory slides.
