# Building End-to-End AI Automation Pipelines with n8n

## Context of This Session

In the **previous** session you built a starter n8n workflow with a **manual form trigger**, **Google Sheets**, and an **IF** branch — useful, but not a full autonomous pipeline. The workflow only ran when someone clicked **Execute workflow**, and it did not use **LLM / AI nodes** yet.

This session moves from isolated steps to a **complete AI automation pipeline**. You will use an **automatic Gmail trigger**, read incoming messages, pass Python code through **LLM summarization**, run a **second LLM step in parallel** for code comments, **merge and aggregate** the outputs, and **deliver the result by email**. You will also practise **documentation**, **credential setup**, **pinning test data**, and **workflow export** for handoff.

**In this session, you will:**

- **Design** an end-to-end pipeline that ingests email messages and routes them through LLM processing
- **Configure** Gmail and OpenAI credentials inside n8n
- **Build** parallel LLM branches, then **merge** and **aggregate** outputs before delivery
- **Send** the final summary and commented code back through Gmail
- **Test** the pipeline, document assumptions, and **export** the workflow as JSON

---

## Why Automatic Triggers Matter

Real business automation should start on its own when an event happens — not only when a human clicks a button.

- **Official Definition:** An **automatic trigger** starts a workflow when a defined event occurs (new email, webhook, schedule, app update).
- **In Simple Words:** The machine watches for a signal and begins work without you pressing start.
- **Real-Life Example:** When your manager emails Python code for review, a pipeline should read it, summarize it, and reply — even if you are in another meeting.

In the **previous** build, the **form trigger** was manual. Today the trigger is **Gmail → On message received**, which polls your inbox and fires when a matching email arrives.

| Trigger style | Who starts it? | Example from class |
|---|---|---|
| **Manual / form execute** | Human clicks run | Product feedback form |
| **On app event** | External app event | New Gmail from a specific sender |
| **Schedule** | Timer | Daily report at 9 a.m. |
| **Webhook** | HTTP call from another system | Payment confirmed |

---

## The Use Case You Will Build

The live demo used a realistic office scenario.

**Story:** You receive an email from a trusted sender (for example, your manager or your own test account). The email body contains **Python code** from an earlier LangChain memory-agent exercise. The code is long and hard to read quickly. You want the system to:

1. Detect the new email automatically
2. Extract the Python code from the message body
3. Summarize the code with an LLM
4. Add beginner-friendly comments to the code with a second LLM (in parallel)
5. Email back both the **summary** and **commented code**

**Demo email setup used in class:**

| Field | Example value |
|---|---|
| **Subject** | Python code |
| **Sender filter** | Your Gmail address (e.g. `deepakkasera18@gmail.com`) |
| **Body** | Full Python script (LangChain agent with memory and order-status tool) |

This is **document ingestion** through email. The same pattern works for PDFs, attachments, or Slack messages in other designs — the idea is: **bring content in → process with AI → send result out**.

---

## Document the Pipeline Before You Build

Strong builders do not jump straight to nodes. They write what the system must do first.

- **Official Definition:** **Workflow documentation** is a written plan of triggers, steps, outputs, credentials, and assumptions before implementation.
- **In Simple Words:** A recipe card before you enter the kitchen.
- **Real-Life Example:** A hospital documents which nurse checks vitals, which doctor reviews reports, and where results are filed — before wiring the actual process.

In n8n you can document inside the canvas using **sticky notes** (markdown-friendly). In class the instructor listed steps such as:

- Agent monitors Gmail
- When email arrives from a particular sender, workflow triggers
- Agent calls an LLM API to summarize code
- Agent sends summary back by email

### Activity — Write your sticky-note plan

On a blank n8n workflow:

1. Add a **sticky note**.
2. Write four bullets: **trigger**, **AI step 1**, **AI step 2 (optional)**, **delivery**.
3. List credentials you will need: **Gmail OAuth**, **OpenAI API key**.
4. Note one operational assumption (for example: "Only emails from sender X are processed").

Keeping this note on the canvas helps you and anyone who inherits the workflow later.

---

## End-to-End Pipeline Overview

![End-to-end n8n AI automation pipeline — Gmail trigger ingests email, parallel code summarizer and code commentator LLM chains, merge and aggregate nodes combine outputs, Gmail send message delivers summary and commented code](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-01-end-to-end-pipeline-overview.png)

