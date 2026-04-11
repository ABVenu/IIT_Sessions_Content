# Lecture Script: Agent Behavior & Understanding the LLM Layer

**Session duration:** 2 hours 15 minutes  
**Audience:** Indian students from varied backgrounds; limited or no prior tech exposure. Keep language plain; define API, token, and transformer in everyday terms before abbreviations stick.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a verbatim transcript. Use the blocks to pace the room, manage screen-share, and place checks for understanding. Adapt wording to your voice; keep the time boxes and engagement beats.

---

## Break rule (not a numbered block)

After roughly **60–75 minutes** of instruction, take **one** break of **5–8 minutes**. Do not schedule multiple formal breaks in the script. If you start late or need to compress, shorten the break or merge light content (see **Timing flex** at the end).

---

## 1. Opening, bridge from Session 7, and what is an LLM? (14 minutes)

**Facilitator actions**

- Screen-share the session title; connect to **last session**: Planning, Reasoning, Memory, Action; Observe → Think → Act — then pose the hook: **what is actually doing the thinking inside the agent?**
- Answer in one beat: **Large Language Model (LLM)**. Promise: no heavy math — concepts and examples only.
- Teach **official definition** + **text in → text out** as the simplest mental model (preview; you will deepen in Block 2).
- **Scholar who read everything** and **autocomplete that grew up** — keep each analogy under 90 seconds.
- Display the **three words** table (Large / Language / Model); read one row at a time.
- Optional: **Cold-call** — “Name one thing you already used this week that might sit on top of an LLM.”

**Students do**

- Recall the four agent components and the loop; add “LLM = brain” as today’s new label.

**Engagement**

- **Thumbs up** if the session goal is clear: *what an LLM is, what it can and cannot do, who builds them, how agents use them, high-level “how.”*

**Bridge sentence**

“That ‘text in, text out’ idea is the spine of everything else — let’s make it concrete with examples.”

---

## 2. Core behavior: text in → text out (10 minutes)

**Facilitator actions**

- State the rule plainly: **input text → output text**; everything else is a variation.
- Walk the **examples table** (capital of India, Hindi translation, summarize, Python function, chef persona, story continue) — skim, do not read every cell aloud unless the room is quiet.
- **Critical insight:** same model, no separate “modes” — task shape comes from the *prompt text*.
- Quick **pair-share (2 minutes):** One partner gives a hypothetical “input”; the other says what kind of “output” might come back.

**Students do**

- Internalize: the LLM is not switching apps — it is continuing text based on what it received.

**Engagement**

- **Cold-call** one pair for their favorite input/output pair.

**Bridge sentence**

“Now we plug this machine into the agent you already understand — the LLM sits in the Think stage.”

---

## 3. The LLM as the agent’s “brain” and the weather mini-example (12 minutes)

**Facilitator actions**

- Map **Planning / Reasoning / Memory / Action** to “who thinks?” → **LLM as central reasoning engine** (definitions from notes).
- **CEO and staff** analogy: LLM decides; tools execute.
- Display **Observe → Think ← LLM → Act** diagram; emphasize **Think** is where the LLM runs.
- Walk **Mumbai weather** mini-example line by line: prompt to decide tool → API → result back to LLM → user-facing reply. Stress **orchestration** vs **thinking**.

**Students do**

- Trace verbally: after the API returns, what is the next Observe?

**Engagement**

- **Thumbs sideways** if “LLM is only in Think, not in every line of code” makes sense.

**Bridge sentence**

“Same brain can wear many hats — next we list what kinds of tasks it can handle in one interface.”

---

## 4. What an LLM can do: seven capabilities (15 minutes)

**Facilitator actions**

- Introduce as a **menu**, not seven mini-lectures: Q&A; summarization; generation; translation; code + explanation; classification/extraction; reasoning/word problems.
- For **Q&A**, state the **nuance:** from training, not live Google — **cricket match yesterday** example for cutoff (preview Limitations block).
- One **India-relevant** example for summarization (e.g. policy doc → bullets) if time.
- Close with **why versatility matters for agents:** one generalist vs many hardcoded programs.

**Students do**

