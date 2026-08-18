# Capstone Project Phase — Buffer & Submission

## Introduction

In the **previous** session you put **Nimbus PayDesk** behind a **Streamlit** counter, wrote a **demo-path cost** note, ran a short live story with **traces**, and captured a honest **retro**.

A good demo still fails submission if a reviewer cannot run it **without you in the room**. This session packs the file: a **checklist**, a **README**, **one stretch** only if G01–G03 still pass, and a **cross-team review**. Then the course wrap: what you can defend in an exam, and what support hours are for.

**What you will learn:**

- Complete a **submission checklist** (code, prompts, eval set, recording if required)
- Write a **README** with setup, env vars, and how to run evals
- Implement **one stretch** if the core path is stable
- **Submit** and review a partner desk from their README only

![Submission tray with code folder, prompt file, golden clipboard, sample JSONL, and a short demo recording card](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session64/session64-01-submission-tray.png)

---

## Submission Checklist: What “Done” Means

Reviewers are tired. They follow a list. If your zip is a mystery tour, they will score the mystery.

- **Official Definition:** A **submission checklist** is the minimum set of artifacts that prove the product runs, is bounded, and was evaluated.
- **In Simple Words:** Everything a stranger needs to replay G01–G03.
- **Real-Life Example:** A passport file: form, photo, old booklet — not a bag of unmarked photocopies.

**Tick these before you zip:**

| Artifact | Passes when |
|---|---|
| **Code** | `app/graph.py` runs; Streamlit imports the **same** graph |
| **Prompts** | `prompts/extract_v1.txt` exists even if live G01 used labels |
| **Golden set** | `eval/golden.json` or `eval/run_golden.py` with G01–G03 |
| **Sample traces** | `logs/sample_paydesk.jsonl` with three anonymised lines (no PAN) |
| **Cost note** | `docs/cost_note.md` with assumptions |
| **Retro** | `docs/retro.md` — four bullets, no fake SLOs |
| **Recording** | Only if your programme asked; same clicks as the live script |
| **Secrets** | `.env` gitignored; `.env.example` has empty `GROQ_API_KEY=` |

**Must not be in the zip:** `paydesk.db` full of classmates’ names, live API keys, a `pay_vendor` script, screenshots of other people’s Groq dashboards.

**Common doubt:** “Can I submit only the Streamlit file?”  
No. Without graph + golden + handbook, the window is a poster.

### Activity — Zip Audit

List three files you would delete from a teammate’s zip. **Sample:** `.env` with a key, `__pycache__`, a bank SDK.

---

## README: The Visitor Guide

If the README is a novel, nobody runs evals. If it is three logos, nobody knows the hard rule.

- **Official Definition:** A **README** is the operator document: what the desk is, how to install, which env vars, how to eval, and what it will refuse.
- **In Simple Words:** A visitor guide stuck on the seva-counter glass.
- **Real-Life Example:** A lab notice: “Wear shoes. Start the machine. Do not use the furnace.”

![One-page PayDesk README on the counter glass: job sentence, setup steps, eval command, and a no-NEFT rule](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session64/session64-02-readme-guide.png)

**Headings to include (keep each short):**

1. **What this is** — one sentence job + `ready_to_pay` is a recommendation
2. **What this is not** — no NEFT, no live GST portal, no OCR promise
3. **Setup** — Python version you actually used, `python -m venv .venv`, `pip install -r requirements.txt`
4. **Environment** — copy `.env.example`; `GROQ_API_KEY` optional for G01–G03 lab path
5. **Seed** — `python scripts/seed.py` for sqlite3 **and** `seed_policy()` so Chroma has `data/policy.md`
6. **Run the desk** — `streamlit run app_ui.py`
7. **Run evals** — `python eval/run_golden.py` — expect three **pass** lines
8. **Evidence** — where JSONL is written
9. **Known limits** — labelled extract; human stamp not in core path unless your stretch added it

```markdown
# Nimbus PayDesk

PayDesk files vendor bills for Nimbus Retail. It recommends ready_to_pay.
It never sends NEFT.

## Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

## Eval (must pass)
python eval/run_golden.py
# G01 CLEAN → ready_to_pay
# G02 HIGH → needs_human / amount_gate
# G03 BADGST → needs_human / gst_mismatch

## UI
streamlit run app_ui.py
```

