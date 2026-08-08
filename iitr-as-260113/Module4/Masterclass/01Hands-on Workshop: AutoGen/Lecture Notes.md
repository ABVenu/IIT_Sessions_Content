# Hands-on: Hotel Guest Complaint Intake Desk with AutoGen

## Introduction

In the **previous** sessions you learnt **AutoGen conversable agents**, **tool registration**, **termination**, then **GroupChat**, **GroupChatManager**, **speaker selection**, and **max rounds**.

This hands-on combines those habits into one hospitality product: a **Hotel Guest Complaint Intake Desk**. A small specialist team intakes a guest complaint, classifies it, looks up the stay with an approved tool, creates a ticket, and closes the chat under clear stop rules.

**What you will build:**

- A **multi-agent hotel intake team** with clear role boundaries
- Two **registered tools**: stay lookup and ticket create
- A **GroupChat** with manager, speaker rules, and **max rounds**
- A habit of reading the **conversation trace** and fixing one orchestration failure

---

## The Real Problem: Hotel Guest Complaints

Hotel front desks hear the same pattern every day. AC fails at midnight. Housekeeping missed a room. The bill has a wrong spa charge. WhatsApp groups and reception notes bury the trail. A specialist agent team keeps roles visible and tickets trackable.

- **Official Definition:** A **guest complaint intake workflow** turns a guest message into a classified, stay-linked ticket with a calm confirmation.
- **In Simple Words:** A digital front-office team that listens, sorts, checks the booking, and issues a case id.
- **Real-Life Example:** Like a hospital triage desk — understand the problem, assign the right ward, check the patient file, then issue a token.

![Chaotic hotel guest complaint chat versus a calm Hotel Guest Complaint Intake Desk with labelled counters and tracked ticket files](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/masterclass/01handson-workshop-autogen/masterclass-autogen-01-chaotic-chat-vs-hotel-desk.png)

| Guest message | Expected path |
|---|---|
| `"AC not cooling in room 412, booking BK-7781"` | Classify `room_comfort` → lookup stay → create ticket |
| `"Something is wrong with my stay"` | Intake asks for booking id / clearer details |
| `"Wrong spa charge of 2500 on my bill, BK-9002"` | Classify `billing` → lookup → ticket (billing desk) |

The same intake pattern also appears in **e-commerce order complaints** and **HR helpdesk tickets**. This workshop uses a hotel so the roles stay concrete and easy to picture.

You are not learning a new framework from zero. You are packaging conversable agents, tools, and group orchestration into one guest-facing desk you can demo end to end.

Keep the hotel story fixed while you practice. Industry renames come later once the team, tools, and stop rules work.

---

## Design First: Team, Tools, and Stop Rules

Draw the operating map before code. Refresh the AutoGen ideas you will reuse.

- **AssistantAgent** — Official: LLM-backed specialist that reasons and may suggest tools. Simple: the expert at one desk. Example: category classifier for guest issues.
- **UserProxyAgent** — Official: user-side / executor agent that can start work and run registered functions. Simple: the office runner who presses approved buttons. Example: executes `create_complaint_ticket`.
- **register_function** — Official: connect a Python helper so a caller may suggest it and an executor may run it. Simple: issue an access card for one tool only. Example: only the desk clerk path may create tickets.
- **GroupChat / GroupChatManager** — Official: shared multi-agent conversation plus coordinator. Simple: meeting room + chairperson. Example: intake → classify → clerk under one manager.
- **Speaker selection / max rounds** — Official: who speaks next / hard turn limit. Simple: chair calls the right person / meeting alarm. Example: stop runaway polite loops.

```text
Guest complaint
   → [IntakeAgent] clarify booking / room if missing
   → [ClassifierAgent] tag category
   → [DeskClerkAgent] suggest tools → [UserProxy] execute tools
   → DeskClerk writes confirmation → TERMINATE
```

**Categories used in this desk:** `room_comfort`, `housekeeping`, `billing`, `dining`, `unclear`

**Why these roles, not one mega-agent?**

- One agent that “does everything” hides mistakes and invents booking details
- Split roles make the **conversation trace** easy to audit in a Zoom demo
- Tool rights stay narrow: only the clerk path may create tickets

**Minimal tools (local fake hotel system):**

| Tool | Purpose | Safe failure |
|---|---|---|
| `lookup_guest_stay(booking_id)` | Return room, guest name, stay dates | `STAY_NOT_FOUND` |
| `create_complaint_ticket(category, summary, room)` | Return ticket id like `HT-ROOM-412` | Never invent an id without calling the tool |

