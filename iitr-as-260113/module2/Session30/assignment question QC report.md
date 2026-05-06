# Assignment Question QC Report — Session 30

## Subjective Assignment QC

| Question No. | Type | Remarks |
|---|---|---|
| Q1 | Subjective — Coding (Multi-file Project) | Medium difficulty ✓. Real-world campus policy scenario (creative reframe of the e-commerce RAG taught in session). All 12 implementation requirements are explicitly stated. Expected input and output examples provided. Submission instructions follow Case D format with specific folder names (`module2 → Session30`). No dataset needed — student creates their own sample PDFs (clearly instructed). Submission link format clarified (folder link, not root repo). |

---

## Overall Assignment Quality Ratings

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | All major pipeline steps covered — ingestion, cleaning, chunking with overlap, embeddings (`text-embedding-3-small`), ChromaDB storage with metadata, retrieval (top-K), prompt construction, and LLM generation. Mirrors the session's 10-step workflow end-to-end. |
| Creativity | 5 | Scenario shifted from the lecture's e-commerce assistant to a campus policy assistant (hostel, refund, library, course withdrawal rules), making the task feel fresh and relatable without introducing out-of-scope concepts. |
| Structural Adherence | 5 | Single practical task ✓. Medium difficulty ✓. Submission format follows Case D (multi-file GitHub repo) with correct folder names derived from lecture notes path. Answer explanation section included with ideal solution walkthrough and mention of alternative valid approaches. |
| No Logical Mistakes | True | All required functions map directly to taught concepts. Chunk size (100–200 words), overlap (10–20%), embedding model, and ChromaDB usage are consistent with session content. The constraint "do not send entire PDF to LLM" directly reinforces the chunking rationale taught. |
| No Presentation Mistakes | True | Clear section headings, consistent formatting, numbered requirements, code blocks for folder structure and terminal commands, and example output block. No grammatical or spelling errors. |

---

## QC Verdict

All criteria meet the expected threshold (ratings ≥ 5, no logical or presentation mistakes). The subjective assignment is approved as-is.
