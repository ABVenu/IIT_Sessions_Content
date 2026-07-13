# Lecture Notes QC Report — Session 30 (RAG: Chunking & Document Preparation)

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-07-04  
**Source:** Reused from `iitr-as-2601/Module3/Session40/Lecture Notes Released.md` (live-taught release edition). Class-facing phrases rewritten for student notes.

---

## Iteration 1

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics covered: in-memory/PDF corpus load; fixed-size chunking with justified size/overlap (500/75 manual, 512/16 large PDF); metadata (`source_id`, `page`, `chunk_index`); persist into Chroma (`policy_chunks`) using the same pattern as the prior FAQ lab. LangChain Tesla demo included as taught. |
| **Creativity** | **5 / 5** | ShopEasy policies, samosa chunk-size analogy, coaching-institute photocopy, newspaper overlap, chat-upload vs true RAG contrast, wrong-match tuning table. |
| **Structural Adherence** | **5 / 5** | `#` title, Context linked to previous FAQ/Chroma lab, Official / Simple / Real-life pattern, full code with line comments and "How the code works", student-facing activities, Key Takeaways, terminology table. |
| **No Logical Mistakes** | **True** | Same-model rule preserved; overlap &lt; chunk_size enforced; metadata not embedded; FAQ collection vs `policy_chunks` separation correct. |
| **No Presentation Mistakes** | **True** | Fixed class-facing phrases (`What was contrasted in class` → `Key contrast`; `class used` / `class ran` / `Extra in class`). No session numbers; no duration metadata. |
| **No Previous Session Number References** | **True** | Uses "previous session" / "prior lab" / "upcoming work" only. Context correctly reflects Embeddings & Vector Search (FAQ + Chroma). |
| **No Metadata/Internal References** | **True** | No audience, duration, or "keep it lite" language in student-facing text. |

**Expected result:** All criteria met — **QC passed**.

### Fixes applied in iteration 1

| Issue | Resolution |
|---|---|
| `What was contrasted in class` | `Key contrast` |
| `class used` (chunk settings) | `a practical setting is` |
| `Extra in class` (metadata table) | `Optional tags` |
| `class ran` (Tesla demo) | `you can run` |

---

## Iteration 2 (Re-QC)

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Re-verified against `metadata.md` — load, chunk size/overlap, metadata, persist all present and complete. |
| **Creativity** | **5 / 5** | Analogies and activities remain clear for non-tech audience. |
| **Structural Adherence** | **5 / 5** | Matches LectureNotesPrompt4 structure requirements. |
| **No Logical Mistakes** | **True** | Lab sequence (corpus → chunk → encode → upsert → query) remains correct. |
| **No Presentation Mistakes** | **True** | No remaining class/instructor phrasing; activities student-facing. |
| **No Previous Session Number References** | **True** | Confirmed — no numbered session references in student text. |
| **No Metadata/Internal References** | **True** | Confirmed — professional student document only. |

**Expected result:** All criteria met — **QC passed**. No further revision required.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Load plain-text or PDF into a corpus | Sample Dataset (in-memory); Real-World PDF Demo (LangChain folder load) |
| Apply chunking with justified size and overlap | Chunk Size; Chunk Overlap; Implement Chunking |
| Attach lightweight metadata (source id; page) | Metadata for Traceability; create_chunks_from_corpus |
| Persist chunked documents into prior vector store | Persist Chunked Documents in Chroma (`policy_chunks`) |

**Line count:** ~518 lines. **Outcome:** Ready for student release.

---

## Iteration 3 — Sync with Session 29 (2026-07-04)

**Trigger:** Align Session 30 lecture notes, preread, and mental map with Session 29 (Embeddings & Vector Search) content and branding.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Unchanged lab coverage; context now explicitly names Session 29 outcomes (embeddings, similarity, five FAQs, `support_knowledge_base`, `all-MiniLM-L6-v2`, `category` → `source_id`/`page`). |
| **Creativity** | **5 / 5** | ShopEasy introduced as continuation of the e-commerce FAQ theme (30-day returns, 499-rupee shipping), not as a prior brand students already used. |
| **Structural Adherence** | **5 / 5** | Context + forward links use "later work" (matches Session 29 wording). |
| **No Logical Mistakes** | **True** | FAQ collection vs `policy_chunks` separation preserved; same Chroma path and same-model rule. |
| **No Presentation Mistakes** | **True** | Removed false "same brand you have been using" claim; recap no longer lists "prompts" as prior-session content. |
| **No Previous Session Number References** | **True** | Still uses previous / later only. |
| **No Metadata/Internal References** | **True** | Unchanged. |

**Sync checklist applied:**

