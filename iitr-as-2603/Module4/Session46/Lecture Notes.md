# LLMOps: Evaluation Frameworks

## Introduction

In the **previous** session you practised **observability** and **tracing**: every parcel enquiry got an **AWB (trace id)**, desks wrote **structured JSON line** stamps, and you followed **retrieve → reason → act** to find the first break.

That shows *where* a single run failed. This session asks: *before we change the reply script (the prompt), how do we prove the new script is not worse?*

**Running story:** the same **campus parcel desk**. The clerk’s reply wording is the **prompt**. Before promoting a new script, you run a **golden checklist**, score replies **offline**, and **block promotion** if scores fall too far.

**What you will learn:**

- Author a **golden task set** of 5–10 tasks with **expected behaviours**
- Run an **offline eval** after each **material prompt** change
- Score with **pass / partial / fail** and record short notes
- **Block prompt promotion** when regressions exceed an agreed threshold

---

## Why Evaluation Belongs in LLMOps

You already know how to *read* one failed AWB. **LLMOps evaluation** is checking a fixed exam paper before you change the clerk’s script.

| Only tracing | Tracing + golden evaluation |
|---|---|
| “This one Amazon enquiry broke” | “Across 6 known questions, 2 now fail” |
| Fix after a student complains | Catch drops before the notice board goes live |

![Campus parcel desk comparison — only a vague Error happened note versus a golden checklist and score sheet for evaluation before changing the clerk script](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session46/session46-01-tracing-vs-golden-eval.png)

- **Official Definition:** **LLMOps** is operating LLM-powered systems with versioning, monitoring, and release discipline (like DevOps for model apps).
- **In Simple Words:** Treat prompts like software you release carefully — not a casual WhatsApp rewrite.
- **Real-Life Example:** A college website update goes through a checklist; you do not publish a broken fee page because “it looked fine once.”

- **Official Definition:** An **evaluation framework** (lightweight here) is a repeatable way to run fixed tasks, score outputs, and decide ship / no-ship.
- **In Simple Words:** Answer key + score sheet + pass rule for the desk.
- **Real-Life Example:** Driving test has fixed manoeuvres; you do not invent new tests every morning.

**Common doubt:** “Isn’t one happy demo enough?”  
No. One Amazon success can hide Flipkart or “not found” regressions.

### Activity — Name the Risk

You change the script to sound friendlier. Yesterday Amazon worked. Today Flipkart gets a wrong gate. What forces a re-check? **Answer:** a golden Flipkart task you always re-run after script changes.

---

## Golden Task Set = Desk Answer Key

A **golden set** is your fixed list of questions the desk must still handle well after any script edit.

- **Official Definition:** A **golden task set** (golden questions / golden tests) is a curated collection of representative inputs with expected behaviours used for regression checks.
- **In Simple Words:** The permanent practice paper for your agent.
- **Real-Life Example:** A canteen app always re-checks “veg thali”, “extra roti”, and “bill for table 4” after a menu text change.

![Golden task cards G01 to G06 on the campus parcel counter — frozen practice paper with expected behaviours and must-not warnings](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session46/session46-02-golden-task-set-answer-key.png)

**What each golden task should include**

| Field | Meaning at the parcel desk |
|---|---|
| `task_id` | Short label (e.g. `G01`) |
| `query` | Exact student question text |
| `expected_behaviours` | What a good reply must do / include |
| `must_not` | What a good reply must avoid |
| `tags` | Optional: `known_parcel`, `unknown`, `tone` |

**Authoring habits:** aim for **5–10** tasks; mix happy paths with edges; write **checkable** behaviours; freeze the set while comparing two prompts.

**Common error:** Demanding one exact sentence. Prefer behaviours (“mentions Gate 2”, “admits not found”) so small wording changes can still **pass**.

### Demo — author a golden set (six desk tasks)

