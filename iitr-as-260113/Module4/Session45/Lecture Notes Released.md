# Multi-Agent Architecture, HTTP, and Automation Foundations

## Context of This Session

In the **previous** module you built **single-agent** applications with LangChain — tools, memory, RAG, evaluation, and a real **HR onboarding assistant**. You learned how one capable agent retrieves policy, calls tools, and escalates when evidence is missing.

This session opens a new module on **multi-agent collaboration and deployment**. Before you use frameworks like **N8N** or **CrewAI**, you need the **design vocabulary**: when to split work across agents, how data passes between them, and how agents talk to the outside world through **HTTP**, **triggers**, **webhooks**, and **automation chains**.

**In this session, you will:**

- **Compare** single-agent and multi-agent architectures and decide when specialized agents are worth the complexity
- **Decompose** complex goals into sub-tasks with clear **role ownership** and **handoff points**
- **Contrast** **sequential pipelines** and **collaborative workflows** using a content-creation example
- **Explain** how **HTTP APIs** let agents and automation tools read from and write to external systems
- **Relate** **triggers**, **events**, and **webhooks** to starting and chaining agent workflows

![Single-agent vs multi-agent architecture — one overloaded agent wearing many hats compared with specialized research, writer, review, and editing agents passing work forward](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session45/session45-01-multi-agent-overview.png)

---

## Why Multi-Agent Thinking Matters

Until now, one agent could handle research, writing, tool calls, and replies in a single loop. That works for many products — but real business processes often look like an **assembly line** with specialists at each step.

- **Official Definition:** A **multi-agent system** is an application where **multiple specialized agents** cooperate on a shared goal, each owning a narrow slice of the workflow.
- **In Simple Words:** Instead of one intern doing everything, you hire a **research intern**, a **writer**, an **editor**, and a **publisher** — each expert in one job.
- **Real-Life Example:** A **newsroom** does not ask one reporter to investigate, write, fact-check, and print the newspaper alone. Different desks hand work to the next desk in order — or send pieces back for revision.

The rest of this document builds that mental model step by step, then connects it to **HTTP** and **automation** — the plumbing that lets agents act on real systems.

---

## Single-Agent vs Multi-Agent Architecture

Whenever you build an agentic application, the architecture falls into one of two buckets:

| Architecture | What it means | Typical shape |
|---|---|---|
| **Single-agent** | One agent handles the full task end to end | One prompt, one loop, many tools/functions inside |
| **Multi-agent** | Several agents, each with a focused responsibility | Research agent → Writer agent → Review agent → … |

### The Content-Writing Flow (Class Example)

Publishing a public blog is **not** "open a doc and type." The natural human flow is:

1. **Research** the topic and gather facts
2. **Write** the first draft
3. **Review** for accuracy and tone
4. **Edit** — often multiple review/edit cycles
5. **Publish** the final content

- **Official Definition:** A **single-agent architecture** assigns all of these steps to **one agent** (often as separate functions inside the same codebase).
- **In Simple Words:** One person wears five hats — researcher, writer, reviewer, editor, and publisher.
- **Real-Life Example:** A solo **YouTube creator** who scripts, shoots, edits, and uploads alone — possible, but exhausting at scale.

**Could one agent technically do all five steps?** Yes — each step can be a function inside the same agent. **Should it always?** No — not when the workflow grows complex or production-critical.

### Limits of a Single Agent

When one agent keeps absorbing more responsibilities, several problems appear:

- **Bloat:** The agent's logic becomes huge and hard to change safely
- **Debugging pain:** If something breaks, you must trace through one massive flow
- **Bottleneck / single point of failure:** One overloaded agent slows everything down
- **Testing cost:** Any small change may require re-testing the **entire** agent, not just one step
- **Latency:** One agent doing everything sequentially takes longer than parallel specialists where possible

### When Multi-Agent Architecture Helps

A **multi-agent system** uses **multiple specialized agents**:

- **Research agent** — gathers topic, facts, and sources
- **Writing agent** — drafts content from research output
- **Review agent** — checks quality, accuracy, and policy fit
- **Editing agent** — applies fixes after review

