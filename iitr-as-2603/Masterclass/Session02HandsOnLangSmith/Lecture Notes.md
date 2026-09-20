# LangSmith: LLM Application Evaluation and Monitoring

## Context of This Session

In **previous** work you treated **LangGraph** as a **workflow map**: **nodes**, **edges**, **shared state**, **checkpoints**, and **retries**. You sat **golden questions** on those graphs and read **execution order** after `invoke`.

That still answers a local question: *did this run look right on my laptop?* It does not answer *what nested step was slow, how many tokens it used, or whether yesterday’s prompt patch dropped quality for the whole team.* **LangSmith** is the evaluation and monitoring layer for those questions.

**What you will learn:**

- **Define** LangSmith and name **traces**, **spans**, **datasets**, **experiments**, **evaluators**, and **monitoring**
- **Turn on tracing** for a **LangGraph** desk without rewriting the graph
- **Read** a nested span tree for one T20 Match Desk run
- **Seed** a golden dataset, **run** an experiment, and **compare** v1 vs v2 after one patch
- **Watch** project-level **latency**, **tokens**, and **errors**

---

## What Is LangSmith

LangSmith is a **hosted platform** for tracing, evaluating, and monitoring LLM applications you already write as **LangGraph** workflows.

- **Official Definition:** **LangSmith** is an observability and evaluation product: it records **runs**, stores **datasets**, scores **experiments**, and shows **latency / token / error** trends for LLM apps (including LangGraph graphs).
- **In Simple Words:** A **control room** for your graph — not a new chatbot library.
- **Real-Life Example:** IRCTC already runs trains. A **control dashboard** shows which train is late and which route failed. LangSmith is that dashboard for graph runs.

You already know the *ideas*: print state after `invoke`, keep a golden list, compare before and after a prompt change. LangSmith’s job is to make those ideas **shared, nested, and measurable**.

| Block | Job in an app |
|---|---|
| **Trace** | One full user request, start to finish |
| **Span** | One step inside the trace (a node, an LLM call, a tool) |
| **Dataset** | Fixed exam paper of inputs + expected outputs |
| **Experiment** | One scored run of your app against that paper |
| **Evaluator** | A scoring rule (route match, keywords, or an LLM judge) |
| **Project** | Named folder of traces (`t20-langsmith-lab`) |
| **Monitoring** | Trends across many traces — not one printout |

- **Common mistake:** Treating LangSmith as “a new graph library.” It does **not** replace LangGraph. It **watches** the graph you already know how to draw.
- **Common doubt:** *“Did we not already sit a golden pack on the graph?”* Yes. Today that list becomes a **dataset**, and each case keeps a **full nested trace**.

---

## LangSmith and a Local Golden Pack — How They Differ

You already sit a **golden pack** on a graph (fixed inputs, expected route or keywords, print PASS / FAIL). Keep that habit. LangSmith does not delete it. It **hosts** the same exam and attaches **evidence** to every row.

![LangSmith sits above LangGraph as traces, evaluation, and monitoring](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session02-hands-on-langsmith/session02-01-langsmith-stack.png)

- **Official Definition:** A **local golden pack** is a script that loops golden cases and prints scores in the terminal. **LangSmith evaluation** stores those cases as a **dataset**, runs your graph as an **experiment**, and links each row to a **trace**.
- **In Simple Words:** Terminal score sheet vs **shared answer booklet with replays**.
- **Real-Life Example:** A teacher can tick answers on paper. A **digital exam portal** keeps every attempt, time taken, and which question was skipped — so two attempts can be compared.

| | **Local golden pack** | **LangSmith** |
|---|---|---|
| Where scores live | Your terminal | Dataset → Experiments in the UI |
| Nested LLM / node steps | Print `trace` / state after `invoke` | **Span tree** you can click |
| Latency and tokens | You print them yourself | Recorded on each span |
| Team compare | Paste a screenshot | **v1 vs v2** experiment table |
| Graph runs | Local logs only | Same project, nested automatically |

**Connecting idea:** Use a terminal golden pack when you are offline or writing the first three cases. Promote the same cases to LangSmith when you need **replay, tokens, and comparison**.

### Advantages of LangSmith

