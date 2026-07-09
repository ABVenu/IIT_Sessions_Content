# Building Your First n8n Workflow with Forms, Google Sheets, and Conditional Logic

## Context of This Session

In the **previous** session you explored **n8n** as a visual automation platform — the workspace, **triggers**, **nodes**, **connections**, **credentials**, and how to run n8n locally with **Docker**. You saw the building blocks; you did not yet wire a full multi-step business flow end to end.

This session is fully **hands-on**. You build a starter workflow: a **Product Feedback Form** collects name, email, and feedback; data is **appended** to **Google Sheets** after **OAuth2** setup; then an **IF** branch updates a **Send voucher** column based on whether feedback is positive. AI / LLM nodes are available in n8n but are saved for the **upcoming** session when you build a fuller end-to-end agent workflow.

**In this session, you will:**

- **Run** n8n locally with Docker and open the canvas at `localhost:5678`
- **Create** a named workflow and add a **form trigger** as the first node
- **Connect** Google Sheets using **OAuth2** (Client ID, Client Secret, consent screen, test user)
- **Map** form fields into spreadsheet columns without hard-coding values
- **Branch** with an **IF** node so positive feedback sets **Send voucher = Yes**, otherwise **No**
- **See** what happens when credentials or API access are removed (**Forbidden**)

---

## Why This Workflow Matters

n8n is not only about knowing what a node is. Real learning happens when you connect **trigger → action → decision** and watch data move live.

- **Official Definition:** A **workflow** is a connected sequence of nodes that starts on a trigger and performs actions or decisions on data.
- **In Simple Words:** Like a factory belt — form submit starts the belt, Sheets stores the packet, IF decides the next station.
- **Real-Life Example:** A product team floats a feedback form on LinkedIn. Every submission should land in a shared sheet, and happy customers should be marked for a voucher — without copy-paste by hand.

Missing one setup step (wrong Google project, missing Drive API, pinned test data) can break the whole chain. That is why this class moves slowly and asks you to build **in parallel**.

![First n8n workflow overview — Product Feedback Form trigger appends rows to Google Sheets, IF node checks feedback, then updates Send voucher to Yes or No based on positive vs negative/neutral](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-01-first-n8n-workflow-overview.png)

---

## Recap: Running n8n on Your Laptop

For learning and small projects, **self-hosted n8n on Docker** is free and unlimited on your machine. You do not pay n8n cloud fees while practising.

- **Official Definition:** **Self-hosted n8n** means the n8n server runs on your computer (or company server), not on n8n’s paid cloud.
- **In Simple Words:** The automation engine lives inside a Docker “box” on your laptop.
- **Real-Life Example:** Like running a small shop from home instead of renting a mall stall — same work, your own space, no monthly rent for learning.

### Quick restart checklist

1. Install **Docker Desktop** (Windows users often need **WSL** first if Docker fails to start).
2. Create a volume (if you have not already):

```bash
# Create a named Docker volume so n8n workflows survive container restarts
docker volume create n8n_data
```

3. Run n8n with India timezone (class used **Asia/Kolkata**):