- **Official Definition:** **Specialized agents** follow **role-based design** — each agent owns one primary responsibility instead of the whole pipeline.
- **In Simple Words:** Change the review rules? Open the **review agent** only — you do not rewrite the research or writing agents.
- **Real-Life Example:** At a **TCS** delivery team, the person who writes client proposals is not always the same person who signs off on legal compliance — roles are split on purpose.

### When to Stay with a Single Agent

Multi-agent is **not** free. More agents means more orchestration, more handoffs, and more things to monitor.

**Use multi-agent architecture only when:**

- The task is **complex enough** to justify multiple specialists
- Responsibilities are **genuinely different** (research logic ≠ editing logic)
- You need **independent testing** and **safer changes** per role

**Single-agent is fine when:**

- The use case is **simple and straightforward**
- One loop with a few tools already meets the business need
- Adding agents would add complexity without clear benefit

---

## Single Responsibility Principle in Agent Design

The instructor connected multi-agent design to a well-known software idea:

- **Official Definition:** The **Single Responsibility Principle (SRP)** says each module (or agent) should have **one reason to change** — one primary job.
- **In Simple Words:** Do not ask your **research agent** to also send payroll emails — give it one clear job.
- **Real-Life Example:** In a **dosa shop**, the person at the tawa does not also handle UPI payments at the counter — separation keeps quality high.

### Single File vs Multiple Agent Files

In a **single-agent architecture**, research, writing, review, and editing logic often live in **one large file**. Every change — even a tiny review-rule tweak — touches that same file and may force a **full re-test**.

In a **multi-agent architecture**, each agent lives in its **own boundary**. Update the research agent → test **only** the research agent. Writing, review, and editing agents stay untouched.

| Single-agent file | Multi-agent split |
|---|---|
| One change → retest everything | One change → retest one agent |
| Many "reasons to change" in one place | Each agent has one main reason to change |
| Hard to scale teams on the same codebase | Different people can own different agents |

---

## Parallelization vs Sequential Dependencies

Multi-agent systems can sometimes run work **in parallel** — but only when tasks are **independent**.

- **Official Definition:** **Parallelization** means executing tasks at the same time (e.g., different threads or services) when outputs do not depend on each other yet.
- **In Simple Words:** Two chefs can chop vegetables **at the same time** if neither needs the other's output first.
- **Real-Life Example:** At **Swiggy**, packing a order and printing the bill can happen together — but you cannot deliver before the food is cooked.

**Rule from class:** Tasks can run in parallel **if and only if** they are **not dependent** on each other. If Task 2 needs Task 1's output, you must wait — no parallel shortcut.

| Pattern | Can parallelize? | Example |
|---|---|---|
| T1 → T2 → T3 → T4 (strict order) | No | Research before writing |
| T1, T2, T3 independent | Yes | Fetch weather + fetch stock price + fetch news headline |
| Mixed pipeline | Partial | Parallel research on two topics, then one writer merges |

**Common mistake:** Forcing parallel agents on a **sequential** business process (write before publish) — you gain speed on paper but break correctness.

---

## Multi-Agent Decomposition

Before you assign agents, you must **break the problem apart**.

- **Official Definition:** **Multi-agent decomposition** is the process of splitting a complex use case into **smaller, manageable sub-tasks**, each suitable for one agent or step.
- **In Simple Words:** Like breaking exam preparation into **syllabus list**, **daily targets**, and **mock tests** instead of one vague "study everything."
- **Real-Life Example:** Planning a **family wedding** — venue, catering, invitations, and photography are separate workstreams with different owners.

### HR Recruitment Platform (Extended Class Example)

The instructor walked through an **HR recruitment platform** — a fresh example beyond prior course builds:

| Step | Sub-task | Possible agent role |
|---|---|---|
| 1 | Review applications and resumes | **Screening agent** — shortlists candidates |
| 2 | Notify shortlisted candidates | **Email agent** — sends congratulations + process overview |
| 3 | Schedule interviews | **Scheduling agent** — matches candidate + interviewer availability |
| 4 | Conduct rounds (DSA, system design, project, etc.) | Domain experts / interview agents |
| 5 | Collect feedback | **Feedback agent** |
| 6 | Send offer or rejection | **Decision / comms agent** |

**Decomposition simply means:** breaking a complex problem statement into **smaller and manageable tasks**. For multi-agent architecture, this step is **critical** — it tells you **how many agents** you need and **what each one owns**.

---

## Handoffs and Handoff Points