- **Nested truth** — see `classify` → `ChatGroq` → `lookup_incident`, not only the final string.
- **Same exam, many attempts** — v1 and v2 share one dataset; **monitoring** then shows error rate and latency across an evening of runs.
- **Works on the graph you already have** — `graph.invoke` records nested node and LLM spans when env vars are set.

### Disadvantages of LangSmith

- **Needs an account, a key, and a network path** — no traces without `LANGSMITH_API_KEY`; do not log secrets or personal data.
- **UI navigation** — experiment traces sit under **Datasets**, not only the project run list.
- **Overkill for a three-line Groq script** — a print is enough until you have a desk to debug.

### When to pick which

| Situation | Prefer |
|---|---|
| First golden list while coding | **Local golden pack** |
| Why did INC-102 call the rules node? | **LangSmith trace** |
| Did the prompt patch help or hurt? | **LangSmith experiment compare** |
| Is the desk getting slower this week? | **Monitoring** |

### Activity — Label the job

For each need, write **golden pack**, **trace**, **experiment**, or **monitoring**:

| Need | Your label |
|---|---|
| See that `classify` returned `incident` | |
| Score four golden questions after a prompt edit | |
| Print PASS/FAIL with no internet | |
| Notice p50 latency jumped from 2s to 8s | |

**Suggested answers:** trace · experiment · golden pack · monitoring

---

## Traces, Spans, and Nested Runs

A **trace** is one desk visit. A **span** is one station or helper inside that visit. Nested spans are how a LangGraph `invoke` appears in LangSmith.

- **Official Definition:** A **trace** is the root run for one invocation. A **span** is a child run (node, LLM call, or `@traceable` function) with its own inputs, outputs, latency, and token counts.
- **In Simple Words:** The **PNR** is the trace. Each station stamp is a span.
- **Real-Life Example:** A UPI payment id is one journey. App → bank → switch → merchant are nested hops. You debug the hop that failed, not the whole payment blindly.

![One T20 Match Desk run as a nested span tree with latency and tokens](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session02-hands-on-langsmith/session02-02-nested-trace.png)

LangGraph **nodes** become spans. **ChatGroq** inside a node becomes a child span. Functions marked **`@traceable`** nest under the node that called them.

- **Official Definition:** **`@traceable`** is a LangSmith decorator that records a Python function as a span and nests it in the current trace.
- **In Simple Words:** A name-badge for a helper so it shows up in the tree.
- **Real-Life Example:** The parcel desk stamps **“opened locker B”** — not only “handled parcel.”

- **Common mistake:** Looking only at the **project run list** after `evaluate()`. Experiment traces attach to the **dataset**. Open **Datasets → your dataset → Experiments**.
- **Common mistake:** Forgetting `LANGSMITH_TRACING=true` — the graph still runs; the control room stays empty.

---

## What You Will Build — T20 Match Desk Lab

The platform is defined. Now you apply it as **one lab**, not five disconnected demos.

| Part of the lab | Real-life role | Piece |
|---|---|---|
| **One graph invoke** | Prove keys and tracing | `run_desk(...)` |
| **Classify node** | Which counter? | ChatGroq → `rules` / `incident` / `refuse` |
| **Rules node** | Playing conditions | Short rulebook in the system prompt |
| **Incident node** | Scorer’s log | `@traceable` dict lookup for `INC-…` |
| **Dataset + experiment** | Same exam, scored attempt | Four cases; `route_match` + `keywords` |

- **Official Definition:** An **instrumented LangGraph desk** is a compiled graph whose every node and LLM call is recorded as nested spans, then scored against a dataset.
- **In Simple Words:** The same T20 desk you could already draw as a graph — now with a **replay and a score sheet**.
- **Real-Life Example:** A broadcast rules desk that can **replay** why it opened the incident log, then sit the **same four questions** after a script change.

> Rule text and incident records here are **teaching samples**, not official ICC documents.

Everything lives in **`t20_langsmith_lab.py`**.

| Phase | Focus | What you prove |
|---|---|---|
| **1 — Trace** | `demo_graph_trace()` | One `invoke` appears in the LangSmith project |
| **2 — Desk** | classify → branch → answer | Nested spans for three routes |
| **3 — Eval** | dataset + `evaluate()` | Scores + v1 vs v2 after one patch |

This lab does **not** add RAG or a second framework. The graph shape is what you already know. Today the new skill is **observability**. Any previous LangGraph file also traces if you export the same LangSmith env vars — you do not rewrite the graph.

