# Observability and Tracing for Agents

## Introduction

In the **previous** session you made agent runs more reliable with **timeouts**, **bounded retries**, and clear **user-facing errors** when a step could not recover.

That stops endless waits. This session is about **Observability** and **Tracing** for agents: *when a multi-step run fails, how do we see which step went wrong — the way a parcel tracking page shows where a package stopped?*

**Running story for this session:** a **campus parcel desk**. A student asks about a package. The agent must **retrieve** the register row, **reason** a short reply, then **act** by posting that reply on the notice board. Every step writes one line in a **tracking diary** (`parcel_runs.jsonl`) — that diary is how we practise **observability**.

**What you will learn:**

- **Tracing:** give each enquiry a **trace id** and stamp **timestamps** on every desk step
- **Observability:** write **structured logs** (JSON lines) like a proper register, not a messy paragraph
- Follow one **trace** through **retrieve → reason → act** when the parcel is missing
- Use a read-only debug workflow — **observability without** fancy control-room software

---

## Why Agents Need Observability (a Tracking Diary)

**Observability** is the skill. The parcel diary is how we see it. A single API call fails in one place. An **agent** fails across many desks. If the notice board only says `"Error happened"`, the student and you both guess.

| Without observability | With observability (tracking diary) |
|---|---|
| “Your parcel failed” | “Register lookup found 0 rows; reply never posted” |
| Blame the last person you see | Open the AWB and see the first failed station |
| Re-run and hope | Re-read the same failed enquiry |

![Campus parcel desk comparison — without observability only a vague Error happened note versus with observability an open tracking diary showing AWB stamps from picked up to ready](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session45/session45-01-without-vs-with-observability.png)

- **Official Definition:** **Observability** is understanding a system from the signals it produces (logs, traces, metrics).
- **In Simple Words:** Keep a tracking diary so you can re-read what happened.
- **Real-Life Example (we will code this):** Parcel tracking — *picked up → hub → out for delivery*. You do not phone the warehouse and hope someone remembers.

- **Official Definition:** **Tracing** means following one run across steps using a shared id.
- **In Simple Words:** One AWB number stamped on every desk note.
- **Real-Life Example:** The same tracking number on SMS, app, and counter printout.

### Activity — Parcel Desk Blind Spot

Student says: “Wrong parcel status.” Without a diary, can you prove (a) wrong row retrieved, (b) reply invented, (c) notice board never ran? **Answers:** No / No / No.

---

## Tracing Basics: Trace Id = AWB, Timestamp = Clock

**Tracing** starts here: one shared id + a clock on every stamp — the two fields every courier page needs.

![Same AWB sticker stamped across three campus desk slips with clock times teaching shared trace id and timestamps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session45/session45-02-trace-id-awb-timestamps.png)

- **Official Definition:** A **trace id** is a unique id shared by all events in one run.
- **In Simple Words:** The AWB for this one enquiry.
- **Real-Life Example:** `PKG-a1b2c3d4` on every line for that student’s question — not mixed with the next queue number.

- **Official Definition:** A **timestamp** records when an event happened (often ISO / UTC).
- **In Simple Words:** The clock printed beside each tracking update.
- **Real-Life Example:** “Hub scan at 10:41” vs “Out for delivery at 14:02” — order matters.

**Habits at the parcel desk:** create the AWB (**trace id**) once; stamp **start** and **end** at each desk; never reuse yesterday’s AWB.

**Common doubt:** “Is student roll number the same as trace id?”  
No. One student can ask many times. Each **enquiry** gets a new AWB.

### Demo — mint an AWB and two clock stamps

Run this small script. You should see **two different times** and one shared id.

```python
# Import tools to mint an AWB-style id and clock stamps
import uuid
from datetime import datetime, timezone
import time


# Make one tracking id for this enquiry
def new_trace_id() -> str:
    # Short courier-style label
    return f"PKG-{uuid.uuid4().hex[:8]}"


# Print the current UTC clock in ISO form
def now_iso() -> str:
    # Same style parcel apps use for scans
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    # Student joins the queue — mint AWB once
    awb = new_trace_id()
    print("AWB (trace_id):", awb)
    # First desk stamp
    print("Picked up at:", now_iso())
    # Small wait so the second stamp is visibly later
    time.sleep(1)
    # Second desk stamp — same AWB, later clock
    print("At hub at:   ", now_iso())
    print("Same AWB on both lines?", awb)
```

**How the code works**

- `new_trace_id` is the AWB creator — call it **once** per enquiry.
- `now_iso` is the scan clock — call it on **every** desk event.
- The one-second sleep is only so you can *see* timestamps differ in the demo.

### Activity — Design Your Desk AWB

Write one pattern for a canteen-order bot (example: `MESS-20260725-x9f2`). List the parts, and why a second order by the same student needs a **new** id.

