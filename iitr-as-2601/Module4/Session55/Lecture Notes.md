# LangGraph Advanced: Timeouts and Retries

## Introduction

In the **previous** session you added **checkpoints** so a long-running LangGraph flow could **persist** progress, **resume** after interruption, and let you **inspect** saved payloads.

That protects a case file across stops and restarts. This session answers a different reliability question: *what if a step is too slow, or an API fails temporarily — how do we wait wisely, try again within limits, and still speak clearly to the user when we must stop?*

**What you will learn:**

- Set **timeouts** for API-backed steps (per-node pattern and a whole-run limit)
- Retry **transient** failures with **bounded attempts** and **backoff**
- Surface clear **user-facing errors** when retries are exhausted
- Document a **minimal reliability checklist** for agent development

This session does **not** re-teach checkpoint save/resume. Keep those skills separate. Here the focus is time limits, retries, and honest failure messages.

---

## When Graphs Fail in Messy Ways

A node that calls an outside service can fail for two common reasons:

| Problem | Everyday feel | What users experience |
|---|---|---|
| Step hangs too long | Phone call that never ends | Screen spins forever |
| Temporary glitch | Network blip at a ticket counter | One failure, then success if asked again |
| Hard failure after many tries | Counter permanently closed | Need a clear “please try later” message |

![Three messy failure modes at a campus help desk — endless spinning wait, temporary glitch retried successfully, and a permanently closed counter with a clear user message](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session55/session55-01-messy-failure-modes.png)

- **Official Definition:** A **timeout** is a maximum time allowed for an operation before it is cancelled as too slow.
- **In Simple Words:** A kitchen timer for one step. When it rings, stop waiting.
- **Real-Life Example:** A UPI app that stops waiting after a few seconds instead of spinning forever.

- **Official Definition:** A **retry** is running the same operation again after a failure, usually with a limit on attempts.
- **In Simple Words:** Knock again — but not 100 times.
- **Real-Life Example:** Refreshing a railway booking page once or twice when the site hiccups.

- **Official Definition:** **Backoff** means waiting longer between successive retries.
- **In Simple Words:** Pause a little, then a little more, so you do not hammer the service.
- **Real-Life Example:** If the canteen line is stuck, you wait, then wait longer before asking again — you do not shout every half second.

**Transient vs permanent failures**

| Kind | Meaning | Retry? |
|---|---|---|
| Transient | Temporary problem (network blip, brief 503) | Yes, within limits |
| Permanent | Clear hard error (bad input, forbidden) | No — fail clearly |

![Split comparison of transient network blip worth retrying versus permanent bad input that should fail fast with clear guidance](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session55/session55-02-transient-vs-permanent.png)

### Activity — Classify the Failure

| Situation | Transient or permanent? | Timeout, retry, or clear error? |
|---|---|---|
| API returns “service busy, try later” | | |
| User typed an empty request | | |
| API hangs with no response for 60 seconds | | |

**Suggested answers:** transient → retry; permanent → clear error; hang → timeout (then maybe retry if your policy allows)

---

## Setup

```bash
pip install langgraph
```

You will use:

- LangGraph **`RetryPolicy`** on a node for bounded retries with backoff
- A small **timeout wrapper** for per-node time limits
- A **global** timeout around `invoke` for the whole run
- Plain Python functions that simulate flaky / slow APIs (no mocking frameworks)

---

## Per-Node Timeout for an API-Backed Step

LangGraph nodes are ordinary functions. For an API-backed step, wrap the slow work with a time limit.

- **Official Definition:** A **per-node timeout** limits how long one node may wait before failing that step.
- **In Simple Words:** Each station has its own kitchen timer.
- **Real-Life Example:** Document verification desk: if the scanner does not respond in 10 seconds, the clerk stops and reports a scanner delay — they do not block the whole office endlessly.

![Metro-style workflow showing per-node kitchen timers at each station versus one large clock limiting the entire journey from start to finish](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session55/session55-03-per-node-vs-global-timeout.png)

### Full code — per-node timeout wrapper

