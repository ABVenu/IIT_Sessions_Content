# Lecture Script: Hands-on Workshop: AutoGen — Hotel Guest Complaint Intake Desk

**Session Duration:** 1 hour 50 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, hospitality-themed, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style. Lean on `Lecture Notes.md` for definitions, code, and diagrams.

**Break rule:** After **60–70 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

**Prerequisite framing:** If students completed prior Module 4 AutoGen sessions (conversable agents, tools, GroupChat), say today is a **full product assembly** lab — same building blocks, one end-to-end hotel desk. If not, treat AssistantAgent / UserProxyAgent / GroupChat as a fast refresher while building.

---

## 1. Welcome, AutoGen Recap, and Today's Build (7 minutes)

- Welcome the group; frame today as **Hands-on AutoGen** — specialist team, registered tools, group orchestration, controlled close.
- Recap prior habits in one breath: conversable agents → tool registration → termination → GroupChat + manager + speaker selection + max rounds.
- Screen-share the "What you will build" bullet list from Lecture Notes.
- **Engagement — cold-call:** "Which agent *runs* the Python tool functions in this desk?" (UserProxyAgent / FrontDeskRunner — not the clerk.)
- **Room action:** Confirm `GROQ_API_KEY` is set; students open a fresh notebook or `hotel_complaint_desk.py`.

**Bridge sentence:** "Blocks are familiar — let's see why a front desk needs a visible specialist team, not another chat thread."

---

## 2. The Real Problem — Hotel Guest Complaints (6 minutes)

- Narrate midnight AC failures, missed housekeeping, wrong spa charges — WhatsApp and reception notes bury the trail.
- Screen-share the **chaotic chat vs hotel desk** image from Lecture Notes.
- Walk the guest-message table: clear AC complaint → classify + lookup + ticket; vague stay → intake clarifies; billing → billing path.
- Use the hospital triage analogy: understand, assign ward, check file, issue token.
- Mention the pattern also ports to e-commerce and HR — hotel keeps roles concrete today.
- **Engagement — thumbs up:** "Has anyone ever had to chase a hotel issue through multiple people?"

**Bridge sentence:** "Product story is clear — draw the team map before we install packages."

---

## 3. Design First — Team, Tools, and Stop Rules (10 minutes)

- Screen-share the ASCII hand-off ladder: Intake → Classify → Desk Clerk + tools → TERMINATE.
- Define terms in plain language (official + simple + example for each):
  - **AssistantAgent** — expert at one desk
  - **UserProxyAgent** — office runner who presses approved buttons
  - **register_function** — access card for one tool only
  - **GroupChat / GroupChatManager** — meeting room + chairperson
  - **Speaker selection / max rounds** — chair calls next speaker / meeting alarm
- Walk **categories**: `room_comfort`, `housekeeping`, `billing`, `dining`, `unclear`.
- Walk the two tools table: `lookup_guest_stay`, `create_complaint_ticket`.
- Screen-share the **specialist team roundtable** diagram.
- **Pair-share (2 min):** "Why must the classifier *not* create tickets?" One volunteer explains role boundaries.

**Bridge sentence:** "Team map is drawn — predict one hand-off before setup."

---

## 4. Activity — Predict the Hand-off (5 minutes)

- **Room action:** Students write for: `"Towels not replaced in room 208, booking BK-3301"`.
  - Expected category, agent after classify, first tool.
- Give **90 seconds** silent work; reveal: `housekeeping` → DeskClerk → `lookup_guest_stay`.
- **Cold-call:** "Why lookup before create?" (Need verified room/guest from booking, not guesswork.)
- **Engagement — thumbs up:** "Does your prediction match?"

**Bridge sentence:** "Hand-off predicted — bootstrap the environment and fake hotel system."

---

## 5. Environment Setup, LLM Config, and Fake Hotel Tools (8 minutes)

- **Live-coding / screen-share:** Run setup from Lecture Notes:

```bash
pip install ag2[openai]
export GROQ_API_KEY="your_groq_api_key"
```

- Paste imports, `llm_config` (Groq + `temperature: 0`), and **`HOTEL_STAYS`** dict.
- Paste **`lookup_guest_stay`** and **`create_complaint_ticket`**; run one manual lookup in a cell to prove the fake system works.
- Paste **`is_done`** termination helper — explain `TERMINATE` and `TICKET_CREATED:` markers.
- **Room action:** Circulate — confirm API key loads and `BK-7781` returns Asha Verma / room 412.
- If someone is behind: share starter file via chat; they catch up during agent building.

**Bridge sentence:** "Hotel system and stop rule are ready — register the three specialists."

---

## 6. Live Build — Specialist Agents and Tool Registration (18 minutes)

- **Live-coding — Agent 1:** `IntakeAgent` system message — clarify missing booking/room; no classify, no tools, no invent data.
- **Live-coding — Agent 2:** `ClassifierAgent` — exactly one `CATEGORY=` label; no tools.
- **Live-coding — Agent 3:** `DeskClerkAgent` — lookup then create ticket then guest confirmation ending in TERMINATE.
- **Live-coding — Executor:** `UserProxyAgent` as `FrontDeskRunner` — `human_input_mode="NEVER"`, `is_termination_msg=is_done`.
- **Live-coding — register_function** twice: clerk = caller, runner = executor; read descriptions aloud.
- **Engagement — cold-call:** "Can IntakeAgent call `create_complaint_ticket`?" (No — not registered as caller.)
- **Room action:** Walk two rows; verify each `register_function` has distinct caller and same executor.

**Bridge sentence:** "Roles and tools are wired — seat the team in a group room with chair rules."

---

## 7. GroupChat, Speaker Selection, and Manager (12 minutes)

