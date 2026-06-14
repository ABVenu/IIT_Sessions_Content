# Pre-read: Evaluating LangChain Agents: Test Sets and Logging

## Context of This Session in the Course

```mermaid
%%{init: {"diagramPadding": 24, "flowchart": {"htmlLabels": true, "nodeSpacing": 90, "rankSpacing": 110, "curve": "basis", "padding": 20}, "theme": "base", "themeVariables": {"fontFamily": "Arial", "fontSize": "15px", "lineColor": "#334155"}}}%%
flowchart TB
    subgraph FOUNDATION[" "]
        direction LR
        M1["&nbsp;&nbsp;<b>Previous Module</b>&nbsp;&nbsp;<br/><br/>Agentic Foundation and Architecture<br/>(Python + APIs)<br/><br/><i>Tech learnt: LLM basics<br/>Prompting and backend foundations</i>"]
        M2["&nbsp;&nbsp;<b>Previous Module</b>&nbsp;&nbsp;<br/><br/>Agent Components: Memory, Tools and RAG<br/>(Memory + Retrieval)<br/><br/><i>Tech learnt: RAG pipeline thinking<br/>Chunking, embeddings and vector search</i>"]
        CM[["&nbsp;&nbsp;<b>Current Module Until Previous Session</b>&nbsp;&nbsp;<br/><br/>Integrated LangChain Agent<br/><br/><i>Retriever tool, second tool<br/>Multi-turn memory and eval pack</i>"]]
    end

    CURRENT{{"&nbsp;&nbsp;<b>Current Session</b>&nbsp;&nbsp;<br/><br/>Evaluating LangChain Agents<br/>Test Sets and Logging<br/><br/><i>eval JSON, runner, results.csv<br/>failure trace and qualitative scoring</i><br/><br/><b>Mental shift:</b><br/>from ad hoc eval pack runs<br/>to a repeatable evaluation harness"}}

    subgraph VALUE[" "]
        direction LR
        COURSE["&nbsp;&nbsp;<b>Course Connection</b>&nbsp;&nbsp;<br/><br/>Institutionalize test cases<br/>structured logging and scoring<br/><br/><i>Foundation for debugging<br/>iteration and production gates</i>"]
        REAL(["&nbsp;&nbsp;<b>Real-Life Connection</b>&nbsp;&nbsp;<br/><br/>Regression tests and audit trails<br/>for support agents before release<br/><br/><i>Know what broke, why it broke<br/>and which cases to fix first</i>"])
    end

    subgraph FUTURE[" "]
        direction LR
        M4["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Multi-Agent Collaboration and Deployment<br/>(Automation + Multi-Agent Frameworks)<br/><br/><i>Will use: n8n and CrewAI<br/>Pipelines and crew orchestration</i>"]
        M5(["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Capstone Project: Autonomous System Build<br/>(Design + Integration)<br/><br/><i>Will use: memory, RAG<br/>agents, evaluation and deployment</i>"])
    end

    M1 ==>|&nbsp;Foundation&nbsp;| CURRENT
    M2 ==>|&nbsp;Components&nbsp;| CURRENT
    CM ==>|&nbsp;Blueprint&nbsp;| CURRENT
    CURRENT ==>|&nbsp;Course Path&nbsp;| COURSE
    CURRENT ==>|&nbsp;Real-Life Use&nbsp;| REAL
    COURSE ==>|&nbsp;Next Module&nbsp;| M4
    REAL ==>|&nbsp;Capstone Use&nbsp;| M5

    classDef previous fill:#f8fafc,stroke:#475569,stroke-width:2px,color:#0f172a
    classDef current fill:#ecfeff,stroke:#0f766e,stroke-width:3px,color:#134e4a
    classDef value fill:#fff7ed,stroke:#c2410c,stroke-width:2px,color:#7c2d12
    classDef future fill:#f0fdf4,stroke:#15803d,stroke-width:2px,color:#14532d

    class M1,M2,CM previous
    class CURRENT current
    class COURSE,REAL value
    class M4,M5 future

    style FOUNDATION fill:transparent,stroke:transparent
    style VALUE fill:transparent,stroke:transparent
    style FUTURE fill:transparent,stroke:transparent
    linkStyle default stroke:#334155,stroke-width:3px
```