```python
# Golden checklist for the campus parcel desk (answer key)
from pathlib import Path
import json


# Six fixed tasks — known parcels, unknown brand, empty input, wording variety
GOLDEN_SET = [
    {
        "task_id": "G01",
        "query": "Where is my Amazon box?",
        "expected_behaviours": ["Mentions Amazon or Amazon box", "Mentions Gate 2 or pickup"],
        "must_not": ["Invents a fake tracking number"],
        "tags": ["known_parcel", "amazon"],
    },
    {
        "task_id": "G02",
        "query": "Status of my Flipkart pouch?",
        "expected_behaviours": ["Mentions Flipkart", "Mentions hostel desk or held"],
        "must_not": ["Says ready at Gate 2"],
        "tags": ["known_parcel", "flipkart"],
    },
    {
        "task_id": "G03",
        "query": "Where is my Myntra packet?",
        "expected_behaviours": ["Admits parcel row not found OR cannot locate"],
        "must_not": ["Claims ready at Gate 2"],
        "tags": ["unknown"],
    },
    {
        "task_id": "G04",
        "query": "Amazon parcel please",
        "expected_behaviours": ["Gives a usable location hint", "Stays under 200 characters"],
        "must_not": ["Pastes the whole warehouse essay"],
        "tags": ["tone", "amazon"],
    },
    {
        "task_id": "G05",
        "query": "   ",
        "expected_behaviours": ["Asks for a brand or clearer question OR says cannot help"],
        "must_not": ["Pretends a random parcel is theirs"],
        "tags": ["edge"],
    },
    {
        "task_id": "G06",
        "query": "Is my Nykaa order here?",
        "expected_behaviours": ["Admits not found OR no register row"],
        "must_not": ["Invents Nykaa shelf location"],
        "tags": ["unknown"],
    },
]


if __name__ == "__main__":
    path = Path("golden_parcel_tasks.json")  # Freeze the answer key to disk
    path.write_text(json.dumps(GOLDEN_SET, indent=2), encoding="utf-8")
    print(f"Wrote {len(GOLDEN_SET)} golden tasks to {path}")
    for t in GOLDEN_SET:
        print(t["task_id"], "→", t["query"][:40])
```

**How the code works**

- Each dict is one exam question with **behaviours**, not one forced sentence.
- Saving to JSON freezes the set so prompt A and prompt B face the **same** paper.
- Six tasks sit in the 5–10 range; you can grow toward ten as the desk matures.

### Activity — Add One Golden Task

Write `G07` for “Where do I collect Amazon?” List two `expected_behaviours` and one `must_not`. Keep checks under 30 seconds.

---

## Offline Eval Run = Re-Take the Practice Paper

After any **material prompt change**, run the agent on the **whole** golden set — not on one cherry-picked question.

- **Official Definition:** An **offline evaluation run** executes fixed tasks against a candidate system without waiting for live user traffic.
- **In Simple Words:** Practise on the answer key before the real queue opens.
- **Real-Life Example:** Rehearse hostel announcements with sample notices before sending to WhatsApp.

![Empty campus queue while the parcel clerk runs an offline eval with Prompt A and Prompt B folders before the notice board goes live](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session46/session46-03-offline-eval-before-queue.png)

- **Official Definition:** A **material prompt change** is an edit that can change behaviour — not a typo in a comment.
- **In Simple Words:** If a student might get a different answer, re-run the golden set.
- **Real-Life Example:** Changing “Gate 2” to “Gate 5” is material; renaming a log file is not.

**Desk rule:** New script → offline eval on all golden tasks → only then consider promotion.

### Full code — tiny agent + offline runner