![Hotel operations round table with Intake Classifier Desk Clerk and Chairperson Manager sharing one conversation notepad](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/masterclass/01handson-workshop-autogen/masterclass-autogen-02-specialist-team-roundtable.png)

### Activity — Predict the Hand-off

For `"Towels not replaced in room 208, booking BK-3301"`, write: expected category, which agent should speak after classify, and which tool runs first.

**Suggested answers:** `housekeeping` → DeskClerkAgent → `lookup_guest_stay`

### Activity — Spot the Role Leak

Which system message is wrong and why?  
“ClassifierAgent may also create tickets if the guest sounds angry.”

**Suggested answer:** Category and ticket creation must stay separate so audits remain clear.

### Setup

```bash
pip install ag2[openai]
export GROQ_API_KEY="your_groq_api_key"
```

`ag2` is the maintained AutoGen package family that still exposes the familiar `AssistantAgent`, `UserProxyAgent`, `GroupChat`, and `GroupChatManager` names used in this course.

If the key is missing, agents cannot call the model. Keep secrets in the environment — never paste keys into notebooks you share.

---

## Build the Full Desk: Agents, Tools, Group Chat

One notebook flow covers role boundaries, tool registration, group orchestration, and controlled close.

### Full code — hotel guest complaint intake end to end

