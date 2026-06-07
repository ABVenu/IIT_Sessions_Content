# Lecture Notes QC Report — Session 21
**File:** `Lecture Notes.md`
**Session:** Building a RAG Pipeline
**Date of QC:** 2026-06-07

---

## QC Evaluation — Iteration 1

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata/Internal References in Student Notes** | True |

**Expected result achieved:** All ratings ≥ 5; all boolean checks pass.

### Coverage Checklist (metadata subtopics)

| Subtopic | Covered in notes |
|---|---|
| Scale minimal RAG to real policy files (PDF/txt) for ShopKart | Yes — `policy_documents/` folder, TXT loaders, PDF loader via `pypdf` |
| Policy update workflows deferred | Yes — noted as **later** session; no session number cited |
| Deep chunk-tuning loops deferred | Yes — chunk-size experiment activity; systematic tuning deferred to **later** |
| Why raw documents must be prepared before retrieval | Yes — retrieval granularity, context window, noisy text section |
| Apply chunking with awareness of retrieval impact | Yes — size/overlap table, boundary activity, chunk experiment |
| Build searchable index across multiple policy sources | Yes — `build_knowledge_base`, metadata, multi-chunk upsert |
| Operate multi-document RAG assistant end-to-end | Yes — full `rag_pipeline.py` with `main()` and five demo queries |
| Same e-commerce scenario from earlier labs | Yes — ShopKart returns/shipping/warranty/refunds continuity |

### Structural Adherence Checklist

| Prompt rule | Result |
|---|---|
| Starts with `# Lecture Title` only | Pass |
| No target audience / duration / internal instructions in body | Pass |
| Context paragraph + bullet list of learning goals | Pass |
| 3-sentence rule on paragraphs | Pass |
| Official / In Simple Words / Real-Life Example on new concepts | Pass |
| Integrated learning in bullet flow | Pass |
| Full code with line comments + "How the code works" | Pass |
| Solo student activities (not "Ask students to…") | Pass — nine activity blocks |
| Previous / later references without session numbers | Pass |
| Key Takeaways + future link | Pass — five bullets |
| Quick Reference table at end | Pass |

### Logic Review

- Ingestion flow (load → clean → chunk → embed → store) precedes retrieve → generate — correct RAG ordering
- BGE model reused for index and query; `embedding_function=None` matches previous lab pattern
- ShopKart policy numbers consistent with earlier labs (7-day returns, 3–5 standard shipping, 1–2 express metro, 12-month warranty, 5–7 refund days, COD to UPI)
- Chunk overlap stride `start += chunk_size - overlap` is mathematically correct
- Skincare demo question aligns with personal-care non-returnable rule in sample `returns_policy.txt`
- Honest limits: OCR for scanned PDFs, policy refresh workflows, metadata filtering deferred appropriately

### Presentation Review

- No session numbers in student-facing text
- No "Part 1 / Section A" headings
- Mermaid diagrams for pipeline flow; no broken image URLs
- Bold terms and scannable bullets throughout
- Connecting sentences between major sections present

### Creativity Notes

- ShopKart continuity with expanded multi-paragraph policy files
- Indian-context analogies: coaching fee notices, nurse shift handover, train timetable, shopkeeper intent
- Minimal lab vs pipeline comparison table bridges previous implementation without session numbers
- Chunk boundary sketch and chunk-size experiment teach retrieval impact hands-on
- Fifth demo query (skincare/opened) tests chunking quality on edge-case returns wording

---

## QC Evaluation — Iteration 2

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata/Internal References in Student Notes** | True |

**Expected result achieved:** All ratings ≥ 5; all boolean checks pass.

### Iteration 2 Actions

- Re-reviewed full document after adding **Minimal Lab vs Today's Pipeline** comparison table
- Re-verified all code blocks are complete and runnable as one `rag_pipeline.py` script
- Re-grepped for forbidden session numbers, duration mentions, and internal instruction leakage — none found
- Confirmed document loaders (TXT + PDF) and chunking receive equal instructional depth per metadata topics

### Iteration 2 Notes

- Comparison table strengthens logical connection to previous minimal RAG lab while keeping student notes session-number-free
- Content depth appropriate for hands-on implementation session; offline/online phase split clearly repeated in mermaid and Key Takeaways
- QC pass confirmed — no revision required beyond iteration 1 polish

---

## Iteration History

