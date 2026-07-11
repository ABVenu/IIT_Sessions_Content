# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation (n8n — end-to-end AI email pipeline)

---

## Q1 (Practical, Medium)

**CodeBridge Solutions** is a remote software consultancy. Contractors email **Python scripts** to a shared inbox when they need a quick review. The operations lead wants an **automatic** n8n pipeline that:

1. Detects a new email from an **approved sender**
2. Reads the Python code from the email body
3. Runs **two AI steps in parallel** — a plain-English **summary** and **inline comments** on the code
4. Waits for **both** AI results, packages them together, and **emails the reply** back to the same inbox

Build everything in your **local n8n** instance (Docker on `localhost:5678`).

---

## Big picture (read this first)

You will create **one workflow**, **one test email**, and **two credential types** (Gmail OAuth + OpenAI API key).

| Item | Name (suggested) | Purpose |
|---|---|---|
| **Workflow** | `CodeBridge Code Review Pipeline` | Gmail in → parallel LLM → merge → aggregate → Gmail out |
| **Sticky note** | On canvas | Document trigger rules, credentials, and assumptions |
| **Test email** | Subject: `Python code` | Body contains the sample script below |

**Total main nodes on canvas: 6** (same Gmail OAuth credential for trigger + send; same OpenAI credential for both LLM chains).

![End-to-end n8n AI automation pipeline — Gmail trigger ingests email, parallel code summarizer and code commentator LLM chains, merge and aggregate nodes combine outputs, Gmail send message delivers summary and commented code](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-01-end-to-end-pipeline-overview.png)

### Visual map — full workflow

```text
[Sticky note: plan + assumptions]

[1] Gmail: On message received
        |---------------------------+
        v                           v
[2] Code Summarizer          [3] Code Commentator
    (Basic LLM Chain)            (Basic LLM Chain)
        |                           |
        +-------------+-------------+
                      v
              [4] Merge (Append)
                      v
              [5] Aggregate (text fields)
                      v
              [6] Gmail: Send message
```

---

## Part A — Sticky note and test email (do this first)

### A1 — Sticky note on canvas

Add a **sticky note** with at least these four bullets:

| Bullet | What to write |
|---|---|
| **Trigger** | Gmail on message received; approved sender only |
| **AI step 1** | Code summarizer — beginner-friendly summary |
| **AI step 2** | Code commentator — inline comments, no code edits |
| **Delivery** | Gmail send message with summary + commented code |

Also list:

- Credentials needed: **Gmail OAuth**, **OpenAI API key**
- One assumption (example: “Only process mail from my test Gmail address”)

### A2 — Send yourself a test email

From your **approved sender Gmail** (same address you will use in the sender filter), send an email **to yourself** with:

| Field | Value |
|---|---|
| **Subject** | `Python code` |
| **Body** | Paste the **Sample Python script** from Part B below |

You will use this email for **Fetch test event** and for the final unpinned end-to-end run.

---

## Part B — Sample Python script (paste into test email body)

Use this script exactly (or equivalent length — do not send an empty body):

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

ORDERS = {
    "ORD101": {"status": "out for delivery"},
    "ORD102": {"status": "cancelled"},
}

@tool
def get_order_status(order_id: str) -> str:
    """Use when the user asks for order status or tracking."""
    order = ORDERS.get(order_id)
    if not order:
        return f"Order with ID {order_id} not found."
    return f"Order status for {order_id} is {order['status']}."

tools = [get_order_status]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chat_history = []

def ask_agent(user_input: str) -> str:
    response = agent_executor.invoke({"input": user_input, "chat_history": chat_history})
    ai_text = response["output"]
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=ai_text))
    return ai_text
