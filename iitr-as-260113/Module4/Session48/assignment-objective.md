# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

Priya runs n8n locally with Docker. She wants to build the Gmail → LLM → Gmail pipeline on her laptop. Which URL opens the n8n editor?

A. `http://localhost:5678`  
B. `http://localhost:5000`  
C. `https://mail.google.com`  
D. `http://localhost:3000`

**Correct Answer:** A

**Answer Explanation:**  
Local self-hosted n8n exposes the workflow canvas at **`http://localhost:5678`**.

Why other options are wrong:
- B and D: Common dev ports, but n8n’s default local UI port is **5678**.
- C: Gmail webmail is where emails are read/sent, not where you design n8n workflows.

---

## Q2 (MCQ, Easy)

**CodeBridge Solutions** wants a workflow that starts automatically when a new email arrives from an approved contractor — without anyone clicking **Execute workflow**. Which trigger fits best?

A. Trigger manually  
B. Gmail → On message received  
C. On form submission  
D. On a schedule only

**Correct Answer:** B

**Answer Explanation:**  
An **on app event** Gmail trigger with **On message received** polls the inbox and starts the workflow when matching mail arrives.

Why other options are wrong:
- A: Manual trigger needs a human to start each run.
- C: Form submission starts on an n8n-hosted form, not on incoming Gmail.
- D: Schedule runs on a timer, not when a specific email lands.

---

## Q3 (MCQ, Easy)

In a **Basic LLM chain** node, what is the main job of the **system prompt**?

A. Store Gmail OAuth Client ID and Client Secret  
B. Set standing rules and role for the model before the user task  
C. Replace the need for an OpenAI API key  
D. Merge outputs from two parallel LLM branches

**Correct Answer:** B

**Answer Explanation:**  
The **system prompt** defines the model’s role and boundaries (for example, “helpful Python coding assistant”). The **user prompt** carries the actual task plus dynamic input.

Why other options are wrong:
- A: OAuth secrets live in n8n **Credentials**, not in prompts.
- C: API keys are still required in the OpenAI credential.
- D: **Merge** combines parallel LLM outputs, not the system prompt.

---

## Q4 (MCQ, Easy)

While building LLM nodes, Arjun pins sample output on the Gmail trigger so he does not re-fetch mail on every test. What is the best practice before a final end-to-end demo?

A. Keep all nodes pinned forever  
B. Unpin trigger and downstream pinned data so the workflow reads a fresh email  
C. Delete the Gmail credential  
D. Change poll time to every second

**Correct Answer:** B

**Answer Explanation:**  
**Pin data** speeds up building, but **unpinning** before a realistic full run ensures the pipeline processes a new email instead of frozen sample data.

Why other options are wrong:
- A: Pinned data can cause repeated runs on the same cached payload.
- C: Deleting credentials breaks the pipeline; it is not a testing step.
- D: Polling every second creates unnecessary API load.

---

## Q5 (MCQ, Moderate)

Meera connected Gmail OAuth but the trigger still cannot read messages. She enabled APIs in Google Cloud. Which API must be enabled for this Gmail integration?

A. Gmail API  
B. Google Maps API  
C. Google Photos API  
D. YouTube Data API

**Correct Answer:** A

**Answer Explanation:**  
Reading and sending mail through n8n’s Gmail nodes requires the **Gmail API** to be enabled in the correct Google Cloud project.

Why other options are wrong:
- B, C, D: Maps, Photos, and YouTube are unrelated to inbox access.

---

## Q6 (MCQ, Moderate)

A pipeline runs **code summarizer** and **code commentator** in parallel from the same Gmail trigger. Before sending the reply email, both outputs must be ready. Which node waits until both branches finish?

A. Aggregate  
B. Merge  
C. IF  
D. Edit Fields

**Correct Answer:** B

**Answer Explanation:**  
The **Merge** node combines multiple streams and waits until data from **both** parallel LLM branches is available.

Why other options are wrong:
- A: **Aggregate** combines fields after merge — it does not synchronize parallel completion by itself.
- C: **IF** branches on a condition; it does not wait for two parallel LLM jobs.
- D: **Edit Fields** remaps fields optionally; it is not the parallel sync step taught for this pipeline.

---

## Q7 (MSQ, Moderate)

Which settings help restrict a Gmail trigger so it does not process every message in the inbox?

A. **Sender** filter set to an approved email address  
B. **Event** set to message received  
C. Hard-coding one customer name inside the OpenAI API key field  
D. **Poll time** chosen based on how quickly new mail must be detected

**Correct Answers:** A, B, D

**Answer Explanation:**  
Sender filter (A) limits which From address can trigger the flow. Message received (B) is the correct event type. Poll time (D) controls check frequency.

Why other options are wrong:
- C: API keys authenticate OpenAI; they do not filter Gmail senders.

---

## Q8 (MSQ, Moderate)

A team is wiring **Basic LLM chain** nodes after a Gmail trigger. Which steps are correct?

A. Choose **Define below** so email `text` can be dragged into the user prompt  
B. Attach an **OpenAI Chat Model** sub-node with a valid API key credential  
C. Map the full email body by typing a fixed sample string instead of expressions  
D. Rename nodes (for example, **code summarizer**) to keep the canvas readable

**Correct Answers:** A, B, D

**Answer Explanation:**  
Define below (A) connects prior node data. OpenAI credential + model (B) powers the chain. Clear node names (D) aid maintenance.

Why other options are wrong:
- C: Hard-coded sample text breaks the pipeline for new emails; use expressions from trigger output.

---

## Q9 (MSQ, Hard)

**CodeBridge** built: **Gmail trigger → parallel summarizer + commentator → Merge → Aggregate → Gmail Send message**. Which statements are correct?

A. Both LLM chains can connect directly from the same Gmail trigger for parallel execution  
B. **Merge** should receive one input from summarizer and one from commentator  
C. **Aggregate** helps combine `text` fields (for example `text0` and `text1`) before mapping the email body  
D. The Gmail send node should map **text0** and **text1** from aggregate output into the outgoing message

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
Parallel branches (A) share the same trigger input. Merge takes two streams (B). Aggregate rolls up text fields (C). Send maps aggregated fields into the reply (D).

Why other options are wrong:
- None — all four statements match the taught pipeline pattern.

---

## Q10 (MSQ, Hard)

While testing and handing off an n8n AI email pipeline, which statements are correct?

A. **Fetch test event** on the Gmail trigger helps verify ingestion before wiring LLM nodes  
B. Exporting workflow **JSON** shares node wiring; teammates still reconnect their own credentials locally  
C. If OpenAI credentials are invalid, the LLM sub-node may fail until a valid API key and model are saved  
D. Sharing Client ID, Client Secret, and API keys in a public chat is the recommended handoff method

**Correct Answers:** A, B, C

**Answer Explanation:**  
Fetch test event (A) validates trigger output. JSON export (B) transfers structure, not private secrets. Bad OpenAI setup causes LLM errors (C).

Why other options are wrong:
- D: Credentials must be treated like passwords and never shared publicly.
