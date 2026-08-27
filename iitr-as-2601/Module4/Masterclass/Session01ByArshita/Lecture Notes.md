# Hands-on: Hostel Maintenance Ticket Desk with LangGraph

## Introduction

In the **previous** sessions you learnt **nodes**, **edges**, **shared state**, **checkpoints**, and **timeouts / retries**.

This hands-on combines them in one campus product: a **Hostel Maintenance Ticket Desk** — design the map, branch, pause/resume, and protect a flaky ticket API with calm failures.

**What you will build:**

- Parse a hostel complaint and **classify** its category
- **Route** to create a ticket or ask for clarification
- **Checkpoint** before ticket creation, then **resume** the same case
- Apply **timeout + RetryPolicy**, and show a clear **user-facing error** when retries fail

---

## The Real Problem: Hostel Maintenance Desk

Hostel life has a familiar pattern. A fan stops. A tap leaks. WiFi dies. Chat complaints get buried. A graph desk keeps stations visible and tickets trackable.

- **Official Definition:** A **maintenance ticket workflow** turns a complaint into a tracked work item, or a clear request for better information.
- **In Simple Words:** A digital complaint desk with stations, not one long messy chat.
- **Real-Life Example:** Like a hospital OPD token system — understand, classify, then issue a token or ask for missing details.

![Chaotic hostel group chat where fan water and wifi complaints get buried versus a calm Hostel Maintenance Ticket Desk that issues a tracked case](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session01byarshita/masterclass01-01-chaotic-chat-vs-ticket-desk.png)

| Student message | Expected path |
|---|---|
| `"Fan not working in room B-204"` | `electrical` → create ticket |
| `"Something is broken in my room"` | `unknown` → ask clarification |
| Valid category, ticket API down | Retry, then calm failure message |

---

## Design First: Map, State, and Rules
Draw the operating map before code. Refresh three ideas, then apply them to this desk.

- **Checkpoint** — Official: saved snapshot of progress (state + position). Simple: save-game for one case. Example: Google Form draft reopened later.
- **Timeout** — Official: max wait before cancelling slow work. Simple: kitchen timer for one API attempt. Example: UPI app that stops spinning forever.
- **RetryPolicy** — Official: bounded try-again rules with backoff. Simple: knock again with longer pauses. Example: refresh railway booking twice, then stop.

```text
START → [parse_complaint] → [classify_category]
                              |--(unknown)--> [ask_clarification] → END
                              |--(known)----> [create_ticket] → [write_confirmation] → END
```

**Minimal shared state:** `complaint`, `cleaned_complaint`, `category`, `ticket_id`, `result`, `error`, `trace`

| If cleaned text contains… | Category |
|---|---|
| `fan`, `light`, `switch`, `power` | `electrical` |
| `water`, `tap`, `leak`, `drain` | `plumbing` |
| `wifi`, `internet`, `network` | `wifi` |
| none of the above | `unknown` |

![Hostel facility counters for electrical plumbing and network with a separate clarification counter for unclear complaints and a shared travel log notebook](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session01byarshita/masterclass01-02-category-desks-branching.png)

### Activity — Predict the Path
For `"WiFi keeps dropping in Block C"`, write: expected `category`, next node after classify, and whether `ask_clarification` runs.
**Suggested answers:** `wifi` → `create_ticket` → No

### Setup
```bash
pip install langgraph langgraph-checkpoint-sqlite
```

---

## Build the Full Desk: Branch, Checkpoint, Harden
One notebook flow covers branching, save/resume, and reliability.
### Full code — hostel ticket desk end to end

