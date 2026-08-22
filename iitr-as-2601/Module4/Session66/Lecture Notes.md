# Capstone Project Phase — Polish, Demo & Submit

## Introduction

In the **previous** session you froze **Nimbus PayDesk**, drew the one-page map, and ran a **LangGraph** core: extract → policy → route. **G01 CLEAN** reached `ready_to_pay`. **G02 HIGH** and **G03 BADGST** stopped with named gates. Traces landed in JSONL.

**First move today:** re-run `python eval/run_golden.py` before any Streamlit. If G02 is not `amount_gate`, you are still in the build. Do not polish a graph that pays HIGH.

A passing graph in the terminal is still a **back office**. Stakeholders will not grep logs to “feel” the desk. A good demo still fails if a reviewer cannot run it **without you in the room**. This meeting does both: polish the **window**, check **token cost**, run a **short live demo**, write a honest **retro**, then pack the **replay kit** and survive a **partner README run**.

**What you will learn:**

- Improve **UI** from peer feedback (Streamlit on the same graph)
- Verify **token/cost** estimates for a demo path and write assumptions
- Deliver a short **live demo** with traces or logs as evidence
- **Retrospect** what more time would improve — without SLI/SLO theatre
- Complete a **submission checklist** and a **README** a stranger can follow
- Add **one stretch** only if G01–G03 still pass
- **Submit** and review a partner desk from their README only

![Faculty at a clean PayDesk Streamlit counter versus a teammate scrolling a terminal dump of JSON traces](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session63/session63-01-counter-vs-terminal.png)

---

## Why the Counter Matters After the Graph

You already know **Streamlit** from the parcel-desk window. PayDesk reuses the habit, not the FAQ copy.

- **Official Definition:** **UX polish** here means a stakeholder can paste a bill, read a status, and optionally open proof — without installing extra mental load.
- **In Simple Words:** A glass counter on the same clerks.
- **Real-Life Example:** IRCTC shows PNR status on one screen. It does not email you a Python traceback.

**Need:** If Streamlit calls a different `decide()` than `eval/run_golden.py`, you will demo a lie. Wire the app to **`graph.invoke`**.

**Peer feedback you will actually hear:**

| Complaint | Polish |
|---|---|
| “Where do I type?” | One text area, one **Run desk** button |
| “Is this paid?” | Status chip: ready vs needs human — never “paid” |
| “Why did HIGH stop?” | Expander: gate name, handbook hits, node **trace** |
| “Can I stamp here?” | Optional checkbox later; **not** an auto-approve |

**Common doubt:** “Can we skip Streamlit and demo the terminal?”  
Only if your reviewer is an engineer who asked for a CLI. Faculty and finance partners need the counter.

### Activity — Ban One Word

List two words that must **not** appear on the success banner. **Sample:** *Paid*, *NEFT sent*, *Transferred*.

---

## Streamlit Window on the Same Graph

Keep the page calm: input, outcome, proof. You practised this layout on the parcel desk. Swap the story to invoices.

- **Official Definition:** A **trace panel** is a foldable view of steps, tools, and sources for one run — beginner-appropriate, not a full APM console.
- **In Simple Words:** Open the file jacket if someone asks “how?”
- **Real-Life Example:** Courier tracking: *picked up → hub → out for delivery* — not the warehouse CCTV.

![PayDesk Streamlit layout with bill box, status chip, handbook quotes, and a folded trace expander](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session63/session63-02-streamlit-layout.png)