```bash
# Start n8n in Docker — expose UI on port 5678, set timezone, attach volume
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -e GENERIC_TIMEZONE="Asia/Kolkata" \
  -e TZ="Asia/Kolkata" \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

### How the commands work

- **`docker volume create n8n_data`** — creates a saved folder for workflows and credentials.
- **`-p 5678:5678`** — opens n8n in the browser at **http://localhost:5678**.
- **`GENERIC_TIMEZONE` / `TZ`** — so schedule triggers use the correct local time.
- **`-v n8n_data:/home/node/.n8n`** — keeps your work after the container stops.
- First run may take a few minutes while Docker **pulls** the n8n image.

**Common doubt:** *"Do I need to reinstall every class?"* — No. If the volume and image already exist, you mainly re-run the `docker run` command and open the browser.

---

## Create a Workflow on the Canvas

Open **http://localhost:5678**. On the home page, click **Create Workflow**.

- Give a clear name, for example: **Sample workflow — 8 July** (use your class date).
- Click **Add first step**.

The blank canvas is your working sheet. Every automation starts here with a **trigger**.

- **Official Definition:** A **trigger** is the first node of a workflow — the event that starts execution.
- **In Simple Words:** The doorbell that starts the whole process.
- **Real-Life Example:** Payment confirmed on Razorpay → workflow starts → customer row written to a sheet.

### Trigger types you should recognise

| Trigger type | When it starts the workflow |
|---|---|
| **Manual** | Only when you click **Execute workflow** |
| **On app event** | Something happens in Telegram, Notion, Gmail, etc. |
| **Schedule** | Timer — e.g. every day at 9 a.m. |
| **Webhook** | An external system sends an HTTP call (e.g. payment confirmed) |
| **Form** | Someone submits an n8n-hosted form |

A form is **one** way to start a flow — not the only way. An email-priority agent might start on a **Gmail event**, not a form.

---

## Build the Product Feedback Form Trigger

In class we used a **form submission** trigger so you can see data appear immediately.

### Form settings used in class

| Setting | Value used |
|---|---|
| **Form title** | Product Feedback Form |
| **Description** | Same idea — product feedback |
| **Authentication** | None (for this starter demo) |
| **Respond when** | Form is submitted |

### Form fields

| Field | Element type | Notes |
|---|---|---|
| **Email** | Text (email) | Mark as **required**; n8n validates email format |
| **Name** | Text | Mark as **required** |
| **Feedback** | Dropdown | Options: **Positive**, **Negative**, **Neutral** |

Dropdown feedback avoids random free text and makes later **IF** conditions easy.

![Product Feedback Form trigger in n8n — required Email and Name fields plus Feedback dropdown with Positive, Negative, and Neutral options feeding node output on submit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-02-product-feedback-form-trigger.png)

### Test the form node

1. Click **Execute step** on the form node.
2. Fill sample data, e.g. email `deepakkasera18@gmail.com`, name `Deepak`, feedback `Positive`.
3. Submit — the node output shows **name**, **email**, and **feedback**.

You now have a working first node. Take a minute and recreate the same form on your canvas.

### Activity — Build the form trigger

On your local n8n:

1. Create a workflow named with today’s date.
2. Add an **On form submission** trigger titled **Product Feedback Form**.
3. Add **Email**, **Name**, and **Feedback** (dropdown: Positive / Negative / Neutral).
4. Execute the step once and confirm the three fields appear in the output panel.

---

## What Can Come After the Form?

Click the **+** after the form. n8n groups next steps into useful buckets.

| Option group | Examples from class | Use when |
|---|---|---|
| **AI** | OpenAI, Anthropic, Gemini, Ollama, AI Agent, guardrails | You need language understanding or an agent |
| **Action in an app** | Google Sheets, Telegram, Notion, Slack | Write or notify in a real tool |
| **Data transformation** | Filter, convert, reshape fields | Clean or reshape data |
| **Flow** | IF, Branch, Merge, Loop | Decisions and paths |
| **HTTP Request** | Call your DB or any API | Save to your own backend |
| **Code** | Python / JavaScript code node | Custom logic when no-code is not enough |
| **Human in the loop** | Approval / review step | Critical decisions need a person |

### Sales-team story from class

Someone fills a LinkedIn lead form → row in **Google Sheets** → instant **Slack** ping to sales with the details. That is classic **action-in-an-app** chaining.

### Human-in-the-loop (concept for later)

- **Official Definition:** **Human-in-the-loop** means a person must approve or review before the workflow continues for certain cases.
- **In Simple Words:** The robot works alone for small cases; a human signs off for big ones.
- **Real-Life Example:** Refund agent — if amount is under **₹500**, decide automatically; if amount is over **₹500**, send for human review.

Full end-to-end AI + human review flows are planned for the **upcoming** session. Today we stay with **Google Sheets** and **IF**.

### HTTP Request (mentioned)

After a form submit you could call your own database or API with an **HTTP Request** node. In this class it was explained as an option; the live build used Sheets instead.

---

## Prepare the Google Spreadsheet

Before connecting n8n, create a spreadsheet that matches the form.

1. Create a Google Spreadsheet named **Customer Feedback Data**.
2. Use column headers that match form fields **exactly**:

| email | name | feedback | send voucher |
|---|---|---|---|
| (empty for now) | | | |

3. Keep the tab name readable — e.g. rename **Sheet1** to **Customer Feedback**.

**Why exact names matter:** Later mapping is smoother when form field names and sheet headers match (`email`, `name`, `feedback`). Mismatched spellings cause empty columns and confusion.

---

## Google Sheets Node and Why Credentials Matter

Add an **Action in an app** → search **Google Sheets** → choose **Append row** (or Append / Update row as needed).

At this point the node cannot talk to your sheet yet. n8n must prove it is allowed to use your Google account.

- **Official Definition:** **Credentials** are securely stored authentication details (API keys, OAuth tokens) that let n8n call a third-party service as you.
- **In Simple Words:** The digital ID card n8n shows to Google.
- **Real-Life Example:** “Login with Google” on LinkedIn — LinkedIn is a **client** asking Google for limited access to your account. Here **n8n** is that client for Sheets.

You need two values from Google:

- **Client ID**
- **Client Secret**

This uses **OAuth2**.

- **Official Definition:** **OAuth2** (Open Authorization, version 2) is an internet protocol that lets a third-party app access another account with scoped permission and user consent.
- **In Simple Words:** You allow n8n to use Sheets/Drive **without** giving n8n your Gmail password.
- **Real-Life Example:** Google is first party, you are second party, n8n is third party — consent screen lists what n8n may touch.

Credentials are the most important setup step for almost any integration — Sheets today, ChatGPT or Slack later.

---

## Google Cloud Setup for n8n (Step by Step)

Follow these steps carefully. One missed toggle is hard to debug later.

![OAuth2 setup for Google Sheets in n8n — Google Cloud project enables Sheets and Drive APIs, OAuth consent and Client ID/Secret connect n8n to your Google account without sharing your password](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-03-oauth2-google-sheets-setup.png)

### Step 1 — Create a Google Cloud project

1. Open [Google Cloud Console](https://console.cloud.google.com/) and sign in.
2. Project dropdown → **New Project**.
3. Name it clearly, e.g. **N8N project** → **Create**.
4. **Select that project** in the top bar before doing anything else.

**Common mistake:** Enabling APIs in the wrong project. Always confirm the project name in the header.

### Step 2 — Enable required APIs

Go to **APIs & Services → Library** (while inside **N8N project**).

Enable:

1. **Google Sheets API**
2. **Google Drive API**

**Why Drive as well?** Sheets files live in Drive. Docs, Sheets, and Slides all need Drive access for OAuth integrations. Enabling only Sheets is a frequent failure point.

You do **not** need Maps, Photos, or other APIs for this workflow. Enable only what the workflow needs.

Optional idea from class: enabling **Gmail API** would let n8n read mail later — same pattern, different API.

### Step 3 — Configure the OAuth consent screen

1. Go to **APIs & Services → OAuth consent screen**.
2. Click **Get started** (first time in this project).
3. **App name:** e.g. `N8N client` or `N8N project`.
4. **Support email:** your own email.
5. **Audience:** choose **External** for personal Gmail learning (Internal is for Google Workspace organisations only).
6. Add developer contact email → agree → **Create**.

**Authorized domain:** For localhost learning you can skip domain registration. Class noted that `http://localhost` is not a normal public domain; local demos work without forcing that field.

