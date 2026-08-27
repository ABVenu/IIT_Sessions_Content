# Pre-read: AutoGen: Hands-on — End-to-End Multi-Agent System

## Context of This Session in the Course

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 70, "rankSpacing": 90, "diagramPadding": 24}} }%%
flowchart TB
  subgraph Foundation["What Students Bring Into This Session"]
    M1["<b>Previous Module</b><br/>Agentic Foundation & Architecture<br/><i>[Python + LLM Basics]</i><br/>Prompts, APIs, agent concepts"]
    M2["<b>Previous Module</b><br/>Agent Components - Memory, Tools & RAG<br/><i>[Memory + Retrieval]</i><br/>Chunking, vectors, RAG pipeline"]
    M3["<b>Previous Module</b><br/>Hands-On Single-Agent Development<br/><i>[LangChain + eval loop]</i><br/>Tools, memory, debug & iterate"]
  end

  CM[["<b>Current Module Until Previous Session</b><br/>Multi-Agent Collaboration and Deployment<br/><i>[n8n + CrewAI production crews]</i><br/>Tools, process choice, validation"]]

  CS{{"<b>Current Session</b><br/>AutoGen: Hands-on — End-to-End Multi-Agent System<br/><i>[Hotel Guest Complaint Intake Desk]</i><br/>Mental shift: from ticket-shaped crews to one conversable intake product"}}

  subgraph Value["Why This Matters"]
    CV["<b>Course Value</b><br/>Intake, classify, tools, ticket<br/>Speaker rules and stop stamps"]
    RV["<b>Real-Life Value</b><br/>Guest complaint in<br/>Case id out, trace to audit"]
  end

  subgraph Future["Where This Leads"]
    F4["<b>Current Module Ahead</b><br/>Multi-Agent Collaboration and Deployment<br/><i>[graph-shaped agent workflows]</i><br/>Nodes, edges, and stateful graphs"]
    F5["<b>Upcoming Module</b><br/>Capstone Project - Autonomous System Build<br/><i>[Architecture + Prototype]</i><br/>End-to-end autonomous system"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Components&nbsp;| M3
  M3 ==>|&nbsp;Scale up&nbsp;| CM
  CM ==>|&nbsp;AutoGen desk&nbsp;| CS
  CS ==>|&nbsp;Course Path&nbsp;| CV
  CS ==>|&nbsp;Real-Life Use&nbsp;| RV
  CS ==>|&nbsp;Next Steps&nbsp;| F4
  F4 ==>|&nbsp;Capstone Prep&nbsp;| F5

  classDef previous fill:#eef6ff,stroke:#4b83c3,stroke-width:2px,color:#0f2540;
  classDef current fill:#fff4cc,stroke:#d99a00,stroke-width:3px,color:#2d2100;
  classDef value fill:#eefaf1,stroke:#4c9f63,stroke-width:2px,color:#16351f;
  classDef future fill:#f4efff,stroke:#7b61c8,stroke-width:2px,color:#261c45;

  class M1,M2,M3,CM previous;
  class CS current;
  class CV,RV value;
  class F4,F5 future;
  linkStyle default stroke-width:3px;
```

---

The **previous** session was a production-style **CrewAI** workflow: custom tools, process choice, optional memory, a validation checklist, and iteration on one weak prompt. That model is excellent when the job is a **fixed ticket list** — research, then write, then review.

This session does **not** continue that story. You will build a **new** product: a **Hotel Guest Complaint Intake Desk** in **AutoGen**. A guest writes “AC not cooling in 412, booking BK-7781.” Specialists intake, classify, look up the stay, file a ticket, and stop. WhatsApp groups bury the trail. A chatbot invents booking ids. A weekly crew is heavy for a midnight AC complaint.

That is where AutoGen enters: named seats, registered tools, a chair, and a **TICKET_CREATED** stamp you can audit.

---

## When a ticket crew is the wrong shape

Picture a hotel night manager. The guest is already in the lobby. The job is not a weekly research brief. The job is: understand the complaint, tag the category, check the booking, issue a case id, stop.

A single chatbot can talk fluently and still invent room 412. A rigid crew can feel heavy for one complaint. A pair with no chair is noisy when intake, classify, and clerk must share **one** thread. A group with no stop rule is an endless meeting.

---

## The challenge we will tackle

What if one incoming guest message had to be clarified, classified, looked up on an approved stay register, filed as a ticket, and stopped on an explicit stamp — with the right specialist speaking at each step, and a trace you can audit?

This session focuses on that **end-to-end** product using AutoGen’s conversable-agent model **inside** a chaired group.

---

## Four seats in one chaired room

AutoGen treats agents as **participants in a conversation**, not only as static role cards on a CrewAI task board.

| Piece | Simple role | What it typically does |
|---|---|---|
| **AssistantAgent** | The specialist | Plans, reasons, replies, and can suggest **registered** tools |
| **UserProxyAgent** | The desk runner | Starts the request, can run tools, and helps control when the run ends |
| **GroupChat** | The shared room | Keeps every specialist contribution in one traceable thread |
| **GroupChatManager** | The chair | Applies flow and stop rules so the meeting stays structured |

In simple Indian English, a **conversable agent** is an AI participant that can send messages, receive replies, and continue until a defined stop point. **Orchestration** means managing turn-taking so a group stays purposeful instead of chaotic.

The power comes from pairing those pieces with boundaries:

1. **System messages** — Seat, limits, and stop phrase. Intake must not create tickets. Classifier must not look up stays.
2. **Registered tools** — Approved helpers (`register_function`) with a **caller** who may suggest and an **executor** who may run.
3. **Termination conditions** — A keyword (`TICKET_CREATED` / `TERMINATE`) or a maximum number of turns.
4. **Speaker selection and max rounds** — Who speaks next, including the desk runner when a tool must execute.

Optional **code execution** and always-on **human input** exist in AutoGen. This lab keeps code execution **off** and the demo automatic, so you can see tools and handoffs clearly.

Together, these pieces turn “agents chatting” into a **delegated front-office desk** you can inspect.

---

## From guest message to stamp

Keep the hotel story primary. CrewAI remains last session’s **skill**, not this session’s plot.

| Behaviour | AutoGen idea | Hotel mapping |
|---|---|---|
| Desk starts the case | UserProxyAgent | HotelDeskRunner |
| Intake / classify / clerk | AssistantAgent specialists | Non-overlapping seats |
| Approved stay lookup and ticket create | register_function | Clerk suggests; desk executes |
| “Case id stamped” | Termination | `TICKET_CREATED` / `TERMINATE` |
| Shared thread + chair | GroupChat + GroupChatManager | One intake meeting |
| Right person next | Speaker selection | Intake → classify → clerk; tools → desk |
| Meeting cannot run forever | Max rounds | `max_round` as a bell |
| Audit file | Conversation trace | Who spoke, which tool ran |

Once you see it this way, AutoGen is not “more chat for chat’s sake.” It is a **controlled dialogue loop** packaged as one guest-facing desk.

---

## Why registration, termination, and a chair matter

Giving an agent tools is like giving a new employee access cards. If everyone gets every card, confusion and risk increase.

**Registering a function** means officially connecting a helper so the assistant can call it under defined rules. The agent should not silently invent tool results. The trace should show **when** a tool was called and **what** came back.

**Termination conditions** solve endless loops. Without them, two agents keep agreeing or chasing minor details.

**Speaker selection** and **max rounds** solve the two most common group failures: **wrong speaker** (the classifier invents a ticket id) and **runaway dialogue**. The fix usually lives in **configuration** — the ladder, the role text, or the round cap.

Professionals do not only ask, “Did it answer?” They ask, “Did it use the right tools, did the right specialist speak, did it stop at the right time, and is there a trace I can verify?”

---

## How this fits with what you already know

You already understand tools, specialist roles, and validation from CrewAI. Crews remain strong when **roles, tasks, and process order** are the main design unit. AutoGen shines when one **incoming request** must be clarified, classified, looked up, and filed under a chair.

Do not force a midnight AC complaint through three CrewAI research tasks. Do not put a yes/no CRM flag through four specialists if a no-code router would do.

**Upcoming** work draws the same kind of workflow as a **graph**: nodes and edges instead of a chat chair. Mastering seats, tools, stop rules, and traces here gives you a clean foundation.

---

In this pre-read, you'll discover:

- **Understand** how conversable AutoGen agents — with clear system messages — form intake, classify, clerk, and desk-runner seats
- **Discover** why **registered tools**, a **caller/executor** split, and `TICKET_CREATED` turn dialogue into a case you can inspect
- **Learn** how **GroupChat**, **speaker selection**, and **max rounds** keep tools executable and the chat finite
- **Understand** how to read a **conversation trace** and apply one configuration fix for missing tools, wrong speaker, deadlock, or a missing stop stamp

---

## What's next

After this session, you should be able to explain the Hotel Guest Complaint Intake Desk in everyday language: who clarifies, who labels, who may suggest tools, who executes them, and what stamp means the job is done.

You will also discuss **safe tool access**, **termination**, and **orchestration**: why the desk runner must speak when a tool is suggested, why a round limit is necessary, and what the trace must show before you trust the confirmation.

Most importantly, you will review a run like a professional. Instead of saying “the chat failed,” you will name the layer — system message, registration, stop rule, or speaker / round cap — and change only that.

---

## Questions to think about before class

1. For `"Towels not replaced in room 208, booking BK-3301"`, how would you divide **intake**, **classify**, **clerk**, and **desk runner** so only the clerk path can create a ticket?

2. Which **tools** should be registered, who should **execute** them, and what **termination** stamp proves the case is filed?

3. If the clerk suggests `lookup_guest_stay` but the next speaker is still the classifier, which failure is that — and what speaker-rule change would you try first?

4. If the confirmation looks correct but the **trace** shows no tool calls, what would you change first, and why is that configuration rather than “AutoGen is broken”?

By the end, AutoGen should feel less like “chatbots talking” and more like a **designed hotel desk** — complaint in, ticket id out, trace you can audit.