---

Your **e-commerce support agent** aced the live demo. The trainer asked about **returns within 30 days** — the bot searched policy and answered correctly. Someone typed **"18% GST on ₹4,200"** — the calculator tool fired. A follow-up about **order #8821** worked because **memory** was wired. Everyone nodded. The product owner said: **"Ship it Monday."**

Monday morning, real customers arrive. Case one: **"Can I return a laptop bought 45 days ago?"** — the bot invents a **15-day electronics rule** that does not exist in any document. Case two: **"What is your CEO's direct phone number?"** — instead of a polite **"I cannot help with that,"** it guesses a number. Case three: a three-turn chat where turn 3 asks **"And pickup?"** — the bot searches **shipping policy** when it should remember **order #8821** from turn 1. Your team opens three separate Slack threads. Each engineer reruns **one** question manually, gets **different** results, and argues about whether the bug is **retrieval**, **tool choice**, or **memory**.

Nobody lied in the demo. The gap was **process** — you had **no shared test booklet**, **no flight recorder**, and **no score sheet** that every run could write to the same way. In the **previous session** you built the **integrated LangChain agent** — retriever tool, auxiliary tool, multi-turn memory — and ran a compact **eval pack** to spot **wrong tool**, **weak retrieval**, and **over-refusal**. That was the right instinct. Today you turn that instinct into **infrastructure**: structured **evaluation cases**, a **runner** that executes them all, **logging** that captures what actually happened inside each run, and a **results file** you can sort, filter, and hand to the next debugging session.

---

## When "it worked in the demo" is not enough

Imagine you are the **quality lead** for a bank's chat assistant. Regulators do not accept **"we tried a few questions and it looked fine."** They want evidence: **which questions were tested**, **what the system did step by step**, **whether answers matched policy**, and **which failures repeat** after you change a prompt.

Now scale that to your **ShopEasy-style agent** with **twenty evaluation scenarios** — in-domain policy questions, out-of-domain refusals, tool-first arithmetic, multi-turn memory threads. Running them **by hand** in a notebook means:

- You forget to log **which tool** was called on case 7.
- You cannot compare **Tuesday's run** with **Thursday's run** after a prompt tweak.
- When case 14 fails, you have **no failure trace** — the full story of inputs, retrievals, tool traffic, and final reply — so the team debates from memory instead of evidence.
- A new teammate adds a **third tool** next month, and someone rewrites all twenty scenarios from scratch because nothing was **structured**.

Manual clicking does not scale. Professional teams treat agent evaluation like **regression testing** for software — same cases, same format, same log fields, every time.

---

## The challenge we will tackle

What if you had to prove — with **one command** — that your integrated agent still passes **grounding checks** after you change a tool description?

What if case **"GST on ₹4,200"** failed because the agent called the **retriever** instead of the **calculator**, but your only note says **"answer was wrong"** — with no record of **tool traffic** or **retrieved chunks**?

What if three eval cases failed for **different reasons** — one **over-refusal**, one **weak retrieval**, one **wrong tool** — and you needed to **rank** which trajectories deserve fixes first before a release meeting?

What if next month you add a **new policy PDF** or a **warehouse lookup tool** — and you want to **extend** the test harness without throwing away the evaluation philosophy you already built?

The live session answers these with a **repeatable harness**: define cases in **eval JSON** (structured test definitions with **explicit expected behaviours** for **tools**, **grounding**, and **refusal**), drive them through a **runner**, emit a **results.csv** scoreboard, and capture **failure traces** for the worst performers so debugging starts from facts, not guesses.

---

## The mystery shopper with a CCTV log

Think of **evaluating a retail store** before a festival sale.

