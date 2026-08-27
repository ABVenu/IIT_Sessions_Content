# AutoGen: Hands-on — End-to-End Multi-Agent System

## Context of This Session

In the **previous** session you upgraded a **CrewAI** Placement Brief Crew into a production-style workflow: **custom tools**, **process** choice, optional **memory**, a validation checklist, and **iteration** on one weak prompt.

This session adds a different unit of design. **AutoGen** treats agents as **conversable** partners in one dialogue. You will ship **one campus desk**: first a stipend-and-dispatch **pair** with registered tools and a stop stamp, then the same facts in a **chaired group** that writes a placement-drive notice.

**In this session, you will:**

- **Configure** conversable agents with system messages and non-overlapping campus seats
- **Register** lookup tools and run a pair until an explicit **termination** condition
- **Orchestrate** a **GroupChat** with speaker selection and max rounds
- **Read** conversation traces to verify tool use, handoffs, and one configuration fix

---

## From Crew Tickets to One Dialogue Desk

Connecting sentence: CrewAI shines when research, write, and review are **tickets**. Morning ops often needs **ask, look up, follow up, stop** — and some mornings that lookup must become a **briefing**.

- **Official Definition:** The **conversable-agent model** is AutoGen’s pattern: agents send and receive messages in a loop until a **termination** condition fires.
- **In Simple Words:** Colleagues on a work chat, not folders on a conveyor.
- **Real-Life Example:** **Ananya** must answer Prof. Meera Kulkarni at Greenfield Institute of Technology, Pune: *Are Nimbus and Riverbank still delayed, and has trainer Slack gone?* If the drive is this week, that same packet must also become faculty copy with **risk fences**.

![From CrewAI ticket folders on a conveyor to an AutoGen pair at a campus desk, then a chaired group briefing in the GIT Pune placement cell](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module4/session42/session42-01-from-crew-to-autogen-desk.png)

The same campus morning can move from ticket folders, to a two-seat work chat, to a chaired briefing room.

**Need:** A weekly crew is heavy for “Riverbank only — has Slack gone?” A pair with no chair is noisy when research, risk, and messaging must share **one** thread.

**Common doubt:** *“Does AutoGen replace CrewAI?”* — No. Crews remain strong for fixed handoffs. AutoGen shines for **interactive delegation** and **chaired specialist talk**.

### Activity — Pick the unit

Write **crew**, **pair**, or **group** for: (1) four-section weekly brief, (2) “Riverbank only — dispatch status”, (3) drive page with risk fences visible.

---

## AssistantAgent and UserProxyAgent

Connecting sentence: A conversation still needs **job titles**. These two seats stay in both runs today.

- **Official Definition:** An **AssistantAgent** is an LLM-backed specialist that plans, replies, and may **suggest** registered tools. A **UserProxyAgent** is the user-side agent that **starts** the task, may execute tools, and helps enforce stop rules.
- **In Simple Words:** The analyst thinks and asks for lookups. The desk runner starts the thread and presses approved buttons.
- **Real-Life Example:** Ananya (or a script standing in for her) posts the morning ask. The stipend analyst must not invent that Infosys owes eight students.

| Agent | Campus seat | Must do | Must not do |
|---|---|---|---|
| **UserProxyAgent** | Campus desk runner | Start the ask; run registered tools | Invent register rows |
| **AssistantAgent** | Specialist | Plan, call tools or write a slice | Guess headcounts; run unregistered code |

![AutoGen pair tech stack: UserProxyAgent CampusDeskRunner, AssistantAgent StipendAnalyst, register_function with caller and executor, tools and SUMMARY_READY](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module4/session42/session42-02-pair-tech-stack.png)

These are the AutoGen building blocks you will type: two agent classes, one registration arrow, and a stop stamp.

