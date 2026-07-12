# LangGraph Advanced: Checkpoints and Resume

## Introduction

In the **previous** session you modelled an agent workflow as a **graph**: **nodes**, **transitions**, and **minimal shared state**. You built a small runnable map and practised an **execution walkthrough** after each run.

That skill answers: *what ran, and what changed?* This session answers a harder operations question: *what if the run stops halfway — can we save progress and continue later without starting from zero?*

**What you will learn:**

- Enable **checkpointing** on a LangGraph workflow
- **Persist** graph state to a store (including a disk file) and **list** available checkpoints
- **Resume** execution after a simulated interruption or restart
- **Inspect checkpoint payloads** to debug stuck or partial runs

By the end, you should treat long-running agent flows like a form you can save mid-way and reopen tomorrow.

---

## Why a Finished Graph Is Still Fragile

A compiled graph that runs once in memory is useful for learning. It is fragile for real work.

Imagine a campus office workflow: understand request → check rules → prepare letter. If the laptop sleeps after step 2, a pure in-memory run forgets everything. You must start again. Staff at a government seva kendra do not work that way — they keep a **file number** and reopen the same file.

- **Official Definition:** A **checkpoint** is a saved snapshot of graph progress (state + position in the workflow) at a point in time.
- **In Simple Words:** A save-game for your agent workflow.
- **Real-Life Example:** Saving a Google Form draft before you submit. You can close the browser and continue later from the same answers.

Without checkpoints:

- A crash forces a full restart
- You cannot prove how far a partial run went
- Debugging becomes guesswork from memory

With checkpoints:

- Progress is **persisted**
- You can **resume** from the last safe point
- You can **inspect** what the graph believed at each save

This session stays focused on save / list / resume / inspect. It does **not** cover timeouts or automatic retries — those are separate reliability controls.

---

## Checkpoint Building Blocks

Three ideas work together.

### Checkpointer

- **Official Definition:** A **checkpointer** is the storage engine LangGraph uses to write and read checkpoints.
- **In Simple Words:** The cupboard where save-files live.
- **Real-Life Example:** A clerk’s filing cabinet — same papers, labelled by file number.

### Thread ID

- **Official Definition:** A **thread ID** is the unique key that groups checkpoints for one ongoing conversation or job.
- **In Simple Words:** The file number for one student’s case.
- **Real-Life Example:** Your bank ticket number. Different customers must not share the same ticket.

### Persisted state

- **Official Definition:** **Persisted state** is graph state written outside the current process memory so it survives restarts.
- **In Simple Words:** The notebook is saved to a diary on disk, not only kept in your head.
- **Real-Life Example:** Notes in a notebook app sync to the cloud. Closing the phone does not erase the note.

### Activity — Match the Idea

| Situation | Best match: checkpointer / thread ID / checkpoint |
|---|---|
| “Use filing cabinet X” | |
| “This is case STUDENT-104” | |
| “Saved after document check, before letter print” | |

**Suggested answers:** checkpointer, thread ID, checkpoint

---

## Recap the Small Workflow We Will Harden

We reuse the same campus appointment-style map from the previous graph basics work — three stations — so the new skill is **checkpointing**, not a brand-new business story.

```text
START → understand_request → check_availability → confirm_outcome → END
```

Minimal state fields:

| Field | Role |
|---|---|
| `request` | User goal |
| `cleaned_request` | Cleaned text |
| `slot_found` | Availability flag |
| `appointment_time` | Demo time if found |
| `result` | Final message |
| `trace` | Nodes visited so far |

You already know how to draw and run this map. Now you will **save** it as it runs.

---

## Setup

Install LangGraph and the SQLite checkpoint package (for disk persistence):

```bash
pip install langgraph langgraph-checkpoint-sqlite
```

You will see two checkpointer styles in this session:

| Checkpointer | Where saves live | Best for |
|---|---|---|
| `MemorySaver` | Process memory | Quick demos in one Python run |
| `SqliteSaver` | SQLite file on disk | Survive restart / reopen later |

Disk persistence is the skill that matches real interruptions. Memory is only a warm-up.

---

## Pause on Purpose with interrupt_before

To practise resume safely in class, you can ask LangGraph to pause before a named node.

- **Official Definition:** **`interrupt_before`** tells the compiled graph to stop before running one or more listed nodes, leaving a checkpoint you can resume from.
- **In Simple Words:** A planned pause point on the metro line.
- **Real-Life Example:** A bank form that saves after “verify OTP” and waits before “submit final application.”