---

## Observability in Practice: Structured Logs = Register Rows

**Observability** needs readable signals. A clerk who writes “parcel somehow delayed near hub maybe” helps nobody. A register with named columns does.

![Messy free-text delay note contrasted with a neat structured parcel register of Trace ID, Time, Step, Event, Status, and Detail rows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session45/session45-03-structured-register-rows.png)

- **Official Definition:** A **structured log** is an entry with named fields, not only free text.
- **In Simple Words:** Fill the register columns.
- **Real-Life Example:** Parcel register: AWB | time | station | status | note.

- **Official Definition:** **JSON Lines** means one complete JSON object per file line.
- **In Simple Words:** One register row per line.
- **Real-Life Example:** Excel-like rows, but in a `.jsonl` text file you can append forever.

**Columns we will use at the desk**

| Field | Parcel-desk meaning |
|---|---|
| `trace_id` | AWB for this enquiry |
| `timestamp` | Scan clock |
| `step` | Which desk: `retrieve`, `reason`, `act` |
| `event` | What happened: `start`, `end`, `tool_call`, `model_message`, `error` |
| `status` | `ok` or `error` |
| `detail` | Short note (hits, why, chars) — not the whole warehouse |

**Common error:** Pasting the entire parcel photo into every row. Write a short note; open the photo only if needed.

### Demo — write two real register rows

```python
# Import json and Path to append register rows
import json
from pathlib import Path
from datetime import datetime, timezone
import uuid


# Mint AWB
def new_trace_id() -> str:
    return f"PKG-{uuid.uuid4().hex[:8]}"


# Clock stamp
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# Append one JSON register row
def log_event(log_path: Path, event: dict) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    LOG = Path("parcel_runs.jsonl")
    awb = new_trace_id()
    # Row 1: parcel picked up at retrieve desk
    log_event(LOG, {
        "trace_id": awb,
        "timestamp": now_iso(),
        "step": "retrieve",
        "event": "start",
        "status": "ok",
        "detail": {"desk": "register_lookup"},
    })
    # Row 2: same AWB, later event
    log_event(LOG, {
        "trace_id": awb,
        "timestamp": now_iso(),
        "step": "retrieve",
        "event": "end",
        "status": "ok",
        "detail": {"hits": 1},
    })
    print("Wrote 2 rows for", awb)
    print("Open parcel_runs.jsonl — you should see 2 lines, same trace_id.")
```

**How the code works**

- Each call to `log_event` adds **one row** (one JSON line).
- Both rows share the same AWB so you can filter later.
- Open the file in any editor — this is your tracking page in text form.

---

## Instrument the Three Desks: Retrieve → Reason → Act

This is **tracing** across an agent path: the same AWB stamped at every desk so one enquiry stays one story.

- **Official Definition:** **Instrumentation** means adding code that emits logs/traces around real work.
- **In Simple Words:** Stamp the register when work starts and ends — without changing the parcel itself.
- **Real-Life Example:** Hub staff still scan the box; the scan is the log.

**Desk map for our agent**

| Desk | Job | Everyday feel |
|---|---|---|
| `retrieve` | Look up the parcel register | Counter checks the book |
| `reason` | Turn the row into a short reply | Clerk decides what to say |
| `act` | Post the reply on the notice board | Message goes to the student |

![Three campus desks — Retrieve at the register, Reason writing a short reply, Act posting on the notice board — linked by the same AWB](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session45/session45-04-retrieve-reason-act-desks.png)

- **Official Definition:** A **tool call** log records an external action (register lookup, notice board) and its outcome.
- **In Simple Words:** Which button or book did we use, and did it work?
- **Real-Life Example:** ATM receipt line — “balance enquiry — success.”

- **Official Definition:** A **model message** log records a short summary of the decided reply (simulated clerk/model turn).
- **In Simple Words:** Save the headline of what we decided to say.
- **Real-Life Example:** Meeting-minute line — decision only, not the full chat.

### Full code — parcel desk agent with diary