```python
# Offline eval: run every golden query through two reply scripts (prompts)
import json
from pathlib import Path

# Tiny register — same campus book idea as earlier desk work
PARCELS = {
    "amazon": "Amazon box for Riya — ready at Gate 2 pickup.",
    "flipkart": "Flipkart pouch for Aman — held at hostel desk.",
}

# Look up a row from the query text
def retrieve(query: str) -> str:
    q = query.lower().strip()  # Normalise for simple matching
    if not q:
        return ""  # Empty question → no row
    if "amazon" in q:
        return PARCELS["amazon"]
    if "flipkart" in q:
        return PARCELS["flipkart"]
    return ""  # Unknown brand

# Prompt A — careful, honest clerk script
PROMPT_A = {
    "name": "prompt_a_careful",
    "found": "{row}",  # Use register text as-is
    "missing": "Sorry — no parcel row found for that brand. Please check the label.",
    "empty": "Please tell the brand name on your parcel slip.",
}

# Prompt B — overconfident script (will regress on unknowns)
PROMPT_B = {
    "name": "prompt_b_overconfident",
    "found": "{row}",
    "missing": "Your parcel is ready at Gate 2 pickup.",  # Wrong for unknowns!
    "empty": "Your parcel is ready at Gate 2 pickup.",  # Also wrong
}

# Apply one prompt script to a register row
def reply_with_prompt(query: str, prompt: dict) -> str:
    row = retrieve(query)  # Desk lookup
    if not query.strip():
        return prompt["empty"]  # Empty input branch
    if not row:
        return prompt["missing"]  # Unknown brand branch
    return prompt["found"].format(row=row)  # Known row branch

# Run one full offline pass over the golden JSON file
def run_offline_eval(golden_path: Path, prompt: dict) -> list:
    tasks = json.loads(golden_path.read_text(encoding="utf-8"))  # Load answer key
    rows = []
    for task in tasks:
        answer = reply_with_prompt(task["query"], prompt)  # Candidate reply
        rows.append({
            "task_id": task["task_id"],
            "query": task["query"],
            "prompt_name": prompt["name"],
            "reply": answer,
            "expected_behaviours": task["expected_behaviours"],
            "must_not": task.get("must_not", []),
        })
    return rows

if __name__ == "__main__":
    golden = Path("golden_parcel_tasks.json")  # From the authoring demo
    for prompt in (PROMPT_A, PROMPT_B):
        results = run_offline_eval(golden, prompt)
        out = Path(f"eval_{prompt['name']}.json")
        out.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"Wrote {len(results)} offline results → {out}")
```

**How the code works**

- `retrieve` is the parcel-book idea; the **prompt dict** is the clerk script under test.
- Prompt B lies on missing/empty cases — that will show as **regressions** later.
- Offline run writes one JSON file per prompt for scoring.

### Activity — When Must You Re-Run?

Mark material or not: (1) change “Gate 2” to “Gate 5” in `found`; (2) rename a log file; (3) rewrite `missing` to sound friendlier. **Answers:** material / not material / material.

---

## Qualitative Scoring = Pass / Partial / Fail Rubric

Offline results are not useful until you **score** them. Keep the rubric simple so any teammate can apply it in minutes.

- **Official Definition:** **Qualitative scoring** judges outputs against expected behaviours using human (or rule-assisted) judgement rather than only automated metrics.
- **In Simple Words:** Tick the answer key behaviours; write a short note.
- **Real-Life Example:** Lab viva marks — full / half / zero — with one line of examiner comment.

**Rubric used at this desk**

| Score | Meaning | Desk feel |
|---|---|---|
| **pass** | All expected behaviours met; no `must_not` broken | Ready to post |
| **partial** | Some behaviours met; minor gap or soft risk | Needs a small fix |
| **fail** | Misses core behaviour or invents a wrong location | Do not promote |

![Score sheet at the parcel desk with PASS, PARTIAL, and FAIL stamps plus a one-line examiner note about inventing Gate 2](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session46/session46-04-pass-partial-fail-rubric.png)

**Scoring steps**

1. Read `reply` for one `task_id`.
2. Check each expected behaviour — yes / no.
3. Check each `must_not` — broken or safe.
4. Assign **pass / partial / fail** and write a **one-line note**.

### Full code — rule-assisted scorer + notes sheet

