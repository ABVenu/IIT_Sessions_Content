# Vibe Coding with Claude — Chat, Cowork, and Code

#### [Instructor Slides](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/d78eab75-d754-4159-8695-3994ad7190ba/bXLXBSmaFMGime2o.zip)

In **previous** work you built **agentic graphs** (nodes, edges, shared state), **RAG** over your own files, **golden evals**, and **token-cost** checks. Those labs answered: *what ran, in which order, and what did it cost?*

This session uses the same ideas inside a **product ecosystem**. You will treat **vibe coding** as a working style, then walk **Claude Chat**, **Claude Cowork**, and **Claude Code**. The last stretch is **cost engineering** — which model to call, when to cache, and how to read unit economics.

**What you will learn:**

- Define **vibe coding** and why you still need **domain knowledge** to check the output
- Define an **agent** as **LLM + harness** (tools, skills, connectors, MCP, system prompts)
- Choose **Chat**, **Cowork**, or **Code** for a job
- Use **Skills** (`SKILL.md`), **Connectors / MCP**, and **human-in-the-loop** approvals
- Route work across **Haiku**, **Sonnet**, and **Opus**
- Read the **Anthropic Messages API**, **thinking tokens**, **prompt caching**, and **Batch API**
- Rebuild a tiny **RAG + Streamlit** app from local Word files with **Claude Code**

---

## What Vibe Coding Means

**Vibe coding** is a label, not a magic compiler. **Andrej Karpathy** coined it in a tweet: give instructions to an LLM, let it write the code, and (in the original joke) barely inspect the result.

- **Official Definition:** **Vibe coding** is building software by describing intent in natural language and letting a coding agent generate, edit, and run the implementation.
- **In Simple Words:** You talk; the agent types. You still have to judge whether the result is right.
- **Real-Life Example:** Asking a junior to “make the hostel notice board look nicer” without reviewing the poster before it goes on the wall.

![Student giving a spoken prompt to a coding agent, then checking the printed hostel notice against the generated result](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-01-vibe-coding-review.png)

People were already doing this before the name existed. The name made it more common — and easier to skip review.

**Better habit:** Keep some **domain knowledge**. You do not need every line by heart, but you must be able to **check** the output: Does the dashboard use the numbers on the sketch? Does the Excel formula treat `O` as zero? Does the hire/fail gate match the job description?

A “build a game in chat” demo can be fun and still be low quality. **Prompt quality** and **review** decide the difference.

---

## How an LLM Reads Language (Short Recap)

Before agents, remember how the **brain** of the agent actually sees text.

Modern **LLMs** grew from **transformer / attention** models (Google, **2017** — BERT and the transformer paper). Older chatbots such as **ELIZA** did not work this way. **Classical NLP** pipelines and **LLMs** are related but not the same thing.

- **Tokenization:** Text is split into **tokens**, not always whole words. `beautiful` may be one token; a compound or rare word may split.
- **Embeddings:** Each token becomes a **vector** (a list of numbers). The model then does **math** on those vectors.
- **King–queen style analogy:** “King is to queen as husband is to ___” → **wife**. The model is not “recalling a riddle.” It is using **distances** between vectors that already sit near related words.

Machines do not “understand 2 + 3” the way you do. They operate on tokens and vectors. That is why **the same idea in a messy prompt** can produce a messy program.

---

## Agent = LLM + Harness

**Claude Code** is an **agent**. So is a Chat session with connectors. So is a third-party coding agent such as **Hermes**.

- **Official Definition:** An **agent** is an **LLM** plus a **harness**: system prompts, **tools**, **MCP** servers, **skills**, and permission rules that let the model *act*, not only *reply*.
- **In Simple Words:** The LLM is the brain. The harness is the hands, the rulebook, and the toolkit.
- **Real-Life Example:** A bank clerk (LLM) plus passbook printer, cheque scanner, and “never skip KYC” poster (harness). Same clerk, different counter, different results.

The same model in two harnesses will not behave the same. That idea returns in the Excel add-in vs Copilot comparison later.

| Piece of the harness | Job |
|---|---|
| **System prompt** / **CLAUDE.md** | Standing rules for this folder or this role |
| **SKILL.md** | Reusable how-to for one task type |
| **Tool / connector** | Actual permission to Gmail, Chrome, disk, Excel |
| **MCP** | Custom tool server you plug in by URL |
| **Human approval** | You confirm a dangerous or external action |