**Reading the diagram:**

- **Ingestion:** Gmail trigger reads the email and exposes fields like `text`, `subject`, `from`.
- **AI processing:** Two LLM chains run **in parallel** on the same email content.
- **Routing / joining:** **Merge** waits until **both** LLM jobs finish.
- **Packaging:** **Aggregate** combines the two text outputs into one structure for email.
- **Delivery:** Gmail **Send message** emails summary + commented code back to you.

---

## Step 1 — Add the Gmail Trigger

Open local n8n at **http://localhost:5678**, create a workflow, and add the first node.

1. Click **+** → **On app event**
2. Search **Gmail**
3. Choose **On message received**
4. Click **Set up credentials** (covered in the next section)

- **Official Definition:** **On message received** is a polling trigger that checks Gmail periodically for new messages matching your filters.
- **In Simple Words:** A security guard who peeks at the mailbox every few minutes for letters from one person.
- **Real-Life Example:** A finance team inbox that should auto-process invoices only from `vendor@company.com`.

**Common doubt:** *"Will it read every email in my account?"* — No, if you set a **sender filter**. Without a filter it may read too broadly. Always restrict by sender for demos.

![Gmail automatic trigger and ingestion — polling inbox for trusted sender with message-received event, sender filter, and contrast between manual form execute versus automatic on-app-event trigger](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-02-gmail-automatic-trigger.png)

---

## Step 2 — Google Cloud OAuth for Gmail

Gmail access uses **OAuth2**, the same pattern you used for Google Sheets in the **previous** session — but this time you enable **Gmail API** instead of Sheets.

### Google Cloud checklist

