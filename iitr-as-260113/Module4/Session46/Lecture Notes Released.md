# Introduction to n8n Workflow Automation

## Context of This Session

In the **previous** part of this module you learned **multi-agent architecture**, **HTTP**, **triggers**, **events**, and **webhooks** — the vocabulary for how agents start, pass data, and talk to external systems. You saw that real business processes are chains of steps, not one magic prompt.

This session introduces **n8n** — a **visual workflow automation platform** where you design those chains on a canvas instead of writing every integration by hand. You will navigate the n8n workspace, understand **triggers**, **nodes**, **connections**, **expressions**, and **credentials**, and run n8n locally with **Docker**. Full multi-step workflows with data flowing across linked nodes will be built hands-on in the **upcoming** classes; today is a strong foundation and overview.

**In this session, you will:**

- **Explain** n8n as a drag-and-drop automation engine for business and agentic workflows
- **Compare** n8n cloud pricing with **self-hosted** Docker setup for learning and development
- **Configure** trigger types and inspect outputs at a single node (form trigger demo)
- **Apply** credentials, environment variables, and **OAuth2** concepts for secure integrations
- **Preview** how nodes chain together for HR, sales, and security use cases

---

## Why Visual Workflow Automation Matters

Until now, connecting Google Sheets, Slack, an LLM, and a database often meant writing Python, managing API keys, and debugging one long script. That works for engineers — but many teams need automation **without** a full engineering sprint for every small process.

- **Official Definition:** **Workflow automation** is software that runs a sequence of steps when a condition is met, moving data between tools with minimal manual work.
- **In Simple Words:** Like setting **auto-debit** for your electricity bill — the same steps happen every month without you visiting the office.
- **Real-Life Example:** A college **placement cell** receives hundreds of form submissions. Copying each row into a spreadsheet, sending confirmation mail, and notifying a trainer by hand becomes error-prone at scale.

**n8n** gives you a **visual canvas** to design that journey: what starts the flow, what each step does, and what data moves forward. The rest of this document walks through the platform, local setup, and core building blocks.

![n8n visual workflow automation — drag-and-drop canvas connecting form trigger, AI agent, Google Sheets, and email nodes with 1500+ integrations instead of writing every connection in code](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session46/session46-01-n8n-workflow-overview.png)

---

## What Is n8n?

n8n (pronounced "n-eight-n") is one of the most popular tools today for building **agents**, **business workflows**, and **AI workflows** through a visual interface.

- **Official Definition:** **n8n** is a **workflow automation platform** — a drag-and-drop engine for connecting apps, databases, APIs, and AI models into multi-step automations.
- **In Simple Words:** A **visual backend** where you pick blocks from a menu instead of typing every integration in code.
- **Real-Life Example:** A **CA firm** wants monthly reports from Tally, email, and Google Sheets. With n8n, a finance person can wire those steps on a canvas; they do not need to become a full-stack developer first.

### Core Properties from Class

| Property | What it means |
|---|---|
| **Visual / no-code first** | Drag-and-drop nodes; thousands of pre-built integrations |
| **1,500+ integrations** | Google Sheets, Slack, Gmail, Postgres, MongoDB, WhatsApp, GitHub, and more |
| **Optional code** | Python or JavaScript inside **code nodes** when you need custom logic |
| **Any LLM** | OpenAI, Anthropic, Gemini, Ollama, Perplexity — connect the model you choose |
| **Observability** | See each node's **input** and **output** on the canvas — trace failures clearly |
| **Templates** | Pre-built workflow examples on the n8n website to learn from |

### n8n Is Not Only for Software Engineers

The instructor stressed a important shift: n8n is usable by **HR**, **finance**, **teachers**, and other non-technical roles. Engineers still decide **what** to automate and **how** data should flow — but the daily wiring can happen visually.

**Common doubt:** *"If it is no-code, can I never write code?"* — You **can**. n8n is **UI when you don't need code; code when you need flexibility** — Python, JavaScript, LangChain, or even RAG logic inside a code node.

### n8n vs "Just Using an LLM"

An **LLM** (like ChatGPT or Ollama) is one piece of an agentic application. Real systems also need **triggers**, **databases**, **email**, **ticketing**, and **conditional logic**. n8n bundles those **tools** around the LLM — that is why it is broader than running a model alone.

---

## n8n Cloud Pricing and Hosting Models

n8n is **not entirely free** for production use on their cloud. Understanding pricing helps you choose between **n8n-hosted** and **self-hosted**.