When Agent 1 finishes, Agent 2 needs **structured input** — not a vague "here you go."

- **Official Definition:** A **handoff** is the act of passing one agent's **output** as the next agent's **input**. A **handoff point** is the exact step where that transfer happens.
- **In Simple Words:** Like a **cricket relay** — the runner must pass the baton in the exchange zone, not halfway down the track.
- **Real-Life Example:** At **Microsoft**, an on-call engineer **hands off** open incidents to the next week's on-call person with notes on what was fixed and what is still burning.

**Key idea:** In a sequential pipeline, **every agent must pass data forward**. The output of Agent 1 becomes the input of Agent 2.

---

## Structured JSON Handoff — Research to Writer

The class used a **content-writing pipeline** with a concrete handoff from **research agent** to **writer agent**.

**Task:** Collect facts about **EV (electric vehicle) adoption in India**.

Instead of passing one plain string, production systems pass a **JSON object** with multiple fields:

```json
{
  "source_agent": "research_agent",
  "next_agent": "writer_agent",
  "task": "Collect facts about EV adoption in India",
  "result": "EV demand is rising in India. Charging infrastructure remains a key limitation.",
  "assumptions": ["Focus on Indian market", "Audience is beginner level"],
  "confidence": "medium",
  "missing_information": ["Exact state-wise breakdown not found in sources"],
  "sources": ["Source A", "Source B"]
}
```

**How this handoff works:**

- **`source_agent`** — who produced this packet (research agent)
- **`next_agent`** — who should consume it next (writer agent)
- **`task`** — the original research instruction
- **`result`** — factual summary the writer will turn into prose
- **`assumptions`** — constraints the writer must respect
- **`confidence`** — how complete the research feels (see scoring below)
- **`missing_information`** — gaps the writer (or a later agent) should not invent
- **`sources`** — audit trail for fact-checking

### Confidence Scoring (Example Logic from Class)

The instructor suggested a simple rule the **research agent** can compute:

| Sources found (out of 10 needed) | Confidence label |
|---|---|
| More than 8 | **High** |
| 5 to 7 | **Medium** |
| Less than 5 | **Low** |

- **Why it matters:** The **writer agent** can refuse to draft a long article on **low confidence** and ask for more research — especially in **collaborative** workflows (covered next).

![Structured JSON handoff and task decomposition — research agent passes a data packet with task, result, confidence, and sources to the writer agent, with HR recruitment steps broken into manageable sub-tasks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session45/session45-03-json-handoff-decomposition.png)

---

## Sequential Multi-Agent Pipeline

When agents run in a **fixed order** — A then B then C — you have a **sequential multi-agent pipeline**.

```
Research Agent  →  Writer Agent  →  Review Agent  →  Editing Agent  →  Publish
     │                  │                │                  │
     └──── handoff ─────┴──── handoff ───┴──── handoff ─────┘
```

- **Official Definition:** A **sequential pipeline** is a workflow where each agent runs after the previous one completes, with one-directional flow unless explicitly redesigned.
- **In Simple Words:** An **assembly line** — the car door is attached **after** the frame exists, not before.
- **Real-Life Example:** **Passport application** — verification happens before printing; you cannot print first and verify later.

In the HR example, agents also walk in sequence: **shortlist → email → schedule interviews → …**

**Strengths:**

- Easy to reason about — clear order of operations
- Predictable data flow through handoff points
- Simpler orchestration than bidirectional collaboration

**Limitations:**

- Hard to send work **backward** for revision without extra design
- One slow step blocks the whole chain

---

## Collaborative Multi-Agent Workflow

![Sequential pipeline vs collaborative workflow — one-directional agent chain compared with bidirectional feedback loops managed by an orchestrator conductor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session45/session45-02-sequential-vs-collaborative.png)

Not every team process is a straight line. Sometimes agents must **talk back** to each other.

- **Official Definition:** A **collaborative multi-agent workflow** lets agents **interact bidirectionally** — sharing outputs, giving feedback, and revisiting earlier steps to improve quality.
- **In Simple Words:** A **study group** where the writer says, "Your research confidence is low — please find two more sources before I draft."
- **Real-Life Example:** A **Bollywood film shoot** — the director sends actors back for another take when a scene is not right; flow is not strictly one-way.