You will use this in the disk example below to simulate failure or restart without crashing your laptop on purpose.

---

## Enable Checkpointing (In-Memory Warm-Up)

First, attach a checkpointer and a **thread ID**. Same graph. New habit: every `invoke` needs a `config`.

### Full code — MemorySaver warm-up

```python
# Import typing helpers for shared state
from typing import TypedDict, List

# Import LangGraph graph markers and builder
from langgraph.graph import StateGraph, START, END

# Import an in-memory checkpointer for a quick demo
from langgraph.checkpoint.memory import MemorySaver


# Shared notebook shape for the appointment workflow
class AppointmentState(TypedDict):
    request: str  # Original user request
    cleaned_request: str  # Cleaned request text
    slot_found: bool  # Whether a demo slot was found
    appointment_time: str  # Demo time when available
    result: str  # Final user-facing message
    trace: List[str]  # Ordered list of visited nodes


# Node 1: clean the request
def understand_request(state: AppointmentState) -> dict:
    cleaned = state["request"].strip().lower()  # Normalise the text
    return {
        "cleaned_request": cleaned,  # Store cleaned text
        "trace": state["trace"] + ["understand_request"],  # Record this node
    }


# Node 2: apply a simple demo availability rule
def check_availability(state: AppointmentState) -> dict:
    text = state["cleaned_request"]  # Read cleaned request
    if "next week" in text:  # Demo success rule
        return {
            "slot_found": True,  # Mark success
            "appointment_time": "Tuesday 11:00 AM",  # Store demo time
            "trace": state["trace"] + ["check_availability"],  # Extend trace
        }
    return {
        "slot_found": False,  # Mark blocked
        "appointment_time": "",  # Keep time empty
        "trace": state["trace"] + ["check_availability"],  # Extend trace
    }


# Node 3: write the final message
def confirm_outcome(state: AppointmentState) -> dict:
    if state["slot_found"]:  # Success path
        message = "Booking confirmed for " + state["appointment_time"] + "."  # Confirm text
    else:  # Blocked path
        message = "No slot found. Please suggest another week."  # Guidance text
    return {
        "result": message,  # Save final message
        "trace": state["trace"] + ["confirm_outcome"],  # Complete trace
    }


# Build the same three-node map
builder = StateGraph(AppointmentState)  # Create graph shell
builder.add_node("understand_request", understand_request)  # Add station 1
builder.add_node("check_availability", check_availability)  # Add station 2
builder.add_node("confirm_outcome", confirm_outcome)  # Add station 3
builder.add_edge(START, "understand_request")  # Start path
builder.add_edge("understand_request", "check_availability")  # Next path
builder.add_edge("check_availability", "confirm_outcome")  # Next path
builder.add_edge("confirm_outcome", END)  # End path

# Create the in-memory checkpointer cupboard
memory = MemorySaver()

# Compile WITH checkpointer enabled
graph = builder.compile(checkpointer=memory)

# Thread ID = one case file number for this student job
config = {"configurable": {"thread_id": "campus-case-001"}}

# Starting notebook values
initial_state = {
    "request": "I need a follow-up visit next week.",  # Input goal
    "cleaned_request": "",  # Empty before node 1
    "slot_found": False,  # Default flag
    "appointment_time": "",  # Empty before decision
    "result": "",  # Empty before final node
    "trace": [],  # Fresh trace
}

# Run once; checkpoints are written automatically along the way
final_state = graph.invoke(initial_state, config)

# Print final values
print("TRACE:", final_state["trace"])  # Show node order
print("RESULT:", final_state["result"])  # Show final message

# Read the latest saved state for this thread
latest = graph.get_state(config)
print("LATEST VALUES:", latest.values)  # Inspect saved notebook
print("NEXT NODES:", latest.next)  # Empty tuple means the run finished
```

### How the code works

- `MemorySaver()` is the checkpointer cupboard for this process
- `compile(checkpointer=memory)` turns on automatic saving
- `thread_id` groups all saves for one job
- `invoke(..., config)` runs the graph **and** writes checkpoints
- `get_state(config)` reads the latest checkpoint payload for that thread

**Common doubt:** “Can I skip `config`?”  
For checkpointed graphs, no. Without a thread ID, LangGraph cannot know which file to open.

---

## Persist Checkpoints to Disk with SqliteSaver

