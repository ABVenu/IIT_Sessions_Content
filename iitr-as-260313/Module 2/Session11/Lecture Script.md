# Lecture Script: Self-Reflection and Feedback Loops

**Session duration:** 2 hours 15 minutes  
**Target audience:** Beginners (including Indian learners who may not have a prior tech background)

---

**How to use this document**  
This file is for **timing and facilitation only**. It is not a substitute for the full content in *Lecture Notes.md*. Use it to pace the room, manage screen-share and exercises, and keep students engaged. Read examples and definitions from the lecture notes as needed.

**Break rule (not a numbered block)**  
After **60–75 minutes** of session time, take **one** break of **5–8 minutes**. Do not split the break across multiple pauses. Use the break to reset attention before feedback loops and agent prompt flows, which are dense.

---

## 1. Welcome, Context, and Outcomes (10 minutes)

- Welcome the cohort; open slides or *Lecture Notes* “Context of This Session” and “In this session, you will” bullets.
- **Screen-share** the session title. In one line, connect to **last session** (Advanced Prompt Engineering for Agents — structure, chain-of-thought) and the **pivot** for today: the AI can still be wrong, so we teach it to *check and improve* its own work.
- **Room action:** Ask for a **thumbs up** if anyone has already asked a model to “improve that answer” or “check your work” in chat — build familiarity with the idea.
- State the **three pillars** of today (in plain terms): (1) self-reflection and self-correction, (2) iterative prompting, (3) feedback loops and full agent-style prompt flows.
- **Cold-call (1–2 people):** “In one sentence, when has an AI’s first answer been ‘technically not wrong’ but useless to you or a user?”
- **Bridge sentence:** *“We’re going to name that failure mode, then give you a toolbelt so your agents don’t stop at the first draft.”*

---

## 2. Why Self-Reflection: Problem, Definition, and “With vs Without” (15 minutes)

- Walk through the **customer support jacket** example: first answer = “contact support” — *not* wrong, but useless.
- Define **self-reflection** in facilitator language: the model (or your prompt) **reviews, evaluates, and revises** before the user sees the final.
- **Screen-share** the **healthy morning routine** side-by-side: “without reflection” (vague) vs “with reflection” (checklist + rewrite). Do **not** read every line; highlight *why* the second wins (specific, timed, beginner-friendly).
- **Pair-share (2 minutes):** Pairs name **one** thing the weak routine answer is missing (e.g. time, steps, audience). Debrief 1–2 pairs.
- Introduce the **“thinking twice”** idea: first draft = rough; second pass = proof-reader, not just spell-check.
- **Bridge sentence:** *“Reflection you can *prompt in’ is self-correction — we’re going to lock that into three explicit stages so the model can’t skip the middle step.”*

---

## 3. Self-Correction Prompts: Three Stages, Sleep Example, Design Rules (16 minutes)

- Teach **Stage 1 — Generate, Stage 2 — Critique, Stage 3 — Rewrite**. Emphasize: **labels matter**; otherwise the model may skip critique.
- **Screen-share** the **sleep and students** self-correction example. Spend time on **Stage 2** — that list of gaps is what makes Stage 3 good.
- Cover **design rules:** separate stages, tell the model what to look for in critique, avoid the fake self-correction line (“give me a perfect answer”).
- **Check for understanding:** “**Thumbs up** if you can say out loud the three stage names in order — no notes.”
- **Bridge sentence:** *“Same human habit — draft, note, fix — is **iterative prompting** when *you* drive each round. Let’s switch from one long prompt to many short, aimed prompts.”*

---

## 4. Iterative Prompting: When One-Shot Fails, the Cycle, ATM Story (12 minutes)

- **One line:** one-shot is fine for “boiling point of water”; for complex tasks, one shot often gives a **title slide**, not a proposal.
- **Screen-share** the **business proposal** one-shot “failure” — ask the room what dimension is missing (market, numbers, USP, etc.).
- Teach the **four steps:** Draft → Review → Refine (one thing) → Repeat. Stress **one fix per follow-up** and **3–5 rounds** as a healthy range.
- Walk the **ATM for a village student** in **three rounds** — only skim Round 3 text; focus the story: Round 1 too jargon-heavy → Round 2 analogies → Round 3 cash source + account balance.
- **Room action:** “What would *you* ask in Round 2?” **Cold-call** one student before revealing the notes’ follow-up.
- **Bridge sentence:** *“When you’re not in the chat for every user message, the agent must loop on **criteria** — that’s a feedback loop.”*

---

## 5. Pre-Break: User vs Internal Loops, Thermostat, Disclaimer Mini-Loop (12 minutes)

- Contrast **chat** (you’re always there) vs **agent at scale** (you’re not).
- **Feedback loop in one line:** output → check against a standard → feed result back until good.
- **User vs internal** — quick role-play: *user says “too vague, three facts”* vs *prompt says “check word count, warning, doctor — rewrite until yes”* (disclaimer).
- **Optional quick poll (hands or Zoom poll):** “Which loop needs a human in the room for every turn?” (User — but internal runs alone.)
- **Bridge sentence before break:** *“After the break we’ll build a full **checklist** into a **job application email** and then into a four-part **agent prompt flow** — role, task, reflection, output.”*

**→ Take the 5–8 minute break here** (you should be near the 60–75 minute window if you started on time).

---