| Step | Action |
|---|---|
| 1 | Open [Google Cloud Console](https://console.cloud.google.com/) |
| 2 | Create project (class used name like **N8N test**) |
| 3 | **APIs & Services → Library** → enable **Gmail API** |
| 4 | **OAuth consent screen** → External audience → add your Gmail as **test user** |
| 5 | **Credentials → Create credentials → OAuth client ID** → **Web application** |
| 6 | Copy n8n **OAuth Redirect URL** into **Authorized redirect URIs** |
| 7 | Paste **Client ID** and **Client Secret** into n8n Gmail credential → **Sign in with Google** |

**Why test user is needed:** External OAuth apps in testing mode only work for emails you explicitly add under **Audience → Test users**. If Google blocks access, add your Gmail there and sign in again — the same fix used in the **previous** Google setup.

**Security habit from class:** Credentials shown live were deleted after class. Treat Client ID, Client Secret, and API keys like passwords. Revoke test clients you exposed on screen.

**Scopes you approve:** Gmail read, compose, send, and related permissions — n8n needs read access for the trigger and send access for the reply email.

![Gmail OAuth and OpenAI credentials in n8n — Google Cloud Console enables Gmail API and OAuth client, credentials stored in n8n vault for Gmail trigger, Gmail send, and Basic LLM Chain nodes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-04-gmail-oauth-openai-credentials.png)

---

## Step 3 — Configure the Gmail Trigger Settings

After credentials connect, tune how the trigger behaves.

| Setting | Class discussion | Practical note |
|---|---|---|
| **Poll time** | Every minute vs every hour | Faster polling = more API calls and load; choose based on urgency |
| **Event** | Message received | Starts when a new message arrives |
| **Max emails per poll** | e.g. 10 or 100 | Limits batch size per check |
| **Sender** | Specific Gmail address | Only process mail from trusted sender |

**Common mistake:** Polling **every second** creates unnecessary network traffic. For learning, **every minute** or **every hour** is enough.

### Test ingestion with Fetch test event

1. Send yourself a test email with subject **Python code** and Python script in the body.
2. On the Gmail trigger node, click **Fetch test event**.
3. Confirm output shows `subject`, headers, and **`text`** field containing the code.

If only a **snippet** appears instead of full body, rebuild credentials and trigger from scratch — full `text` content is required for the LLM step.

### Activity — Reach a working Gmail trigger

1. Complete Gmail OAuth in a fresh Google Cloud project.
2. Set sender filter to your own test email.
3. Send a test message with Python code in the body.
4. Run **Fetch test event** and verify the code appears under **`text`**.

---

## Pin Data While Building Later Nodes

Once fetch works, **pin** the trigger output so you do not re-hit Gmail on every test.

- **Official Definition:** **Pin data** freezes a node's sample output on the canvas for downstream design.
- **In Simple Words:** Photocopy the sample letter and reuse it while wiring the rest of the factory.
- **Real-Life Example:** You keep one sample invoice on your desk while designing the approval form — you do not fetch a new invoice for every pencil mark.

**Rule from class:** Pin while building LLM, merge, and email nodes. **Unpin** before a realistic full end-to-end run so the workflow reads a fresh email again.

| Mode | Best for |
|---|---|
| **Pinned** | Designing prompts, merge, aggregate, email mapping |
| **Unpinned** | Final demo — trigger reads latest real email |

---

## Step 4 — Add the Code Summarizer (Basic LLM Chain)

Connect an AI node after the Gmail trigger.

1. Click **+** on the Gmail node → search under **AI**
2. Select **Basic LLM chain** (not AI templates)
3. Choose **Define below** for input (connect data from previous node)
4. Attach an **OpenAI Chat Model** sub-node

- **Official Definition:** **Basic LLM chain** is a simple n8n pattern: prompt + model → text output.
- **In Simple Words:** You hand the model a note; it writes a reply.
- **Real-Life Example:** Asking a senior developer to explain a code file in plain English.

Rename the node to **code summarizer** so the canvas stays readable.

### Map the Python code into the prompt

Drag the email **`text`** field into the prompt window. Do not type the code manually — use expressions so any future email works.

**User prompt used in class:**

```text
Given the Python code, please summarize this code in a beginner friendly manner.
Make sure to include all the technical details about the code and what we can do.
Just provide a proper summary of the code. Do not edit it.
```

**System prompt used in class:**

```text
You are a helpful coding assistant who is very good at Python.
```

- **System prompt** = standing rules for the model (role and boundaries).
- **User prompt** = the actual task plus the code content from the email.

Expand the prompt editor if the window feels too small — click to enlarge before writing long instructions.

### OpenAI credentials

1. On the OpenAI Chat Model sub-node → **Set up credential**
2. Paste your **OpenAI API key**
3. Save — n8n verifies the key
4. Select a model (class used **GPT** family models such as **gpt-4o** / **gpt-5** variants)

**Common error from class:** `Error in subnode, OpenAI chat model` — usually fixed by saving credentials, picking a valid model name, and executing again.

### Execute and verify

Click **Execute step** on the summarizer. You should receive a detailed summary describing the script (class output mentioned a small customer-support chatbot using LangChain, tools, and conversation memory).

### Sample Python code in the demo email

The email body used code from the LangChain **memory agent** exercise. Below is the same style of script the class summarized — paste this into a test email body:

```python
from langchain_openai import ChatOpenAI  # Import OpenAI chat model wrapper
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder  # Prompt templates
from langchain_core.messages import HumanMessage, AIMessage  # Message types for history
from langchain_core.tools import tool  # Decorator to register a tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent  # Agent runtime

# Fake order database stored in application memory (lost on restart)
ORDERS = {
    "ORD101": {"status": "out for delivery"},  # Sample order 1
    "ORD102": {"status": "cancelled"},  # Sample order 2
}

@tool
def get_order_status(order_id: str) -> str:
    """Use when the user asks for order status or tracking."""
    order = ORDERS.get(order_id)  # Look up order in fake DB
    if not order:
        return f"Order with ID {order_id} not found."  # Handle missing ID
    return f"Order status for {order_id} is {order['status']}."  # Return status text

tools = [get_order_status]  # List of tools the agent may call

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # Low temperature for factual replies

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful customer support agent. "
        "If the user gives an order ID, remember it for this conversation. "
        "For follow-ups like 'track it' or 'what is the status of it', use the order ID from chat history. "
        "Use tools when order status is required. "
        "If no order ID is available, ask politely for it."
    )),
    MessagesPlaceholder(variable_name="chat_history", optional=True),  # Slot for past turns
    ("human", "{input}"),  # Current user message
    MessagesPlaceholder(variable_name="agent_scratchpad"),  # Tool steps for current run
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)  # Build tool-calling agent

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # Print tool steps while learning
)

chat_history = []  # Python list storing conversation across turns

def ask_agent(user_input: str) -> str:
    response = agent_executor.invoke({
        "input": user_input,
        "chat_history": chat_history,
    })
    ai_text = response["output"]  # Final assistant reply text
    chat_history.append(HumanMessage(content=user_input))  # Save user turn
    chat_history.append(AIMessage(content=ai_text))  # Save assistant turn
    return ai_text

print("Turn 1")
print("User:", "Hi, my order ID is ORD102.")
print("AI:", ask_agent("Hi, my order ID is ORD102."))
print()
print("Turn 2")
print("User:", "What is the status of it?")
print("AI:", ask_agent("What is the status of it?"))
```

**How the code works:**

- **`get_order_status`** is a tool the LLM may call when the user asks about tracking.
- **`chat_history`** lets turn 2 understand *"it"* refers to **ORD102** from turn 1.
- **`AgentExecutor`** runs the tool loop and returns the final natural-language answer.
- The n8n pipeline does not run this Python — it **reads the code as text** and asks the LLM to summarize and comment on it.

### Activity — Build the summarizer node

1. Add **Basic LLM chain** after the pinned Gmail trigger.
2. Use **Define below** and drag **`text`** into the user prompt.
3. Add the class user and system prompts.
4. Configure OpenAI credentials and model.
5. Execute once and confirm a readable code summary appears.

---

## Step 5 — Add Parallel Code Commentator

One LLM task is not always enough. The class added a **second branch** that adds inline comments to the same Python code.

**Why parallel?** Summarizing and commenting are **independent** jobs. Running them together saves time versus doing them strictly one after another.

1. **Duplicate** the summarizer node and OpenAI sub-node (credentials copy over automatically).
2. Rename the copy to **code commentator**.
3. Connect **both** LLM nodes directly from the **same Gmail trigger**.

**User prompt for commentator (class version):**

```text
Given the Python code, please provide proper comments in this code in a beginner friendly manner.
Make sure to include all the technical details about the code in the comments.
Comments should not be very long.
Do not make changes in the code.
```

Keep the **same system prompt** as the summarizer. Execute the commentator once with pinned email data and confirm hash-style or inline comments appear in the output.

**Developer mindset from class:** Always ask, *"Which steps do not depend on each other?"* Those are candidates for parallel execution.

---

## Step 6 — Merge Node (Wait for Both LLM Branches)

Before sending email, you need **both** outputs ready. Parallel paths finish in unpredictable order.

- **Official Definition:** The **Merge node** combines streams and can wait until all inputs arrive.
- **In Simple Words:** Two cooks finish dishes at different times; merge waits until both plates are ready before plating.
- **Real-Life Example:** Uber Eats order with burger and shake — packaging starts only when both items reach the counter.

1. Add **Merge** from the flow menu
2. Connect **code summarizer** → Merge input 1
3. Connect **code commentator** → Merge input 2
4. Mode discussed: **Append** — two items in one list (summary item + comments item)

**Key idea:** Merge does not send email itself. It only guarantees both LLM results are available together.

![Parallel LLM branches with merge and aggregate — Gmail text feeds code summarizer and code commentator in parallel, merge waits for both outputs, aggregate combines text fields into one email payload](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-03-parallel-llm-merge-aggregate.png)

---

## Step 7 — Aggregate Node (Combine Text Fields)

The merge output still has **two separate items**. The email node is easier to build if you combine text fields.

- **Official Definition:** The **Aggregate node** rolls up fields from multiple items into a consolidated structure.
- **In Simple Words:** Putting summary and commented code into one envelope instead of two loose sheets.
- **Real-Life Example:** A report appendix that attaches both executive summary and annotated source code in one PDF section.

1. Add **Aggregate** after Merge
2. Connect Merge → Aggregate
3. Aggregate the **`text`** field from both items
4. After execution you should see **`text0`** (summary) and **`text1`** (code with comments)

Pin aggregate output while configuring the Gmail send step.

---

## Step 8 — Deliver Results with Gmail Send Message

**Delivery mechanism in this build:** email only. The same pipeline pattern can later point to **Slack** or a **database update** node instead of — or in addition to — Gmail.

1. Click **+** after Aggregate → **Gmail → Send message**
2. Credentials should auto-select your Gmail account
3. Configure:

| Field | Class example |
|---|---|
| **To** | Your Gmail (same account used for testing) |
| **Subject** | Python code with summary and comments |
| **Message type** | Text first; later HTML (see enhancement section) |
| **Body** | Drag **`text1`** (commented code) and **`text0`** (summary) into the message |

Connect Aggregate → Send message so the email node sees both text fields in its input panel.

### Map message body with expressions

- **Code with comments** → from **`text1`**
- **Code summary** → from **`text0`**

Execute the send step. Check your inbox — class saw a new mail within seconds with subject like **Python code with summary and comments**.

### Disable N8N email attribution (optional)

Gmail may append **"Sent with N8N"** footer. In send node **Options**, disable **Append N8N attribution** if you want a cleaner professional email.

### Dynamic subject line (class tip)

Instead of hard-coding subject text, drag the **`subject`** field from the original trigger email into the send node's subject line — or reply on the same thread using Gmail reply options.

---

## Step 9 — Run the Full Pipeline End to End

After all nodes are wired, test like a real user — not only step by step.

1. **Unpin** data on Gmail trigger, LLM nodes, merge, and aggregate
2. Delete or archive old test emails so the trigger does not keep re-reading the same message
3. Send a **fresh** email with updated subject (class changed subject to spot the new run)
4. Click **Execute workflow** from the start (or wait for poll trigger in production mode)
5. Watch nodes animate: summarizer + commentator parallel → merge → aggregate → send

**Success signs:**

- Green checkmarks on all nodes
- New email received with both summary and commented code
- Footer shows automatic send (unless attribution disabled)

---

## Optional Enhancement — HTML-Formatted Email

Plain **text** emails flatten code formatting. Class improved readability with **HTML output**.

1. Add to **both** LLM user prompts:

```text
Please give the output in HTML format, which can be easily sent over the mail without losing the context.
```

2. Re-execute summarizer and commentator
3. In Gmail send node, change message type from **Text** to **HTML**
4. Send again

**Result:** Code blocks, bullets, and highlights render properly in Gmail — much easier to read than one long plain-text paragraph.

### Optional Edit Fields node

Class briefly showed **Edit Fields** with manual mapping to separate `code_with_comments` and `code_summary` before sending. This is optional — you can achieve the same outcome by careful prompt design and aggregate mapping.

---

## Pipeline Testing — Normal, Failure, and Edge Cases

A pipeline is production-ready only when you test more than the happy path. The live class focused heavily on the **success path**; the checklist below completes the subtopic you need for real handoff.

### Representative input (happy path)

| Test | Input | Expected result |
|---|---|---|
| **T1** | Email from allowed sender with valid Python code | Summary + comments emailed back |

### Failure path to test deliberately

| Test | How to simulate | Expected handling |
|---|---|---|
| **T2** | Invalid or missing OpenAI API key | LLM node fails with credential error — fix key and re-run |
| **T3** | Wrong Gmail OAuth / removed test user | Trigger or send fails — re-authorize and add test user |

**What class debugged live:** OpenAI subnode error after adding credentials — resolved by selecting a valid model and re-executing. Treat that as a reminder to test credentials **before** demo day.

### Edge-case paths to test

| Test | Input | What you learn |
|---|---|---|
| **T4** | Email from sender **not** in filter | Trigger should ignore or not fire — confirms filtering works |
| **T5** | Email with empty body or no code | LLM may return vague output — add an IF check later to skip empty `text` |
| **T6** | Very long code paste | Watch token limits, latency, and truncation — may need chunking in production |

### Activity — Three-test checklist

Run these on your own workflow:

1. **Happy path:** Valid code email → receive summary and comments.
2. **Failure path:** Temporarily break OpenAI key → confirm LLM node error → restore key → confirm recovery.
3. **Edge case:** Send email from a different sender address → confirm it is **not** processed.

Document what happened for each test in your sticky note — that becomes part of handoff documentation.

---

## Document the Workflow for Handoff

Anyone who inherits your pipeline needs more than a pretty canvas. Record **credentials**, **dependencies**, and **assumptions**.

### What to document (minimum)

| Item | Example from this build |
|---|---|
| **Trigger assumptions** | Poll interval, sender filter, max emails per poll |
| **Credentials** | Gmail OAuth (Google Cloud project name), OpenAI API key |
| **APIs enabled** | Gmail API |
| **External services** | Gmail, OpenAI |
| **Input format** | Plain Python code in email `text` body |
| **Outputs** | HTML or text email with summary + commented code |
| **Known limits** | Testing OAuth requires test-user Gmail; pinned data blocks fresh runs |
| **Security** | Delete or revoke credentials shared during demos |

### Sticky note on canvas

Keep the markdown sticky note updated as the source of truth for teammates.

### Export workflow as JSON

At end of class the workflow was **downloaded as JSON** and shared for import.

1. In n8n workflow menu → **Download** / export workflow JSON
2. Teammates use **Import from file** on their n8n server
3. They reconnect credentials on their own accounts — exported JSON describes node wiring, not your private passwords

**Handoff tip:** Share the JSON **plus** a short note listing which credentials each importer must create locally.

![HTML email delivery and workflow handoff — styled Gmail output with commented code and bullet summary versus plain text, plus pipeline testing checklist and JSON export for teammate import](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session48/session48-05-delivery-html-and-handoff.png)

---

## Other Delivery Channels (Conceptual)

This session implemented **email → AI → email**. The same aggregate output could feed:

| Channel | n8n action | When teams use it |
|---|---|---|
| **Slack** | Slack → Send message | Daily ops alerts to a team channel |
| **Database** | HTTP Request / Postgres / Sheets | Store summaries for audit and search |
| **Email** | Gmail send (built today) | Personal notifications and client replies |

The ingestion → LLM → routing → delivery pattern stays the same; only the last node changes.

---

## Key Takeaways

- A real **AI automation pipeline** spans **ingestion, AI processing, joining parallel results, and delivery** — not a single LLM node in isolation.
- **Gmail on message received** turns email into an automatic trigger; **sender filters** and **poll intervals** are operational choices with real trade-offs.
- **Parallel LLM branches** speed up independent tasks; **Merge** then **Aggregate** prepares a clean combined payload for email.
- **Pin data** while building; **unpin** for truthful end-to-end tests; document credentials and assumptions for handoff.
- **Export JSON** so others can import the workflow structure and attach their own credentials.

These skills prepare you for **upcoming** work where full pipelines may add Slack, database writes, error branches, and multi-agent coordination.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Quick meaning |
|---|---|
| **n8n** | Visual workflow automation platform |
| **localhost:5678** | Local n8n UI address |
| **Workflow** | Connected automation from trigger to final action |
| **On app event** | Trigger category for external apps like Gmail |
| **On message received** | Gmail trigger when new mail arrives |
| **Poll time** | How often n8n checks Gmail for new messages |
| **Sender filter** | Restrict which From address can trigger the flow |
| **Fetch test event** | Pull sample data into trigger without waiting for poll |
| **Pin data** | Freeze sample node output for downstream design |
| **Unpin** | Remove frozen data for realistic full runs |
| **Basic LLM chain** | Prompt + chat model → text output |
| **OpenAI Chat Model** | n8n sub-node connecting to OpenAI API |
| **System prompt** | Standing instructions defining model role and rules |
| **User prompt** | Task instruction plus dynamic input (email code) |
| **Define below** | Take input from connected previous node |
| **code summarizer** | LLM node that explains the script |
| **code commentator** | Parallel LLM node that adds inline comments |
| **Merge node** | Waits for multiple branches and combines streams |
| **Append mode** | Merge strategy placing both items in one list |
| **Aggregate node** | Combines fields like `text0` and `text1` for one send step |
| **Gmail Send message** | Delivery node that emails workflow output |
| **N8N attribution** | Optional "Sent with n8n" footer in outgoing mail |
| **HTML message type** | Sends formatted email body instead of plain text |
| **Edit Fields** | Optional manual field mapping node |
| **OAuth2** | Secure delegated access without sharing passwords |
| **Client ID / Client Secret** | Google OAuth app identifiers |
| **Test user** | Allowed Gmail for unverified External OAuth apps |
| **Gmail API** | Google API that must be enabled for mail access |
| **OpenAI API key** | Secret key stored in n8n credentials |
| **Expression / drag-drop mapping** | Dynamic reference to prior node JSON fields |
| **Workflow JSON export** | Download pipeline definition for sharing |
| **Import from file** | Load shared JSON workflow into n8n |
| **Parallel execution** | Independent nodes running at the same time |
| **LangChain** | Python framework referenced in sample email code |
| **AgentExecutor** | Runs tool-calling agent loop in sample code |
| **chat_history** | Conversation memory list in sample agent code |