**Mystery shoppers** arrive with a **printed checklist** — not vague impressions, but exact scripts: *"Ask about 30-day returns for electronics,"* *"Ask for the CEO's personal email,"* *"Ask 18% of ₹4,200 after mentioning order #8821."* Each line states **what good service looks like**: which **counter** the staff member should visit (policy desk vs calculator vs order desk), whether they should **refuse politely**, and whether they should **remember** what you said two minutes ago.

That checklist is your **eval JSON** — machine-readable **evaluation cases** where every scenario names the **input**, the **expected tool behaviour**, the **grounding expectation**, and the **refusal rule** where applicable. JSON here simply means a **structured text file** computers can read reliably — the same idea as a form with fixed fields, not a free-form diary entry.

The **runner** is the **coordinator** who sends every mystery shopper through the **same script** in the **same order** — no one skips case 12 because they are tired. One run, all cases, consistent conditions.

**Structured logging** is the **CCTV plus receipt printer** behind the counter. For every case it records: what the **customer said** (input), what **documents were pulled** (retrievals), every **tool call and return** (tool traffic), and the **final spoken answer**. When something goes wrong, you do not rely on the shopper's memory — you replay the log.

**results.csv** is the **mark sheet** exported after the round — one row per case with **pass / fail / partial** style outcomes you can sort in a spreadsheet. **Qualitative scoring** means you judge behaviour categories — did it ground correctly? refuse honestly? pick the right tool? — not just whether the final sentence sounded nice.

A **failure trace** is the **expanded case file** for the lowest performers — the full trajectory of a single bad run so you can see *exactly* where the agent took a wrong turn. That is how you **isolate lowest-performing trajectories** and assign fixes: patch the tool description, tune retrieval, or adjust refusal instructions — each backed by a trace, not a hunch.

When the store adds a **new service counter** (a new tool) or a **new policy binder** (a new corpus), you **add rows to the checklist** and **one column to the log** — you do not redesign the entire audit programme. That is **harness extensibility**: the philosophy stays; the catalogue grows.

---

## From eval pack to evaluation harness

In the **previous session**, the **eval pack** gave you a **shared set of scenarios** — in-domain, out-of-domain, tool-first, multi-turn — to **appraise** integrated agent behaviour and read **failure signatures**. That was **bounded evaluation**: enough to prioritise fixes in a testing block.

Today's step is **institutionalization** — making evaluation **repeatable and inspectable**:

| Piece | What it gives you |
|---|---|
| **eval JSON** | Fixed **evaluation cases** with explicit **expected behaviours** — which tool should fire, when answers must be **grounded** in retrieved text, when the agent must **refuse** |
| **runner** | One pathway that executes **all cases** against your agent the same way every time |
| **Structured logging** | Consistent fields across runs: **inputs**, **retrievals**, **tool traffic**, **final responses** |
| **results.csv** | A **sortable outcomes table** for comparing runs before and after changes |
| **failure trace** | Deep dive on **worst cases** — the full step-by-step story for focused follow-up |

**Classify qualitative outcomes** means tagging each run: **grounded pass**, **wrong tool**, **weak retrieval**, **over-refusal**, **fabrication risk** — the same language you started using with the eval pack, now **recorded systematically**. **Isolate lowest-performing trajectories** means sorting the mark sheet, opening traces for the bottom rows, and fixing those first — the way engineering teams triage production incidents.

This harness is what **upcoming** work on **debugging and iteration** will lean on: change a prompt, rerun the runner, diff **results.csv**, prove improvement with numbers and traces instead of gut feel.

---

In this pre-read, you'll discover:

- **Why** a successful demo and a compact eval pack are **not the same** as a **production-ready evaluation programme** — and what breaks when teams skip structured logging
- **How** to **define evaluation cases** in **eval JSON** with clear expectations for **tool use**, **grounding**, and **refusal**
- **How** a **runner** plus **structured logging** produce an audit trail of **inputs**, **retrievals**, **tool traffic**, and **final answers** across every case
- **How** **results.csv** and **failure traces** help you **classify outcomes**, **rank weak trajectories**, and **extend the harness** when new tools or corpora arrive — without rewriting your entire testing philosophy

---

## Words you will hear — explained right away

