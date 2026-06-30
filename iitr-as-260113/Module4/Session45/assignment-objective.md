# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**Meera** builds a chatbot that answers **20 FAQs from a single PDF** of company timings. The PDF rarely changes and the bot needs only one retrieval tool plus a reply loop.

Which architecture fits **best** for this use case?

A. **Single-agent** — the workflow is simple and one loop is enough  
B. Multi-agent with separate research, writer, review, and editing agents  
C. Collaborative workflow with an orchestrator and bidirectional loops  
D. Event-driven microservices with ten independent agents

**Correct Answer:** A

**Answer Explanation:**  
Simple, straightforward use cases where one agent with a few tools meets the need should stay **single-agent**. Multi-agent adds orchestration cost without clear benefit here.

**Why other options are wrong:**  
- B, C, D: Over-engineered for a small FAQ bot — unnecessary handoffs, monitoring, and complexity.

---

## Q2 (MCQ, Easy)

A startup wants an automated **blog pipeline**: research facts, draft articles, review accuracy, edit tone, and publish. Each step uses **different logic** and the team wants to **change review rules** without retesting the entire system.

What is the **main reason** to prefer a **multi-agent** design here?

A. Multi-agent always runs faster than single-agent for every task  
B. **Specialized agents** let each role change independently — easier testing and safer updates per step  
C. Single-agent systems cannot call HTTP APIs  
D. Multi-agent means you never need an orchestrator

**Correct Answer:** B

**Answer Explanation:**  
Role-based agents follow **Single Responsibility** — update the review agent alone without touching research or writing code, and retest only that agent.

**Why other options are wrong:**  
- A: Multi-agent can add latency; speed is not guaranteed.  
- C: Single agents can call tools over HTTP.  
- D: Complex multi-agent flows often need an orchestrator.

---

## Q3 (MCQ, Easy)

In a content-writing pipeline, the **research agent** finishes and passes a structured packet to the **writer agent**.

What is this transfer called?

A. **Handoff** — output of one agent becomes input of the next  
B. Webhook — external payment gateway calling your server  
C. DELETE request — removing a resource from a database  
D. Parallelization — running all agents at the same time always

**Correct Answer:** A

**Answer Explanation:**  
A **handoff** (or handoff point) is where one agent passes its **result** forward so the next agent can continue the workflow.

**Why other options are wrong:**  
- B: Webhooks are external HTTP callbacks on events — not inter-agent data passing.  
- C: DELETE is an HTTP method, unrelated to agent transfers.  
- D: Parallelization applies only when tasks are independent — research must finish before writing in this chain.

---

## Q4 (MCQ, Easy)

An **AI travel agent** needs to check flight prices on MakeMyTrip and send a confirmation email through an email API. Both calls happen over the internet.

Why does the agent rely on **HTTP** for these tool calls?

A. HTTP is only used for writing Python code locally  
B. **HTTP is the standard protocol** for client-server communication over the network — agents act as clients calling external APIs  
C. HTTP replaces the need for any LLM in agentic systems  
D. Agents never communicate with servers — only with users in chat

**Correct Answer:** B

**Answer Explanation:**  
Agents take actions via **tool calls**; network calls to weather APIs, databases, email services, and other agents typically use **HTTP** request/response.

**Why other options are wrong:**  
- A: HTTP is a networking protocol, not a local coding format.  
- C: HTTP carries requests; the LLM still reasons and plans.  
- D: Agents routinely call external systems, not only chat replies.

---

## Q5 (MCQ, Moderate)

**Arjun** cancels an **Amazon order** from his account history. The order row stays visible with status changed to **"Cancelled"**.

Which CRUD operation and HTTP method **best** describe this action?

A. **Delete (DELETE)** — the order row is removed from the database entirely  
B. **Update (PUT)** — the order status field changes; the record usually remains in history  
C. **Create (POST)** — a brand-new order is placed  
D. **Read (GET)** — only viewing the catalog without changes

**Correct Answer:** B

**Answer Explanation:**  
Cancel order typically **updates status** to cancelled — the order history remains. That is an **update**, not a true delete.

**Why other options are wrong:**  
- A: Most e-commerce systems keep cancelled orders in history.  
- C: Placing a new order is create/POST, not cancel.  
- D: GET reads data without modifying status.

---

## Q6 (MCQ, Moderate)

