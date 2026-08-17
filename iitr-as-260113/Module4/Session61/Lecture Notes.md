# Hands-on: Project Setup and Scaffolding

## Introduction

In the **previous** session you froze PayDesk **architecture**: four floors, five HTTP doors, SQLite as the register, Chroma for policy, sequential LangChain later, n8n as courier, **no bank**.

This session **scaffolds** that map. You will create the repository, secrets file, folders, Pydantic packet, SQLite schema, sample policy, and FastAPI **health** plus **ingest** stubs. Success today is a ticket that exists **without** calling a model.

**What you will learn:**

- Initialise the repository, virtual environment, dependencies, and secret handling (`nimbus_paydesk` venv; `.env` gitignored)
- Scaffold folders for app code, knowledge corpus, samples, and eval cases (`app/`, `data/policy.md`, labelled invoices)
- Connect **SQL** and persist core records (SQLite tickets, events, vendors, purchase_orders; seed Kaveri / PO-7781)
- Expose **API stubs** for health and ingest (`GET /health` and `POST /ingest` storing status `ingested`)
- Prove the empty pipeline can **create and fetch** a record without calling a model (restart test on `paydesk.db`)

![Empty PayDesk office with labelled rooms for app, data, and eval waiting to be furnished](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session61/session61-01-empty-office.png)

---

## Why Scaffold Before the Model

A fluent model on a missing table is a magic show. A boring health check on a real table is a desk.

- **Official Definition:** **Scaffolding** is the minimum runnable skeleton — folders, config, schema, and doors — that later sessions fill with agents.
- **In Simple Words:** Build the office rooms and the register book before you hire clerks who talk.
- **Real-Life Example:** A **passport seva** counter opens with tokens and files on day one. The fancy printer can wait. PayDesk opens with `/health` and a ticket row.

**Need:** If ingest only prints JSON in memory, a restart wipes the audit. SQLite must write **before** LangChain joins.

**Common doubt:** “Can we add extract today?” You may parse labelled sample fields into the packet. You must **not** block scaffolding on an LLM key.

---

## Repository, Environment, and Secrets

Work from a project folder named `nimbus_paydesk`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pydantic python-dotenv
```

**How the commands work:**

- `venv` isolates course libraries from the rest of your laptop.
- `fastapi` and `uvicorn` are Floor 1. `pydantic` is the packet. `python-dotenv` loads `.env`.
- LangChain and Chroma wait for the **next** session so today’s proof stays offline-friendly.

`.gitignore` must include:

```text
.venv/
.env
*.db
__pycache__/
.chroma/
```

`.env.example` (commit this, not `.env`):

```text
# copy to .env and fill; never commit .env
PAYDESK_DB=paydesk.db
OLLAMA_MODEL=llama3.2
# OLLAMA_BASE_URL=http://localhost:11434
```

- **Official Definition:** **Secret handling** means live keys and local database files stay out of git while examples stay in the repo.
- **In Simple Words:** Share the blank form. Do not share the filled lock combination.
- **Real-Life Example:** You photocopy a KYC *template*. You do not photocopy someone’s PAN card onto GitHub.

### Activity — What Must Not Be Committed?

You created `paydesk.db` after one ingest. Git status shows it. Add or ignore? Why?

**Suggested answer:** **Ignore.** The desk file is local state. Seed scripts recreate vendors; tickets are not source code.

---

## Folder Map on Disk

Create the architecture folders even if some files stay empty until the next session.

```text
nimbus_paydesk/
  .env.example
  .gitignore
  requirements.txt
  app/
    __init__.py
    config.py
    models.py
    db.py
    main.py
    pipeline.py          # empty stub: return packet unchanged
    tools.py             # empty stub
    memory.py            # empty stub
  data/
    policy.md
    seed.sql
    samples/
      inv_clean.txt
      inv_high.txt
      inv_badgst.txt
  eval/
    cases.json
```

`requirements.txt`:

```text
fastapi
uvicorn
pydantic
python-dotenv
```

Leave a comment in `pipeline.py` that extract and policy **will** live there. Do not invent `pay_vendor.py`.

![Ticket form showing locked InvoicePacket fields on a clipboard](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session61/session61-02-packet-form.png)

---

## Config and Packet Models

`app/config.py` holds procedural memory — gates and statuses — not prompts.

```python
# app/config.py — gates and doors frozen in architecture
AMOUNT_GATE_INR = 50000  # AP-lead stamp at or above this rupee value
MIN_CONFIDENCE = 0.80  # below this, type-check; do not guess GSTIN
DB_PATH = "paydesk.db"  # sqlite file; override later with env if needed
ALLOWED_STATUSES = (  # only these strings may be stored
    "ingested",  # row created from ingest
    "needs_extract",  # waiting for extractor
    "needs_policy",  # fields filled
    "needs_typecheck",  # low confidence
    "ready_to_pay",  # recommendation only
    "needs_human",  # exception queue
    "approved",  # human stamped yes
    "rejected",  # stopped
)  # end statuses
```

`app/models.py` is the handoff contract as Pydantic.

```python
# app/models.py — request and ticket shapes for FastAPI
from pydantic import BaseModel, Field  # typed bodies


