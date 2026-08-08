# Hands-on: Campus Lost & Found Claim Desk with LangGraph

## Introduction

In the **previous** masterclass you built a **Hostel Maintenance Ticket Desk** — classify a complaint, branch to create a ticket or ask for clarification, pause with a checkpoint, and protect a flaky API with timeout plus retries.

This hands-on applies the same LangGraph habits to a different campus product: a **Campus Lost & Found Claim Desk**. You will design the map, use a **three-way branch**, pause before releasing an item, and keep search failures calm.

**What you will build:**

- Parse a lost-item report and **classify** its category
- **Route** three ways: ask clarification, escalate high-value items, or search for a match
- **Checkpoint** before item release, then **resume** the same claim file
- Apply **timeout + RetryPolicy**, and show a clear **user-facing error** when retries fail

---

## The Real Problem: Campus Lost & Found Desk

Hostel notice boards fill with “lost black bottle” messages. WhatsApp groups mix jokes with urgent ID-card posts. A graph desk keeps stations visible and claim files trackable.

- **Official Definition:** A **lost & found claim workflow** turns a report into a tracked claim: clarify, escalate, or match-and-release.
- **In Simple Words:** A digital claim counter with clear desks, not one buried chat thread.
- **Real-Life Example:** Like a railway cloak room — describe the bag, check the register, then release only after verification.

![Chaotic campus WhatsApp lost-item chat versus a calm Campus Lost and Found Claim Desk with labelled counters and tracked claim files](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session02byprofabhinandan/masterclass02-01-chaotic-chat-vs-claim-desk.png)

| Student report | Expected path |
|---|---|
| `"Lost black water bottle near mess"` | `apparel` → search → release path |
| `"Something is missing from my bag"` | `unknown` → ask clarification |
| `"Lost laptop charger bag with MacBook inside"` | `high_value` → escalate security |
| Valid category, match API down | Retry, then calm failure message |

---

## Design First: Map, State, and Rules

Draw the operating map before code. Refresh the same reliability ideas, then apply them to this desk.

- **Checkpoint** — Official: saved snapshot of progress (state + position). Simple: save-game for one claim. Example: UPI payment draft you reopen after network blip.
- **Timeout** — Official: max wait before cancelling slow work. Simple: kitchen timer for one API attempt. Example: IRCTC page that stops spinning forever.
- **RetryPolicy** — Official: bounded try-again rules with backoff. Simple: knock again with longer pauses. Example: refresh exam result page twice, then stop.
- **Three-way branch** — Official: a conditional edge with more than two next nodes. Simple: one junction with three roads. Example: campus gate — visitor / staff / delivery.
- **High-value escalation** — Official: route sensitive claims away from the normal happy path to a privileged review desk. Simple: skip the queue and call security. Example: lost passport goes to the security office, not the bottle counter.

```text
START → [parse_report] → [classify_item]
                           |--(unknown)----> [ask_clarification] → END
                           |--(high_value)-> [escalate_security] → END
                           |--(normal)-----> [search_match] → [release_item] → [write_confirmation] → END
```

**Minimal shared state:** `report`, `cleaned_report`, `category`, `route`, `match_id`, `result`, `error`, `trace`

| If cleaned text contains… | Category | Route |
|---|---|---|
| `laptop`, `passport`, `aadhaar`, `wallet with cash`, `macbook` | `high_value` | `escalate_security` |
| `phone`, `earbuds`, `charger`, `pendrive` | `electronics` | `search_match` |
| `id card`, `admit`, `marksheet`, `notebook` | `documents` | `search_match` |
| `bottle`, `bag`, `jacket`, `umbrella`, `shoes` | `apparel` | `search_match` |
| none of the above | `unknown` | `ask_clarification` |

![Campus lost and found counters for electronics documents and apparel plus a security escalation desk and a clarification desk with a shared claim notebook](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session02byprofabhinandan/masterclass02-02-category-desks-three-way-branch.png)

### Activity — Predict the Path

For `"Found student's ID card near Block A library"`, write: expected `category`, expected `route`, and whether `escalate_security` runs.

**Suggested answers:** `documents` → `search_match` → No

### Setup

```bash
pip install langgraph langgraph-checkpoint-sqlite
```

---

## Build the Full Desk: Three-Way Branch, Checkpoint, Harden

