# Lecture Script: GenAI Concepts for Beginners

**Session duration:** 2 hours 15 minutes (total session time, including one scheduled pause)  
**Audience:** Indian learners from mixed backgrounds (not assumed to be technical); first session in Module 3 (Agentic Systems), building on Module 2 classical ML.

---

## Break rule (not a numbered block)

After roughly **60–70 minutes** of instruction (end of Block 4), take **one** break of **5–8 minutes**. Do not start a new major demo during the last 2 minutes before the break—use that time for questions or a quick recap.

---

## How to use this document

This file is **for timing and facilitation only**. It is not a substitute for the full content in `Lecture Notes.md`. Use it to pace the room, manage screen-sharing and live coding, and trigger engagement checks. Keep lecture explanations aligned with the notes and slides/images linked there.

---

## 1. Opening and “Where Classical ML Hits a Wall” (18 minutes)

**Instructor actions**

- Welcome the cohort; state the shift: **Module 2 = tabular ML**; **today = language and LLMs** (Module 3, Session 35).
- Quick callback: joblib, metrics tables, Gradio deployment—then the honest question from the notes: **“Can any of those models write an email?”** Cold-call one student for a one-line “why / why not.”
- Screen-share the **tabular vs language** figure (`session35-01-tabular-vs-language.png`). Narrate: rows/columns vs free-form text.
- Teach **feature engineering bottleneck** with the *“Please reschedule my meeting”* vs *“push the meeting to the next day”* example; pause for **pair-share (90 seconds)**: “What would a single ‘feature column’ miss?”
- **Word ambiguity:** “I went to the bank”—show `session35-02-word-ambiguity-bank.png`; cold-call: “Does the model see meaning or just a label?”
- Summarise **bag-of-Words, keywords, regex** as brittle; **thumbs up/down**: “Has anyone had a chatbot fail because the customer didn’t use the exact keyword?”

**Student actions**

- Recall Module 2 models mentally; participate in pair-share and cold calls.

**Bridge sentence**

“That frustration—language not fitting in a table—is exactly why we need a different kind of model; the bridge is the neural network.”

---

## 2. Neural Networks — Intuition and Learning Loop (16 minutes)

**Instructor actions**

- Connect to **logistic regression** (Session 30): one layer of weighted sum + nonlinearity → **stack many layers** = neural network. Use the “team of decision-makers in a line” analogy from the notes.
- Walk **input → hidden → output** with `session35-03-neural-network-layers.png`; define **deep** simply as “many hidden layers.”
- Teach the **learning loop** (forward pass, loss, backprop, repeat) in plain language; nod to **gradient descent** from Module 2.
- Emphasise the unlock: **unstructured data** (text, images, audio) → numbers → learn patterns—no fixed spreadsheet columns required.

**Student actions**

- Sketch or mentally trace “layers” on paper if helpful; nod to prior regression intuition.

**Bridge sentence**

“Once a network can digest sequences of numbers that represent text, we can tell the story of how we got from Word2Vec to ChatGPT.”

---

## 3. The Rise of Large Language Models (18 minutes)

**Instructor actions**

- Timeline narrative, using `session35-05-llm-evolution-timeline.png` when you show it:
  - **Word2Vec** — vectors and “king − man + woman ≈ queen.”
  - **RNNs** — word-by-word, but **forget early context** in long text.
  - **Transformer (2017)** — attention; use the **“trophy / bag / it”** example from the notes; show `session35-04-transformer-attention.png`.
  - **GPT + pre-training** (next-word prediction at scale) vs **fine-tuning**; contrast with “one random forest per task” thinking.
- **ChatGPT moment** — why the cohort is here: LLMs power agents in this module.
- Quick **check for understanding**: “In one sentence, what did pre-training change about how much ‘the internet’ the model sees?” Cold-call 2 students.

**Student actions**

- Listen for story beats; answer the one-sentence check.

**Bridge sentence**

“Under the hood, the model never sees your sentence as Gmail sees it—it sees **tokens**; let’s make that concrete with code.”

---

## 4. Tokens and Live Tokenisation (`tiktoken`) (18 minutes)

**Instructor actions**

- Define **token** using the notes’ official + simple + Lego analogies; show `session35-06-tokens-lego-blocks.png`.
- Explain **tokenizer**: split → map to vocabulary IDs; round-trip to text.
- **Subword tokenisation** — why not million-word vocabularies; common vs rare word splits.
- **Live demo:** run the `tiktoken` snippet from the notes (`encoding_for_model("gpt-4")`, `encode`, print IDs, decode per token). **Circulate** the room: confirm everyone sees output (or pair with a neighbour if environment issues).
- Assign **60-second try**: Hindi (Roman script) vs English sentence, “Transformer” vs “cat”—compare counts.
- Mention **cost and Indian languages**: more tokens → higher API cost; same idea later for agents.

**Student actions**

- Run or watch the notebook; compare token counts on the suggested sentences.

**Bridge sentence**

“If tokens are the bricks, the **context window** is the size of the table you’re allowed to stack them on in one shot—next we’ll budget memory like an engineer.”

---

**→ After this block (≈ 70 minutes from start), take the scheduled 5–8 minute break.**

---

## 5. Context Windows and Estimation (10 minutes)

**Instructor actions**