### Class Example: Writer Sends Work Back to Researcher

1. **Research agent** hands facts to **writer agent** with **confidence: low**
2. **Writer agent** responds: "I cannot write a strong article — please research more"
3. Flow returns to **research agent** for another pass
4. Cycle repeats until confidence is acceptable

This is **not** the same as a simple sequential pipeline — agents can loop and refine each other's output.

### The Agent Orchestrator

Collaborative and complex sequential systems often need an **orchestrator**.

- **Official Definition:** An **orchestrator** is a **workflow manager** (not an agent itself) that decides **which agent runs when**, what to do with each output, and when to loop or stop.
- **In Simple Words:** The **orchestra conductor** — not playing an instrument, but telling 50 musicians when to start, stop, and get louder.
- **Real-Life Example:** The conductor in a **symphony orchestra** coordinates timing across violin, drums, and flute sections for one final performance.

**Important:** The orchestrator is **not** an agent doing research or writing — it **manages the flow**.

### Trade-off: Quality vs Cost

| Sequential pipeline | Collaborative workflow |
|---|---|
| Faster, simpler | Slower, more resource-intensive |
| Less back-and-forth | Higher quality through feedback loops |
| Good for well-defined steps | Good when quality bar is high and tasks are ambiguous |

**Common doubt:** *"Should I always use collaborative workflows?"* — No. Use them when **quality gains** justify **extra time and compute**.

---

## Why HTTP Matters for Agentic AI

The second half of the session shifted to **HTTP** — the language agents use to reach the outside world.

- **Official Definition:** **HTTP (Hypertext Transfer Protocol)** is the standard **network protocol** for communication between **clients** and **servers** on the internet.
- **In Simple Words:** The **postal rules** every website and API follows when sending requests and receiving replies.
- **Real-Life Example:** When you open **IRCTC**, your browser (client) asks IRCTC's server for train data using HTTP — you do not manually wire a cable to their database.

### Agents Are Heavy HTTP Users

Agents **take actions** — they call tools. Almost every tool call over the network uses HTTP:

- Weather API lookup
- Database read/write through an API layer
- Sending email or creating a support ticket
- Updating **Google Sheets** or **Google Calendar**
- Calling **another agent** hosted as a separate service

**Key line from class:** Every request over the internet needs a protocol — for web APIs, that is **HTTP**.

![HTTP for agentic AI — agent as client sending requests to a server API with CRUD methods POST GET PUT DELETE, HTTPS security, and a 200 OK response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session45/session45-04-http-crud-client-server.png)

---

## Client-Server Architecture

HTTP conversations follow **client-server** roles:

```
Client  ── HTTP Request ──►  Server
Client  ◄── HTTP Response ──  Server
```

- **Client** — the party that **asks** (browser, Python script, your agent)
- **Server** — the party that **processes** and **responds** (Amazon backend, Razorpay, your FastAPI app)

**Agent as client:** When your agent calls MakeMyTrip's API, the **agent acts as client** and MakeMyTrip acts as **server**.

- **Why this matters:** Tool design maps cleanly to "my agent sends a request; the external system sends a response."

---

## HTTP vs HTTPS

Every URL you use starts with **`http://`** or **`https://`**.

| Protocol | Meaning | Security |
|---|---|---|
| **HTTP** | Hypertext Transfer Protocol | Data travels in **plain text** |
| **HTTPS** | HTTP **Secure** | Data is **encrypted** in transit |

- **Official Definition:** **HTTPS** is the secure, encrypted version of HTTP — same idea, extra protection layer (TLS/SSL).
- **In Simple Words:** HTTP is a **postcard** anyone can read in transit; HTTPS is a **sealed envelope**.
- **Real-Life Example:** You would not share your **UPI PIN** on a public notice board — HTTPS keeps payment and login data private on the wire.

**Class note:** For production apps (login, payments, personal data), always prefer **HTTPS** endpoints.

---

## CRUD Operations and HTTP Methods

Almost every internet operation is one of four types — **CRUD**:

| Letter | Operation | Meaning | HTTP method (typical) |
|---|---|---|---|
| **C** | **Create** | Add something new | **POST** |
| **R** | **Read** | Fetch existing data | **GET** |
| **U** | **Update** | Change existing data | **PUT** (sometimes PATCH) |
| **D** | **Delete** | Remove a resource | **DELETE** |