One notebook flow covers three-way branching, save/resume before release, and reliability.

### Full code — campus lost & found desk end to end

```python
# Import typing helpers for shared state
from typing import TypedDict, List

# Import timeout helper from the standard library
from concurrent.futures import ThreadPoolExecutor

# Import LangGraph graph tools and markers
from langgraph.graph import StateGraph, START, END

# Import disk checkpointer for pause and resume
from langgraph.checkpoint.sqlite import SqliteSaver

# Import bounded retry rules for the match API node
from langgraph.types import RetryPolicy


# Shared notebook for one campus lost & found claim
class ClaimState(TypedDict):
    report: str  # Original student report text
    cleaned_report: str  # Normalised report text
    category: str  # electronics / documents / apparel / high_value / unknown
    route: str  # ask_clarification / escalate_security / search_match
    match_id: str  # Match id after successful search
    result: str  # Final user-facing message
    error: str  # Calm failure text when needed
    trace: List[str]  # Ordered list of visited nodes


# Mutable counter used by the flaky match API demo
ATTEMPT_BOX = {"count": 0}  # Counts API attempts across retries


# Run a function with a maximum wait time in seconds
def run_with_timeout(fn, seconds: float, *args):
    with ThreadPoolExecutor(max_workers=1) as pool:  # One worker thread
        future = pool.submit(fn, *args)  # Start the work
        return future.result(timeout=seconds)  # Wait only up to the limit


# Flaky match API: fails twice, then returns a match id
def flaky_match_api(category: str, report: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    if ATTEMPT_BOX["count"] < 3:  # First two attempts are transient failures
        raise ConnectionError("Temporary match service glitch")  # Retryable error
    return "LF-" + category[:3].upper() + "-4421"  # Success payload on attempt 3


# Always-down API used only for the exhausted-retry drill
def always_down_api(category: str, report: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    raise ConnectionError("Service unavailable")  # Never recovers in this drill


# Node 1: clean the report and start the trace
def parse_report(state: ClaimState) -> dict:
    cleaned = state["report"].strip().lower()  # Normalise spaces and case
    return {
        "cleaned_report": cleaned,  # Save cleaned text
        "error": "",  # Clear old errors at claim start
        "trace": state["trace"] + ["parse_report"],  # Record this station
    }


# Node 2: classify category and choose route label
def classify_item(state: ClaimState) -> dict:
    text = state["cleaned_report"]  # Read cleaned report
    high_value_clues = [  # High-value or sensitive items
        "laptop",
        "macbook",
        "passport",
        "aadhaar",
        "wallet with cash",
    ]
    if any(w in text for w in high_value_clues):  # Sensitive claim
        category = "high_value"  # Security must review
        route = "escalate_security"  # Jump to escalation desk
    elif any(w in text for w in ["phone", "earbuds", "charger", "pendrive"]):  # Gadgets
        category = "electronics"  # Electronics counter
        route = "search_match"  # Search register
    elif any(w in text for w in ["id card", "admit", "marksheet", "notebook"]):  # Papers
        category = "documents"  # Documents counter
        route = "search_match"  # Search register
    elif any(w in text for w in ["bottle", "bag", "jacket", "umbrella", "shoes"]):  # Soft goods
        category = "apparel"  # Apparel counter
        route = "search_match"  # Search register
    else:  # No clear keyword
        category = "unknown"  # Force clarification path
        route = "ask_clarification"  # Ask for better details
    return {
        "category": category,  # Store classification decision
        "route": route,  # Store routing decision
        "trace": state["trace"] + ["classify_item"],  # Record this station
    }


# Router: choose clarification, escalation, or search path
def route_after_classify(state: ClaimState) -> str:
    return state["route"]  # Use the route label written by classify_item


# Alternate node: ask for clearer details
def ask_clarification(state: ClaimState) -> dict:
    message = (  # Build calm guidance
        "I could not classify your lost & found report. "
        "Please mention the item type (electronics, documents, or apparel), "
        "a short description, and where you last saw it."
    )
    return {
        "result": message,  # Save guidance as final result
        "trace": state["trace"] + ["ask_clarification"],  # Record this station
    }


# Alternate node: escalate sensitive items to security
def escalate_security(state: ClaimState) -> dict:
    message = (  # Build escalation note
        "This looks like a high-value or sensitive item. "
        "Your claim file has been sent to campus security. "
        "Please visit the security desk with ID proof. Ref: SEC-"
        + state["category"].upper()
    )
    return {
        "result": message,  # Save escalation as final result
        "trace": state["trace"] + ["escalate_security"],  # Record this station
    }


# API node: search match register with per-attempt timeout
def search_match(state: ClaimState) -> dict:
    match = run_with_timeout(  # Bound one attempt's wait
        flaky_match_api,  # Flaky service
        2.0,  # Two-second timeout
        state["category"],  # Pass category
        state["cleaned_report"],  # Pass report
    )
    return {
        "match_id": match,  # Save match id
        "error": "",  # Clear error on success
        "trace": state["trace"] + ["search_match"],  # Record this station
    }


# Gate node: prepare release after a human review pause
def release_item(state: ClaimState) -> dict:
    return {
        "trace": state["trace"] + ["release_item"],  # Record release station
    }


# Final node: write confirmation or prefer error text
def write_confirmation(state: ClaimState) -> dict:
    if state["error"]:  # Prefer calm error when present
        message = state["error"]  # Show failure text
    else:  # Happy path after successful match + release
        message = (
            "Match " + state["match_id"] + " found for your "
            + state["category"] + " claim. Item ready for collection "
            "at the Lost & Found counter after ID check."
        )
    return {
        "result": message,  # Save final user message
        "trace": state["trace"] + ["write_confirmation"],  # Record this station
    }


# Helper: fresh starting notebook for one report
def fresh_state(report: str) -> dict:
    return {
        "report": report,  # Student input
        "cleaned_report": "",  # Empty before parse
        "category": "",  # Empty before classify
        "route": "",  # Empty before classify
        "match_id": "",  # Empty before search
        "result": "",  # Empty before final node
        "error": "",  # No error yet
        "trace": [],  # Fresh trace
    }


# Assemble the full desk map
builder = StateGraph(ClaimState)  # Create graph shell
builder.add_node("parse_report", parse_report)  # Register parse
builder.add_node("classify_item", classify_item)  # Register classify
builder.add_node("ask_clarification", ask_clarification)  # Register clarification
builder.add_node("escalate_security", escalate_security)  # Register escalation
builder.add_node(  # Register search with bounded retries
    "search_match",
    search_match,
    retry_policy=RetryPolicy(  # House rules for try-again
        max_attempts=3,  # Stop after 3 tries
        initial_interval=0.2,  # Short first wait
        backoff_factor=2.0,  # Grow wait after each failure
        max_interval=2.0,  # Cap wait growth
        jitter=False,  # Keep timing predictable for learning
    ),
)
builder.add_node("release_item", release_item)  # Register release gate
builder.add_node("write_confirmation", write_confirmation)  # Register confirm
builder.add_edge(START, "parse_report")  # Always start at parse
builder.add_edge("parse_report", "classify_item")  # Then classify
builder.add_conditional_edges(  # Three-way branch after classification
    "classify_item",
    route_after_classify,
    {
        "ask_clarification": "ask_clarification",  # Unclear path
        "escalate_security": "escalate_security",  # High-value path
        "search_match": "search_match",  # Normal search path
    },
)
builder.add_edge("ask_clarification", END)  # Clarification ends
builder.add_edge("escalate_security", END)  # Escalation ends
builder.add_edge("search_match", "release_item")  # Search continues to release
builder.add_edge("release_item", "write_confirmation")  # Release continues
builder.add_edge("write_confirmation", END)  # Confirm ends


# Demo 1 — Path proof: search branch vs clarification vs escalation
plain_graph = builder.compile()  # Compile without checkpointer
ATTEMPT_BOX["count"] = 0  # Reset flaky counter
success = plain_graph.invoke(fresh_state("Lost black water bottle near mess"))  # Apparel case
print("SUCCESS TRACE:", success["trace"])  # Expect search + release + confirm
print("SUCCESS RESULT:", success["result"])  # Expect match confirmation
print("ATTEMPTS:", ATTEMPT_BOX["count"])  # Expect 3 because API is flaky by design

blocked = plain_graph.invoke(fresh_state("Something is missing from my bag"))  # Vague case
print("BLOCKED TRACE:", blocked["trace"])  # Expect ask_clarification only
print("BLOCKED RESULT:", blocked["result"])  # Expect guidance message

ATTEMPT_BOX["count"] = 0  # Reset before high-value path
escalated = plain_graph.invoke(
    fresh_state("Lost laptop charger bag with MacBook inside")  # High-value case
)
print("ESCALATED TRACE:", escalated["trace"])  # Expect escalate_security
print("ESCALATED RESULT:", escalated["result"])  # Expect security note


# Demo 2 — Pause before release, inspect checkpoint, resume same thread
with SqliteSaver.from_conn_string("campus_lost_found.db") as checkpointer:  # Disk cupboard
    paused_graph = builder.compile(  # Compile with save points
        checkpointer=checkpointer,  # Persist every checkpoint
        interrupt_before=["release_item"],  # Planned pause before release
    )
    config = {"configurable": {"thread_id": "claim-case-118"}}  # Claim file number
    ATTEMPT_BOX["count"] = 0  # Reset attempts for this claim
    partial = paused_graph.invoke(  # Runs parse → classify → search, then pauses
        fresh_state("Lost student ID card near Block A library"),
        config,
    )
    print("PARTIAL TRACE:", partial["trace"])  # Expect parse + classify + search
    latest = paused_graph.get_state(config)  # Read latest checkpoint payload
    print("SAVED CATEGORY:", latest.values.get("category"))  # Expect documents
    print("SAVED MATCH:", latest.values.get("match_id"))  # Expect LF-DOC-4421 style id
    print("WAITING TO RUN:", latest.next)  # Expect release_item pending
    print("CHECKPOINT COUNT:", len(list(paused_graph.get_state_history(config))))  # List saves
    # Human review moment: desk staff verifies ID, then resumes the same thread
    resumed = paused_graph.invoke(None, config)  # Resume same thread_id
    print("RESUMED TRACE:", resumed["trace"])  # Expect release + confirm added
    print("RESUMED RESULT:", resumed["result"])  # Expect collection confirmation


# Demo 3 — Exhausted retries become a calm user-facing error
down_builder = StateGraph(ClaimState)  # Small failure-focused graph


def search_match_down(state: ClaimState) -> dict:
    match = run_with_timeout(  # Always fails inside timeout wrapper
        always_down_api,
        1.0,
        state["category"],
        state["cleaned_report"],
    )
    return {
        "match_id": match,  # Unreachable while down
        "trace": state["trace"] + ["search_match"],  # Would record station
        "error": "",  # Would clear error on success
    }


down_builder.add_node(  # API node with the same retry budget
    "search_match",
    search_match_down,
    retry_policy=RetryPolicy(  # House rules for try-again
        max_attempts=3,  # Stop after 3 tries
        initial_interval=0.1,  # Short first wait
        backoff_factor=2.0,  # Grow wait after each failure
        jitter=False,  # Keep timing predictable for learning
    ),
)
down_builder.add_edge(START, "search_match")  # Start at API node
down_builder.add_edge("search_match", END)  # End after API node
down_graph = down_builder.compile()  # Compile failure drill
ATTEMPT_BOX["count"] = 0  # Reset counter

try:  # Catch exhausted retries at the call site
    down_graph.invoke(
        {
            "report": "Lost phone near canteen",  # Original text
            "cleaned_report": "lost phone near canteen",  # Already cleaned for this drill
            "category": "electronics",  # Known category so search would be valid
            "route": "search_match",  # Route label for consistency
            "match_id": "",  # Empty before success
            "result": "",  # Empty before final message
            "error": "",  # Empty before failure handling
            "trace": [],  # Fresh trace
        }
    )
except Exception:  # Translate technical failure into desk language
    user_facing = (
        "We could not search the Lost & Found register after 3 attempts "
        "because the match service is unavailable. Please try again after some time, "
        "or visit the Lost & Found counter with this note: MATCH-SERVICE-DOWN."
    )
    print("USER-FACING ERROR:", user_facing)  # What the student should see
    print("INTERNAL ATTEMPTS:", ATTEMPT_BOX["count"])  # Proof retries happened
```