---

## Before You Start — Setup

Reuse **Python 3**, a **venv**, and **`GROQ_API_KEY`**. Add a **LangSmith** account at [smith.langchain.com](https://smith.langchain.com), create an API key, and keep **both** keys in the environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core langchain-groq langgraph langsmith
export GROQ_API_KEY="your_key_here"
export LANGSMITH_API_KEY="your_key_here"
export LANGSMITH_TRACING=true
export LANGCHAIN_TRACING_V2=true
export LANGSMITH_PROJECT="t20-langsmith-lab"
```

| Name | Role |
|---|---|
| **`GROQ_API_KEY`** / **`LANGSMITH_API_KEY`** | ChatGroq calls / LangSmith auth — never commit either |
| **`LANGSMITH_TRACING=true`** | Send LangGraph runs |
| **`LANGCHAIN_TRACING_V2=true`** | Helps graph evaluation traces attach |
| **`LANGSMITH_PROJECT`** | Named folder (`t20-langsmith-lab`; else `default`) |
| **`langchain-core`**, **`langchain-groq`**, **`langgraph`**, **`langsmith`** | Prompt helper and `ChatGroq` inside nodes, `StateGraph`, `Client` / `evaluate` / `@traceable` |

Keep keys in the environment. Never paste them into the file. Do not put Aadhaar numbers, live tickets, or production secrets in traces.

Create **`t20_langsmith_lab.py`**, paste the file below, then run phases in order.

---

## The Complete App — `t20_langsmith_lab.py`

```python
# T20 Match Desk — LangSmith tracing + dataset experiment (one file, three phases)
import os  # Read API keys from the environment; never hard-code secrets
import re  # Pull INC-101 style ids out of the user question
from typing import TypedDict  # Describe shared graph state as named fields
from langchain_core.prompts import ChatPromptTemplate  # Reusable prompt with {variables}
from langchain_core.output_parsers import StrOutputParser  # Turn the model reply into a plain string
from langchain_groq import ChatGroq  # Groq chat model used inside graph nodes
from langgraph.graph import StateGraph, START, END  # Graph builder plus start and end sentinels
from langsmith import Client, evaluate, traceable  # Dataset client, experiment runner, span decorator

if not os.environ.get("GROQ_API_KEY"):  # Fail fast if Groq cannot be called
    raise RuntimeError("Set GROQ_API_KEY in the environment before running.")  # Do not start the desk without Groq
if not os.environ.get("LANGSMITH_API_KEY"):  # Fail fast if traces cannot be sent
    raise RuntimeError("Set LANGSMITH_API_KEY in the environment before running.")  # Do not pretend monitoring works without a key

os.environ["LANGSMITH_TRACING"] = "true"  # Force tracing on for this lab even if the shell had it unset
os.environ["LANGCHAIN_TRACING_V2"] = "true"  # Extra flag so graph evaluation traces attach reliably
os.environ.setdefault("LANGSMITH_PROJECT", "t20-langsmith-lab")  # Keep classroom traces in one named project unless already set

RULEBOOK = (  # Short teaching rulebook — production would retrieve this, not paste it
    "Powerplay (T20): overs 1-6; maximum 2 fielders outside the 30-yard circle. "  # Grounds the powerplay eval keyword 2
    "Free hit: after a no-ball; batter out only run out, hit twice, or obstruct. "  # Supports INC-102 wording
    "DRS: 2 unsuccessful reviews per innings. Penalty: 5 runs if bowler runs on protected pitch after warning."  # Grounds the DRS eval case
)  # Concatenated into the rules_node system prompt

INCIDENTS = {  # Live log the static rulebook does not contain
    "INC-101": "Match MI vs CSK, over 12.3: Bowler warned for running on the pitch. Penalty: 5 runs to batting side.",  # Pitch-running sample
    "INC-102": "Match RCB vs RR, over 8.1: Front-foot no-ball called. One run added; free hit on next delivery.",  # Eval incident — keywords no-ball, free hit
    "INC-103": "Match GT vs DC, over 15.4: DRS review upheld — batter out LBW. Batting team has 1 review remaining.",  # Extra live id
}  # INC-102 is the eval row; the others are for live queries

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)  # Classroom Groq model; temperature 0 for stabler routing