```python
# Import typing helpers for state
from typing import TypedDict, List

# Import timeout support from the standard library
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout

# Import LangGraph builder tools
from langgraph.graph import StateGraph, START, END


# Shared notebook for a tiny campus status workflow
class StatusState(TypedDict):
    request: str  # User request text
    api_status: str  # Raw status from the simulated API
    result: str  # Final user-facing message
    trace: List[str]  # Nodes visited
    error: str  # Clear error text when something fails


# Simulated slow API call (stands in for a real HTTP request)
def fake_status_api(request_text: str) -> str:
    import time  # Local import to keep the demo self-contained
    time.sleep(3)  # Pretend the remote API is slow
    return "OPEN"  # Demo status payload


# Run a function with a maximum wait time in seconds
def run_with_timeout(fn, seconds: float, *args):
    with ThreadPoolExecutor(max_workers=1) as pool:  # One worker thread
        future = pool.submit(fn, *args)  # Start the work
        return future.result(timeout=seconds)  # Wait only up to the limit


# Node 1: prepare the request
def understand_request(state: StatusState) -> dict:
    cleaned = state["request"].strip()  # Clean spaces
    return {
        "request": cleaned,  # Store cleaned request
        "trace": state["trace"] + ["understand_request"],  # Log node
        "error": "",  # Clear old errors at the start
    }


# Node 2: API-backed step with a SHORT timeout (will fail in this demo)
def fetch_status(state: StatusState) -> dict:
    try:  # Attempt the timed API call
        status = run_with_timeout(fake_status_api, 1.0, state["request"])  # 1 second limit
        return {
            "api_status": status,  # Save API payload
            "trace": state["trace"] + ["fetch_status"],  # Log success path
            "error": "",  # No error
        }
    except FuturesTimeout:  # Timer rang before the API finished
        return {
            "api_status": "",  # No useful payload
            "trace": state["trace"] + ["fetch_status"],  # Still record the attempt
            "error": "Status service took too long. Please try again in a minute.",  # User-facing timeout message
        }


# Node 3: turn state into a final message
def write_result(state: StatusState) -> dict:
    if state["error"]:  # Prefer clear error if present
        message = state["error"]  # Show the timeout (or other) error
    elif state["api_status"]:  # Happy path
        message = "Campus desk status: " + state["api_status"]  # Show status
    else:  # Unexpected empty path
        message = "Could not read campus desk status."  # Fallback text
    return {
        "result": message,  # Final message
        "trace": state["trace"] + ["write_result"],  # Log node
    }


# Build the graph
builder = StateGraph(StatusState)  # Shell
builder.add_node("understand_request", understand_request)  # Node 1
builder.add_node("fetch_status", fetch_status)  # Timed API node
builder.add_node("write_result", write_result)  # Final message node
builder.add_edge(START, "understand_request")  # Wire
builder.add_edge("understand_request", "fetch_status")  # Wire
builder.add_edge("fetch_status", "write_result")  # Wire
builder.add_edge("write_result", END)  # Wire

# Compile and run
graph = builder.compile()
final_state = graph.invoke(
    {
        "request": "Is the scholarship desk open?",  # User goal
        "api_status": "",  # Empty before API
        "result": "",  # Empty before final node
        "trace": [],  # Fresh trace
        "error": "",  # No error yet
    }
)

print("TRACE:", final_state["trace"])  # Show path
print("ERROR:", final_state["error"])  # Expect timeout message
print("RESULT:", final_state["result"])  # User-facing text
```

### How the code works

- `fake_status_api` sleeps 3 seconds to simulate a slow remote call
- `run_with_timeout(..., 1.0, ...)` allows only 1 second
- When the timer rings, the node catches `FuturesTimeout` and writes a **clear error** into state
- The final node prefers `error` over a fake success message

**Common mistake:** Raising a raw exception and showing a stack trace to end users. Prefer a short, calm sentence in an `error` or `result` field.

### Activity — Tune the Timer

Change the timeout from `1.0` to `5.0` and run again.

| Timeout used | Did fetch succeed? | Final `result` (short paraphrase) |
|---|---|---|
| 1.0 second | | |
| 5.0 seconds | | |

---

## Global Timeout Around the Whole Run

Sometimes you also want a limit for the **entire** graph invoke, not only one node.

- **Official Definition:** A **global timeout** limits the total time for one full graph run.
- **In Simple Words:** One timer for the whole journey, not only one station.
- **Real-Life Example:** An exam has a total duration even if each question also has a suggested time.

### Full code — global timeout helper

