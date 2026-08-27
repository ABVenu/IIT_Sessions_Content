# LLM Operations: Versioning, Eval Gates & Cost

## Introduction

In the **previous** session you built a **golden task set**, ran **offline evals**, scored with **pass / partial / fail**, and used a **promotion gate** so a bad clerk script never reaches the notice board.

That answers *“is this script good enough?”* This session answers *“how do we package, gate, price, and protect a full release?”*

**Running story:** the same **campus parcel desk**. A release is not only a new reply script. It is a **bundle**: script + tools + retrieval settings, checked by an **eval gate**, priced by **token cost**, and unlocked with **secrets** that never sit in a notebook.

**What you will learn:**

- Version **prompt**, **tool**, and **retrieval** configs together as one release
- Run a **pre-release eval gate** against the golden set before deploy
- Measure **token usage** and estimate **cost per task**
- Store **API keys** in environment variables — never in committed files

---

## Why Releases Need More Than a Prompt File

You already know how to version a single prompt file. A live desk also needs matching **tools** and **retrieval** settings. If only one piece moves, students get strange answers.

| Change only the prompt | Change the whole release bundle |
|---|---|
| Script says “check Flipkart shelf” but tool still searches Amazon only | Prompt, tools, and retrieval all agree on the same desk policy |
| You cannot roll back cleanly | One version label restores the full working desk |

![Campus parcel desk comparison — lone script paper causing mismatch versus a full release kit with prompt, tools, and retrieval under one sticker](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session58/session58-01-prompt-only-vs-release-bundle.png)

- **Official Definition:** **LLM Operations (LLMOps)** is running LLM apps with versioning, evaluation gates, cost control, and secure configuration — like DevOps for model-powered products.
- **In Simple Words:** Treat the desk like a product release, not a casual WhatsApp rewrite.
- **Real-Life Example:** A canteen app update ships menu text, payment button, and kitchen printer settings together — not menu text alone.

- **Official Definition:** A **release** is a named, shippable bundle of configs that together define agent behaviour for a period of time.
- **In Simple Words:** One labelled “desk kit” you can install or roll back.
- **Real-Life Example:** Hostel notice board version “March Week-2” includes wording, duty roster, and QR code — all three, not just the wording.

**Common doubt:** “Can I tweak tools later and keep the same prompt version?”  
You can experiment locally, but a **shipped** version should pin all three pieces so yesterday’s bug report is reproducible.

### Activity — Spot the Mismatch

Prompt says “look up by AWB”. Retrieval config still searches only by brand name. What breaks? **Answer:** Students with AWB slips get “not found” even when the parcel exists.

---

## Release Versioning = One Bundle, One Label

Extend the “one prompt file per version” habit into a **release workflow**: prompt, tools, and retrieval travel under the **same version id**.

- **Official Definition:** **Release versioning** assigns one version label to a coordinated set of artefacts (prompt text, tool allow-list, retrieval / index settings) so they are stored, compared, and rolled back together.
- **In Simple Words:** One sticker on the whole desk kit — not three stickers that drift apart.
- **Real-Life Example:** Exam hall kit “Set-B” includes question paper, answer key, and seating chart. Mixing Set-B paper with Set-A key is a disaster.

**Suggested folder layout (parcel desk)**

```text
releases/
  v1.0.0/
    prompt.json       # clerk reply scripts
    tools.json        # which tools the desk may call
    retrieval.json    # how the parcel register is searched
    RELEASE.md        # short human note: what changed
  v1.1.0/
    prompt.json
    tools.json
    retrieval.json
    RELEASE.md
  current.json        # points to the live version id
```

**What each file owns**

| File | Owns | Desk feel |
|---|---|---|
| `prompt.json` | Reply templates / system rules | How the clerk speaks |
| `tools.json` | Allowed tools + max steps | Which buttons the clerk may press |
| `retrieval.json` | Index name, top-k, filters | How the register is searched |
| `current.json` | Live version pointer | Which kit is on the notice board |

![Two parcel-desk release crates labeled v1.0.0 and v1.1.0 each holding prompt, tools, and retrieval together while LIVE pointer marks the notice-board kit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session58/session58-02-release-bundle-versioning.png)

**Why version them together:** A friendlier prompt that invents locations is already dangerous. A prompt that calls a new tool while retrieval still uses an old index is worse — failures look “random.”

**Common error:** Bumping only `prompt.json` while leaving tools/retrieval unnamed. Always copy the full folder and change what you need inside it.

