# LangGraph Basics

## Introduction

In the **previous** session you refreshed **agent communication**, then built **MasaiMato** — a mini restaurant MCP server where an AI model discovered the menu and placed food orders through MCP tools.

That gave you structured handoffs and a portable tool connection pattern. This session asks the next design question: how do you draw an agent workflow as a **map**, keep a **shared notebook** across steps, and then **run** a small version while tracing what changed after each step?

**What you will learn:**

- Draw an agent workflow as **nodes** (steps) and **transitions** (paths or conditions)
- Define **minimal graph state** shared across nodes
- Build and run a simple **two- to three-node** graph for a bounded task
- Trace **execution order** and read **state updates** after each node

By the end, you should treat orchestration less like one long prompt and more like a small, visible operating map for a task.

---

## From a Step List to a Workflow Graph

A sticky-note list of steps is useful. It is not enough when you must explain *what ran*, *why control moved*, and *what information changed*.

- **Official Definition:** A **workflow graph** models a process as steps (**nodes**) connected by paths (**edges / transitions**), often with shared data (**state**).
- **In Simple Words:** It is a flowchart your program can actually follow.
- **Real-Life Example:** A hospital front desk does not only keep a to-do list for “check record → find slot → confirm.” It needs a map of stations, clear handoffs, and a file that travels with the patient request.

Without a graph view, even a good tool-connected agent design can feel invisible during a run.

Ask yourself these four questions while a workflow is running:

- Which step is running now?
- Why did control move to this next step?
- What information was updated before the next step began?
- Where did the flow finish?

**LangGraph** helps you build and run that map for agent workflows.

![Workflow graph as a metro map with stations for understand, check, and confirm, plus a shared travel card that carries request, slot, and result across the journey](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session53/session53-01-workflow-graph-metro-map.png)

- **Official Definition:** **LangGraph** is a framework for building stateful, multi-step agent workflows as graphs (nodes, edges, and shared state).
- **In Simple Words:** It is a toolkit for turning your flowchart into runnable code.
- **Real-Life Example:** Think of a city metro map published for passengers — stations, tracks, and a travel card that updates at each stop — instead of shouting directions in a crowded lobby.

**Orchestration** is the habit of making sure the right step runs at the right time with the right shared context.

- **Official Definition:** **Orchestration** is coordinated control of multi-step work so each step runs in the correct order with shared context.
- **In Simple Words:** A stage manager for your workflow.
- **Real-Life Example:** In a railway control room, signals decide which train moves next. The control room does not replace the trains; it coordinates them.

---

## Nodes: The Stations of Work

Before writing code, name the stations. Each node should do **one bounded job**.

![Campus help-desk stations showing three separate desks — understand request, check rules, and prepare outcome — each with one clear job along a shared pathway](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session53/session53-02-nodes-as-stations.png)

- **Official Definition:** A **node** is a unit of work in the graph — usually a function that reads state, does one task, and returns state updates.
- **In Simple Words:** A station on the journey. One clear job per station.
- **Real-Life Example:** In a bank onboarding desk, “check KYC documents” is one station. “Write the status note” is another. Mixing both into one messy desk makes audits harder.

### Good node design habits

- Give each node a **verb + object** name: `understand_request`, `check_slot`, `write_confirmation`
- Keep the job **small** enough to explain in one sentence
- Prefer **clear outputs** written into state, not silent side effects
- Avoid stuffing five decisions into one node just to look “smart”

### Common doubt

Students often ask: “Should every tiny detail be its own node?”

No. If two lines of cleanup always happen together and never branch, they can stay inside one node. Split a node when:

- a **condition** may send control on different paths, or
- you need to **debug / explain** that step separately

### Activity — Name the Nodes

A campus help desk gets this request: *“I need a library late-fee waiver letter for last month.”*

Write **three node names** for a simple graph. Use verb + object style. Then sketch arrows between them on paper.

| Step idea | Your node name |
|---|---|
| Clean and capture the request | |
| Check if waiver rules allow it | |
| Prepare final message / blocked reason | |

**Suggested answers:** `understand_request`, `check_waiver_rules`, `prepare_outcome`