```python
# Import operating-system helpers to read the API key
import os  # Standard library for environment variables

# Import AutoGen agent and group-chat building blocks
from autogen import (  # Core AutoGen symbols used in this desk
    AssistantAgent,  # Specialist LLM agent
    UserProxyAgent,  # Starter + tool executor
    GroupChat,  # Shared conversation room
    GroupChatManager,  # Chairperson for the room
    register_function,  # Safe tool wiring helper
)


# Read Groq key from the environment (never hard-code secrets)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")  # Empty if not set

# Shared LLM settings for all specialist agents
llm_config = {  # Dictionary passed into each LLM-backed agent
    "config_list": [  # One model endpoint entry
        {
            "model": "llama-3.3-70b-versatile",  # Fast capable Groq model
            "api_key": GROQ_API_KEY,  # Key from environment
            "api_type": "groq",  # Tell AutoGen to use Groq
        }
    ],
    "temperature": 0,  # Keep answers steadier for learning
}


# Tiny fake hotel property system used by tools
HOTEL_STAYS = {  # booking_id → stay record
    "BK-7781": {  # Sample stay 1
        "guest": "Asha Verma",  # Guest name
        "room": "412",  # Room number
        "dates": "08–10 Aug",  # Stay window
    },
    "BK-9002": {  # Sample stay 2
        "guest": "Rohit Nair",  # Guest name
        "room": "215",  # Room number
        "dates": "07–09 Aug",  # Stay window
    },
    "BK-3301": {  # Sample stay 3
        "guest": "Neha Shah",  # Guest name
        "room": "208",  # Room number
        "dates": "08–12 Aug",  # Stay window
    },
}


# Tool 1: look up a guest stay by booking id
def lookup_guest_stay(booking_id: str) -> str:  # Tool signature for stay lookup
    """Return stay details for a booking id from the hotel system."""
    stay = HOTEL_STAYS.get(booking_id.strip().upper())  # Normalise id
    if not stay:  # Unknown booking
        return "STAY_NOT_FOUND"  # Calm structured miss
    return (  # Human-readable stay card
        f"guest={stay['guest']}; room={stay['room']}; dates={stay['dates']}"
    )


# Tool 2: create a complaint ticket in the hotel desk system
def create_complaint_ticket(category: str, summary: str, room: str) -> str:  # Tool signature for tickets
    """Create a complaint ticket and return a ticket id."""
    code = category[:4].upper()  # Short category code
    ticket_id = f"HT-{code}-{room}"  # Simple learnable ticket pattern
    return f"TICKET_CREATED:{ticket_id}"  # Structured success marker


# Termination helper: stop when ticket is created or TERMINATE appears
def is_done(message) -> bool:  # Shared stop-rule helper
    content = (message.get("content") or "") if isinstance(message, dict) else str(message)  # Read text safely
    upper = content.upper()  # Case-insensitive checks
    return ("TERMINATE" in upper) or ("TICKET_CREATED:" in upper)  # Success or explicit stop


# Agent 1: intake specialist — clarify missing booking or room details
intake_agent = AssistantAgent(  # Create intake specialist
    name="IntakeAgent",  # Unique agent name
    system_message=(  # Strict role boundary
        "You are the hotel intake specialist. "
        "Read the guest complaint. If booking id or room is missing, ask for it briefly. "
        "If details are enough, summarise the complaint in one short paragraph for the next agent. "
        "Do not classify categories. Do not invent stay data. Do not create tickets."
    ),
    llm_config=llm_config,  # Shared model config
)

# Agent 2: classifier — assign one category label only
classifier_agent = AssistantAgent(  # Create classifier specialist
    name="ClassifierAgent",  # Unique agent name
    system_message=(  # Strict role boundary
        "You are the hotel complaint classifier. "
        "Choose exactly one category: room_comfort, housekeeping, billing, dining, or unclear. "
        "Reply with: CATEGORY=<label> and one sentence reason. "
        "Do not call tools. Do not create tickets."
    ),
    llm_config=llm_config,  # Shared model config
)

# Agent 3: desk clerk — use tools then write guest confirmation
desk_clerk = AssistantAgent(  # Create desk clerk specialist
    name="DeskClerkAgent",  # Unique agent name
    system_message=(  # Strict role boundary
        "You are the hotel desk clerk. "
        "First call lookup_guest_stay with the booking id. "
        "Then call create_complaint_ticket with category, short summary, and room. "
        "Finally write a calm guest confirmation that includes the ticket id. "
        "End with the word TERMINATE when the ticket is created. "
        "Never invent tool results."
    ),
    llm_config=llm_config,  # Shared model config
)

# User-side executor: starts the chat and runs approved tools
user_proxy = UserProxyAgent(  # Create front-desk runner / executor
    name="FrontDeskRunner",  # Unique agent name
    human_input_mode="NEVER",  # Fully automatic demo run
    code_execution_config=False,  # No free-form code execution
    is_termination_msg=is_done,  # Stop on ticket or TERMINATE
)

# Register stay lookup: clerk suggests, runner executes
register_function(  # Wire stay lookup tool
    lookup_guest_stay,  # Python function
    caller=desk_clerk,  # Who may suggest the tool
    executor=user_proxy,  # Who may run the tool
    description="Look up guest stay details by booking id.",  # LLM-facing help text
)

# Register ticket create: clerk suggests, runner executes
register_function(  # Wire ticket create tool
    create_complaint_ticket,  # Python function
    caller=desk_clerk,  # Who may suggest the tool
    executor=user_proxy,  # Who may run the tool
    description="Create a hotel complaint ticket and return ticket id.",  # LLM-facing help text
)


# Custom speaker policy: keep handoffs intentional and tool-safe
def select_hotel_speaker(last_speaker, groupchat):  # Chair rule for next speaker
    messages = groupchat.messages  # Full shared transcript
    if not messages:  # First turn after kickoff
        return intake_agent  # Start at intake
    last = messages[-1]  # Latest message dict
    # If a tool call is pending, the executor must speak next
    if last.get("tool_calls") or last.get("function_call"):  # Tool suggestion present
        return user_proxy  # Runner executes the tool
    # After tool result, return to desk clerk to continue
    if last_speaker is user_proxy:  # Runner just spoke
        return desk_clerk  # Clerk consumes tool output
    # Normal specialist ladder
    if last_speaker is intake_agent:  # Intake finished
        return classifier_agent  # Then classify
    if last_speaker is classifier_agent:  # Classify finished
        return desk_clerk  # Then clerk + tools
    return desk_clerk  # Default safe speaker


# Shared group room with hard round limit
groupchat = GroupChat(
    agents=[user_proxy, intake_agent, classifier_agent, desk_clerk],  # Team roster
    messages=[],  # Fresh transcript
    max_round=12,  # Hard stop against runaway dialogue
    speaker_selection_method=select_hotel_speaker,  # Custom chair rules
)

# Chairperson that runs the group exchange
manager = GroupChatManager(
    groupchat=groupchat,  # Attach the room
    llm_config=llm_config,  # Manager may use LLM when needed
    is_termination_msg=is_done,  # Same stop rule as runner
)


# Helper: print a short readable trace for learning
def print_trace(chat_result):
    print("=== CONVERSATION TRACE ===")  # Section header
    for i, msg in enumerate(groupchat.messages, start=1):  # Numbered turns
        name = msg.get("name") or msg.get("role") or "unknown"  # Speaker label
        content = (msg.get("content") or "")[:220]  # Short preview
        print(f"{i}. [{name}] {content}")  # One line per turn
    print("=== END TRACE ===")  # Section footer


# Demo 1 — Happy path: clear complaint with booking id
complaint_1 = (  # Guest message with enough detail
    "Guest complaint: AC not cooling since evening in room 412. "
    "Booking id BK-7781. Please raise a ticket."
)
chat_1 = user_proxy.initiate_chat(  # Start the group through the manager
    manager,  # Recipient is the chairperson
    message=complaint_1,  # Opening guest complaint
)
print_trace(chat_1)  # Review who spoke and whether tools ran


# Demo 2 — Vague complaint: intake should ask for missing details first
groupchat.messages = []  # Reset shared transcript for a new case
complaint_2 = "Something is wrong with my stay. Please help."  # Vague guest text
chat_2 = user_proxy.initiate_chat(  # Second run
    manager,  # Same chairperson
    message=complaint_2,  # Vague opening
)
print_trace(chat_2)  # Expect intake clarification behaviour


# Demo 3 — Billing complaint path
groupchat.messages = []  # Reset transcript again
complaint_3 = (  # Billing-focused complaint
    "Wrong spa charge of 2500 on my bill. Booking BK-9002, room 215."
)
chat_3 = user_proxy.initiate_chat(  # Third run
    manager,  # Same chairperson
    message=complaint_3,  # Billing complaint
)
print_trace(chat_3)  # Expect billing category + ticket confirmation
```

