# Full-Cycle Agent Design

## Introduction

In the **previous** session you drew a **six-box canvas** for **Nimbus Retail**: roles, JSON handoffs, tools, human gates, risks, and metrics. That canvas is a blueprint. It is not yet a product you can demo.

This session freezes the capstone as **Nimbus PayDesk**. You will lock the **problem**, **scope**, **tools**, **memory architecture**, and **success criteria** so the next session can draw architecture without arguing about the business.

**What you will learn:**

- Define the business problem and scope for the capstone (Nimbus PayDesk: cut 9-day AP wait; no live NEFT)
- Create a plan for **multi-agent** roles, non-goals, and handoff contracts (Intake, Extractor, Policy, Router, Reporter; InvoicePacket)
- Specify **tools** and data sources the agents may call (GST check, PO lookup, policy RAG, logging, human stamp)
- Design **memory** architecture for short-term, semantic, and episodic stores (ticket packet, Chroma handbook, SQLite log)
- Write **success criteria** and an evaluation pack (CLEAN, HIGH, BADGST; missed-gate rate = 0)

![From a six-box design canvas to a named Nimbus PayDesk product on an Indian retail accounts counter](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session59/session59-01-canvas-to-paydesk.png)

---

## Why Full-Cycle Design Comes Before a Repo

A full-cycle design answers *what the agent observes, remembers, decides, and is not allowed to do* — before folders exist.

- **Official Definition:** **Full-cycle agent design** is the contract that names the problem, the observe–think–act loop, the tools, the memory stores, and the tests that count as done.
- **In Simple Words:** Before you hire clerks, you write the job cards, the registers they may open, and the exam they must pass.
- **Real-Life Example:** A **passport seva** counter does not start by buying printers. It first writes which documents are accepted, which window stamps, and what “done” means on the token slip.

**Need:** Jumping to LangChain or CrewAI with an unfinished contract produces a chatbot that *talks about* invoices. PayDesk must *move a ticket* with an audit line.

**Common doubt:** “Did we not already design this?” You designed the *desk*. Today you freeze the *capstone product*: what four live sessions will actually ship.

---

## Problem Identification: One Sentence Two Audiences Can Share

Write the pain so money people and builders nod at the same line.

**Locked problem statement:**

> Nimbus Retail’s Accounts Payable team takes **9 days** to clear a vendor invoice, and about **30%** of bills need a human because GST, PO, or amount looks wrong. **Nimbus PayDesk** must cut that wait without paying a wrong **GSTIN** or skipping a high-value stamp.

| Audience | What they hear in that sentence |
|---|---|
| **CFO** | Faster vendor peace; no surprise GST notice |
| **Engineer** | Cycle-time metric; missed-gate rate must stay **0** |
| **AP clerk** | Dirty bills still stop; clean small bills should not wait in the same pile |

- **Official Definition:** **Problem identification** is naming the user, the current failure, the harm if nothing changes, and the outcome that would count as better.
- **In Simple Words:** Who is stuck, how badly, and what “unstuck” looks like.
- **Real-Life Example:** “Festival week, kirana stock not arriving because bills sit unsigned” is a problem. “Let us add AI” is not.

**Harm type for this capstone:** **money**. Not hiring fairness, not brand claims. Every later choice must protect rupees.

### Activity — Rewrite in One Line

A teammate writes: “We will use CrewAI to process PDFs.” Rewrite it as a **problem**, not a tool.

**Suggested answer:** Vendors wait nine days while GST and high-value bills mix with clean ones in one mailbox.

---

## Scope Definition: What Four Sessions Will Ship

Scope is how you stop the prototype from becoming a bank.

- **Official Definition:** **Scope** is the boundary of work the system is allowed to complete. Outside scope is a **handoff**, not “the model will figure it out.”
- **In Simple Words:** The desk prepares the file. The cashier still signs the cheque.
- **Real-Life Example:** A pathology lab *reports* values. The doctor *prescribes*. Mixing those jobs is unsafe.

| In scope for PayDesk prototype | Out of scope (on purpose) |
|---|---|
| Simulated inbox (text invoices + JSON) | Live Gmail / scanned Hindi-English PDFs |
| Extract vendor, GSTIN, amount, PO, date | Invent a missing PO or “fix” GST |
| Dummy GST registry + format check | Live GST portal |
| SQLite vendor and PO register (ERP stand-in) | Tally / real ERP write |
| Policy RAG on a short AP handbook | Full company wiki |
| Human stamp API for gated tickets | Actual **NEFT** / UPI payout |
| Ticket log + simple report counts | CFO dashboard product |
| n8n **webhook** into ingest (optional later) | WhatsApp Business production |