```python
# app_ui.py — stakeholder counter; same graph as eval
import streamlit as st  # browser UI from Python
from app.graph import graph  # do not import a second brain
from app.log import write_trace  # same diary as golden eval


st.set_page_config(page_title="Nimbus PayDesk", layout="centered")  # calm page
st.title("Nimbus PayDesk")  # product name
st.caption("Recommends ready_to_pay. Never sends NEFT.")  # hard rule on screen

G01 = "Vendor: Kaveri\nGSTIN: 29AAAAA0000A1Z5\nPO: PO-7781\nAmount: 18600"  # same string as golden
G02 = "Vendor: Nilgiri\nGSTIN: 29BBBBB0000B1Z3\nPO: PO-8802\nAmount: 90000"  # same string as golden

c1, c2 = st.columns(2)  # two equal buttons
if c1.button("Load CLEAN sample"):  # demo card 1
    st.session_state["raw"] = G01  # keep text across rerun
if c2.button("Load HIGH sample"):  # demo card 2
    st.session_state["raw"] = G02  # keep text

raw = st.text_area("Paste labelled invoice", height=160, key="raw")  # key binds the Load buttons
run = st.button("Run desk")  # one action

if run and raw.strip():  # avoid empty invoke
    packet = graph.invoke(  # identical door to golden eval
        {
            "ticket_id": "ui-live",  # demo id
            "raw_text": raw,  # bill text
            "trace": [],  # start empty — Chroma is seed_policy(), not pasted here
        }
    )
    write_trace(packet)  # chip and JSONL must match
    status = packet.get("status", "")  # outcome
    gate = packet.get("gate", "")  # reason
    if status == "ready_to_pay":  # clean small bill
        st.success("Recommendation: ready to pay (cashier still signs).")  # not paid
    else:  # any stop
        st.warning("Needs a human. Gate: " + gate)  # named stop
    with st.expander("Proof — sources and trace"):  # optional detail
        st.write("Handbook hits:", packet.get("policy_hits", ""))  # RAG quotes
        st.write("Stations:", " → ".join(packet.get("trace", [])))  # LangGraph order
        st.write("Prompt:", packet.get("prompt_version", ""))  # version
```

**How the code works**

- One button, one `invoke` — no hidden prompt in the UI layer
- Success copy says **recommendation**, so a CFO does not think money moved
- The expander is proof; the main banner stays one sentence
- The UI does **not** paste handbook lines. `policy_node` retrieves from **Chroma** the same way eval does

**Layout habits from peer feedback**

- Put G01 / G02 sample buttons so a nervous demo does not depend on typing
- Show amount in ₹ with the Indian grouping you already used in the packet
- Never show Groq’s full hidden chain-of-thought; stations + gate are enough
- If Streamlit reruns on every keystroke, keep work behind the **button**

**CLI versus counter:** polish the counter **after** CLI G01–G03 pass. The terminal is a debug skin. The CFO story needs the glass.

### Activity — Same Door Test

Run G02 in the UI. Confirm the warning shows `amount_gate`. Then run `eval/run_golden.py`. If UI says stop and eval says ready, you have two products. **Fix:** one `graph` import.

---

## Sample Buttons, Privacy, and a Shared Laptop

The Load CLEAN / Load HIGH buttons in `app_ui.py` must use `key="raw"` on the text area. Setting `st.session_state["raw"]` without that key **does not** fill the box — the demo then depends on nervous typing again.

**How the wiring works**

- Samples are the **same strings** as the golden file — do not rewrite amounts by memory
- `key="raw"` is the binder between the button and the box
- You still press **Run desk** so a load is not an accidental invoke

**Privacy on the projector:** no real internship GSTIN; no open `.env`; mask anything that looks like PAN. Prefer **local** `streamlit run app_ui.py`. A public link without a rate limit will burn the classroom Groq key.

After `graph.invoke`, call the same `write_trace` helper you used in the build meeting. If the UI shows `amount_gate` but the last JSONL line says `none`, you invoked twice or wrote the log before policy ran.

### Activity — Match the Line

Run G03. Copy the last JSONL object. Tick: does `gate` equal `gst_mismatch` on both the warning chip and the file? If not, find which invoke you forgot.

---

## Demo-Path Cost: Count Before You Perform

You already measured tokens on the parcel hatch. PayDesk must not “look cheap” by skipping Groq on CLEAN and then surprising the bill on a messy extract.

- **Official Definition:** A **demo-path cost estimate** is tokens (and a classroom INR guess) for the exact bills you will show, with written assumptions.
- **In Simple Words:** A receipt for the two bills in the script — not a production budget.
- **Real-Life Example:** A wedding card lists catering for 80 plates, not “food in general.”

![Two PayDesk receipts: CLEAN labelled parse with near-zero Groq tokens versus a messy-prose Groq extract that still cannot skip the amount gate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session63/session63-03-demo-cost-receipts.png)

**Assumptions to write in `docs/cost_note.md`:**

| Assumption | Typical lab value | Why it matters |
|---|---|---|
| Extract path | Lab labels for G01–G03 | Token cost near **zero** for the live exam |
| Groq extract | One `extract_v1` call on a messy bill | Tokens ≈ prompt + invoice + JSON slip |
| RAG | Tiny `policy.md` in **Chroma** | Embed once at seed; retrieve is local |
| Cache | May cache **handbook retrieve** | Must **not** cache HIGH → ready |
| Classroom rate | Use the Groq rate you logged in ops | Write the date of the rate |

