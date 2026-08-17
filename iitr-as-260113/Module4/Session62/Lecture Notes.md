# Prototyping a Multi-Agent System

## Introduction

In the **previous** session you opened PayDesk as an **empty office**: folders, SQLite, seeded registers, `/health`, and ingest that stored status `ingested`. The pipeline was a stub.

This session **hires the specialists**. You will implement tools, attach memory, run a **sequential LangChain** pipeline (extract → policy → route), stamp through FastAPI, and sit three exam cases. Success is **INV-CLEAN** ready and **INV-HIGH** / **INV-BADGST** stopped.

**What you will learn:**

- Implement **tools** the agents can call (GST check, PO lookup, policy retrieve, append-only ticket logging)
- Build a sequential **multi-agent pipeline** with LangChain (extract → policy → route on InvoicePacket)
- Connect **SQL** as working and episodic memory (ticket row after pipeline; `find_duplicate`)
- Connect the **RAG pipeline** with Chroma DB (seed `data/policy.md`; fail closed if the store is empty)
- Attach a **human-approval** path on the API (`POST /tickets/{id}/stamp`; router must not approve)
- Create an **n8n workflow** and attach it to the system (HTTP Request to `POST /ingest`; alert on `needs_human`)
- Evaluate and iterate on live cases (INV-CLEAN ready; INV-HIGH and INV-BADGST gated; one targeted fix)

![PayDesk assembly line with extract, policy, and route clerks stamping a live invoice packet](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session62/session62-01-assembly-line.png)

---

## Why a Prototype Is a Thin Slice, Not a Rewrite

A prototype proves the **contract** on real doors. It does not grow a bank.

- **Official Definition:** A **functional prototype** runs the critical paths with real tools and memory, on the same HTTP doors you will demo.
- **In Simple Words:** Two bills through the real office — one clean, one dirty — not a new slideshow.
- **Real-Life Example:** A **passport seva** dry run uses one clean file and one file missing police verification. It does not print 10,000 booklets on day one.

**Need:** Eval must hit `POST /ingest`, not a private function FastAPI never sees.

Install the Floor 2–4 libraries (venv still active):

```bash
pip install langchain langchain-core langchain-ollama chromadb httpx
```

Add those names to `requirements.txt`. Keep **no** payout SDK.

---

## Tools: The Workshop on Floor 3

Tools are Python functions with clear inputs. Policy must call them. It must not “remember” the vendor table.

- **Official Definition:** A **tool** is a bounded function an agent may call to read or write a system of record.
- **In Simple Words:** A phone to the register, not a guess.
- **Real-Life Example:** Checking a PO in Tally is a tool. Inventing a PO in chat is fraud.

```python
# app/tools.py — GST, PO, policy retrieve, log
from langchain_core.tools import tool  # langChain-callable wrappers
from app.db import connect, log_event  # sqlite
from app.memory import retrieve_policy_chunks  # chroma


@tool  # extractor and policy may call this
def check_gstin(gstin: str) -> str:  # read vendor register
    conn = connect()  # open sqlite
    row = conn.execute("SELECT vendor FROM vendors WHERE gstin = ?", (gstin,)).fetchone()  # exact match
    conn.close()  # release
    if row is None:  # unknown or dummy-invalid
        return "UNKNOWN"  # caller must fail closed / mismatch
    return f"KNOWN:{row['vendor']}"  # registry hit


@tool
def lookup_po(po_number: str) -> str:  # read ERP stand-in
    conn = connect()  # open
    row = conn.execute("SELECT vendor FROM purchase_orders WHERE po_number = ?", (po_number,)).fetchone()
    conn.close()  # release
    if row is None:  # missing PO
        return "MISSING"  # do not invent
    return f"FOUND:{row['vendor']}"  # exists


@tool
def retrieve_policy(query: str) -> str:  # semantic handbook
    chunks = retrieve_policy_chunks(query)  # chroma; may be empty
    if not chunks:  # empty store is a failure
        return "POLICY_STORE_EMPTY"  # fail closed upstream
    return " | ".join(chunks)  # short grounded string


@tool
def log_tool(ticket_id: str, action: str, detail: str) -> str:  # audit
    log_event(ticket_id, "tool", action, detail)  # append-only
    return "logged"  # tiny ack
```