### Full code — load a release bundle

```python
# Load one release: prompt + tools + retrieval under the same version id
from pathlib import Path
import json

RELEASES_DIR = Path("releases")  # Root folder for every named release


def read_json(version: str, filename: str) -> dict:
    path = RELEASES_DIR / version / filename  # e.g. releases/v1.0.0/prompt.json
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}")  # Fail early if kit is incomplete
    return json.loads(path.read_text(encoding="utf-8"))


def load_release(version: str) -> dict:
    return {
        "version": version,  # Keep the label with the data
        "prompt": read_json(version, "prompt.json"),  # Clerk script
        "tools": read_json(version, "tools.json"),  # Allowed tools
        "retrieval": read_json(version, "retrieval.json"),  # Search settings
    }


def set_current(version: str) -> None:
    pointer = {"live_version": version}  # Notice-board pointer
    (RELEASES_DIR / "current.json").write_text(json.dumps(pointer, indent=2), encoding="utf-8")


def get_current() -> str:
    data = json.loads((RELEASES_DIR / "current.json").read_text(encoding="utf-8"))
    return data["live_version"]


if __name__ == "__main__":
    v, folder = "v1.0.0", RELEASES_DIR / "v1.0.0"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "prompt.json").write_text(
        json.dumps({"name": "careful_clerk", "missing": "No parcel row found."}, indent=2), encoding="utf-8"
    )
    (folder / "tools.json").write_text(
        json.dumps({"allowed": ["lookup_parcel"], "max_steps": 2}, indent=2), encoding="utf-8"
    )
    (folder / "retrieval.json").write_text(
        json.dumps({"index": "campus_parcels", "top_k": 3, "filter": "active"}, indent=2), encoding="utf-8"
    )
    set_current(v)
    bundle = load_release(get_current())
    print(bundle["version"], "→ tools:", bundle["tools"]["allowed"])
```

**How the code works**

- Every artefact is read from the **same** version folder — no mixing `v1` prompt with `v2` retrieval.
- `current.json` is the notice-board pointer; rolling back means pointing to an older folder.
- Missing files raise errors early so you never ship a half kit.

### Activity — Name the Bundle

You change `top_k` from 3 to 1 and rewrite the missing-parcel line. Keep `v1.0.0` or create `v1.1.0`? **Answer:** Create **`v1.1.0`** (full folder copy) so the old kit stays reproducible.

---

## Pre-Release Eval Gate = Automated Ship Check for the Desk

Versioning alone does not prove the new kit is safe. Before `current.json` flips, run the **golden set** through a **pre-release eval gate** — an automated ship check, like a checklist that must pass before the notice board updates.

- **Official Definition:** A **pre-release eval gate** is a check that runs the candidate release against a frozen golden set and blocks promotion when scores breach the agreed threshold.
- **In Simple Words:** Re-take the practice paper with the new desk kit; fail the gate → keep the old kit live.
- **Real-Life Example:** Printers will not hang a new timetable if more than one room number fails the proof checklist.

You already authored golden tasks and a promotion decision in the **previous** session. Here we wire that gate to a **release version**, not only a prompt name.

![Pre-release eval gate blocking an overconfident desk kit from the student notice board while the careful LIVE baseline stays posted](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session58/session58-03-pre-release-eval-gate.png)

**Desk release pipeline**

1. Copy `v1.0.0` → `v1.1.0` and edit what you need.
2. Run offline eval on the golden JSON using the candidate bundle.
3. Score pass / partial / fail (same rubric as before).
4. Compare to the live baseline version.
5. If within threshold → update `current.json`; else **block**.

**Agreed gate threshold**

| Rule | Meaning |
|---|---|
| Fail count ≤ 1 | At most one hard fail |
| No new fail vs baseline | A former `pass` must not become `fail` |
| Partial count ≤ 2 | Soft gaps allowed but limited |

### Full code — gate a candidate release against the golden set