### Step 4 — Create OAuth client credentials

1. **APIs & Services → Credentials → Create credentials → OAuth client ID**.
2. Application type: **Web application**.
3. Name: e.g. `n8n client`.
4. In n8n’s Google Sheets credential screen, **copy the OAuth Redirect URL**.
5. Paste it into Google’s **Authorized redirect URIs** → **Create**.
6. Copy **Client ID** and **Client Secret** into n8n → **Sign in with Google**.

Treat Client ID / Secret like passwords. Do not share them in screenshots or chat.

### Step 5 — Fix “Access blocked” for External apps

If Google says the app has not completed verification:

1. In Cloud Console go to **Audience** (OAuth consent).
2. Confirm you are in **N8N project**.
3. **Add test user** — your Gmail (the account you will sign in with).
4. Save, return to n8n, **Sign in with Google** again.

After consent, Google shows scopes (Drive, Sheets, etc.). Continue and finish.

### Activity — Complete OAuth once

1. Create project **N8N project**.
2. Enable **Sheets** + **Drive** APIs.
3. Configure consent (External) and add yourself as **test user**.
4. Create Web OAuth client; paste n8n redirect URI.
5. Paste Client ID/Secret into n8n and complete Sign in with Google.

---

## Connect Nodes and Map Form Data to Columns

After credentials work, the Sheets node can list your documents.

1. Select document **Customer Feedback Data**.
2. Select the sheet/tab **Customer Feedback** (not only the spreadsheet name — a spreadsheet can contain many tabs).
3. Choose columns: **email**, **name**, **feedback**.
4. Use **Refresh** if a column does not appear yet.

### Connect the form to Sheets

Drag a connection from the **form trigger** to the **Google Sheets** node.

- Output of the form becomes **input** of Sheets.
- Without this link, the nodes sit on the canvas but do not pass data.