In-memory saves disappear when the Python process ends. Disk persistence keeps the case file.

- **Official Definition:** **SqliteSaver** stores checkpoints in a SQLite database file.
- **In Simple Words:** A small on-disk diary for your workflow saves.
- **Real-Life Example:** Saving exam answers as a file on your laptop, not only on the classroom whiteboard.

### Full code — persist, stop early, list history, resume

```python
# Import typing helpers
from typing import TypedDict, List

# Import graph tools
from langgraph.graph import StateGraph, START, END

# Import SQLite checkpointer for disk persistence
from langgraph.checkpoint.sqlite import SqliteSaver


# Shared state for the disk-backed workflow
class AppointmentState(TypedDict):
    request: str  # User request text
    cleaned_request: str  # Cleaned text
    slot_found: bool  # Availability flag
    appointment_time: str  # Demo appointment time
    result: str  # Final message
    trace: List[str]  # Execution trace


# Clean the request
def understand_request(state: AppointmentState) -> dict:
    cleaned = state["request"].strip().lower()  # Clean input
    return {
        "cleaned_request": cleaned,  # Save cleaned text
        "trace": state["trace"] + ["understand_request"],  # Log node
    }


# Decide availability with the demo rule
def check_availability(state: AppointmentState) -> dict:
    text = state["cleaned_request"]  # Read cleaned text
    if "next week" in text:  # Success condition
        return {
            "slot_found": True,  # Found flag
            "appointment_time": "Tuesday 11:00 AM",  # Demo time
            "trace": state["trace"] + ["check_availability"],  # Log node
        }
    return {
        "slot_found": False,  # Not found
        "appointment_time": "",  # No time
        "trace": state["trace"] + ["check_availability"],  # Log node
    }


# Write confirmation or blocked message
def confirm_outcome(state: AppointmentState) -> dict:
    if state["slot_found"]:  # Success branch text
        message = "Booking confirmed for " + state["appointment_time"] + "."  # Confirm
    else:  # Blocked branch text
        message = "No slot found. Please suggest another week."  # Guide user
    return {
        "result": message,  # Save result
        "trace": state["trace"] + ["confirm_outcome"],  # Log node
    }


# Assemble the graph map
builder = StateGraph(AppointmentState)  # Graph shell
builder.add_node("understand_request", understand_request)  # Node 1
builder.add_node("check_availability", check_availability)  # Node 2
builder.add_node("confirm_outcome", confirm_outcome)  # Node 3
builder.add_edge(START, "understand_request")  # Wire start
builder.add_edge("understand_request", "check_availability")  # Wire middle
builder.add_edge("check_availability", "confirm_outcome")  # Wire late
builder.add_edge("confirm_outcome", END)  # Wire end

# Open a SQLite file as the persistent cupboard
with SqliteSaver.from_conn_string("campus_checkpoints.db") as checkpointer:
    # Compile with disk checkpointer
    # interrupt_before pauses BEFORE confirm_outcome to simulate a mid-run stop
    graph = builder.compile(
        checkpointer=checkpointer,  # Persist every checkpoint
        interrupt_before=["confirm_outcome"],  # Stop before final node
    )

    # One case file number for this run
    config = {"configurable": {"thread_id": "campus-case-104"}}

    # Initial notebook
    initial_state = {
        "request": "Please book a follow-up next week.",  # Goal
        "cleaned_request": "",  # Empty
        "slot_found": False,  # Default
        "appointment_time": "",  # Empty
        "result": "",  # Empty
        "trace": [],  # Fresh
    }

    # First invoke: runs understand + check, then pauses (simulated interruption)
    partial = graph.invoke(initial_state, config)
    print("PARTIAL TRACE:", partial["trace"])  # Expect two nodes only
    print("PARTIAL RESULT:", partial.get("result", ""))  # Still empty

    # Inspect the latest checkpoint payload
    latest = graph.get_state(config)
    print("SAVED VALUES:", latest.values)  # Notebook at pause point
    print("WAITING TO RUN:", latest.next)  # Should include confirm_outcome

    # List available checkpoints for this thread (history of saves)
    history = list(graph.get_state_history(config))
    print("CHECKPOINT COUNT:", len(history))  # How many saves exist
    for i, snap in enumerate(history):  # Walk newest to older
        print("--- checkpoint", i, "---")  # Label each save
        print(" values:", snap.values)  # State at that save
        print(" next:", snap.next)  # What was due to run next
        print(" checkpoint_id:", snap.config["configurable"].get("checkpoint_id"))  # Save id

    # Resume after the simulated failure/restart: same thread_id, invoke(None)
    resumed = graph.invoke(None, config)
    print("RESUMED TRACE:", resumed["trace"])  # Should now include confirm_outcome
    print("RESUMED RESULT:", resumed["result"])  # Final message appears
```

