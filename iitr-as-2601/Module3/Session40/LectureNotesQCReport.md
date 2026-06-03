# Lecture Notes QC Report — Session 40 (RAG: Chunking & Document Preparation)

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-05-30  
**Iteration:** 1

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics covered: plain-text and PDF loading into a unified corpus; chunk size (500) and overlap (75) with justification and comparison activity; metadata (`source_id`, `page`, `chunk_index`); persist chunked rows to Chroma via embed-and-upsert; verify (`count`, `peek`, `get`) and top-k query on chunked policies. Bridges from Session 39 FAQ lab without naming session numbers. |
| **Creativity** | **5 / 5** | Indian-context analogies (kirana ledger, coaching photocopy shop, samosa bite-size, Zomato menu cards, WhatsApp broadcast policy, court citation). ShopEasy e-commerce thread consistent with prior module labs. Troubleshooting table and chunk-count comparison activity reinforce tuning intuition. |
| **Structural Adherence** | **5 / 5** | Clean `#` title start; no audience/duration header. Context + bullet goals. Official / Simple / Real-life on new terms. Full code blocks with per-line comments and "How the code works" sections. Student-facing activities (corpus inspect, chunk-count compare, trace-the-answer). Key Takeaways + terminology table at end. Paragraphs kept short; scannable bullets throughout. |
| **No Logical Mistakes** | **True** | Corpus record shape consistent across `.txt` and PDF loaders; chunk loop guard (`chunk_size > overlap`); same-model rule and `embedding_function=None` workflow aligned with Session 39; warranty PDF separated from returns `.txt` to avoid duplicate corpus rows; metadata copied per chunk; Chroma upsert index alignment correct. |
| **No Presentation Mistakes** | **True** | No session numbers or duration in student-facing text. References use "previous session", "later work", "upcoming work" only. Activities written as notebook tasks, not "Ask students to". No internal metadata (Keep it Lite, pacing, instructor blocks) exposed. |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes: **True** — **Met**

**Outcome:** QC passed on iteration 1. No further revision required.

---

## Iteration 2

**Trigger:** Rebalance priority — subtopics 2–4 (chunking, metadata, storage) primary; subtopic 1 (loading/corpus) secondary; lighter overall (~Session 39 length).

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics retained: chunking strategies with justified size/overlap + compare activity; source_id/page metadata on every chunk; Chroma persist; loading as condensed end section with in-memory `sample_corpus` for main lab path. |
| **Creativity** | **5 / 5** | Coaching photocopy, samosa, newspaper overlap, court citation; three strategy types named (fixed/sentence/page). |
| **Structural Adherence** | **5 / 5** | Context states priority order; theory before optional load; full code with comments; activities on chunk compare + metadata check + trace Rank 1; Key Takeaways + table. |
| **No Logical Mistakes** | **True** | Lab order note (load → chunk → upsert) vs teaching order explained; same Chroma/model rules; metadata not embedded. |
| **No Presentation Mistakes** | **True** | No session numbers/duration; student-facing activities; loading explicitly secondary. |

**Line count:** ~430 lines (down from ~653). **Outcome:** QC passed.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Load plain-text or PDF into consistent corpus | Loading Plain-Text Documents; Loading PDF Documents; Merge Files into One Master Corpus |
| Apply chunking with justified chunk size and overlap | Why Chunking Matters; Choosing Chunk Size; Chunk Overlap; Implement Chunking with Size and Overlap; Compare Chunk Counts activity |
| Attach lightweight metadata (source id; page) | The Document Corpus; Metadata for Traceability; `create_chunks_from_corpus` |
| Persist chunked documents into vector store from prior session | Set Up the Vector Store Lab; Persist Chunked Documents in Chroma; Verify Storage; Run Semantic Search |

**Line count:** ~647 lines.

---

## Iteration 3 — Post-session alignment (`Lecture Notes Released.md`)

**Trigger:** Align released notes to `Live Topic Coverage.md` and Session 40 transcript (2026-06-03).  
**File reviewed:** `Lecture Notes Released.md`  
**Inputs:** Transcript, Live Topic Coverage, metadata subtopics, original `Lecture Notes.md`.

### Alignment changes

| Action | Detail |
|---|---|
| **Removed** | Compare-chunk-count activity (300/500/800 runs) — not delivered live |
| **Removed** | Long manual `pypdf` / `load_corpus_from_folder` walkthrough — class used in-memory corpus + LangChain folder load |
| **Added** | Document upload vs true RAG / in-memory RAG contrast |
| **Added** | Ground rule **512 / 16** for large PDFs (Tesla demo) alongside **500 / 75** policy lab |
| **Added** | LangChain Tesla demo (`PyPDFDirectoryLoader`, splitter, `Chroma.from_documents`, 351 chunks) |
| **Added** | Semantic chunking (advanced), vector DB similarity indexes (HNSW/IVF), optional metadata filters |
| **Retained** | All 7 S3 diagram images; manual `policy_chunks` lab code and activities |

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics plus live extras: RAG prepare recap, ChatGPT upload contrast, 512/16 large-PDF rule, semantic chunking intro, LangChain Tesla path, similarity indexes. Manual Chroma lab + verify/query retained. |
| **Creativity** | **5 / 5** | Original analogies preserved; new chat-upload vs indexed-RAG contrast; Tesla SEC filing anchors large-PDF tuning. |
| **Structural Adherence** | **5 / 5** | Clean title; context bullets; Official/Simple/Real-life pattern; full code blocks; student activities (metadata check, trace Rank 1); Key Takeaways + terminology table. |
| **No Logical Mistakes** | **True** | Overlap < chunk_size rule; metadata not embedded; same-model rule; LangChain vs manual paths distinguished; Tesla demo notes metadata omission intentionally. |
| **No Presentation Mistakes** | **True** | No session numbers or duration; no Mentimeter; no internal instructor notes; activities student-facing. |
| **No Previous Session Number References** | **True** | Uses “previous lab/work” only. |
| **No Metadata/internal reference in student text** | **True** | No “keep it lite”, pacing, or grader rubrics. |

### Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes: **True** — **Met**

**Line count:** ~518 lines. **Outcome:** QC passed on iteration 3. Released file ready for students.