### Map with expressions — do not hard-code

Do **not** type fixed values like `Deepak` into the sheet fields.

Drag each form field into the matching column so n8n inserts expressions (JavaScript-style references to the previous JSON), for example:

- Email column ← form `email`
- Name column ← form `name`
- Feedback column ← form `feedback`

- **Official Definition:** An **expression** in n8n is a dynamic reference that pulls a value from earlier node data at runtime.
- **In Simple Words:** “Whatever email arrived in the form, put that here.”
- **Real-Life Example:** Like a courier label that copies the address from the order form automatically instead of rewriting it by hand.

![Expression mapping from form to Google Sheets — drag email, name, and feedback from the form node into matching sheet columns instead of hard-coding fixed customer values](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-04-expression-mapping-form-to-sheet.png)

### Execute the Sheets step

Click **Execute step**. A new row should appear in Google Sheets with the mapped values. That confirms n8n ↔ Google connectivity.

---

## Pin Data: Helpful for Testing, Dangerous for Full Runs

When you execute a form step, sample output is **temporary**. Refreshing the page can clear it.

- **Pin data** keeps that sample on the node so you can design later nodes without re-filling the form every time.
- **Unpin** before a realistic full-workflow test.

**What went wrong in class:** With data **pinned**, **Execute workflow** kept appending the **same cached row** again and again and did **not** open a fresh form. After **unpinning**, Execute workflow showed the form again and new submissions (e.g. Nesarg / Neutral) appended correctly.

**Rule of thumb:** Pin while building mappings; unpin when you want a real end-to-end run.

| Mode | What Execute workflow does | Best for |
|---|---|---|
| **Pinned** | Reuses frozen sample; may skip opening the form | Designing Sheets mapping / IF conditions |
| **Unpinned** | Opens the form; new user input flows through | Realistic end-to-end testing |

Think of pin like a **sticky note** on a photocopy — useful while you design the filing system, but remove it before you invite real customers to fill a fresh form.

---

## Add Conditional Logic with an IF Node

Business flows rarely stop at “save the row.” Often you branch on a value.

Class goal: based on **feedback**, fill **Send voucher**.

| Feedback | Send voucher |
|---|---|
| Positive | **Yes** |
| Negative or Neutral | **No** |

### Add the IF node

1. Click **+** after Sheets → **Flow** → **IF**.
2. Condition: **feedback** **equals** `Positive` (or your exact dropdown spelling).
3. Execute the IF step once to see **true** / **false** paths light up.

- **Official Definition:** An **IF node** evaluates a condition and sends items down the **true** or **false** branch.
- **In Simple Words:** A yes/no junction on the road.
- **Real-Life Example:** If marks ≥ 40, pass lane; else fail lane — same idea as LangChain-style chains, but visual.

Data flow in this workflow:

**Form → Append row in Sheets → IF on feedback → Update row (Yes or No)**

![IF node branching on feedback — positive path sets Send voucher Yes, negative or neutral path sets No, both update the matched row using email as the key column](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-05-if-branch-send-voucher.png)

### True and false actions (Update row)

On the **true** path (positive):

1. Add **Google Sheets → Append or update row** (update behaviour).
2. Same document and sheet.
3. **Column to match on:** **email** (unique key for the person).
4. Set **Send voucher** = `Yes`.
5. Map the email value from previous data so the correct row is found.

On the **false** path (not positive):

1. **Duplicate** the update node (faster than rebuilding).
2. Same match on **email**.
3. Set **Send voucher** = `No`.
4. Connect this node to the IF **false** output.

**Critical fix from class:** Matching only on feedback is wrong for updates. Multiple people can share the same feedback label. Match on **email**, then write Yes/No into **Send voucher**.

### Watch the colours when you run

Execute the full workflow and watch nodes highlight:

- Example **Navdeep / Negative** → IF goes **false** → No branch runs.
- Example **Gaurav / Positive** → IF goes **true** → Yes written.
- Example **Chirag / Neutral** → also **false** path → No (only two outcomes in this design).

### Activity — Complete the voucher branch

1. Add column **send voucher** to your sheet.
2. Add IF: feedback equals Positive.
3. True path updates matched email with Yes; false path with No.
4. Run once with Positive and once with Neutral; confirm the sheet.

---

## Credentials Are Power — and Can Be Taken Away

Near the end of class, OAuth client access was removed / APIs disabled to show security reality.

When Sheets/Drive access is no longer valid, the workflow fails with errors such as **Forbidden — check your credentials**.