### How the code works

- `SqliteSaver.from_conn_string("campus_checkpoints.db")` creates/opens a disk file
- `interrupt_before=["confirm_outcome"]` simulates an interruption before the last node
- First `invoke` writes checkpoints and stops with work still pending
- `get_state` shows the **latest** payload
- `get_state_history` **lists** checkpoints so you can see partial progress over time
- Second `invoke(None, config)` **resumes** the same thread from the pause point

**Common mistake:** Changing the `thread_id` on resume. That opens a different case file. Always reuse the same ID for the same job.

### Activity — Predict the Pause

Before running, predict the answers:

| Question | Your prediction |
|---|---|
| Nodes in `PARTIAL TRACE` | |
| Is `result` filled after the first invoke? | |
| What should `latest.next` contain? | |

Then run and compare.

---

## Resume After a True Restart (New Process, Same Disk File)

A pause inside one script is useful. A stronger proof is: stop Python, start again, reopen the same SQLite file and the same thread.

### Full code — reopen disk file and continue

```python
# Import typing helpers
from typing import TypedDict, List

# Import graph tools
from langgraph.graph import StateGraph, START, END

# Import disk checkpointer
from langgraph.checkpoint.sqlite import SqliteSaver


# Same state shape as before (must match saved payloads)
class AppointmentState(TypedDict):
    request: str  # User request
    cleaned_request: str  # Cleaned text
    slot_found: bool  # Flag
    appointment_time: str  # Time
    result: str  # Final text
    trace: List[str]  # Trace


# Rebuild the same node functions (code must match the saved workflow shape)
def understand_request(state: AppointmentState) -> dict:
    cleaned = state["request"].strip().lower()  # Clean
    return {
        "cleaned_request": cleaned,  # Save
        "trace": state["trace"] + ["understand_request"],  # Log
    }


def check_availability(state: AppointmentState) -> dict:
    text = state["cleaned_request"]  # Read
    if "next week" in text:  # Rule
        return {
            "slot_found": True,  # Success
            "appointment_time": "Tuesday 11:00 AM",  # Time
            "trace": state["trace"] + ["check_availability"],  # Log
        }
    return {
        "slot_found": False,  # Blocked
        "appointment_time": "",  # Empty
        "trace": state["trace"] + ["check_availability"],  # Log
    }


def confirm_outcome(state: AppointmentState) -> dict:
    if state["slot_found"]:  # Branch
        message = "Booking confirmed for " + state["appointment_time"] + "."  # Success text
    else:
        message = "No slot found. Please suggest another week."  # Blocked text
    return {
        "result": message,  # Save
        "trace": state["trace"] + ["confirm_outcome"],  # Log
    }


# Rebuild the same graph wiring
builder = StateGraph(AppointmentState)  # Shell
builder.add_node("understand_request", understand_request)  # Node 1
builder.add_node("check_availability", check_availability)  # Node 2
builder.add_node("confirm_outcome", confirm_outcome)  # Node 3
builder.add_edge(START, "understand_request")  # Edges
builder.add_edge("understand_request", "check_availability")  # Edges
builder.add_edge("check_availability", "confirm_outcome")  # Edges
builder.add_edge("confirm_outcome", END)  # Edges

# Reopen the SAME database file created earlier
with SqliteSaver.from_conn_string("campus_checkpoints.db") as checkpointer:
    # Same interrupt setting keeps behaviour consistent while learning
    graph = builder.compile(
        checkpointer=checkpointer,  # Same cupboard
        interrupt_before=["confirm_outcome"],  # Same pause rule if still pending
    )

    # SAME thread ID as the interrupted case
    config = {"configurable": {"thread_id": "campus-case-104"}}

    # Inspect what survived on disk
    latest = graph.get_state(config)
    print("AFTER RESTART — VALUES:", latest.values)  # Should show prior progress
    print("AFTER RESTART — NEXT:", latest.next)  # Pending node if not finished

    # If next is waiting, resume; if already finished, just print values
    if latest.next:  # Work still pending
        final_state = graph.invoke(None, config)  # Continue from checkpoint
        print("FINAL TRACE:", final_state["trace"])  # Full path
        print("FINAL RESULT:", final_state["result"])  # Outcome
    else:  # Already complete
        print("Case already finished. Result:", latest.values.get("result"))  # Show saved result
```