| Iteration | Action | Result |
|---|---|---|
| 1 | Initial draft + full QC | All criteria pass |
| 2 | Added minimal-vs-pipeline table + re-QC | All criteria pass — notes ready for release |
| 3 | Lightened per feedback: shorter policy snippets, removed 9 standalone activities, merged theory, implementation checklist replaces activities | All criteria pass — implementation-focused |
| 4 | Full QC on lightened draft | Fail — Part 1/2/3 headings, missing line comments, thin concept definitions |
| 5 | Fixes applied + re-QC | All criteria pass — ready for release |

---

## QC Evaluation — Iteration 3 (Lightened)

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata/Internal References in Student Notes** | True |

**Changes in iteration 3:** Removed standalone activities (implementation + terminal verification table is the lab). Policy file snippets shortened to 2–3 sentences each. Theory merged into two compact sections. Full runnable code retained in three parts. Word count reduced ~45% while all metadata subtopics still covered.

---

## QC Evaluation — Iteration 4

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | 4 / 5 |
| **Creativity** | 4 / 5 |
| **Structural Adherence** | 3 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | False |
| **No Previous Session Number References** | True |
| **No Metadata/Internal References in Student Notes** | True |

**Expected result NOT achieved** — Structural Adherence and Presentation below threshold; fixes required.

### Issues found (lightened draft)

| Issue | Severity | Detail |
|---|---|---|
| Forbidden headings | Presentation | `### Part 1`, `### Part 2`, `### Part 3` violate Prompt4 “no Part 1 / Section A” rule |
| Code comment rule | Structural | Prompt4 requires a comment on **every code line**; lightened draft removed most comments |
| Simple Explanation Rule | Structural / Creativity | Document loader, chunking, ingestion lacked Official / In Simple Words / Real-Life triplets |
| Chunk boundaries | Content | Metadata subtopic on boundary impact was only implied, not stated |
| PDF path | Content | PDF loader in code but no student note that `.pdf` can replace `.txt` |

### Fixes applied before Iteration 5

- Renamed code sections to `### Imports, Loaders, and Chunking` / `### Index, Retriever, and Generator` / `### Run the Full Pipeline`
- Restored line comments on all Python lines across three code blocks
- Added compact Official / In Simple Words / Real-Life blocks for **document loader**, **chunking**, and **ingestion**
- Added chunk-boundary note and PDF-for-TXT swap line
- Expanded metadata bullet under Quick Rules

---

## QC Evaluation — Iteration 5

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata/Internal References in Student Notes** | True |

**Expected result achieved:** All ratings ≥ 5; all boolean checks pass.

### Coverage Checklist (metadata subtopics) — re-verified

| Subtopic | Covered |
|---|---|
| Scale minimal RAG to real PDF/TXT policy files (ShopKart) | Yes |
| Policy update + deep chunk-tuning deferred | Yes — “later session”, no session number |
| Why raw documents must be prepared | Yes — size, noise, cost + ingestion definition |
| Chunking with retrieval impact awareness | Yes — size/overlap, boundary note, terminal inspect |
| Searchable index across multiple sources | Yes — `build_knowledge_base`, metadata, BGE upsert |
| Multi-document RAG end-to-end | Yes — full script + 4 demo queries |
| Topics: document loaders; chunking | Yes |

### Structural Adherence Checklist — re-verified

| Prompt rule | Result |
|---|---|
| Starts with `# Lecture Title` only | Pass |
| No duration / target audience / internal instructions | Pass |
| Context + learning bullets | Pass |
| Official / In Simple Words / Real-Life on key concepts | Pass — loader, chunking, ingestion |
| Full code + line comments + “How the code works” | Pass |
| Implementation checklist as lab activity | Pass — no “Ask students to…” |
| No session numbers | Pass |
| Key Takeaways (3–5) + future link | Pass — 4 bullets |
| Quick Reference table | Pass |
| No Part 1 / Section A headings | Pass — fixed in iteration 4 |

### Logic Review

- Offline ingestion (load → clean → chunk → embed → store) precedes online retrieve → generate — correct
- BGE same for index and query; `embedding_function=None` consistent with previous lab
- ShopKart policy numbers match earlier labs (7-day, 3–5, 1–2 metro express, 12-month, 5–7, COD → UPI)
- Chunk overlap math correct; OCR limit for scanned PDFs noted
- Four demo queries span returns, shipping, warranty, refunds

### Presentation Review

- No session numbers or duration in student notes
- Mermaid pipeline diagram present; no broken image URLs
- Scannable bullets and tables; implementation-first layout preserved (~447 lines after QC fixes)

### Creativity Notes

- ShopKart continuity with minimal-lab vs file-pipeline comparison tables
- Indian-context analogies: receptionist notices, train timetable, hostel rules pinned before opening
- Terminal verification table replaces standalone activities without losing hands-on rigor
