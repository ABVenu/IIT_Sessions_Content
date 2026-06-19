# Assignment Question QC Report — Session 24: Tool Integration in AI Agents

## Per-Question QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Easy) | Correct option **B** (`search_shopkart_policy`) — relevant: policy-only routing for returns question. |
| Q2 | MCQ (Easy) | Correct option **C** (local Python runtime executes GET) — relevant: Groq proposes, runtime executes. |
| Q3 | MCQ (Easy) | Correct option **C** (`tool_choice="auto"`) — relevant: model decides tool selection. |
| Q4 | MCQ (Easy) | Correct option **B** (MCP as translator) — relevant: surface-level MCP concept from notes; not tested in subjective. |
| Q5 | MCQ (Moderate) | Correct option **C** (model returns `tool_calls` first) — relevant: tool execution loop order. |
| Q6 | MCQ (Moderate) | Correct option **A** (`json.loads`) — relevant: parse tool argument strings. |
| Q7 | MSQ (Moderate) | Correct options **A, B, C** — relevant: tool schema fields; D correctly excluded (`tool_call_id` is response-side). |
| Q8 | MSQ (Moderate) | Correct options **A, C** — relevant: combined policy + weather routing and grounding; B, D correctly excluded. |
| Q9 | MSQ (Hard) | Correct options **A, C** — relevant: safe error JSON + grounding prompt for non-200 weather; B, D correctly excluded. |
| Q10 | MSQ (Hard) | Correct options **A, C, D** — relevant: local runtime pattern, `role: tool`, `json.dumps`; B correctly excluded. |
| Subjective Q1 | Practical (Medium) | Implement `run_tool_agent` loop only; tools/registry supplied. Two demo queries (policy-only + combined). Submission: case c (single `.py` in LMS). Requires `GROQ_API_KEY` + Open-Meteo — no external dataset. MCP/n8n not in subjective (surface-only in notes). |

---

## Objective Assignment — Overall QC

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**Notes:** 10 questions total — 6 MCQs (4 Easy Q1–Q4, 2 Moderate Q5–Q6) + 4 MSQs (2 Moderate Q7–Q8, 2 Hard Q9–Q10). Progressive Easy → Moderate → Hard. Scenario-based ShopKart framing; no session-reference phrasing. Every question includes answer explanations with distractor reasoning. Topics: function calling, tool routing, `tool_choice="auto"`, local runtime vs Groq cloud, tool schema, execution loop order, `json.loads`/`json.dumps`, combined policy+weather grounding, safe error JSON, MCP surface concept.

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

**Notes:** Medium difficulty — student implements core **`run_tool_agent`** loop (~35 lines); tool functions and **`TOOLS`** registry provided as starter. Creative applied scenario (missing runtime wiring). Two verification queries with expected routing table. Case-c submission clear. Full reference solution in answer explanation (no grader rubric in CSV). Chroma swap and MCP integration excluded (surface / extension topics).

**Outcome:** PASS

---

## Combined Expected Result

| Assignment | Content Coverage | Creativity | Structural Adherence | Logical Mistakes | Presentation Mistakes |
|---|---|---|---|---|---|
| Objective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |
| Subjective | 5 / 5 | 5 / 5 | 5 / 5 | None | None |

**Final QC status:** PASS — all criteria meet expected thresholds.

---

## QC Pass 2 (Re-verification after Q4 typo fix)

| Criterion | Objective | Subjective |
|---|---|---|
| **Content Coverage** | 5 / 5 | 5 / 5 |
| **Creativity** | 5 / 5 | 5 / 5 |
| **Structural Adherence** | 5 / 5 | 5 / 5 |
| **No Logical Mistakes** | True | True |
| **No Presentation Mistakes** | True | True |

**Notes:** Fixed presentation typo in Q4 explanation (`LLM's`). Re-verified all correct options against released lecture notes. Subjective scope limited to taught loop — does not require full file-from-scratch or MCP implementation.

**Pass 2 outcome:** PASS — expected QC result achieved.

---

## CSV Export QC — `AssignmentCreation.csv`

**Trigger:** CSV export with `tagRelationships` = `6a34f24e756f0bcb6cf8fe44`.

| Check | Result |
|---|---|
| Total rows | 11 (10 objective + 1 subjective) + header |
| `tagRelationships` on all rows | `6a34f24e756f0bcb6cf8fe44` |
| CSV parse (Python `csv.reader`) | PASS — 12 rows, 19 columns each |
| Question bodies | No question numbers / difficulty prefixes in `contentBody` |
| Options | Direct content only (no `A.` / `B.` prefixes) |
| `mcscAnswer` values Q1–Q6 | 2, 3, 3, 2, 3, 1 — verified |
| `mcmcAnswer` values Q7–Q10 | 1,2,3 / 1,3 / 1,3 / 1,3,4 — verified |
| `difficultyLevel` | Easy=0 (Q1–Q4), Moderate=0.5 (Q5–Q8, subjective), Hard=1 (Q9–Q10) |
| Subjective `contentBody` | Scenario + setup + starter code + tasks + submission — no answer in body |
| Subjective `answerExplanation` | Walkthrough + reference `run_tool_agent` code + sample output; no grader rubric |
| Markdown preserved | `contentType=markdown`, code blocks intact |

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

**CSV QC outcome:** PASS
