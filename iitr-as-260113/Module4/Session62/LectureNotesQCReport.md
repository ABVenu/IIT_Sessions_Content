# Lecture Notes QC Report — Prototyping a Multi-Agent System

**File reviewed:** `Lecture Notes.md`  
**Batch / folder:** `iitr-as-260113/Module4/Session62`  
**Review date:** 2026-08-17

---

## Iteration 1

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Tools, LCEL sequential agents, Chroma memory, stamp/report doors, three-case eval, iterative fix table. |
| **Creativity** | **5 / 5** | Workshop stamps; two-path desk; clipboard exams; polite invoice injection. |
| **Structural Adherence** | **4 / 5** | Code complete with comments. **Gap:** first draft under 480 lines; LangChain `@tool.invoke` first used positional strings. |
| **No Logical Mistakes** | **False** | `check_gstin.invoke(gstin)` must be `invoke({"gstin": ...})` for StructuredTool. Amount gate must stay in Python. Insert-after-pipeline reminder added. |
| **No Presentation Mistakes** | **False** | Line count short; optional prose-extract needed connecting sentence so labelled parse does not look like a banned “lite mode.” |
| **No Previous Session Number References** | **True** | previous / upcoming only. |
| **No Metadata/internal reference** | **True** | No “lite version” wording; labelled slips framed as lab clerk typing. |

### Expected Result

- All ≥ 5 and flags True — **Not met**

**Outcome:** QC **failed** on iteration 1. Fixed tool invoke dicts; added wiring checklist, optional `extract_prose`, eval-through-doors runner; line count **481**.

---

## Iteration 2

**Re-review after improvisation.** Line count: **481**. Four S3 images uploaded. Tools return UNKNOWN/MISSING/POLICY_STORE_EMPTY. Stamp actor is `human`.

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Multi-agent implementation, tool integration, memory setup, iterative development + live CLEAN/HIGH/BADGST. |
| **Creativity** | **5 / 5** | Fail-closed empty binder as a feature then seed; CFO five-minute demo order. |
| **Structural Adherence** | **5 / 5** | `#` title; Official/Simple/Real-life; full commented Python; How the code works; activities; takeaways; terminology. |
| **No Logical Mistakes** | **True** | Sequential `|`; gates in Python; no payout; eval uses TestClient on `/ingest`; duplicate helper is episodic SQL. |
| **No Presentation Mistakes** | **True** | Confirmed. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

### Expected Result

- All **≥ 5** and flags **True** — **Met**

**Outcome:** QC **passed** on iteration 2.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Implement GST, PO, policy, log tools | Tools: The Workshop |
| Sequential LangChain pipeline | Sequential Pipeline; optional extract_prose |
| Attach packet, SQLite, Chroma memory | Memory section; find_duplicate |
| Happy path and human-gate through FastAPI | Stamp Door; live demo script |
| Three-case eval and one targeted fix | Eval Runner; Iterative Fix Loop |
| Create n8n workflow and attach | Attach n8n as the Courier |

---

## Iteration 3 — Logical correctness and pedagogical flow

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Tools, LCEL pipeline, SQL memory, Chroma RAG, human stamp, n8n attach, three-case eval. |
| **Creativity** | **5 / 5** | Workshop stamps; two paths; courier vs judge. |
| **Structural Adherence** | **5 / 5** | Hire clerks → exam → courier; 480 lines. |
| **No Logical Mistakes** | **True** | Policy now **returns** if status is `needs_typecheck` (was overwriting to ready). Confidence can be read from the slip. RAG chunks cannot skip Python gates. `httpx` added for TestClient. n8n is taught on the same `/ingest` door after cases pass. |
| **No Presentation Mistakes** | **True** | n8n no longer listed as “can wait” while also being an LO. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

**Pedagogical flow:** Tools → memory/RAG → sequential agents → stamp → live demo → eval → one fix → **then** n8n. Courier is not attached to a broken desk. Support week is remaining cases/UI, not the first n8n hook.

**Outcome:** QC **passed** on iteration 3.