**How this README works**

- Commands are **copyable**. Stories stay in lecture notes, not here
- Expected outcomes are **named**. “It should work” is not an eval
- The hard rule sits in the **first** paragraph so a skimming reviewer sees it

**Env example:**

```text
# .env.example — safe to commit
GROQ_API_KEY=
# Leave blank if you only run labelled G01–G03
```

Never commit the filled `.env`. You practised this on Render and on the parcel hatch.

### Activity — Partner Cold Start

Give your README to a partner. You may not speak. If they cannot run G02 on a cold start, the README failed — not the partner.

---

## One Stretch — Only After the Core Holds

Stretch is **optional**. A broken HIGH plus a fancy hatch is a worse submission than a boring desk that stops.

- **Official Definition:** A **stretch goal** is one extra capability added after the golden path is stable.
- **In Simple Words:** One bonus door, not a second product.
- **Real-Life Example:** After the seva counters work, you add a token SMS — you do not add a printing press in the lobby.

![Three optional stretch doors: Groq messy extract, LangGraph checkpoint stamp, GST cache photocopy — bank vault still locked](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session64/session64-03-stretch-doors.png)

**Pick at most one:**

| Stretch | Uses what you already learned | Done when |
|---|---|---|
| **A. Groq messy extract** | Versioned prompt + structured JSON | One unlabelled bill fills the same `InvoicePacket`; G02 still stops |
| **B. Checkpoint + stamp** | LangGraph persist and resume | HIGH pauses; a human `stamp` resume; router still cannot self-approve |
| **C. GST lookup cache** | Ops caching | Repeat `check_gstin` is cheap; **never** cache final `ready_to_pay` |

**Thin Groq extract sketch (stretch A):**

```python
# app/extract_groq.py — optional messy-prose path; same packet as labels
import json  # S46 structured output
import os  # env vars
from pathlib import Path  # prompt file
import urllib.request  # HTTPS call, same idea as the Groq hatch you already ran


def extract_with_groq(raw: str) -> dict:  # fills InvoicePacket fields
    system = Path("prompts/extract_v1.txt").read_text(encoding="utf-8")  # versioned script
    body = json.dumps({  # chat payload
        "model": "llama-3.1-8b-instant",  # classroom Groq model you already used
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": raw},
        ],
        "temperature": 0,  # stable extract
    }).encode("utf-8")  # bytes for the request
    req = urllib.request.Request(  # Groq chat endpoint
        "https://api.groq.com/openai/v1/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + os.environ["GROQ_API_KEY"],  # never hard-code
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:  # bounded wait
        reply = json.loads(resp.read().decode("utf-8"))  # envelope
    text = reply["choices"][0]["message"]["content"]  # model JSON string
    parsed = json.loads(text)  # S46: parse or fail closed
    parsed["prompt_version"] = "extract_v1"  # eval gate field
    parsed["confidence"] = float(parsed.get("confidence", 0.5))  # number
    return parsed  # same keys as parse_labelled
```

**How the code works**

- Uses **Groq + JSON parse** you already practised — not a new API framework and not Pydantic
- If JSON is malformed, extract should lower confidence and let policy demand a type-check
- After this stretch, re-run G01–G03 on **labelled** bills. They must still pass. Then try one messy bill; HIGH must still hit `AMOUNT_GATE`

**Checkpoint stretch (B):** persist graph state when `amount_gate` fires; resume only after a **human** function writes `stamped=True`. The graph must not set that flag itself.

**Cache stretch (C):** key = GSTIN string; value = `KNOWN`/`UNKNOWN`; TTL short. If you cache `ready_to_pay` keyed by vendor name, you have rebuilt the unsafe ops mistake on purpose.

**Forbidden stretches:** payout, live GST scraping, “auto-approve festival week,” deleting G03 because it is awkward.

If G01–G03 are not all **pass**, **do not stretch**. Fix the core. Write in the retro that stretch was skipped on purpose.

---

## Cross-Team Review and Course Wrap

Submission is not only upload. It is **someone else** surviving your README.