**Quick check:** If a friend cannot read your three names and guess the story, rename the nodes until the story is obvious.

---

## Transitions: How Control Moves

Nodes alone are not a workflow. You also need paths between them.

- **Official Definition:** A **transition** (edge) is the connection that moves execution from one node to another. It may be **unconditional** or **conditional**.
- **In Simple Words:** The track between stations. Sometimes the train always goes next; sometimes a rule decides the next station.
- **Real-Life Example:** After document check at a passport office, if papers are complete you go to biometrics; if not, you go back to the help counter.

### Two kinds of transitions

![Side-by-side comparison of an unconditional straight track from A to B versus a conditional fork after a check that routes to confirm or need more info](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session53/session53-03-unconditional-vs-conditional.png)

| Type | Meaning | When to use |
|---|---|---|
| **Unconditional** | Always go from A to B | Fixed pipeline: understand → check → confirm |
| **Conditional** | Choose next node based on a rule | Branching: if slot found → confirm; else → ask_more_info |

### Diagram first (paper before code)

Draw the workflow on paper or in a text diagram before you open the editor.

```text
START
  |
  v
[understand_request]
  |
  v
[check_availability] ----(slot missing)----> [need_more_info] --> END
  |
  +(slot found)
  v
[confirm_booking] --> END
```

This diagram is your contract with yourself. If you cannot draw it, the code will also feel confusing.

### Activity — Label the Transitions

For each case, write **unconditional** or **conditional**.

| Case | Transition type |
|---|---|
| Always run `summarise` after `transcribe` | |
| If payment succeeded go to `receipt`, else go to `request_new_payment` | |
| Always end after `send_confirmation` | |

**Suggested answers:** unconditional, conditional, unconditional

---

## Graph State: The Shared Notebook

Now that you have stations and tracks, you need one shared file that travels with the run.

![Shared travel card updating at three stations — cleaned request, slot found with time, then booking confirmed — showing one notebook moving through the whole graph](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session53/session53-04-shared-state-travel-card.png)

- **Official Definition:** **Graph state** is the shared data structure passed through the graph. Each node can read it and return updates.
- **In Simple Words:** One common notebook for the whole journey — not a private diary in each node.
- **Real-Life Example:** A metro **travel card** updates at each station: entry point, current stop, destination, delay note. Every station reads the same card. No station invents a private journey other stations cannot see.

### Minimal state mindset

Beginners often write impressive node logic and forget state design. Professionals design **minimal state** first.

| If state is… | What goes wrong |
|---|---|
| Too empty | Later nodes guess or invent missing fields |
| Too crowded | Every node gets confused by unused details |
| Just enough | Each node finds what it needs and writes clear updates |

Pack state like a small office file for a meeting: only the papers the next person needs.

### Example minimal state for an appointment helper

| Field | Purpose |
|---|---|
| `request` | Original user goal in plain text |
| `slot_found` | Whether a valid slot exists (`True` / `False`) |
| `appointment_time` | Chosen time if available |
| `result` | Final message or blocked reason |
| `trace` | Short list of which nodes ran (helps learning and debugging) |

You do **not** need twenty fields for a first graph. Start small. Add a field only when a node truly needs it.

### Activity — Design Minimal State

For a mess refund request workflow, tick **keep** or **drop** for each candidate field.

| Candidate field | Keep or drop? | Why (one line) |
|---|---|---|
| `student_message` | | |
| `favourite_food` | | |
| `refund_allowed` | | |
| `final_reply` | | |
| `weather_today` | | |

**Suggested answers:** keep, drop, keep, keep, drop

---

## Setup for a Simple LangGraph Lab

This session uses a **small local graph** with plain Python node functions. You do not need an LLM API key for the first build. The goal is to understand nodes, edges, state, and tracing.

### Install

```bash
pip install langgraph
```

### Mental model of the build steps

1. Define **state** (the notebook shape)
2. Write **node functions** (each returns updates)
3. Create a **StateGraph** and add nodes
4. Add **edges** (transitions)
5. **Compile** the graph
6. **Invoke** with starting state
7. **Read** final state and the trace