### How the code works

- `classify_item` writes both `category` and `route`; `route_after_classify` creates a **visible three-way branch**
- Unclear reports stop at **ask_clarification**; sensitive items stop at **escalate_security**; normal items go to **search_match**
- `RetryPolicy` retries transient `ConnectionError` with **backoff**; `run_with_timeout` bounds each attempt
- `interrupt_before=["release_item"]` plus `SqliteSaver` saves the claim after a match; `invoke(None, config)` resumes the same **thread ID** after human review

![Lost and found claim file paused at a human review gate with progress saved before the Release Item stamp so the same claim can resume later](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session02byprofabhinandan/masterclass02-03-checkpoint-pause-before-release.png)

- When retries are exhausted, `try/except` around `invoke` produces a calm **user-facing error**, not a stack trace

![Lost and found match machine succeeding after bounded retries with growing waits, contrasted with a scary technical error versus a calm visit-the-counter message](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/masterclass/session02byprofabhinandan/masterclass02-04-retry-and-calm-error.png)

- `trace` proves which stations ran on success, blocked, escalated, pause, and resume paths

**Common mistakes:** Changing `thread_id` on resume opens a different claim file. Do not release high-value items through the normal search path. Do not show raw `ConnectionError` text to claimants.

---

## Why This Desk Is Different From a Ticket Desk