```python
# Import timeout tools
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout

# Import the compiled graph object from your module OR rebuild a tiny graph below
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END


# Tiny state for the global-timeout demo
class TinyState(TypedDict):
    value: int  # Simple counter value
    trace: List[str]  # Trace list


# A deliberately slow node
def slow_step(state: TinyState) -> dict:
    import time  # Local import for the demo
    time.sleep(2)  # Slow work
    return {
        "value": state["value"] + 1,  # Update value
        "trace": state["trace"] + ["slow_step"],  # Log node
    }


# Build a one-node graph
builder = StateGraph(TinyState)  # Shell
builder.add_node("slow_step", slow_step)  # Only node
builder.add_edge(START, "slow_step")  # Start
builder.add_edge("slow_step", END)  # End
graph = builder.compile()  # Compile


# Run any invoke with a maximum total wait
def invoke_with_global_timeout(graph_obj, state: dict, seconds: float) -> dict:
    with ThreadPoolExecutor(max_workers=1) as pool:  # Worker pool
        future = pool.submit(graph_obj.invoke, state)  # Start full run
        return future.result(timeout=seconds)  # Enforce global limit


# Attempt with a timeout that is too small
try:  # Catch global timeout for a user-facing message
    result = invoke_with_global_timeout(
        graph,  # Graph to run
        {"value": 0, "trace": []},  # Start state
        0.5,  # Global limit too short for sleep(2)
    )
    print("UNEXPECTED SUCCESS:", result)  # Should not happen in this demo
except FuturesTimeout:  # Whole run exceeded the limit
    user_message = (
        "Sorry — this request timed out before completion. "
        "Please try again in a little while."
    )  # Calm user-facing error
    print("USER MESSAGE:", user_message)  # Show what you would display
```

### How the code works

- The helper wraps `graph.invoke` with one timer for the full run
- If the timer rings, you catch the timeout and convert it into a polite user message
- Use global limits for overall UX; use per-node limits to pinpoint which station was slow

**Design tip:** If both exist, choose clear ownership. Example: per-node 8s for API fetch, global 20s for the whole journey.

---

## Retry Transient API Failures with Bounded Attempts and Backoff

Timeouts stop endless waiting. Retries handle temporary failure.

LangGraph supports a **`RetryPolicy`** on a node.

- **Official Definition:** A **retry policy** defines how many times to retry, how long to wait between attempts, and how wait time grows (backoff).
- **In Simple Words:** House rules for “try again” — count, pause, and stop.
- **Real-Life Example:** Calling a customer-care line: try up to 3 times, wait longer between calls, then give a reference number and stop.

![Campus ticket counter retrying a flaky service with bounded attempts and growing pause gaps between tries until success on the third attempt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session55/session55-04-retry-backoff-policy.png)

### Full code — RetryPolicy on a flaky node

```python
# Import typing helpers
from typing import TypedDict, List

# Import LangGraph tools and retry policy
from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy


# Shared state for the retry demo
class TicketState(TypedDict):
    request: str  # User request
    ticket_id: str  # ID returned by simulated API
    attempts_seen: int  # How many times the flaky function ran
    result: str  # Final user-facing message
    error: str  # Error text if retries fail completely
    trace: List[str]  # Node visit list


# Module-level counter to simulate transient failures
ATTEMPT_BOX = {"count": 0}  # Mutable counter shared by the flaky function


# Simulated flaky API: fails twice, then succeeds
def flaky_create_ticket(request_text: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    if ATTEMPT_BOX["count"] < 3:  # First two attempts fail
        raise ConnectionError("Temporary network glitch")  # Transient failure
    return "TKT-7781"  # Success payload on third attempt


# Node that calls the flaky API
def create_ticket(state: TicketState) -> dict:
    ticket = flaky_create_ticket(state["request"])  # May raise transient errors
    return {
        "ticket_id": ticket,  # Save ticket id
        "attempts_seen": ATTEMPT_BOX["count"],  # Store how many tries happened
        "trace": state["trace"] + ["create_ticket"],  # Log node
        "error": "",  # Clear error on success
    }


# Final node writes a success message
def write_success(state: TicketState) -> dict:
    message = "Ticket created: " + state["ticket_id"]  # User-facing success
    return {
        "result": message,  # Save message
        "trace": state["trace"] + ["write_success"],  # Log node
    }


# Build graph with retry policy on the API node
builder = StateGraph(TicketState)  # Shell
builder.add_node(
    "create_ticket",  # Node name
    create_ticket,  # Node function
    retry_policy=RetryPolicy(  # Bounded retry rules
        max_attempts=3,  # Try at most 3 times
        initial_interval=0.2,  # Wait 0.2s before first retry
        backoff_factor=2.0,  # Double the wait after each failure
        max_interval=2.0,  # Do not wait more than 2s between tries
        jitter=False,  # Keep timing predictable for learning
    ),
)
builder.add_node("write_success", write_success)  # Success writer
builder.add_edge(START, "create_ticket")  # Wire
builder.add_edge("create_ticket", "write_success")  # Wire
builder.add_edge("write_success", END)  # Wire

# Reset attempt counter before the run
ATTEMPT_BOX["count"] = 0  # Fresh demo

# Compile and invoke
graph = builder.compile()
final_state = graph.invoke(
    {
        "request": "Create a hostel maintenance ticket",  # Goal
        "ticket_id": "",  # Empty before success
        "attempts_seen": 0,  # Default
        "result": "",  # Empty
        "error": "",  # Empty
        "trace": [],  # Fresh
    }
)

print("ATTEMPTS:", final_state["attempts_seen"])  # Expect 3
print("TICKET:", final_state["ticket_id"])  # Expect TKT-7781
print("RESULT:", final_state["result"])  # Success message
print("TRACE:", final_state["trace"])  # Node order
```