- **Official Definition:** **Hosted n8n** runs workflows on n8n's servers; you pay for the platform and infrastructure. **Self-hosted n8n** runs on your laptop or your company's servers — you manage Docker and hardware.
- **In Simple Words:** **Hosted** = renting a furnished flat (n8n maintains the machines). **Self-hosted** = running the app on your own computer for learning.
- **Real-Life Example:** A startup testing automations in class uses **Docker on a laptop** (free). A company serving 500 employees 24/7 may pay for **n8n cloud** or host on **AWS** themselves.

### Cloud Tiers (Website Walkthrough)

| Tier | Rough idea from class | Hosting |
|---|---|---|
| **Starter** | Around **20 euros**/month; limited users and workflows (e.g. ~50 AI workflows) | Hosted by n8n |
| **Pro / Business / Enterprise** | More users, features, and support | Hosted by n8n (or hybrid for large orgs) |

**Why n8n charges:** Workflows run on **machines** that need power, internet, and maintenance. On paid cloud plans, **n8n hosts** that infrastructure for you.

**Free path for learning:** Run n8n **locally with Docker** — no per-run charge from n8n for infrastructure you own. You can also activate a **free license key** (sent by email during setup) to unlock features on self-hosted instances.

**Key line from class:** n8n's **source code** is available; you pay when you use **their platform and hosting**, not for learning on your own machine.

---

## Website Walkthrough — Example Workflows

Before touching the local install, the instructor walked through **n8n.io** use-case diagrams. These show how **triggers**, **nodes**, and **branches** fit together — the same ideas you will build in upcoming classes.

### HR / IT Ops — New Employee Onboarding

**Trigger:** **Form submission** — HR fills a "create user" form on joining day (name, email, department, manager, etc.).

**Flow after trigger:**

1. **AI agent** with an LLM (Anthropic, Gemini, OpenAI — any model)
2. **Postgres** — store employee data / memory
3. **Jira** — create an onboarding ticket
4. **Conditional branch** — *Is the employee a manager?*
   - **If true** → add to a manager channel
   - **If false** → update profile differently

- **Real-Life Example:** When you join **Microsoft**, HR does not manually create every account, ticket, and channel step — automation chains handle repeatable onboarding.

This connects directly to the **previous** lesson: the **form submit** is the **trigger** that **starts** the workflow.

### Sales — Customer Insights from Reviews

**Scenario:** After a free masterclass or perfume sample event, thousands of customers leave **ratings (1–5)** and text reviews. The sales team wants to know **whom to call first**.

**Workflow shape on the website:**

1. **Load reviews** from a file or data source
2. **K-means clustering** — groups people into low / medium / high rating clusters (machine-learning grouping; you do not need to master the algorithm to use the node)
3. **LLM agent** — classify detailed reviews; rank top 10%, 20%, 30% interest levels
4. **Google Sheets** — refined output for the sales team (who to call first, who to call later)

**Manual vs automated:** Earlier, sales staff read every review by hand. The workflow delivers a **sorted, actionable sheet** — more insight with less repetitive effort.

### SecOps — Security Incident Enrichment

**Trigger:** New **security incident ticket** created.

**Steps:**

1. Extract **IP address** and **domain** from the ticket
2. **Virus scan** the artifact automatically
3. **URL scan** — check if a link is vulnerable
4. **Merge reports** and store results

- **Real-Life Example:** A **SOC team** at a bank cannot manually scan every suspicious URL at 2 a.m. — automation enriches the ticket before a human analyst opens it.

### Platform Highlights from the Homepage

- **Build visually** — canvas like draw.io / diagrams.net
- **Connect to anything** — 1,900+ integrations listed (growing weekly)
- **Inspect every decision** — observability on the canvas
- **Human in the loop** — for **critical decisions** (refunds, money transfers, ticket booking), ask for human approval instead of blind agent action
- **Deploy with Docker** — self-host on your infrastructure

---

## n8n and Docker — Two Different Things

Many beginners assume **n8n = Docker**. That is **not** correct. They are separate tools that work together only when you choose the **self-hosted** path.

| Tool | What it actually is |
|---|---|
| **n8n** | The **workflow automation application** — the canvas, nodes, triggers, and integrations you learn in this course |
| **Docker** | A **helper program** that runs other applications inside a packaged box on your laptop |

