# Assignment Subjective

Total Questions: 8
Difficulty: Medium
Type: Applied Theory (English answers — no code)

---

Answer all eight questions below in your own words. Write in clear English paragraphs or bullet points. No code is required.

Keep each answer between **40 and 120 words** unless a question asks for a specific count.

---

## Q1

A college club wants a system where a daily report is generated automatically after new form submissions are received. Explain what **automation** means in this context, and also explain how a **workflow** is different from a **trigger**.

---

## Q2

Sana is an HR coordinator who is not comfortable with coding. She wants to set up onboarding steps like: collect details, store them, and create a ticket for the IT team. Explain why a **visual workflow tool** like n8n can help non-technical users. Also mention what part still requires careful decision-making (example: order of steps or mapping fields).

---

## Q3

A university wants to start a process when a student fills a “Course Feedback” form. After that, it should compute a dynamic result (for example, categorize feedback sentiment) and store it in a spreadsheet. In your answer:
1. Which **trigger type** starts the process?
2. What roles do **nodes** and **connections/data flow** play in moving the form data forward?

---

## Q4

One of your friends claims: “To use n8n, Docker is mandatory.” Write a clear reply. Your answer must include:
- What **n8n** is (in simple words)
- What **Docker** is (in simple words)
- Why Docker is useful for **self-hosted learning**, even though n8n can also run without Docker in hosted mode

---

## Q5

Explain the difference between **image**, **container**, and **volume** in Docker, but in the context of running n8n locally. Also state clearly which of these is mainly responsible for keeping workflow data after you stop the server and restart it.

---

## Q6

An organization integrates n8n with Google Sheets. Explain:
- What **credentials** do inside n8n
- What **OAuth2** achieves at a high level (no need for client-id technical steps)
- One security best practice related to permissions

---

## Q7

A workflow receives changing input values (like marks or ratings). Explain what **expressions** do, and why they are better than hard-coding values inside the workflow.

Use one short mini-example in plain English (no code) like “if marks are in a range, set grade”.

---

## Q8

During testing, a workflow fails at the third step. Describe two practical ways **observability** helps you debug. Then describe one situation where you would add a **human-in-the-loop** approval gate (example: refunds or security escalations) and why.

---

## Submission Instruction

- Type your answers to all eight questions in the answer box in the LMS.
- Label each answer clearly (**Q1**, **Q2**, ..., **Q8**).
- Write in English only. No code is required.

---

## Answer Explanation (Ideal Solution Walkthrough)

### Q1 — Automation vs trigger vs workflow
- **Automation:** running steps automatically when a condition/event happens, with minimal human effort.
- **Trigger:** the “start signal” (e.g., form submission, schedule, webhook call).
- **Workflow:** the whole connected sequence of nodes that starts from the trigger and produces an outcome.

### Q2 — Why n8n helps non-technical users
- Visual canvas and drag-and-drop reduce need to code every integration.
- Node-based steps make the process understandable.
- Still, someone must map fields correctly and choose the right order of steps (data dependencies).

### Q3 — Trigger + nodes + connections/data flow
1. Trigger type: **on form submission** (form trigger).
2. Nodes: each step (compute/categorize, then store).
   Connections: carry output from the form node to the next nodes so the data keeps moving in the correct shape.

### Q4 — n8n vs Docker independence
- n8n is the workflow automation application (triggers, nodes, integrations, UI).
- Docker is a packaging/runtime helper to run apps in isolated boxes.
- Docker is useful for self-hosted learning because it gives a repeatable setup locally.
- n8n cloud can run in the browser without Docker on the user’s machine.

### Q5 — Docker terms for n8n
- **Image:** packaged n8n software bundle downloaded once.
- **Container:** running instance of that image.
- **Volume:** persistent storage for n8n data; keeps workflows/settings across restarts.

### Q6 — Credentials + OAuth2 + permissions best practice
- Credentials: stored secure authorization data (API keys/tokens) used by nodes.
- OAuth2: high-level authorization/permission granting without sharing password.
- Best practice: request only the minimum permissions needed (scopes).

### Q7 — Expressions and dynamic computation
- Expressions compute values at runtime based on input data.
- They prevent hard-coded logic from breaking when inputs change.
- Mini-example: “if rating is 5, mark it as high priority; otherwise low/medium”.

### Q8 — Observability + human approval
- Observability: inspect node inputs/outputs and see where data shape mismatched or where the error occurred.
- Logging/tracing decisions helps understand the failure cause.
- Human-in-the-loop: needed for high-stakes actions like refunds, transfers, or security escalations to avoid costly mistakes.