![LLM brain on a workbench surrounded by harness objects: SKILL.md, CLAUDE.md, Gmail Chrome Excel Disk tools, MCP plug, and an Approve stamp](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-02-agent-harness.png)

**Common mistake:** Calling a skill a “permission.” A skill teaches *how*. A **connector** grants *access*.

### A coding agent at work (Hermes + nano-GPT)

A host demo used **Hermes** on **Karpathy’s nano-GPT** repo (a tiny **PyTorch** GPT in about **350 lines**, three real files).

1. “Use your **GitHub skill** and clone this repo into this folder.”
2. Hermes **reads the skill**, **clones**, then lists files.
3. “Explain this codebase” → repeated **read_file** tool calls, then a walkthrough.
4. Training data is **not** in the repo. `prepare.py` downloads **Tiny Shakespeare** and tokenizes it. You must **prepare once** before a demo.
5. Default GPT-2-scale configs can **run out of memory** on an **8 GB** GPU once optimizer states are included. Production training uses much larger **accelerator** cards (32 GB / 64 GB and up).

**Why some people pick Hermes over Claude Code or Codex:** less **vendor lock-in**.

Claude Code wants an Anthropic subscription; Codex wants an OpenAI one. Hermes can swap models or point at a **local** LLM. Today the products overlap; some agents still pair better with some models.

**Claude plugins and add-ins do not take Ollama.** Inside Claude’s own harness you stay on **Anthropic** models. Your *own* agent can talk to Groq, local weights, or anything else.

---

## Paradigm Shift: Chat Assistant → Consultant Workflow

Most of us started with **conversational AI**: ask → answer → you stitch the next step.

The shift in this ecosystem is **AI as a consultant**: you **show the problem** (files, a sketch, a dirty spreadsheet, a folder), and the agent runs a **multi-step workflow**.

| Old habit | New habit |
|---|---|
| Long prompt that lists every step | Short prompt + **the artefact** (PNG, CSV, folder) |
| Download from chat A, upload to chat B | One workspace with **memory of the task** |
| You are the orchestrator | The agent plans, calls tools, and writes outputs |

- **Official Definition:** **Claude Chat** is the conversational product surface (web or Desktop **Chat** tab) for prompts, uploads, and replies in one thread.
- **In Simple Words:** The familiar chat box — like ChatGPT, from Anthropic.
- **Real-Life Example:** Asking one question — “write a 55-inch TV ad campaign” — and reading the answer in the same window.

**When Chat is enough:** clear start and end, **no** dependency on previous steps, **no** need for task memory across sessions. Draft a mail. Summarise one PDF. Brainstorm that TV campaign.

**When Chat is painful:** a **weekly report** that must gather sources, analyse trends, take feedback, and publish. You can force it in chat, but you become the glue.