- **Official Definition:** **CRUD** maps business actions to four database/API patterns that HTTP methods express.
- **In Simple Words:** Your **phone contacts app** — add contact (create), open contact (read), edit number (update), remove contact (delete).
- **Real-Life Example:** **Amazon** — place order (POST/create), view order history (GET/read), cancel order (UPDATE status, not true delete), delete a saved address (DELETE).

### Method Examples from Class

| User action | CRUD type | HTTP method |
|---|---|---|
| Click **Buy Now** on Amazon | Create order | **POST** |
| Browse product listing | Read catalog | **GET** |
| **Sign up** for a new account | Create user record | **POST** |
| **Cancel** an order | Update status to "cancelled" | **PUT** (update) — order row usually stays in history |
| **Delete** a LinkedIn post | Remove resource | **DELETE** |

**Common mistake:** Thinking **cancel order = DELETE**. In most systems the order remains in your history — only the **status field changes** → that is an **update**.

---

## Anatomy of an HTTP Request

When an agent (or browser) calls an API, the request typically includes:

| Part | Purpose | Example |
|---|---|---|
| **URL** | Address of the API endpoint | `https://api.example.com/orders/123` |
| **Method** | CRUD intent | `GET`, `POST`, `PUT`, `DELETE` |
| **Headers** | Metadata — often **authentication** | `Authorization: Bearer <token>` |
| **Body** | Payload for create/update with many fields | JSON with email, password, address on sign-up |

### Headers and Login Tokens

After you log in to **Amazon**, you do not re-enter password for every click. Your browser stores a **token** and sends it in the **header** on later requests. The server validates the token before fulfilling the request.

- **Why agents care:** Tool calls to private APIs must attach the same kind of **auth header** your backend expects.

### Request Body

When you **sign up** or **place an order**, you send many fields (email, phone, address, product IDs). Those fields go in the **request body** — usually JSON for modern APIs.

---

## Anatomy of an HTTP Response

After the server processes your request, you receive an **HTTP response**:

| Part | Purpose |
|---|---|
| **Status code** | 3-digit summary — success, client error, or server error |
| **Headers** | Metadata about the response |
| **Body** | Data payload (JSON, HTML, etc.) |

### Common Status Codes (Mentioned in Class)

| Code | Meaning | Plain English |
|---|---|---|
| **200** | OK | Request succeeded |
| **401** | Unauthorized | Not logged in / bad credentials |
| **403** | Forbidden | Logged in but not allowed |
| **404** | Not Found | URL or resource does not exist |
| **500** | Internal Server Error | Something broke on the server |
| **502 / 503** | Bad Gateway / Service Unavailable | Server or upstream service down |

- **Agent debugging habit:** When a tool call fails, read the **status code first** — it tells you whether to fix auth (401), permissions (403), bad URL (404), or server outage (500).

---

## Sample Python — Making an HTTP GET Request

The instructor noted that upcoming classes will make requests hands-on. This minimal example shows the idea an agent's tool would wrap:

```python
# http_tool_demo.py — read public data from an API (GET = read)

import requests  # Popular library for HTTP calls in Python

# URL of the API endpoint we want to read from
url = "https://api.example.com/weather?city=Delhi"

# Send GET request — we are READING data, not creating anything
response = requests.get(url)

# Status code tells us success or failure (200 = OK)
print("Status code:", response.status_code)

# Response body is usually JSON — convert to Python dict
if response.status_code == 200:
    data = response.json()  # Parse JSON body into a dictionary
    print("Temperature:", data.get("temperature"))
else:
    print("Request failed — check URL, auth, or server health")
```

**How the code works:**

- **`requests.get(url)`** — client asks server to **read** a resource (GET method)
- **`response.status_code`** — quick health check before trusting body data
- **`response.json()`** — parses JSON body so the agent can use fields in its reply
- **Error branch** — agents should not assume 200; failed tool calls need visible handling

---

## Triggers — Starting a Workflow

Automation begins when **something happens** that should kick off a chain of actions.

- **Official Definition:** A **trigger** is any signal that **starts** an agent or automation **workflow**.
- **In Simple Words:** The **doorbell** — ring it and the whole house wakes up to respond.
- **Real-Life Example:** When a **job application** status changes to "shortlisted," HR sends email and schedules interview — the status change is the trigger.

