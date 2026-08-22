# Curriculum Coverage QC — Sessions 65 & 66 vs `iitr-as-2601 - detailed_curriculum.csv`

**Question:** Do the last two capstone meetings contain all course learnings?

**Short answer:** **No, not all 64 sessions.** **Yes, they cover the official capstone contract** in the same CSV: Session 62’s objective is *“Build an integrated autonomous agent that applies **M3–M4 skills** on a chosen scenario.”* Module 1 is used as craft. Module 2 is not a second product inside PayDesk.

Source of truth: `Command Center/Curriculums/IITR-AS-2601/iitr-as-2601 - detailed_curriculum.csv` (Sessions 1–64). 65/66 replace calendar 62–64 as the two 2.5 h meetings.

---

## Official capstone LOs (CSV rows 62–64) → 65/66

| CSV LO | 65 | 66 | Verdict |
|---|---|---|---|
| Select scenario with users, data, success | Live | — | Pass |
| One-page architecture: RAG, tools, memory, orchestration, deploy path | Live | Deploy path built | Pass |
| Core flows with versioned prompts | Live (`extract_v1.txt` + labelled path) | Stretch A uses the same packet | Pass (live extract is labels, not the LLM) |
| Integration tests from golden set (S57) | G01–G03 live | Same paper + UI same door | **Partial** — CSV S57 asks **5–10** tasks; live paper is **3** (+ G04/G05 only if time) |
| Improve UI from peer feedback | — | Streamlit | Pass |
| Token/cost for a demo path | Named | `docs/cost_note.md` | Pass (honest zeros if labelled) |
| Live demo with traces | — | CLEAN + HIGH + JSONL | Pass |
| Retro, no SLI/SLO | — | `docs/retro.md` | Pass |
| Submission checklist, README, evals | Seed script started | Pack + partner review | Pass |
| One stretch if core stable | Forbidden today | A / B / C / none | Pass |

---

## Module 3–4 (what the CSV says the capstone must apply)

Legend: **Live** = required on the submit path. **Stretch** = only if G01–G03 pass. **Named** = spoken/written, not coded. **Out** = not on PayDesk.

| CSV # | Title | In 65/66? | How / gap |
|---|---|---|---|
| 35 | GenAI concepts (tokens, hallucinations) | Named | Fail-closed and confidence. Tokens billed in 66. Hallucination not named as a term. |
| 36 | Prompt engineering (system/user, few-shot, CoT) | **Partial** | `extract_v1.txt` is a system script. Live G01–G03 **do not call a model**. Few-shot / CoT **out**. |
| 37 | Open-source LLMs / **Ollama** | **Out** | Product uses optional **Groq**. Ollama never appears. |
| 38–41 | RAG: ingest, chunk, embed, Chroma, retrieve, ground | **Live** | `seed_policy()` + `retrieve_policy`. Weak vs 40: no overlap strategy, no PDF loader. Weak vs 41: RAG is **evidence quotes**, not a generated answer. |
| 42 | Memory, loop stop, error handling | **Live** | Graph state + sqlite + JSONL; graph ends at `END`. Compaction **out**. |
| 43 | Agent **tool use** (model selects tools) | **Partial** | GST / PO / retrieve are **Python calls from `policy_node`**, not an LLM function-calling loop. Schema-bound model tools **out** of the live path. |
| 44 | Tokens, temperature, context limits | **Partial** | Stretch A `temperature: 0`. Cost note. Context-window design **out**. |
| 45 | Prompt versioning, rate limits, retries | **Partial** | `prompt_version` **live**. Rate-limit / exponential backoff **named** (429) not implemented. |
| 46 | Structured JSON outputs | **Partial** | `InvoicePacket` live. Model JSON parse is **stretch A**. Live bills are labelled lines. |
| 47 | RAG workshop | **Live** | Same Chroma shelf, smaller corpus (`policy.md`). |
| 48 | Safety & guardrails | **Live** | Injection (G04), Python gates, pay-tool allow-list. |
| 49 | Chunking & metadata filters | **Partial** | `source_id=policy.md` on add. **No** metadata filter on query, **no** re-index drill. |
| 50 | Retrieval tuning (top-k experiments, hit rate) | **Out** | `k=3` fixed. No before/after retrieval eval. Empty shelf is the only retrieval failure class. |
| 51 | Memory architecture, compaction, PII | **Partial** | Three drawers live. PII: no PAN in JSONL. **Compaction out.** |
| 52 | Planner–executor, JSON contracts, stop | **Live** (unnamed) | extract → policy → route + `InvoicePacket` + `needs_human`. Word “planner” rarely used. |
| 53 | LangGraph basics | **Live** | Core of 65. |
| 54 | Checkpoints & resume | **Stretch B** | Not on the submit bar. |
| 55 | Timeouts & retries | **Partial** | Stretch A `timeout=30`. Bounded retries / backoff **out**. |
| 56 | Observability / JSONL | **Live** | `write_trace` on eval and UI. |
| 57 | Golden set 5–10 tasks | **Partial** | **3 live.** Paper extras G04/G05. Below CSV count. |
| 58 | Eval gates, cost, secrets | **Live** | Re-golden after prompt change; `.env`; cost sticky. |
| 59 | Streamlit UI | **Live** (66) | Same `graph.invoke`. |
| 60 | FastAPI facade & hosting | **Out of core** | Notes **forbid** a second HTTP hatch. Hosting is a local-vs-public **warning**, not a PaaS lab. |
| 61 | Cache, rate limits, queue, cost log | **Partial** | Cache **rule** live (retrieve yes / `ready_to_pay` no). GST cache = stretch C. Per-session rate limiter and queue **not built** on PayDesk. |

