# Lecture Script: Hands-on Session: LangGraph — Hostel Maintenance Ticket Desk

**Session Duration:** 60 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, campus-themed, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style. Lean on `Lecture Notes.md` for definitions, code, and diagrams.

**Break rule:** After **35–40 minutes** of instruction, take **one** optional pause of **3–5 minutes** (not a numbered block). Skip the break if you are already behind — this session is compact.

**Prerequisite framing:** If students completed prior LangGraph theory sessions (nodes, edges, state, checkpoints), say today is a **first full desk build** — same ideas, one end-to-end hostel product. If not, treat checkpoint / retry / conditional routing as a fast refresher while coding.

---

## 1. Welcome, LangGraph Recap, and Today's Build (5 minutes)

- Welcome the group; frame today as **Hands-on LangGraph 01** — parse, classify, branch, checkpoint, harden a flaky API.
- Recap prior habits in one breath: nodes → edges → shared state → checkpoints → timeout + retries.
- Screen-share the "What you will build" bullet list from Lecture Notes.
- **Engagement — cold-call:** "How many branches after classify in this desk?" (Two — create ticket or ask clarification.)
- **Room action:** Confirm Python env is active; students open a fresh notebook or `hostel_ticket_desk.py`.

**Bridge sentence:** "Blocks are familiar — let's see why a ticket desk beats another hostel group chat."

---

## 2. The Real Problem — Hostel Maintenance Desk (4 minutes)

- Narrate fans, taps, WiFi — chat complaints get buried.
- Screen-share the **chaotic chat vs ticket desk** image from Lecture Notes.
- Walk the three-row table: fan → electrical ticket; vague → clarification; API down → retry then calm error.
- Use the hospital OPD token analogy.
- **Engagement — thumbs up:** "Has anyone reported a hostel issue in a group chat and lost track?"

**Bridge sentence:** "Problem is clear — draw the map before we install packages."

---

## 3. Design First — Map, State, and Rules (6 minutes)

- Screen-share the ASCII flow: `START → parse → classify → two roads → END`.
- Define **Checkpoint**, **Timeout**, **RetryPolicy** in plain language (official + simple + one example each).
- Walk **minimal shared state** fields and the **category keyword** table.
- Screen-share the **category desks** diagram.
- **Pair-share (1 min):** "Which desk handles a leaking tap?" One volunteer: `plumbing`.

**Bridge sentence:** "Map is drawn — predict one path before setup."

---

## 4. Activity — Predict the Path (4 minutes)

- **Room action:** Students write for: `"WiFi keeps dropping in Block C"`.
  - Expected `category`, next node after classify, does `ask_clarification` run?
- Give **60 seconds** silent work; reveal: `wifi` → `create_ticket` → No.
- **Cold-call:** "What keyword triggered `wifi`?"

**Bridge sentence:** "Prediction checked — bootstrap the environment."

---

## 5. Environment Setup and TicketState Overview (5 minutes)

- **Live-coding / screen-share:**

```bash
pip install langgraph langgraph-checkpoint-sqlite
```

- Paste imports, **`TicketState` TypedDict**, and helpers: `run_with_timeout`, `ATTEMPT_BOX`, `fresh_state`.
- **Room action:** Circulate — confirm everyone has `TicketState` with all seven fields.
- If someone is behind: share starter cell via chat; they catch up during the build block.

**Bridge sentence:** "Notebook defined — register stations and wire the branch."

---

## 6. Live Build — Nodes, Branch, and Graph Assembly (12 minutes)

- **Live-coding:** `parse_complaint` → `classify_category` → `route_after_classify` (two-way branch).
- **Live-coding:** `ask_clarification`, `create_ticket` with `run_with_timeout` + **`RetryPolicy`**, `write_confirmation`.
- **Live-coding:** Wire graph — `add_conditional_edges` with two keys; compile `plain_graph`.
- **Engagement — cold-call:** "Where does the router send `unknown`?" (`ask_clarification`.)
- **Room action:** Walk one row; verify conditional edge dict keys match router return values.

**Bridge sentence:** "Desk compiled — run success and blocked paths and read the trace."