**Why out matters:** An agent that *moves money* without a named human fails the governance you already learned. The demo may show a **simulated** “ready to pay” status. It must never pretend the bank was called.

**Prototype honesty:** Extract in class uses **clear text invoices**, not OCR. Production would add a type-check path for stamps covering numbers. That limitation stays on the one-pager.

---

## Agents, Non-Goals, and the Observe–Think–Act Loop

Roles fail when two agents share a job, or one agent wears every hat.

- **Official Definition:** An **agent role** is a specialist with a **goal**, a **task**, allowed **tools**, and a **non-goal**.
- **In Simple Words:** The extractor reads the bill. The policy agent does not rewrite the bill.
- **Real-Life Example:** At a **bank branch**, cashier, KYC desk, and manager are different people on purpose.

**PayDesk loop (full cycle):**

1. **Observe** — Intake sees a new invoice packet
2. **Think** — Extractor structures fields; Policy compares rules and registers
3. **Act** — Router queues “ready” or stops a human; nothing pays
4. **Remember** — Ticket row and policy chunks are stored for the next question

| Agent | Goal | Main task | Must not |
|---|---|---|---|
| **Intake** | One ticket per bill | Assign `INV-id`, store raw text | Judge GST or amount |
| **Extractor** | Structured fields | Vendor, GSTIN, amount, PO, date, confidence | Change policy rules |
| **Policy checker** | Compare fields to truth | GST tool, PO lookup, policy RAG | Invent a missing PO |
| **Exception router** | Send dirty cases to a named human | Reason codes + evidence pack | Quietly “fix” GST |
| **Reporter** | Counts for leadership | Read logs only | Approve invoices |

**Why five names, four live specialists?** Reporter is a **batch read** on logs, not a chatty extra agent on the hot path. The prototype implements Intake, Extractor, Policy, Router, plus a report **endpoint**.

**Common mistake:** One “Invoice GPT” that extracts, judges, and emails the vendor. When GST is wrong, you cannot tell whether the PDF was misread or the rule was skipped.

![Specialist clerks passing a labelled invoice packet through intake, extract, policy, and a human stamp window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session59/session59-02-roles-and-cycle.png)

---

## The Handoff Contract You Will Code Against

A role without a schema is a hallway conversation.

- **Official Definition:** A **handoff** is the moment one agent’s **output** becomes the next agent’s **input**, using an agreed **schema**.
- **In Simple Words:** The next clerk should not re-read the whole bill if the form is already filled — unless confidence is low.
- **Real-Life Example:** A lab sends patient id, test, and value — not a voice note — to the doctor.

**Minimum packet (locked):**

```json
{
  "ticket_id": "INV-1042",
  "vendor": "Kaveri Packaging Pvt Ltd",
  "gstin": "29AAAAA0000A1Z5",
  "amount_inr": 18600,
  "po_number": "PO-7781",
  "invoice_date": "2026-08-01",
  "confidence": 0.91,
  "status": "needs_policy",
  "reasons": [],
  "raw_text": "..."
}
```

**Status values you will allow:** `ingested` → `needs_extract` → `needs_policy` | `needs_typecheck` → `ready_to_pay` | `needs_human` → `approved` | `rejected`.

**Why `confidence` exists:** Below **0.80**, skip auto-policy and ask a human to type-check GSTIN from the bill. Guessing a GSTIN is how you pay the wrong vendor.

The same shape in Python (this file is the contract, not the full app):