- **Official Definition:** **Cross-team review** is a paired run where the reviewer follows only committed docs and records pass/fail plus one UX note.
- **In Simple Words:** Swap counters. No whispering the GSTIN.
- **Real-Life Example:** A new clerk on Monday follows the SOP, not the person who “usually remembers.”

![Two student teams swapping laptops at a review table, running G01 to G03 from README with a pass-fail sheet](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session64/session64-04-cross-team-review.png)

**Reviewer sheet (copy into `docs/review.md`):**

| Check | Pass? | Note |
|---|---|---|
| README ran without the author | | |
| G01 ready | | |
| G02 amount_gate | | |
| G03 gst_mismatch | | |
| UI does not say paid | | |
| `.env` not in git | | |
| Stretch (if any) still uses the same graph | | |

**You may speak only after** the partner finishes G03. Then fix **one** README hole if it blocked them.

**Course wrap (what you can defend):**

- You selected a **money-harm** scenario and refused a bank tool
- You orchestrated with **LangGraph**, grounded policy with **RAG**, remembered tickets in **SQL**
- You **versioned** prompts, **traced** runs, **gated** releases with a golden paper
- You showed a **Streamlit** window and a **cost** sticky
- You know ops: cache retrieve, not outcomes

**Support hours after this session** are for remaining golden cards, a clearer screen, or wiring stretch A/B/C — **not** for inventing NEFT. Module evaluation and the offline exam will ask you to **explain** gates and traces, not to recite library names.

**Common doubt:** “Can we change product the night before submit?”  
No. A new story with no golden paper is a fail. Polish PayDesk.

### Activity — Reviewer First Line

Write the first sentence you want a reviewer to read. If it starts with a framework name, rewrite until it starts with the **job**.

---

## Git Hygiene, Requirements, and a Recording

A reviewer who cannot install cannot eval. Pin what you actually imported.

**`requirements.txt` (minimum story):**

```text
langgraph
streamlit
chromadb
sentence-transformers
python-dotenv
```

`sqlite3` is already in Python. **Chroma + all-MiniLM-L6-v2** is the RAG stack from Module 3. Do not add FastAPI, Pydantic, or SQLAlchemy.

**`.gitignore` must include:** `.env`, `.venv/`, `data/paydesk.db`, `.chroma/`, `__pycache__/`, `.streamlit/secrets.toml` if you used it.

**Recording (only if required):**

- Same two bills as the live script
- Camera or screen shows the **hard-rule caption**
- HIGH is in the tape — a CLEAN-only video is incomplete evidence
- No zoom on a `.env` file

If you cannot record audio, the JSONL sample plus golden `pass` printout still counts as evidence for a file submission. Follow whatever your programme listed.

**`eval/golden.json` shape** so a stranger can extend it:

```json
[
  {"id": "G01", "status": "ready_to_pay", "gate": "none"},
  {"id": "G02", "status": "needs_human", "gate": "amount_gate"},
  {"id": "G03", "status": "needs_human", "gate": "gst_mismatch"}
]
```

Keep the **raw_text** next to each id in the runner, not only in your head.

---

## Stretch B and C a Little More Clearly

**Checkpoint + stamp (B)** is the human-in-the-loop pattern you practised when graphs had to **resume**. HIGH should persist state, show `needs_human` in Streamlit, and only then expose a **Stamp as AP lead** button that writes a resume payload. The button is a **person**. Putting `stamped=True` inside `route_node` is cheating.

**GST cache (C)** keys on the GSTIN string. First call hits SQLite; second call with the same GSTIN may hit memory. If Nilgiri’s ₹90,000 bill is cached as ready because Kaveri’s ₹18,600 was ready, you mixed two tickets. Cache **lookup results**, not **ticket outcomes**.

After any stretch, re-run G01–G03. If G02 flips to ready, delete the stretch.

### Activity — Choose in One Line

Write “Stretch: A / B / C / none — because G01–G03 are pass/fail.” Circle one. If you circle two, you are starting a new product.

---

## Exam Defence: Questions You Should Answer Aloud

Support hours and the offline exam will not ask you to recite import paths. They will ask **why**.