- **Official Definition:** A **system message** is the initial instruction that sets an agent’s seat, limits, and stop phrase.
- **In Simple Words:** The job contract taped to the chair.
- **Real-Life Example:** Weak: “Be helpful.” Strong: “Use lookup tools for every company status. Never invent a student count.”

**Common error:** Both agents writing the final summary. Roles blur and the trace becomes unreadable.

### Activity — Tighten one system message

Rewrite *“You are a helpful analyst”* in two sentences: campus setting, and one thing the analyst must **not** do.

---

## Register Functions and Termination

Connecting sentence: A system message is a promise. **Registration** is the access card. **Termination** is the meeting alarm.

- **Official Definition:** **`register_function`** connects a Python helper to a **caller** (who may suggest it) and an **executor** (who may run it).
- **In Simple Words:** Issue one swipe card. The analyst asks; the desk swipes.
- **Real-Life Example:** `lookup_stipend_status("Infosys")` must return `UNKNOWN_COMPANY`, not a guessed row.

- **Official Definition:** A **termination condition** is an explicit rule (`is_termination_msg`, a keyword, or a turn cap) that ends the loop.
- **In Simple Words:** Stamp **minutes ready** so the chat may stop.
- **Real-Life Example:** The analyst ends the pair with `SUMMARY_READY`. The group ends with `BRIEF_READY`.

![AutoGen conversable data flow: initiate_chat, suggest tool, execute function, tool result in the trace, then SUMMARY_READY stops the loop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module4/session42/session42-03-pair-data-flow.png)

Messages and tool results travel in a loop until `is_termination_msg` sees **SUMMARY_READY**. That loop is the data flow, not a conveyor of tickets.

| Function | Returns | Fail honestly |
|---|---|---|
| `lookup_stipend_status(company)` | Delayed count and last HR reminder | `UNKNOWN_COMPANY` |
| `lookup_dispatch_queue()` | Trainer Slack and second-reminder status | Never invent “sent” |

- **Official Definition:** **Code execution** (`code_execution_config` on a UserProxyAgent) lets that agent run generated Python during the chat.
- **In Simple Words:** The desk may execute whatever script the analyst writes.
- **Real-Life Example:** Useful later for a chart. Dangerous on a shared campus key. **This run keeps it off** — lookups only.

**Logic:** CrewAI stopped when the **task list** finished. AutoGen stops when **you** say the job is done. If you never say it, the dialogue can run until money or patience runs out.

**Common error:** Registering tools with the same agent as caller and executor, or checking only for `TERMINATE` while the analyst writes “done” in plain English.

### Activity — Who swipes, and what stamp?

If the analyst suggests `lookup_dispatch_queue`, who must speak next? Write the last two lines of a successful pair summary, including the keyword you will search for.

---

## Lab Setup and Bounded Campus Facts

Connecting sentence: Same secret habit as CrewAI: the key lives in `.env`. One folder holds **both** runs.

Create folder `campus_ops_autogen`. Inside it, `.env` (do **not** commit):

```text
OPENAI_API_KEY=your_openai_key_here
```

```bash
pip install ag2 python-dotenv
```

`ag2` is the maintained AutoGen package family that still exposes `AssistantAgent`, `UserProxyAgent`, `register_function`, `GroupChat`, and `GroupChatManager`.

Keep this data **inside** the scripts as the training-wheels version of a campus lookup: **Nimbus Analytics** (8 delayed, HR reminder 4 August) and **Riverbank Retail** (6 delayed, same reminder). Trainer Slack is **not sent**; the second HR reminder is **pending**. The tracker launch is a **status board**, not a payment guarantee.

**Pair goal:** Daily ops summary + `SUMMARY_READY`. **Group goal:** Research → risk → messaging notice + `BRIEF_READY`.

---

## Full Pair Script

Connecting sentence: First product of the morning: two seats, two tools, one stop rule.

Save as `campus_ops_pair.py` in the same folder as `.env`.