- Pick two capabilities they would want in a “personal assistant agent” and why.

**Engagement**

- Rapid **raise of hands:** “Which capability would you trust least without verification?” (often facts or math — tee up later limits.)

**Bridge sentence**

“Capabilities depend entirely on what you *send* — that input text has a name: the prompt.”

---

## 5. Prompts: the instructions that shape output (11 minutes)

**Facilitator actions**

- **Prompt** definition: input text = instruction + shape of answer.
- **Stationery shop** analogy: vague vs specific pen request.
- Walk **photosynthesis** prompt table — five outputs, **same model**, different prompts.
- **Agent prompt ingredients:** Role, Context, Task, Format — one line each; say deeper prompt design comes later.
- Key line: **quality of thinking ≈ quality of prompt construction.**

**Students do**

- Rewrite mentally: one vague ask → one specific ask for the same topic.

**Engagement**

- **Pair-share (90 seconds):** A “role + task” one-liner for a fake customer-support agent.

**Bridge sentence**

“Prompts let us steer the model — next we separate where models are genuinely strong from where they are dangerously weak.”

---

## 6. Strengths and limitations (16 minutes)

**Facilitator actions**

**Strengths (about 6 minutes):** Natural language understanding (e.g. “Can you not make it simpler?”); generalization across topics; flexible output formats; in-context learning (3 complaint examples); multi-step language reasoning.

**Limitations (about 10 minutes):** Spend **extra time on hallucination** — definition, exam-student analogy, IIT professor books / legal citation examples, **why** (patterns not lookup), **agent risk** (actions on fake facts). Then brisk: **training cutoff** + search fix; **math** + code tool fix; **inconsistency** + review for legal/medical/financial; **context window** + “forgot message #5” — “tokens next block.”

**Students do**

- Note one strength they will leverage and one limit they will **never** trust blindly.

**Engagement**

- **Think-pair-share:** “One real-world harm from a hallucination in an agent that sends email or files.”

**Bridge sentence**

“Those brains are built by a small set of big companies — useful to know the names and flavors.”

---

## 7. Who builds LLMs? Major providers (11 minutes)

**Facilitator actions**

- Frame: you do not forge the engine; you **use** it — **model providers**.
- **OpenAI** (GPT, ChatGPT, API) — showroom vs service door analogy.
- **Google DeepMind** (Gemini, Search/Workspace); mention **Transformer** invention tease.
- **Anthropic** (Claude, safety emphasis) — sports car vs safety-featured car analogy.
- **Meta** (LLaMA, **open source** — weights available; why that matters for researchers).
- Walk **comparison table**; close: different brands, **same fundamental family** — Transformer (next section).

**Students do**

- Match “I would try first in a browser” vs “I would read about open weights” to any two providers.

**Engagement**

- Optional **chat poll:** “Which provider name was new to you today?”

**Bridge sentence**

“Naming providers is step one; step two is how your code actually talks to them — usually an API.”

---

## 8. How LLMs are used: APIs (conceptual) (9 minutes)

**Facilitator actions**

- **API** definition: software talking to software; **waiter / kitchen** and **electricity grid** analogies from notes.
- **Six conceptual steps:** code → prompt to server → GPUs → response → back to code → use result.
- Project the **simplified Python snippet**; read pattern only: `prompt` → `create` → `message.content`. Explicitly say **full coding comes later** — today is pattern recognition.
- **Agent implication:** many Think cycles → many API calls → **cost** links to tokens (next).

**Students do**

- Complete the sentence: “An API carries ___ in and ___ out.”

**Engagement**

- **Thumbs up** if “I don’t need to memorize the code” feels okay.

**Bridge sentence**

“Providers charge and models limit size by chunks of text — those chunks are tokens.”

---

## 9. Tokens, context window, cost, and speed (9 minutes)

**Facilitator actions**

- **Token** definition: bite-sized pieces; not always whole words — show 2–3 examples from notes (Hello vs Unbelievable vs biryani).
- **Roti pieces** analogy.
- **Three reasons tokens matter:** context window (max tokens per call; cite rough GPT/Claude numbers as *order of magnitude*); **cost** (input + output tokens); **speed**.
- Mention **tiktoken** / tools — no manual counting required.
- Tie back to **Limitation 5** (long chat forgets early messages).

