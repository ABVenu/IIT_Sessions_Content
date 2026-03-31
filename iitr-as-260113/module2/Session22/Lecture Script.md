# Lecture Script: Short-Term vs Long-Term Memory in Agentic Systems

**Session duration:** 2 hours 15 minutes  
**Audience:** As per cohort; session is primarily theoretical, with one short implementation walk-through in the notes.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—exact definitions, figures, and analogies live in `Lecture Notes.md` (project those as slides or share the doc).

**Break (only pause in this plan):** After roughly **65–80 minutes** of session clock time, take **one** pause of **5–8 minutes**, then continue with the next teaching segment. Every numbered section below is **teaching or activity**—there are **no** separate “break” sections in the list.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm access to materials and any platform used for the cohort.
- State outcomes aligned with the session objective: **memory types**, **how conversation history maps to short-term (context) memory**, **limits of context-only designs**, **buffer / window / summary strategies**, **long-term types (episodic, semantic, procedural)**, a **compact Python illustration** of the three short-term patterns, and **how agents choose what to remember** plus a **storage-awareness** bridge to later topics (RAG, vector DBs).
- Preview rhythm: concepts and discussion first, then a focused walk-through of the small Python classes, then design and “what to remember,” then closing synthesis.

---

## 2. Role of memory in agent behavior (11 minutes)

- Project **Section 1** of the notes (memory definition—simple and detailed); use the **name example** (“My name is Ravi” → “What is my name?”).
- Contrast **stateless** vs **stateful** in one sentence each; emphasize that memory is what makes an agent stateful.
- Optional: 1 minute—ask for one real service learners use that *feels* stateful vs one that resets every turn.
- Use the **conversation analogy** slide if available; do not read paragraphs line by line.

---

## 3. Short-term vs long-term memory (11 minutes)

- Cover **Section 2**: short-term as **working / session** memory; long-term as **persistent** memory.
- **Whiteboard vs diary** (or notes) analogies—quick; let the figure carry the comparison.
- Stress the distinction: short-term = consistency **within** a conversation; long-term = improvement **across** conversations.

---

## 4. Conversation history, context window, and tokens (14 minutes)

- **Section 3**: conversation history as structured message sequence; **context window** as “how much the model sees at once.”
- **ChatGPT-style example**: short chat vs very long chat—slowdown, quality, “start new chat”—link explicitly to **context filling up**.
- **Tokens**: smallest units; show or quote the example sentence split into tokens; one line on billing/limits if the cohort is practitioner-oriented.
- Key idea (quote or paraphrase once): the model does not “remember” like humans—it is **shown past conversation again** each turn.

---

## 5. Limitations of context-window-based memory (13 minutes)

- **Section 4**: **token limit** (input + output cap), **cost** (more history → more tokens → API/production cost), **performance** (noise, focus, latency).
- Use the **company chatbot** cost sketch from the notes briefly; reinforce that memory design affects **cost, scale, and performance**.
- **Analogy**: “20 pages of notes then one question”—don’t extend into new topics; 2–3 clarifying questions only.

---

## 6. Designing short-term memory strategies (13 minutes)

- **Section 5** with the strategy figure: **conversation buffer** (full history), **sliding window** (last *N* messages; mention `history[-3:]` idea), **summary memory** (compress older turns).
- For each: one line **when it works** and one line **trade-off** (completeness vs efficiency vs relevance).
- Optional 2 minutes: pairs—**which strategy** for a 200-message support thread vs a 5-turn FAQ bot?

---

## 7. Long-term memory and its types (11 minutes)

- **Section 6**: why long-term matters (users, personalization, learning over time).
- **Episodic** (events/interactions), **semantic** (facts/knowledge), **procedural** (how-to/workflows)—definitions simple → detailed only if time; use examples from the notes (Python preference, ticket workflow, etc.).
- One pass over the **three types** figure; avoid duplicating textbook depth—this session sets vocabulary for later architecture sessions.

---

## 8. Implementing memory strategies in Python—walk-through (18 minutes)

- **Section 7**: frame as *illustration of behavior*, not a production framework lesson.

- Walk the three classes **in order**: `BufferMemory`, `WindowMemory` (emphasize `size` and `[-self.size:]`), `SummaryMemory` (`summary`, `recent`, `summarize()` placeholder).
- Live or **follow-along**: the shared loop over sample `conversation`, then `print` outputs; compare to the **comparison table** (storage style, advantage, limitation).
- **Important note** from notes: in-memory demo vs **databases / vector stores** in production—one sentence to set up Section 10.

---

## 9. How agents decide what to remember (11 minutes)

- **Section 8** in the notes: agents **cannot** remember everything—technical, cost, and “cognitive” (clarity) constraints.
- **Relevance** vs **recency**; walk through the three cases (old-but-important, recent-but-unimportant, recent-and-important).
- Close with **selective retention**—good design is not “store everything.”

---

## 10. Choosing short-term vs long-term; storage awareness; forward connection (12 minutes)

- **Choosing between STM and LTM**: when conversation-local turns suffice vs when persistence is needed; use **loops explanation** vs **platform remembering struggle with loops**.
- **Customer support** and **personal assistant** split (STM: current issue/task; LTM: history, preferences)—stress **combination**, not either/or.
- **Design questions** from notes: temporary vs permanent, reuse, cost vs benefit.
- **Storage awareness**: STM in context; LTM outside the model (DBs, storage). Tease **RAG, vector DBs, scalable agents** as next-step foundations—do not teach RAG here.
- Optional: **Key takeaway** bullets from the notes (trade-offs: completeness, efficiency, scalability) on screen for 60 seconds.

---

## 11. Closing (6 minutes)

- Recap the **headline decisions**: what to put in context vs what to persist; which short-term **pattern** fits constraints.
- One prompt: *What would you store in long-term memory for your domain vs leave in the window only?*
- Thank-you; pointer to **Preread**, assignments, or **next session** as per program ops.

---

### Timing flex

- If running long before the break: trim **Section 8 (Python)** to **instructor demo only** (no follow-along) or shorten **Section 4 (tokens)** to definitions + ChatGPT example only.
- If running short after the break: add **5 minutes Q&A** on **buffer vs window vs summary**, or extend **Section 10** with one more domain example from the room.
- If the cohort is **non-coders**: cap **Section 8** at **10 minutes** (behavior + table only; share code as optional reading).