```python
# campus_ops_pair.py — AutoGen conversable pair for a daily campus ops summary
import os  # read OPENAI_API_KEY from the environment
from dotenv import load_dotenv  # load .env into environment variables
from autogen import AssistantAgent, UserProxyAgent, register_function  # pair building blocks

load_dotenv()  # read the API key before any model call
API_KEY = os.getenv("OPENAI_API_KEY", "")  # empty string if missing

llm_config = {  # shared LLM settings for the specialist
    "config_list": [{"model": "gpt-4o-mini", "api_key": API_KEY}],  # classroom OpenAI model
    "temperature": 0.2,  # steady facts for a daily desk
}  # end llm_config

STIPEND_REGISTER = {  # bounded company rows — not a live HTTP API
    "nimbus analytics": {"students": 8, "status": "delayed", "last_hr": "4 August"},  # file-backed row
    "riverbank retail": {"students": 6, "status": "delayed", "last_hr": "4 August"},  # file-backed row
}  # end register

DISPATCH_QUEUE = {  # bounded dispatch board
    "trainer_slack": "not sent",  # Campus Ops Inbox has not pinged trainers
    "second_hr_reminder": "pending",  # second company HR mail not yet sent
}  # end dispatch queue

def lookup_stipend_status(company: str) -> str:  # tool 1 — company stipend row
    """Return stipend status for one company from the campus register."""  # agent-facing description
    key = company.strip().lower()  # normalise the company name
    row = STIPEND_REGISTER.get(key)  # lookup or None
    if not row:  # unknown company
        return f"UNKNOWN_COMPANY:{company}"  # honest miss
    return f"company={company}; students={row['students']}; status={row['status']}; last_hr={row['last_hr']}"  # card

def lookup_dispatch_queue() -> str:  # tool 2 — pending campus dispatch
    """Return the current trainer Slack and HR reminder dispatch flags."""  # agent-facing description
    return f"trainer_slack={DISPATCH_QUEUE['trainer_slack']}; second_hr_reminder={DISPATCH_QUEUE['second_hr_reminder']}"  # board

def is_done(message) -> bool:  # termination helper
    content = (message.get("content") or "") if isinstance(message, dict) else str(message)  # read text safely
    upper = content.upper()  # case-insensitive
    return ("SUMMARY_READY" in upper) or ("TERMINATE" in upper)  # success stamp or explicit stop


analyst = AssistantAgent(  # specialist who may suggest tools
    name="StipendAnalyst",  # unique name in the trace
    system_message=(  # responsibility boundary
        "You are the GIT Pune stipend analyst for Ananya's Campus Ops Inbox. "  # campus seat
        "For every company status you must call lookup_stipend_status. "  # tool rule
        "For dispatch you must call lookup_dispatch_queue. "  # second tool
        "Never invent student counts or claim Slack was sent. "  # accuracy fence
        "Write a daily summary with three short bullets, then the line SUMMARY_READY. "  # stop stamp
        "Do not run code. Do not treat UNKNOWN_COMPANY as a delayed employer."  # honest miss
    ),  # end system message
    llm_config=llm_config,  # model config
)  # end analyst

desk = UserProxyAgent(  # starter + tool executor
    name="CampusDeskRunner",  # unique name
    human_input_mode="NEVER",  # fully automatic demo
    code_execution_config=False,  # optional code execution stays OFF
    is_termination_msg=is_done,  # stop on SUMMARY_READY or TERMINATE
)  # end desk

register_function(  # wire stipend lookup
    lookup_stipend_status,  # Python function
    caller=analyst,  # who may suggest
    executor=desk,  # who may run
    description="Look up internship stipend status by company name.",  # model-facing help
)  # end register stipend

register_function(  # wire dispatch lookup
    lookup_dispatch_queue,  # Python function
    caller=analyst,  # who may suggest
    executor=desk,  # who may run
    description="Look up trainer Slack and second HR reminder flags.",  # model-facing help
)  # end register dispatch

if __name__ == "__main__":  # run only when executed directly
    if not API_KEY:  # fail clearly
        raise ValueError("Set OPENAI_API_KEY in .env")  # setup reminder
    opening = (  # delegated morning task
        "Prepare this morning's campus ops summary for Prof. Meera Kulkarni. "  # daily ask
        "Cover Nimbus Analytics and Riverbank Retail stipend delays, "  # two companies
        "then dispatch status, then one recommended next action. Use tools. Do not guess."  # no hallucination
    )  # end opening
    result = desk.initiate_chat(analyst, message=opening)  # start the pair dialogue
    history = getattr(result, "chat_history", None) or []  # AutoGen history if present
    if not history and hasattr(desk, "chat_messages"):  # fallback to stored pair transcript
        history = desk.chat_messages.get(analyst, [])  # messages with the analyst
    print("=== PAIR TRACE ===")  # banner
    for i, msg in enumerate(history, start=1):  # numbered turns
        name = msg.get("name") or msg.get("role") or "unknown"  # speaker
        print(f"{i}. [{name}] {str(msg.get('content') or '')[:220]}")  # preview
    print("=== END PAIR TRACE ===")  # footer
```