**Unsafe cache:** photocopying `ready_to_pay` because “this vendor was clean yesterday.” Amount and GST can change on the next bill.

```markdown
# Demo-path cost (classroom)

Date of Groq rate used: YYYY-MM-DD
INR per 1K tokens (assumed): ...

## Bills in the live script
- G01 CLEAN: labelled extract, Groq calls = 0, tokens = 0
- G02 HIGH: labelled extract, Groq calls = 0, tokens = 0
- Optional messy bill: 1 × extract_v1, tokens ≈ ... (from JSONL)

## Cache
- Handbook retrieve may be cached.
- ready_to_pay must not be cached.

## What this is not
- Not a monthly production forecast.
- Not an SLI.
```

If both live bills are labelled, **say that**. A zero-token demo is honest. A zero-token demo that secretly called Groq is not.

### Activity — Write Three Assumptions

In one sticky note: (1) which bills you will click, (2) whether Groq runs, (3) the token rate date. That sticky **is** the cost check.

---

## Live Demo Script (Evidence, Not Theatre)

A demo is a **story with proof**. Aim for a short run a CFO can interrupt.

- **Official Definition:** A **demo script** is a timed sequence of clicks and spoken lines, with a fallback if a tool is down.
- **In Simple Words:** Rehearsed seva-counter walkthrough.
- **Real-Life Example:** Passport office mock: one clean file, one file that must stop — then show the register.

![Instructor walking CLEAN then HIGH on the PayDesk counter while a JSONL diary and expander show the same gates](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session63/session63-04-demo-with-evidence.png)

**Suggested spoken arc (keep it short):**

1. **Job** — “Nine-day AP wait. We recommend. We never NEFT.”
2. **CLEAN** — paste G01, Run, green recommendation, open expander: `extract → policy → route`
3. **HIGH** — paste G02, amber `amount_gate`, say “Python constant, not a vibe”
4. **Proof** — open `logs/paydesk.jsonl` or the expander; same `gate` as golden eval
5. **Stop** — “With more time: Groq messy extract, or a human stamp resume. We would not add a bank.”

**Fallback if Streamlit dies:** run `eval/run_golden.py` and read three lines. A working exam is better than a frozen browser.

**Open:** “Nimbus PayDesk is an accounts desk for a 40-store chain. Vendors wait about nine days. We file bills and recommend. We never send NEFT.”

**CLEAN:** “This is Kaveri, ₹18,600, known GSTIN, known PO. The graph should say ready to pay — that means the cashier may pay, not that we paid.”

**HIGH:** “This is ₹90,000. Policy must stop on `amount_gate` even if the bill text is polite. The constant lives in Python.”

**Do not:** invent a payout animation; skip HIGH because “it looks negative”; edit JSONL by hand; load HIGH then edit the amount down to ₹18,600 “to be safe.”

**G03 on stage:** optional. Two bills already prove pass vs stop. If you are shaky, skip G03 live and show the golden printout — do not fumble `99INVALID` and accidentally seed it.

### Activity — Job Line Aloud

Say the job sentence and the hard rule without notes. If you mention Streamlit before GST, restart the sentence.

---

## Troubleshooting During a Live Demo

Things break. Have a card, not a panic.

| Symptom | Likely cause | What you say |
|---|---|---|
| Import error on Streamlit | Wrong folder / venv | “I will run from the repo root.” |
| CLEAN needs_human / empty_policy | Chroma not seeded | “The binder is empty; fail closed is correct. Seeding now.” |
| HIGH shows ready | UI not using graph, or amount parsed as 0 | “That is a defect; we stop the demo and show golden CLI.” |
| Expander empty | Forgot to return `trace` from nodes | “Stations did not stamp; we will not pretend.” |
| Groq 429 | Shared key | “Lab path does not need Groq; labelled bills still prove gates.” |

**Need:** Stopping the demo to show a honest fail-closed is **better** than commenting out policy. If you change Streamlit copy, you do **not** need to re-golden. If you change `AMOUNT_GATE` or extract prompt, you **do**.

### Activity — Pick the Honest Line

HIGH comes back ready. Do you (a) laugh and load CLEAN twice, or (b) say “this is a miss — here is the CLI gate”? **Answer:** (b).

---

## Retrospective Without Fake Metrics

A retro is a **learning log**, not a dashboard of made-up uptime.

- **Official Definition:** A **retrospective** lists what worked, what hurt, and what you would do with more time — without claiming production SLIs/SLOs you did not measure.
- **In Simple Words:** Honest “if we had another week.”
- **Real-Life Example:** After a college fest, you write “queue signs were late,” not “we achieved 99.9% visitor happiness.”