- Define **context window** (input + output in one call); use **short-term memory / last pages of a book** analogy; show `session35-07-context-window-viewport.png`.
- Show the **model table** from the notes (4k → 128k → 200k → 1M tokens); relate to “pages” only as rough intuition.
- Lead **Activity 2** verbally: walk through **5,000-word chapter ≈ ~6,667 tokens + prompt** vs **4,096 limit**—then release the three estimation prompts (WhatsApp 200 messages, 50-page PDF, Harry Potter) as **pair-share or small groups (3 minutes)**; debrief highlights only (don’t need exact answers).

**Student actions**

- Estimate with ~0.75 words per token heuristic; discuss in pairs/groups.

**Bridge sentence**

“Even with a huge window, the model isn’t ‘looking up’ your answer—it’s guessing the next token over and over; let’s feel that in our bones.”

---

## 6. Probabilistic Generation and the Sentence Game (10 minutes)

**Instructor actions**

- State clearly: **LLM ≠ search engine** (no single stored document for your query).
- Use **autocomplete** analogy from the notes; keep the explanation verbal—no extra slide required beyond the discussion table.
- **Activity 3 — sentence completion** (Eiffel Tower, tea, door, capital of India, once upon a…): do rapid **round-robin** or **think-pair-share**; tie to high vs spread-out probability.
- Flash the **Search engine vs LLM** comparison table from the notes.

**Student actions**

- Shout or share completions; notice variation vs certainty.

**Bridge sentence**

“When the model samples more wildly, you feel it as **temperature**—and you control it in every major provider’s API.”

---

## 7. Temperature — Live API Experiment (16 minutes)

**Instructor actions**

- Define **temperature** (0–2); show `session35-08-temperature-sampling.png`.
- Stress: **same parameter concept** across OpenAI, Gemini, Claude-class APIs; pick **one** path live based on what most of the class has keys for:
  - **Option A:** OpenAI snippet (`gpt-4o-mini`, 0.1 vs 1.5) from the notes.
  - **Option B:** Gemini snippet (`gemini-1.5-flash`, `GenerationConfig`) from the notes.
- Pre-warn: **no sharing API keys on screen**; use env vars or notebook secrets. **Circulate** while students run or observe.
- Optional quick exercise: “Run high temperature three times—raise hand if all three felt different.”
- Show the **use-case temperature table** (support low, creative high, code low).

**Student actions**

- Run one provider’s example or watch lab partner’s screen; compare outputs.

**Bridge sentence**

“That probabilistic fluency is also why the model can sound right and be wrong—time for **hallucinations**.”

---

## 8. Hallucinations — Safety Frame and Spot-the-Problem (12 minutes)

**Instructor actions**

- Define **hallucination** (confident but wrong/unverifiable); show `session35-09-hallucination-fluent-not-true.png`.
- Brief real examples: **fake legal citations**, medical risk, fake quotes—keep tone serious, not sensational.
- Explain **why**: trained for plausible next tokens, not truth; mention **knowledge cutoff**.
- **Activity 4:** **Pair-share** the three sample responses from the notes; reconvene and reveal hints (1889 vs 1900 fair, Python 4.0, fabricated legal).
- Emphasise **agentic risk**: wrong text → **real actions** (email, bookings, DB updates).
- Tease mitigations: **RAG**, constrained prompts, **human-in-the-loop**, temperature 0 for facts—deeper later in Module 3.

**Student actions**

- Discuss in pairs which lines “smell” fabricated; volunteer one insight per example.

**Bridge sentence**

“Let’s land the plane: a tight summary of what you can actually control Monday morning—tokens, context, temperature, and scepticism.”

---

## 9. Key Takeaways, Quick Reference, and Next Session (9 minutes)

**Instructor actions**

- Rapid-fire the **five bullets** from “Key Takeaways” in the notes.
- Optionally scroll the **Quick Reference** table—invite one student to pick a term and explain it in their own words (**cold-call**).
- Preview **next session: Prompt Engineering** (how phrasing changes quality).
- **Final thumbs up / thumbs sideways**: “How clear is the difference between classical ML tables and LLM tokens?” Address sideways.

**Student actions**

- Note follow-up reading in `Lecture Notes.md`; install libraries if homework requires.

**Bridge sentence**

“Next time we stop admiring the engine and start steering it—with prompts.”

---

## Timing flex (if the session is running late)

**Cut first (preserve one live demo):**

- Shorten **Block 6** (sentence game) to 2 completions + search vs LLM table only (−5 to −7 min).
- In **Block 7**, run **one** temperature only (e.g. high) and narrate what low would do (−6 to −8 min).
- In **Block 5**, do chapter math **solo** instead of all three estimation scenarios (−3 min).
- In **Block 3**, summarise RNN weakness in one sentence; spend less time on Word2Vec arithmetic (−4 min).

**Cut only if still behind:**

- **Block 8:** one hallucination example + Activity 4 Response 2 only (−5 min).
- **Block 4:** students run `tiktoken` on **your** machine while they watch, skip comparative Hindi/English try (−4 min).

**Never skip:** classical ML vs language limitation, tokens + at least one tokenisation demo, probabilistic vs lookup intuition, hallucination definition + agentic risk, and next-session preview (even if 60 seconds).
