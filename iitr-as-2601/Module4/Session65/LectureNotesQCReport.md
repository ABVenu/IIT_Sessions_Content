# Lecture Notes QC Report — Session 65 (Capstone Build, 2.5 h)

Two-meeting redesign. Source of truth for content: Session 62 (unchanged). Extra contact time is lab, not new libraries.

## Iteration 1 — Fork from Session 62

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Scenario, architecture, LangGraph, G01–G03, fail closed; lab-order section added |
| Creativity | 5 | Passport seva + metro stations |
| Structural Adherence | 5 | previous/upcoming only |
| No Logical Mistakes | True | Inherited 62 gates (GST before PO; Python `AMOUNT_GATE`) |
| Pedagogical flow | False | Agenda interleaved labs; notes were a theory dump with a checklist at the end. No copyable `scripts/seed.py` for a 40-min seed lab. Eval snippet never called `write_trace` but “Build done” required JSONL lines. Duplicate-gate hint could break G01 (no `bill_date`). |

## Iteration 2 — Logical + pedagogical flow QC

### Flow 65 → 66 (what must stay true)

| Carry forward | Check |
|---|---|
| Same product, no NEFT | Pass — freeze + bank floor absent |
| Graph before window | Pass — Streamlit still “next meeting”; early-finish is G04 INJECT |
| G01–G03 on `graph.invoke` | Pass — eval uses the compiled graph |
| Chroma fail-closed | Pass — empty hits → `empty_policy` before GST |
| Dummy GSTINs; never seed `99INVALID` | Pass |
| Next meeting is window **and** handover | Pass — takeaways and preread agree |

### Logical findings (and fixes)

| Finding | Severity | Fix applied |
|---|---|---|
| `InvoicePacket` comment said `ingested`; nodes write `extracted` / `ok_for_route` | Low | Comment aligned |
| Architecture listed `log_event`; code is `write_trace` in `app/log.py` | Medium | Table and folder map aligned |
| `eval/run_golden.py` never wrote JSONL; “three diary lines” could not happen | High | Runner calls `write_trace` |
| `write_trace` opened `logs/paydesk.jsonl` with no `mkdir` | High | `Path("logs").mkdir(exist_ok=True)` |
| Duplicate-ticket habit invited a live gate G01–G03 cannot pass | Medium | Explicitly **not** a live gate today |
| 40-min Lab A had SQL sketch only; copyable seed lived in old Session 64 | High | `scripts/seed.py` now in this meeting |

**Still true (kept on purpose):** GST checked before PO so G03 stays `gst_mismatch`. Amount gate is Python. Eval does not inject handbook chunks. `tickets` / `events` tables are sketched, not wired — diary is JSONL; do not make students build a second register in Lab A.

### Pedagogical findings (and fixes)

| Finding | Severity | Fix applied |
|---|---|---|
| Timed agenda is freeze → map → walkthrough → **Lab A** → guardrails → **Lab B**. Notes taught all theory then lab | High | Live pause **Lab A** after seed script; **Lab B** after golden runner |
| Lab A pause sat *before* the seed script (students told to run a file they had not seen) | High | Pause moved to after Empty-Shelf activity |
| Extra 40 min vs old Build looked like “more lecture” | Medium | Extra time named as lab in metadata, flow, and pauses |

### Residual (do not “fix” in this meeting)

- `retrieve_policy` query is a fixed string — enough for a three-line handbook; not a production retriever.
- PO vendor is not matched to invoice vendor — out of live G01–G03.
- Mental map still says “Upcoming **Module**” for the next meeting (house style; 66 is the same module).
- Diagrams reuse Session 62 S3 URLs until 65 PNGs exist.

### Scores after Iteration 2

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Metadata LOs covered; seed + eval now runnable |
| Creativity | 5 | |
| Structural Adherence | 5 | ~594 lines (540–600); previous/upcoming only; no session numbers in student notes |
| No Logical Mistakes | True | After eval/log/seed/status fixes |
| Pedagogical flow | True | Lab A / Lab B match the 150-min agenda; Streamlit still forbidden |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |
| Taught-stack only | True | |

Expected QC result achieved after Iteration 2.

## Iteration 3 — Full-curriculum coverage

See `Curriculum-Coverage-QC.md` in this folder (CSV Sessions 1–64 vs 65/66).

**Verdict:** 65/66 meet the CSV capstone contract (M3–M4 on one scenario) with a thin golden set. They do **not** contain every Module 1–2 lab. Faculty map is in `Capstone Flow.md`.