**How the code works:**

- `@tool` makes the same functions usable from a LangChain agent later.
- `UNKNOWN` / `MISSING` / `POLICY_STORE_EMPTY` are **signals**, not English essays.
- Logging is a tool so traces show *when* the workshop was used.

![Four workshop stamps labelled GST, PO, policy binder, and audit log](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session62/session62-02-tool-stamps.png)

---

## Memory: Packet, SQLite, Chroma

You froze three stores. Wire two helpers: seed Chroma from `data/policy.md`, retrieve top chunks.

```python
# app/memory.py — long-term semantic policy
from pathlib import Path  # file path
import chromadb  # vector store from the RAG track


def policy_client() -> chromadb.PersistentClient:  # disk-backed
    return chromadb.PersistentClient(path=".chroma")  # gitignored folder


def seed_policy() -> None:  # run once at startup after init_db
    text = Path("data/policy.md").read_text(encoding="utf-8")  # handbook
    lines = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.startswith("#")]  # skip heading
    col = policy_client().get_or_create_collection("ap_policy")  # named collection
    if col.count() == 0 and lines:  # seed only when empty
        ids = [f"p{i}" for i in range(len(lines))]  # stable ids
        col.add(ids=ids, documents=lines)  # default embedding


def retrieve_policy_chunks(query: str, k: int = 2) -> list[str]:  # semantic retrieve
    col = policy_client().get_or_create_collection("ap_policy")  # same collection
    if col.count() == 0:  # nobody seeded
        return []  # signal empty
    res = col.query(query_texts=[query], n_results=k)  # top-k
    docs = res.get("documents") or [[]]  # chroma shape
    return docs[0]  # list of strings
```

Call `seed_policy()` from FastAPI startup next to `seed()`.

**How the code works:**

- Each handbook **line** is a chunk — enough for a six-rule lab file.
- Empty collection returns `[]` so Policy can fail closed.
- Ticket history stays in **SQLite**, not Chroma. Duplicates are a SQL lookup.

Duplicate helper (add to `db.py`):

```python
def find_duplicate(vendor: str, amount_inr: int, invoice_date: str, ticket_id: str) -> bool:
    conn = connect()  # open
    row = conn.execute(  # episodic memory: a prior ticket with same triple
        """SELECT ticket_id FROM tickets
           WHERE vendor = ? AND amount_inr = ? AND invoice_date = ? AND ticket_id != ?""",
        (vendor, amount_inr, invoice_date, ticket_id),
    ).fetchone()  # one hit is enough
    conn.close()  # release
    return row is not None  # True → duplicate_invoice reason
```

---

## Sequential Pipeline: Three Specialists in LCEL

Roles stay Crew-like. Runtime is a LangChain **runnable sequence** so steps stay inspectable.

- **Official Definition:** **Sequential multi-agent orchestration** runs specialist steps in a fixed order; later steps receive the packet, not a free-form debate.
- **In Simple Words:** Token windows in order — not a shouting match over rupees.
- **Real-Life Example:** Lab → verification → supervisor. The supervisor does not rewrite the blood values.

Lab invoices are **labelled slips**. Extract is a parser tool composed in LCEL. A ChatOllama extract chain can replace it when you point at prose; do not block the three exam cases on a down model.