---

## 7. Demo 1 — Path Proof: Success vs Clarification (6 minutes)

- **Live-coding:** Reset `ATTEMPT_BOX`; invoke fan complaint; print `trace`, `result`, `ATTEMPTS`.
- Invoke vague complaint; print blocked trace ending at `ask_clarification`.
- **Activity (2 min):** Students run both; circle the node where paths diverge.
- **Engagement — thumbs up:** "Two different traces?"

**Bridge sentence:** "Paths proven — pause the case before ticket creation."

---

## 8. Demo 2 — Checkpoint Pause, Inspect, and Resume (8 minutes)

- **Live-coding:** `SqliteSaver.from_conn_string("hostel_tickets.db")`; compile with `interrupt_before=["create_ticket"]`.
- Invoke plumbing leak with `thread_id: "hostel-case-204"`; show partial trace.
- **Live-coding:** `get_state(config)` — print saved `category`, `next` (expect `create_ticket` pending).
- **`invoke(None, config)`** on same thread — print resumed trace and ticket confirmation.
- **Activity — Checkpoint Detective (2 min):** One sentence: *This case is ready / not ready to create a ticket because…*
- **Cold-call:** "What breaks if you change `thread_id` on resume?"

**Bridge sentence:** "Save and resume works — stress the API until retries run out."

---

## 9. Demo 3 — Exhausted Retries and Calm User-Facing Error (6 minutes)

- **Live-coding:** Build `down_builder` with `always_down_api`; wrap `invoke` in `try/except`.
- Print **user-facing error** from Lecture Notes — not raw stack trace.
- Screen-share the **retry vs calm error** diagram briefly.
- Students tick rows 1–3 on the **Reliability Checklist**.

**Bridge sentence:** "Reliability wired — lock takeaways and one practice move."

---

## 10. Practice, Takeaways, and Wrap-Up (4 minutes)

- **Activity — Run Your Own Complaint (1 min):** One custom one-liner; note `category` and `trace`.
- Rapid-fire **Key Takeaways** from Lecture Notes: nodes + branch, checkpoint + thread ID, timeout + RetryPolicy, trace as proof.
- **Common mistakes** aloud: wrong thread on resume; showing raw `ConnectionError`.
- **Exit ticket:** "Name one thing `trace` shows that the final message alone hides."
- Point to terminology table in Lecture Notes; preview Session 02 lost & found desk (three-way branch + pause before release).

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 5 min late | Shorten Block 2; skip pair-share in Block 3 |
| 8 min late | Paste full code via chat; instructor demos Block 7 only |
| 12 min late | Skip Block 4 Predict-the-Path; give answers verbally |
| 15 min late | Instructor runs Demo 2 only; describe Demo 3 failure verbally |
| 18+ min late | Skip optional break; students read practice activities as homework |

| If you are **ahead** | Add |
|----------------------|-----|
| 3–5 min spare | Students complete **Execution Walkthrough** table for fan vs vague complaints |
| 8+ min spare | Finish full **Reliability Checklist** (all 6 rows) and peer-check |

**Hard stop at 60 minutes:** Everyone has compiled the graph, seen two distinct traces (success / blocked), and witnessed one checkpoint pause + resume on the same `thread_id`.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 5 min | Introduction | Recap; build list |
| 2 | 4 min | The Real Problem | Image; message → path table |
| 3 | 6 min | Design First | ASCII map; state; category table |
| 4 | 4 min | Activity — Predict the Path | WiFi prediction |
| 5 | 5 min | Setup + TicketState | `pip install`; TypedDict |
| 6 | 12 min | Build the Full Desk | All nodes; conditional edges |
| 7 | 6 min | Demo 1 — Path proof | Fan + vague invokes |
| 8 | 8 min | Demo 2 — Checkpoint | `SqliteSaver`; resume |
| 9 | 6 min | Demo 3 — Retries / calm error | `down_builder`; try/except |
| 10 | 4 min | Practice + Takeaways | Own complaint; exit ticket |

**Break placement (optional):** After Block 7 (~42 min cumulative).
