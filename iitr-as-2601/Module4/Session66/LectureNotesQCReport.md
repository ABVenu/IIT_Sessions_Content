# Lecture Notes QC Report — Session 66 (Polish, Demo & Submit, 2.5 h)

Two-meeting redesign. Merges Session 63 (Polish & Demo) and Session 64 (Buffer & Submission). Those folders are unchanged reference.

## Iteration 1 — Merge 63 + 64 into one 2.5 h meeting

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | All eight metadata LOs present |
| Creativity | 5 | Courier counter + passport file |
| Structural Adherence | 5 | ~630 lines |
| No Logical Mistakes | False | See Iteration 2 |
| Pedagogical flow | False | Partner swap before seed; no cold-start of the graph; sample buttons did not fill the text area; two reviews in one squeezed meeting |

## Iteration 2 — Logical + pedagogical flow QC

### Flow 65 → 66 (what must stay true)

| Carry forward from 65 | Check |
|---|---|
| Same `graph.invoke` as golden | Pass — UI imports `app.graph` |
| Re-seed sqlite **and** Chroma | Pass — README + `scripts/seed.py` (never `99INVALID`) |
| No second brain / no NEFT | Pass |
| Cache retrieve, not `ready_to_pay` | Pass — cost note + stretch C |
| Stretch only after G01–G03 | Pass — default under the clock is **none** |
| Overnight laptop / empty `.chroma` | Was fail — 66 opened on widgets. **Fix:** first move is re-run golden; if G02 is not `amount_gate`, do not polish |

### Logical findings (and fixes)

| Finding | Severity | Fix applied |
|---|---|---|
| Load CLEAN/HIGH set `st.session_state["raw"]` but `text_area` had no `key="raw"` — buttons did not fill the box | High | Buttons + `key="raw"` in the same `app_ui.py` |
| UI `invoke` did not call `write_trace`; “Match the Line” activity could not pass | High | `write_trace(packet)` after invoke |
| Flow sheet said “CLEAN vs HIGH on a **small** receipt” — HIGH is ₹90,000 | Low | “two scripted bills” |
| Partner Cold Start sat **before** `scripts/seed.py` — README says seed, partner has no command yet | High | Early swap removed; scored swap is Cross-team Review after seed |

**Still true (kept on purpose):** G03 optional on stage; CLI golden is demo fallback; stretch A/B/C use taught stack only; human cannot self-stamp.

### Pedagogical findings (and fixes)

| Finding | Severity | Fix applied |
|---|---|---|
| 8 LOs in 150 min (old plan had ~220 min) | High | Stretch default **none**; handover beats a second product |
| Two partner rituals (Cold Start + Cross-team Review) | Medium | One scored swap at the end |
| Retro “more time” lists Groq/stamp, then stretch offers them 15 min later | Low | Stretch only if golden **and** seed command already exist |
| Opening assumed 65 state still on disk | High | Re-run `eval/run_golden.py` before Streamlit |

### Residual (clock, not a content hole)

- Cross-team review is 15 minutes for seed + G01–G03 + “UI does not say paid.” If README is weak, that block overruns wrap. Instructors should start the swap even if stretch is skipped.
- Stretch A (Groq extract) cannot honestly finish in 15 minutes. Notes already say skip. Do not treat stretch as a required LO on submit day.
- Seed script is duplicated from 65 on purpose — 66 is the handover copy a stranger needs.
- Diagrams reuse Session 63/64 S3 URLs until 66 PNGs exist.

### Scores after Iteration 2

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Metadata LOs covered; stretch optional under the clock |
| Creativity | 5 | |
| Structural Adherence | 5 | ~629 lines (620–680); previous/upcoming only |
| No Logical Mistakes | True | After widget-key, `write_trace`, seed-before-review |
| Pedagogical flow | True | Graph proven first; window; evidence; pack; one review; skip stretch if behind |
| No Presentation Mistakes | True | Duplicate sample-button snippet removed |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |
| Taught-stack only | True | |

Expected QC result achieved after Iteration 2.

## Iteration 3 — Full-curriculum coverage (detailed_curriculum.csv)

See `../Session65/Curriculum-Coverage-QC.md`.

| Check | Result |
|---|---|
| CSV capstone LOs (rows 62–64) | Pass with hole: 3 live goldens vs S57’s 5–10 |
| All M3–M4 skills **live** on submit | Fail — several stretch/named/out (Ollama, FastAPI, retrieval tuning, LLM tool loop, compaction, retries) |
| All M1–M2 sessions re-labbed | Fail (correct) — M2 is eval mindset only |
| Student can name where the course lives | Pass after wrap table “Where this course shows up on the desk” |