```python
# app/pipeline.py — extract → policy → route
from langchain_core.runnables import RunnableLambda  # wrap python as LCEL
from app.config import AMOUNT_GATE_INR, MIN_CONFIDENCE  # procedural gates
from app.models import InvoicePacket  # packet
from app.tools import check_gstin, lookup_po, retrieve_policy, log_tool  # workshop
from app.db import find_duplicate  # episodic


def parse_labelled(raw: str) -> dict:  # extractor specialist
    fields = {}  # collected labels
    for line in raw.splitlines():  # one key per line
        if ":" not in line:  # skip blanks
            continue  # next line
        key, val = line.split(":", 1)  # split once
        fields[key.strip().lower()] = val.strip()  # normalise
    return {  # map labels to packet names
        "vendor": fields.get("vendor", ""),
        "gstin": fields.get("gstin", ""),
        "amount_inr": int(fields.get("amountinr", "0") or 0),
        "po_number": fields.get("po", ""),
        "invoice_date": fields.get("date", ""),
        "confidence": float(fields.get("confidence", "0.91") or 0.91),  # labelled default; BLUR can send 0.55
    }  # extract output


def extract_agent(packet: InvoicePacket) -> InvoicePacket:  # specialist 1
    data = parse_labelled(packet.raw_text)  # observe → structure
    for key, val in data.items():  # copy onto packet
        setattr(packet, key, val)  # field update
    packet.status = "needs_typecheck" if packet.confidence < MIN_CONFIDENCE else "needs_policy"
    log_tool.invoke({"ticket_id": packet.ticket_id, "action": "extract", "detail": packet.status})
    return packet  # handoff


def policy_agent(packet: InvoicePacket) -> InvoicePacket:  # specialist 2
    if packet.status == "needs_typecheck":  # extract already stopped for a human
        return packet  # do not overwrite with ready_to_pay
    reasons: list[str] = []  # start empty
    gst = check_gstin.invoke({"gstin": packet.gstin})  # tool: registry
    if gst == "UNKNOWN":  # not in vendors table
        reasons.append("gst_mismatch")  # tax desk
    po = lookup_po.invoke({"po_number": packet.po_number})  # tool: ERP stand-in
    if po == "MISSING":  # unknown PO
        reasons.append("po_missing")  # do not invent
    pol = retrieve_policy.invoke({"query": "amount gate GSTIN purchase order NEFT"})  # grounded rules
    if pol == "POLICY_STORE_EMPTY":  # chroma not seeded
        reasons.append("tool_error_fail_closed")  # fail closed
    if packet.amount_inr >= AMOUNT_GATE_INR:  # python gate, not prompt
        reasons.append("amount_gate")  # AP lead
    if find_duplicate(packet.vendor, packet.amount_inr, packet.invoice_date, packet.ticket_id):
        reasons.append("duplicate_invoice")  # episodic
    packet.reasons = reasons  # write packet
    packet.status = "needs_human" if reasons else "ready_to_pay"  # think → decision
    log_tool.invoke({"ticket_id": packet.ticket_id, "action": "policy", "detail": ",".join(reasons)})
    return packet  # handoff


def route_agent(packet: InvoicePacket) -> InvoicePacket:  # specialist 3
    if packet.status != "needs_human":  # clean path
        return packet  # reporter will count ready
    if "gst_mismatch" in packet.reasons:  # owner pick
        log_tool.invoke({"ticket_id": packet.ticket_id, "action": "route", "detail": "tax_desk"})
    else:  # amount, po, duplicate, tool
        log_tool.invoke({"ticket_id": packet.ticket_id, "action": "route", "detail": "ap_lead"})
    return packet  # still needs_human; no stamp here


def run_pipeline(packet: InvoicePacket) -> InvoicePacket:  # LCEL sequence
    seq = RunnableLambda(extract_agent) | RunnableLambda(policy_agent) | RunnableLambda(route_agent)
    return seq.invoke(packet)  # one ticket, three specialists
```

Replace the stub `run_pipeline` in `app/pipeline.py`. Ingest already calls it — status will now move past `ingested`.

**How the code works:**

