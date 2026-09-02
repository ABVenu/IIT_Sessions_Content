# Lecture Notes QC Report — Hands-On LangChain

**File reviewed:** `Lecture Notes.md`  
**Folder:** `IIT_Sessions_Content/iitr-as-2603/Masterclass/Session01HandsOnLangChain`  
**Review date:** 2026-09-02

---

## Iteration 1 (first full draft)

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **4 / 5** | LangChain vs LangGraph intro, LCEL, full T20 app, EvalPack present. Draft was **423 lines** (metadata target **480–500**). Package why-table incomplete; unused `import os`; no fail-fast on missing `GROQ_API_KEY`; Chroma-on-import not called out. |
| **Creativity** | **5 / 5** | T20 rulebook vs incident-log split; toolkit vs metro-map contrast for students who already know LangGraph. |
| **Structural Adherence** | **4 / 5** | Clean `#` title; Official Definition / In Simple Words / Real-Life Example on core terms. **Runnable** lacked a Real-Life Example. Informal “agent religion” phrasing. Some `run_eval` lines uncommented. |
| **No Logical Mistakes** | **False** | `import os` unused (`ChatGroq` reads the env key itself). Empty-keyword eval path was already N/A (good). Importing the file always builds Chroma — undocumented, so Phase-1-only import still downloads MiniLM. |
| **No Presentation Mistakes** | **True** | No duration / audience in body; four S3 images; student-facing activities. |
| **No Previous Session Number References** | **True** | Previous work named as graphs / RAG / Groq / golden questions only. |
| **No Metadata/Internal References in Student Text** | **True** | No lite/keep-it-light/instructor labels. |

### Expected Result

- Not met (coverage 4, structure 4, logical mistake True→False required)

**Outcome:** QC failed. Improvise, then re-run.

### Improvisation applied (iteration 1 → 2)

1. Expanded to metadata band: package table, label-the-job activity, skipped-imports table, Phase-1-only run command, end-to-end map, MiniLM first-download note.
2. Added `GROQ_API_KEY` fail-fast so `os` is used.
3. End-of-line comments on remaining eval prints; comments on each rule/incident document line.
4. Real-Life Example added for **Runnable**. Softened informal contrast line. Removed a capstone product name that this batch may not have reached yet.
5. Four lecture images uploaded to S3 and linked.

---

## Iteration 2 (after improvise)