class DeskState(TypedDict):  # Shared notebook the graph nodes read and write
    question: str  # User text for this invoke
    route: str  # rules, incident, or refuse after classify
    answer: str  # Final student-facing string
    incident_id: str  # INC-xxx if present, else empty


@traceable(name="extract_incident_id")  # Nested span so the id parse is visible in the tree
def extract_incident_id(text: str) -> str:
    """Return INC-123 from the question, or empty string."""
    match = re.search(r"INC-\d+", text.upper())  # Normalise case so inc-102 still matches
    return match.group(0) if match else ""  # Empty string means incident_node will report a miss


@traceable(name="lookup_incident")  # Nested span for the dict hop (not an LLM call)
def lookup_incident(incident_id: str) -> str:
    """Return the scorer log row, or a clear miss message."""
    return INCIDENTS.get(incident_id, f"No incident found for {incident_id or 'missing id'}.")  # Dict lookup; missing id stays honest


def classify_node(state: DeskState) -> dict:
    """Station 1: choose rules, incident, or refuse. Does not write the final answer."""
    prompt = ChatPromptTemplate.from_messages([  # Classifier prompt — one word out
        ("system", "Classify the user question. Reply with exactly one word: rules, incident, or refuse. rules = T20 playing conditions. incident = live match INC-id. refuse = unrelated (FIFA, auctions, gossip)."),  # Tool-arbitration in one line
        ("human", "{question}"),  # Current user text
    ])
    raw = (prompt | llm | StrOutputParser()).invoke({"question": state["question"]}).strip().lower()  # Prompt plus ChatGroq inside the node — nested LLM span
    token = raw.split()[0].strip(".,:") if raw else "refuse"  # First token only if the model adds extra words
    route = token if token in {"rules", "incident", "refuse"} else "refuse"  # Unknown labels fail closed to refuse
    return {"route": route, "incident_id": extract_incident_id(state["question"])}  # Save route plus any INC id


def route_after_classify(state: DeskState) -> str:
    """Conditional edge: the route field is the next node name."""
    return state["route"]  # Must be rules, incident, or refuse — those keys are registered below


def rules_node(state: DeskState) -> dict:
    """Station 2a: answer from the short rulebook only."""
    prompt = ChatPromptTemplate.from_messages([  # Grounded explainer, not open-world cricket chat
        ("system", "Answer from this T20 rulebook only. Use digits for counts (write 2, not two). If the fact is not in the book, say you do not have that rule.\n" + RULEBOOK),  # Inline teaching corpus; digits keep keyword eval stable
        ("human", "{question}"),  # User question
    ])
    return {"answer": (prompt | llm | StrOutputParser()).invoke({"question": state["question"]})}  # Second LLM span on the rules path


def incident_node(state: DeskState) -> dict:
    """Station 2b: scorer log only — no LLM, so the span stays a dict lookup."""
    return {"answer": lookup_incident(state["incident_id"])}  # Uses the id classify already extracted


def refuse_node(state: DeskState) -> dict:
    """Station 2c: polite out-of-domain line. No tool, no rulebook."""
    return {"answer": "I can help only with T20 playing rules and match incident IDs (INC-xxx). Please ask about those."}  # Fixed string so refusal is stable in eval


builder = StateGraph(DeskState)  # Empty map that uses DeskState as the shared notebook
builder.add_node("classify", classify_node)  # Always the first station
builder.add_node("rules", rules_node)  # Playing-conditions counter
builder.add_node("incident", incident_node)  # Live log counter
builder.add_node("refuse", refuse_node)  # Safety counter
builder.add_edge(START, "classify")  # Every ticket starts at classify
builder.add_conditional_edges("classify", route_after_classify, {"rules": "rules", "incident": "incident", "refuse": "refuse"})  # Branch on the route field
builder.add_edge("rules", END)  # Each leaf finishes the graph
builder.add_edge("incident", END)  # Incident path does not fall through to rules
builder.add_edge("refuse", END)  # Refuse path does not call Groq again
graph = builder.compile()  # Runnable desk — LangSmith records this invoke as the root trace


def run_desk(question: str) -> dict:
    """One invoke with empty fields so nodes only write what they own."""
    return graph.invoke({"question": question, "route": "", "answer": "", "incident_id": ""})  # Fresh notebook per question