### How the code works

- The first two API calls raise `ConnectionError` (transient)
- `RetryPolicy(max_attempts=3, ...)` retries automatically with backoff
- The third attempt succeeds, so the graph continues to `write_success`
- `attempts_seen` helps you prove retries happened during learning

### Activity — Shrink the Budget

Set `max_attempts=2` and run again.

| `max_attempts` | Did the graph succeed? | What happened? |
|---|---|---|
| 3 | | |
| 2 | | |

With `max_attempts=2`, the node should fail after bounded retries. Next you will catch that failure and show a calm user message.

---

## Surface Clear Errors When Retries Are Exhausted

Retries must end. When the budget is finished, talk to the user like a professional desk — not like a crash log.

- **Official Definition:** A **user-facing error** is a short, actionable message meant for humans when the system cannot complete the task.
- **In Simple Words:** A polite explanation, not a stack trace.
- **Real-Life Example:** “Payment could not be completed after 3 attempts. Please try again in 10 minutes or visit the accounts desk.” 

![Contrast between showing a scary technical stack trace to a student versus a calm professional help-desk message with clear next steps after retries are exhausted](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session55/session55-05-user-facing-error.png)

### Full code — catch exhausted retries and write a calm message

When the retry budget is finished, LangGraph raises an error from `invoke`. Catch it at the call site and translate it for humans.

```python
# Import typing helpers
from typing import TypedDict, List

# Import LangGraph tools
from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy


# Minimal state for the exhaustion demo
class TicketState(TypedDict):
    request: str  # User request
    ticket_id: str  # Ticket id if success ever happens
    trace: List[str]  # Trace list


# Counter for the always-down API
ATTEMPT_BOX = {"count": 0}  # Shared attempt counter


# API that always fails (retries will be exhausted)
def always_down_api(request_text: str) -> str:
    ATTEMPT_BOX["count"] += 1  # Count this attempt
    raise ConnectionError("Service unavailable")  # Never recovers in this demo


# Node that calls the always-down API
def create_ticket(state: TicketState) -> dict:
    ticket = always_down_api(state["request"])  # Raises until retries end
    return {
        "ticket_id": ticket,  # Unreachable while the API stays down
        "trace": state["trace"] + ["create_ticket"],  # Would log on success
    }


# One-node graph focused on retry exhaustion
builder = StateGraph(TicketState)  # Shell
builder.add_node(
    "create_ticket",  # API node
    create_ticket,  # Function
    retry_policy=RetryPolicy(  # Bounded retries
        max_attempts=3,  # Stop after 3 tries
        initial_interval=0.1,  # Short wait for class demos
        backoff_factor=2.0,  # Exponential backoff
        jitter=False,  # Predictable timing
    ),
)
builder.add_edge(START, "create_ticket")  # Start at API node
builder.add_edge("create_ticket", END)  # End after API node

graph = builder.compile()  # Compile
ATTEMPT_BOX["count"] = 0  # Reset counter

# Invoke and convert exhausted retries into a user-facing error
try:  # Catch failure after retry budget is used
    final_state = graph.invoke(
        {
            "request": "Create a lab access ticket",  # Goal
            "ticket_id": "",  # Empty before success
            "trace": [],  # Fresh trace
        }
    )
    print("RESULT:", final_state)  # Only if somehow succeeded
except Exception:  # Retries exhausted or node failed hard
    user_facing = (
        "We could not create your ticket after 3 attempts because the service is unavailable. "
        "Please try again after some time, or visit the IT helpdesk with this note: TICKET-SERVICE-DOWN."
    )  # Clear, actionable message
    print("USER-FACING ERROR:", user_facing)  # What you show in the product
    print("INTERNAL ATTEMPTS:", ATTEMPT_BOX["count"])  # Proof retries happened
```