| Question | Strong answer |
|---|---|
| Why not NEFT in the agent? | Harm type is money; recommendation vs cashier |
| Why LangGraph, not one mega-prompt? | Stations you can trace; gates in Python |
| Why a handbook in Chroma if gates are Python? | Retrieved lines are evidence and citations, not a waiver |
| Why golden eval? | Prompt edits regress; G02/G03 must stay red |
| Why fail closed on empty Chroma? | Guessing policy is how GST gets skipped |
| Why not cache ready_to_pay? | Next bill from the same vendor can be HIGH |

Practise each answer in two sentences. If you need a third sentence for a library name, you are drifting.

**Module wrap in one breath:** *We built an AP desk that files faster without skipping GST or high-value stamps, proved it with a golden paper and traces, showed a window, and refused a bank.*

---

## Seed Script and .gitignore (Copyable)

Reviewers fail when `paydesk.db` is missing and there is no command to build it.

```python
# scripts/seed.py — vendors, POs, not 99INVALID
import sqlite3  # file db
from pathlib import Path  # folders


Path("data").mkdir(exist_ok=True)  # strong-room folder
conn = sqlite3.connect("data/paydesk.db")  # create if needed
conn.execute("CREATE TABLE IF NOT EXISTS vendors (gstin TEXT PRIMARY KEY, vendor TEXT)")  # register
conn.execute("CREATE TABLE IF NOT EXISTS purchase_orders (po_number TEXT PRIMARY KEY, vendor TEXT)")  # PO book
conn.execute("INSERT OR REPLACE INTO vendors VALUES ('29AAAAA0000A1Z5', 'Kaveri')")  # dummy GSTIN
conn.execute("INSERT OR REPLACE INTO vendors VALUES ('29BBBBB0000B1Z3', 'Nilgiri')")  # dummy GSTIN
conn.execute("INSERT OR REPLACE INTO purchase_orders VALUES ('PO-7781', 'Kaveri')")  # seed PO
conn.execute("INSERT OR REPLACE INTO purchase_orders VALUES ('PO-8802', 'Nilgiri')")  # seed PO
conn.commit()  # persist
conn.close()  # release
from app.memory import seed_policy  # Chroma RAG
seed_policy()  # index data/policy.md
print("seeded sqlite and chroma")  # reviewer sees success
```

**How the code works**

- `INSERT OR REPLACE` makes the command safe to re-run
- `99INVALID` is **absent**, so G03 can fire
- README should say `python scripts/seed.py` before eval — that command must fill **both** sqlite3 **and** Chroma

**`.gitignore`:**

```text
.venv/
.env
__pycache__/
data/paydesk.db
.chroma/
logs/*.jsonl
!logs/sample_paydesk.jsonl
.streamlit/secrets.toml
```

The `!` line keeps one **sample** log in git so evidence exists without leaking a whole class run.

**Public GitHub warning:** dummy GSTINs are fine. Real vendor masters from an internship are not. If the repo is public, double-check `prompts/` for pasted invoices with phone numbers.

---

## Support Hours Versus This Session

This session **submits**. Later support meetings are not a second capstone product.

**Use support hours for:** G04 injection, duplicate tickets, tool-down fail-closed, a stamp button, Groq messy extract, clearer Streamlit copy.

**Do not use support hours for:** renaming the company the night before eval, adding UPI, scraping GST, training a new model.

If core G01–G03 are red on submit day, support hours start with **fix the gate**, not with Streamlit themes.

---

## Copy-Paste Checklist (Markdown)

Put this in `SUBMISSION.md` and tick it.

```markdown
# PayDesk submission

- [ ] One-sentence job in README
- [ ] No NEFT / no pay_vendor file
- [ ] python scripts/seed.py documented
- [ ] python eval/run_golden.py → G01 G02 G03 pass
- [ ] streamlit run app_ui.py uses app.graph
- [ ] prompts/extract_v1.txt present
- [ ] logs/sample_paydesk.jsonl committed (anonymised)
- [ ] docs/cost_note.md has a rate date
- [ ] docs/retro.md has Never: payout
- [ ] .env not in git; .env.example is
- [ ] Stretch is none or exactly one of A/B/C
- [ ] Partner ran G02 from README
```