```python
# Parcel-desk agent: retrieve register → reason reply → act on notice board
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path


# Create AWB for one enquiry
def new_trace_id() -> str:
    return f"PKG-{uuid.uuid4().hex[:8]}"  # Short unique tracking label


# Scan clock
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()  # Comparable UTC stamp


# Write one register row
def log_event(log_path: Path, event: dict) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)  # Create folder if needed
    with log_path.open("a", encoding="utf-8") as f:  # Append; keep older runs
        f.write(json.dumps(event, ensure_ascii=False) + "\n")  # One JSON object per line


# Standard desk stamp used everywhere
def step_log(log_path, trace_id, step, event, status="ok", detail=None):
    log_event(log_path, {  # Build and persist one structured row
        "trace_id": trace_id,  # Shared AWB for this enquiry
        "timestamp": now_iso(),  # When this stamp happened
        "step": step,  # retrieve / reason / act / run
        "event": event,  # start / end / tool_call / model_message / error
        "status": status,  # ok or error
        "detail": detail or {},  # Short extras only
    })


# Tiny campus parcel register (real-life book on the counter)
PARCELS = {
    "amazon": "Amazon box for Riya — ready at Gate 2 pickup.",  # Known row
    "flipkart": "Flipkart pouch for Aman — held at hostel desk.",  # Known row
}


# Desk 1: retrieve — look up the register
def retrieve(query: str, trace_id: str, log_path: Path) -> str:
    step_log(log_path, trace_id, "retrieve", "start", detail={"query": query})
    # Simple keyword match like a clerk scanning names
    key = None
    if "amazon" in query.lower():
        key = "amazon"
    elif "flipkart" in query.lower():
        key = "flipkart"
    row = PARCELS.get(key, "")
    step_log(
        log_path, trace_id, "retrieve", "tool_call",
        status="ok" if row else "error",
        detail={"tool": "parcel_register", "hits": 1 if row else 0},
    )
    step_log(
        log_path, trace_id, "retrieve", "end",
        status="ok" if row else "error",
        detail={"row_chars": len(row)},
    )
    return row


# Desk 2: reason — write a short reply from the row (simulated model)
def reason(query: str, row: str, trace_id: str, log_path: Path) -> str:
    step_log(log_path, trace_id, "reason", "start", detail={"query": query[:60]})
    if not row:
        step_log(
            log_path, trace_id, "reason", "model_message", status="error",
            detail={"role": "clerk", "summary": "no_register_row"},
        )
        step_log(log_path, trace_id, "reason", "end", status="error", detail={"why": "empty_register"})
        return ""
    reply = row
    step_log(
        log_path, trace_id, "reason", "model_message", status="ok",
        detail={"role": "clerk", "summary": reply[:40]},
    )
    step_log(log_path, trace_id, "reason", "end", status="ok")
    return reply


# Desk 3: act — post on the student notice board
def act(reply: str, trace_id: str, log_path: Path) -> str:
    step_log(log_path, trace_id, "act", "start")
    if not reply:
        step_log(log_path, trace_id, "act", "error", status="error", detail={"why": "nothing_to_post"})
        step_log(log_path, trace_id, "act", "end", status="error")
        return "Sorry — no parcel row found to post."
    step_log(
        log_path, trace_id, "act", "tool_call", status="ok",
        detail={"tool": "notice_board", "chars": len(reply)},
    )
    step_log(log_path, trace_id, "act", "end", status="ok")
    return reply


# Full enquiry: one AWB, three desks in order
def run_parcel_enquiry(query: str, log_path: Path) -> str:
    trace_id = new_trace_id()
    step_log(log_path, trace_id, "run", "start", detail={"query": query})
    row = retrieve(query, trace_id, log_path)
    reply = reason(query, row, trace_id, log_path)
    final = act(reply, trace_id, log_path)
    step_log(
        log_path, trace_id, "run", "end",
        status="ok" if reply else "error",
        detail={"trace_id": trace_id},
    )
    print(f"AWB / trace_id = {trace_id}")
    return final


if __name__ == "__main__":
    LOG = Path("parcel_runs.jsonl")
    # Success path — Amazon is in the register
    print("SUCCESS:", run_parcel_enquiry("Where is my Amazon box?", LOG))
    # Failure path — Myntra is not in the register
    print("FAIL:   ", run_parcel_enquiry("Where is my Myntra packet?", LOG))
```

**How the code works**

- **Amazon** enquiry: register hit → clerk reply → notice board post — all `ok`.
- **Myntra** enquiry: `hits: 0` at retrieve → reason and act log errors — the diary shows the first break.
- Printed AWB is what you search in `parcel_runs.jsonl`.

### Activity — Predict Before You Open the File

First error desk for the Myntra run: retrieve / reason / act? **Answer:** retrieve (`hits: 0`); later errors are follow-on.

---

## Follow One Trace (One AWB) Like a Tracking Page

Here **tracing** and **observability** meet: you follow one `trace_id` and read the diary — you do not guess.

![Read-only tracking timeline for one AWB with magnifying glass on the first retrieve error while later reason and act errors show as follow-on](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session45/session45-05-follow-awb-first-error.png)

- **Official Definition:** A **read-only debug workflow** means inspecting logs before changing systems blindly.
- **In Simple Words:** Read the tracking history before you redesign the warehouse.
- **Real-Life Example:** Open the courier app, paste the AWB, see the last successful scan.

### Desk checklist

