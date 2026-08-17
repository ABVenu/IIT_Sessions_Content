# Lecture Script: Agent Communication Patterns

**Session Duration:** 1 Hour 50 Minutes  
**Audience:** Absolute beginners (Indian students, little or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Keep the detailed explanations, definitions, diagrams, and full code in *Lecture Notes.md*; use this script to run the room, share screens, and check that learners are following on their machines.

---

## Break rule

After roughly **55–65 minutes** of session time, take **one** break of **5–8 minutes**. Do **not** treat the break as a numbered teaching block — announce it, pause the recording if applicable, and resume with the bridge into block 6.

---

## Pre-session (before students join)

- Confirm your `.env` has a working `GROQ_API_KEY`.
- Install once: `pip install fastmcp groq python-dotenv openai`.
- Have two folders ready: `planner_executor.py` from the notes, and `masaimato_mcp/` with `server.py` + `ai_mcp_chat.py`.
- Keep *Lecture Notes.md* open on a second screen for diagrams and activity tables.

---

## 1. Opening, recap, and session roadmap (7 minutes)

**Facilitator**

- Welcome the group; confirm everyone can open a terminal or VS Code and a Python file.
- **Cold-call** one or two students: “In the **previous session**, what happened if the food photo and the spoken ingredients did **not** match?” Accept **refusal** — no recipe, no audio.
- Bridge: that app **decided** (cook or refuse). Today agents must also **talk in order** — plan, then execute, then stop.
- Project the four session goals: planner–executor + JSON; sequential script + stop conditions; MCP roles; MasaiMato AI ordering loop with **one** key (`GROQ_API_KEY`).
- Set the lab rule: one Groq key for the main demo; Ollama Cloud is a later swap, not required tonight.

**Students**

- Open a new folder for today’s files; confirm Python runs.

**Engagement**

- **Thumbs up:** “Thumbs up if last session’s recipe app refused at least once on your machine (railway photo or cement audio).”

**Bridge sentence:** “A recipe app decides yes or no — now we need a **checklist** that one worker ticks off, item by item.”

---

## 2. Planner–executor, JSON contracts, and stop conditions (12 minutes)

**Facilitator**

- Define **planner–executor** from the notes: planner writes the ordered plan; executor does **one step at a time**.
- Use the kitchen-ticket analogy: “2 Masala Dosa for Asha” → check menu → place order → share order id.
- **Screen-share** the handoff diagram and the six-row idea table (decomposition, JSON input / ok / error, sequential flow, stop condition).
- Walk one input, one ok output, and one error JSON **aloud** — students should hear the three families.
- Kill the common doubt on the board: **no second planner debating**. Sequential only.

**Students**

- Copy the three JSON shapes into their notes or a comment block.

**Engagement**

- **Cold-call:** “If the executor returns `status: error`, do we still run the next step — yes or no?” Accept **no** — stop as **blocked**.

**Bridge sentence:** “The table is the contract — next we **run** that contract as a short Python script, with no extra agents in the room.”

---

## 3. Sequential planner–executor script (15 minutes)

**Facilitator**

- **Live-code** `planner_executor.py` from the notes (or paste and narrate): `planner` → `executor` → `run`.
- Point at the unused-goal comment: this lab uses a **fixed Asha/Dosa checklist** so beginners see JSON, not NLP parsing.
- Run the happy path: expect step 1 `get_menu` ok, step 2 `place_order` ok, stop **complete**, `MM1001`, total **160**.
- Change `item_name` to `"pizza"`; re-run; show stop **blocked**.
- Run **Name the stop** from the notes — three JSON rows; wait for chat answers before you reveal.

**Students**

- Run the same script; **check screens** — everyone should print a `complete` run once.
- Fill the three-row stop table in chat: complete / blocked / blocked.

**Engagement**

- **Pair-share (90 seconds):** Partner A explains **complete**; Partner B explains **blocked**. Then one pair reports back.

**Bridge sentence:** “That is how steps talk **inside** one task — next we ask how an AI talks to a **restaurant system** without a custom plugin for every app.”

---

## 4. Why MCP — the N × M problem (10 minutes)

**Facilitator**

- Tell the N × M story: WhatsApp bot, hostel chatbot, Cursor agent — each rewriting get-menu and place-order plugins.
- **Screen-share** the two comparison tables and the “messy plugins vs one MCP hub” diagram.
- Define **MCP**: USB-C for AI tools — one server, many clients.
- Answer the REST doubt: a restaurant API can stay; MCP **wraps** it for AI hosts.

**Students**

- Write one line: “Without MCP we rewrite ___; with MCP we write MasaiMato ___.”

**Engagement**

- **Thumbs up:** “Thumbs up if you have used more than one AI app this month (ChatGPT, Cursor, a campus bot) — that is exactly the N × M pain.”

**Bridge sentence:** “A standard needs **roles** — who the student talks to, who holds the cable, and who is the kitchen.”

---

## 5. Host, client, server — API vs MCP (12 minutes)

**Facilitator**

- Walk Host / Client / Server with the hungry-student diagram.
- Contrast **traditional API** (you already know the URL) vs **MCP** (`list_tools` then `call_tool`).
- **Screen-share** the API vs MCP table and the two-line flow in the notes.
- Run **API or MCP?** — three situations; freeze chat 60 seconds; then reveal: Traditional API; MCP; Both.
- Name tools vs resources vs prompts in one breath; tonight is **tools only**.

**Students**

- Type `API`, `MCP`, or `Both` for each row before you reveal.

**Engagement**

- **Cold-call:** “Your browser loads `/api/menu` — is that MCP?” Accept **traditional API**.

**Bridge sentence:** “Roles are clear — after the break we **build the kitchen**: MasaiMato MCP tools, then Groq orders through them.”

---

## 6. Setup and MasaiMato MCP server (16 minutes)

**Facilitator**

- Resume: same sequential idea, now the planner is the **model** and the executor is **MCP `call_tool`**.
- **Screen-share** setup: `pip install`, `.env` with `GROQ_API_KEY` only, folder `masaimato_mcp/` with two files.
- **Live-code** `server.py`: `MENU`, `get_menu`, `place_order` (unknown dish → error; `MM1001` ids).
- Stress: docstrings become tool descriptions the AI will read.
- Quick check aloud: `place_order("Pizza", 1, "Asha")` → `status: error`. Do **not** leave the class sitting on `python server.py` (stdio wait looks like a freeze).

**Students**

- Create the folder and `.env`; paste `server.py`; **check screens** for `GROQ_API_KEY` present (do not ask anyone to paste the key in chat).

**Engagement**

- **Thumbs up:** “Thumbs up when `server.py` is saved next to where `ai_mcp_chat.py` will live.”

**Bridge sentence:** “The kitchen is ready — now the **waiter** (Groq) must **discover** the buttons and press only those.”

---

## 7. Groq orders through MCP (18 minutes)

**Facilitator**

- **Screen-share** the AI-orders diagram: student request → Groq → `call_tool` → MasaiMato JSON → confirmation.
- **Live-code** (or paste in chunks) `ai_mcp_chat.py`: `list_tools` → Groq schemas → `call_tool` → append tool JSON → loop until no `tool_calls`.
- Narrate the stop rule correctly: the `while` loop ends when Groq sends a **final answer**, not when a tool returns `status: error`. Error JSON still goes **back to Groq**.
- Run `python ai_mcp_chat.py` from `masaimato_mcp/`. Point at printed `MCP call_tool` lines, then the final order id and total.
- If a student hits `ModuleNotFoundError: server`, they are in the wrong folder.

**Students**

- Run the same file; **circulate / check screens** for `=== MCP TOOLS ===` then a real `MM` order id.

**Engagement**

- **Cold-call:** “Did the model invent the price, or did `get_menu` return it?” Accept **tool result**.

**Bridge sentence:** “A happy path is not enough — we trace one order, then we **break** it with pizza.”

---

## 8. Trace the order, error path, and the full story (10 minutes)

**Facilitator**

- Run **Trace One Order** from the notes: `get_menu`? `place_order`? order id? invented dish?
- Change the prompt to `"Order Pizza for Asha"`; show error JSON, then Groq’s grounded refusal.
- Optional second prompt: Filter Coffee for Rohan — only if most machines already succeeded once.
- Mention Ollama Cloud in **one minute**: same MCP loop, swap only the LLM client and `OLLAMA_API_KEY` — skip live run unless you are ahead.
- Close the four-line story: inside the task (plan → execute → stop); outside (MCP); build MasaiMato once; Groq orders through tools, not imagination.

**Students**

- Fill the four-row trace table; run the pizza prompt if time.

**Engagement**

- **Pair-share (1 minute):** “What stopped the pizza order — the model’s opinion, or MasaiMato’s JSON?” Accept the **JSON error**.

**Bridge sentence:** “You now have two talking styles — **JSON handoffs inside a plan**, and **MCP tools outside the app**.”

---

## 9. Recap and session close (5 minutes)

**Facilitator**

- Rapid takeaways: sequential planner–executor; JSON ok/error; stop complete vs blocked; MCP host/client/server; MasaiMato `get_menu` + `place_order`; Groq must call tools.
- Point to the **Important Commands, Libraries, Terminologies** table for revision.
- Preview lightly: **upcoming** sessions use workflow graphs for *when* steps run; MCP-style tools remain *how* outside systems are reached.
- Remind: never commit `.env`.

**Students**

- Exit ticket in chat: “One JSON field I will never skip is ___.”

**Engagement**

- **Thumbs up:** “Thumbs up if you can tell a friend why the AI must not invent an order id.”

**Bridge sentence:** “Close with this habit — **plan, execute, stop on JSON** — then let the model press only the tools you published.”

---

## Timing flex — if you are running late

- **Cut first:** Drop the Ollama mention entirely; shorten pair-shares to 30 seconds; show the MCP hub diagram without a long N × M story; skip the Filter Coffee second prompt.
- **Cut second:** In block 3, run the happy path only and **tell** the pizza stop instead of re-coding it; in block 7, paste `ai_mcp_chat.py` rather than typing it; run the demo once on the instructor machine and have students watch the `MCP call_tool` log.
- **Never skip:** Block 2 (JSON input / ok / error + sequential stop rule), block 3 (`planner_executor.py` at least one complete run), block 5 (host / client / server + API vs MCP activity), and block 7 (Groq **discovers** tools and places one real MasaiMato order).
- **If ahead of schedule:** Live-swap the Groq client snippet to Ollama Cloud for one extra order, or let students change quantity / customer name and confirm a new `MM` id.