**How the code works:**

- `AssistantAgent` holds the analyst **system message**. `UserProxyAgent` starts the chat and **executes** tools.
- `register_function` sets **caller=analyst** and **executor=desk**. Suggestions and runs stay on different seats.
- `code_execution_config=False` keeps the desk on lookups only. `is_done` looks for `SUMMARY_READY`.
- The printed **trace** is how you verify the analyst did not invent a row.

Run: `python campus_ops_pair.py`

| Symptom | Likely cause | Fix |
|---|---|---|
| Auth / import error | Missing key or package | `.env` + `pip install ag2 python-dotenv` |
| Endless rephrasing | Keyword never emitted | Repeat `SUMMARY_READY` in the system message |
| Invented Infosys count | Tool not called | Trace must show `lookup_stipend_status` |

A healthy pair trace typically shows: desk opening → analyst suggests a lookup → desk returns students=8 or 6 → dispatch tool → three bullets + **SUMMARY_READY**. A final paragraph with **zero** tool lines is a guessing chatbot, not a delegated workflow.

### Activity — Trace detective (pair)

After your run, tick: both tools visible? Final bullets match 8 and 6 and Slack **not sent**? Chat ended with **SUMMARY_READY**? Optional probe: add *Also check Infosys* and confirm `UNKNOWN_COMPANY`, not a delayed headcount.

---

## GroupChat, Speaker Selection, and Max Rounds

Connecting sentence: The pair finished the lookup. A drive notice needs **three slices** in one room — or Infosys appears in a cheerful poster.

- **Official Definition:** A **GroupChat** is a shared message space for several conversable agents. A **GroupChatManager** is the coordinator that runs that space under your rules.
- **In Simple Words:** The meeting room, and the person who gives the floor.
- **Real-Life Example:** Ananya’s opening ask stays in one thread. The manager is the chair, not a fourth novelist.

- **Official Definition:** **Speaker selection** is the policy for who speaks next. **Max rounds** (`max_round`) is a hard cap on group turns. A **handoff** is the designed move of work from one specialist to another.
- **In Simple Words:** Call the right expert; pass the folder; ring the bell.
- **Real-Life Example:** After research lists Nimbus and Riverbank, **risk** must speak before **messaging** writes the poster. If messaging speaks first, the poster invents urgency-as-lawsuit.

![AutoGen GroupChat orchestration: GroupChatManager chairs a shared GroupChat, speaker selection Research then Risk then Messaging, max_round 10, BRIEF_READY](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module4/session42/session42-04-groupchat-orchestration.png)

The shared room is **GroupChat**. The chair is **GroupChatManager**. Numbered arrows are **speaker selection**. `max_round` is the bell.