**BlogNova** runs agents in fixed order: **Research → Writer → Review → Publish**. Data flows one way unless the product team redesigns the pipeline.

Which workflow pattern is this?

A. **Sequential multi-agent pipeline** — agents run in a defined order with forward handoffs  
B. Collaborative workflow — writer and researcher loop bidirectionally by default  
C. Single-agent with no handoffs  
D. Webhook — Razorpay calling your server after payment

**Correct Answer:** A

**Answer Explanation:**  
A fixed A → B → C → D chain with one-directional flow is a **sequential pipeline**.

**Why other options are wrong:**  
- B: Collaborative allows agents to send work **back** for revision — not the default here.  
- C: Multiple named agents with handoffs is multi-agent, not single.  
- D: Webhooks are external HTTP callbacks, not internal agent ordering.

---

## Q7 (MSQ, Moderate)

A team compares **single-agent** vs **multi-agent** architecture for a growing product.

Which statements are **correct**?

A. A single agent doing hundreds of responsibilities can become a **bottleneck** and **hard to debug** at scale  
B. Multi-agent should be used **only when** complexity justifies multiple specialists — not for every small use case  
C. Multi-agent always eliminates the need to test any agent after changes  
D. **Parallelization** of agent tasks is possible only when those tasks are **not dependent** on each other's outputs

**Correct Answers:** A, B, D

**Answer Explanation:**  
Single-agent limits include bloat and debugging pain. Multi-agent is justified by complexity. Parallel work requires **independent** tasks.

**Why other options are wrong:**  
- C: You still must test agents when their logic changes — multi-agent reduces **full-system** retesting scope, not all testing.

---

## Q8 (MSQ, Moderate)

An agent tool sends an **HTTPS POST** request to create a support ticket. The server responds with status **401**.

Which statements about **HTTP requests and responses** are **correct**?

A. **POST** typically maps to **Create** in CRUD — adding a new ticket resource  
B. **401 Unauthorized** suggests an **authentication** problem — missing or invalid token/credentials  
C. **Headers** often carry authentication tokens after login  
D. **401** always means the server crashed — same as **500 Internal Server Error**

**Correct Answers:** A, B, C

**Answer Explanation:**  
POST creates resources. 401 = auth failure. Headers commonly store **Authorization** tokens.

**Why other options are wrong:**  
- D: **500** indicates server-side failure; **401** is a client auth issue — different fixes.

---

## Q9 (MSQ, Hard)

**GreenMobility** publishes EV adoption articles. The **writer agent** receives research output with **confidence: low** and asks the **research agent** to gather more sources before drafting. An **orchestrator** decides when to loop back.

Which statements about **collaborative workflows** are **correct**?

A. Agents can **interact bidirectionally** — not only strict one-way pipelines  
B. The **orchestrator** manages **which agent runs when** — it is a workflow manager, **not** a research/writing agent itself  
C. Collaborative workflows are always faster and cheaper than sequential pipelines  
D. Collaborative patterns can **improve output quality** through feedback loops but may use **more time and resources**

**Correct Answers:** A, B, D

**Answer Explanation:**  
Collaborative flows allow loops (writer → researcher). Orchestrator coordinates timing. Trade-off: higher quality vs higher cost/latency.

**Why other options are wrong:**  
- C: Collaborative workflows are typically **slower and more resource-intensive**, not always faster.

---

## Q10 (MSQ, Hard)

**CourseKart** sells online courses with **Razorpay** payments. When payment succeeds or fails, Razorpay should notify CourseKart's backend automatically so agents can update enrollment and send email.

Which statements about **triggers, events, and webhooks** are **correct**?

A. A **trigger** is a signal that **starts** a workflow — e.g. payment failure starting a retry-payment chain  
B. An **event** is a **record** that something happened — e.g. `order_created` stored with timestamp  
C. A **webhook** is an **HTTP request** from one system to another when an external event occurs — Razorpay **POSTing** payment status to CourseKart's API URL  
D. A webhook means CourseKart must poll Razorpay every five seconds manually — no HTTP call from Razorpay

**Correct Answers:** A, B, C

**Answer Explanation:**  
Triggers start automation. Events are logged occurrences. Webhooks push notifications via HTTP — Razorpay calls **your** server.

**Why other options are wrong:**  
- D: Polling is the opposite of webhooks — webhooks are **server-initiated callbacks** when events fire.
