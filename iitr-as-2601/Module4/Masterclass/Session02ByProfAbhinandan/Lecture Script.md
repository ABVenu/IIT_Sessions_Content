# Lecture Script: Hands-on Workshop: LangGraph 02 — Campus Lost & Found Claim Desk

**Session Duration:** 1 hour 50 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, campus-themed, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style. Lean on `Lecture Notes.md` for definitions, code, and diagrams.

**Break rule:** After **60–70 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

**Prerequisite framing:** If students completed Masterclass 01 (Hostel Maintenance Ticket Desk), say today is a **domain port + one extra branch** lab — same LangGraph habits, new campus product. If not, treat checkpoint / retry / conditional routing as a fast refresher while building the lost & found desk.

---

## 1. Welcome, Bridge from Session 01, and Today's Build (8 minutes)

- Welcome the group; frame today as **LangGraph Masterclass 02** — same reliability toolkit, **new product** (Campus Lost & Found Claim Desk).
- Recap Session 01 in one breath: classify → branch → checkpoint → timeout + retries on a flaky API.
- Screen-share the "What you will build" bullet list from Lecture Notes: three-way branch, pause before release, calm failure message.
- **Engagement — cold-call:** "What changed between a ticket desk and a lost & found desk?" (Physical item handover; high-value escalation; pause sits *after* search, not before create.)
- **Room action:** Confirm Python env is active; students open a fresh notebook or `.py` file named `campus_lost_found.py`.

**Bridge sentence:** "Same habits, new map — let's see why a claim desk beats another WhatsApp thread."

---

## 2. The Real Problem — Campus Lost & Found (7 minutes)

- Narrate the chaos: hostel notice boards, WhatsApp jokes mixed with urgent ID-card posts.
- Screen-share the **chaotic chat vs claim desk** image from Lecture Notes.
- Walk the table: bottle → search path; vague bag → clarification; MacBook → security escalation; API down → retry then calm error.
- Use the railway cloak-room analogy: describe, check register, release only after verification.
- **Engagement — thumbs up:** "Has anyone ever lost something on campus and had to dig through a group chat?" Pause for nods.

**Bridge sentence:** "We know the product story — now we draw the operating map before we touch code."

---

## 3. Design First — Map, State, and Rules (10 minutes)

- Screen-share the ASCII flow: `START → parse → classify → three roads → END`.
- Define terms in plain language (official + simple + example for each):
  - **Checkpoint** — save-game for one claim
  - **Timeout** — kitchen timer per API attempt
  - **RetryPolicy** — knock again with longer pauses
  - **Three-way branch** — one junction, three roads
  - **High-value escalation** — skip the queue, call security
- Walk the **minimal shared state** fields: `report`, `cleaned_report`, `category`, `route`, `match_id`, `result`, `error`, `trace`.
- Screen-share the **category → route** keyword table and the **category desks** diagram.
- **Pair-share (2 min):** "Which desk would a lost umbrella visit?" One volunteer reads the route aloud.

**Bridge sentence:** "Map is on the board — predict one path before we install packages."

---

## 4. Activity — Predict the Path (5 minutes)

- **Room action:** Students write on paper or in chat for: `"Found student's ID card near Block A library"`.
  - Expected `category`, expected `route`, does `escalate_security` run?
- Give **90 seconds** silent work; then reveal suggested answers: `documents` → `search_match` → No.
- **Cold-call:** "Why not high_value?" (Keywords hit documents list, not laptop/passport list.)
- **Engagement — thumbs up:** "Does your prediction match?"

**Bridge sentence:** "Prediction checked — bootstrap the environment and the shared claim notebook."

---

## 5. Environment Setup and ClaimState Overview (7 minutes)

- **Live-coding / screen-share:** Run setup from Lecture Notes:

```bash
pip install langgraph langgraph-checkpoint-sqlite
```

- Paste imports and **`ClaimState` TypedDict**; read each field aloud and tie to the map.
- Paste helper stubs: `run_with_timeout`, `ATTEMPT_BOX`, `fresh_state`.
- **Room action:** Circulate — confirm everyone sees `ClaimState` with all eight fields.
- If someone is behind: share starter cell via chat; they catch up during node building.

**Bridge sentence:** "Notebook is defined — we register stations one by one."

---

## 6. Live Build — Nodes, Three-Way Branch, and Graph Assembly (20 minutes)

- **Live-coding — Node 1–2:** `parse_report` then `classify_item`; narrate keyword lists and how `category` + `route` are written together.
- **Live-coding — Router:** `route_after_classify` returns `state["route"]` — this is the visible three-way junction.
- **Live-coding — Alternate paths:** `ask_clarification`, `escalate_security` — read sample `result` strings aloud.
- **Live-coding — Search path:** `search_match` with `run_with_timeout` + `flaky_match_api`; attach **`RetryPolicy`** on the node (`max_attempts=3`, backoff).
- **Live-coding — Gate + confirm:** `release_item`, `write_confirmation` (prefer `error` text when present).
- **Live-coding — Wire graph:** `add_node`, `add_conditional_edges` with three keys, linear edges to `END`.
- Compile once: `plain_graph = builder.compile()`.
- **Engagement — cold-call:** "After `classify_item`, how many possible next nodes?" (Three.)
- **Room action:** Walk two rows; verify `add_conditional_edges` dict matches route labels exactly.

**Bridge sentence:** "Desk is compiled — run three reports and read the trace like a station log."

---

## 7. Demo 1 — Path Proof: Success, Blocked, Escalated (10 minutes)