- **Live-coding:** Paste **`select_hotel_speaker`** — narrate the ladder and the tool-call branch returning `user_proxy`.
- **Live-coding:** Build **`GroupChat`** with all four agents, `max_round=12`, custom speaker method.
- **Live-coding:** Build **`GroupChatManager`** with same `is_termination_msg`.
- Paste **`print_trace`** helper for readable audit output.
- **Engagement — pair-share (2 min):** "What happens if last message has `tool_calls`?" (Runner must speak next.)
- **Cold-call:** "Why reset `groupchat.messages = []` between demos?" (Fresh transcript per case.)

**Bridge sentence:** "Chair is seated — run the happy-path complaint and read the trace like an audit file."

---

## 8. Demo 1 — Happy Path and Conversation Trace (12 minutes)

- **Live-coding:** Run AC complaint (`BK-7781`); call `print_trace(chat_1)`.
- Narrate turn-by-turn: Intake summary → Classifier `CATEGORY=room_comfort` → Clerk tool suggestions → Runner executes → confirmation + TERMINATE.
- **Activity — Trace Detective (3 min):** Students write: *Tool use was visible / not visible because…*
- **Engagement — cold-call:** "Which line proves the ticket was created?" (`TICKET_CREATED:` in trace or final message.)
- **Room action:** Circulate — students highlight tool-call turns in their trace printout.

**Bridge sentence:** "Happy path works — stress vague and billing complaints next."

---

## 9. Demo 2 and Demo 3 — Vague Complaint and Billing Path (12 minutes)

- **Live-coding:** Reset `groupchat.messages = []`; run vague `"Something is wrong with my stay"` — expect intake clarification, not immediate ticket.
- Reset again; run billing complaint (`BK-9002`, spa charge) — expect `billing` category and ticket confirmation.
- **Activity (4 min):** Students run both demos; compare trace length and whether tools ran.
- **Engagement — thumbs up:** "Did Demo 2 avoid creating a ticket without a booking id?"
- **Cold-call:** "Which demo shows the classifier choosing `billing`?"

**Bridge sentence:** "Three paths seen — now break the system on purpose and fix one failure mode."

---

## 10. Trace Audit, Failure Modes, and Break-Then-Fix Activity (12 minutes)

- Screen-share the **four trace audit questions** from Lecture Notes.
- Walk the failure-mode table: wrong speaker, repetition deadlock, tool not executed, invented booking.
- Screen-share **wrong speaker vs controlled close** diagram.
- **Activity — Break Then Fix (5 min):** Set `max_round=3`, re-run Demo 1, note what failed; restore `max_round=12` and confirm recovery.
- **Engagement — cold-call:** "Chat stopped on round limit only — which knob failed?" (`max_round` too low or missing TERMINATE.)
- Students tick rows 1–4 on the **AutoGen Reliability Checklist**.

**Bridge sentence:** "Orchestration is debuggable — same shape ports to other industries with new labels."

---

## 11. Industry Port, Practice, and Wrap-Up (8 minutes)

- Screen-share **Same Pattern, Other Industries** table (hotel vs e-commerce vs HR).
- **Activity — Rename the Desks (2 min, paper only):** Three specialist names for an e-commerce order desk.
- **Activity — Role Boundary Check:** Rapid fill of the four-agent table (classify? tools? invent data?).
- Rapid-fire **Key Takeaways**: specialist boundaries, register_function caller/executor, GroupChat + speaker + max rounds, trace as proof.
- **Common mistakes** aloud: every agent calling every tool; `human_input_mode="ALWAYS"` without plan; forgetting transcript reset; tool calls not routed to executor.
- **Exit ticket:** "Name one thing the trace showed that the final paragraph alone would hide."
- Point to terminology table in Lecture Notes for revision.

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 8–10 min late | Shorten Block 2; skip pair-share in Block 3 |
| 12–15 min late | Paste full code from Lecture Notes via chat; instructor demos Block 8 while students scroll |
| 18+ min late | Skip Block 4 Predict-the-Hand-off; give answers verbally |
| 20+ min late | Run Demo 1 only; describe Demo 2/3 outcomes from Lecture Notes |
| 25+ min late | Skip Break-Then-Fix; describe `max_round=3` failure verbally |

| If you are **ahead** | Add |
|----------------------|-----|
| 5–8 min spare | Students complete **Execution Walkthrough** table for AC complaint (`BK-7781`) |
| 10–15 min spare | **Run Your Own Complaint** — custom one-liner using a `HOTEL_STAYS` booking id |
| 15+ min spare | Students finish full **AutoGen Reliability Checklist** (all 7 rows) and peer-check |

**Hard stop at 1 hour 50 minutes:** Everyone has registered two tools, run at least one full group chat to ticket confirmation, and printed or read a numbered conversation trace.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 7 min | Introduction | Recap; build list |
| 2 | 6 min | The Real Problem | Image; guest → path table |
| 3 | 10 min | Design First | ASCII ladder; tools; categories |
| 4 | 5 min | Activity — Predict the Hand-off | Towels / BK-3301 prediction |
| 5 | 8 min | Setup + tools | `pip install`; `HOTEL_STAYS`; tool fns |
| 6 | 18 min | Build agents + register_function | Three AssistantAgents; UserProxy |
| 7 | 12 min | GroupChat + speaker + manager | `select_hotel_speaker`; `print_trace` |
| 8 | 12 min | Demo 1 — Happy path | AC complaint; Trace Detective |
| 9 | 12 min | Demo 2 & 3 | Vague + billing paths |
| 10 | 12 min | Read trace + failure modes | Break Then Fix; failure table |
| 11 | 8 min | Same pattern + practice + takeaways | Rename desks; exit ticket |

**Break placement:** After Block 7 or early Block 8 (~60–70 min cumulative).