### How the code works

- The SQLite file is the bridge across process restarts
- Rebuilding the graph code is required; the checkpointer stores **state**, not your Python source file
- Matching `thread_id` reconnects you to the same case
- `invoke(None, config)` continues from the saved position

### Activity — Restart Drill

1. Run the persist-and-pause script once so `campus_checkpoints.db` exists.
2. Close that Python session.
3. Run the reopen script.
4. Fill this table:

| Check | What you observed |
|---|---|
| Did values survive restart? | |
| Was `confirm_outcome` still pending (or already done)? | |
| Final `result` text | |

---

## Inspect Checkpoint Payloads Like a Debugger

Saving is not enough. You must **read** payloads when a run looks stuck.

- **Official Definition:** A **checkpoint payload** is the saved bundle of state values, next nodes, and metadata for one save point.
- **In Simple Words:** The contents of one save-file page.
- **Real-Life Example:** Opening a courier tracking event list — scanned at hub, out for delivery, delayed — not only the final “delivered” stamp.

### What to read on each snapshot

| Field / idea | Question it answers |
|---|---|
| `values` | What did the notebook contain here? |
| `next` | Which node was due to run next? |
| `checkpoint_id` | Which exact save is this? |
| History order | How did the case evolve over time? |

### Debugging checklist for partial or stuck runs

- Is the **thread ID** correct?
- Does `next` point to an unexpected node?
- Is a required state field empty at this save?
- Are there fewer checkpoints than expected (run never reached a node)?
- After resume, did `trace` grow, or did nothing move?

### Activity — Payload Detective

From `get_state_history`, pick the snapshot **just before** `confirm_outcome` and write:

1. `slot_found` value  
2. `appointment_time` value  
3. `next` value  
4. One sentence: “This case is ready / not ready to confirm because…”

---

## Design Habits for Checkpointed Graphs

Keep these habits while you practise:

- Give every real job a clear **thread ID** naming style (`campus-case-104`, not `"test"`)
- Prefer **disk** checkpointers when you need restart proof
- Pause on purpose while learning (`interrupt_before`) so you can practise resume
- Inspect **history**, not only the final print
- Do not change state field names casually after saves exist — old payloads will not match new shapes

**Boundary reminder:** Checkpointing protects progress across stops and restarts. It does not by itself set time limits or retry flaky API calls. Keep those as separate skills.

---

## Key Takeaways

- A **checkpoint** is a save-point of graph state and position; a **checkpointer** is where those saves live.
- **`thread_id`** is the case file number that groups one job’s checkpoints.
- **SqliteSaver** persists checkpoints to disk so you can reopen after a restart; **MemorySaver** is only for quick in-process demos.
- **Resume** uses the same thread and `invoke(None, config)` after an interruption.
- **Inspecting payloads** (`get_state`, `get_state_history`) turns partial runs into explainable operations evidence.

In the **next** session you will add separate reliability controls for slow or flaky steps. This session’s foundation stays: save progress, reopen the same case, and read the checkpoint trail clearly.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **Checkpoint** | Saved snapshot of progress (state + position) |
| **Checkpointer** | Storage engine for checkpoints |
| **Persisted state** | State that survives process restart |
| **Thread ID** | Unique key for one job’s checkpoint trail |
| **`MemorySaver`** | In-memory checkpointer |
| **`SqliteSaver`** | SQLite disk checkpointer |
| **`compile(checkpointer=...)`** | Enables checkpointing on a graph |
| **`interrupt_before`** | Pauses before named nodes (simulated stop) |
| **`config["configurable"]["thread_id"]`** | Case file identity for invoke/resume |
| **`invoke(state, config)`** | Run and save checkpoints |
| **`invoke(None, config)`** | Resume from the latest checkpoint |
| **`get_state(config)`** | Read latest checkpoint payload |
| **`get_state_history(config)`** | List checkpoint history for a thread |
| **`checkpoint_id`** | Identifier for one save point |
| **`pip install langgraph langgraph-checkpoint-sqlite`** | Install packages used here |
| **Graph basics (previous idea)** | Nodes, edges, and shared state that checkpoints protect |