- **Official Definition:** **Scoped access** means the app may use only the APIs and permissions you enabled and consented to.
- **In Simple Words:** If you take back the key, the door will not open.
- **Real-Life Example:** Revoking a third-party app in your Google Account settings stops that app from reading your Drive.

**Practice habit:** After demos, delete or disable test OAuth clients you exposed on screen so strangers cannot reuse them.

---

## Code Nodes and LangChain / LangGraph

n8n is often called no-code, but that is incomplete.

- n8n **supports no-code** for most steps.
- n8n **also supports code** — add a **Code** node and write **Python** (or JavaScript) when you need custom logic.

**Integration with LangChain / LangGraph:** Yes, it is possible. You can combine visual orchestration in n8n with code-based agent frameworks when a use case needs both.

Major day-to-day use is still visual nodes; code is there when you need flexibility.

---

## End-to-End Picture of Today’s Workflow

The full chain you built in class: **form submit → append row in Customer Feedback Data → IF on feedback → update Send voucher (Yes/No) matched by email**. The overview and IF-branch visuals earlier in these notes show the same flow on the n8n canvas.

### What you practised

- Local n8n + canvas workflow naming
- Form trigger with validated fields and dropdown
- Google Cloud project, Sheets + Drive APIs, OAuth consent, test user, Client ID/Secret
- Node connections, expressions, pin/unpin behaviour
- IF branching and row updates keyed by email
- Credential failure (**Forbidden**) when access is revoked

### What comes next

In the **upcoming** session you will go further: automatic triggers (not only manual Execute), **LLM / AI agent** nodes, richer multi-step pipelines (for example email-driven flows), and tighter human-review patterns.

---

## Key Takeaways

- A useful n8n workflow is a **chain**: trigger collects data, actions store or notify, flow nodes decide the path.
- **OAuth2 credentials** are the bridge to Google; enable **Sheets and Drive**, pick the **correct project**, and add a **test user** for External apps.
- **Map expressions** from the form — never hard-code live customer fields into Sheets nodes.
- **Pin data** speeds building but can cause duplicate cached runs; **unpin** for real form tests.
- **IF + Update row (match on email)** turns feedback into business actions like **Send voucher Yes/No**; revoked credentials correctly produce **Forbidden**.

These habits prepare you for the **upcoming** AI-assisted n8n workflows, where the same trigger–action–branch pattern will wrap LLM and agent steps.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Quick meaning |
|---|---|
| **n8n** | Visual workflow automation platform (node canvas) |
| **Docker** | Runs n8n in an isolated container on your laptop |
| **`docker volume create n8n_data`** | Creates persistent storage for n8n data |
| **`docker run ... n8n`** | Starts the n8n container |
| **localhost:5678** | Browser URL for local n8n UI |
| **Asia/Kolkata** | Timezone used in class for schedule-correct local time |
| **Workflow** | Connected automation from trigger to final action |
| **Trigger** | First node — event that starts the workflow |
| **Form trigger** | Starts when a user submits the n8n form |
| **Manual execute** | You click Execute workflow to run (demo mode) |
| **Webhook / Schedule / App event** | Other trigger styles for real automation |
| **Node** | One step on the canvas |
| **Connection** | Link that passes output → next input |
| **Google Sheets node** | Reads/writes spreadsheet rows from n8n |
| **Append row** | Adds a new row to the sheet |
| **Append or update row** | Creates or updates a row using a match column |
| **Column to match on** | Key field for updates (use **email** here) |
| **Credential** | Stored auth for a third-party service |
| **OAuth2** | Open Authorization v2 — scoped third-party access |
| **Client ID / Client Secret** | OAuth app identifiers from Google Cloud |
| **OAuth consent screen** | Google page where the user approves scopes |
| **Test user** | Allowed Gmail for unverified External OAuth apps |
| **Google Sheets API** | Must be enabled for Sheets access |
| **Google Drive API** | Also required because Sheets live in Drive |
| **Expression** | Dynamic value from previous node JSON |
| **Pin data** | Freeze sample output on a node for building |
| **IF node** | True/false branch on a condition |
| **Send voucher** | Example business column set by IF outcome |
| **Human-in-the-loop** | Human approval for sensitive automated cases |
| **HTTP Request node** | Call any API/DB from the workflow |
| **Code node** | Run Python/JS custom logic inside n8n |
| **Forbidden** | Typical error when credentials/API access are invalid |
| **LangChain / LangGraph** | Agent frameworks that can integrate with n8n via code/custom logic |