If any of these steps is missing, the graph either will not run or you will not understand the run.

---

## Build a Three-Node Graph (Bounded Task)

We will model a tiny campus appointment helper:

1. **understand_request** — clean the request text
2. **check_availability** — decide if a slot exists (simple rule, no database)
3. **confirm_outcome** — write a final success or blocked message

This is intentionally small. Small graphs force clear design.

### Full code — three-node linear graph with a trace

```python
# Import TypedDict so we can describe the shape of shared state
from typing import TypedDict, List

# Import LangGraph building blocks for a runnable workflow graph
from langgraph.graph import StateGraph, START, END


# Define the shared notebook fields for this graph
class AppointmentState(TypedDict):
    request: str  # Original user request text
    cleaned_request: str  # Cleaned version after the first node
    slot_found: bool  # Whether a simple availability rule passed
    appointment_time: str  # Chosen time if a slot was found
    result: str  # Final message shown to the user
    trace: List[str]  # Ordered list of node names that already ran


# Node 1: understand the request and start the trace
def understand_request(state: AppointmentState) -> dict:
    raw = state["request"]  # Read the original request from shared state
    cleaned = raw.strip().lower()  # Clean spaces and standardise case
    return {
        "cleaned_request": cleaned,  # Save cleaned text for later nodes
        "trace": state["trace"] + ["understand_request"],  # Record that this node ran
    }


# Node 2: apply a tiny availability rule (demo logic, not a real calendar)
def check_availability(state: AppointmentState) -> dict:
    text = state["cleaned_request"]  # Use the cleaned request from Node 1
    # Demo rule: if the user mentioned "next week", treat a slot as available
    if "next week" in text:
        return {
            "slot_found": True,  # Mark that a slot exists
            "appointment_time": "Tuesday 11:00 AM",  # Store a demo time
            "trace": state["trace"] + ["check_availability"],  # Extend the run trace
        }
    # Otherwise mark as not found and leave appointment_time empty
    return {
        "slot_found": False,  # No valid slot under this demo rule
        "appointment_time": "",  # Keep time blank when blocked
        "trace": state["trace"] + ["check_availability"],  # Still record the node visit
    }


# Node 3: write the final outcome message into state
def confirm_outcome(state: AppointmentState) -> dict:
    if state["slot_found"]:  # Choose success text when a slot exists
        message = (  # Build the confirmation sentence in parts
            "Booking confirmed for "  # Start of success message
            + state["appointment_time"]  # Insert the chosen demo time
            + ". Confirmation will be sent."  # End of success message
        )
    else:  # Choose blocked text when no slot exists
        message = (  # Build the blocked guidance sentence in parts
            "No suitable slot found for this request. "  # Explain the block
            "Please suggest another week or contact the desk."  # Tell the user what to do next
        )
    return {  # Return only the fields this node updates
        "result": message,  # Save the final reply
        "trace": state["trace"] + ["confirm_outcome"],  # Complete the execution trace
    }


# Create an empty graph that uses AppointmentState as the shared notebook
builder = StateGraph(AppointmentState)

# Register each station (node) with a name and a function
builder.add_node("understand_request", understand_request)  # Add station 1
builder.add_node("check_availability", check_availability)  # Add station 2
builder.add_node("confirm_outcome", confirm_outcome)  # Add station 3

# Connect START -> understand -> check -> confirm -> END (unconditional path)
builder.add_edge(START, "understand_request")  # Journey always begins at understand
builder.add_edge("understand_request", "check_availability")  # Then always go to check
builder.add_edge("check_availability", "confirm_outcome")  # Then always go to confirm
builder.add_edge("confirm_outcome", END)  # Then finish the graph

# Compile turns the design into a runnable graph object
graph = builder.compile()

# Starting notebook values before any node runs
initial_state = {
    "request": "I need a follow-up visit next week with the same doctor.",  # Input goal
    "cleaned_request": "",  # Empty before Node 1 fills it
    "slot_found": False,  # Default flag before Node 2 decides
    "appointment_time": "",  # Empty before a slot is chosen
    "result": "",  # Empty before Node 3 writes the reply
    "trace": [],  # Empty list before any node appends its name
}

# Run the full graph once and capture the final state
final_state = graph.invoke(initial_state)

# Print key fields so you can inspect the journey
print("TRACE:", final_state["trace"])  # Show execution order
print("SLOT FOUND:", final_state["slot_found"])  # Show availability decision
print("TIME:", final_state["appointment_time"])  # Show chosen time if any
print("RESULT:", final_state["result"])  # Show final user-facing message
```

