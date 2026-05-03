# Lecture Script: Short-Term vs Long-Term Memory in AI Agents

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners (Indian students, limited prior tech background)

---

**Break rule:** After roughly 60–75 minutes of instruction, take **one** break of 5–8 minutes. Do **not** treat the break as a numbered teaching block; resume with the next numbered segment when students return.

**How to use this file:** This document is for **timing and facilitation only**. It is not a substitute for Lecture Notes — use it to manage pace, room checks, activities, and transitions. Keep Lecture Notes open for definitions, diagrams, and exact tables.

---

## 1. Welcome & Why Memory Still Matters (10 minutes)

- Quick housekeeping: screen share on, chat for questions, plan for one mid-session break.
- Bridge from Session 12 in one line: last time = *state* and the library metaphor; today = *how* the shelf is organised.
- **Cold-call (2–3 students):** “Name one thing that gets worse if an agent has **no** memory.” Rotate corners of the room so everyone expects a turn over the hour.
- Screen-share the session objectives list from Lecture Notes (bullets under “In this session, you will”) — read aloud briefly; ask for **thumbs up** in gallery or chat if the list makes sense.
- Revisit the three bullets: continuity, personalisation, better decisions — pause for nods.

**Bridge sentence:** “If that is *why* memory matters, the next question is what *kind* — short versus long — because your brain does not treat a phone number and your mother’s face the same way.”

---

## 2. Short-Term vs Long-Term — Definitions, Table, First Image (12 minutes)

- Present STM: session-only, notepad / customer-care analogy; LTM: persistent, doctor’s file analogy.
- Show the **comparison table** (duration, storage, speed, capacity, risk, use case) — give students 30 seconds to skim, then **pair-share** (2 min): “Which row surprises you?”
- Display `session13-stm-vs-ltm.png`; circulate and glance at a few student screens to confirm the image loaded.

**Bridge sentence:** “Before we wire this into bots, check whether you can sort real life — short, long, or both.”

---

## 3. Student Activity 1 — “Short-Term or Long-Term?” (8 minutes)

- **Format:** Individual reflection → 3–4 volunteers share (Zoom spotlight or mic).
- Read Situation A (shopping assistant, “I prefer blue”) and Situation B (fitness app after three months). **Cold-call** for one sentence of reasoning each; fill briefly on chat if shy.
- Debrief: A = STM (same thread); B = LTM (across sessions) — acknowledge “both” nuance only if someone raises it.

**Bridge sentence:** “Good — now we pull back the curtain: in software, ‘remembering’ in-session usually means something very concrete — the context window.”

---

## 4. Conversation History as Working Memory (12 minutes)

- Define **context window** and **tokens** in plain language; use the “desk space” / “10 open books” analogy from notes.
- Show `session13-context-window-desk.png`.
- Walk through the sample transcript (Priya / name) — optionally **live-annotate** in a doc or slide so they see System + User + Assistant stacking.
- **Check:** “Thumbs up if it is clear that the model does not have a magical memory chip — it gets the history inside the prompt.”

**Bridge sentence:** “If everything lives on that desk, you can already guess where long chats hurt us — limits, money, and model behaviour.”

---

## 5. Limitations of Raw History (10 minutes)

- Three limitations: token ceiling (whiteboard eraser), cost per token, performance when context is huge.
- Show `session13-context-limitations.png`.
- **Quick poll** (chat or hand raise): “Which limitation worries you most for a real product — **cost**, **forgetting old turns**, or **slow / sloppy answers**?” Tabulate verbally.

**Bridge sentence:** “That pain is why nobody ships ‘dump entire chat forever’ — we use three short-term strategies instead.”

---

## 6. Short-Term Strategies — Buffer, Window, Summary (20 minutes)

- **Buffer:** full transcript every time — when it shines (short, precise chats) vs when it breaks (long, expensive).
- **Window:** last *N* messages — conveyor belt; mention “pinned” system/profile as a fix for lost early context.
- **Summary:** compress old turns — journalist’s notebook; extra LLM call, may lose verbatim detail.
- Show comparison table (strategy / kept / best for / risk) and `session13-buffer-window-summary.png`.
- Keep energy: **circulate** briefly while they read the table; spot-check two screens.