Access: **[claude.ai](https://claude.ai)** or **Claude Desktop**. Much of the desktop power is **subscription-based** — unlike a free ChatGPT-style playground for many features.

---

## Three Layers in Claude Desktop

Claude Desktop groups the same brain into three working modes.

| Layer | You bring | The agent can |
|---|---|---|
| **Chat** | Text, uploads, one conversation | Answer, draft, use skills and connectors **in that thread** |
| **Cowork** | A **folder** on disk | Read/write local files, run OS-level commands, schedule tasks |
| **Code** | A **dev folder** (and often VS Code) | Vibe-code apps, edit trees, run and **self-test** UIs |

**Chat** = bring the task to the model. **Cowork** = show the model the **workspace**. **Code** = the same local idea, aimed at **software**.

![Three Claude Desktop stations: Chat for a TV ad prompt, Cowork on a local department folder with CLAUDE.md, and Code with VS Code plus a Streamlit RAG UI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-03-chat-cowork-code.png)

### Activity — pick the layer

Write **Chat**, **Cowork**, or **Code** (or a pair):

| Need | Your pick |
|---|---|
| One TV ad slogan, no files | |
| Monthly pack from five department files already on disk | |
| Streamlit UI on two Word docs in `outputs/` | |
| Daily 8am inbox categorisation via Gmail | |

**Check:** slogan → Chat. Monthly pack → Cowork. Streamlit → Code. Inbox at 8am → Cowork **schedule** (Gmail connector).

---

## Skills — Reusable Instruction Files

**Skills** are how Claude stops you from re-pasting the same mega-prompt.

- **Official Definition:** A **skill** is a reusable workflow stored mainly as **`SKILL.md`** — a detailed instruction set the agent can load when the user request matches.
- **In Simple Words:** A saved recipe. Say “create a document” and Claude loads the **docx** skill without you naming it.
- **Real-Life Example:** A hostel mess card that already lists portion size, oil, and garnish — the cook does not invent the recipe every night.

Built-in skills live under paths such as `/skills/public/docx`. Hover the skill in the UI and you see the **Markdown** instructions: page size, formatting, allowed commands.

You can add **custom skills** (the session’s planned example: an **EDA** skill with its own `SKILL.md`). You can also set **Claude Instructions** on the desktop — standing rules across Chat and Cowork.

**Need:** Chat follow-ups are **not reusable**. A new session forgets the ritual unless it is a skill.

**Logic:** Claude is unusually **visible**. It shows which skill loaded and which bash/commands ran. Treat that as the opposite of a black box.

---

## Prompting Shift and a Multimodal Dashboard

The old habit was a **very long prompt** (what to do and how). The new habit, especially **multimodal**, is: **show the problem** and state the outcome.

**Live demo prompt** (whiteboard / PNG wireframe of a dashboard):

> Build this as a single-file working dashboard. Use the numbers written on the sketch. Make case titles turn red when the target is missed.

Claude loaded the built-in **`front-end-design`** skill (`front-end-design SKILL.md`) and returned a **single HTML file** — clickable, inspectable, downloadable.

HTML is the language of the web. Inspect any site and you will see the same family of tags. A sketch → HTML path is a fast way to prototype a campus dashboard or a small website.

---

## Model Tiers: Haiku, Sonnet, Opus

Not every step deserves the most expensive brain.

| Model | Role in the family | Typical jobs |
|---|---|---|
| **Haiku** | Fastest and cheapest | Classification, tagging, extraction, **routing / triage**, lookups |
| **Sonnet** | Balanced default | Everyday writing, reports, summaries, most Cowork runs |
| **Opus** | Strongest reasoning | Deep multi-step decisions, research, **final hiring calibration** |

**Support-desk routing picture:** Haiku handles general inquiries. **Sonnet** drafts a balanced complaint reply. **Opus** handles a **refund** that needs careful reasoning. In a well-designed desk, only a tiny slice of traffic (the session used “about **0.01%**”) should hit Opus.

![Query routing from Haiku triage into Haiku, Sonnet, and Opus lanes, with thinking tokens billed as output](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-07-model-routing.png)

**Tradeoff dimensions:** **speed vs quality vs cost**, plus **latency**. Instant FAQ answers want Haiku. A refund that can wait a few seconds can use Opus.

The same idea exists across vendors (a small router model, a stronger specialist). The rule is **right model for the step**, not one model for the whole factory.

### Reasoning tokens are output tokens

In the UI you may expand a **thinking** block. Those tokens are still **billed as output**, even when hidden.

- **Extended thinking** can multiply usage (session ballpark: **3–5×**).
- For project budgets, keep a **30–40% buffer** for thinking.
- From **Sonnet 4.6 / Opus 4.6** onward, Claude often uses **adaptive** thinking (the provider chooses the thinking budget). Older APIs let you set `budget_tokens` explicitly. Hidden reasoning is still billed.

---

## Connectors, MCP, and Plugins

**Chat is already an agent** once tools are attached.

- **Official Definition:** A **connector** is an external tool call — Gmail, Drive, Calendar, Slack, Chrome, Excel, PowerPoint, or a **custom MCP** server you register by URL.
- **In Simple Words:** A plug that lets Claude *do* something outside the text box.
- **Real-Life Example:** Giving the clerk a phone line to the warehouse, not only a notepad.

**Custom connector (live):** add an MCP server (the session used a **Hugging Face** MCP) — name + URL.

**Plugin:** a **bundle** of several skills **and** several connectors for one role. Skills without connectors still cannot browse Amazon or draft Gmail.

![Layer diagram of SKILL.md for how-to instructions, Connector and MCP for access, and a Plugin that packs both](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-06-skills-connectors-plugin.png)

Built-in examples shown: Gmail, Calendar, Drive, Slack, weather, health, code, Microsoft 365 / Outlook, Excel, PowerPoint.

### Gmail + Chrome research workflow

**Prompt** (Sonnet, high effort):

> Research the top 5 55-inch TVs from Amazon via Chrome. Collate a short summary document and save it as a draft in Gmail.

**Prerequisites:** Gmail connector on; **Claude in Chrome** extension installed and signed in.

**What you should see:**

1. Claude searches tools → `chrome` navigate.
2. **You approve** which browser tab it may control (orange overlay: controlled by Claude).
3. It reads Amazon, writes a summary, then the **Gmail connector** creates a **draft** (checked in Gmail during the live run).
4. “Send to X” is a further permission, not automatic.

You can skip all permissions at the start of a conversation. The live run kept **approvals** so the class could see the gates.

**Browser caution:** a browser agent sees **logged-in sessions**. Prefer **read-only** where possible, a **separate browser profile**, and approval gates. A custom site (the session mentioned **USPTO**-style government pages) is not “just browse it.” Use an official **rate-limited API + MCP**, with cache, retries, and human review.

### Browser agent comparison: Perplexity Comet

**Comet** is a **browser-first** agent. Claude-in-Chrome is a **broader** agent (connectors + skills + browser).

**Comet prompt (LinkedIn):** find top 3 leaders to reach at a company/location; **draft** a short message for the top leader; **do not send**. Comet opened compose and used **memory** (a past collaboration not written in the prompt). Prefer **Sonnet** there too if you have a choice.

---

## Excel Add-in — Healthcare Data Cleaning

Same LLM idea, different harness: **Claude inside Excel**.

**Dataset:** a messy **healthcare CSV** — blood types written many ways (`B negative` vs `AB negative`, `A+VE` vs `A positive`, stray `0`), billing amounts with letter **O** instead of zero (`6452O`), missing cells, admission and discharge dates.

**Prompt used (about six lines — vibe-coding style):**

```text
Clean the data given the issues present.
Also add a few calculated columns as you deem important.
Finally build a simple dashboard with a few key insights which can enable us to take action.
```

Claude wrote Excel formulas and added columns such as **length of stay**, **age group**, **billing per day**, and **admission month**. Output: a cleaned sheet plus a **Dashboard** sheet with charts and a **key insights** paragraph — in a few minutes.

Alternatives named: **ChatGPT Excel add-in** (free up to a limit), **Microsoft Copilot**. Copilot may call a Claude-class model internally and still look different because the **harness** differs.

**Human-in-the-loop:** the add-in flagged a **dangerous** range clear (`A89:C89`) and asked. That is the same family of idea as a **LangGraph interrupt / resume**. Settings trade **safety** vs **approval fatigue** (accept all edits vs ask first).

You still need judgement: when a **pie** chart is the wrong chart, when a trend is fake, when a formula is legally wrong. AI writes **VLOOKUP**-style work quickly; **you** own the meaning.

---

## Claude Cowork — Filesystem Agent

**Cowork** is a **local filesystem agent**. You grant a folder. It reads, writes, and can run **OS-level commands**.

- **Official Definition:** **Cowork** runs multi-step workflows against a **local workspace**, with optional **scheduled** recurrence and **parallel** subtasks.
- **In Simple Words:** Chat uploads; Cowork **lives in the folder**.
- **Real-Life Example:** A chartered accountant who sits in your accounts cupboard vs one who only reads the PDFs you email.

**Agent coordination:** break a big ask into subtasks; run disconnected work **in parallel** (same idea as parallel nodes on a graph).

**Scheduled tasks:** `/schedule` or the Schedule UI. Examples: weekdays **8am** — categorise Gmail, draft important, park junk; **daily briefing** from Gmail + Outlook calendars for tomorrow’s urgent meetings. Built-in templates exist; you can still write a custom schedule.

**Risks you must name:** privacy of local files and browser sessions; a bad command that **deletes** instead of creating a PPT; **approval fatigue**; **compliance**. Guardrails belong in **CLAUDE.md**, not only in your head.

The deck names **ReAct** (reason + act in a loop) as the pattern behind this tool-using behaviour. You stay in charge of approvals.

### Monthly close pack (live)

**Problem:** five department files — **Finance, Sales, Support, Product, HR**. An operations director needs a **monthly close pack**. Manual work was described as about **three hours**. Cowork works **without uploads**.

**`CLAUDE.md`** in the folder is the standing system prompt: role, folder map, KPI targets, “what not to do,” and the close-pack steps. Markdown (`.md`) is the instruction format of this ecosystem.

```markdown
# Monthly close pack
You are the operations analyst for this workspace.
Keep Finance, Sales, Support, Product, and HR source files.
Write finished files only into outputs/.
Never delete source files. Reconcile KPIs before commentary.
```

**Run shape:**

1. Keep the five sources + `CLAUDE.md`. Empty or reset `outputs/` if you are rerunning.
2. New Cowork task → **grant folder access**.
3. Ask for the monthly close pack (Sonnet is a reasonable default).
4. Approve disk access. Cowork reads `CLAUDE.md`, reads sources, **plans**, then writes.

**Outputs in the live run:** three files under `outputs/` (Word docs plus a heavy Excel dashboard), with commentary and methodology, stamped at session time.

![Cowork working on a local folder of Finance Sales Support Product HR files plus CLAUDE.md, then writing a Monthly close pack into outputs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-05-cowork-monthly-close.png)

**What made it agentic:** no upload hop; `CLAUDE.md` auto-loaded; planning before acting; local FS + OS commands; you could `/schedule` this monthly.

### Activity — write a tiny CLAUDE.md

In a notes file, write **six lines** for a campus folder that contains `attendance.xlsx` and `notices/`: who the agent is, where it may write, and one hard rule (for example: never delete source files).

---

## Anthropic Messages API and a Four-Layer Hiring Workflow

Desktop tools are one harness. **Production** workflows use the **Messages API**.

Anthropic does **not** put `role: system` inside the `messages` array the way some OpenAI-style clients do. **`system` is a top-level argument.**

```python
from anthropic import Anthropic  # Official SDK for the Claude Messages API

client = Anthropic()  # Uses ANTHROPIC_API_KEY from the environment

EXTRACT_SYSTEM = (  # Layer 1: extraction instructions
    "Extract a JSON profile with keys: "  # Tell the model the schema
    "name, years_experience, languages, distributed_systems."  # Fields used in the live lab
)

resume_text = (  # Sample CV fragment in the same spirit as the demo
    "Priya Sharma. Six years. Python, Java, Kafka. "  # Candidate used in class
    "Distributed systems at scale."  # Skill the JD will later test
)

response = client.messages.create(  # One complete API call
    model="claude-haiku-4-5",  # Cheap model for structured extraction
    max_tokens=400,  # Upper bound on completion tokens
    system=EXTRACT_SYSTEM,  # System prompt lives here, not as a message role
    messages=[  # Only user/assistant turns go in this list
        {  # First user turn
            "role": "user",  # Speaker
            "content": f"Extract the structured profile from this resume:\n{resume_text}",  # Task
        }
    ],
)

print(response.model)  # Which snapshot actually ran
print(response.stop_reason)  # end_turn = finished; max_tokens = truncated
print(response.usage.input_tokens)  # Input tokens billed
print(response.usage.output_tokens)  # Output tokens billed
print(response.content[0].text)  # JSON profile as text
```

**How the code works**

- `Anthropic()` does not hard-code the secret; the key stays in the environment.
- `system=` is the standing instruction. The user message is only the resume.
- `stop_reason == "max_tokens"` means you cut the answer off. The live demo set **`max_tokens=8`** once to show truncation on purpose.
- For **triage**, Haiku can answer **pass/fail** with **`max_tokens=16`**. You do not pay for an essay.

### Four layers (Priya Sharma vs Lumen Analytics JD)

| Layer | Model | Job | Output |
|---|---|---|---|
| **1. Extract** | Haiku | Resume text → JSON profile | Structured fields |
| **2. Triage** | Haiku | Meet the **minimum bar** for the JD? | `pass` / `fail` |
| **3. Analyse** | Sonnet (+ thinking) | Skill-gap vs JD; keep **history** for recruiter follow-ups | Gap analysis |
| **4. Decide** | **Opus 4.6** | VP Engineering **calibration review** | Hire recommendation |

![Four hiring stations in a row: Haiku extract, Haiku triage pass/fail, Sonnet skill-gap analysis, Opus VP calibration for Priya Sharma versus Lumen Analytics](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-04-hiring-four-layers.png)

One model does not do the whole factory. **Haiku** parses and gates. **Sonnet** reasons about gaps. **Opus** makes the expensive, high-stakes call.

**Older thinking API** (deprecated on newest snapshots, still useful to understand billing):

```python
from anthropic import Anthropic  # Same SDK as the extraction call

client = Anthropic()  # Same environment key

response = client.messages.create(  # Sonnet layer with explicit thinking budget
    model="claude-sonnet-4-6",  # Analysis model from the four-layer lab
    max_tokens=8000,  # INCLUSIVE of thinking — only 3000 tokens left if thinking uses 5000
    thinking={"type": "enabled", "budget_tokens": 5000},  # Reserve 5000 tokens for hidden reasoning
    system="You are a recruiter doing skill-gap analysis versus the JD.",  # Layer 3 standing role
    messages=[{"role": "user", "content": "Compare Priya Sharma to the Lumen Analytics JD."}],  # Task
)

print(response.stop_reason)  # end_turn means it finished inside the 8000 cap
print(response.usage.output_tokens)  # Billed output; includes thinking tokens
```

**How the thinking call works**

- `budget_tokens=5000` plus `max_tokens=8000` leaves **3000** tokens for the visible answer. Cross that and you truncate.
- A live inspect showed about **1514** reasoning tokens and a ~**600** character summary. Newer **4.6** APIs prefer **`type: "adaptive"`** (or an effort setting); Anthropic allocates thinking.

**Thinking on** usually means more confident answers and more tokens. For a **wrong hire**, that extra cost is easier to justify than for a 25,000/day listing rewrite.

Package the four calls as **one function** that returns an **interview brief** plus the final recommendation. Then log **cost and latency** for each layer.

---

## Prompt Caching, Batch API, and Unit Economics

Building the graph is not the end. **It boils down to the math.**

- **Official Definition:** **Prompt caching** reuses a stable prefix of a prompt so later calls with the same prefix are billed at a **cached input** rate for a short **TTL** (session figure: about **five minutes**).
- **In Simple Words:** If the long system prompt did not change, do not pay full price for it again.
- **Real-Life Example:** The printed exam instructions stay the same for every student; only the answer sheet is new.

Session price sketch: if normal input is about **$1.75 per million** tokens, **cached input** was shown at about **one-tenth** of that. Cached output may also appear on the provider’s price table. The same *idea* exists at other providers.

**Batch API:** for work that is **not latency-sensitive**, discounts in the **50–90%** range were cited. Generating **real-estate listing** copy for a CMS is a batch-shaped job.

### Worked example — 25,000 listings a day

| Quantity | Value used in class |
|---|---|
| Volume | **25,000** listings / day |
| System prompt | **145** tokens |
| User message | **83** tokens |
| Base annual cost | **$7,738** |
| After Batch API (~50% off) | **$3,869** / year |
| After caching + **12%** retry / thinking buffer | Lower still |
| **Unit cost** | about **$0.0004** per listing |

Cost **scales linearly** with volume. After Batch + cache you still add a retry buffer for failures and extra reasoning.

**Always compute for every workflow** (RAG, single agent, LangGraph): input tokens, output tokens, **reasoning tokens**, then **per-unit** cost.

### Model selection order (cost is last)

Do **not** start with “pick the cheapest model.” Rank:

1. **Cost of failure** — wrong hire vs slightly clumsy listing text
2. **Reversibility** — can a human fix it before damage?
3. **Volume** — 25k/day vs a handful of hiring decisions
4. **Criticality / regulation / audit**
5. **Latency sensitivity**
6. **Dollar cost of tokens**

| Use case | Lean toward | Why |
|---|---|---|
| Real-estate listing → CMS | **Haiku + Batch** | Low failure cost; editable; huge volume; no need for instant replies |
| Government **benefits pre-screening** | **Opus-class** | Wrong **denial** withholds food or medicine; hard to reverse; appeals and audit |

Incorrect denial of rations or medicine is not a “retry the listing” problem. That is why a powerful model can still be the **cheaper** choice in total risk.

### Activity — unit cost sketch

Take any one API call you already have (RAG answer, classifier, or hire gate). Write down **input tokens**, **output tokens**, and whether thinking was on. Multiply by a published per-million price. Divide by the number of real-world items that call represents. That is your first **unit economics** sketch.

---

## Claude Code — RAG and Streamlit from a Folder

**Claude Code** reuses Cowork ideas (**skills**, folder access) for **development**. Open the **Code** tab in Claude Desktop, or the **VS Code** add-in (often nicer for daily engineering).

**Live prompt** after granting `co-work exercise/outputs/`:

> Please use the two Word document files and build a simple RAG system, then build a Streamlit UI where users can ask questions and get answers.

What appeared locally: a **`RAG_app/`** folder, **`.env`**, Python RAG logic, and a Streamlit app. The agent **cannot invent API keys**. The live run switched `.env` to a **Groq** key and a **GPT-OSS 20B** model when the Anthropic key was not set.

![Pipeline from monthly-close Word docs through RAG_app chunk embed store retrieve into a Streamlit Q and A window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/masterclass/session01-vibe-coding-claude/session01-08-rag-streamlit-pipeline.png)

The agent **self-tested** the UI (clicks, typed questions). Streamlit opened; Q&A over the monthly-close Word docs worked.

Follow-up vibe edits (“add a ready expansion,” “add information compression”) can patch UI files **without** you opening the editor. The next improvement is **efficiency**: caching, the right model per step, evals, or an **agentic RAG** loop in the **ReAct** style.

---

## Key Takeaways

- **Vibe coding** is instruction-driven building. Keep enough **domain knowledge** to verify the result; do not ship the first generation blindly.
- An **agent** is **LLM + harness**. **Skills** teach how; **connectors / MCP** grant access; **CLAUDE.md** is folder-level law. The **same model** in two harnesses is two different products.
- Use **Chat** for one-shot work, **Cowork** for local multi-file workflows and schedules, **Code** for apps. Route **Haiku → Sonnet → Opus** by **failure cost**, not by habit.
- **Thinking tokens are output tokens.** **Prompt caching** (short TTL) and **Batch API** change unit cost. Compute **input / output / reasoning** and a **per-item** price for every workflow you ship.

Upcoming work will keep asking you to **design the harness** and the **bill**, not only the happy-path demo — whether the next build is RAG, a graph, or a multi-agent desk.

---

## Important Commands, Libraries, and Terminologies

| Term / artefact | Meaning in this session |
|---|---|
| **Vibe coding** | Karpathy’s name for LLM-written code from natural-language intent |
| **Agent / harness** | LLM + tools + prompts + MCP + permissions |
| **Hermes** | Model-agnostic coding agent used to clone and explain **nano-GPT** |
| **nano-GPT** | Minimal PyTorch GPT; **Tiny Shakespeare** via `prepare.py` |
| **Claude Chat** | Conversational surface at claude.ai / Desktop Chat tab |
| **Claude Cowork** | Local filesystem + OS commands + `/schedule` |
| **Claude Code** | Same local idea for software (Desktop Code tab or VS Code) |
| **SKILL.md** | Reusable task recipe (docx, front-end-design, custom EDA) |
| **CLAUDE.md** | Folder-level standing instructions |
| **Connector / MCP** | External tool; custom MCP added by URL (e.g. Hugging Face) |
| **Plugin** | Pack of skills + connectors for a role |
| **Haiku / Sonnet / Opus** | Fast-cheap / balanced / deep-reasoning Claude tiers |
| **Messages API** | `client.messages.create`; `system=` is top-level |
| **stop_reason** | `end_turn` vs `max_tokens` |
| **Prompt caching** | Cheaper reuse of a stable prompt prefix (~5 min TTL in the talk) |
| **Batch API** | Discounted, higher-latency bulk calls |
| **ReAct** | Reason–act loop behind tool-using agents |
| **HITL** | Human approval (Chrome tab, Excel dangerous edit, LangGraph interrupt) |
| **anthropic** | Python SDK used for the hiring pipeline |
| **Streamlit** | UI Claude Code generated on top of local RAG |
| **Groq / GPT-OSS 20B** | Substitute LLM in `.env` when Anthropic key was missing |