def demo_graph_trace() -> None:
    """Phase 1: one graph invoke. Proves Groq + tracing before the four live tickets."""
    out = run_desk("what is a free hit in T20")  # Smallest proof that the project receives a nested graph trace
    print("Phase 1 — one graph invoke (open project t20-langsmith-lab traces):\n", out["route"], "\n", out["answer"])  # Local print; the tree is in LangSmith


def demo_live_queries() -> None:
    """Four live tickets: rules, incident, refuse, DRS — then open the project traces."""
    queries = [  # Three routes plus a second rules question
        "During powerplay, how many fielders can stand outside the 30-yard circle?",  # Expect route=rules
        "What happened in incident INC-102?",  # Expect route=incident and lookup_incident span
        "Who won the FIFA World Cup?",  # Expect route=refuse
        "How many unsuccessful DRS reviews does a team get per innings in T20?",  # Expect route=rules and keyword 2
    ]  # Expect routes: rules, incident, refuse, rules
    for q in queries:  # Print a compact local log; the real tree is in LangSmith
        out = run_desk(q)  # Each call is one root trace in t20-langsmith-lab
        print(f"Q: {q}\n  route={out['route']}\n  answer={out['answer'][:180]}\n")  # Truncate for the terminal


DATASET_NAME = "t20-desk-golden"  # Stable name so v1 and v2 share the same paper

CASES = [  # Golden pack: empty keywords means score route only (not a fake PASS)
    {"question": "During powerplay in T20, how many fielders can be outside the 30-yard circle?", "route": "rules", "keywords": ["2"]},  # Digit 2 is in the rulebook
    {"question": "Tell me about match incident INC-102.", "route": "incident", "keywords": ["no-ball", "free hit"]},  # Exact phrases from the dict, not the LLM
    {"question": "Who won the FIFA World Cup?", "route": "refuse", "keywords": []},  # Empty keywords = N/A, not a fake PASS
    {"question": "How many unsuccessful DRS reviews does a team get per innings in T20?", "route": "rules", "keywords": ["2"]},  # Second rules case
]


def seed_dataset(client: Client):
    """Create the dataset once; skip example insert if rows already exist."""
    try:  # Re-runs should not create a second dataset with the same name
        ds = client.read_dataset(dataset_name=DATASET_NAME)  # Fetch if the student already seeded
    except Exception:  # First run: dataset is missing
        ds = client.create_dataset(dataset_name=DATASET_NAME, description="T20 Match Desk golden cases for LangSmith experiments")  # Named exam paper
    if next(client.list_examples(dataset_id=ds.id), None) is None:  # Insert only when the paper is empty
        client.create_examples(dataset_id=ds.id, inputs=[{"question": c["question"]} for c in CASES], outputs=[{"route": c["route"], "keywords": c["keywords"]} for c in CASES])  # Insert golden rows once
    return ds  # Caller runs evaluate against ds.name


def target(inputs: dict) -> dict:
    """Experiment wrapper: dataset inputs → desk outputs LangSmith can score."""
    out = run_desk(inputs["question"])  # Same function as live queries — no eval-only fork
    return {"answer": out["answer"], "route": out["route"]}  # Evaluators read these keys from run.outputs


def eval_route(run, example):
    """Score 1 if the predicted route matches the golden route."""
    predicted = (run.outputs or {}).get("route")  # What the desk actually chose
    expected = (example.outputs or {}).get("route")  # What the paper required
    return {"key": "route_match", "score": int(predicted == expected)}  # 1 or 0 for the experiment table


def eval_keywords(run, example):
    """Keyword hunt; empty list is N/A (refusal judged by route_match only)."""
    kws = (example.outputs or {}).get("keywords") or []  # Golden tokens
    if not kws:  # FIFA / refuse row
        return {"key": "keywords", "score": None, "comment": "N/A — refusal judged by route_match"}  # Not a fake PASS
    answer = ((run.outputs or {}).get("answer") or "").lower()  # Case-insensitive scan
    missing = [kw for kw in kws if kw.lower() not in answer]  # Tokens the answer skipped
    return {"key": "keywords", "score": int(len(missing) == 0), "comment": "ok" if not missing else f"missing={missing}"}  # 1 only when every token appears