The hostel ticket desk had **two roads** after classify: clarify or create. This lost & found desk adds a third road for **high-value escalation**, and the planned pause sits **after** the API call (before release), not before it.

- Ticket pattern: pause before a write that creates an external record
- Claim pattern: search first, then pause before **handing over** a physical item
- Same LangGraph tools — different operating map for a different campus job

### Activity — Compare the Maps
Write one sentence: *In a lost & found desk, the checkpoint before release protects…*

**Suggested answer:** It protects against releasing an item before staff verify the claimant’s identity.

---

## Student Practice

### Activity — Run Your Own Report
Invoke the path-proof demo with your own one-line lost-item report. Record `category`, `route`, `trace`, and a short paraphrase of `result`.

### Activity — Checkpoint Detective
After the partial pause in the checkpoint demo, write one sentence: *This claim is ready / not ready to release because…*

### Activity — Reliability Checklist

| # | Check | Done? |
|---|---|---|
| 1 | Match API node has a timeout | |
| 2 | Retries are bounded (`max_attempts`) | |
| 3 | Backoff is enabled | |
| 4 | Unclear reports go to clarification | |
| 5 | High-value reports go to security escalation | |
| 6 | Exhausted retries show a clear next step | |
| 7 | You can explain `trace` for success, blocked, and escalated paths | |