```python
# Score offline replies with pass / partial / fail and short notes
import json
from pathlib import Path

# Tiny helper: does the reply mention any of these words?
def mentions(text: str, words: list) -> bool:
    t = text.lower()  # Compare in lowercase
    return any(w.lower() in t for w in words)  # True if any word appears

# Heuristic checks tied to our golden behaviours (teaching demo)
def score_one(row: dict) -> dict:
    reply = row["reply"]  # Candidate text to judge
    tid = row["task_id"]  # Which golden item
    notes = []  # Short examiner comments
    score = "fail"  # Default until proven better

    if tid in ("G01", "G04"):  # Amazon family
        ok_brand = mentions(reply, ["amazon"])
        ok_place = mentions(reply, ["gate 2", "pickup"])
        if ok_brand and ok_place:
            score = "pass"
        elif ok_brand or ok_place:
            score = "partial"
            notes.append("Amazon hint incomplete")
        else:
            notes.append("Missing Amazon / Gate 2 cues")

    elif tid == "G02":  # Flipkart
        ok = mentions(reply, ["flipkart", "hostel"])
        wrong_gate = mentions(reply, ["gate 2"]) and not mentions(reply, ["hostel"])
        if ok and not wrong_gate:
            score = "pass"
        elif ok:
            score = "partial"
            notes.append("Flipkart ok but Gate 2 risk")
        else:
            notes.append("Missing Flipkart / hostel cues")

    elif tid in ("G03", "G06"):  # Unknown brands must stay honest
        honest = mentions(reply, ["not found", "no parcel", "cannot", "check the label"])
        invents = mentions(reply, ["gate 2", "ready"])
        if honest and not invents:
            score = "pass"
        elif invents:
            score = "fail"
            notes.append("Invented a location for unknown brand")
        else:
            score = "partial"
            notes.append("Unclear unknown handling")

    elif tid == "G05":  # Empty query
        asks = mentions(reply, ["please", "brand", "tell", "cannot"])
        invents = mentions(reply, ["gate 2", "ready"])
        if asks and not invents:
            score = "pass"
        elif invents:
            score = "fail"
            notes.append("Pretended a parcel exists for blank input")
        else:
            score = "partial"
            notes.append("Weak empty-input handling")

    if len(reply) > 200 and score == "pass":
        score = "partial"
        notes.append("Reply longer than 200 chars")

    return {
        "task_id": tid,
        "prompt_name": row["prompt_name"],
        "score": score,
        "note": "; ".join(notes) if notes else "Looks aligned",
        "reply": reply,
    }

def score_file(eval_path: Path) -> list:
    rows = json.loads(eval_path.read_text(encoding="utf-8"))  # Load offline results
    return [score_one(r) for r in rows]  # One score row per task

if __name__ == "__main__":
    for name in ("prompt_a_careful", "prompt_b_overconfident"):
        scored = score_file(Path(f"eval_{name}.json"))
        out = Path(f"scores_{name}.json")
        out.write_text(json.dumps(scored, indent=2), encoding="utf-8")
        summary = {s: sum(1 for x in scored if x["score"] == s) for s in ("pass", "partial", "fail")}
        print(name, "→", summary)
```

**How the code works**

- Rules encode golden behaviours in a teaching-friendly way (you can still score by hand).
- Each result stores **score** + **note** — the qualitative paper trail.
- Printing pass/partial/fail counts makes the two prompts easy to compare.

### Activity — Score This Reply by Hand

Task G03 expected: admit not found; must not claim Gate 2.  
Reply: `"Your parcel is ready at Gate 2 pickup."`  
Your score? **Answer:** **fail** — invents a location for an unknown brand.

---

## Regression Habit and Promotion Gate

Scoring once is not enough. The desk needs a **regression habit**: compare the new script to the last accepted script, and **block promotion** when drops exceed a threshold.

- **Official Definition:** A **regression** is a case that used to meet the bar and now scores worse after a change.
- **In Simple Words:** Something that worked on yesterday’s answer key now fails.
- **Real-Life Example:** After a “friendlier” fee notice, the payment link disappears — friendliness caused a regression.

- **Official Definition:** A **promotion gate** (ship rule) blocks releasing a new prompt/version until eval results stay within an agreed threshold.
- **In Simple Words:** Do not put the new script on the notice board if the score sheet got worse beyond your limit.
- **Real-Life Example:** Hostel mess will not print a new weekly menu if more than one allergen line is wrong on the proof.

![Promotion gate blocking an overconfident new script from the student notice board while the baseline careful script stays live](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session46/session46-05-promotion-gate-block.png)

**Agreed threshold example (starting policy)**

| Rule | Meaning |
|---|---|
| Fail count ≤ 1 | At most one hard fail on the golden set |
| No new fails vs baseline | A task that was `pass` must not become `fail` |
| Partial count ≤ 2 | Soft gaps allowed but limited |