**Students do**

- Estimation game: “Roughly more tokens — longer prompt or shorter prompt?”

**Engagement**

- **Cold-call:** “Why might a 500-page document break a single prompt?”

**Bridge sentence**

“Tokens are processed by a specific architecture — the Transformer — and one idea inside it is attention.”

---

## 10. Transformer and attention (intuition only) (12 minutes)

**Facilitator actions**

- **Before 2017 vs after:** “Attention Is All You Need”; **Transformer** = blueprint for GPT, Gemini, Claude, LLaMA.
- **Bicycle vs car engine** analogy; **before:** word-by-word, forget start; **after:** whole input, relationships across distance.
- **Attention** definition in plain language: which words matter for understanding this word?
- **Trophy / suitcase “it”** — walk slowly; **river bank vs money bank**.
- **Spotlight at concert** analogy; end with: **no math required today** — intuition = every word can relate to every other word.

**Students do**

- Paraphrase attention in one sentence to a neighbor.

**Engagement**

- If energy is low, **stand and stretch** for 30 seconds before the diagram in Block 11 (optional micro-movement).

**Bridge sentence**

“We now zoom out: LLM + memory + tools in one picture, then failure stories.”

---

## 11. Connecting the LLM to the full agent flow (8 minutes)

**Facilitator actions**

- Display **full diagram**: User → Agent (memory, tools, **LLM**) → loop → user.
- Walk **loop stage table**: Observe (LLM off) → Think (plan, reason, decide — LLM on) → Act (execute — LLM off) → Observe with tool result (LLM on for interpretation).
- Anchor phrase: **LLM = thinker; Python = executor** (or your course’s language).

**Students do**

- Point on screen to where **tool** runs vs where **LLM** runs.

**Engagement**

- **One-minute** silent look at the diagram; then one clarifying question only.

**Bridge sentence**

“When the brain fails, the agent fails in public — let’s make those cases memorable.”

---

## 12. When agents fail because of LLM limits, recap, and quick reference (18 minutes)

**Facilitator actions**

- **Four failure examples** from notes — **Hyderabad hospitals** (hallucination + search fix); **SBI FD rate** (stale training + real-time tool); **essay grading** (inconsistency + temperature + rubric); **invoice totals** (math + code execution). Two minutes each max.
- **Big picture recap** as a spoken chain: LLM definition → brain → API → prompt → providers → tokens → Transformer/attention → limits → Think vs Act.
- Display **Quick Reference** table; invite photo or download; read **only** 3–4 rows aloud (e.g. hallucination, token, context window, temperature).
- Preview **next sessions:** deeper prompting, more code — today was the conceptual layer.

**Students do**

- **Exit ticket** (chat or slip): “One limitation you will design around first” + “one term to look up before next class.”

**Engagement**

- Final **cold-call:** “Fix in one phrase for the hospital report agent.”

**Bridge sentence**

“You now know what sits inside the Think stage — next we make that stage reliable with tools, prompts, and discipline.”

---

## Timing flex

**If you are 10–15 minutes behind**

- Shorten Block 4: cover capabilities as a numbered list with one example total for the group.  
- In Block 6, deliver limitations as **headlines + one example** each; keep hallucination at full length, trim in-context learning story in strengths.  
- In Block 10, cover only **trophy/suitcase** and skip the concert spotlight analogy.

**If you are 15–25 minutes behind**

- Merge Block 2 into Block 1 (eight minutes total for text in/out).  
- Skip Block 11 live diagram; give **one static slide** of Think vs Act only.  
- Reduce Block 12 to **two** failure stories (hallucination + math) plus a 60-second recap; send Quick Reference as reading.

**If you finish early**

- Expand Block 6 with **temperature** and rubric discussion using grading example.  
- Optional: show a provider’s public pricing page and relate to tokens (stay conceptual).

**Break placement**

- Natural pause after Block 6 (strengths/limits) or after Block 7 (providers) if the clock hit ~65 minutes; resume with APIs or Tokens.