**Triggering an agent = starting its workflow.**

### Trigger Examples from Class

| Event in business | Workflow that should start |
|---|---|
| Candidate **shortlisted** | Send email → schedule interviews → check availability |
| New **refund ticket** created | Route to accounts → ask for human approval |
| **Payment fails** | Trigger retry-payment workflow |
| New support ticket | Assign agent → notify on-call engineer |

**Pattern:** *When this happens → do that.* Triggers are the **"when"** in automation.

---

## Events — Recording That Something Happened

Triggers start work; **events** are the **records** that something occurred.

- **Official Definition:** An **event** is a stored record that a specific action or state change happened at a point in time.
- **In Simple Words:** Your **bank SMS** — "₹500 debited at 3:42 PM" is a permanent note that the transaction happened.
- **Real-Life Example:** **Order cancelled** on Flipkart — the platform keeps a log with timestamp and new status, not amnesia.

### Event Examples

- Order **created**
- Order **cancelled**
- Refund **issued** or **denied**
- User **created** or **deleted**
- Ticket **opened** or **closed**

**Class distinction:**

| Concept | Role |
|---|---|
| **Trigger** | Starts a workflow |
| **Event** | Documents that something happened (often stored in DB or event log) |

Many systems emit an **event** and also use it as a **trigger** for downstream automation — the terms overlap in practice but the ideas differ.

---

## Webhooks — HTTP Calls When Events Happen

A **webhook** is how an **external system notifies you** automatically — by calling **your** API over HTTP.

- **Official Definition:** A **webhook** is an **HTTP request** sent from one system to another **when a configured event occurs**.
- **In Simple Words:** Instead of you refreshing Razorpay every five seconds asking "payment done yet?", Razorpay **calls your phone** when payment completes.
- **Real-Life Example:** **Razorpay / PayPal / Stripe** on an e-commerce site — you register a URL; when payment succeeds or fails, the gateway **POSTs** the result to your server.

### Razorpay Flow (Class Walkthrough)

1. You integrate **Razorpay** on your business website
2. Customer clicks **Pay**
3. Payment succeeds, fails, expires, or OTP fails — each is an **event**
4. You configure: *"For these events, call my API URL"*
5. Razorpay sends an **HTTP request** to your endpoint with payment status
6. Your backend (or agent pipeline) reacts — update order, send email, retry payment

```
Customer pays on your site
        │
        ▼
   Razorpay processes payment
        │
        ▼ (event: payment_success / payment_failed / link_expired)
   Razorpay ── HTTP POST (webhook) ──► Your server's API URL
        │
        ▼
   Your workflow updates DB, notifies user, triggers agents
```

**Key insight:** A webhook **is** an HTTP request — just initiated by the **other** party when **their** event fires.

![Triggers events and webhooks in automation — a trigger starts an agent chain, events are recorded in a log, and a payment gateway sends an HTTP webhook callback to your server](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session45/session45-05-triggers-webhooks-automation.png)

---

## Automation and Agent Chains

The session closed by tying agents to **automation** — reducing manual repetition.

- **Official Definition:** **Automation** is the use of software workflows to perform business steps with minimal human effort.
- **In Simple Words:** **Auto-debit** for electricity bill — you do not visit the office every month.
- **Real-Life Example:** HR recruitment platform automates shortlist emails and interview scheduling so ten people are not copy-pasting the same mail all day.

### How Agents Fit Automation

Automation chains often look like:

```
Trigger → Agent 1 → Agent 2 → Agent 3 → External tool calls (HTTP)
```

- Chains can be **linear** (step 1 → 2 → 3)
- Chains can **branch** (if payment fails → retry branch; if success → fulfillment branch)
- **Agentic AI** is one way to implement intelligent steps inside those chains

### Production-Grade Multi-Agent + HTTP

In enterprise deployments, agents may run as **independent services**, communicate over **HTTP**, and react to **events** in an **event-driven architecture**. The exact layout depends on the product — but the building blocks from this session (agents, handoffs, HTTP, triggers, webhooks) repeat everywhere.

---

## Student Activities

Work through these on your own after reading each section. Each activity takes a few minutes and mirrors classroom discussion.

### Activity 1 — Single vs Multi-Agent Decision