```

---

## Part C — Credentials (one time)

### C1 — Gmail OAuth2

1. Google Cloud project → enable **Gmail API**
2. OAuth consent screen (External) → add your Gmail as **test user** if needed
3. Create **Web application** OAuth client → paste n8n redirect URI
4. In n8n: Gmail credential → Client ID + Secret → **Sign in with Google**

### C2 — OpenAI API key

1. In n8n: **OpenAI** credential → paste valid API key → save
2. Attach to **both** OpenAI Chat Model sub-nodes (summarizer + commentator)

---

## Part D — Build the workflow (6 nodes)

### Node 1 — Gmail: On message received (trigger)

| Setting | Value |
|---|---|
| Workflow name | `CodeBridge Code Review Pipeline` |
| Event | Message received |
| Poll time | Every minute (or every hour — your choice) |
| Sender | Your approved test Gmail address |
| Max emails per poll | 10 |

**Test:** Click **Fetch test event**. Confirm output includes **`text`** with the Python script.  
**Then pin** this output while building nodes 2–6.

---

### Node 2 — Code Summarizer (Basic LLM chain)

1. **+** after Gmail → **AI** → **Basic LLM chain**
2. Input: **Define below**
3. Drag Gmail **`text`** into the user prompt
4. Attach **OpenAI Chat Model** sub-node (your credential + model, e.g. `gpt-4o-mini`)

**System prompt:**

```text
You are a helpful coding assistant who is very good at Python.
```

**User prompt:**

```text
Given the Python code, please summarize this code in a beginner friendly manner.
Make sure to include all the technical details about the code and what we can do.
Just provide a proper summary of the code. Do not edit it.
```

Rename node to **code summarizer**. Execute once — confirm summary text appears.

---

### Node 3 — Code Commentator (Basic LLM chain, parallel)

1. **Duplicate** node 2 (credentials and model copy over)
2. Rename to **code commentator**
3. Connect **Gmail trigger → code commentator** (parallel branch, not after summarizer)

**User prompt (change only this):**

```text
Given the Python code, please provide proper comments in this code in a beginner friendly manner.
Make sure to include all the technical details about the code in the comments.
Comments should not be very long.
Do not make changes in the code.
```

Keep the **same system prompt**. Execute once — confirm commented output appears.

---

### Node 4 — Merge

1. Add **Merge** node
2. Connect **code summarizer → Merge input 1**
3. Connect **code commentator → Merge input 2**
4. Mode: **Append** (two items in one list)

Execute merge with pinned LLM outputs — confirm **two items** in the output list.

---

### Node 5 — Aggregate

1. Add **Aggregate** after Merge
2. Connect **Merge → Aggregate**
3. Aggregate the **`text`** field from both items

After execute, confirm fields like **`text0`** (summary) and **`text1`** (commented code). Pin aggregate output while configuring send.

---

### Node 6 — Gmail: Send message

| Field | Map from |
|---|---|
| **To** | Your own Gmail (inbox that receives the reply) |
| **Subject** | `CodeBridge review — summary and comments` |
| **Message type** | Text (HTML optional bonus — see Part F) |
| **Body** | Drag **`text1`** (commented code) and **`text0`** (summary) from aggregate output |

Connect **Aggregate → Send message**. Execute step — check inbox for the automated reply.

Optional: disable **Append N8N attribution** in send options for a cleaner email.

---

## Part E — Testing checklist (required)

Run all three tests and note results in your Google Doc (Part G).

| Test | What to do | Pass criteria |
|---|---|---|
| **T1 Happy path** | Unpin all nodes → send **fresh** test email → execute full workflow | Reply email contains **both** summary and commented code |
| **T2 Failure path** | Temporarily break OpenAI key (wrong value) → execute summarizer | LLM node shows credential/model error → restore key → succeeds again |
| **T3 Edge case** | Send email from a **different** sender (not in filter) | Workflow should **not** process that mail as a new pipeline run |

**Before T1:** Delete or archive old test emails if the trigger keeps re-reading the same message.

---

## Part F — Optional bonus (HTML email)

If you finish early:

1. Add to **both** LLM user prompts:  
   `Please give the output in HTML format, which can be easily sent over the mail without losing the context.`
2. Re-execute both LLM nodes
3. Change Gmail send **message type** from Text to **HTML**
4. Send again and screenshot the more readable formatted email

---

## Part G — Export and handoff

1. **Download** workflow as JSON from n8n
2. On sticky note, add one line: which credentials a teammate must recreate after import

---

## Part H — What to submit (Google Doc)

Create a Google Doc with:

1. **Canvas screenshot** — all **6 nodes** + sticky note visible
2. **Gmail trigger screenshot** — Fetch test event showing `text` with Python code
3. **Parallel LLM screenshot** — both summarizer and commentator connected from Gmail trigger
4. **Merge + Aggregate screenshot** — showing two inputs / `text0` and `text1`
5. **Inbox screenshot** — received reply email with summary + commented code
6. **Testing table** — one row each for T1, T2, T3 (what you did + pass/fail)
7. Short write-up (**100–150 words**) answering:
   - Why summarizer and commentator run **in parallel** instead of one after another
   - What **Merge** does that a single LLM node cannot do alone
   - Why you **unpin** data before the final end-to-end test

### Submission Instruction

- create a google doc in your google drive - suggested folder (for your ref) is module name in that session name in that the submission file
- write properly and neatly after reasearching duly - do add images wherever needed
- once the doc is ready - submit the doc link (click share button and copy the link)
- make sure the sharing settings is `View anyone with the link` (sharing should be public)

---

## Common mistakes (save yourself debugging time)

| Mistake | What happens | Fix |
|---|---|---|
| Commentator chained **after** summarizer | No true parallel run | Both LLM nodes connect **from Gmail trigger** |
| Hard-coded code in prompt | Only works for one email | Drag **`text`** field with expressions |
| Skipped Merge | Email may send before both LLM jobs finish | Add Merge before Aggregate |
| Pinned data during final demo | Same old email processed again | Unpin trigger + downstream nodes |
| Wrong sender on test email | Trigger never fires | Sender filter must match From address |
| Only Gmail API missing | OAuth works but mail fails | Enable **Gmail API** in correct project |
| Empty email body | Vague or empty LLM output | Send full sample script from Part B |

---

## Answer Explanation (Ideal Solution Walkthrough)

### Node checklist

| # | Node type | Purpose |
|---|---|---|
| 1 | Gmail On message received | Ingest email; filter by sender |
| 2 | Basic LLM chain (summarizer) | Plain-English code summary |
| 3 | Basic LLM chain (commentator) | Inline comments on same code |
| 4 | Merge (Append) | Wait for both LLM outputs |
| 5 | Aggregate | Combine `text0` + `text1` for send node |
| 6 | Gmail Send message | Deliver summary + commented code |

### Grading checklist (for evaluators)

| Check | Pass criteria |
|---|---|
| Sticky note | Trigger, 2 AI steps, delivery, credentials, one assumption |
| Gmail trigger | Sender filter set; Fetch test event shows code in `text` |
| Parallel LLM | Both chains wired from trigger; distinct prompts |
| Merge + Aggregate | Two streams merged; send maps text0 and text1 |
| Delivery | Automated reply received with both summary and comments |
| Testing | Evidence for happy path, failure recovery, wrong-sender edge case |
| Credentials | Gmail OAuth + OpenAI; no secrets pasted in doc |
| Evidence | Google Doc with screenshots + 100–150 word write-up |

### Alternative approaches

- **HTML message type** after prompt tweak — acceptable bonus; plain text delivery is sufficient for pass.
- **Edit Fields** node before send — acceptable if mapping is correct; not required.
- **Single LLM node** that asks for summary + comments in one prompt — does **not** meet the parallel-branch requirement of this task.