### How the code works

- `AppointmentState` defines the **minimal shared notebook** every node can read and update
- Each node function returns a **dictionary of updates**, not a mysterious global variable
- `StateGraph` is the builder that holds nodes and edges
- `START` and `END` mark where the journey begins and finishes
- `compile()` freezes the map into something you can `invoke`
- `invoke(initial_state)` runs the nodes in order and returns the **final state**
- The `trace` field is a learning tool: after the run, you can prove which stations were visited and in what order

### Expected output idea (success case)

Because the request contains `"next week"`, the demo rule finds a slot:

- `TRACE` should list `understand_request` → `check_availability` → `confirm_outcome`
- `SLOT FOUND` should be `True`
- `RESULT` should mention the demo appointment time

### Activity — Run the Blocked Path

Change only the starting `request` to:

`"I need a follow-up visit tomorrow morning."`

Run the same graph again and fill this table:

| Field after run | Your observed value |
|---|---|
| `trace` | |
| `slot_found` | |
| `appointment_time` | |
| `result` (short paraphrase) | |

You should see `slot_found = False` and a blocked-style `result`, while the **same three nodes** still run in order.

---

## Add One Conditional Transition

A linear graph always visits the same stations. Real workflows often branch.

We will add a fourth node, `need_more_info`, and route after `check_availability`:

- if `slot_found` is `True` → go to `confirm_outcome`
- if `slot_found` is `False` → go to `need_more_info`

### Full code — conditional routing after availability check

