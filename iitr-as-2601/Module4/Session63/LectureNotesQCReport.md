# Lecture Notes QC Report — Session 63 (Polish & Demo)

## Iteration 1

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 4 | UX, cost, demo, retro present but thin vs 480-line target |
| Creativity | 5 | Courier counter vs CCTV; “green means paid” trap |
| Structural Adherence | 4 | Under length; activity names with clock-time |
| No Logical Mistakes | False | Risk of UI `policy_chunks` shortcut hiding empty Chroma |
| No Presentation Mistakes | False | Duplicate closing picture after padding |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |

**Fixes applied:** same-graph warning; cost note template; sample buttons; troubleshooting table; removed duration-ish activity titles; removed duplicate closing picture; cache must not skip gates.

## Iteration 2

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Streamlit on `graph.invoke`, cost assumptions, demo script, retro without SLI/SLO |
| Creativity | 5 | |
| Structural Adherence | 5 | Curriculum LOs covered; previous/upcoming only |
| No Logical Mistakes | True | UI and golden share one graph; labelled vs Groq tokens separated |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |

Expected QC result achieved.

## Iteration 3 — Logic, flow, taught-stack only

| Criterion | Result | Notes |
|---|---|---|
| Content Coverage | 5 | Streamlit on the same `graph.invoke` as eval; cost; demo; retro |
| Creativity | 5 | |
| Structural Adherence | 5 | UX session does not introduce a second API app |
| No Logical Mistakes | True | UI no longer pastes handbook lines; empty `policy.md` still fail-closed |
| No Presentation Mistakes | True | |
| No Previous Session Number References | True | |
| No Metadata/internal reference | True | |
| Taught-stack only | True | FastAPI removed from demo close and retro “more time” |

**Fix:** Streamlit calls the graph with only `ticket_id`, `raw_text`, `trace`.