- **Official Definition:** **n8n** is a workflow platform. **Docker** is a **container runtime** — software that launches pre-packaged apps without manual dependency setup.
- **In Simple Words:** **n8n** is the **car**. **Docker** is the **garage with a ready-made parking slot** — you do not build the engine yourself; you just drive.
- **Real-Life Example:** **WhatsApp** (the app) is not the same as the **Play Store** (how you install it). n8n is the app; Docker is one convenient way to install and run it on your machine.

**Important:** You can use n8n **without ever touching Docker** if you sign up for **n8n cloud** on n8n.io — they host everything in the browser. Docker appears in this course because we want a **free, local setup** for practice, not because n8n depends on Docker by design.

### Three Ways to Run n8n

| Option | Do you need Docker? | Best for |
|---|---|---|
| **n8n cloud** (paid hosted) | **No** — open n8n.io, log in, build workflows in the browser | Teams that want public URLs and zero server setup |
| **Self-hosted with Docker** (class method) | **Yes** — Docker downloads and runs n8n on your laptop | **Learning, testing, free practice** |
| **Self-hosted without Docker** (advanced) | **No** — install via npm or direct server setup | Experienced developers on production servers |

**Why the class uses Docker:** It is the **recommended beginner path** for self-hosting. One copy-paste command gets the same n8n version running on Windows, Mac, and Linux — without installing Node.js, databases, and ten other dependencies by hand.

**You are not learning Docker as a career skill in this session.** You only need enough Docker to **start n8n**, **open localhost:5678**, and **stop the container** when done. Deep Docker topics (building custom images, Kubernetes) are outside today's scope.

![n8n and Docker are different — n8n is the automation app while Docker is one helper to run it locally; compare n8n cloud, self-hosted with Docker, and advanced self-hosted without Docker](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session46/session46-02-n8n-vs-docker-three-ways.png)

---

## What Is Docker? (For Complete Beginners)

If Docker is new to you, read this section slowly. Every term below connects to the install steps in the next section.

### The Problem Docker Solves

Imagine you write a Python app on your Mac. A classmate on Windows clones the same code. It fails because:

- Python version is different (3.10 vs 3.12)
- A library is missing (`pip install` was forgotten)
- An **environment variable** (API key) is not set
- File paths work on Mac but break on Windows

The instructor described this in class: *"The same code running on my laptop may not run on your laptop."* Out of 30–40 students, some succeed and some get errors — not because they are weak, but because **each machine is configured differently**.

**Docker's fix:** The n8n team bundles their entire app — code, runtime, libraries, settings — into one **ready-to-run package**. You download that package and run it. Everyone gets the **same box**, so everyone gets the **same result**.

### Docker in One Picture (Mental Model)

![Docker beginner mental model for n8n — laptop runs Docker Desktop, n8n container runs inside, browser opens localhost:5678; image is the installer package, container is the running app, volume saves workflows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session46/session46-03-docker-beginner-mental-model.png)

- **Your laptop** stays unchanged — Docker does not replace Windows or Mac.
- **Docker Desktop** is the app you install from docker.com (like installing Chrome).
- **Container** is n8n running **inside** Docker's box — separate from your Python projects, separate from system files.
- **localhost:5678** is the "door" from your browser into that box.

### Three Docker Words You Must Know

| Term | Plain meaning | n8n example |
|---|---|---|
| **Image** | A **frozen installer file** — the full n8n app package downloaded from the internet | Like a `.exe` or `.dmg` installer, but for server apps |
| **Container** | The **running copy** of that image — n8n actually working right now on your machine | Like double-clicking the installer and the app being open |
| **Volume** | A **saved folder** Docker keeps even if you stop the container — stores your workflows and login | Like saving game progress so you do not lose work when you close the app |

**Analogy from class:**

- **Image** = executable file you download
- **Container** = the place where that executable is **running**
- **Volume** = the place where your **data is stored** so it survives restarts

**Common doubt:** *"If I close Docker, do I lose my workflows?"* — **No**, if you used a **volume** (`n8n_data`). The volume keeps your workflows on disk. The container is just the running process.

**Common doubt:** *"Is Docker only for n8n?"* — **No**. Docker runs thousands of apps (databases, web servers, AI tools). We use it here **only** because n8n's team published an official Docker image that makes self-hosting easy.

### Why Docker Is Needed to Run n8n Locally (But Not to Use n8n Itself)

Break this into two clear questions:

**Q1: Do I need Docker to learn n8n?**  
**No** — if you pay for n8n cloud, you use n8n in the browser with zero Docker.