### How the code works

- **IntakeAgent**, **ClassifierAgent**, and **DeskClerkAgent** are **AssistantAgent** specialists with non-overlapping system messages
- **FrontDeskRunner** (`UserProxyAgent`) starts the case and **executes** only registered tools
- `register_function` gives the clerk permission to *suggest* tools and the runner permission to *run* them
- `select_hotel_speaker` enforces a clear ladder and always routes tool calls to the executor
- `max_round=12` plus `TERMINATE` / `TICKET_CREATED:` prevent endless polite loops

![Desk clerk station with approved Lookup Guest Stay and Create Complaint Ticket tool cards for safe registered function use](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/masterclass/01handson-workshop-autogen/masterclass-autogen-03-registered-tools-cards.png)

**Common mistakes:** Letting every agent call every tool. Using `human_input_mode="ALWAYS"` in a Zoom demo without a plan. Forgetting to reset `groupchat.messages` between cases. Changing speaker rules so tool calls never reach the executor.

---

## Read the Trace and Fix One Failure Mode

A polished final paragraph is not enough. Professionals read the **conversation trace** like an audit file.

- **Official Definition:** A **conversation trace** is the ordered record of agent messages, tool suggestions, tool results, and the final close signal.
- **In Simple Words:** It is the CCTV footage of the meeting.
- **Real-Life Example:** Like a hotel duty-manager logbook that shows who handled the guest and when the ticket was stamped.

Check these four questions after every run:

- Did **IntakeAgent** speak before classification when details were thin?
- Did **ClassifierAgent** output exactly one `CATEGORY=` label?
- Did **DeskClerkAgent** call tools instead of inventing stay data?
- Did the chat **stop** because of ticket success / TERMINATE, not only because rounds expired?

**Sample happy-path shape (Demo 1):**

| Order | Likely speaker | What good looks like |
|---|---|---|
| 1 | IntakeAgent | Short complaint summary with booking `BK-7781` |
| 2 | ClassifierAgent | `CATEGORY=room_comfort` |
| 3 | DeskClerkAgent | Suggests `lookup_guest_stay` |
| 4 | FrontDeskRunner | Returns stay card for room 412 |
| 5 | DeskClerkAgent | Suggests `create_complaint_ticket` |
| 6 | FrontDeskRunner | Returns `TICKET_CREATED:...` |
| 7 | DeskClerkAgent | Calm guest confirmation + `TERMINATE` |

| Failure mode | What you see | Configuration fix to try |
|---|---|---|
| **Wrong speaker** | Classifier starts creating tickets | Tighten system messages + speaker ladder |
| **Repetition deadlock** | Agents restate the same apology | Lower `max_round` slightly and strengthen TERMINATE instruction |
| **Tool not executed** | Clerk asks for lookup but runner never runs it | Ensure tool-call branch returns `user_proxy` |
| **Invented booking** | Room/guest details appear with no tool result | Reinforce “Never invent tool results” in clerk message |