## 6. Building Feedback-Loop Prompts: Job Application Email (19 minutes)

- **Screen-share** the **four parts:** Generate, Evaluate, Improve, Deliver — and the **email** with Attempt 1 vs self-eval → Attempt 2.
- **Circulate** (or in online: ask students in chat) to find **one failed criterion** in Attempt 1’s opening. Tie to *measurable* Yes/No checks.
- When to use **user** vs **internal** feedback (creative vs checklist tasks).
- **Pair-share (90 seconds):** “Name one **measurable** criterion for *your* last assignment email or message.”
- **Bridge sentence:** *“We’ve used pieces; now we **assemble** them: role, task, reflection criteria, and output format in one flow.”*

---

## 7. Complete Agent Prompt Flow: Four Components, Shopkeeper + ML (14 minutes)

- **Four components:** Role, Task, Reflection + feedback criteria, Output format — each a **guardrail**.
- **Screen-share** “Explain ML simply” **bad** (jargon) vs **good** flow: shopkeeper, rice, helper — reflection criteria *force* the rewrite.
- **Thumbs up / thumbs down:** “Would a non-technical family member get the *bad* version?” (Down.) “The *good* version?” (Up.)
- **Bridge sentence:** *“You now have three *strategies* — one-shot, iterative, reflection. The job is to pick the right one like tools in a box.”*

---

## 8. Comparing Strategies: Table + One Task Three Ways (8 minutes)

- **Screen-share** the **comparison table** (one-shot vs iterative vs reflection-based).
- Run the **high blood pressure health tip** in three **speed modes**: one-sentence one-shot, three-line iterative story, one reflection-based outcome — map each to the table’s “best suited” column.
- State the **golden rule** in your own words; invite **one cold-call** for a real project: “Which strategy would *you* use first?”
- **Bridge sentence:** *“Next we *practice* strengthening a weak prompt the way you’ll do on the job — one gap at a time.”*

---

## 9. Practicing Prompt Refinement: “Online Safety” (5 minutes)

- **Option A (time tight):** You demonstrate **Rounds 1–3** of the *online safety* exercise on screen.  
- **Option B (if energy is high):** Students in **pairs** add **one** refinement (e.g. audience, or one new rule) in the chat, not the full exercise.
- Close with: Round 1 = **role + audience**, Round 2 = **scenario**, Round 3 = **reflection + format**.
- **Bridge sentence:** *“To fix outputs, you must **see** bad output — the next block is a **quality radar**: five failure types and the EVAL check.”*

---

## 10. Evaluating Response Quality: Five Bad Types + EVAL + Corrections (10 minutes)

- Rapid-fire **five types:** hallucination, vagueness, incomplete, wrong format, logical contradiction — one **short** example each from the notes (Python inventor is the memorable hallucination).
- Teach **EVAL: Exactness, Validity, Adequacy, Layout** as the **exit checklist** for any output.
- **Screen-share** **weak** vs **strong** correction: “wrong, try again” vs pointing at the *wrong name* and the *fix*.
- **Cold-call:** “Which letter of EVAL does ‘wrong person for Python’ fail?” (Validity.)
- **Bridge sentence:** *“Last stretch: make loops **fast and reusable** in production — measurable criteria, small loops, templates.”*

---

## 11. Optimizing Feedback Loops, Master Template, Key Takeaways (7 minutes)

- **Four principles:** measurable criteria, **2–3** cycles max, **template** the working flow, **layer** criteria gradually (Stage 1–3 loop).
- **Screen-share** the **master [ROLE] / [TASK] / [REFLECTION] / [LOOP] / [OUTPUT]** template; say clearly: *this is your default skeleton for future sessions*.
- Skim **Key Takeaways** bullets from *Lecture Notes*; tie back to “next: multi-step and multi-agent pipelines.”
- **Final engagement:** “**One thing** you’ll change in your next prompt” in chat or popcorn **3 students**.
- Thank the room; point to the glossary in *Lecture Notes* if you need definitions on the way out.

**Bridge sentence (session close):** *“The pattern today — draft, check, improve — is the same pattern we’ll stack when multiple agents hand work to each other. See you in the next session with that in your toolkit.”*

---

## Timing flex (if you are running late)

**Cut in this order** (saves approximately):

1. **5–7 min:** Shorten the **ATM** story to Rounds 1 and 2 only; assign Round 3 as “read at home in Lecture Notes.”
2. **4–5 min:** Drop **Option B** pair work in Block 9; only demo the online safety refinements.
3. **3–4 min:** In Block 6, show **self-eval** for Attempt 1 only; summarize Attempt 2 without line-by-line read.
4. **3 min:** In Block 10, cover **three** of the five bad types (keep hallucination, vagueness, wrong format) and mention the other two in one line.
5. **2–3 min:** Table in Block 8 — read the “best suited” column only, skip the long health tip quotes.

**If you are *ahead* of time:** add **unstructured Q&A** (3–5 min), or expand Block 9 into full pair drafting of a **second** follow-up for online safety, then debrief one pair.

**If you need to end exactly on the clock:** skip the “Key Takeaways” read-aloud and send them as a **one-slide summary** or “first 3 bullets only” in Block 11.

---

*Generated for alignment with* Lecture Notes: Self-Reflection and Feedback Loops *and* `LectureScriptPrompt2.md` *requirements.*