| Specialist | Distinct sub-result | Must not do |
|---|---|---|
| **ResearchSpecialist** | File-backed facts: 14 students, two companies, tracker is status-only | Write final student copy |
| **RiskSpecialist** | Fence list: no legal threats, no unpaid totals, no extra companies | Invent replacement facts |
| **MessagingSpecialist** | Notice from **approved** lines only | Invent Nimbus headcount |

**This run:** custom `select_briefing_speaker` after the desk opens: research → risk → messaging, with **max rounds = 10**.

**Common error:** `max_round=3` on a three-specialist brief so messaging never speaks — that is an **incomplete handoff**, not efficiency. Treating the manager as a fourth novelist also hides which specialist failed.

### Activity — Set the bell

If each specialist needs one substantial turn, what is the **smallest** `max_round` you would try — 4, 10, or 40 — and why not 40?

---

## Full Group Script

Connecting sentence: Same folder, same facts, new objects: room, chair, ladder.

Save as `campus_ops_group.py`.

```python
# campus_ops_group.py — AutoGen group chat for a placement-drive briefing
import os  # read OPENAI_API_KEY
from dotenv import load_dotenv  # load .env
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager  # group blocks

load_dotenv()  # load the key
API_KEY = os.getenv("OPENAI_API_KEY", "")  # empty if missing
llm_config = {"config_list": [{"model": "gpt-4o-mini", "api_key": API_KEY}], "temperature": 0.2}  # classroom model

FACTS = (  # bounded briefing fence — same campus register as the pair
    "Campus: Greenfield Institute of Technology, Pune. Lead: Prof. Meera Kulkarni. "  # people
    "Issue: June internship stipends delayed for 14 students. "  # problem
    "Companies: Nimbus Analytics; Riverbank Retail. Range: Rs 8000 to 15000. "  # on-file names
    "HR reminder sent 4 August. Trainer Slack not sent. "  # dispatch facts
    "Launch: stipend-status tracker shows delay status only — not a payment promise. "  # feature fence
    "Do not invent companies, unpaid totals, or legal threats."  # hard no
)  # end FACTS

def is_done(message) -> bool:  # shared stop rule
    content = (message.get("content") or "") if isinstance(message, dict) else str(message)  # safe text
    return "BRIEF_READY" in content.upper() or "TERMINATE" in content.upper()  # completion stamps

research = AssistantAgent(  # specialist 1
    name="ResearchSpecialist",  # trace label
    system_message=(  # slice
        "You are campus research for a GIT Pune placement-drive briefing. "  # seat
        f"Use only these facts: {FACTS} "  # fence
        "Write 5 to 7 bullets of evidence. No student-facing poster. No legal language."  # sub-result
    ),  # end research message
    llm_config=llm_config,  # model
)  # end research

risk = AssistantAgent(  # specialist 2
    name="RiskSpecialist",  # trace label
    system_message=(  # slice
        "You are policy risk for the placement cell. Read research bullets. "  # seat
        "List fences: no extra companies, no unpaid totals, no legal threats, tracker is status-only. "  # fences
        "Flag any invented claim. Do not write the final student notice."  # not messaging
    ),  # end risk message
    llm_config=llm_config,  # model
)  # end risk

messaging = AssistantAgent(  # specialist 3
    name="MessagingSpecialist",  # trace label
    system_message=(  # slice
        "You write faculty and student messaging for the stipend-tracker launch. "  # seat
        "Use only research bullets that Risk did not flag. "  # approved inputs
        "Produce a short notice with Title, What students will see, What we will not claim. "  # shape
        "End with the line BRIEF_READY. Never invent facts."  # stop stamp
    ),  # end messaging message
    llm_config=llm_config,  # model
)  # end messaging

desk = UserProxyAgent(  # starts the meeting
    name="CampusDeskRunner",  # trace label
    human_input_mode="NEVER",  # automatic demo
    code_execution_config=False,  # no generated code
    is_termination_msg=is_done,  # stop on BRIEF_READY
)  # end desk


def select_briefing_speaker(last_speaker, groupchat):  # custom speaker selection
    if (not groupchat.messages) or (last_speaker is desk):  # empty room or desk just opened
        return research  # research speaks first
    if last_speaker is research:  # research handoff
        return risk  # then policy
    if last_speaker is risk:  # risk handoff
        return messaging  # then copy
    return messaging  # stay until BRIEF_READY / max_round


groupchat = GroupChat(  # the room
    agents=[desk, research, risk, messaging],  # roster
    messages=[],  # fresh transcript
    max_round=10,  # hard stop against runaway dialogue
    speaker_selection_method=select_briefing_speaker,  # chair rules
)  # end groupchat

manager = GroupChatManager(  # the chair
    groupchat=groupchat,  # attach the room
    llm_config=llm_config,  # available if the manager must speak
    is_termination_msg=is_done,  # same close rule
)  # end manager

if __name__ == "__main__":  # direct execution only
    if not API_KEY:  # fail clearly
        raise ValueError("Set OPENAI_API_KEY in .env")  # setup
    opening = (  # complex campus task
        "Prepare one placement-drive briefing for faculty and a student notice "  # two audiences
        "for the stipend-status tracker launch. Research, then risk, then messaging. Stay inside known facts."  # order
    )  # end opening
    desk.initiate_chat(manager, message=opening)  # start through the chair
    print("=== GROUP TRACE ===")  # banner
    for i, msg in enumerate(groupchat.messages, start=1):  # numbered turns
        name = msg.get("name") or msg.get("role") or "unknown"  # speaker
        print(f"{i}. [{name}] {str(msg.get('content') or '')[:200]}")  # preview
    print("=== END GROUP TRACE ===")  # footer
```