```python
# Pre-release eval gate: candidate release vs baseline using golden tasks
from pathlib import Path
import json

PARCELS = {
    "amazon": "Amazon box for Riya — ready at Gate 2 pickup.",
    "flipkart": "Flipkart pouch for Aman — held at hostel desk.",
}


def retrieve(query: str, retrieval: dict) -> str:
    q = query.lower().strip()
    if not q:
        return ""
    _ = retrieval.get("top_k", 3)  # Settings belong to the release bundle
    if "amazon" in q:
        return PARCELS["amazon"]
    if "flipkart" in q:
        return PARCELS["flipkart"]
    return ""


def reply(query: str, release: dict) -> str:
    prompt = release["prompt"]  # Clerk script from the bundle
    row = retrieve(query, release["retrieval"])  # Register lookup using retrieval settings
    if not query.strip():
        return prompt.get("empty", "Please tell the brand name.")  # Empty input branch
    if not row:
        return prompt.get("missing", "No parcel row found.")  # Unknown brand branch
    return prompt.get("found", "{row}").format(row=row)  # Known row branch


def eval_release(golden_path: Path, release: dict) -> dict:
    tasks = json.loads(golden_path.read_text(encoding="utf-8"))  # Load frozen golden set
    scores = {}
    for task in tasks:
        text = reply(task["query"], release).lower()  # Candidate desk reply
        tid = task["task_id"]  # e.g. G01 … G06 from previous work
        invents = "gate 2" in text and tid in ("G03", "G05", "G06")  # Unknowns must not invent
        honest = any(w in text for w in ("not found", "no parcel", "please", "brand"))
        if invents:
            scores[tid] = "fail"  # Hard fail — invented a location
        elif tid in ("G01", "G02", "G04") and ("amazon" in text or "flipkart" in text):
            scores[tid] = "pass"  # Known brands look aligned
        elif honest:
            scores[tid] = "pass"  # Honest empty / unknown handling
        else:
            scores[tid] = "partial"  # Soft gap — needs a human note later
    return scores


def gate_decision(baseline: dict, candidate: dict) -> dict:
    order = {"pass": 2, "partial": 1, "fail": 0}  # Higher number = better score
    fails = sum(1 for s in candidate.values() if s == "fail")  # Hard fails on candidate
    partials = sum(1 for s in candidate.values() if s == "partial")  # Soft gaps on candidate
    regs = [tid for tid, b in baseline.items() if tid in candidate and order[candidate[tid]] < order[b]]
    reasons = []  # Collect why we would block
    if fails > 1:
        reasons.append(f"fails={fails} > 1")  # Threshold: at most one fail
    if partials > 2:
        reasons.append(f"partials={partials} > 2")  # Threshold: at most two partials
    if regs:
        reasons.append(f"regressions={regs}")  # Any score drop vs baseline
    return {"promote": not reasons, "reasons": reasons or ["ok"], "regressions": regs}


if __name__ == "__main__":
    golden = Path("golden_parcel_tasks.json")  # Frozen answer key from previous work
    baseline_release = {
        "prompt": {"found": "{row}", "missing": "Sorry — no parcel row found.", "empty": "Please tell the brand."},
        "tools": {"allowed": ["lookup_parcel"], "max_steps": 2},
        "retrieval": {"index": "campus_parcels", "top_k": 3},
    }
    candidate_release = {
        "prompt": {"found": "{row}", "missing": "Your parcel is ready at Gate 2 pickup.", "empty": "Your parcel is ready at Gate 2 pickup."},
        "tools": {"allowed": ["lookup_parcel"], "max_steps": 2},
        "retrieval": {"index": "campus_parcels", "top_k": 3},
    }
    decision = gate_decision(eval_release(golden, baseline_release), eval_release(golden, candidate_release))
    print(json.dumps(decision, indent=2))
    print("FLIP current.json" if decision["promote"] else "BLOCK — keep live version")
```

**How the code works**

- The **whole release** (prompt + retrieval settings) answers each golden query.
- Baseline = live careful kit; candidate = overconfident kit that invents Gate 2.
- Gate prints **BLOCK** so `current.json` is not flipped.

**Avoid:** Flipping `current.json` because “G01 still passes”; editing golden tasks to match a bad release.

**Release flow at a glance**

| Step | Question the desk asks |
|---|---|
| Bundle | Are prompt, tools, and retrieval labelled together? |
| Eval gate | Does the golden set still pass the threshold? |
| Flip pointer | Only then may `current.json` point to the new folder |

### Activity — Apply the Pre-Release Gate

Baseline: 5 pass, 1 partial, 0 fail. Candidate: 3 pass, 1 partial, 2 fail (new fails on unknowns). Flip `current.json`? **Answer:** **No — block.**

---

## Token Usage and Cost = The Desk Meter

A release can pass the eval gate and still be too expensive for campus budget. You need a simple **meter**: tokens in, tokens out, and **rupees per task**.

