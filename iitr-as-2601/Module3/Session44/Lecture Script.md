# Lecture Script: LLM Internals for Designers

**Session duration:** 1 hour 50 minutes (110 minutes)  
**Audience:** Absolute beginners — Indian learners from any background; they should have built **RAG**, **conversation memory**, and **tool-using agents** in prior labs. Today is **designer-facing internals** — tokens, context limits, temperature, and what users feel when context runs out. **Not** model training or deep engineering.

---

**How to use this document**  
This file is **for timing and facilitation only**. It does not replace `Lecture Notes.md`; it tells you *what to do in the room*, when to circulate, and how to bridge topics. Keep definitions, code blocks, diagram URLs, and activity tables on the notes file / projector.

**Break rule**  
After **approximately 55–65 minutes** from session start (typically once **RAG token budget** and **`build_context_block`** are demonstrated — **before** the truncation simulation), take **one pause of 5–8 minutes**. Do **not** count the break as a numbered block; resume with Block 7 (memory & truncation).

---

## 1. Opening & Session Map (5 minutes)

- Screen-share `Lecture Notes.md` — show **session44-01** image: RAG + memory + tools share one **context window**.
- State today aloud: you are **not** training models; you are learning what drives **billing**, **latency**, **consistency**, and **user-visible bugs** when chats get long.
- Read the **"What you will learn"** four bullets; **thumbs up** if anyone is unsure what a **token** is (promise replay in Block 3).
- **Cold-call:** "Name one thing from a prior RAG lab that gets sent to the LLM besides the user's question." *(retrieved chunks, instructions, etc.)*

**Bridge sentence:** "You've already packed RAG, memory, and tools into API calls — today we measure what that packing costs and what breaks when the box is full."

---

## 2. Why Designers Need LLM Internals (7 minutes)

- Walk **tiffin box** and **DMRC metro capacity** analogies from notes — 60 seconds each.
- Screen-share the **Common design decision** table (`top_k`, chat history file, verbose trace, `temperature=0`).
- Emphasise the two **core design questions** aloud: *How much can I pack in?* and *Why did the bot forget turn three?*
- **Common mistake** line: LLM is **not** unlimited Google Drive.
- **Pair-share (30 seconds):** Partner A names one design knob; Partner B names the hidden internal it affects.

**Bridge sentence:** "Those knobs all boil down to one unit the API actually counts — **tokens** — which are not the same as words on your screen."

---

## 3. Tokens vs Words & tiktoken Live Demo (15 minutes)

- Official definition + **ration shop / kilograms** analogy.
- Screen-share **session44-02** image — words on screen vs tokens billed.
- Walk the **What you see / What API measures** table — stress **URLs** and **Hindi + English** gaps.
- **Rule of thumb:** ~4 characters ≈ 1 token — planning only; **measure** in production.
- Cover **billing**, **latency**, and **prompt length** bullets — one minute each.
- **Common doubt:** Groq feels slow → often **token volume**, not brand.
- **Live-code** (screen-share notebook): `pip install tiktoken` if needed, then the **Measuring Tokens in Python** block from notes.
  - Run on the sample Acme Corp RAG prompt; point at **word count vs token count** printout.
  - Mention **Groq / Llama note:** tiktoken is **budgeting-close**, not exact billing.
- **Circulate / scan chat:** fix `ModuleNotFoundError` before Activity 1.
- **Thumbs-up check:** "Thumbs up when you see both word and token numbers printed."

**Bridge sentence:** "You can count tokens now — let's budget a full RAG prompt and see what one question really costs."

---

## 4. Activity 1 — Token Budget for One RAG Call (12 minutes)

- Post Activity 1 instructions from notes on projector.
- **Room action:** learners build a sample prompt — instructions + 3 chunks with `=== CONTEXT START/END ===` + one question — and run it through their **tiktoken** cell.
- **Circulate:** check fill-in table progress — instructions / chunks / question / **total input**.
- Prompt follow-ups aloud after ~8 minutes:
  1. Percentage of an **8,000-token** window used?
  2. Input cost at **₹0.002 per 1,000 input tokens**?
  3. What to trim first for **slow replies**?
- **Cold-call:** "Who will share their **total input** token count — ballpark is fine?"
- **Check for thumbs:** "Thumbs up if your total is under half the 8k window for this single question."

