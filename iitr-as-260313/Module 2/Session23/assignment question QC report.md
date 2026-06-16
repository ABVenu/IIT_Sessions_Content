# Assignment Question QC Report — Session 23: Working with APIs and JSON

## Per-Question QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Easy) | Correct option **B** (API for live order tracking) — relevant: RAG vs API distinction for changing facts. |
| Q2 | MCQ (Easy) | Correct option **B** (RAG for warranty policy) — relevant: stored rules vs live data. |
| Q3 | MCQ (Easy) | Correct option **B** (handle error before parsing) — relevant: status-before-body habit; 404 typo scenario. |
| Q4 | MCQ (Easy) | Correct option **C** (429 rate limit) — relevant: Groq free-tier experience from prior sessions. |
| Q5 | MCQ (Moderate) | Correct option **B** (GET read-only) — relevant: weather lab REST mapping. |
| Q6 | MCQ (Moderate) | Correct option **C** (`json.loads` on string) — relevant: parse log/file JSON text. |
| Q7 | MSQ (Moderate) | Correct options **A, B, C** — relevant: RAG/API routing scenarios; D correctly excluded (policy summary needs RAG). |
| Q8 | MSQ (Moderate) | Correct options **A, B, C** — relevant: Groq request–response mapping; D correctly excluded. |
| Q9 | MSQ (Hard) | Correct options **A, B, C** — relevant: lab best practices (status, field extraction, label/coordinate match); D correctly excluded. |
| Q10 | MSQ (Hard) | Correct options **A, B, C** — relevant: nested JSON paths and dumps vs loads; D correctly excluded (`response.json` already parses). |
| Subjective Q1 | Practical (Light, guided) | Fetch helper supplied; student writes one extract function + `json.loads` block only. No Groq, no second city, no error-drill, no repo. Submission: case c (single `.py` in LMS). Inline order JSON — no external dataset. Correct option N/A — practical task. |

---

## Objective Assignment — Overall QC

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes:** 10 questions total — 6 MCQs (4 Easy Q1–Q4, 2 Moderate Q5–Q6) + 4 MSQs (2 Moderate Q7–Q8, 2 Hard Q9–Q10). Progressive Easy → Moderate → Hard. Scenario-based ShopKart framing; no session-reference phrasing. Every question includes answer explanations with distractor reasoning. Topics: RAG vs API, status codes, GET/REST, `json.loads`/`dumps`/`response.json`, request–response mapping, field extraction discipline. Surface-only REST verbs (PUT/PATCH/DELETE) not tested in subjective; function calling deferred to next session.

**Outcome:** PASS

---

## Subjective Assignment — Overall QC

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes:** Kept **lighter** per guidance — ~15 lines of student code vs full lab from scratch. Starter provides complete GET + status-check pattern; tasks limited to `extract_weather_fields`, `json.loads` on inline order string, and one Delhi run. Medium concepts from prompt downgraded to **light guided** difficulty. Case-c submission clear. No dataset beyond public Open-Meteo; order JSON embedded in file.

**Outcome:** PASS

---

## Combined Expected Result

| Assignment | Content Coverage | Creativity | Structural Adherence | Logical Mistakes | Presentation Mistakes |
|---|---|---|---|---|---|
| Objective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |
| Subjective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |

**Final QC status:** PASS — all criteria meet expected thresholds.