class IngestBody(BaseModel):  # what POST /ingest accepts today
    raw_text: str = Field(min_length=3)  # labelled invoice text
    ticket_id: str | None = None  # optional; we generate if missing


class StampBody(BaseModel):  # human-only door; unused until next session
    approve: bool  # yes or no
    comment: str = ""  # audit note


class InvoicePacket(BaseModel):  # ticket returned to the clerk
    ticket_id: str  # INV-…
    vendor: str = ""  # filled later by extract
    gstin: str = ""  # dummy format in samples
    amount_inr: int = 0  # 0 means not extracted yet
    po_number: str = ""  # claimed PO
    invoice_date: str = ""  # ISO date if present
    confidence: float = 0.0  # 0 until extract
    status: str  # must be from ALLOWED_STATUSES
    reasons: list[str] = []  # gate reasons
    raw_text: str = ""  # original ingest text
```

**How the code works:**

- `IngestBody` is Floor 1. `InvoicePacket` is the packet that will travel Floor 2.
- `amount_inr: 0` on ingest is honest: scaffolding has not extracted yet. Do not copy `Field(ge=1)` from a filled-slip example onto this ingest model.
- Stamp body exists so the door list stays complete even if we do not wire stamp today.

---

## SQLite Schema and Helpers

Four tables match the architecture winner list: tickets, events, vendors, purchase orders.

```python
# app/db.py — sqlite system of record
import sqlite3  # stdlib database
from app.config import DB_PATH  # file name


def connect() -> sqlite3.Connection:  # one connection helper
    conn = sqlite3.connect(DB_PATH)  # open or create paydesk.db
    conn.row_factory = sqlite3.Row  # rows act like dicts
    return conn  # caller must close or use context


def init_db() -> None:  # create tables if missing
    conn = connect()  # open
    conn.executescript(  # several statements at once
        """
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            vendor TEXT,
            gstin TEXT,
            amount_inr INTEGER,
            po_number TEXT,
            invoice_date TEXT,
            confidence REAL,
            status TEXT NOT NULL,
            reasons TEXT,
            raw_text TEXT
        );
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT,
            actor TEXT,
            action TEXT,
            detail TEXT
        );
        CREATE TABLE IF NOT EXISTS vendors (
            vendor TEXT PRIMARY KEY,
            gstin TEXT
        );
        CREATE TABLE IF NOT EXISTS purchase_orders (
            po_number TEXT PRIMARY KEY,
            vendor TEXT
        );
        """
    )  # schema ready
    conn.commit()  # save
    conn.close()  # release file


def log_event(ticket_id: str, actor: str, action: str, detail: str = "") -> None:
    conn = connect()  # open
    conn.execute(  # append-only audit line
        "INSERT INTO events(ticket_id, actor, action, detail) VALUES (?, ?, ?, ?)",
        (ticket_id, actor, action, detail),  # bound parameters, never string-paste SQL
    )  # event stored
    conn.commit()  # save
    conn.close()  # release