```python
# Import typing helpers for state definition
from typing import TypedDict, List

# Import LangGraph graph tools and END marker
from langgraph.graph import StateGraph, START, END


# Shared notebook for the branching appointment workflow
class AppointmentState(TypedDict):
    request: str  # Raw user request
    cleaned_request: str  # Cleaned request text
    slot_found: bool  # Availability decision flag
    appointment_time: str  # Demo time when available
    result: str  # Final user-facing message
    trace: List[str]  # Ordered execution record


# Clean the request and start the trace
def understand_request(state: AppointmentState) -> dict:
    cleaned = state["request"].strip().lower()  # Normalise the request text
    return {
        "cleaned_request": cleaned,  # Store cleaned text
        "trace": state["trace"] + ["understand_request"],  # Log this node
    }


# Decide availability with the same simple demo rule
def check_availability(state: AppointmentState) -> dict:
    text = state["cleaned_request"]  # Read cleaned request
    if "next week" in text:
        return {
            "slot_found": True,  # Happy path flag
            "appointment_time": "Tuesday 11:00 AM",  # Demo booking time
            "trace": state["trace"] + ["check_availability"],  # Log this node
        }
    return {
        "slot_found": False,  # Blocked path flag
        "appointment_time": "",  # No time when unavailable
        "trace": state["trace"] + ["check_availability"],  # Log this node
    }


# Success node: confirm the booking message
def confirm_outcome(state: AppointmentState) -> dict:
    message = "Booking confirmed for " + state["appointment_time"] + "."  # Success text
    return {
        "result": message,  # Save confirmation
        "trace": state["trace"] + ["confirm_outcome"],  # Log this node
    }


# Alternate node: ask for clearer timing when no slot is found
def need_more_info(state: AppointmentState) -> dict:
    message = (  # Build a clear guidance message for the blocked path
        "I could not find a matching slot. "  # Explain what failed
        "Please reply with a preferred week (for example: next week)."  # Ask for better input
    )
    return {  # Return updates for the alternate branch
        "result": message,  # Save blocked guidance
        "trace": state["trace"] + ["need_more_info"],  # Log this alternate node
    }


# Router function: choose the next node name from current state
def route_after_check(state: AppointmentState) -> str:
    if state["slot_found"]:  # Success branch condition
        return "confirm_outcome"  # Go to success station
    return "need_more_info"  # Go to clarification station


# Build the graph shell with shared state
builder = StateGraph(AppointmentState)

# Add all four stations
builder.add_node("understand_request", understand_request)  # Station 1
builder.add_node("check_availability", check_availability)  # Station 2
builder.add_node("confirm_outcome", confirm_outcome)  # Station 3 (success branch)
builder.add_node("need_more_info", need_more_info)  # Station 4 (blocked branch)

# Fixed start of the journey
builder.add_edge(START, "understand_request")  # Always start at understand
builder.add_edge("understand_request", "check_availability")  # Always move to check next

# Conditional transition: decide next node after the availability check
builder.add_conditional_edges(
    "check_availability",  # From this node
    route_after_check,  # Use this function to choose the next node name
    {
        "confirm_outcome": "confirm_outcome",  # Map success label to success node
        "need_more_info": "need_more_info",  # Map blocked label to guidance node
    },
)

# Both branches finish the graph
builder.add_edge("confirm_outcome", END)  # Success path ends here
builder.add_edge("need_more_info", END)  # Blocked path ends here

# Compile the branching workflow
graph = builder.compile()

# Try the blocked path first
blocked_start = {
    "request": "Please book a follow-up tomorrow.",  # Request without "next week"
    "cleaned_request": "",  # Empty before cleaning
    "slot_found": False,  # Default before check
    "appointment_time": "",  # Empty before decision
    "result": "",  # Empty before final node
    "trace": [],  # Fresh trace for this run
}

blocked_final = graph.invoke(blocked_start)  # Run blocked scenario
print("BLOCKED TRACE:", blocked_final["trace"])  # Expect need_more_info in the path
print("BLOCKED RESULT:", blocked_final["result"])  # Expect guidance message

# Then try the success path
success_start = {
    "request": "Please book a follow-up next week.",  # Request that passes demo rule
    "cleaned_request": "",  # Empty before cleaning
    "slot_found": False,  # Default before check
    "appointment_time": "",  # Empty before decision
    "result": "",  # Empty before final node
    "trace": [],  # Fresh trace for this run
}

success_final = graph.invoke(success_start)  # Run success scenario
print("SUCCESS TRACE:", success_final["trace"])  # Expect confirm_outcome in the path
print("SUCCESS RESULT:", success_final["result"])  # Expect confirmation message
```

### How the code works

- `route_after_check` reads state and returns the **name of the next node**
- `add_conditional_edges` wires that router into the graph
- The blocked request never visits `confirm_outcome`
- The success request never visits `need_more_info`
- Your `trace` field becomes the proof of which branch ran

This is the same idea as stop conditions from the previous pattern work — but now the branch is visible on the graph map.

### Activity — Predict Before You Run

Without running code, predict the `trace` for this request:

`"Can I get an appointment next week afternoon?"`

Write your prediction:

| Prediction field | Your guess |
|---|---|
| Nodes in `trace` (in order) | |
| Final `result` style (confirm / ask more info) | |

Then run it and compare. Prediction before execution builds professional debugging habits.

---

## Execution Walkthrough: Read State Like an Operations Lead

Building the graph is only half the skill. The other half is **tracing**.

- **Official Definition:** An **execution walkthrough** is a step-by-step review of node order and state changes for one complete run.
- **In Simple Words:** Replay the journey and explain what the notebook contained after each stop.
- **Real-Life Example:** After a failed courier delivery, ops does not only say “it failed.” They check: scanned at hub? left warehouse? wrong address flag set?

### Walkthrough template (use for every graph run)

Copy this table and fill it after each `invoke`.

| Step order | Node name | Important state after this node | Why control moved next |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Sample filled walkthrough (success path)

Request: `"I need a follow-up visit next week with the same doctor."`

| Step order | Node name | Important state after this node | Why control moved next |
|---|---|---|---|
| 1 | `understand_request` | `cleaned_request` set; `trace` has one name | Unconditional edge to check |
| 2 | `check_availability` | `slot_found=True`; `appointment_time` set | Unconditional edge to confirm (linear graph) |
| 3 | `confirm_outcome` | `result` contains confirmation text | Edge to END |