**Bridge sentence:** "One question can eat a surprising slice of the window — next we name the ceiling itself and everything that competes inside it."

---

## 5. Context Window & Shared Budget (10 minutes)

- **Context window** definition + **exam answer sheet** analogy.
- Model class table (4k–8k / 8k–32k / 128k+) — remind: check **provider docs** for exact numbers.
- **Input + output share one budget** — 7k prompt + 8k window ≈ 1k left for answer.
- Screen-share **session44-03** image — stacked blocks: system, RAG, history, tools, question, output slot.
- Briefly narrate the **mermaid** flow from notes if rendered; otherwise use the image.
- **Memory implication:** file on disk ≠ what model sees this turn.
- **Design pattern:** **progressive disclosure** — low `top_k` first, raise only if answer is thin.
- **Cold-call:** "What gets pushed out silently if you raise `top_k` without shrinking chunks?" *(older chat turns / other blocks.)*

**Bridge sentence:** "RAG exists because the window is small — so let's see how designers cap retrieval before history and tools get squeezed out."

---

## 6. RAG Token Budget & build_context_block Demo (12 minutes)

- **IRCTC** analogy — 30 seconds; walk **RAG knob** table (`top_k`, chunk size, delimiters, citation labels).
- Screen-share **session44-04** image — chunks dropped when budget full.
- **Live-code** the **Trim Context Assembly** block from notes:
  - Run with `MAX_CONTEXT_TOKENS = 600`; read `Chunks included`, `Context tokens`, `Full prompt tokens`.
  - Optionally lower to **300** and re-run — narrate which `source_id` rows drop.
- Point at **short source_id** labels and early **break** in the loop.
- **Grounding vs stuffing** — more chunks ≠ better answers.
- **Pair-share (45 seconds):** When window is tight, would you lower `top_k` or shrink chunk size first? One reason each.

> **Break placement:** Take the **5–8 minute break** now (~58–65 min mark) unless the room is more than 10 minutes behind — then break immediately after Block 7's truncation printout.

**Bridge sentence:** "RAG chunks are only one passenger — chat history and agent scratchpads grow every turn, and that's where users feel 'the bot forgot me.'"

---

**Break:** 5–8 minutes. Remind learners: truncation script needs **no API key**; temperature demo needs **`GROQ_API_KEY`** exported.

---

## 7. Memory, Truncation Simulation & Activity 2 (18 minutes)

- **Short-term memory** definition + **phone gallery / email attachment** analogy.
- Walk **Source of growth** table — chat, scratchpad, tool results, RAG + memory together.
- **Silent vs visible truncation** — no error toast vs cut-off mid-sentence.
- Screen-share **session44-05** image — full `chat_history.json` vs tail sent to model.
- **Live-code** the **Simulating Truncation** block — `MAX_MESSAGES = 4`.
  - Read aloud which messages land in **dropped** vs **kept**; highlight the **grounding rule** in dropped.
- Post **Activity 2** table on projector — **12,000-token** budget allocation.
- **Room action:** learners fill token budget rows, then answer the four bullets (dropped rule, what to drop first, design fix, user banner vs silent).
- **Circulate** during Activity 2; cold-call one learner for bullet 4 (banner vs silent failure).
- **Thumbs-up check** before moving on: "Thumbs up when you identified which message held the grounding rule."

**Bridge sentence:** "Truncation is a memory problem — **temperature** is a randomness problem; same product needs both dials set correctly."

---

## 8. Temperature, Determinism & Groq Comparison Demo (12 minutes)

- **Temperature** definition + **cricket style** and **board exam vs rangoli** analogies.
- Walk settings table — `0`, `0.2–0.5`, `0.7–1.0`, above `1.0`.
- Screen-share **session44-06** image — stable `0` vs varied `0.8`, **seed** for QA.
- **Seed** one-liner; **agents** rule: low temp for tool steps, higher only for separate creative mode.
- **Common mistakes:** high temp on policy bot; expecting `temperature=0` to fix bad retrieval.
- **Live-code** **Same Prompt, Two Temperatures** block if keys work; otherwise screen-share **canned output** from a pre-run notebook.
  - Narrate three runs at `0` vs `0.8` — identical vs varied wording.
- **Circulate:** auth errors on missing `GROQ_API_KEY`.

**Bridge sentence:** "You've seen randomness in isolation — now assign temperature and seed **per product feature** and tie it back to a real bug report."

