# Lecture Notes QC Report — Agent Build Workshop

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-06-20

---

## Iteration 1

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics covered: corpus selection (reuse + BYO); ingest/chunk; embed/store in Chroma; retrieval config; context assembly; grounded generation; packaged runnable script; peer-review demo. |
| **Creativity** | **5 / 5** | Railway enquiry display board; hostel PDF shelf; kitchen/dukaan layout; open-book exam; librarian top-k; startup demo day; corpus map on paper; test matrix as quality gate. |
| **Structural Adherence** | **4 / 5** | `#` title; context + What you will build; Official/Simple/Real-life on new terms; step-by-step code with line comments and "How the code works"; student-facing activities; Key Takeaways; terminology table. Missing one consolidated full-file script block; sectional code only. |
| **No Logical Mistakes** | **True** | Pipeline order ingest → retrieve → augment → generate correct; same embed model rule; force_reingest guard; grounding refusal path; Ollama/Groq routing consistent. |
| **No Presentation Mistakes** | **False** | "### Demo script (about 5 minutes)" mentions session-adjacent duration; prompt forbids duration in student notes. |
| **No Previous Session Number References** | **True** | Grep: no `Session N` / `S39` etc. Uses **previous** and **earlier RAG labs** only. |
| **No Metadata/internal reference** | **True** | No audience, session duration, or internal instruction leakage. |

**Expected Result:** Not met — Structural Adherence 4/5; Presentation Mistakes False.

**Action:** Added complete `shop_easy_rag_app.py` monolithic script with line comments; removed "about 5 minutes" from demo heading; rephrased startup demo analogy to avoid duration wording.

---

## Iteration 2

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Full coverage retained; consolidated script strengthens runnable-app subtopic; peer review checklist and test matrix complete workshop arc. |
| **Creativity** | **5 / 5** | Analogies unchanged; workshop flow reads as build narrative not slide list. |
| **Structural Adherence** | **5 / 5** | All prompt rules met; complete end-to-end script; 7 student-facing activities; Key Takeaways + terminology table present. |
| **No Logical Mistakes** | **True** | Complete script matches sectional functions; corpus fallback; Chroma upsert id stability; without-RAG contrast optional path sound. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; paragraphs ≤3 sentences; activities student-facing (no "Ask students to"). |
| **No Previous Session Number References** | **True** | Verified via grep after edits. |
| **No Metadata/internal reference** | **True** | "Workshop default" used as lab config label, not internal QC instruction text. |

**Expected Result:** Met — all ratings ≥ 5; all boolean checks True.

**Outcome:** QC passed on iteration 2.

---

## Iteration 3 (line-limit revision)

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics retained after condensing from ~1014 to ≤500 lines. |
| **Creativity** | **5 / 5** | Analogies preserved; workshop flow tighter. |
| **Structural Adherence** | **5 / 5** | One complete script; concepts + activities; Key Takeaways + terminology table. |
| **No Logical Mistakes** | **True** | Pipeline unchanged; full script intact. |
| **No Presentation Mistakes** | **True** | No duration/session-number leakage. |
| **No Previous Session Number References** | **True** | Verified via grep. |
| **No Metadata/internal reference** | **True** | No internal instruction leakage. |

**Expected Result:** Met — condensed to 500-line limit per user request.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Choose a small document corpus (or reuse from earlier labs) | Step 1 — Choose Your Document Corpus |
| Apply RAG flow: load and chunk documents | Step 3 — Load, Chunk, and Attach Metadata |
| Create embeddings; store in a vector database | Step 4 — Embed and Store in Chroma |
| Configure retrieval and assemble context for the LLM prompt | Step 5 — Configure Retrieval; Step 6 — Assemble Context |
| Generate grounded answers from retrieved chunks only | Step 7 — Grounded Generation |
| Package as simple runnable RAG app and demo for peer review | Step 8 — Package the Runnable RAG Application; Complete runnable script; Step 10 — Peer Review Demo |