**Write four bullets in `docs/retro.md`:**

- **Keep:** Python amount/GST gates; golden G01–G03 on the same graph
- **Change:** labelled extract is a lab crutch — Groq extract needs its own golden messy bill
- **More time:** remaining cards (duplicate, tool-down), Streamlit stamp button wired to a **checkpoint**, Groq extract on one messy bill
- **Never:** payout SDK, caching `ready_to_pay`, deleting fail-closed to look green

**Common doubt:** “Should we add a Grafana board?”  
No. Traces + golden paper + cost sticky are the evidence this course asked for.

### Activity — Four-Bullet Retro

Fill keep / change / more time / never on paper before you type `docs/retro.md`. If “more time” includes NEFT, cross it out.

---

## Submission Checklist: What “Done” Means

Reviewers are tired. They follow a list. If your zip is a mystery tour, they will score the mystery.

- **Official Definition:** A **submission checklist** is the minimum set of artifacts that prove the product runs, is bounded, and was evaluated.
- **In Simple Words:** Everything a stranger needs to replay G01–G03.
- **Real-Life Example:** A passport file: form, photo, old booklet — not a bag of unmarked photocopies.

![Submission tray with code folder, prompt file, golden clipboard, sample JSONL, and a short demo recording card](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session64/session64-01-submission-tray.png)

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

**`requirements.txt` (minimum story):** `langgraph`, `streamlit`, `chromadb`, `sentence-transformers`, `python-dotenv`. `sqlite3` is already in Python. Do not add FastAPI, Pydantic, or SQLAlchemy.

**`.gitignore` must include:** `.env`, `.venv/`, `data/paydesk.db`, `.chroma/`, `__pycache__/`, `.streamlit/secrets.toml` if you used it. Keep one sample log with `!logs/sample_paydesk.jsonl`.

You now have a seed command. The scored swap is **Cross-team Review** later in this meeting — after stretch-or-skip. Do not swap yet.

---

## Seed Script (Copyable)

Reviewers fail when `paydesk.db` is missing and there is no command to build it.

```python
# scripts/seed.py — vendors, POs, not 99INVALID
import sqlite3  # file db
from pathlib import Path  # folders


Path("data").mkdir(exist_ok=True)  # strong-room folder
conn = sqlite3.connect("data/paydesk.db")  # create if needed
conn.execute("CREATE TABLE IF NOT EXISTS vendors (gstin TEXT PRIMARY KEY, vendor TEXT)")  # register
conn.execute("CREATE TABLE IF NOT EXISTS purchase_orders (po_number PRIMARY KEY, vendor TEXT)")  # PO book
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

A stranger should need **three commands** after clone: create venv and install, seed, eval. UI is the fourth.

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
import json  # structured output
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
    parsed = json.loads(text)  # parse or fail closed
    parsed["prompt_version"] = "extract_v1"  # eval gate field
    parsed["confidence"] = float(parsed.get("confidence", 0.5))  # number
    return parsed  # same keys as parse_labelled
```

**How the code works**

- Uses **Groq + JSON parse** you already practised — not a new API framework
- If JSON is malformed, extract should lower confidence and let policy demand a type-check
- After this stretch, re-run G01–G03 on **labelled** bills. They must still pass. Then try one messy bill; HIGH must still hit `AMOUNT_GATE`

**Checkpoint stretch (B):** persist graph state when `amount_gate` fires; resume only after a **human** function writes `stamped=True`. The graph must not set that flag itself.

**Cache stretch (C):** key = GSTIN string; value = `KNOWN`/`UNKNOWN`; TTL short. If you cache `ready_to_pay` keyed by vendor name, you have rebuilt the unsafe ops mistake on purpose.

**Forbidden stretches:** payout, live GST scraping, “auto-approve festival week,” deleting G03 because it is awkward.

If G01–G03 are not all **pass**, **do not stretch**. Fix the core. Write in the retro that stretch was skipped on purpose. Under this meeting’s clock, **none** is the default. Stretch is only if G01–G03 are already green **and** the README already has a seed command.

### Activity — Choose in One Line

Write “Stretch: A / B / C / none — because G01–G03 are pass/fail.” Circle one. If you circle two, you are starting a new product.

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

**Support hours after this meeting** are for remaining golden cards, a clearer screen, or wiring stretch A/B/C — **not** for inventing NEFT. Module evaluation and the offline exam will ask you to **explain** gates and traces, not to recite library names.