| Item | Alignment |
|---|---|
| Prior lab | Five FAQs, Chroma, `support_knowledge_base`, Sentence Transformers, top-k |
| Metadata bridge | `category` → `source_id` / `page` / `chunk_index` |
| Branding | ShopEasy = longer policies on the same e-commerce support theme |
| Mental map M3U | Embeddings & Vector Search done (not generic "RAG + vector search") |
| Session 29 forward links | What Comes Next / Key Takeaways / Preread point to chunking + richer metadata |

**Expected result:** All criteria met — **QC passed**.

---

## Iteration 4 — Align Released Notes to Live Topic Coverage (2026-07-13)

**File reviewed:** `Lecture Notes Released.md`  
**Sources:** `Transcript.md`, `Live Topic Coverage.md`, `Lecture Notes.md`, `metadata.md`

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **4 / 5** | Core LOs present, but released draft still needed cuts/fixes vs live teach: HNSW/IVF section not taught; chat-upload framing not taught (Siemens proprietary RAG was); Tesla notes wrongly said MiniLM + metadata omitted; GTE Large, LangChain auto-metadata, and Groq answer preview were taught but missing/wrong. |
| **Creativity** | **5 / 5** | Siemens manuals, samosa size, newspaper overlap, ShopEasy policies retained/strengthened. |
| **Structural Adherence** | **5 / 5** | Context → concepts → code → activities → takeaways → terminology table; Official / Simple / Real-life pattern kept. |
| **No Logical Mistakes** | **False** | Tesla demo incorrectly listed MiniLM and claimed metadata was omitted; live teach used GTE Large and showed `source` + `page` (e.g. page 125). |
| **No Presentation Mistakes** | **True** | No Mentimeter/quiz; images retained; student-facing activities only. |
| **No Previous Session Number References** | **True** | Uses previous / upcoming / later only. |
| **No Metadata/Internal References** | **True** | No audience, duration, or keep-it-lite language. |

**Expected result:** Not met — improvise and re-QC.

### Fixes applied in iteration 4

| Change | Reason |
|---|---|
| Removed **Vector Stores and Similarity Indexes (HNSW/IVF)** | Not covered in transcript |
| Replaced chat-upload section with **Normal Generation vs RAG for Proprietary Data** (Siemens) | Matches live opening |
| Removed **sentence-aware** strategy; kept page-as-chunk as concept-only | Matches live “strategy 3 is concept only” |
| Shortened **semantic chunking** to brief look-ahead | Introduced only as future advanced topic |
| Corrected Tesla demo: **GTE Large**, auto metadata, `persist_directory`, retriever, Groq preview | Matches Live Topic Coverage extras |
| Added top-k too-few / too-many note; LangChain one-call helpers | Taught extras |
| Trimmed Key Takeaways to 5 bullets; added terminology rows for GTE Large / Groq preview | Prompt + coverage alignment |

---

## Iteration 5 (Re-QC after alignment fixes)

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics + taught extras (RAG recap, LangChain, semantic verify, Tesla end-to-end preview, GTE Large, semantic-chunking look-ahead). Untaught HNSW/IVF and chat-upload framing removed. |
| **Creativity** | **5 / 5** | Siemens proprietary manuals, ShopEasy policies, samosa/newspaper analogies, Rank-1 tuning table. |
| **Structural Adherence** | **5 / 5** | Matches LectureNotesPrompt4; full code with comments + “How the code works”; student activities; Key Takeaways; terminology table; all prior images retained. |
| **No Logical Mistakes** | **True** | Manual lab = MiniLM + `policy_chunks`; Tesla demo = GTE Large + LangChain metadata; overlap < chunk_size; metadata not embedded. |
| **No Presentation Mistakes** | **True** | Softened “live demo” phrasing; no quiz/Mentimeter; professional student document. |
| **No Previous Session Number References** | **True** | Confirmed — previous / upcoming / later only. |
| **No Metadata/Internal References** | **True** | Confirmed — no internal dial/audience/duration language. |

**Expected result:** All criteria met — **QC passed**.

### Coverage checklist (released notes vs live)

| Subtopic / taught extra | Status in `Lecture Notes Released.md` |
|---|---|
| Load plain-text or PDF into a corpus | Covered — sample corpus + `PyPDFDirectoryLoader` |
| Apply chunking with justified size and overlap | Covered — 500/75 manual, 512/16 Tesla |
| Attach metadata (`source_id`, `page`) | Covered — manual tags + LangChain auto metadata |
| Persist into Chroma | Covered — `upsert` + `Chroma.from_documents` |
| LangChain / GTE Large / RAG answer preview | Covered — Tesla section |
| Semantic chunking (introduced only) | Kept brief look-ahead |
| HNSW/IVF, chat-upload framing, sentence-aware strategy | Removed |

**Outcome:** `Lecture Notes Released.md` ready for student release.
