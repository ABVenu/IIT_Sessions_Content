# Lecture Script: GenAI Concepts for Beginners

**Session Duration:** 1 Hour 50 Minutes  
**Audience:** Absolute beginners (Indian students, little or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Keep the detailed explanations, definitions, diagrams, and code snippets in *Lecture Notes.md*; use this script to run the room, share screens, and check that learners are following on their machines.

---

## Break rule

After roughly **55–65 minutes** of session time, take **one** break of **5–8 minutes**. Do **not** treat the break as a numbered teaching block — announce it, pause the recording if applicable, and resume with the bridge into block 6.

---

## 1. Opening, recap, and session roadmap (8 minutes)

**Facilitator**

- Welcome the group; confirm everyone can open **Google Colab** (or your chosen notebook environment).
- **Cold-call** one or two students: “In the **previous session**, what did we use to **save a trained model** to disk — name the library.” Accept **joblib**.
- Bridge from Module 2 close-out: we compared models in **metric tables**, judged **complexity**, and walked a **selection checklist** — all on **tabular data**. Today the input is **free-form language**.
- Project the four session goals from the notes (LLM vs rule-based, tokens & context, hallucinations & failure modes, relate GenAI to ML without maths).
- Set expectations: **mental models first** — heavy API and agent builds come later in the module.

**Students**

- Connect today’s topic to regression/classification from earlier weeks — rows and columns in, prediction out.

**Engagement**

- **Thumbs up:** “Thumbs up if you have used **ChatGPT** or a similar assistant at least once this week.”

**Bridge sentence:** “Let’s name the shift properly — from **spreadsheet ML** to **Generative AI** — before we touch a single line of code.”

---

## 2. From classical ML to Generative AI (10 minutes)

**Facilitator**

- Walk the **ML vs GenAI comparison table** from the notes line by line — same pattern-learning idea, different input/output shape.
- Define **GenAI** in one sentence: systems that **create new content**, not only classify or score.
- Use the **spam filter vs ChatGPT** example — classical ML sorts mail; GenAI drafts the reply.
- Stress: no matrix calculus required today — you need an accurate **mental model**, not training maths.
- Link to prior habits: **baselines**, **fair comparison**, and **“does this tool fit the job?”** still matter with LLMs.

**Students**

- In chat or notebook, write one sentence: “Classical ML answers ___ ; GenAI answers ___.”

**Engagement**

- **Cold-call:** “Name one model from the ML workshop — logistic regression, random forest, K-Means — and say what type of **output** it produced.”

**Bridge sentence:** “Language breaks the table — so engineers tried **rules** first, then **LLMs**; let’s compare those two worlds side by side.”

---

## 3. Rule-based software vs token-based LLMs (14 minutes)

**Facilitator**

- Define **rule-based software** — fixed `if`/keyword paths; **IVR menu** analogy.
- Define **token-based LLM** — autocomplete at internet scale; generates **one token at a time**.
- **Screen-share** the tabular-vs-language diagram and the **rule-based vs LLM comparison table** from the notes.
- Run the **Spot the Rule Break** activity — three refund messages; reveal that only message 1 hits the keyword *refund*.
- **Live-code** the tiny **rule-based support router** from the notes (`rule_based_support` + three test messages). Narrate line by line — no ML library needed.
- Close the contrast: rules are **predictable but brittle**; LLMs handle **paraphrase** but can **hallucinate**.

**Students**

- Answer the Spot the Rule Break activity in chat before you reveal.
- Run the rule-based demo in Colab; confirm three printed customer/bot pairs.

**Engagement**

- **Pair-share (2 minutes):** Partner A explains when rules are **enough** (OTP flow, menu routing); Partner B explains when an **LLM** is worth the risk.

**Bridge sentence:** “Rules are frozen flowcharts — now let’s meet the **Large Language Model** itself and the short story of how it got here.”

---

## 4. What is an LLM and the rise of LLMs (15 minutes)

**Facilitator**

- Define **LLM** — engine behind ChatGPT, Gemini, Claude, LLaMA; **text in → text out** via **prompt** and **completion**.
- Use the **junior copywriter** analogy — fast drafter, can state wrong facts confidently.
- Contrast with **Random Forest** from the workshop — not trained on 500 tumour rows; **pre-trained** once on massive text by predicting the **next token**.
- Walk the **five beats** from the notes at bird’s-eye level only — words as numbers → RNNs forget long context → **Transformer (2017)** → **GPT pre-training** → **ChatGPT (2022)**.
- **Screen-share** the transformer-attention and LLM-evolution timeline diagrams.
- Answer the common doubt aloud: ChatGPT does **not** browse the web by default — it **generates** from training patterns plus what you paste in the prompt.

**Students**

- Note three vocabulary words: **prompt**, **completion**, **pre-training**.

**Engagement**

- **Cold-call:** “In the trophy-and-bag sentence from the notes — what does **it** refer to, and why does that matter for language understanding?”

**Bridge sentence:** “The model never sees your words on screen — it sees **tokens**; that is where cost, speed, and limits begin.”

---

## 5. Tokens — counting and comparing in Python (17 minutes)

**Facilitator**

- Define **token** — Lego brick of text; **ration shop** bills by kilograms, APIs bill by **tokens**.
- **Screen-share** the tokens-as-Lego diagram and the **what you type vs token reality** table — flag **Indian languages** often costing **2–3×** more tokens for the same meaning.
- State the planning rule of thumb: ~**1 token ≈ 0.75 English words** — measure for real work.
- **Live-code** the **tiktoken** block from the notes: `pip install tiktoken` if needed → `cl100k_base` → three samples (English, Hinglish mix, long URL) → print counts and token pieces.
- Pause on output — point at how URLs and punctuation explode token count.
- Run the **Estimate Before You Measure** activity verbally — ask for guesses on a 10-word email vs Hindi paragraph vs 800-word paste; then measure one example live.

**Students**

- Run the same tiktoken cells; **check screens** — everyone should see three labelled token counts.
- Optional: students replace `hindi_english_mix` with one sentence in **Devanagari** and compare counts.

**Engagement**

- **Thumbs up:** “Thumbs up if your Hinglish or Hindi sample used **more tokens** than the English fox sentence.”

**Bridge sentence:** “Tokens are the currency — next we ask how many fit in the model’s **tiffin box** at once: the **context window**.”

---

## 6. Context windows — limits and the fit checker (17 minutes)

**Facilitator**

- Define **context window** — max tokens in **one API call**; prompt **plus** answer share the same box.
- **Screen-share** the context-window viewport diagram and the **model comparison table** (4k vs 128k vs 1M).
- Explain **usable context** — reserve space for the **reply** and **system instructions**; overflow often **drops the beginning** without a loud error.
- **Live-code** `check_context_fit` from the notes on the `long_chapter` placeholder — show `fits: False` and `overflow_tokens`.
- Walk **Context Budget Estimation** scenario 1 (WhatsApp thread vs 4,096) on the board — rough math, then optional tiktoken check on a short thread sample.
- Mention agent foreshadowing: **history + instructions + tool logs** compete for the same window in later sessions.

**Students**

- Run `check_context_fit`; change `MODEL_CONTEXT_LIMIT` to `128000` and re-run — observe `fits` flip to True for the same text.
- Paper estimate for scenario 3 (system prompt + chat + tool log totals).

**Engagement**

- **Cold-call:** “If the box is full, what typically gets dropped first — the **oldest** chat turns or the **newest** user message?” Accept oldest / early instructions.

**Bridge sentence:** “Knowing the box size explains **forgetting** — knowing **how text is written** explains why answers can change and sound true when they are not.”

---

## 7. Probabilistic generation — prediction, not retrieval (10 minutes)

**Facilitator**

- Define **probabilistic text generation** — one token at a time, not a filing-cabinet lookup.
- **Screen-share** the search-engine vs LLM table and the fluent-not-true diagram.
- Mention **temperature** in one line — low = steadier, high = more varied; you will tune it when building apps.
- Run the **Sentence Completion Game** — read starters 1–5; ask students to shout or type the first word that comes to mind.
- Debrief: starters 1, 4, 5 have one dominant answer; starter 2 has many — links to **sampling** and **inconsistency** across runs.

**Students**

- Play the completion game in chat or aloud; note which starters felt “forced” to one answer.

**Engagement**

- **Cold-call:** “Is an LLM more like **Google Search** or **phone autocomplete** — and can it invent text that was never on any webpage?”

**Bridge sentence:** “Fluent autocomplete is the superpower and the trap — let’s name the trap: **hallucinations** and the other ways these models fail.”

---

## 8. Hallucinations, failure modes, and close the mental model (14 minutes)

**Facilitator**

- Define **hallucination** — confident, fluent, **false**; tell the **2023 lawyers / fake court cases** story briefly.
- Walk the **failure modes table** — knowledge cutoff, no live data, math errors, inconsistency, sycophancy, context loss, bias.
- Run **Failure Mode Detective** — four scenarios; reveal answers from the notes after 2 minutes of chat silence.
- Stress mitigation preview only: ground in documents, refuse when unsure, human review for high stakes — built later in the module.
- Rapid **key takeaways** from the notes (five bullets).
- Point learners to the **Quick Reference** terminology table for revision.
- Preview lightly: **upcoming** work covers **prompt engineering**, APIs, and retrieval — today’s vocabulary is the floor.

**Students**

- Label the four detective scenarios in chat before reveal.
- Star three terms to remember: **token**, **context window**, **hallucination**.

**Engagement**

- Final **cold-call:** “A bot forgets *respond only in Hindi* after 40 messages — which failure mode is that?” Accept **context loss**.

**Bridge sentence:** “You now have the beginner’s map — **tokens**, **context**, **generation**, and **failure** — carry it into every prompt and agent you build from here.”

---

## 9. Recap and session close (5 minutes)

**Facilitator**

- One-minute synthesis: classical ML vs GenAI; rules vs LLMs; tokens & context window; probabilistic generation; hallucinations & failure modes.
- Remind learners to skim *Preread.md* gaps if they joined late.
- Announce assignment or tutorial expectations if applicable for the cohort.
- End on energy: accurate mental models prevent expensive mistakes when agents start **acting**, not only **chatting**.

**Students**

- Optional: one-sentence exit ticket in chat — “The biggest surprise for me today was ___.”

**Engagement**

- **Thumbs up:** “Thumbs up if you can explain to a friend why **confident tone ≠ correct facts**.”

**Bridge sentence:** “Close your notebook knowing **what the model eats, what it forgets, and why it sometimes makes things up** — that is the discipline every agent builder needs.”

---

## Timing flex — if you are running late

- **Cut first (save core demos):** Shorten pair-shares from 2 minutes to 1; compress the five-beat LLM history to three beats (Transformer → pre-training → ChatGPT); show diagrams briefly instead of full narration; do token estimation verbally without waiting for all chat guesses.
- **Cut second:** In block 5, live-code **English + URL samples only** — assign Hinglish comparison as post-class. In block 6, demo `check_context_fit` once; skip handwritten budget scenario 3. In block 7, run three sentence completions instead of five.
- **Never skip:** Block 3 (rule-based vs LLM contrast + Spot the Rule Break), block 5 (**tiktoken** live count), block 6 (**context window** + `check_context_fit`), and block 8 (**hallucination** definition + at least four failure modes) — these are the session’s core outcomes per metadata.
- **If ahead of schedule:** Add 5 minutes for students to paste their own **WhatsApp-length paragraph** into `check_context_fit`; or run a **mini-poll**: “Would you trust an LLM alone for a **medical dosage** decision — yes/no and one-word why?”