If any box is empty, do not invent a new feature to feel productive. Tick the box.

**FAQ for the reviewer (optional README section):**

- **Why labelled extract?** Golden paper must be stable in class. Groq extract is stretch A, not the core exam.
- **Why dummy GSTIN?** We do not publish a real firm’s number. Format is for labs only.
- **Why no second HTTP hatch?** Core path is Streamlit on the graph. Do not add a new API framework for submit.
- **Why JSONL not Grafana?** Course evidence is traces + golden rubric, not a monitoring suite.

### Activity — Tick Without Mercy

Read your `SUBMISSION.md` as if you dislike the project. Untick anything you cannot prove in one command.

---

## Key Takeaways

- Submission is a **replay kit**: graph, prompts, golden paper, sample traces, cost and retro notes.
- The README must run **G01–G03** and state **no NEFT** in the opening lines.
- Stretch is **one** door (hatch, stamp-resume, or GST cache) and only after the core is green.
- Cross-team review is the real integration test. **Upcoming** support hours extend PayDesk — they do not reopen the bank.

Pack the tray. Then stop adding logos.

If the README cannot seed and sit G02, the zip is not a product yet. Stretch will not hide that. The handover is the capstone as much as the graph.

**Before you zip:** seed command works on a clean folder, golden prints three passes, UI import matches, `.env` absent from `git status`, partner ticked G02, stretch is one or none.

**Last connecting thought:** the parcel desk taught you to ship a hatch. PayDesk taught you to **refuse** a dangerous hatch. That refusal is the capstone skill as much as LangGraph.

If a reviewer asks “could this scale to 40 stores?” answer with gates, eval, and traces — not with a hosting logo.

**Zip tree (target):**

```text
nimbus_paydesk/
  README.md
  SUBMISSION.md
  requirements.txt
  .env.example
  app/
  eval/
  prompts/extract_v1.txt
  data/policy.md
  scripts/seed.py
  docs/cost_note.md
  docs/retro.md
  logs/sample_paydesk.jsonl
  app_ui.py
```

If `pay_vendor.py` appears anywhere in that tree, delete it before you zip.

A stranger should need **three commands** after clone: create venv and install, seed, eval. UI is the fourth. Anything else belongs in stretch or support hours.

If eval needs a secret key for G01–G03, the lab path is not actually labelled — fix that before you claim “optional Groq.”

**Last zip check:** `git status` shows no `.env`; `python eval/run_golden.py` prints three passes on a clean venv; partner ticked G02 without you in the call.

If any of those three fail, do not start stretch A. Fix the replay kit. The exam will ask why the gate exists, not whether Groq was wrapped in a new framework.

Support hours can add G04 injection and a stamp button. They cannot add NEFT “because the reviewer asked for a complete AP product.” Completeness here means **stopped money leaks**, not more pipes.

You are done when a stranger can replay G02 from the README and the vault is still locked.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Submission checklist | Artifact | Code, prompts, eval, traces, cost, retro |
| README | Doc | Setup, env, eval commands, hard rule |
| `.env.example` | File | Empty key; safe to commit |
| Stretch A | Groq | Messy extract with `extract_v1.txt` + JSON parse |
| Stretch B | LangGraph | Checkpoint; human stamp to resume |
| Stretch C | Cache | GST lookup only |
| Cross-team review | Ritual | Partner + README, no author hints |
| `requirements.txt` | File | Pinned enough to install |
| Sample JSONL | Evidence | Anonymised, committed |
| Support hours | After | Remaining cases and UI — still no payout |
| `scripts/seed.py` | Command | Kaveri + Nilgiri; never 99INVALID |
| `SUBMISSION.md` | Checklist | Tick only what a command can prove |
| `.gitignore` bang rule | Git | Keep `sample_paydesk.jsonl` only |
| Dummy GSTIN | Lab data | `29AAAAA0000A1Z5` / `29BBBBB0000B1Z3` |
| Eval gate | Habit | Prompt change → re-run G01–G03 |
| Human stamp | Stretch B | Resume payload; graph cannot self-stamp |
| Public repo | Risk | No internship vendor masters |