def insert_ticket(packet: dict) -> None:  # first write of a ticket
    conn = connect()  # open
    conn.execute(  # insert the ingest row
        """INSERT OR REPLACE INTO tickets(
            ticket_id, vendor, gstin, amount_inr, po_number, invoice_date,
            confidence, status, reasons, raw_text
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (  # tuple matches columns
            packet["ticket_id"], packet.get("vendor", ""), packet.get("gstin", ""),
            packet.get("amount_inr", 0), packet.get("po_number", ""),
            packet.get("invoice_date", ""), packet.get("confidence", 0.0),
            packet["status"], ",".join(packet.get("reasons", [])), packet.get("raw_text", ""),
        ),
    )  # row saved
    conn.commit()  # save
    conn.close()  # release


def get_ticket(ticket_id: str) -> dict | None:  # clerk fetch
    conn = connect()  # open
    row = conn.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,)).fetchone()  # one row
    conn.close()  # release
    return dict(row) if row else None  # None if unknown id
```

**How the code works:**

- `?` placeholders stop a crafted invoice text from becoming SQL.
- `INSERT OR REPLACE` lets eval and n8n **retry the same ticket_id** without a primary-key crash.
- `reasons` is stored as a comma-separated string for the prototype. Upcoming work can use JSON.
- `events` is append-only. Do not UPDATE event history.

Seed vendors and POs once (`data/seed.sql` run from Python or a tiny function in `init_db` after create):

| vendors.vendor | vendors.gstin |
|---|---|
| Kaveri Packaging Pvt Ltd | 29AAAAA0000A1Z5 |
| Nilgiri Cartons | 29BBBBB0000B1Z5 |

| purchase_orders.po_number | vendor |
|---|---|
| PO-7781 | Kaveri Packaging Pvt Ltd |
| PO-8802 | Nilgiri Cartons |

Unknown GSTIN `99INVALID` and PO-0000 must **not** appear in these tables.

---

## Sample Policy and Sample Invoices

`data/policy.md` is what Chroma will index next. Keep it short and numbered so retrieval is obvious.

```text
# Nimbus Retail AP Handbook (lab)

1. Amount gate: any invoice of 50000 INR or more needs AP lead stamp.
2. GSTIN must exist in the vendor register. Unknown GSTIN goes to tax desk.
3. Purchase order must exist in ERP. Missing PO is an exception, not a guess.
4. Duplicate: same vendor, amount, and date as a previous ticket needs AP lead.
5. PayDesk never sends NEFT. Status ready_to_pay is a recommendation only.
6. If a lookup tool fails, fail closed and send the ticket to a human.
```

Labelled sample (`data/samples/inv_clean.txt`):

```text
Vendor: Kaveri Packaging Pvt Ltd
GSTIN: 29AAAAA0000A1Z5
AmountINR: 18600
PO: PO-7781
Date: 2026-08-01
```

High-value sample uses `AmountINR: 90000`. Bad GST sample uses `GSTIN: 99INVALID` and `AmountINR: 12000`.

**Need:** Labelled slips make eval stable. Production extract will read prose. Do not pretend today’s ingest already “understood” a scan.

Copy the eight-case JSON from the design session into `eval/cases.json`. The runner waits until tools exist.

---

## FastAPI Doors: Health, Ingest, Get Ticket

`app/main.py` implements Floor 1 with a **pass-through** pipeline.

```python
# app/main.py — run: uvicorn app.main:app --reload
from uuid import uuid4  # ticket ids when caller sends none
from fastapi import FastAPI, HTTPException  # HTTP framework
from app.db import init_db, insert_ticket, get_ticket, log_event  # sqlite helpers
from app.models import IngestBody, InvoicePacket  # pydantic shapes
from app.pipeline import run_pipeline  # stub today

app = FastAPI(title="Nimbus PayDesk")  # OpenAPI at /docs


@app.on_event("startup")  # once when the server boots
def boot() -> None:  # create tables
    init_db()  # schema + you can call seed here


@app.get("/health")  # liveness door
def health() -> dict:  # n8n can ping this
    return {"status": "ok"}  # architecture contract


@app.post("/ingest", response_model=InvoicePacket)  # mailbox door
def ingest(body: IngestBody) -> InvoicePacket:  # synchronous ingest
    ticket_id = body.ticket_id or f"INV-{uuid4().hex[:6].upper()}"  # generate if missing
    packet = InvoicePacket(  # scaffolding packet: stored, not judged
        ticket_id=ticket_id,  # identity
        status="ingested",  # honest: pipeline is still a stub
        raw_text=body.raw_text,  # keep source
    )  # model-ready object
    packet = run_pipeline(packet)  # today: returns the same packet
    insert_ticket(packet.model_dump())  # system of record
    log_event(ticket_id, "api", "ingest", packet.status)  # audit line
    return packet  # clerk sees JSON


@app.get("/tickets/{ticket_id}")  # clerk fetch
def read_ticket(ticket_id: str) -> dict:  # raw row for now
    row = get_ticket(ticket_id)  # sqlite
    if not row:  # unknown id
        raise HTTPException(status_code=404, detail="unknown ticket")  # honest miss
    return row  # includes status and raw_text
```

Empty pipeline stub `app/pipeline.py`:

```python
# app/pipeline.py — sequential agents will replace this stub
from app.models import InvoicePacket  # packet type


def run_pipeline(packet: InvoicePacket) -> InvoicePacket:  # Floor 2 placeholder
    return packet  # no extract, no policy, no route yet
```

**How the code works:**

- Startup creates tables so the first POST cannot fail on “no such table.”
- Ingest **writes SQLite first-class**, even though status stays `ingested`.
- `/docs` is the prototype clerk UI. Try POST ingest, then GET the id.

Run:

```bash
uvicorn app.main:app --reload
```

Open `/health`. You should see `{"status":"ok"}`. POST `/ingest` with `{"raw_text":"Vendor: Kaveri"}`. GET `/tickets/INV-…` should show `ingested`.

![Green health lamp on the PayDesk reception window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session61/session61-03-health-lamp.png)

### Activity — Restart Test

Ingest once. Stop uvicorn. Start it again. GET the same ticket id. What proves SQLite is the system of record?

**Suggested answer:** The row is still there with the same `ticket_id`. Memory-only JSON would have vanished.

---

## Seed Function You Can Call at Boot

Add this to `db.py` and call it from `boot()` after `init_db()`.

```python
def seed() -> None:  # lab vendors and POs; safe to run twice
    conn = connect()  # open
    conn.execute(  # dummy GSTIN — not a real firm
        "INSERT OR IGNORE INTO vendors(vendor, gstin) VALUES (?, ?)",
        ("Kaveri Packaging Pvt Ltd", "29AAAAA0000A1Z5"),
    )  # known vendor
    conn.execute(
        "INSERT OR IGNORE INTO vendors(vendor, gstin) VALUES (?, ?)",
        ("Nilgiri Cartons", "29BBBBB0000B1Z5"),
    )  # second vendor
    conn.execute(
        "INSERT OR IGNORE INTO purchase_orders(po_number, vendor) VALUES (?, ?)",
        ("PO-7781", "Kaveri Packaging Pvt Ltd"),
    )  # known PO
    conn.execute(
        "INSERT OR IGNORE INTO purchase_orders(po_number, vendor) VALUES (?, ?)",
        ("PO-8802", "Nilgiri Cartons"),
    )  # second PO
    conn.commit()  # save
    conn.close()  # release
```

**How the code works:**

- `INSERT OR IGNORE` lets you reboot without duplicate-key errors.
- Tools in the next session will **read** these rows. They will not invent POs.

![Seed packets of two vendors and two purchase orders landing in a register](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session61/session61-04-seed-register.png)

---

## What “Done” Means Today

Tick these before you add LangChain:

- `.venv` active; `/health` returns ok
- `.env` exists locally and is gitignored
- `paydesk.db` has four tables; vendors and POs seeded
- POST `/ingest` creates a row with status `ingested`
- GET `/tickets/{id}` returns that row after a process restart
- `data/policy.md` and three samples exist
- No file named like payout or NEFT
- `pipeline.py` is a stub, not a secret second API

**Common mistake:** Calling Ollama from `boot()` so the server cannot start without a model. Keep startup **offline**.

---

## Key Takeaways

- Scaffolding opens PayDesk as an **empty office with a real register**: folders, secrets, schema, and doors.
- **Ingest writes SQLite** even before extract. Audit starts on day one of the repo.
- **Labelled samples** and **policy.md** are data, not afterthoughts.
- FastAPI `/docs` is enough UI for this prototype. n8n can ping `/health` already.
- Upcoming work fills `tools.py`, `memory.py`, and `pipeline.py` and must pass CLEAN, HIGH, and BADGST.

---

## Important Commands, Libraries, Terminologies Used

| Term / item | Meaning |
|---|---|
| Scaffolding | Runnable skeleton: folders, schema, doors, no agents yet |
| `python -m venv .venv` | Isolated environment |
| `pip install fastapi uvicorn pydantic python-dotenv` | Floor 1 dependencies |
| `.env` / `.env.example` | Live secrets vs committed template |
| `.gitignore` | Drops `.venv`, `.env`, `*.db`, `.chroma` |
| `uvicorn app.main:app --reload` | Local API server |
| `/health` | Liveness door |
| `POST /ingest` | Create ticket from `raw_text` |
| `GET /tickets/{id}` | Clerk fetch |
| `InvoicePacket` | Pydantic handoff |
| `init_db` / `seed` | Schema and lab registers |
| `INSERT OR IGNORE` | Idempotent seed |
| Bound `?` parameters | Safe SQL |
| `events` table | Append-only audit |
| `run_pipeline` stub | Returns packet unchanged |
| Labelled sample | `Vendor:` / `GSTIN:` lines for stable eval |
| `data/policy.md` | Handbook for upcoming Chroma |
| System of record | SQLite file survives restart |
| OpenAPI `/docs` | Prototype clerk UI |