- **Official Definition:** A **token** is a chunk of text the model reads or writes; billing is usually based on input tokens + output tokens.
- **In Simple Words:** Tokens are like SMS characters for the model — more text ≈ more charge.
- **Real-Life Example:** A long hostel circular costs more SMS packs than a one-line “Gate 2 ready” note.

- **Official Definition:** **Cost per task** estimates the money spent for one representative workload item (one golden query or one student enquiry).
- **In Simple Words:** “How many rupees for one Amazon parcel question?”
- **Real-Life Example:** Mess billing — cost per thali, not only the monthly total.

![Parcel desk token meter comparing a short honest reply versus a long warehouse essay burning many token chips and rupees](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session58/session58-04-token-cost-meter.png)

**Teaching price card (illustrative rates)**

| Direction | Example rate |
|---|---|
| Input tokens | ₹0.50 per 1,000 tokens |
| Output tokens | ₹1.50 per 1,000 tokens |

**Formula:** `cost = (input_tokens / 1000) * input_rate + (output_tokens / 1000) * output_rate`

**Why measure on a representative workload:** One lucky short reply hides a verbose prompt that burns tokens on every enquiry. Use the same golden set as your cost sample when possible — quality and cost then share one paper.

**Common doubt:** “Is counting words the same as tokens?”  
Close for teaching demos; real APIs return exact `usage` fields. Use API counts in production; word×1.3 is only a classroom estimate.

**Desk habit:** Log `input_tokens`, `output_tokens`, and `cost_inr` next to each eval run so a “friendlier” release that triples cost is visible before you scale.

### Full code — estimate tokens and cost per task

```python
# Estimate token use and rupee cost for a small golden workload
from pathlib import Path
import json

INPUT_RATE_PER_1K = 0.50  # Teaching rate: ₹ per 1,000 input tokens
OUTPUT_RATE_PER_1K = 1.50  # Teaching rate: ₹ per 1,000 output tokens


def estimate_tokens(text: str) -> int:
    words = len(text.split())  # Simple word count for classroom demos
    return max(1, int(words * 1.3))  # ~1 token ≈ 0.75 words → words * 1.3


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    inp = (input_tokens / 1000.0) * INPUT_RATE_PER_1K
    out = (output_tokens / 1000.0) * OUTPUT_RATE_PER_1K
    return round(inp + out, 4)


def cost_report(golden_path: Path, system_prompt: str) -> dict:
    tasks = json.loads(golden_path.read_text(encoding="utf-8"))
    rows, total_in, total_out, total_cost = [], 0, 0, 0.0
    for task in tasks:
        inp_text = system_prompt + "\n" + task["query"]  # What the model "reads"
        out_text = f"Status note for {task['task_id']}: please check the register."  # Fake reply
        tin, tout = estimate_tokens(inp_text), estimate_tokens(out_text)
        cost = estimate_cost(tin, tout)
        total_in += tin
        total_out += tout
        total_cost += cost
        rows.append({"task_id": task["task_id"], "input_tokens": tin, "output_tokens": tout, "cost_inr": cost})
    n = max(1, len(rows))
    return {
        "tasks": rows,
        "totals": {
            "input_tokens": total_in,
            "output_tokens": total_out,
            "cost_inr": round(total_cost, 4),
            "avg_cost_per_task_inr": round(total_cost / n, 4),
        },
    }


if __name__ == "__main__":
    system = "You are the campus parcel desk clerk. Be honest. Never invent Gate 2 for unknown brands."
    report = cost_report(Path("golden_parcel_tasks.json"), system)
    print(json.dumps(report["totals"], indent=2))
    for row in report["tasks"]:
        print(row["task_id"], "→", row["cost_inr"], "INR")
```

**How the code works**

- Each golden task becomes one **workload item** with estimated input/output tokens.
- Totals and **average cost per task** help you compare a verbose prompt vs a short one.
- Swap the estimator for real API `usage` when you call a live model.

### Activity — Cost Instinct

Two releases both pass the eval gate. A averages ₹0.02 / task; B averages ₹0.18 / task (long warehouse essay in every system prompt). Prefer for 10,000 daily enquiries? **Answer:** Prefer **A** (or shorten B) — quality gate first, then cost.

---

## Secrets Handling = Keys Stay Off the Notice Board

Releases and cost meters need API access. The key itself must never be pasted into notebooks or committed to git.