- `|` is LCEL: extract, then policy, then route. No AutoGen debate.
- If extract sets `needs_typecheck`, **policy does not run**. That matches the gate you froze in design.
- Gates live in **Python** and **tool return codes**. Retrieved handbook lines are evidence, not a licence to skip `AMOUNT_GATE_INR`.
- `ready_to_pay` remains a **recommendation**.

Optional LangChain extract for unlabelled prose (same packet fields): `ChatPromptTemplate | ChatOllama | JsonOutputParser`. Swap it inside `extract_agent` when the model is up. Keep labelled parse for the eval pack.

### Activity — Who Must Not Stamp?

`route_agent` logs `tax_desk`. May it set `status = "approved"`?

**Suggested answer:** **No.** Only `POST /tickets/{id}/stamp` (a human) may approve.

---

## Human Stamp Door and Report

Add to `app/main.py`:

```python
from app.models import StampBody  # human body
from app.db import connect, log_event  # writes


@app.post("/tickets/{ticket_id}/stamp")  # human-only door
def stamp(ticket_id: str, body: StampBody) -> dict:  # named person in real life
    row = get_ticket(ticket_id)  # must exist
    if not row:  # unknown
        raise HTTPException(status_code=404, detail="unknown ticket")
    new_status = "approved" if body.approve else "rejected"  # stamp
    conn = connect()  # open
    conn.execute("UPDATE tickets SET status = ? WHERE ticket_id = ?", (new_status, ticket_id))
    conn.commit()  # save
    conn.close()  # release
    log_event(ticket_id, "human", "stamp", body.comment or new_status)  # actor is human
    return {"ticket_id": ticket_id, "status": new_status}  # clerk view


@app.get("/report")  # CFO counts
def report() -> dict:  # read-only
    conn = connect()  # open
    cur = conn.execute("SELECT status, COUNT(*) AS n FROM tickets GROUP BY status")  # group
    counts = {r["status"]: r["n"] for r in cur.fetchall()}  # dict
    conn.close()  # release
    return counts  # no payout field
```

Also **update** `insert_ticket` to save fields *after* `run_pipeline` (ingest already dumps the packet — you are done if `model_dump()` includes extract output). If ingest inserted *before* pipeline in your copy, move `insert_ticket` to **after** `run_pipeline`.

![Two paths on the desk: green ready-to-pay for a clean bill and red human-stamp window for a high-value bill](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session62/session62-03-two-paths.png)

**Live demo script:**

1. POST ingest with `inv_clean.txt` → expect `ready_to_pay`, empty reasons
2. POST ingest with `inv_high.txt` → expect `needs_human` including `amount_gate`
3. POST stamp `approve: false` on the high ticket → `rejected`
4. GET `/report` → counts moved

---

## Three-Case Eval Runner

Eval is how you iterate without “the demo felt good.”

```python
# eval/runner.py — run: python -m eval.runner  (from nimbus_paydesk/)
import json  # cases file
from pathlib import Path  # paths
from fastapi.testclient import TestClient  # in-process HTTP
from app.main import app  # same doors as demo

client = TestClient(app)  # no live port needed
CASES = json.loads(Path("eval/cases.json").read_text())["cases"]  # eight-pack
LIVE = {"INV-CLEAN", "INV-HIGH", "INV-BADGST"}  # today's slice


def labelled(case: dict) -> str:  # build sample text
    return (  # same format as data/samples
        f"Vendor: Kaveri Packaging Pvt Ltd\nGSTIN: {case['gstin']}\n"
        f"AmountINR: {case['amount_inr']}\nPO: {case['po_number']}\nDate: 2026-08-01\n"
    )  # extractable slip


if __name__ == "__main__":  # sit the exam
    for case in CASES:  # walk pack
        if case["id"] not in LIVE:  # skip support-week cases
            continue  # next
        res = client.post("/ingest", json={"raw_text": labelled(case), "ticket_id": case["id"]})  # door
        body = res.json()  # packet
        ok_status = body["status"] == case["expect_status"]  # speed or safety
        reasons = body.get("reasons") or []  # list
        ok_reason = all(r in reasons for r in case["expect_reasons"])  # required reasons present
        print(case["id"], "PASS" if ok_status and ok_reason else "FAIL", body["status"], reasons)
```