---

## 9. Activity 3 — Temperature, Seed & Feature Design (15 minutes)

- Post Activity 3 **Parts A, B, C** from notes.
- **Part A:** confirm learners noted `temperature=0` stability vs `0.8` variation.
- **Part B — Room action:** complete ShopEasy table — Refund RAG, `lookup_order`, Festive SMS — temp + seed + reason.
- **Circulate** during Part B; spot-check that **policy** rows use **`0`** and **seed yes** for QA.
- **Part C:** two **truncation** causes + one **temperature** cause for *"bot invents revenue after 15 questions"*; one design fix each.
- **Cold-call:** "For Festive SMS, what temperature and would you use a fixed seed?" 
- **Pair-share (1 min):** Partner A defends **per-step** temperature; Partner B defends **one global** dial — one sentence each.

**Bridge sentence:** "Single messages are one sample — agents chain many laps, so tokens and randomness **multiply** every turn."

---

## 10. Agent Loops, Designer Playbook & End-to-End Anatomy (10 minutes)

- Screen-share **session44-07** image — ReAct laps adding tokens.
- Walk **Loop stage** table and **user-visible effects** bullets — forgotten constraints, contradictory answers, tool hallucination.
- **Designer checklist** — four bullets from notes; read quickly, don't lecture each.
- Screen-share **Designer Playbook** table — five yes/no questions and actions.
- **Latency UX** and **error UX** one-liners — friendly "chat too long" message, not raw traceback.
- Screen-share **session44-08** image + ASCII anatomy block (~5,530 tokens); stress **10–15% safety margin**.
- **Cold-call:** "Which two blocks would you cap first in a 20-turn session?" *(scratchpad / history typical answers.)*

**Bridge sentence:** "Let's land the session with five takeaways you can paste into your next design review."

---

## 11. Key Takeaways & Close (6 minutes)

- Read the **five Key Takeaways** bullets from notes — one sentence each; don't re-teach.
- Ask learners to save one **token budget table** template for their next RAG or agent feature.
- **Final check:** "On a scale of 1–5 in chat, how clear are **tokens**, **context window**, and **temperature** now?"
- Assign no new homework unless course calendar specifies; point to **Activity tables** in notes for async completion.
- Thank the room; mention next session topic only if calendar is confirmed on slide.

**Bridge sentence:** *(Session end — no bridge required.)*

---

## Timing Flex — If Running Late

| If you are behind at… | Cut or shorten… | Save at least… |
|---|---|---|
| **Block 4** (Activity 1) | Skip follow-up cost math; collect only **total tokens** | Blocks 7–9 (truncation + temperature) |
| **Block 6** (`build_context_block`) | Instructor runs script once at 600 only; skip 300 re-run | Block 7 truncation live demo |
| **Block 7** (Activity 2) | Give budget table answers on slide; learners only run truncation script | Block 9 Activity 3 Part B |
| **Block 8** (Groq demo) | Use pre-recorded / canned temperature output | Activity 3 Part A live comparison |
| **Block 10** (playbook) | Show **session44-08** image only; skip reading full playbook table | Block 11 close + takeaways |

**Minimum viable session (≈90 minutes):** Blocks 1, 3, 4, 5, 7, 8, 9, 11 — tokens + window + truncation + temperature + one activity each + close.

**If ahead by 10+ minutes:** Let learners redo Activity 1 on their **own** RAG prompt from a prior lab; or extend pair-shares on ShopEasy temperature table.

---

## Facilitator Quick Reference

| Item | Location in notes |
|---|---|
| Diagram 01 — LLM internals overview | Introduction |
| Diagram 02 — Tokens vs words | Tokens vs Words |
| Diagram 03 — Context window budget | Context Limits |
| Diagram 04 — RAG token cap | How Context Limits Constrain RAG |
| Diagram 05 — Memory truncation | Memory and Agent Loops |
| Diagram 06 — Temperature & seed | Temperature section |
| Diagram 07 — Agent token growth | Randomness in Multi-Turn Agent Loops |
| Diagram 08 — End-to-end anatomy | Putting It Together |
| Activity 1 | After tiktoken demo |
| Activity 2 | After truncation simulation |
| Activity 3 | After temperature demo |
| Notebook deps | `tiktoken`; optional `langchain-groq` + `GROQ_API_KEY` |