```python
# packet_contract.py — run: python packet_contract.py
from pydantic import BaseModel, Field  # typed ticket that FastAPI can later accept


class InvoicePacket(BaseModel):  # one bill moving along PayDesk
    ticket_id: str  # unique id from intake, example INV-1042
    vendor: str  # name printed on the bill
    gstin: str  # GST number; dummy format only in this course
    amount_inr: int = Field(ge=0)  # rupees; 0 means not extracted yet; ≥ 1 after extract
    po_number: str  # purchase order claimed on the bill
    invoice_date: str  # ISO date string from the bill
    confidence: float = Field(ge=0, le=1)  # extractor self-score between 0 and 1
    status: str  # current desk status from the allowed list
    reasons: list[str] = []  # why a gate fired; empty on a clean pass
    raw_text: str = ""  # original invoice text; not dumped into Slack alerts


if __name__ == "__main__":  # prove a clean packet validates
    p = InvoicePacket(  # happy-path sample used in later eval cases
        ticket_id="INV-1042",  # intake id
        vendor="Kaveri Packaging Pvt Ltd",  # known vendor
        gstin="29AAAAA0000A1Z5",  # dummy GSTIN, not a real firm
        amount_inr=18600,  # below the 50000 gate
        po_number="PO-7781",  # exists in the seed register
        invoice_date="2026-08-01",  # bill date
        confidence=0.91,  # above 0.80 so no type-check
        status="needs_policy",  # next specialist is Policy
        reasons=[],  # no exceptions yet
        raw_text="Kaveri / PO-7781 / 18600",  # short stand-in for a PDF
    )  # packet ready
    print(p.ticket_id, p.status, p.amount_inr)  # INV-1042 needs_policy 18600
```

**How the code works:**

- `InvoicePacket` is the **handoff schema** you will reuse in FastAPI bodies.
- `Field(ge=0)` allows an ingest stub with amount `0`. After extract, a real bill must be ≥ 1.
- Dummy GSTIN `29AAAAA0000A1Z5` is a **teaching id**, not a live company.

### Activity — Add One Field or Not?

Should the packet include the vendor’s full PAN? Write **yes/no** and one reason.

**Suggested answer:** **No.** Pass a vendor **id**. Full PAN in prompts and Slack is a privacy leak.

---

## Tool Requirements: What PayDesk May Touch

Agents are only as trustworthy as the systems they may call.

- **Official Definition:** A **tool requirement** lists each **source of truth**, who may call it, and whether the call is **read** or **write**.
- **In Simple Words:** A pantry list plus a rule: who may open the fridge, who may throw food away.
- **Real-Life Example:** A hospital EMR is readable by many roles; only a doctor **writes** a prescription.

| Tool | Stands in for | Agent | Read / write | Prototype shape |
|---|---|---|---|---|
| `ingest_invoice` | AP mailbox | Intake | Write ticket | FastAPI POST |
| `extract_fields` | Clerk reading the bill | Extractor | Read raw text | LangChain later |
| `check_gstin` | GST lookup | Policy | Read | Dummy registry + format |
| `lookup_po` | ERP / Tally | Policy | Read | SQLite `purchase_orders` |
| `retrieve_policy` | AP handbook | Policy | Read | Chroma RAG |
| `log_event` | Audit book | All | Append-only write | SQLite `events` |
| `request_stamp` | Exception desk | Router | Write queue | Status `needs_human` |
| `apply_stamp` | AP lead / tax desk | **Human** | Write decision | FastAPI POST |
| `summarise_desk` | Weekly CFO note | Reporter | Read | Counts endpoint |

**Hard rule:** **Bank / NEFT** is not a tool. If the demo needs a pay button, it only flips a label and writes an audit line.

**Fail closed:** If `check_gstin` or `lookup_po` errors, Policy must send the ticket to a human. It must not assume “valid.”

![Tool wall with mailbox, policy binder, vendor register, GST stamp, and a red lock on the bank drawer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session59/session59-03-tools-wall.png)

**n8n later, not today:** A webhook can POST the same ingest body the API already accepts. Do not design a second business flow for automation.

---

## Memory Architecture: Three Stores, Three Jobs

Without a memory map, teams dump the whole PDF into every prompt and call it “context.”

- **Official Definition:** **Memory architecture** is the plan for what is kept **this request**, what is stored **across tickets**, and what is **retrieved by meaning**.
- **In Simple Words:** Whiteboard for this bill, steel almirah for old tickets, binder for policy.
- **Real-Life Example:** A railway TTE has the current coach list (working memory), yesterday’s chart in the office (episodic), and the rule book (semantic). Mixing all three into one WhatsApp chat is how stations get missed.

| Store | Type | Holds | Lives in | Used by |
|---|---|---|---|---|
| **Ticket packet** | Short-term / working | Current fields, status, reasons | Request object + row | Extractor, Policy, Router |
| **AP policy chunks** | Long-term **semantic** | GST, PO, duplicate, amount rules | Chroma | `retrieve_policy` |
| **Ticket + event log** | Long-term **episodic** | Who did what, when | SQLite | Reporter, duplicate check, audit |
| **Gate rules** | **Procedural** | Amount ≥ 50000; confidence < 0.80 | Python constants | Policy, Router |

