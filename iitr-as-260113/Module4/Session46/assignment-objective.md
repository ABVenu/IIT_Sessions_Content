# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

Ravi wants to connect **Google Sheets** and **Slack** so that every new row in a sheet sends a message automatically. Which tool description best fits this job?

A. A workflow automation platform where you build connections on a visual canvas  
B. A language model that writes text responses only  
C. A database that stores only application data  
D. A CSS framework for styling web pages

**Correct Answer:** A

**Answer Explanation:**  
This is **workflow automation**. A platform like n8n helps you connect apps visually and run steps when conditions/events happen.

Why other options are wrong:
- B: LLMs generate text, but they do not automatically orchestrate integrations across apps by themselves.
- C: Databases store data; they do not create multi-step automation flows.
- D: CSS frameworks style UI; they do not implement triggers and nodes.

---

## Q2 (MCQ, Easy)

An HR team collects onboarding details using an n8n form. The workflow should start automatically when a person submits that form. Which trigger type should be used?

A. Trigger manually  
B. On a schedule  
C. On a webhook call  
D. On form submission

**Correct Answer:** D

**Answer Explanation:**  
When a form is submitted, the workflow starts from the **form submission trigger** (form trigger).

Why other options are wrong:
- A: Manual trigger runs only when you click execute.
- B: Schedule runs on time (daily/hourly/etc.).
- C: Webhook starts when an external system calls an HTTP endpoint.

---

## Q3 (MCQ, Easy)

In n8n, you draw a canvas with connected blocks. What does a **node** represent?

A. The secret key used to log in to a service  
B. A connector that passes data between nodes  
C. A single step (action or decision) in the workflow  
D. A formula used only for login

**Correct Answer:** C

**Answer Explanation:**  
A **node** is one action or one decision step on the canvas, like "send email" or "if condition".

Why other options are wrong:
- A: That is **credentials**, not a node.
- B: That is a **connection**.
- D: Login formulas are not the purpose of nodes.

---

## Q4 (MCQ, Moderate)

A workflow needs to assign a grade based on input marks. The marks can change for different students. Which n8n feature is best suited to compute the grade dynamically?

A. Hard-code the grade in the workflow and never change it  
B. Use an **expression** to compute the grade at runtime  
C. Store the grade inside **credentials**  
D. Use OAuth2 to calculate grades

**Correct Answer:** B

**Answer Explanation:**  
An **expression** computes values dynamically based on the workflow input at runtime.

Why other options are wrong:
- A: Hard-coding breaks automation because grades must change per input.
- C: Credentials store access permissions, not computed values.
- D: OAuth2 is about authorization, not runtime calculations.

---

## Q5 (MCQ, Moderate)

You are running n8n locally using Docker. You want to use an API key without putting it directly into the workflow. Which statement is most correct?

A. Docker is only for desktop UI themes, so environment variables do not apply  
B. Environment variables are a common way in self-hosting to provide secrets to the running app  
C. OAuth2 replaces the need for any environment variables in self-hosting  
D. Credentials should be written in plain text inside workflow connections

**Correct Answer:** B

**Answer Explanation:**  
In self-hosting, secrets can be provided through **environment variables** so the running container reads them at startup/runtime.

Why other options are wrong:
- A: Environment variables are a standard mechanism for configuration and secrets.
- C: OAuth2 is for third-party authorization scopes; it does not eliminate secret management patterns.
- D: Plain-text secrets in workflows is unsafe.

---

## Q6 (MCQ, Moderate)

The workflow must run every day at 10:00 AM and generate a report from yesterday's data. Which trigger is best?

A. Trigger manually  
B. On a schedule  
C. On webhook call  
D. On app event

**Correct Answer:** B

**Answer Explanation:**  
Time-based execution uses a **schedule trigger**.

Why other options are wrong:
- A: Manual execution does not happen automatically every day.
- C: Webhook triggers on external HTTP events.
- D: App event triggers on a change in a connected app (like sheet row created).

---

## Q7 (MSQ, Moderate)

Which statements are correct about why n8n is useful for automation?

A. You can build multi-step automations by connecting nodes visually on a canvas  
B. You can use integrations to connect many external apps (like spreadsheets and chat tools)  
C. Observability means you can inspect the input/output of nodes during execution  
D. n8n requires multi-agent architecture for every workflow, even for simple tasks

**Correct Answers:** A, B, C

**Answer Explanation:**  
n8n helps build automations visually (A), provides many integrations (B), and provides observability per node (C). Multi-agent design is not mandatory for every workflow.

Why other options are wrong:
- D: n8n can be used for simple single-step or single-flow automations too.

---

## Q8 (MSQ, Moderate)

A workflow connects to Google Sheets. Which statements about **credentials** and **OAuth2** are correct?

A. Credentials in n8n store authentication information (like API keys/tokens) securely  
B. OAuth2 is a way for a third-party app to get limited access without sharing your password  
C. Minimum-permission idea applies: OAuth2 scopes should request only what is needed  
D. OAuth2 is only for cloud-hosted n8n; self-hosted setups never use OAuth2

**Correct Answers:** A, B, C

**Answer Explanation:**  
Credentials authorize access securely (A). OAuth2 is authorization with limited scopes and not password sharing (B). Minimum permissions is part of secure OAuth design (C). Both cloud and self-hosted can use OAuth2 depending on integrations.

Why other options are wrong:
- D: OAuth2 can be used in both hosting styles.

---

## Q9 (MSQ, Hard)

In Docker-based self-hosting, which statements correctly describe Docker terms for n8n?

A. An image is the packaged installer/bundle that Docker downloads  
B. A container is the running instance of that image on your machine  
C. A volume is used to persist saved data (like workflows) between restarts  
D. An image and a container are always identical and interchangeable

**Correct Answers:** A, B, C

**Answer Explanation:**  
Docker uses an **image** as the packaged app, a **container** as the running process, and a **volume** to persist data like workflows.

Why other options are wrong:
- D: An image is not the same as a running container.

---

## Q10 (MSQ, Hard)

When debugging a failed workflow execution in n8n, which statements are correct?

A. Observability helps by letting you inspect node inputs/outputs to find where data breaks  
B. Logging decisions or steps helps you trace why a workflow failed  
C. Human-in-the-loop is important for high-stakes actions such as refunds or transfers  
D. Observability guarantees correctness, so you do not need error handling or approvals

**Correct Answers:** A, B, C

**Answer Explanation:**  
Observability lets you inspect node I/O (A). Tracing steps/decisions improves debugging (B). Human approval is recommended for critical actions (C). Observability is not a guarantee of correctness (D).

Why other options are wrong:
- D: You still need safe design choices, error handling, and approval gates where appropriate.