---

## Module 1 (craft the desk uses)

| CSV # | Title | In 65/66? |
|---|---|---|
| 1 | AI vs ML vs GenAI landscape | Named only (new product, not a model bake-off) |
| 2–3 | Lab, VS Code, secrets, Git, CLI, scripts vs notebooks | **Live** — `.env`, `.gitignore`, `scripts/seed.py`, not a notebook desk |
| 4–9 | Python syntax, files, functions | **Live** — entire PayDesk |
| 10–11 | NumPy | **Out** as a student skill (embeddings library uses arrays internally) |
| 12 | JSON | **Live** — packet + JSONL + stretch parse |
| 13–15 | Pandas | **Out** |
| 16–18 | SQL | **Partial** — `sqlite3` SELECT / INSERT, not JOIN/ORDER BY coursework |
| 19–21 | Matplotlib / EDA | **Out** |
| 22–23 | APIs, status codes, env keys, privacy | **Partial** — stretch A `urllib` + `.env`; no Requests lab |
| 24 | EDA workshop / Streamlit demo | **Live** as Streamlit habit (59/66), not a Pandas dashboard |

---

## Module 2 (ML)

| CSV # | Title | In 65/66? |
|---|---|---|
| 25–34 | Workflow, leakage, regression, classification, trees, clustering, PCA, time series, model selection | **Out of the product** |

What *does* transfer: **eval thinking** — freeze a paper, do not leak the answer into the packet, re-run after a change, missed-gate rate = 0. That is S25/S27/S57 habit, not a scikit-learn model.

Putting Linear Regression or K-Means **inside** Nimbus PayDesk would violate the CSV capstone (M3–M4 agent on one money-harm scenario) and the no-NEFT product.

---

## Scores

| Check | Result |
|---|---|
| CSV capstone LOs (rows 62–64) in 65+66 | **Pass with one hole** (golden set size 3 vs 5–10) |
| Every **M3–M4** skill **live** on the submit path | **Fail** — several are stretch, named, or out (Ollama, FastAPI, retrieval-tuning lab, LLM tool-calling loop, compaction, retries, 5–10 goldens) |
| Every **M1–M2** session re-taught as a lab | **Fail** (correctly) — M2 models and M1 EDA/NumPy/Pandas are not this product |
| Student can **point at** M3–M4 on the desk in an exam | **Partial** — wrap table lists gates/RAG/graph/UI/cost; does not walk Ollama, FastAPI, S50 tuning, S54 checkpoint unless stretch B |

---

## What would have to change if “all course learnings” meant *live code*

Do **not** do this in 5 hours. It would be a third product.

If the bar is “M3–M4 **visible** on submit, not optional”:

1. Golden paper: add G04 INJECT and G05 EMPTY as **required** (closes S57 count toward 5).
2. Live extract: one messy bill through Groq JSON (S36/S46) **in addition to** labelled G01–G03 — currently stretch A.
3. Checkpoint stamp **or** timeout/retry on Groq — currently stretch B / missing retries (S54/S55).
4. Do **not** add Ollama + FastAPI + Pandas + sklearn. Those fight the taught-stack table and the 150-minute clocks.

---

## Recommendation

Keep PayDesk as the **integration exam** for M3–M4, with M1 as the programming craft and M2 as the eval mindset.

Treat “all learnings in 65/66” as: **every M3–M4 session has a named home** (live, stretch, or explicit out-of-product with a reason), not as **re-running Sessions 1–34**.

Faculty map lives in `Capstone Flow.md` (same folder). Student exam map: Session 66 wrap table **Where this course shows up**.