- **Live-coding:** Reset `ATTEMPT_BOX["count"] = 0`; invoke bottle report; print `trace`, `result`, `ATTEMPTS`.
- Invoke vague bag report; print blocked trace ending at `ask_clarification`.
- Reset counter; invoke MacBook report; print escalated trace ending at `escalate_security`.
- **Activity (3 min):** Students run all three invokes; circle the node where paths **diverge**.
- **Cold-call:** "Why did the bottle case need three API attempts?" (Flaky demo by design.)
- **Engagement — thumbs up:** "All three traces look different?"

**Bridge sentence:** "Paths proven — next we pause the claim before anyone hands over an item."

---

## 8. Demo 2 — Checkpoint Pause, Inspect, and Resume (15 minutes)

- **Live-coding:** Open `SqliteSaver.from_conn_string("campus_lost_found.db")`; compile with `interrupt_before=["release_item"]`.
- Set `config = {"configurable": {"thread_id": "claim-case-118"}}`; invoke ID-card report; show **partial** trace (stops before release).
- **Live-coding:** `get_state(config)` — print saved `category`, `match_id`, `next` (expect `release_item` pending).
- Show `get_state_history(config)` checkpoint count.
- Narrate the human review moment: desk staff verifies ID, then **`invoke(None, config)`** on the **same thread_id**.
- Print resumed trace and final collection message.
- **Activity — Checkpoint Detective (3 min):** Students write one sentence: *This claim is ready / not ready to release because…*
- **Cold-call:** "What breaks if you change `thread_id` on resume?" (Opens a different claim file.)

**Bridge sentence:** "Save and resume works — now we stress the match API until retries run out."

---

## 9. Demo 3 — Exhausted Retries and Calm User-Facing Error (12 minutes)

- **Live-coding:** Build small `down_builder` with `always_down_api` and same `RetryPolicy`.
- Wrap `down_graph.invoke(...)` in `try/except`; print the **user-facing error** string from Lecture Notes — not the raw stack trace.
- Point to the **retry vs calm error** diagram in Lecture Notes.
- **Engagement — pair-share (2 min):** "Why show 'visit the counter with MATCH-SERVICE-DOWN' instead of `ConnectionError`?"
- **Room action:** Students tick rows 1–3 on the **Reliability Checklist** (timeout, bounded retries, backoff).

**Bridge sentence:** "Reliability is wired — let's compare this desk to the ticket desk you built last time."

---

## 10. Ticket Desk vs Claim Desk and Compare-the-Maps Activity (8 minutes)

- Screen-share the contrast bullets: two roads vs three; pause before create vs pause before **handover**.
- **Activity (4 min):** One sentence: *In a lost & found desk, the checkpoint before release protects…*
  - Suggested answer: against releasing an item before staff verify the claimant's identity.
- **Cold-call:** "Same LangGraph tools — what must you redraw when the campus job changes?" (Operating map / nodes / branch count.)

**Bridge sentence:** "Map compared — time to practice on your own reports and lock takeaways."

---

## 11. Student Practice, Takeaways, and Wrap-Up (8 minutes)

- **Activity — Run Your Own Report (3 min):** Students invoke path-proof demo with a one-line report; note `category`, `route`, `trace`, paraphrased `result`.
- **Activity — Execution Walkthrough (optional if time):** Fill first two rows of the table for bottle vs MacBook reports.
- Rapid-fire **Key Takeaways** from Lecture Notes: nodes + three-way path, checkpoint + stable thread ID, timeout + RetryPolicy + calm errors, prove runs with `trace`.
- **Common mistakes** aloud: wrong thread on resume; releasing high-value through normal search; showing raw `ConnectionError`.
- **Exit ticket:** "Name one habit that stayed the same from the ticket desk and one thing new today." (e.g., third branch; pause after search.)
- Point to the terminology table in Lecture Notes for revision.

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 8–10 min late | Shorten Block 2; skip pair-share in Block 3 |
| 12–15 min late | Paste full code from Lecture Notes via chat; demo Block 7 instructor-only while students scroll |
| 18+ min late | Skip Block 4 Predict-the-Path; give answers verbally |
| 20+ min late | Instructor runs Demo 1 + Demo 2 only; describe Demo 3 failure path verbally |
| 25+ min late | Skip Compare-the-Maps activity; students read Block 10 as homework |

| If you are **ahead** | Add |
|----------------------|-----|
| 5–8 min spare | Students complete **Execution Walkthrough** table for both bottle and MacBook reports |
| 10–15 min spare | **Design a Sibling Desk** activity — mess feedback desk, three nodes + one branch on paper |
| 15+ min spare | Students finish full **Reliability Checklist** (all 7 rows) and peer-check |

**Hard stop at 1 hour 50 minutes:** Everyone has compiled the graph, seen three distinct traces (success / blocked / escalated), and witnessed at least one checkpoint pause + resume on the same `thread_id`.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 8 min | Introduction | Bridge from ticket desk; build list |
| 2 | 7 min | The Real Problem | Image; report → path table |
| 3 | 10 min | Design First | ASCII map; state fields; category table |
| 4 | 5 min | Activity — Predict the Path | ID card prediction |
| 5 | 7 min | Setup + ClaimState | `pip install`; TypedDict; helpers |
| 6 | 20 min | Build the Full Desk | All nodes; conditional edges; compile |
| 7 | 10 min | Demo 1 — Path proof | Three invokes; trace reading |
| 8 | 15 min | Demo 2 — Checkpoint | `SqliteSaver`; `get_state`; resume |
| 9 | 12 min | Demo 3 — Retries / calm error | `down_builder`; try/except message |
| 10 | 8 min | Why This Desk Is Different | Compare maps activity |
| 11 | 8 min | Student Practice + Takeaways | Own report; checklist; exit ticket |

**Break placement:** After Block 7 or early Block 8 (~60–70 min cumulative).