**Bridge sentence:** “Definitions are easy — choosing under pressure is harder; you will pick strategies for three real jobs next.”

---

## 7. Student Activity 2 — Pick Buffer, Window, or Summary (10 minutes)

- **Format:** Individual think → reveal rows one at a time (legal clause-by-clause → **Buffer**; food-delivery 3–4 turns → **Window**; career coach 60+ messages → **Summary** — accept close variants if argued well).
- After each row, **cold-call** a different student for a one-line “why.”

**Bridge sentence:** “Everything so far dies when the tab closes — unless we deliberately persist; that is long-term memory.”

---

## 8. Long-Term Memory — Episodic, Semantic, Procedural (15 minutes)

- LTM = external storage (file, DB, vector store); bridge from limitation “session ends.”
- **Episodic:** diary / “last Tuesday Ravi in Pune”; retrieval (logs, vectors).
- **Semantic:** encyclopedia / facts; knowledge bases, semantic search.
- **Procedural:** SOP / escalation steps; system prompt vs workflow stores.
- Show the three-type comparison table and `session13-ltm-three-types.png`.

**Bridge sentence:** “Same assistant can use all three buckets; practice sorting what goes where.”

---

## 9. Student Activity 3 — Medical Assistant LTM Types (8 minutes)

- **Format:** Individual think → row-by-row reveal (patient profile → **episodic**; metformin fact → **semantic**; chest-pain triage steps → **procedural**).
- Invite one volunteer per row; affirm that real agents mix all three.

**Bridge sentence:** “Storage is easy to say — *what* to save is the design fight: recency versus relevance.”

---

## 10. How Agents Decide What to Remember (8 minutes)

- Recency vs relevance — simple example: health condition mentioned 50 messages ago.
- Skim the four approaches: rule-based flagging, LLM extraction, user-controlled, implicit learning — no deep dive; **pair-share** (90 sec): “Which approach would you trust for a banking bot?”

**Bridge sentence:** “Theory becomes code when the list you pass to the model changes — I’ll show three patterns.”

---

## 11. Pseudo-Code Walkthrough — Buffer, Window, Summary (12 minutes)

- **Screen-share** the three Python blocks from Lecture Notes (or your own IDE with identical logic).
- **Buffer:** walk `append` → full `call_llm(messages=conversation_history)` — emphasise simplicity and cost growth.
- **Window:** `WINDOW_SIZE`, `full_history[-WINDOW_SIZE:]` — “what the model sees” vs what you might still log.
- **Summary:** `running_summary`, `SUMMARISE_AFTER`, merge step — note extra summarisation call.
- **Check:** “Show **thumbs up** if slicing `[-N:]` makes sense; **thumbs sideways** if you want a quick repeat.”

**Bridge sentence:** “In-session lists are one thing; anything that must survive weeks lives outside the process — files, DBs, vectors.”

---

## 12. Storage Awareness & Close (10 minutes)

- Three tiers: in-memory (session only), file/JSON (simple persistence), database/vector (scale, semantic retrieval).
- Show storage comparison table and `session13-storage-tiers.png`; tease deeper sessions on vector DBs.
- Rapid **key takeaways** from Lecture Notes (five bullets); optionally flash the terminology table — assign **1 minute silent read** then one **cold-call**: “Which term will you Google tonight?”
- Homework / next session hook: external storage and retrieval at scale.

**Bridge sentence:** “We end where engineering starts — picking memory types and stores on purpose, not by accident.”

---

## Timing flex (if running late)

- **Cut 3–5 min:** Trim pair-shares in Blocks 2, 10, and 12; keep one cold-call per activity instead of many volunteers.
- **Cut 5–8 min:** Shorten pseudo-code Block 11 to Buffer + Window only; assign Summary as async reading with Lecture Notes.
- **Cut 5–7 min:** Merge limitations (Block 5) into Block 4 as a single “three bullets, no poll.”
- **If ahead:** Extend Activity 2 or 3 with a fourth row you invent, or add a **live mini-demo** of list slicing in a REPL (2–3 min).
- **Never skip** the break if the cohort is tired — shorten Block 6 or 11 instead so attention stays sharp after resume.