```python
# Import typing helpers for shared state
from typing import TypedDict, List

# Import timeout helper from the standard library
from concurrent.futures import ThreadPoolExecutor

# Import LangGraph graph tools and markers
from langgraph.graph import StateGraph, START, END

# Import disk checkpointer for pause and resume
from langgraph.checkpoint.sqlite import SqliteSaver

# Import bounded retry rules for the API node
from langgraph.types import RetryPolicy


# Shared notebook for one hostel maintenance case
class TicketState(TypedDict):
    complaint: str  # Original student complaint
    cleaned_complaint: str  # Normalised complaint text
    category: str  # electrical / plumbing / wifi / unknown
    ticket_id: str  # Ticket id after successful create
    result: str  # Final user-facing message
    error: str  # Calm failure text when needed
    trace: List[str]  # Ordered list of visited nodes


# Mutable counter used by the flaky ticket API demo
ATTEMPT_BOX = {"count": 0}  # Counts API attempts across retries


# Run a function with a maximum wait time in seconds
def run_with_timeout(fn, seconds: float, *args):
    with ThreadPoolExecutor(max_workers=1) as pool:  # One worker thread
        future = pool.submit(fn, *args)  # Start the work
        return future.result(timeout=seconds)  # Wait only up to the limit


# Flaky ticket API: fails twice, then returns a ticket id
def flaky_ticket_api(category: str, complaint: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    if ATTEMPT_BOX["count"] < 3:  # First two attempts are transient failures
        raise ConnectionError("Temporary ticket service glitch")  # Retryable error
    return "HT-" + category[:3].upper() + "-7781"  # Success payload on attempt 3


# Always-down API used only for the exhausted-retry drill
def always_down_api(category: str, complaint: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    raise ConnectionError("Service unavailable")  # Never recovers in this drill


# Node 1: clean the complaint and start the trace
def parse_complaint(state: TicketState) -> dict:
    cleaned = state["complaint"].strip().lower()  # Normalise spaces and case
    return {
        "cleaned_complaint": cleaned,  # Save cleaned text
        "error": "",  # Clear old errors at case start
        "trace": state["trace"] + ["parse_complaint"],  # Record this station
    }


# Node 2: classify category with keyword rules
def classify_category(state: TicketState) -> dict:
    text = state["cleaned_complaint"]  # Read cleaned complaint
    if any(w in text for w in ["fan", "light", "switch", "power"]):  # Electrical clues
        category = "electrical"  # Route to electrical desk
    elif any(w in text for w in ["water", "tap", "leak", "drain"]):  # Plumbing clues
        category = "plumbing"  # Route to plumbing desk
    elif any(w in text for w in ["wifi", "internet", "network"]):  # Network clues
        category = "wifi"  # Route to wifi desk
    else:  # No clear keyword
        category = "unknown"  # Force clarification path
    return {
        "category": category,  # Store classification decision
        "trace": state["trace"] + ["classify_category"],  # Record this station
    }


# Router: choose create path or clarification path
def route_after_classify(state: TicketState) -> str:
    if state["category"] == "unknown":  # Unclear complaint
        return "ask_clarification"  # Go to guidance station
    return "create_ticket"  # Go to ticket creation station


# Alternate node: ask for clearer details
def ask_clarification(state: TicketState) -> dict:
    message = (  # Build calm guidance
        "I could not classify your hostel issue. "
        "Please mention if it is electrical, plumbing, or wifi, "
        "and include your room or block number."
    )
    return {
        "result": message,  # Save guidance as final result
        "trace": state["trace"] + ["ask_clarification"],  # Record this station
    }


# API node: create ticket with per-attempt timeout
def create_ticket(state: TicketState) -> dict:
    ticket = run_with_timeout(  # Bound one attempt's wait
        flaky_ticket_api,  # Flaky service
        2.0,  # Two-second timeout
        state["category"],  # Pass category
        state["cleaned_complaint"],  # Pass complaint
    )
    return {
        "ticket_id": ticket,  # Save ticket id
        "error": "",  # Clear error on success
        "trace": state["trace"] + ["create_ticket"],  # Record this station
    }


# Final node: write confirmation or prefer error text
def write_confirmation(state: TicketState) -> dict:
    if state["error"]:  # Prefer calm error when present
        message = state["error"]  # Show failure text
    else:  # Happy path
        message = (
            "Ticket " + state["ticket_id"] + " created for "
            + state["category"] + " issue. Maintenance team notified."
        )
    return {
        "result": message,  # Save final user message
        "trace": state["trace"] + ["write_confirmation"],  # Record this station
    }


# Helper: fresh starting notebook for one complaint
def fresh_state(complaint: str) -> dict:
    return {
        "complaint": complaint,  # Student input
        "cleaned_complaint": "",  # Empty before parse
        "category": "",  # Empty before classify
        "ticket_id": "",  # Empty before create
        "result": "",  # Empty before final node
        "error": "",  # No error yet
        "trace": [],  # Fresh trace
    }


# Assemble the full desk map
builder = StateGraph(TicketState)  # Create graph shell
builder.add_node("parse_complaint", parse_complaint)  # Register parse
builder.add_node("classify_category", classify_category)  # Register classify
builder.add_node("ask_clarification", ask_clarification)  # Register clarification
builder.add_node(  # Register create with bounded retries
    "create_ticket",
    create_ticket,
    retry_policy=RetryPolicy(  # House rules for try-again
        max_attempts=3,  # Stop after 3 tries
        initial_interval=0.2,  # Short first wait
        backoff_factor=2.0,  # Grow wait after each failure
        max_interval=2.0,  # Cap wait growth
        jitter=False,  # Keep timing predictable for learning
    ),
)
builder.add_node("write_confirmation", write_confirmation)  # Register confirm
builder.add_edge(START, "parse_complaint")  # Always start at parse
builder.add_edge("parse_complaint", "classify_category")  # Then classify
builder.add_conditional_edges(  # Branch after classification
    "classify_category",
    route_after_classify,
    {
        "ask_clarification": "ask_clarification",  # Unclear path
        "create_ticket": "create_ticket",  # Known-category path
    },
)
builder.add_edge("ask_clarification", END)  # Clarification ends
builder.add_edge("create_ticket", "write_confirmation")  # Create continues
builder.add_edge("write_confirmation", END)  # Confirm ends


# Demo 1 — Path proof: success branch vs clarification branch
plain_graph = builder.compile()  # Compile without checkpointer
ATTEMPT_BOX["count"] = 0  # Reset flaky counter
success = plain_graph.invoke(fresh_state("Fan not working in room B-204"))  # Electrical case
print("SUCCESS TRACE:", success["trace"])  # Expect create + confirm path
print("SUCCESS RESULT:", success["result"])  # Expect ticket confirmation
print("ATTEMPTS:", ATTEMPT_BOX["count"])  # Expect 3 because API is flaky by design

blocked = plain_graph.invoke(fresh_state("Something is broken in my room"))  # Vague case
print("BLOCKED TRACE:", blocked["trace"])  # Expect ask_clarification only
print("BLOCKED RESULT:", blocked["result"])  # Expect guidance message


# Demo 2 — Pause before create, inspect checkpoint, resume same thread
with SqliteSaver.from_conn_string("hostel_tickets.db") as checkpointer:  # Disk cupboard
    paused_graph = builder.compile(  # Compile with save points
        checkpointer=checkpointer,  # Persist every checkpoint
        interrupt_before=["create_ticket"],  # Planned pause before create
    )
    config = {"configurable": {"thread_id": "hostel-case-204"}}  # Case file number
    ATTEMPT_BOX["count"] = 0  # Reset attempts for this case
    partial = paused_graph.invoke(  # Runs parse + classify, then pauses
        fresh_state("Water leaking from tap in B-118"),
        config,
    )
    print("PARTIAL TRACE:", partial["trace"])  # Expect parse + classify only
    latest = paused_graph.get_state(config)  # Read latest checkpoint payload
    print("SAVED CATEGORY:", latest.values.get("category"))  # Expect plumbing
    print("WAITING TO RUN:", latest.next)  # Expect create_ticket pending
    print("CHECKPOINT COUNT:", len(list(paused_graph.get_state_history(config))))  # List saves
    resumed = paused_graph.invoke(None, config)  # Resume same thread_id
    print("RESUMED TRACE:", resumed["trace"])  # Expect create + confirm added
    print("RESUMED RESULT:", resumed["result"])  # Expect ticket confirmation


# Demo 3 — Exhausted retries become a calm user-facing error
down_builder = StateGraph(TicketState)  # Small failure-focused graph


def create_ticket_down(state: TicketState) -> dict:
    ticket = run_with_timeout(always_down_api, 1.0, state["category"], state["cleaned_complaint"])  # Always fails
    return {"ticket_id": ticket, "trace": state["trace"] + ["create_ticket"], "error": ""}  # Unreachable while down


down_builder.add_node(  # API node with the same retry budget
    "create_ticket",
    create_ticket_down,
    retry_policy=RetryPolicy(max_attempts=3, initial_interval=0.1, backoff_factor=2.0, jitter=False),
)
down_builder.add_edge(START, "create_ticket")  # Start at API node
down_builder.add_edge("create_ticket", END)  # End after API node
down_graph = down_builder.compile()  # Compile failure drill
ATTEMPT_BOX["count"] = 0  # Reset counter

try:  # Catch exhausted retries at the call site
    down_graph.invoke(
        {
            "complaint": "Light not working in A-12",  # Original text
            "cleaned_complaint": "light not working in a-12",  # Already cleaned for this drill
            "category": "electrical",  # Known category so create would be valid
            "ticket_id": "",  # Empty before success
            "result": "",  # Empty before final message
            "error": "",  # Empty before failure handling
            "trace": [],  # Fresh trace
        }
    )
except Exception:  # Translate technical failure into desk language
    user_facing = (
        "We could not create your hostel maintenance ticket after 3 attempts "
        "because the ticket service is unavailable. Please try again after some time, "
        "or visit the hostel office with this note: TICKET-SERVICE-DOWN."
    )
    print("USER-FACING ERROR:", user_facing)  # What the student should see
    print("INTERNAL ATTEMPTS:", ATTEMPT_BOX["count"])  # Proof retries happened
```