**Q2: Then why does this course use Docker?**  
Because we want you to run n8n **for free on your own laptop** without paying for cloud hosting. For that **self-hosted local** setup, n8n officially supports Docker as the simplest install method.

| Without Docker (manual self-host) | With Docker (class method) |
|---|---|
| Install Node.js, npm, and n8n packages yourself | One `docker run` command |
| Debug version conflicts per operating system | Same image works on Mac and Windows |
| Easy to break when you update one library | n8n team maintains the boxed image |

**Bottom line:** **n8n is independent of Docker.** Docker is a **shortcut to run n8n on your machine** when you are not using n8n's paid cloud. Think of it as choosing **home delivery (cloud)** vs **cooking at home with a meal kit (Docker)** — the food (n8n) is the same idea; the delivery method differs.

### What You Actually Install (Checklist for Freshers)

1. **Docker Desktop** — download from [docker.com](https://www.docker.com/products/docker-desktop/); install like any normal app
2. **Wait for Docker to start** — the whale icon in the menu bar / system tray must show "Docker is running"
3. **Run two terminal commands** — create volume, then run n8n (next section)
4. **Open browser** — go to `http://localhost:5678`; you are now using **n8n**, not "using Docker" day to day

After setup, your daily work happens entirely in the **n8n web UI** — building workflows, adding nodes, testing forms. You only return to Docker/terminal to **start** or **stop** the server.

**Prerequisites from class:**

- Install **Docker Desktop** (Mac or Windows)
- Roughly **8–16 GB RAM** recommended
- Image size ~2.5 GB; allow **5–10 GB** disk space after install
- First download may take a few minutes; later starts are faster

---

## Step-by-Step — Install and Run n8n with Docker

Follow the official n8n Docker documentation. The instructor demonstrated these steps live.

### Step 1 — Create a Docker Volume

A volume stores your workflows and settings so they survive container restarts.

```bash
# Create a named volume — stores all n8n data on your machine
docker volume create n8n_data
```

**How this works:**

- **`docker volume create`** — asks Docker to reserve a storage area
- **`n8n_data`** — the volume name (you can pick another name; stay consistent in the next command)

### Step 2 — Run the n8n Container

Set your **timezone** so scheduled triggers fire at the correct local time. The class used **Asia/Kolkata**.

**Mac / Linux** (use `\` at the end of each line to continue the command):

```bash
# Run n8n — maps port 5678, sets India timezone, mounts the volume
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -e GENERIC_TIMEZONE="Asia/Kolkata" \
  -e TZ="Asia/Kolkata" \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

**Windows:** Use the **backtick** `` ` `` instead of `\` for line breaks, or write the command on one line.

**How this works:**

- **`docker run`** — starts a new container from an image
- **`-p 5678:5678`** — exposes n8n at **http://localhost:5678** (same idea as FastAPI on port 8000)
- **`-e GENERIC_TIMEZONE` / `-e TZ`** — tells n8n which timezone to use for schedules
- **`-v n8n_data:/home/node/.n8n`** — attaches your volume so workflows persist
- **`docker.n8n.io/n8nio/n8n`** — the official n8n image URL

**First run:** Docker prints `Unable to find image locally` — it **downloads** (pulls) the image. This may take a few minutes (~300 MB+). Later runs start faster because the image is cached.

### Step 3 — Open n8n in the Browser

1. Go to **http://localhost:5678**
2. Create an **owner account** (email + password)
3. Answer the short onboarding questions (role, use case, etc.)
4. Optional: click **"Send me a free license key"** — paste the **activation key** from your email to unlock features on self-hosted n8n without paying for cloud hosting

**Key point:** Self-hosted n8n on your laptop has **no time limit** for learning. n8n charges when **they** host production infrastructure, not when **you** run Docker locally.

### Localhost vs Public Form Links

When you build an **n8n form** on localhost, the share link looks like `http://localhost:5678/form/...`. **Other people cannot open that link** — it only exists on your machine.

- **Self-hosted on your laptop** → test forms yourself; link is not public
- **n8n cloud or server on AWS** → public URL; anyone with the link can submit

This is one reason companies pay for hosted n8n — **public endpoints** for customer-facing forms and webhooks.

---

## The n8n Workspace — Canvas and First Steps

After setup, the homepage offers **Build workflow**. The editor feels like **draw.io** or **Excalidraw** — a blank canvas where you add steps.

### Adding the First Step — Choose a Trigger

Every workflow begins with a **trigger** — the answer to *"When should this automation start?"*

| Trigger type | When it fires | Class example |
|---|---|---|
| **Trigger manually** | You click **Execute** to test | Empty workflow demo |
| **On app event** | Something happens in a connected app | New row in Google Sheets; row deleted |
| **On a schedule** | Cron-style timing | Every day at 9 a.m. — compile yesterday's report |
| **On webhook call** | External system sends HTTP request | **Razorpay** payment success → start shipping workflow |
| **On form submission** | Someone submits an n8n or connected form | HR onboarding form; student feedback form |
| **When executed by another workflow** | Another workflow calls this one | Reusable sub-workflows |

**Connecting to the previous lesson:** A **webhook** is an HTTP call from outside — Razorpay notifying your server that payment completed is the same pattern as **on webhook call** in n8n.

![n8n trigger types — manual execute, daily schedule, Razorpay webhook, form submission, and Google Sheets app event each start a workflow at the right moment](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session46/session46-04-triggers-and-nodes.png)

### Schedule Trigger — Plain English

- Run **every day**, **hour**, **week**, or **month** at a fixed time
- Example: At **10 a.m. daily**, pull yesterday's data, analyse, email a report to managers

### Webhook Trigger — Razorpay Flow (Recap)

1. Customer pays via Razorpay link on your site
2. Razorpay sends an HTTP callback — payment success, failure, expired, etc.
3. Your n8n workflow **starts** — e.g. ship product, send receipt, alert finance

### After the Trigger — Node Menu Changes

Once a trigger exists, the **+** menu shows different options: **AI agents**, **LLM chains**, **actions** (Google Sheets, Gmail, Slack), **logic**, and **code**. You cannot add a form in the middle without a **form trigger** at the start — n8n enforces sensible order.

---

## Nodes — Every Step in the Workflow

- **Official Definition:** A **node** is one **action or decision** in a workflow — a single step on the canvas.
- **In Simple Words:** One **station** on a train route — form station, AI station, spreadsheet station.
- **Real-Life Example:** In a **dosa shop**, taking order, cooking, and billing are separate steps — each could be one node.

### Node Categories from Class

| Category | Role | Example |
|---|---|---|
| **Trigger node** | Starts the workflow | Manual trigger, form trigger, webhook |
| **Action node** | Talks to an external service | Google Sheets — create row; Gmail — send email |
| **AI / LLM node** | Calls a language model | OpenAI chat model; sentiment analysis on feedback |
| **Logic node** | Branching rules | If rating > 4 → high-priority path; else low-priority |
| **Code node** | Custom Python or JavaScript | LangChain, LangGraph, RAG, vector DB logic |

**LangGraph connection:** In LangGraph you called each function a **node**. n8n uses the same word — every task is a node, connected by arrows (**connections**).

### Conceptual Multi-Step Chain (Preview)

The instructor described — but did not fully wire live — this feedback pipeline:

```
Form trigger (name, email, rating)
        │
        ▼
OpenAI node — sentiment analysis on feedback text
        │
        ▼
Google Sheets — create row with results
```

You will build chains like this in the **upcoming** classes. Today you validated the **form trigger** and inspected its output alone.

### Code Node — When Visual Blocks Are Not Enough

Click **Code** → write **Python** (or JavaScript) inside the workflow. Use this for custom LangChain agents, RAG pipelines, or logic no pre-built node covers.

**Rule from class:** Use the **UI** for standard integrations; drop to **code** when you need full control.

---

## Live Demo — n8n Form Trigger and Output Inspection

The class built a **student feedback form** for a hypothetical Masai experience survey.

### Build Order Matters

**Mistake shown in class:** Adding a **form page** node before a **form trigger** causes an error — *"Form Trigger node must be set before this node."*

**Correct order:**

1. First step → **On new n8n form event** (form trigger)
2. Configure form fields
3. Later nodes process the submission (not built end-to-end today)

### Form Fields Configured

| Field | Type | Notes |
|---|---|---|
| **Name** | Text | **Required** field |
| **Email** | Email (not plain text) | Validates email format — same idea as Pydantic `EmailStr` |
| **Batch** | Text | Required |
| **Rating** | Dropdown | Options 1, 2, 3, 4, 5 — all required |

**Form title:** Feedback form  
**Response:** When form is submitted

### Execute and Inspect

1. Click **Execute step** on the form trigger
2. Fill test data — e.g. name **Deepak**, valid email, rating **5**
3. Click **Submit** — *"Your form response has been recorded"*

### Output Views at One Node

n8n shows the captured data in multiple formats:

| View | What you see |
|---|---|
| **Table** | Columns — name, email, batch, rating, submitted time, mode |
| **JSON** | Structured object for the next node to consume |
| **Schema** | Field names and types |

**Test mode:** The demo ran in **test mode** — fine for learning; production forms behave similarly but with public URLs when hosted.

**Inspecting inputs and outputs** is how you debug: if step 3 fails, open step 2's output and verify the JSON shape. Full **per-node validation across a multi-step run** will be practiced when complete workflows are built next.

---

## Connections and Data Flow

- **Official Definition:** A **connection** is the link between two nodes that defines how **output** from one becomes **input** to the next.
- **In Simple Words:** The **track** between train stations — if the track is wrong, luggage (data) reaches the wrong place.
- **Real-Life Example:** HR form output `{ "email": "...", "department": "..." }` must connect to the Google Sheets node that expects those field names.

**Data flow** is the journey of information from trigger → transform → store → notify. n8n's observability lets you open any executed node and see exactly what arrived and what left.

### App-Event Triggers — Google Sheets Example

| Event | Automation idea |
|---|---|
| **New row added** | Welcome email + assign sales rep |
| **Row deleted** | Alert manager — someone removed a lead (knowingly or by mistake) |

These are **app-specific triggers** — the workflow starts when the sheet changes, not when you click Execute.

---

## Expressions — Dynamic Values Instead of Hard-Coding

- **Official Definition:** An **expression** is a formula or rule that computes a value at **runtime** from input data instead of using a fixed constant.
- **In Simple Words:** A **formula in Excel** — the cell updates when marks change; you do not retype the grade by hand.
- **Real-Life Example:** A school report card: grade depends on marks, not a number typed once in January.

### Marks-to-Grade Example from Class

**Static (bad for automation):**

```text
grade = "A"
```

**Dynamic (expression logic):**

```text
if marks > 90 → grade A
if marks > 80 → grade B
… and so on
```

Whenever new **marks** arrive in the workflow input, the expression **recalculates** the grade. In n8n, you use the expressions UI (often `{{ }}` syntax) to reference fields from earlier nodes — e.g. `{{ $json.marks }}` — instead of hard-coding.

**Why it matters:** Agents and automations must react to **changing** form data, API responses, and LLM outputs. Expressions glue steps together without rewriting the workflow for every new student.

---

## Credentials and Secure Integrations

Connecting Google Sheets, Slack, OpenAI, or Gemini requires **permission**. n8n stores those permissions as **credentials** — not as plain text in your workflow file.

- **Official Definition:** A **credential** in n8n is a securely stored authentication record (API key, OAuth token, etc.) that authorizes access to a third-party service.
- **In Simple Words:** The **key card** that lets n8n open the Google Sheets door — stored in a safe, not taped to the monitor.
- **Real-Life Example:** If your company's **Slack** login leaked, strangers could join internal channels — credential security is non-negotiable.

### How n8n Protects Credentials

- Credentials are **not stored in plain text** on the canvas
- Stored as **API keys** or **tokens** in n8n's secure credential store
- For self-hosted setups, sensitive values can live in **environment variables** that n8n reads at runtime

**Never do this in production:**

```bash
# BAD — hard-coding secrets in workflow JSON or chat
token = "sk-abc123plaintext"
```

**Do this instead (self-hosted):**

```bash
# Set API key in terminal before starting n8n — n8n reads from environment
export OPENAI_API_KEY="your-key-here"
```

### Self-Hosted vs n8n Cloud — Environment Variables

| Hosting | How you set secrets |
|---|---|
| **Self-hosted (Docker on your laptop)** | `export VAR=value` in terminal, or `.env` file — same pattern as earlier Python labs |
| **n8n cloud** | Enter variables in the **n8n settings UI** — you cannot SSH into their servers |

**Rule from class:** `export OPENAI_API_KEY=...` in the terminal works when **you** control the machine. On **n8n-hosted** infrastructure, you provide keys through their dashboard and n8n applies them on their servers.

### Setup Credentials UI — Google Sheets

In the workflow editor, nodes like **Google Sheets** open a **Set up credentials** panel. For Google, you typically use **OAuth2** — covered next.

**Documentation habit:** Every node has a **Docs** link — e.g. Spreadsheet node documentation lists parameters, OAuth steps, and examples. You do not need to memorise every field.

![Secure n8n integrations — data flows through expressions from form input to Google Sheets; credentials stored in a vault; OAuth2 grants minimum Google permissions without sharing passwords](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session46/session46-05-credentials-oauth-data-flow.png)

---

## OAuth2 — Logging In with Google (Conceptual)

Before n8n can edit your Google Sheet, it must prove you allowed access. That process is **OAuth2** (Open Authorization).

- **Official Definition:** **OAuth2** is a protocol where a **third-party app** (n8n) gets limited access to your account on another service (Google) **without** sharing your Google password with n8n.
- **In Simple Words:** **Scalar** offers **Login with Google** — you stay on Scalar's site, Google asks *"Allow Scalar to see your email?"*, you click Continue, and Scalar gets a token — not your password.
- **Real-Life Example:** **GitHub** and **LinkedIn** also offer *Login with Google* or *Login with Apple* — the same handshake pattern.

### Step-by-Step (Login with Google on a Website)

1. You use **App A** (e.g. an learning platform) and click **Login with Google**
2. **App A** redirects to **Google** (the authorization server)
3. Google shows a popup — *"App A wants access to …"*
4. If you are already logged into Google in the browser, it may show **Continue** / **Cancel**
5. If not logged in, Google asks for your Google email and password first
6. Google lists **exact permissions** — e.g. email only vs Gmail + Drive + Photos
7. You click **Continue** → Google issues a token → App A can access only what you approved

### Security Lesson from Class

**Do not blindly click Continue.** Read the first two lines:

- Does a school portal need your **Gmail inbox**? Probably **no** — only email
- Does a **photo editor** need **Google Photos**? **Yes** — that permission is reasonable

Grant **minimum** access. Extra permissions are a **red flag**.

### OAuth2 in n8n for Google Sheets

**Analogy:** n8n is like Scalar asking Google for access — but instead of your profile photo, n8n wants permission to **read/write Google Sheets**.

Setup (high level — full implementation in upcoming class):

1. Open **Google Sheets** node → **Set up credentials** → **OAuth2**
2. Provide **Client ID** and **Client Secret** from Google Cloud Console
3. Click **Save** → complete Google consent screen
4. Paste your **spreadsheet URL** in the node

If Client ID and secret are correct, n8n can act on your sheet on your behalf.

---

## Observability and Human-in-the-Loop

### Observability on the Canvas

n8n advertises: *"Every step of your agent's reasoning traceable on the canvas."*

- See **what went in** and **what came out** of each node
- When an agent **fails**, read the **error message** at the failing step
- Log decisions to a sheet or database instead of trusting black-box output

**Debugging habit:** When step 4 breaks, inspect step 3's JSON — mismatched field names are the most common issue.

### Human-in-the-Loop for Critical Actions

Not every decision should be fully automatic.

| Critical action | Why human approval matters |
|---|---|
| **Issuing a refund** | Money leaves the company |
| **Booking tickets / transfers** | Wrong booking is costly |
| **Security escalations** | False positives waste senior engineers |

Build workflows that **pause for human feedback** on high-stakes branches — especially in production agentic systems.

---

## n8n Templates, Docs, and Learning Path

- **Templates** on n8n.io — import starter workflows (HR, sales, SecOps) and study node wiring
- **Per-node Docs** — click **Docs** on any node for parameters and credential help
- **Today's scope** — platform overview, Docker install, triggers, single-node form demo, credentials concepts
- **Upcoming classes** — build **real multi-step agentic workflows** with third-party integrations end to end

**Common mistake:** Expecting a full production pipeline on day one. The instructor deliberately kept today as a **glimpse**; implementation depth comes next.

---

## Student Activities

Work through these on your own. Each takes a few minutes and mirrors classroom discussion.

### Activity 1 — Trigger Pick for a Scenario

**Scenario:** Every night at 11 p.m., compile the day's Razorpay payments and email a summary to finance.

Which n8n trigger fits best — **manual**, **schedule**, **webhook**, or **form submission**? Write one sentence explaining your choice.

---

### Activity 2 — Map the HR Onboarding Flow

Draw four boxes in order for the website HR example: **Form submit** → **?** → **Jira ticket** → **If manager? branch**.

Fill in what the missing AI/database step might do in one sentence.

---

### Activity 3 — Form Field Design

Design three fields for a **workshop registration** form: one **text**, one **email**, one **dropdown** (Beginner / Intermediate / Advanced). Mark which should be **required** and why email should use type **email** not plain text.

---

### Activity 4 — Static vs Expression

A workflow receives `marks = 85`. Write the expression rules (if/else in plain English) for grades: **A** if marks > 90, **B** if marks > 80, **C** otherwise. What grade should the workflow output for 85?

---

### Activity 5 — OAuth Permission Check

A random app asks for: **email**, **Google Drive**, **Google Photos**, and **Gmail read access** — but it only displays your profile name on screen.

List two permissions you would **deny** and one sentence why.

---

### Activity 6 — n8n vs Docker (Beginner Check)

Answer in one sentence each:

1. Is **n8n** the same thing as **Docker**? (Yes or No — then explain briefly.)
2. Name one way to use n8n **without** installing Docker.
3. After setup, write the **URL** and **port** you open in the browser. Why can a `localhost` form link not be shared with a classmate on another laptop?

---

### Activity 7 — Inspect JSON Shape

Imagine a form trigger outputs:

```json
{
  "name": "Priya",
  "email": "priya@example.com",
  "rating": 4
}
```

Write one sentence: what field might a **Google Sheets "create row"** node need mapped from this JSON?

---

## Key Takeaways

- **n8n** is a **visual workflow automation platform** with **1,500+ integrations** — drag-and-drop for most tasks, **Python/JavaScript** when you need custom agent logic.
- **n8n and Docker are not the same thing** — n8n is the automation app; **Docker is only one way to run n8n locally for free**. You can also use **n8n cloud** in the browser with no Docker at all.
- **Triggers** (manual, schedule, webhook, form, app event) answer *when* a workflow starts — connecting directly to **triggers** and **webhooks** from the **previous** lessons.
- **Nodes** are individual steps; **connections** move data forward; **expressions** compute dynamic values; **credentials** and **OAuth2** secure third-party access without plain-text secrets.
- **Docker for freshers:** install **Docker Desktop** once, run two commands, then work entirely in the **n8n web UI** at **localhost:5678** — image = installer, container = running app, volume = saved workflows.
- **Observability** and **human-in-the-loop** keep automations trustworthy — inspect each node's I/O and require approval for refunds, transfers, and similar critical actions.
- **Upcoming** classes will wire **multi-step workflows** (form → LLM → Sheets, webhooks, and more) — today you learned the workspace, vocabulary, and local setup.

---

## Important Terminologies Used

| Term | Quick meaning |
|---|---|
| **n8n** | Visual workflow automation platform (node-based canvas) — **independent of Docker** |
| **Docker** | Program that runs packaged apps in isolated boxes; **one way** to self-host n8n locally |
| **n8n cloud** | Browser-hosted n8n on n8n.io — **no Docker required** |
| **Self-hosted n8n** | n8n running on your machine/server — Docker is the recommended beginner install method |
| **Workflow** | Connected sequence of automation steps from trigger to outcome |
| **Trigger** | Event that **starts** a workflow (manual, schedule, webhook, form, app event) |
| **Node** | One step/action on the canvas (trigger, action, logic, code, AI) |
| **Connection** | Link passing output from one node as input to the next |
| **Data flow** | How information moves and transforms through the workflow |
| **Expression** | Runtime formula for dynamic values (e.g. marks → grade) |
| **Credential** | Securely stored API key or token for a third-party service |
| **OAuth2** | Protocol for third-party apps to access your account with scoped permission |
| **Environment variable** | Secret or config value set outside the workflow (e.g. `export API_KEY=...`) |
| **Hosted n8n** | n8n cloud — they run servers; you pay subscription |
| **Docker image** | Frozen installer package — the full n8n app downloaded from the internet |
| **Docker container** | Running copy of the image — n8n active on your machine right now |
| **Docker volume** | Saved folder for workflows and settings — survives container restarts |
| **Docker Desktop** | The app you install on Mac/Windows to run Docker commands |
| **Form trigger** | Workflow starts when someone submits an n8n-hosted form |
| **Webhook trigger** | Workflow starts when an external system sends an HTTP request |
| **Schedule trigger** | Workflow starts on a timer (daily, hourly, etc.) |
| **Code node** | Custom Python or JavaScript inside a workflow |
| **Observability** | Ability to trace inputs, outputs, and errors per node |
| **Human-in-the-loop** | Require human approval before critical automated actions |
| **localhost** | URL pointing to your own machine — not public on the internet |
| **Test mode** | Safe trial execution of a form or workflow during development |
| **Client ID / Client Secret** | OAuth app identifiers used to set up Google (or other) credentials in n8n |
| **Integration** | Pre-built n8n connector to an external app (Sheets, Slack, OpenAI, …) |
| **Template** | Pre-made workflow you can import and customise from n8n.io |