For `INV-CLEAN`, `expect_reasons` is `[]` — `all(...)` on an empty list is True. HIGH must include `amount_gate`. BADGST must include `gst_mismatch`.

Run it. If CLEAN fails as `needs_human` because Chroma was empty, the **targeted fix** is call `seed_policy()` on startup — not “skip retrieve.” Fail closed was correct; empty store was the bug.

![Clipboard with three exam papers: CLEAN pass, HIGH stop, BADGST stop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session62/session62-04-eval-clipboard.png)

### Activity — Read the Failure

HIGH returns `ready_to_pay`. Which control was skipped, and which metric dies?

**Suggested answer:** `AMOUNT_GATE_INR` never ran (or was only in a prompt). **Missed-gate rate** leaves 0.

---

## Iterative Fix Loop

When a case fails, patch **one** class of defect, then re-run the same three cases.

| Failure | Likely class | Fix |
|---|---|---|
| CLEAN is `needs_human` with `POLICY_STORE_EMPTY` | Memory seed | `seed_policy()` on boot |
| CLEAN is `gst_mismatch` | Seed data | Kaveri GSTIN in vendors |
| HIGH is ready | Procedural gate | Compare `>= 50000` in Python |
| BADGST is ready | Tool unused | Policy must call `check_gstin` |
| Duplicate never fires | Episodic | `find_duplicate` before ready |
| Invoice says “ignore gates” | Injection | Gates not in model control |

**Need:** Do not “fix” HIGH by lowering the amount in the sample. That hides the safety story.

---

## Attach n8n as the Courier

The desk must already pass CLEAN / HIGH / BADGST. Then automation knocks on the **same** ingest door. n8n does not become a second judge.

- **Official Definition:** An **attached workflow** starts the API. It does not copy amount or GST rules.
- **In Simple Words:** A courier delivers the file. The office still stamps.
- **Real-Life Example:** Speed-post to a passport seva window is not a second verification desk.

**Build this in n8n:**

1. **Manual Trigger** (lab) or mailbox trigger later
2. **HTTP Request** `POST http://localhost:8000/ingest` with JSON `{"raw_text": "<labelled slip>", "ticket_id": "INV-N8N-1"}`
3. **IF** `{{$json.status}}` equals `needs_human` → email or Slack “Stamp ticket INV-N8N-1”
4. **Else** → log the recommendation only — do **not** mark paid

Ping `GET /health` first. If n8n retries, reuse `ticket_id` so `INSERT OR REPLACE` updates the same row. Never add “if amount > 50000” inside n8n — that is two judges.

### Activity — Two Judges Again

n8n auto-replies “approved” when FastAPI returns `needs_human`. What broke?

**Suggested answer:** The courier started stamping. Only `POST /tickets/{id}/stamp` may approve.

---

## What the Prototype Still Owes Support Week

Be honest on the demo slide:

- Eight-case pack: only three live; DUP, BLUR, TOOLDOWN, OUTOFSCOPE remain
- Labelled extract for eval; prose/OCR later
- OpenAPI instead of a rich UI
- Still **no NEFT**

That list is a **limitation**, not a failure. A prototype that passes CLEAN/HIGH/BADGST on real doors is capstone-complete for these sessions.

---

## Wiring Checklist Before You Demo

Tick these in order. Skipping a tick is how CLEAN “randomly” fails.