| Question | Strong answer |
|---|---|
| Why not NEFT in the agent? | Harm type is money; recommendation vs cashier |
| Why LangGraph, not one mega-prompt? | Stations you can trace; gates in Python |
| Why a handbook in Chroma if gates are Python? | Retrieved lines are evidence, not a waiver |
| Why fail closed on empty Chroma? | Guessing policy is how GST gets skipped |
| Why not cache ready_to_pay? | Next bill from the same vendor can be HIGH |

**Module wrap in one breath:** *We built an AP desk that files faster without skipping GST or high-value stamps, proved it with a golden paper and traces, showed a window, and refused a bank.*

**Where this course shows up on the desk** (so an exam is not a library quiz):

| You already learned | Point at this on PayDesk |
|---|---|
| Python, files, JSON, git, secrets (Module 1) | Scripts, `InvoicePacket`, `.env.example`, `.gitignore` |
| SQL thinking (Module 1) | Vendor and PO tables in `sqlite3` — not a Pandas workbook |
| ML eval habits (Module 2) | Frozen golden paper; do not leak handbook lines into the packet |
| RAG + embeddings (Module 3) | `seed_policy()` → Chroma → `policy_hits` as quotes |
| Tools + structured output (Module 3) | GST/PO phones in Python; Groq JSON is stretch, not the live exam |
| Guardrails (Module 4) | Bill text cannot skip `AMOUNT_GATE`; no pay tool |
| LangGraph + traces + golden eval (Module 4) | extract → policy → route; JSONL; G01–G03 |
| Streamlit + cost + cache rule (Module 4) | Same `graph.invoke`; cost sticky; never cache `ready_to_pay` |

Not on this desk (on purpose): Ollama, a FastAPI second hatch, linear regression, clustering. Support hours do not add those to look “complete.”

### Activity — Reviewer First Line

Write the first sentence you want a reviewer to read. If it starts with a framework name, rewrite until it starts with the **job**.

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

### Activity — Tick Without Mercy

Read your `SUBMISSION.md` as if you dislike the project. Untick anything you cannot prove in one command.

---

## Key Takeaways

- Streamlit is a **window on the same graph** the golden set already calls — not a second PayDesk.
- A **demo-path receipt** names lab vs Groq tokens and forbids cache from skipping gates.
- The live story is **one bill through, one bill stopped**, with expander or JSONL as proof.
- The retro is a short honest list. Submission is a **replay kit**: graph, prompts, golden paper, sample traces, cost and retro notes.
- The README must run **G01–G03** and state **no NEFT** in the opening lines.
- Stretch is **one** door (hatch, stamp-resume, or GST cache) and only after the core is green.
- Cross-team review is the real integration test. **Upcoming** support hours extend PayDesk — they do not reopen the bank.

If the live HIGH click and the golden HIGH row disagree, stop presenting and fix the import. A beautiful wrong window is the failure mode this meeting exists to prevent.

**Before you zip:** CLI golden pass, UI same import, two sample buttons, caption with no-NEFT, cost note dated, retro has a Never line, seed command works on a clean folder, `.env` absent from `git status`, partner ticked G02, stretch is one or none.

You are done when a stranger can replay G02 from the README and the vault is still locked.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Streamlit | UI | `st.text_area`, `st.button`, expander |
| `graph.invoke` | Door | Shared with golden eval |
| Status chip | UX | ready vs needs human — never “paid” |
| Trace panel | UX | Stations + handbook hits |
| Demo-path cost | Note | Tokens for scripted bills + assumptions |
| Cache rule | Ops | Retrieve yes; `ready_to_pay` no |
| JSONL | Evidence | One run, one line |
| Retro | Doc | Keep / change / more time / never |
| SLI / SLO | Out of scope | Do not invent uptime theatre |
| `streamlit run app_ui.py` | Command | Local counter |
| `st.session_state` | API | Keep sample text across reruns |
| Submission checklist | Artifact | Code, prompts, eval, traces, cost, retro |
| README | Doc | Setup, env, eval commands, hard rule |
| `.env.example` | File | Empty key; safe to commit |
| Stretch A / B / C | Optional | Groq extract / checkpoint stamp / GST cache |
| Cross-team review | Ritual | Partner + README, no author hints |
| `scripts/seed.py` | Command | Kaveri + Nilgiri; never 99INVALID |
| `SUBMISSION.md` | Checklist | Tick only what a command can prove |
| Fail closed | Habit | Empty binder → human, even in a demo |