If any rule breaks → **block promotion**, keep the old prompt live, fix, re-run offline eval.

### Full code — compare scores and block promotion

```python
# Promotion gate: block new prompt if regressions exceed threshold
import json
from pathlib import Path

# Load score sheet produced by the scorer
def load_scores(path: Path) -> dict:
    rows = json.loads(path.read_text(encoding="utf-8"))
    return {r["task_id"]: r for r in rows}  # Index by task_id

# Count score labels
def count_label(scores: dict, label: str) -> int:
    return sum(1 for r in scores.values() if r["score"] == label)

# Detect tasks that got worse vs baseline
def regressions(baseline: dict, candidate: dict) -> list:
    order = {"pass": 2, "partial": 1, "fail": 0}  # Higher is better
    bad = []
    for tid, base in baseline.items():
        cand = candidate.get(tid)
        if cand and order[cand["score"]] < order[base["score"]]:
            bad.append({"task_id": tid, "from": base["score"], "to": cand["score"], "note": cand.get("note", "")})
    return bad

# Apply the desk promotion policy
def promotion_decision(baseline: dict, candidate: dict) -> dict:
    fails = count_label(candidate, "fail")
    partials = count_label(candidate, "partial")
    regs = regressions(baseline, candidate)
    reasons = []
    if fails > 1:
        reasons.append(f"fail count {fails} exceeds threshold 1")
    if partials > 2:
        reasons.append(f"partial count {partials} exceeds threshold 2")
    if regs:
        reasons.append(f"{len(regs)} regression(s) vs baseline")
    return {
        "promote": len(reasons) == 0,
        "reasons": reasons or ["Within threshold — ok to promote"],
        "regressions": regs,
        "candidate_summary": {"pass": count_label(candidate, "pass"), "partial": partials, "fail": fails},
    }

if __name__ == "__main__":
    baseline = load_scores(Path("scores_prompt_a_careful.json"))
    candidate = load_scores(Path("scores_prompt_b_overconfident.json"))
    decision = promotion_decision(baseline, candidate)
    print(json.dumps(decision, indent=2))
    print("PROMOTE" if decision["promote"] else "BLOCK — keep baseline on the notice board")
```

**How the code works**

- Baseline = last accepted script (Prompt A). Candidate = Prompt B.
- Any score drop is a **regression**; too many fails/partials also block.
- Overconfident Prompt B should print **BLOCK**.

**Avoid:** Promoting because “G01 still passes”; editing golden tasks to match a bad prompt.

### Activity — Apply the Gate

Baseline: 5 pass, 1 partial, 0 fail. Candidate: 3 pass, 1 partial, 2 fail (G03 and G05 newly failed). Promote? **Answer:** **Block**.

Observability (**previous** session) explains one broken AWB. **Golden evaluation** protects the whole desk script before students see it.

---

## Key Takeaways

- Build a **golden task set** (5–10) with checkable **expected behaviours** and clear **must_not** lines.
- After every **material prompt** change, run an **offline eval** on the full set — not one lucky demo.
- Score with **pass / partial / fail** and keep a one-line **note** per task.
- Use a **promotion gate**: block the new prompt when fails, partials, or regressions exceed the agreed threshold.
- Pair with tracing: logs explain a single miss; golden eval prevents silent desk-wide drops.

These checks prepare you to change prompts with evidence, not hope.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| LLMOps | Term | Operate LLM apps with release discipline |
| Evaluation framework | Term | Repeatable tasks + scores + ship rule |
| Golden task set | Term | Fixed 5–10 tasks with expected behaviours |
| Offline eval run | Term | Re-run golden tasks without live traffic |
| Material prompt change | Term | Edit that can change student-facing answers |
| Qualitative scoring | Term | Human/rule judgement vs behaviours |
| pass / partial / fail | Rubric | Simple three-level desk scores |
| Regression | Term | A case that got worse after a change |
| Promotion gate / threshold | Term | Block ship when score sheet breaks policy |
| Baseline prompt | Term | Last accepted script used for comparison |
| `json` / `pathlib.Path` | Library | Save and read desk JSON files |
| Prompt dict (A/B) | Pattern | Candidate clerk scripts under test |