![Runaway wrong-speaker hotel meeting versus a chaired complaint meeting with max-rounds timer and clear ticket-done close](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/masterclass/01handson-workshop-autogen/masterclass-autogen-04-wrong-speaker-vs-controlled-close.png)

### Activity — Trace Detective

After Demo 1, write one line: *Tool use was visible / not visible because…*

### Activity — Break Then Fix

Temporarily set `max_round=3` and re-run Demo 1. Write what failed, then restore `max_round=12` and confirm the ticket path recovers.

### Activity — Wrong-Speaker Drill

Imagine ClassifierAgent replies with a fake ticket id. Which two changes would you make first — system message, speaker rule, tool registration, or termination check?

**Suggested answer:** system message (remove ticket rights) and speaker rule (send ticket work only through DeskClerk → runner tools).

---

## Same Pattern, Other Industries

Once the hotel desk works, the AutoGen shape transfers with new labels only.

| Industry desk | Intake asks for… | Classifier labels | Tools |
|---|---|---|---|
| **Hotel** (this workshop) | booking id, room | room_comfort / housekeeping / billing / dining | stay lookup, ticket create |
| **E-commerce** | order id, SKU | delivery / refund / damaged / wrong_item | order lookup, case create |
| **HR helpdesk** | employee id, topic | leave / payroll / policy / unclear | employee lookup, case create |

### Activity — Rename the Desks

On paper only, rename the three specialists for an **e-commerce order complaint desk**. Keep the same tool pattern: one lookup + one case create.

### Activity — HR Variant One-Liner

Write one guest/employee-style opening message for an HR payroll complaint that includes an employee id placeholder like `EMP-1044`.

---

## Student Practice

### Activity — Run Your Own Complaint
Invoke Demo 1 style with your own one-line hotel complaint that includes a booking id from `HOTEL_STAYS`. Record category, ticket id style, and whether TERMINATE appeared.

### Activity — Role Boundary Check

| Agent | Allowed to classify? | Allowed to call tools? | Allowed to invent stay data? |
|---|---|---|---|
| IntakeAgent | | | |
| ClassifierAgent | | | |
| DeskClerkAgent | | | |
| FrontDeskRunner | | | |

Fill with Yes/No. Compare with the system messages if any cell feels uncertain.

### Activity — AutoGen Reliability Checklist

| # | Check | Done? |
|---|---|---|
| 1 | Each specialist has a clear system message boundary | |
| 2 | Tools are registered with caller + executor | |
| 3 | Tool suggestions are executed by UserProxyAgent | |
| 4 | Speaker selection sends tool calls to the executor | |
| 5 | `max_round` is set | |
| 6 | Termination checks for ticket success or TERMINATE | |
| 7 | You can explain the trace for one successful run | |

### Activity — Execution Walkthrough
Fill this table for the AC complaint (`BK-7781`):

| Step order | Speaker | Important output | Why control moved next |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

If the result looks wrong, decide whether the bug is in a **role prompt**, a **speaker rule**, a **tool registration**, or a **termination check**.

---

## Key Takeaways

- Model a complaint desk as **specialist conversable agents** with non-overlapping responsibilities.
- Use **register_function** so tool use is explicit: one caller suggests, one executor runs.
- Orchestrate with **GroupChat**, **GroupChatManager**, **speaker selection**, and **max rounds**.
- Prove quality with a **conversation trace**, not only the final guest message.
- The same AutoGen intake pattern ports to **e-commerce** and **HR** desks by renaming roles and tools.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this session |
|---|---|
| **AutoGen / AG2** | Framework for multi-agent conversations and tool-backed workflows |
| **AssistantAgent** | Specialist LLM agent with a system message |
| **UserProxyAgent** | Starter / executor agent; runs registered tools in this desk |
| **register_function** | Wires a Python tool to a caller and an executor |
| **GroupChat** | Shared multi-agent conversation room |
| **GroupChatManager** | Chairperson that runs the group exchange |
| **Speaker selection** | Rule for who speaks next |
| **max_round** | Hard limit on group turns |
| **Termination** | Stop rule (`TERMINATE` / `TICKET_CREATED:`) |
| **Conversation trace** | Ordered message evidence for debugging |
| **`pip install ag2[openai]`** | Package install used for this hands-on |
| **`GROQ_API_KEY`** | Environment variable for the model endpoint |