**Scenario:** Build a chatbot that answers **FAQs from one PDF** (20 pages, rarely updated).

Write two sentences: Would you choose **single-agent** or **multi-agent**? List **one reason** for your choice using terms from this document (bloat, complexity, SRP, etc.).

---

### Activity 2 — Decompose the HR Platform

List **five sub-tasks** for the HR recruitment platform. Next to each, write one **agent role name** (e.g., `screening_agent`). Draw arrows showing which step must finish before the next begins.

---

### Activity 3 — Build a JSON Handoff

Copy the EV research JSON template from this document. Change the task to **"Summarise UPI growth in India"**. Fill in sample `result`, `confidence`, and `missing_information` fields as if you were the research agent.

---

### Activity 4 — Sequential vs Collaborative

**Scenario:** A legal team needs a contract draft where **accuracy is critical** and reviewers may send work back twice for fact checks.

Which pattern fits better — **sequential pipeline** or **collaborative workflow**? Write **two sentences** explaining why, mentioning **orchestrator** or **feedback loop**.

---

### Activity 5 — CRUD and HTTP Methods

For each action, write **CRUD letter** and **HTTP method**:

1. View your **Swiggy order history**
2. **Create** a new GitHub repository
3. **Update** your profile photo on LinkedIn
4. **Delete** an old tweet/post

---

### Activity 6 — Triggers, Events, and Webhooks

For an online course payment through Razorpay, identify:

1. One **trigger** that starts your post-payment workflow
2. One **event** you would store in your database
3. What **webhook** Razorpay sends and who is the HTTP **client** vs **server** in that call

---

## Key Takeaways

- **Single-agent** systems are enough for simple workflows; **multi-agent** systems shine when tasks are complex, roles differ, and you need safer changes and clearer debugging per step.
- **Decomposition**, **handoffs**, and **structured JSON** between agents turn vague "AI magic" into maintainable pipelines — sequential for straight lines, **collaborative** when agents must refine each other's work under an **orchestrator**.
- **HTTP** is how agents and automation tools **read and write** the real world — know **CRUD**, **methods**, **request/response** parts, and **status codes** before building tools.
- **Triggers** start workflows; **events** record what happened; **webhooks** deliver event notifications as **HTTP calls** from external systems like payment gateways.
- **Automation** chains agents and HTTP actions together — often with branches — and sets the foundation for building multi-agent applications with workflow tools in the **upcoming** part of this module.

---

## Important Terminologies Used

| Term | Quick meaning |
|---|---|
| **Single-agent architecture** | One agent handles the full workflow |
| **Multi-agent system** | Multiple specialized agents cooperate on one goal |
| **Specialized / role-based agent** | Agent with one primary responsibility (research, write, review, edit) |
| **Single Responsibility Principle (SRP)** | Each agent/module should have one main reason to change |
| **Multi-agent decomposition** | Breaking a complex use case into smaller manageable sub-tasks |
| **Handoff / handoff point** | Passing one agent's output as the next agent's input |
| **Sequential pipeline** | Agents run in fixed order (A → B → C) |
| **Collaborative workflow** | Agents interact bidirectionally and improve each other's output |
| **Orchestrator** | Workflow manager (not an agent) that controls execution order |
| **Parallelization** | Running independent tasks at the same time |
| **HTTP** | Hypertext Transfer Protocol — client-server communication on the web |
| **HTTPS** | Encrypted, secure version of HTTP |
| **Client / Server** | Requester vs processor in a network call |
| **CRUD** | Create, Read, Update, Delete — four core data operations |
| **GET / POST / PUT / DELETE** | HTTP methods mapping to read, create, update, delete |
| **Request body** | JSON or data payload sent with create/update requests |
| **Headers** | Metadata on requests/responses — often authentication tokens |
| **Status code** | 3-digit HTTP result (200 success, 404 not found, 500 server error) |
| **Trigger** | Signal that starts a workflow |
| **Event** | Record that something happened |
| **Webhook** | HTTP callback from an external system when an event occurs |
| **Automation** | Software chain that reduces manual work across steps |
| **Event-driven architecture** | Systems react to events (often via webhooks/HTTP) |
| **API** | Interface allowing programs to request services over HTTP |
| **JSON handoff** | Structured object passed between agents with task, result, confidence, etc. |