**How the code works:**

- Three **AssistantAgent** specialists have **non-overlapping** system messages. Each must produce a different sub-result.
- **GroupChat** is the shared room. **GroupChatManager** is the chair `initiate_chat` talks to.
- `select_briefing_speaker` encodes **handoffs**: desk opening → research → risk → messaging. That is **speaker selection**, not luck.
- `max_round=10` is the bell. `BRIEF_READY` is the success stamp.

Run: `python campus_ops_group.py`

If you temporarily set `speaker_selection_method="round_robin"`, the desk or the wrong specialist may talk out of turn. Restore `select_briefing_speaker`. Rigidity is the point when risk must speak before messaging.

---

## Read Traces and Fix One Failure

Connecting sentence: A polished last paragraph is not evidence. The **trace** is the CCTV of both runs.

- **Official Definition:** A **conversation trace** is the ordered record of messages, tool suggestions, tool results, and the close signal.
- **In Simple Words:** CCTV of the work chat.
- **Real-Life Example:** If the pair summary says “Slack sent” but dispatch returned `not sent`, the **analyst** ignored the tool.

- **Official Definition:** A **group-chat failure mode** is a repeatable bad pattern such as **wrong speaker** or **repetition deadlock**.
- **In Simple Words:** The meeting got stuck, or the wrong person grabbed the mic.
- **Real-Life Example:** Messaging answers “can we threaten legal action?” That is **wrong speaker**. Research repeating the same seven bullets four times is **repetition deadlock**.

| Failure | What you see | One configuration fix |
|---|---|---|
| Guessing pair | Final paragraph, zero tool lines | Strengthen “must call lookup” |
| Wrong speaker | Messaging speaks right after the desk | Restore the custom ladder (do not use loose auto select) |
| Repetition deadlock | Risk restates research with no new fence | Tighten risk’s message; keep room for messaging |
| Incomplete handoff | Messaging never speaks / no `BRIEF_READY` | Raise `max_round`; confirm the ladder after risk |
| Missing stamp | Endless “happy to help” | Put `SUMMARY_READY` / `BRIEF_READY` in the system message and in `is_done` |