**What must not be “memory”:**

- The LLM’s pretrained guess about a vendor — **ERP is truth**
- Full PAN or bank account in Chroma — **ids only**
- Slack threads as the only history — **SQLite is the register**

**Duplicate bills:** Before Policy says ready, look up vendor + amount + date in the ticket log. That is episodic memory doing a job RAG cannot do reliably.

```python
# memory_map.py — run: python memory_map.py
POLICY_HITS = ("gst", "po", "duplicate", "amount")  # words that belong in the handbook
LOG_HITS = ("yesterday", "last week", "already paid", "same bill")  # words that need the register


def pick_store(question: str) -> str:  # decide STM vs semantic vs episodic
    q = question.lower()  # normalise for simple matching
    if any(word in q for word in LOG_HITS):  # this is about a past ticket
        return "episodic_sqlite"  # query the ticket log, not Chroma
    if any(word in q for word in POLICY_HITS):  # this is about a rule
        return "semantic_chroma"  # retrieve AP handbook chunks
    return "working_packet"  # default: look at the current ticket fields


if __name__ == "__main__":  # three questions, three stores
    print(pick_store("What is the amount gate?"))  # semantic_chroma
    print(pick_store("Did we already pay this same bill?"))  # episodic_sqlite
    print(pick_store("What GSTIN is on this ticket?"))  # working_packet
```

**How the code works:**

- Policy questions go to **Chroma**. History questions go to **SQLite**. Field questions stay on the **packet**.
- This is a teaching router, not embeddings. Upcoming work will retrieve for real.

### Activity — Pick the Store

“Show me every ticket from Kaveri this month.” Which store? Why not Chroma?

**Suggested answer:** **Episodic SQLite.** That is a list of past events, not a policy paragraph.

![Three memory drawers labelled this ticket, policy binder, and history register behind a PayDesk counter](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session59/session59-04-memory-drawers.png)

---

## Success Criteria: Speed and Safety on Separate Dials

If you only say “the agent should be accurate,” teams hide exceptions to look good.

- **Official Definition:** A **success criterion** is a number you can collect from logs without arguing. **Safety** metrics and **speed** metrics must not be averaged into one vanity score.
- **In Simple Words:** Fast trains and trains that skip red signals are different stories.
- **Real-Life Example:** A local can be *on time* or *safe at every crossing*. You publish both numbers.

**Locked targets for the prototype (demo-scale, same names as production):**

| Criterion | Definition | Prototype target |
|---|---|---|
| **Happy-path pass** | Clean small bill → `ready_to_pay` with empty reasons | **Must** on INV-CLEAN |
| **Amount gate** | ≥ ₹50,000 never auto-ready | **Must** on INV-HIGH |
| **GST gate** | Unknown GSTIN → `needs_human` | **Must** on INV-BADGST |
| **Low confidence** | < 0.80 → type-check, not guess | **Must** on INV-BLUR |
| **Missed-gate rate** | High-amount or GST-fail that skipped stamp | **0** |
| **No payout tool** | No function calls a bank | **0** bank tools |
| **Audit line** | Every status change has an event row | **Must** |
| **Cost cap (lab)** | One ticket uses a small model path | Log tokens if a model runs |

**CFO sentence:** Median cycle time should fall from 9 days toward **same-day ready** for clean bills. **Missed-gate rate stays 0.**

---

## Human Gates Stay Written as Policy

Memory and tools do not replace the stamps you already designed. They *serve* those stamps.

- **Official Definition:** A **human approval gate** is a required stop when a rule fires. Below the threshold, the workflow may continue without a person.
- **In Simple Words:** The manager stamps big or weird bills. Clean small bills should not wait in the same line.
- **Real-Life Example:** UPI lets you pay ₹200 with less friction; a ₹2 lakh transfer asks for extra confirmation.

| Condition | Gate | Owner | Memory/tool that proves it |
|---|---|---|---|
| Amount ≥ **₹50,000** | Must stamp | AP lead | Working packet `amount_inr` |
| GSTIN mismatch or unknown | Must stamp | Tax desk | `check_gstin` + packet |
| Extract confidence < **0.80** | Must type-check | AP clerk | Packet `confidence` |
| Duplicate invoice | Must stamp | AP lead | Episodic SQLite lookup |
| Tool error | Must stamp | AP clerk | Fail-closed, no guess |
| Else PO matches, GST ok, below limit | **No gate** | — | Speed path |