1. Copy the printed AWB (`trace_id`).
2. Open `parcel_runs.jsonl`.
3. Keep only lines with that AWB.
4. Walk **retrieve → reason → act**; stop at the first `"status": "error"`.
5. Read `detail` (`hits: 0`, `empty_register`, `nothing_to_post`).
6. Fix that desk only; run again; confirm a new AWB shows clean `ok` stamps.

### Full code — open one AWB timeline

```python
# Read-only tracking page for one AWB
import json
from pathlib import Path


# Load only rows for one tracking id
def load_trace(log_path: Path, trace_id: str) -> list:
    events = []  # Collect matching rows in file order
    with log_path.open("r", encoding="utf-8") as f:  # Read the diary
        for line in f:
            if not line.strip():  # Skip blank lines
                continue
            item = json.loads(line)  # Parse one JSON register row
            if item.get("trace_id") == trace_id:  # Keep only this AWB
                events.append(item)
    return events


# Print a human tracking timeline
def print_timeline(events: list) -> None:
    for e in events:
        print(  # One readable scan line per event
            f"{e.get('timestamp')} | {e.get('step'):8} | "
            f"{e.get('event'):14} | {e.get('status'):5} | {e.get('detail')}"
        )


# First failed scan
def first_error(events: list):
    for e in events:
        if e.get("status") == "error":  # Stop at earliest break
            return e
    return None  # Clean timeline


if __name__ == "__main__":
    # Paste the FAIL run AWB printed by the agent
    AWB = "PKG-REPLACE"
    events = load_trace(Path("parcel_runs.jsonl"), AWB)
    print_timeline(events)
    err = first_error(events)
    if err:
        print("First break at desk:", err.get("step"), "→", err.get("detail"))
    else:
        print("No error status for this AWB.")
```

**How the code works**

- Filters the register to **one parcel enquiry**.
- Prints the same story a tracking page would show.
- Points you to the **first** broken desk so you do not “fix” the notice board first.

**Myntra failure pattern**

| Desk | Status | Clue |
|---|---|---|
| retrieve | error | `hits: 0` |
| reason | error | `why: empty_register` |
| act | error | `why: nothing_to_post` |

Fix the **register / lookup**, then re-run. Do not rewrite the notice-board message first.

### Activity — Localise This Timeline

1. `retrieve | tool_call | ok | hits: 1` · 2. `reason | model_message | error | garbled_reply` · 3. `act | error | nothing_to_post`  
Fix first? **Answer:** reason.

---

## Observability Without a Control-Room APM

Big companies use **APM** dashboards (airport-style ops screens). **Observability** for learning still works with a `.jsonl` register alone.

- **Official Definition:** **APM tooling** collects traces, metrics, and logs across live services.
- **In Simple Words:** A paid control room for production.
- **Real-Life Example:** Airport ops wall vs your paper boarding checklist while learning — same idea, lighter tool.

**Diary alone can prove:** register hit/miss; reply drafted or not; notice board ran or not; success AWB vs fail AWB.

**Avoid:** retries before reading the first error; deleting `parcel_runs.jsonl` mid-check; changing three desks at once.

### Activity — Fill a Desk Debug Card

After Myntra fail: AWB · first error desk · detail/why · fix (e.g. add `myntra` to `PARCELS`) · new AWB after success.

Timeouts and retries (**previous** session) stop endless waits. **Observability** and **tracing** show *where* and *why* something still failed.

---

## Key Takeaways

- **Observability** means you can understand an agent run from the signals it left (logs / traces) — here, the parcel diary.
- **Tracing** means one **AWB (trace id)** plus **timestamps** stamped on every desk so the full path is followable.
- Prefer **JSON line** register rows (`step`, `event`, `status`, `detail`) over essay-style prints.
- Instrument **retrieve → reason → act** the same way; on failure, fix the **first** error desk.
- Practise observability with a **read-only** timeline — no production APM needed for learning builds.

These habits prepare you for larger agents where evidence, not guesswork, drives fixes.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Observability | Term | Understand a run from logs/traces it produces |
| Tracing | Term | Follow one run across steps with a shared id |
| `trace_id` / AWB | Term | Unique id for one enquiry / run |
| Timestamp (ISO / UTC) | Term | Clock on each register stamp |
| Structured log | Term | Named fields, not free essay |
| JSON Lines / NDJSON | Term | One JSON object per line |
| Instrumentation | Term | Stamping desks around real work |
| Tool call log | Term | Which tool/register/board and outcome |
| Model message log | Term | Short reply summary |
| Read-only debug workflow | Term | Read timeline before changing code |
| APM | Term | Production control-room tools (optional later) |
| `json` | Library | Build/parse register rows |
| `datetime` / `timezone` | Library | Scan timestamps |
| `uuid` | Library | Mint AWB-style ids |
| `pathlib.Path` | Library | Append/read `parcel_runs.jsonl` |
| Editor search / `grep` | Skill | Filter one AWB from the file |