### Sample filled walkthrough (conditional blocked path)

Request: `"Please book a follow-up tomorrow."`

| Step order | Node name | Important state after this node | Why control moved next |
|---|---|---|---|
| 1 | `understand_request` | cleaned text saved | Unconditional edge to check |
| 2 | `check_availability` | `slot_found=False` | Router chose `need_more_info` |
| 3 | `need_more_info` | `result` asks for a preferred week | Edge to END |

### Common mistakes while tracing

- Looking only at the final message and ignoring mid-run state
- Forgetting to check **which branch** the router chose
- Adding too many print statements instead of a simple `trace` field
- Changing three nodes at once when one failed field is enough

### Activity — Full Trace Practice

Run either graph once with your own campus-style request (one sentence). Fill the walkthrough table completely. Then answer in one line each:

1. Which node added the most important new field?
2. Did any node run that was unnecessary for your request?
3. If the result looked wrong, was the bug in a **node**, a **transition**, or a **state field**?

---

## Connecting Communication Thinking to Graphs

You already know structured agent communication and MCP-style tool connections. LangGraph does not replace those ideas. It gives workflow control a **runnable map**.

| Communication idea | Graph equivalent |
|---|---|
| Ordered steps / subtasks | Nodes |
| Message handoff between steps | State updates between nodes |
| Stop when complete / blocked | END, or a branch to a blocked node |
| Clear JSON contracts | Minimal typed state fields |

A useful design order for beginners:

1. Write the **user goal**
2. Draw **2–3 nodes** and transitions
3. List **minimal state fields**
4. Implement node functions
5. Run once and complete an **execution walkthrough**

If you skip the drawing step, code becomes guesswork. If you skip the walkthrough, bugs hide in plain sight.

---

## Design Checklist Before You Call It Done

Use this checklist for every small graph in this course:

- Can a teammate understand your diagram in under one minute?
- Does each node have **one job**?
- Is state **minimal** but complete enough for the next node?
- Are conditional transitions written as clear rules, not vibes?
- After one run, can you explain **order + state change** without guessing?
- Does the graph finish cleanly on both success and blocked paths?

If any answer is “no,” fix the design before adding more nodes.

---

## Key Takeaways

- An agent workflow becomes trustworthy when you model it as **nodes**, **transitions**, and **shared state** — not only as a list of sticky notes.
- **Minimal graph state** is a design skill: pack only the fields later nodes truly need.
- A **two- to three-node** graph is enough to practise building, running, and tracing a bounded task.
- **Execution walkthroughs** turn debugging into an operations habit: order, state update, reason for the next hop.
- These basics are the foundation for later graph work: once nodes, transitions, and state are clear, you can extend the same map without redesigning it from scratch.

In the **next** sessions you will add advanced LangGraph controls on top of this foundation. For now, stay with a small visible map: clear stations, clear paths, and a shared notebook you can read after every stop.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **LangGraph** | Framework for building stateful multi-step workflows as graphs |
| **Node** | One step / station of work (usually a function) |
| **Transition / Edge** | Path from one node to another |
| **Conditional edge** | Transition chosen by a router rule |
| **Graph state** | Shared notebook passed through the run |
| **Minimal state** | Smallest useful set of shared fields |
| **Orchestration** | Running the right step at the right time with shared context |
| **`StateGraph`** | Builder object used to assemble nodes and edges |
| **`START` / `END`** | Special markers for graph entry and exit |
| **`add_node`** | Registers a node name and function |
| **`add_edge`** | Adds an unconditional transition |
| **`add_conditional_edges`** | Adds a branching transition using a router |
| **`compile()`** | Turns the graph design into a runnable object |
| **`invoke(state)`** | Runs the graph once with starting state |
| **Execution walkthrough** | Ordered review of node visits and state updates |
| **`trace` field** | Simple list used here to record execution order |
| **`pip install langgraph`** | Install command for the LangGraph package |
| **MCP / structured tool handoffs (previous idea)** | Outside capabilities and clear messages that graphs can orchestrate |