### Activity — Execution Walkthrough
Fill this table once for the bottle report and once for the MacBook report:

| Step order | Node name | Important state after node | Why control moved next |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

If the result looks wrong, decide whether the bug is in a **node**, a **transition**, or a **state field**.

### Activity — Design a Sibling Desk
On paper only, sketch three nodes and one branch for a **campus mess feedback desk** (quality vs hygiene vs unclear). Map and minimal state only — no code yet.

---

## Key Takeaways

- Model the claim desk as **nodes**, a **three-way conditional path**, and **minimal shared state**.
- **Checkpoints** pause before item release and resume with a stable **thread ID** after human review.
- **Timeouts** and **RetryPolicy** protect flaky match APIs; exhausted retries need calm **user-facing errors**.
- Prove every run with a **`trace`** and a short **execution walkthrough**.
- The same LangGraph habits transfer across campus products when the operating map is drawn first.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **LangGraph** | Framework for stateful multi-step workflows as graphs |
| **Node / Conditional edge** | Station of work / branch chosen by a router |
| **Three-way branch** | One classify junction with three next desks |
| **Graph state / `trace`** | Shared notebook / ordered proof of node visits |
| **`StateGraph` / `compile()` / `invoke()`** | Build, freeze, and run the workflow |
| **`interrupt_before`** | Planned pause before a named node (here: release) |
| **`SqliteSaver` / `thread_id`** | Disk checkpoints grouped by claim file number |
| **`get_state` / `get_state_history`** | Inspect latest save and checkpoint trail |
| **`invoke(None, config)`** | Resume from the latest checkpoint |
| **Timeout / `RetryPolicy` / backoff** | Max wait per attempt / bounded retries / growing wait |
| **User-facing error** | Calm next-step message after hard failure |
| **High-value escalation** | Sensitive claims routed to security instead of normal search |
| **`pip install langgraph langgraph-checkpoint-sqlite`** | Packages used in this hands-on |