def run_experiment(prefix: str) -> None:
    """Phase 3: seed the paper, score the desk, print where to open the UI."""
    client = Client()  # Uses LANGSMITH_API_KEY
    ds = seed_dataset(client)  # Idempotent seed
    results = evaluate(target, data=ds.name, evaluators=[eval_route, eval_keywords], experiment_prefix=prefix, max_concurrency=1)  # Sequential; traces hang off the dataset
    print("Phase 3 — experiment prefix:", prefix)  # Local banner
    print("Open LangSmith → Datasets →", ds.name, "→ Experiments (not only the project run list)")  # UI gotcha
    print(results)  # SDK summary; the clickable table is in the UI


if __name__ == "__main__":
    demo_graph_trace()  # Phase 1
    demo_live_queries()  # Phase 2
    run_experiment("t20-desk-v1")  # Phase 3 baseline
```

**How the code works**

- **Phase 1** — `run_desk` is one LangGraph `invoke`. Open project **`t20-langsmith-lab`**. If that trace is missing, env vars are wrong — do not debug routing yet.
- **Phase 2** — `classify` writes `route` and `incident_id`. The **conditional edge** sends the ticket to **one** leaf (`rules`, `incident`, or `refuse`).
- **Phase 2 continued** — Rules use the rulebook prompt. Incident uses **`@traceable`** lookup. Refuse returns a fixed sentence.
- **Phase 3** — `seed_dataset` creates the paper once. `evaluate()` calls `target` per row. Re-runs with `t20-desk-v2` share the same dataset.
- **Phase 3 scoring** — **`keywords` score is `None`** on the FIFA case so it is **not** counted as a keyword PASS.

- **Official Definition:** A **dataset** is a named set of example inputs and expected outputs. An **experiment** is one scored pass of a target function over that dataset, with **evaluator** columns on each row.
- **In Simple Words:** The **exam paper** stays fixed. Each sitting is a new score sheet.
- **Real-Life Example:** Before a UPI release, ops run the same four dispute queries and keep both score sheets.
- **Official Definition:** An **evaluator** is a function `(run, example) → {key, score}` that fills one experiment column (`route_match`, `keywords`).
- **In Simple Words:** The marking scheme for one kind of check.
- **Real-Life Example:** One examiner ticks “correct counter”; another ticks “digits 2 present.”

- **Common mistake:** Creating a **new dataset name** for v2 — then you cannot compare columns.
- **Common mistake:** Expecting RAG / Chroma in this file — they are intentionally absent so the lab stays on **tracing and eval**.

**Skipped on purpose:** RAG (not today’s skill), checkpointers (one-shot tickets; you already know resume), and LLM-as-judge (route + keywords are enough).

---

## Build Walkthrough — Tracing, Eval, Monitoring

### Reading a nested trace

After `demo_live_queries()`, open **smith.langchain.com** → project **`t20-langsmith-lab`**. Pick the INC-102 run. You should see root invoke → `classify` (child **ChatGroq**, `route=incident`) → `extract_incident_id` (`INC-102`) → `incident` → `lookup_incident` (text with **no-ball** and **free hit**). If `classify` chose **rules**, fix the **classifier system line** first — not the model size.

### Activity — Span table

Fill from the UI (not from memory):

| Query | Expected route | Spans you actually saw |
|---|---|---|
| Powerplay fielders | `rules` | |
| INC-102 | `incident` | |
| FIFA | `refuse` | |
| DRS quota | `rules` | |

### Activity — Trace any previous graph

Export the **same** LangSmith variables. Re-run a previous LangGraph `graph.invoke`. You should get traces **without changing that file**. That is the point of env-based instrumentation.

### Dataset, evaluators, and one patch

![Dataset rows flow through evaluate() into experiment scores you can compare after a patch](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session02-hands-on-langsmith/session02-03-dataset-experiment.png)

```bash
python3 t20_langsmith_lab.py
```

| Signature | Symptom in LangSmith | First fix |
|---|---|---|
| **Wrong route** | INC id span tree goes through `rules` | Sharpen classify system text (`INC-xxx`) |
| **Weak grounding** | Route is `rules` but keywords miss `2` | Tighten rulebook sentence for that fact |
| **Over-refusal** | Powerplay row route=`refuse` | Loosen classify; keep FIFA as refuse |
| **Empty project** | No Phase 1 trace | Check `LANGSMITH_TRACING` and the project name |
| **Empty experiment** | Project has live runs, Datasets tab is empty | You skipped Phase 3 or opened the wrong dataset |

**Activity — one patch:** Note `t20-desk-v1` `route_match` scores. Change **one** classify prompt line (or one rulebook sentence). In `__main__`, call `run_experiment("t20-desk-v2")`. Compare columns on the **same** dataset. If the score did not move, revert and pick a different **failure class**.

If Groq rate-limits `llama-3.1-8b-instant`, switch `model=` — same `ChatGroq` pattern.

### Monitoring — after many runs, not one print

- **Official Definition:** **Monitoring** is watching aggregate health of a project over time: **error rate**, **latency** (p50 / p99), **token usage**, and eval **pass rate**.
- **In Simple Words:** The **station dashboard**, not one PNR lookup.
- **Real-Life Example:** A UPI switch cares that p99 climbed this hour — not only that *your* last payment succeeded.

![Project monitoring tiles for errors, latency, tokens, and eval pass rate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/masterclass/session02-hands-on-langsmith/session02-04-monitoring-signals.png)

| Signal | Where to look | What a change means |
|---|---|---|
| **Errors** | Project filters | A node exception or missing key |
| **Latency p50** | Run table / monitor view | Typical wait; a sudden jump is a Groq or network stall |
| **Tokens** | LLM spans | Longer prompts or extra classify retries cost more |
| **Eval pass rate** | Experiment compare | Quality moved after your patch — or did not |

Live Phase 1–2 runs sit in the **project**; Phase 3 sits under **Datasets → Experiments** — both are LangSmith, two **different doors**.

---

## Confidence Checkpoint — Explain Without Looking

1. What is LangSmith for, in one sentence, compared with LangGraph?
2. What is the difference between a **trace** and a **span**?
3. Why can `evaluate()` traces be missing from the project run list?
4. Why is an empty keyword list scored as **N/A**, not PASS?
5. After a classify patch, what must stay the **same** so v1 and v2 are comparable?

If you can answer all five, you can put the same env vars on a UPI desk graph or a campus appointment graph and read the control room the same way.

---

## Key Takeaways

- **LangSmith** is the **control room** (traces, datasets, experiments, monitoring). **LangGraph** remains the **workflow map**.
- Set **`LANGSMITH_TRACING`**, **`LANGSMITH_API_KEY`**, and **`LANGSMITH_PROJECT`** — `graph.invoke` records nested spans without a rewrite; **`@traceable`** names extra Python hops.
- A **dataset** is the golden paper. An **experiment** is one sitting of that paper. Compare **v1 vs v2** after **one** patch.
- **Monitoring** is latency, tokens, and errors **across runs** — a local golden pack still prints one sitting.
- Next you can attach the same project to nodes that already use checkpoints and retries, and read **which station** failed instead of only that the graph failed.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| `t20_langsmith_lab.py` | File | One-file lab — graph trace, T20 desk, experiment |
| **LangSmith** | Platform | Tracing, evaluation, and monitoring for LLM apps |
| **Trace** | Concept | One full invocation (root run) |
| **Span** | Concept | One nested step (node, LLM, `@traceable`) |
| **`@traceable`** | Decorator | Record a Python function as a span |
| **Dataset** | Concept | Fixed inputs + expected outputs |
| **Experiment** | Concept | One scored pass over a dataset |
| **Evaluator** | Concept | Scoring function (`route_match`, `keywords`) |
| **Monitoring** | Concept | Errors, latency, tokens over many traces |
| `LANGSMITH_TRACING` | Config | `true` to send runs |
| `LANGSMITH_API_KEY` | Config | Auth — never commit it |
| `LANGSMITH_PROJECT` | Config | Project name (`t20-langsmith-lab`) |
| `LANGCHAIN_TRACING_V2` | Config | Helps LangGraph eval traces attach |
| `Client` | Class | Create/read datasets and examples |
| `evaluate()` | Function | Run the target + evaluators |
| `ChatGroq` / `StateGraph` | Class | Groq chat model inside nodes / LangGraph builder |
| `llama-3.1-8b-instant` | Model | Classroom Groq chat model |
| `max_concurrency=1` | Setting | Sequential experiment calls |
| **Golden pack** (contrast) | Concept | Local terminal loop of golden cases — promote the same cases to a dataset |