### How the code works

- `classify_category` + `route_after_classify` create a **visible branch**: known category vs clarification
- `RetryPolicy` retries transient `ConnectionError` with **backoff**; `run_with_timeout` bounds each attempt
- `interrupt_before=["create_ticket"]` plus `SqliteSaver` saves the case mid-way; `invoke(None, config)` resumes the same **thread ID**

![Maintenance case file paused at a review gate with progress saved before the Create Ticket stamp station so the same case can resume later](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session01byarshita/masterclass01-03-checkpoint-pause-before-create.png)

- When retries are exhausted, `try/except` around `invoke` produces a calm **user-facing error**, not a stack trace

![Hostel ticket machine succeeding after bounded retries with growing waits, contrasted with a scary technical error versus a calm visit-the-hostel-office message](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session01byarshita/masterclass01-04-retry-and-calm-error.png)

- `trace` proves which stations ran on success, blocked, pause, and resume paths

**Common mistakes:** Changing `thread_id` on resume opens a different case. Do not show raw `ConnectionError` text to students.
---
## Student Practice

### Activity — Run Your Own Complaint
Invoke the path-proof demo with your own one-line hostel complaint. Record `category`, `trace`, and a short paraphrase of `result`.

### Activity — Checkpoint Detective
After the partial pause in the checkpoint demo, write one sentence: *This case is ready / not ready to create a ticket because…*