- **Official Definition:** A **secret** (here, an API key) is a credential that grants access to a paid or private service and must be stored outside source code.
- **In Simple Words:** The desk’s master key stays in a locked drawer — not taped to the notice board.
- **Real-Life Example:** You do not write your UPI PIN in a shared Google Doc with the fest budget sheet.

- **Official Definition:** An **environment variable** is a named value provided by the OS / runtime to a process (for example `OPENAI_API_KEY`) without hard-coding it in files.
- **In Simple Words:** A labelled slip the program reads at start-up, not text inside your `.py` file.
- **Real-Life Example:** Hostel Wi-Fi password lives in the warden’s config; apps read it at start — students do not carve it into the library wall.

![Unsafe API key taped on the notice board versus safe key locked in the parcel-desk drawer with no secret text on the laptop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session58/session58-05-secrets-locked-drawer.png)

**Safe habits**

- Put keys in `.env` (local) or the host’s secret store (cloud); load via environment variables.
- Add `.env` to `.gitignore` so git never uploads keys.
- Rotate a key if it was ever pasted into chat, screenshot, or a committed notebook.
- Share access via the provider dashboard — not by WhatsApp-ing the raw key.

**Unsafe patterns**

| Unsafe | Why it hurts |
|---|---|
| `api_key = "sk-..."` in a notebook | Anyone with the file can spend your money |
| Committing `.env` “just once” | Git history keeps secrets even after delete |
| Pasting keys into release JSON | Release folders are meant to be shared and versioned |

### Full code — read the key from the environment

```python
# Read API key from environment — never hard-code secrets in the repo
import os
from pathlib import Path


def load_dotenv_if_present(path: Path = Path(".env")) -> None:
    if not path.exists():
        return  # Cloud hosts may inject env vars another way
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue  # Skip blanks and comments
        key, value = line.split("=", 1)  # Split on first '=' only
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_secret(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing {name}. Export it or add it to local .env (do not commit).")
    return value


if __name__ == "__main__":
    load_dotenv_if_present()
    # Local .env line (never commit): PARCEL_DESK_API_KEY=replace-me
    key = require_secret("PARCEL_DESK_API_KEY")
    preview = key[:4] + "..." if len(key) >= 4 else "(short)"  # Never log the full key
    print("API key loaded for parcel desk. Preview:", preview)
```

**How the code works**

- `.env` can help on your laptop; the important rule is **process environment**, not source code.
- `require_secret` fails loudly if the key is missing — better than silent empty-string calls.
- Logs print a **preview**, never the full secret.

### Activity — Secret Check

Which is safe to commit: (1) `releases/v1.1.0/prompt.json`, (2) notebook cell `KEY="sk-live-..."`, (3) `.gitignore` entry for `.env`? **Answers:** safe / **unsafe** / safe.

Versioned releases + eval gates protect quality. Cost meters protect budget. Environment secrets protect the keys that pay for both.

---

## Key Takeaways

- Ship a **release bundle** — **prompt + tools + retrieval** under one version label, with `current.json` as the live pointer.
- Run a **pre-release eval gate** on the **golden set** before flipping the live version; block when regressions exceed the threshold.
- Track **tokens** and **cost per task** on a representative workload so a verbose prompt does not burn the campus budget.
- Keep **API keys** in **environment variables** / `.env` (gitignored) — never in notebooks, release JSON, or chat.
- Quality gate first, then cost, then secrets — all three belong in everyday LLM operations.

These habits turn “we changed a prompt” into a repeatable, safe release workflow you can trust.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| LLM Operations / LLMOps | Term | Version, gate, meter, and secure LLM apps |
| Release / release bundle | Term | Prompt + tools + retrieval under one version |
| Release versioning | Term | One label for the whole desk kit |
| `current.json` | Pattern | Pointer to the live version folder |
| Pre-release eval gate | Term | Golden-set ship check before deploy |
| Golden task set | Term | Frozen practice paper from previous work |
| Baseline vs candidate | Term | Live kit compared to proposed kit |
| Token | Term | Billing unit for model input/output text |
| Cost per task | Term | Estimated ₹ for one representative enquiry |
| Secret / API key | Term | Credential that must stay out of source |
| Environment variable | Term | Runtime value like `PARCEL_DESK_API_KEY` |
| `.env` + `.gitignore` | Practice | Local secrets file that never gets committed |
| `os.environ` | Library | Read secrets in Python without hard-coding |
| `json` / `pathlib.Path` | Library | Load release folders and golden JSON |