1. Startup runs `init_db()`, `seed()`, and `seed_policy()`
2. `run_pipeline` in ingest is the LCEL sequence, not the old stub
3. `insert_ticket` runs **after** pipeline so SQLite stores `ready_to_pay` / `needs_human`
4. `.chroma/` is gitignored; `paydesk.db` is gitignored
5. `INV-CLEAN` uses dummy GSTIN `29AAAAA0000A1Z5` and `PO-7781`
6. Stamp is tested on a `needs_human` ticket, never on CLEAN
7. `/report` has no `paid` or `neft` key
8. n8n posts `/ingest` only after the three cases pass — no amount-gate node in n8n

**Common doubt:** “Can CrewAI replace LCEL this afternoon?” Roles are already sequential. Swapping runtime mid-demo burns the hour. Keep LangChain `|` for this prototype.

### Activity — Demo Order

You have five minutes with a CFO. Which two POSTs do you run first, and which door do you *not* open?

**Suggested answer:** Ingest CLEAN, ingest HIGH. Do **not** open a payout door. Stamp HIGH only if they ask who stops ₹90,000.

---

## LangChain Extract for Unlabelled Prose (Same Packet)

When a bill is a paragraph, keep the **same** packet fields. Swap `parse_labelled` for `ChatPromptTemplate | ChatOllama | JsonOutputParser` that returns `vendor`, `gstin`, `amount_inr`, `po_number`, `invoice_date`, `confidence`. Policy still calls tools. Eval stays on labelled slips so class does not depend on model mood.

---

## Key Takeaways

- PayDesk prototype is a **sequential LangChain pipeline** of extract, policy, and route on the FastAPI doors you already opened.
- **Tools** read SQLite and Chroma; **gates** stay in Python; **humans** stamp on a separate door.
- **Memory** is three stores in action: packet, policy chunks, ticket history (duplicates).
- **Eval through `/ingest`** plus one targeted fix beats a fluent untested demo.
- **n8n** may start ingest and alert on `needs_human`. It must not copy gates or send money.
- Support week extends remaining cases and UI — it must not add a payout tool.

A CFO demo that shows CLEAN ready, HIGH queued, and a human reject is a complete story.

---

## Important Commands, Libraries, Terminologies Used

| Term / item | Meaning |
|---|---|
| Functional prototype | Critical paths on real doors with tools and memory |
| `pip install langchain langchain-core langchain-ollama chromadb httpx` | Floor 2–4 libraries plus TestClient |
| `@tool` | LangChain-callable GST/PO/policy/log functions |
| `check_gstin` / `lookup_po` | Registry reads; UNKNOWN/MISSING signals |
| `retrieve_policy` | Chroma chunks or POLICY_STORE_EMPTY |
| `PersistentClient` `.chroma/` | Disk vector store, gitignored |
| `RunnableLambda` and `|` | LCEL sequential specialists |
| `parse_labelled` | Extractor for lab slips |
| `AMOUNT_GATE_INR` | Python amount stop |
| `find_duplicate` | Episodic SQLite memory |
| `POST /tickets/{id}/stamp` | Human approve/reject |
| `GET /report` | Status counts; not a bank |
| `TestClient` | Eval hits the same app |
| INV-CLEAN / HIGH / BADGST | Live exam slice |
| Targeted fix | One defect class, then re-run |
| Fail closed | Empty Chroma → needs_human, then seed |
| `ready_to_pay` | Recommendation only |
| Support week | Remaining cases and UI — no NEFT |
| n8n courier | POST /ingest then IF needs_human; no amount node |
| `extract_prose` | Optional ChatOllama JSON fill; Policy still judges |
| `JsonOutputParser` | Structured extract output |
| Wiring checklist | Seed, pipeline, insert-after, gitignore, demo order |
| TestClient | In-process HTTP so eval uses real doors |
| `seed_policy()` | Startup must fill Chroma or CLEAN fail-closes |
| Labelled slip | Vendor / GSTIN / AmountINR / PO / Date lines |
| Type-check skip | `needs_typecheck` means policy must not run |