### Activity — Reliability Checklist

| # | Check | Done? |
|---|---|---|
| 1 | API node has a timeout | |
| 2 | Retries are bounded (`max_attempts`) | |
| 3 | Backoff is enabled | |
| 4 | Unclear complaints go to clarification | |
| 5 | Exhausted retries show a clear next step | |
| 6 | You can explain `trace` for success and blocked paths | |

### Activity — Execution Walkthrough
Fill this table once for the fan complaint and once for the vague complaint:

| Step order | Node name | Important state after node | Why control moved next |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

If the result looks wrong, decide whether the bug is in a **node**, a **transition**, or a **state field**.

---

## Key Takeaways

- Model the desk as **nodes**, **conditional paths**, and **minimal shared state**.
- **Checkpoints** pause before ticket creation and resume with a stable **thread ID**.
- **Timeouts** and **RetryPolicy** protect flaky APIs; exhausted retries need calm **user-facing errors**.
- Prove every run with a **`trace`** and a short **execution walkthrough**.
- The same desk pattern extends to other campus queues using the same LangGraph habits.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **LangGraph** | Framework for stateful multi-step workflows as graphs |
| **Node / Conditional edge** | Station of work / branch chosen by a router |
| **Graph state / `trace`** | Shared notebook / ordered proof of node visits |
| **`StateGraph` / `compile()` / `invoke()`** | Build, freeze, and run the workflow |
| **`interrupt_before`** | Planned pause before a named node |
| **`SqliteSaver` / `thread_id`** | Disk checkpoints grouped by case file number |
| **`get_state` / `get_state_history`** | Inspect latest save and checkpoint trail |
| **`invoke(None, config)`** | Resume from the latest checkpoint |
| **Timeout / `RetryPolicy` / backoff** | Max wait per attempt / bounded retries / growing wait |
| **User-facing error** | Calm next-step message after hard failure |
| **`pip install langgraph langgraph-checkpoint-sqlite`** | Packages used in this hands-on |