**Line count:** 488 (inside 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Direct LangChain intro; advantages / disadvantages; vs LangGraph table and pick-which guide; real-life apps; LCEL + Runnable; one-file T20 assistant (RAG tool, `@tool`, memory, refusal); EvalPack with results log, N/A for empty keywords, failure signatures, one-patch activity. Stack matches this batch: `ChatGroq`, `GROQ_API_KEY`, MiniLM, Chroma. |
| **Creativity** | **5 / 5** | Distinct from ShopEasy / parcel-desk labs. Cricket two-source desk plus toolkit-vs-map teaching picture for LangGraph-first students. |
| **Structural Adherence** | **5 / 5** | `#` title only; context of previous work without session ids; connecting sentences; Official / Simple / Real-Life on new terms; full file + How the code works; student activities (not “Ask students”); Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | Tool split is sound; history cleared between eval cases; empty keywords print N/A; key guard before ingest; teaching samples labelled non-ICC; graph vs agent jobs not conflated. |
| **No Presentation Mistakes** | **True** | No duration/audience; four themed images with S3 URLs; no 1/5 badges in notes; scannable tables. |
| **No Previous Session Number References** | **True** | Grep clean for `Session N` / `session N`. |
| **No Metadata/Internal References in Student Text** | **True** | No keep-it-light / lite version / instructor-only headings. |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 2.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Direct LangChain intro (not scenario-first) | What Is LangChain |
| Advantages, disadvantages, vs LangGraph, applications | LangChain and LangGraph — How They Differ |
| Prior LangGraph / RAG / Groq / golden evals, no session numbers | Context of This Session |
| LCEL: `ChatPromptTemplate \| ChatGroq \| StrOutputParser` | LCEL — The Pipe Pattern; Phase 1 in the file |
| One file, three phases | What You Will Build; complete `t20_rules_assistant.py` |
| T20 rulebook RAG + incident tool + memory + refusal | What You Will Build; Phase 2 |
| HuggingFace MiniLM, Chroma, `create_retriever_tool`, `AgentExecutor`, `ask()` | The Complete App |
| EvalPack, results log, failure signatures, one patch | EvalPack and first fixes |
| Groq + essential langchain packages | Setup + package table |

---

## Differentiation Check vs This Batch’s LangGraph Work

| Aspect | LangGraph (already taught) | This masterclass | OK? |
|---|---|---|---|
| Picture | Nodes, edges, shared state, checkpoints | LCEL chains + one `AgentExecutor` desk | Yes |
| App | Appointment / reliability graphs | T20 rules + INC log | Yes |
| Model | Groq in later modules | `ChatGroq` + `llama-3.1-8b-instant` | Yes |
| Embeddings | MiniLM in RAG labs | Same MiniLM via `HuggingFaceEmbeddings` | Yes |

---

## Iteration 3 (verification pass — required even after pass)

Re-read after iteration 2 edits. Line count **488**. Images resolve under `iitr-as-2603/masterclass/session01-hands-on-langchain/`. No session-number or metadata leaks. Unused-import and informal-phrasing issues remain closed.

### QC Criteria

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | **5 / 5** |
| **Creativity** | **5 / 5** |
| **Structural Adherence** | **5 / 5** |
| **No Logical Mistakes** | **True** |
| **No Presentation Mistakes** | **True** |
| **No Previous Session Number References** | **True** |
| **No Metadata/Internal References in Student Text** | **True** |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 3. No further improvisation required.

---

## Iteration 4 (fresh QC after image refresh — prompt re-run)

Re-read the live `Lecture Notes.md` (post architecture-image swap) against `LectureNotesPrompt4.md` + `LectureNotesQC.md` + `metadata.md`.

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics still present: LangChain intro, vs LangGraph, LCEL, one-file T20 app, EvalPack, Groq/MiniLM stack. Line count 488 (in band). |
| **Creativity** | **5 / 5** | T20 two-source desk; four architecture/eval figures (no name strip). |
| **Structural Adherence** | **4 / 5** | **Agentic RAG**, **EvalPack**, and **tool arbitration** were used without the full Official / In Simple Words / Real-Life Example triad. A few code lines (`@tool`) uncommented. |
| **No Logical Mistakes** | **False** | **Q3** asks the rulebook about INC-101’s 5-run pitch penalty, but the corpus had **no** penalty-runs document — follow-up cannot be grounded. **out_of_domain** printed Keywords N/A but still set `keywords_ok=True`, so the results log counted a refusal case as a keyword **PASS**. |
| **No Presentation Mistakes** | **False** | Body still called LangGraph a **metro map** after images were changed to a node-and-edge graph. One-patch activity said “try another class” (ambiguous). |
| **No Previous Session Number References** | **True** | Grep clean. |
| **No Metadata/Internal References in Student Text** | **True** | No lite / duration / audience in student body. |

### Expected Result

- Not met (structure 4; logical False; presentation False)

**Outcome:** QC failed. Improvise, then re-run.

### Improvisation applied (iteration 4 → 5)

1. Added a **penalty-runs** `Document` so Q3 (INC-101 → rulebook) is grounded.
2. Eval N/A path now uses `keywords_ok=None`; summary is `passed/scored` and the refusal row prints **N/A**, not PASS.
3. Added Official / Simple / Real-Life for **Agentic RAG**, **EvalPack**, and **tool arbitration**.
4. Replaced leftover metro-map wording; clarified the one-patch activity; commented `@tool`.

---

## Iteration 5 (after improvise)

**Line count:** 500 (upper bound of 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Unchanged metadata coverage; Q3 now has a matching rule chunk; eval scoring matches the N/A story. |
| **Creativity** | **5 / 5** | Same T20 product + LangGraph-first contrast; images remain framework/architecture/eval dashboards. |
| **Structural Adherence** | **5 / 5** | `#` title; previous-work context without session ids; triad on new terms including Agentic RAG, EvalPack, tool arbitration; full file + How the code works; student activities; Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | Pitch-penalty doc grounds Q3; history cleared between eval cases; N/A not counted as keyword pass; `if keywords_ok is False` does not fire on None; teaching samples still labelled non-ICC. |
| **No Presentation Mistakes** | **True** | Metro-map leftover removed; four S3 architecture images; no duration/audience; no 1/5 badges. |
| **No Previous Session Number References** | **True** | Grep clean. |
| **No Metadata/Internal References in Student Text** | **True** | Confirmed. |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 5.

---

## Iteration 6 (verification pass — required even after pass)

Re-read after iteration 5 edits. Line count **500**. Eval N/A path, penalty-runs chunk, and definition triads re-checked. No session-number or metadata leaks.

### QC Criteria

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | **5 / 5** |
| **Creativity** | **5 / 5** |
| **Structural Adherence** | **5 / 5** |
| **No Logical Mistakes** | **True** |
| **No Presentation Mistakes** | **True** |
| **No Previous Session Number References** | **True** |
| **No Metadata/Internal References in Student Text** | **True** |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 6. No further improvisation required.
