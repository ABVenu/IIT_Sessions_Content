# Assignment Subjective

Total Questions: 8  
Difficulty: Medium  
Type: Applied Theory (English answers — no code)

---

Answer **all eight questions** below in your own words. Write in clear English paragraphs or bullet points. **No code, no JSON blocks, and no Google Doc link** is required — type everything directly in the LMS answer box.

Keep each answer between **40 and 120 words** unless a question asks for a specific count.

---

## Q1

**BlogKart** wants a bot that answers **15 FAQs from one company policy PDF**. The PDF changes once a year.

Explain the **difference between a single-agent architecture and a multi-agent architecture** in your own words. Then state which approach fits **BlogKart's FAQ bot better** and give **two reasons** for your choice.

---

## Q2

A team builds an automated **content pipeline**: research a topic → write a draft → review facts → edit tone → publish.

List **four problems** that can happen if all five steps are handled by **one single agent** instead of separate specialized agents. Use terms such as **bloat**, **debugging**, **testing**, or **bottleneck** where they apply.

---

## Q3

What is **multi-agent decomposition**?  

Using the **HR recruitment platform** idea (review resumes → email shortlisted candidates → schedule interviews → collect feedback → send offer/rejection), break the workflow into **four sub-tasks**. For each sub-task, write **one agent role name** and **one line** describing what that agent owns.

---

## Q4

What is a **handoff** (or **handoff point**) in a multi-agent system?  

Describe **without writing JSON code** what information the **research agent** should pass to the **writer agent** when the topic is *"EV adoption in India"*. Mention **at least four** useful fields (e.g. task summary, confidence level, sources) and explain why structured handoffs are better than passing one vague sentence.

---

## Q5

Compare **sequential multi-agent pipeline** and **collaborative multi-agent workflow**.

| Your answer must cover |
|---|
| How data flows in a **sequential** pipeline |
| How agents can interact in a **collaborative** workflow |
| **One situation** where sequential is enough |
| **One situation** where collaborative is the better fit |

---

## Q6

What is an **orchestrator** in a multi-agent system?  

Explain whether the orchestrator **is or is not** the same as a research agent or writer agent. In **two sentences**, describe what happens when the **writer agent** receives research output with **low confidence** in a collaborative design.

---

## Q7

An AI agent needs to **read weather data**, **place an order on an e-commerce site**, and **update a Google Sheet**.

1. Why do agents use **HTTP** for these actions?  
2. What is the **difference between HTTP and HTTPS**? Give **one example** where HTTPS is required.  
3. A user **cancels an Amazon order** but the order still appears in history with status **"Cancelled"**. Is this **Create, Read, Update, or Delete**? Which **HTTP method** (GET, POST, PUT, or DELETE) best matches this action? Explain briefly.

---

## Q8

**CoursePay** sells online courses. Customers pay through a payment gateway (like Razorpay). When payment succeeds or fails, CoursePay's backend must react automatically.

In your own words, explain:

1. What is a **trigger**? Give **one CoursePay example**.  
2. What is an **event**? Give **one example** CoursePay should **store in a database log**.  
3. What is a **webhook**? Who is the HTTP **client** and who is the **server** when the payment gateway notifies CoursePay?  
4. How is a webhook **different from** CoursePay manually refreshing the payment page every few seconds?

---

### Submission Instruction

- Type your answers to **all eight questions** in the answer box in the LMS  
- Label each answer clearly (**Q1**, **Q2**, … **Q8**)  
- Write in English only — **no code** required

---

## Answer Explanation (Ideal Solution Walkthrough)

### Q1 — Single-agent vs multi-agent

| Point | Ideal answer |
|---|---|
| **Difference** | **Single-agent:** one agent handles the full workflow end to end (often many functions inside one loop). **Multi-agent:** several **specialized agents**, each owning one primary role, passing work forward or collaborating. |
| **BlogKart choice** | **Single-agent** — FAQ from one small PDF is simple; one retrieval tool + reply loop is enough. |
| **Reasons** | (1) Use case is **straightforward** — multi-agent adds unnecessary orchestration. (2) No need to split research/write/review roles for static FAQs. |