- **Evaluation harness:** The **full testing setup** — case definitions, runner, logging rules, and output files — that runs your agent the same way on every audit.
- **eval JSON:** A **structured file** listing evaluation cases; each case specifies the **input** and **expected behaviours** (tools, grounding, refusal).
- **Expected behaviour:** What **should** happen for a case to pass — e.g. **retriever called**, answer **quotes policy**, or **polite refusal** for out-of-domain questions.
- **runner:** A script or workflow that **loops through all eval cases** and invokes your agent with **consistent settings**.
- **Structured logging:** Writing the **same fields** every run — user input, retrieved passages, each tool call and result, final reply — so traces are comparable.
- **Tool traffic:** The **record of which tools were called**, with what arguments, and what they returned — the agent's behind-the-counter activity.
- **results.csv:** A **spreadsheet-style output** with one row per case and columns for **outcome labels** and summary scores.
- **Qualitative scoring:** Human-readable **judgement categories** (pass, wrong tool, weak retrieval, over-refusal) rather than only a single numeric metric.
- **Failure trace:** The **complete logged trajectory** for a failed or weak case — everything that happened from input to final response.
- **Harness extensibility:** Adding **new tools or document corpora** by extending cases and log fields while keeping the **same evaluation philosophy**.

---

## What you will be ready to do

After this session, you will be able to:

- **Define** structured **evaluation cases** with explicit expectations for **tool selection**, **grounded answers**, and **honest refusal**
- **Implement** consistent **logging** of **inputs**, **retrievals**, **tool traffic**, and **final responses** across all evaluation runs
- **Run** the cohort **runner** to execute the full case set and produce a **results.csv** outcomes table
- **Classify** qualitative results and **isolate lowest-performing trajectories** using **failure traces** for targeted follow-up
- **Explain** how the harness **extends** when you add a **new tool** or **new document corpus** without discarding your existing cases
- **Connect** today's infrastructure to the **integrated agent** and **eval pack** from the **previous session** — same scenarios, now **institutionalized**
- **Prepare** for **upcoming** work on **systematic debugging and iteration**, where every fix is validated by rerunning the same harness

---

## Why this matters beyond the classroom

Shipping an agent without a **regression harness** is like shipping a mobile app with **no automated tests** — every release is a gamble. Stakeholders ask **"did quality improve?"** and teams answer with anecdotes. Regulated and high-trust domains — **banking, HR onboarding, healthcare FAQs** — need **evidence**: what was tested, what failed, what changed after the fix.

Structured evaluation also saves **money**. Random manual retesting burns API tokens and engineer time. A **runner** that logs **tool traffic** shows whether a prompt change accidentally made the agent **search policy five times** for a simple calculation — a cost signal you catch before production.

Teams that build **eval JSON + runner + results.csv + failure traces** early can hand debugging to the **next engineer** with a trace file instead of a verbal recap. That discipline is what turns a classroom agent into something you would **defend in a release review**.

---

## Questions to carry into the session

1. Your **eval JSON** includes a case: user asks **"What is 18% GST on ₹4,200?"** after discussing **order #8821** in an earlier turn. The agent answers with a **policy paragraph** about refunds and never calls the calculator. What **expected behaviours** would you write in the case file for **tool use** and **grounding** — and which fields must your **log** capture to prove the wrong tool fired?

2. You run the **runner** twice — Monday before a prompt change, Thursday after. **results.csv** shows case **"CEO personal email"** failed both times, but Monday's failure was **fabrication** and Thursday's was **over-refusal**. How does comparing **failure traces** — not just pass/fail columns — tell you whether your fix moved in the right direction?

3. Next month you add a **warehouse stock lookup tool** and a **new warranty PDF**. Which parts of the harness should stay **unchanged** (runner philosophy, log field names, scoring categories) and what do you **add** (new eval JSON cases, new expected tool behaviours) so you do not rewrite evaluation from scratch?

Keep these questions in mind. The session turns your **eval pack instincts** into a **repeatable quality system** — the kind that lets you say, with evidence, **which cases pass, which fail, and exactly what the agent did wrong** before the next debugging sprint begins.