**Need:** If Policy can *override* the amount gate with a fluent sentence, the design is theatre. Gates live in **Python constants**, not only in a prompt.

**Common doubt:** “Can the LLM be the gate?” It can *explain* why a gate fired. It must not *delete* the gate.

### Activity — Keep or Drop the Type-Check?

A teammate says, “Our model is good now; drop the 0.80 rule.” What safety metric breaks first?

**Suggested answer:** Wrong-vendor payments. **Missed-gate rate** on low-confidence GSTIN guesses will leave 0.

---

## What This Course Already Gave PayDesk

You are not starting from a blank notebook. You are assembling skills you already practised.

| Course skill | PayDesk use |
|---|---|
| Prompting and self-reflection | Extractor prompt + “check your GSTIN digits” |
| SQL + Pydantic | Vendor/PO register and `InvoicePacket` |
| Embeddings, Chroma, RAG | AP handbook retrieval |
| APIs, JSON, function calling | Tools and FastAPI bodies |
| LangChain agent + memory + eval | Sequential pipeline and the eight cases |
| CrewAI / AutoGen role split | Specialist agents with non-goals |
| n8n webhooks | Later: mailbox → `POST /ingest` |
| Guardrails, HITL, cost, audit | Gates, no PAN in logs, token log |

**Need:** The capstone is a **product**, not a new subject. If a design needs a skill you never learned (live bank APIs, production OCR), it is out of scope.

---

## Eight-Case Evaluation Pack

Design is unfinished until you can fail on purpose.

- **Official Definition:** An **evaluation pack** is a frozen set of inputs with **expected status** and **expected reasons**, run the same way after every change.
- **In Simple Words:** Eight exam papers the desk must sit, not a live demo you cherry-pick.
- **Real-Life Example:** A driving test has a hill, a signal, and a reverse. Passing only on an empty Sunday road is not a licence.

```json
{
  "cases": [
    {"id": "INV-CLEAN", "amount_inr": 18600, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.91, "expect_status": "ready_to_pay", "expect_reasons": []},
    {"id": "INV-HIGH", "amount_inr": 90000, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.92, "expect_status": "needs_human", "expect_reasons": ["amount_gate"]},
    {"id": "INV-BADGST", "amount_inr": 12000, "gstin": "99INVALID", "po_number": "PO-7781", "confidence": 0.90, "expect_status": "needs_human", "expect_reasons": ["gst_mismatch"]},
    {"id": "INV-NOPO", "amount_inr": 15000, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-0000", "confidence": 0.88, "expect_status": "needs_human", "expect_reasons": ["po_missing"]},
    {"id": "INV-BLUR", "amount_inr": 14000, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.55, "expect_status": "needs_typecheck", "expect_reasons": ["low_confidence"]},
    {"id": "INV-DUP", "amount_inr": 18600, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.90, "expect_status": "needs_human", "expect_reasons": ["duplicate_invoice"]},
    {"id": "INV-TOOLDOWN", "amount_inr": 11000, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.90, "expect_status": "needs_human", "expect_reasons": ["tool_error_fail_closed"]},
    {"id": "INV-OUTOFSCOPE", "amount_inr": 5000, "gstin": "29AAAAA0000A1Z5", "po_number": "PO-7781", "confidence": 0.90, "expect_status": "rejected", "expect_reasons": ["asks_to_pay_now"]}
  ]
}
```

**How to read the pack:**

- **INV-CLEAN** is the speed story. **INV-HIGH** and **INV-BADGST** are the safety story.
- **INV-DUP** needs episodic memory (the log), not only RAG.
- **INV-TOOLDOWN** proves fail-closed. **INV-OUTOFSCOPE** proves the desk refuses “please NEFT now.”

The prototype in upcoming sessions must pass **CLEAN, HIGH, BADGST** live. The other five stay on the pack so support-week work has a north star.

**Walkthrough of the three live cases:**

| Case | What the desk should do | If it does the opposite |
|---|---|---|
| **INV-CLEAN** | Extract → policy pass → `ready_to_pay` | You automated nothing; clerks still wait |
| **INV-HIGH** | Policy adds `amount_gate` → `needs_human` | A ₹90,000 bill skipped the AP lead |
| **INV-BADGST** | Policy adds `gst_mismatch` → `needs_human` | You recommended paying a dead GSTIN |