### How the code works

- The API never recovers, so retries run until `max_attempts`
- After the budget is used, `invoke` fails with a technical exception
- The `try/except` around `invoke` converts that failure into a calm user-facing message
- The message says **what failed**, **that retries were tried**, and **what to do next**

### Good user-facing error ingredients

- What the user asked for (ticket / status / booking)
- That the system already retried (when true)
- A next action (try later / visit desk / contact support)
- No raw traceback, no secret tokens, no scary internal jargon

### Activity — Rewrite the Message

Rewrite this bad message into a good user-facing error:

`ConnectionError: Service unavailable`

Your version:

> 

**Suggested style:** short, calm, next step included.

---

## Minimal Reliability Checklist for Agent Development

Use this checklist when you harden an agent graph during development. Stay practical. You do not need a mocking framework for these checks.

### Reliability checklist

| # | Check | Done? (Yes/No) | Notes |
|---|---|---|---|
| 1 | Every API-backed node has a **timeout** that fits the step | | |
| 2 | The full `invoke` has a sensible **global** time limit for UX | | |
| 3 | Retries are **bounded** (`max_attempts` set on purpose) | | |
| 4 | Backoff is enabled so retries do not hammer the service | | |
| 5 | Only **transient** errors are retried; bad input fails fast | | |
| 6 | Exhausted retries produce a **clear user-facing message** | | |
| 7 | Logs/traces keep technical detail; users see calm language | | |
| 8 | You ran one **slow** demo and one **flaky** demo before calling it done | | |

### Activity — Score Your Graph

Pick one graph from this session (timeout demo or retry demo). Fill the checklist table above. Aim for honest “No” marks — they tell you what to fix next.

---

## How This Fits with Checkpoint Skills

Keep the skills independent in your mind:

| Skill family | Question it answers |
|---|---|
| Graph basics | What are the stations, paths, and notebook fields? |
| Checkpoints and resume | Can we save mid-way and continue the same case later? |
| Timeouts and retries | Can we stop waiting, retry temporary glitches, and fail clearly? |

You can combine them later in larger systems. For this session, practise timeouts, retries, and clear errors until they feel natural on their own.

---

## Key Takeaways

- **Timeouts** protect users from endless waits — use per-node timers for API steps and a global limit for the whole run when needed.
- **RetryPolicy** handles transient failures with **bounded attempts** and **backoff**.
- When retries are exhausted, convert technical exceptions into **calm, actionable user-facing errors**.
- A **minimal reliability checklist** keeps development honest without heavy mocking frameworks.
- Treat reliability controls as a separate layer from workflow mapping and checkpoint save/resume.

These habits prepare you to demonstrate agent systems that fail gracefully in development and explain themselves clearly when something goes wrong.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **Timeout** | Maximum wait before cancelling slow work |
| **Per-node timeout** | Time limit applied inside one node |
| **Global timeout** | Time limit around a full `invoke` |
| **Retry** | Running the same step again after failure |
| **Retry policy** | Rules for attempts, wait, and backoff |
| **Backoff** | Increasing wait between retries |
| **Transient failure** | Temporary error worth retrying |
| **User-facing error** | Short human message after hard stop |
| **`RetryPolicy`** | LangGraph helper for node retries |
| **`max_attempts`** | Upper bound on tries |
| **`initial_interval`** | First wait before a retry |
| **`backoff_factor`** | Multiplier for wait growth |
| **`ThreadPoolExecutor` / `FuturesTimeout`** | Standard-library timeout tools used here |
| **Reliability checklist** | Short verification list for agent hardening |
| **`pip install langgraph`** | Install command for this session |
| **Checkpoints (previous idea)** | Save/resume progress — complementary, not replaced here |