### Q2 — Single-agent problems at scale

Model points (any four): **Bloat** — logic becomes huge; **Debugging pain** — hard to trace failures in one massive flow; **Testing cost** — small change forces retesting entire agent; **Bottleneck / single point of failure** — one overloaded agent slows everything; **Latency** — all steps serial in one agent vs parallel specialists where possible.

### Q3 — Decomposition + HR roles

**Decomposition:** breaking a complex use case into **smaller, manageable sub-tasks**, each with clear ownership.

| Sub-task | Agent role | Responsibility |
|---|---|---|
| Resume screening | `screening_agent` | Review applications and shortlist candidates |
| Shortlist notification | `email_agent` | Send congratulations and process overview email |
| Interview scheduling | `scheduling_agent` | Match candidate and interviewer availability |
| Final decision | `decision_agent` | Collect feedback and send offer or rejection |

Four distinct rows required; naming variations OK if responsibilities are clear.

### Q4 — Handoff

**Handoff:** passing one agent's **output** as the next agent's **input** at a defined step.

Useful fields (any four+): **task/topic**, **factual result/summary**, **sources**, **confidence** (high/medium/low), **assumptions** (audience, market), **missing_information** gaps writer must not invent.

**Why structured:** gives writer audit trail, sets expectations, prevents hallucination on weak research — better than *"here are some EV facts"* with no source or confidence context.

### Q5 — Sequential vs collaborative

| Pattern | Ideal points |
|---|---|
| **Sequential** | Fixed order A → B → C; one-directional handoffs; e.g. research then write then publish in strict order. |
| **Collaborative** | Agents interact **bidirectionally** — writer can send work back to researcher; review can loop to editing. |
| **Sequential enough** | Simple, well-defined steps with no need to revisit earlier agents — e.g. HR shortlist → email → schedule in one pass. |
| **Collaborative better** | High accuracy bar — writer rejects **low-confidence** research; legal/medical content needing multiple revision loops. |

### Q6 — Orchestrator

**Orchestrator:** a **workflow manager** (not a content agent) that decides **which agent runs when**, handles loops, and when to stop.

**Not** a research or writer agent — it does not gather facts or draft prose; it **coordinates** agents.

**Low-confidence example:** Writer tells orchestrator/research path that confidence is too low → flow returns to **research agent** for more sources before drafting continues.

### Q7 — HTTP, HTTPS, CRUD

1. **HTTP:** standard **client-server protocol** for network tool calls — agents act as **clients** calling external APIs (weather, orders, sheets).  
2. **HTTPS:** encrypted secure HTTP; plain HTTP sends data in readable form. **HTTPS required** for login, payments, UPI/card checkout, personal data.  
3. **Cancel order:** **Update (U)** — status field changes to cancelled; record stays in history. Method: **PUT** (update), **not DELETE** — order row is not removed.

### Q8 — Trigger, event, webhook

1. **Trigger:** signal that **starts** a workflow — e.g. **payment_failed** starts retry-payment or alert workflow.  
2. **Event:** **stored record** that something happened — e.g. `payment_success` logged with user ID, amount, timestamp.  
3. **Webhook:** **HTTP request** (often POST) from payment gateway (**client**) to CoursePay API URL (**server**) when payment completes.  
4. **Vs polling:** Webhook is **push** — gateway calls you when ready. Polling is **pull** — you repeatedly ask *"done yet?"* — wasteful and slower.

### Common mistakes (all questions)

- Saying multi-agent is always better.  
- Calling orchestrator a writing/research agent.  
- Mapping cancel order to DELETE.  
- Describing webhook as polling.  
- Confusing trigger (starts work) with event (records what happened).  
- Submitting code or JSON instead of English explanations.

### Alternative valid approaches

- Q1: Valid if student picks multi-agent but must justify with strong reasons (generally weaker for FAQ bot).  
- Q3: Content-writing agents acceptable **only if** four clear steps with roles — HR example preferred but parallel structure OK.  
- Q7: PATCH accepted instead of PUT for update if student notes partial update semantics.