**INV-DUP** is the memory exam: after CLEAN is logged, the same vendor + amount + date must not look “new.” If your only store is Chroma, duplicates slip through because the handbook never saw that ticket.

**INV-OUTOFSCOPE** is the governance exam: a user message “NEFT this now” must **reject**, not grow a payout tool.

### Activity — Name the Missing Case

A student pack has only CLEAN and HIGH. Which harm is untested?

**Suggested answer:** Wrong or inactive **GSTIN** (and likely duplicates, tool-down, and “pay now”).

---

## Capstone Contract Checklist

Before architecture, this page should be yes on every line:

- Problem is one sentence plus **money** as the harm type
- In/out scope lists **no live NEFT**
- Every agent has a **non-goal**
- Packet fields are frozen (`ticket_id`, `gstin`, `confidence`, `status`, `reasons`)
- Every tool is **read or write** with an owner
- Memory names **three stores** (packet, Chroma, SQLite)
- Gates: amount ₹50,000, confidence 0.80, GST/PO fail, fail-closed
- Eval pack has at least **speed** and **safety** cases
- Reporter cannot pay

If a teammate only has a framework screenshot, they are not designed yet.

**What this session does not freeze (on purpose):** FastAPI route names, SQLite table DDL, LangChain class names, n8n node screenshots. Those are **architecture and scaffolding**. Today you freeze *business and memory*. Tomorrow you freeze *floors and wires*.

Keep this page beside you in upcoming sessions. Architecture chooses floors. Scaffolding builds rooms. The prototype walks one clean bill and one gated bill through those rooms. If a later choice fights this contract — a payout tool, a single mega-agent, policy stored only in chat history — the choice is wrong, even if the demo looks fluent.

---

## Key Takeaways

- **Nimbus PayDesk** is the capstone product: faster AP clearing without a wrong GSTIN or a skipped high-value stamp.
- **Full-cycle design** freezes problem, scope, observe–think–act roles, tools, memory, and tests **before** a repository.
- **Memory** is three jobs: this ticket, policy by meaning, history in a log — not one giant prompt.
- **Success** splits **speed** (happy path) from **safety** (missed-gate rate = 0).
- Upcoming work turns this contract into architecture, then folders, then a running prototype.

Print the contract on one page. If a later demo cannot point to **INV-CLEAN**, **INV-HIGH**, and **INV-BADGST**, it is not PayDesk yet — it is a chat window with invoices in the prompt.

Carry **money** as the harm type into architecture. If a floor plan cannot show where ₹50,000 stops, the plan is incomplete even if every framework logo is present.

Take the eight-case JSON with you. Architecture will place it under `eval/`. Scaffolding will copy it. The prototype will sit three of the papers live.

---

## Important Commands, Libraries, Terminologies Used

| Term / item | Meaning |
|---|---|
| Nimbus PayDesk | Capstone invoice-exception desk for Nimbus Retail |
| Full-cycle agent design | Problem, loop, tools, memory, success tests — before code layout |
| Problem identification | User, current failure, harm, better outcome |
| Scope | In vs out (recommend pay, do not NEFT) |
| Observe–think–act | Intake sees, Policy judges, Router acts |
| Non-goal | What an agent must not do |
| Handoff / `InvoicePacket` | Pydantic/JSON ticket schema |
| Confidence threshold | Below 0.80 → human type-check |
| Tool requirement | Named system, owner, read vs write |
| Fail closed | Tool error → human, never assume pass |
| Short-term memory | Current packet / request state |
| Semantic memory | Policy chunks in Chroma |
| Episodic memory | Ticket and event rows in SQLite |
| Procedural memory | Gate rules in Python |
| Success criterion | Loggable number; speed ≠ safety |
| Missed-gate rate | Safety metric; target **0** |
| Evaluation pack | Frozen cases with expected status/reasons |
| `packet_contract.py` | Runnable schema check |
| `memory_map.py` | Teaching router for which store to query |
| Dummy GSTIN | `29AAAAA0000A1Z5` — not a real firm |
| Amount gate | ≥ ₹50,000 must stop for AP lead |
| `ready_to_pay` | Recommended queue; human still pays |
| `needs_human` | Exception queue with reason codes |
| n8n webhook (later) | Same ingest body; not a second business flow |
| Observe–think–act–remember | Full cycle PayDesk must document |
| INV-CLEAN | Happy-path eval identity |
| INV-HIGH | Amount-gate eval identity |
| INV-BADGST | GST-mismatch eval identity |