**Lab fix:** Set `max_round=3`, re-run, write what failed (likely incomplete handoff). Restore `max_round=10` and confirm messaging returns. That is a **configuration** fix, not a new framework.

A messy trace is a configuration document. Change one setting: the ladder, the role text, or the round cap.

### Activity — Break then fix

After the group run: Did research speak before risk? Did messaging include `BRIEF_READY`? Did any extra company appear? Then run the `max_round=3` experiment and name the failure.

---

## What “Good” Looks Like on This Desk

A successful **end-to-end** morning has all of the following:

- Pair trace names **StipendAnalyst** and **CampusDeskRunner**, shows both lookups, ends with **SUMMARY_READY**
- Group trace shows **ResearchSpecialist**, then **RiskSpecialist**, then **MessagingSpecialist** with three distinct sub-results
- No extra company names; no legal threats; tracker stays status-only
- You can name one failure you induced and the **one** setting you changed

Do not put three novelists in a GroupChat for a yes/no dispatch question. Do not ask one pair to own research, risk, *and* messaging without a chair. Keep this run automatic so the ladder stays visible.

| # | Check | Done? |
|---|---|---|
| 1 | Pair system messages name seats and fences | |
| 2 | Two functions registered with caller ≠ executor; code execution off | |
| 3 | Pair trace shows stipend + dispatch lookups and SUMMARY_READY | |
| 4 | Custom speaker ladder is research → risk → messaging | |
| 5 | Group trace shows three distinct sub-results and BRIEF_READY (or a named failure + one fix) | |

If a box is empty, name **system message**, **registration**, **termination**, or **speaker / max_round** — then change only that layer.

**Upcoming** work moves from AutoGen’s conversation loop to **graph-shaped** agent workflows, where nodes and edges replace the chat chair.

---

## Key Takeaways

- **AutoGen** delegates work through **dialogue**: a conversable **pair** for lookups, a **GroupChat** when several specialists must share one thread.
- Split seats: **AssistantAgent** reasons and suggests; **UserProxyAgent** starts the job and **executes** registered tools. **`register_function`** plus a keyword stamp keep the desk inspectable.
- **GroupChatManager**, **speaker selection**, and **max rounds** keep research, risk, and messaging in order and stop runaway chat.
- Judge quality from the **conversation trace**, then change **one** configuration — system message, registration, stop rule, or speaker / round cap.

These habits — clear seats, registered tools, a designed stop, and a chair you can debug — are what you will reuse when workflows are drawn as graphs in **upcoming** sessions.

---

## Important Commands, Libraries, and Terminologies Used

| Term / Command | Type | Meaning |
|---|---|---|
| **AutoGen / ag2** | Framework | Conversable multi-agent library |
| **Conversable-agent model** | Pattern | Agents chat until a stop rule fires |
| **AssistantAgent** | Class | LLM specialist; may suggest tools |
| **UserProxyAgent** | Class | Starts the task; may execute tools |
| **register_function** | Call | Caller suggests; executor runs |
| **Termination condition** | Rule | `is_termination_msg` / keyword |
| **SUMMARY_READY / BRIEF_READY** | Keywords | Pair and group success stamps |
| **GroupChat** | Class | Shared multi-agent message room |
| **GroupChatManager** | Class | Chair that runs the group |
| **Speaker selection** | Policy | Who speaks next |
| **max_round** | Setting | Hard cap on group turns |
| **Wrong speaker / deadlock** | Failures | Unsuitable agent, or same points looping |
| **Conversation trace** | Evidence | Ordered messages and tool results |
| **initiate_chat** | Method | Desk starts the pair or the chair |
| `pip install ag2 python-dotenv` | Command | Install AutoGen family and `.env` loader |
| `python campus_ops_pair.py` | Command | Run the daily ops pair |
| `python campus_ops_group.py` | Command | Run the placement-drive group |
