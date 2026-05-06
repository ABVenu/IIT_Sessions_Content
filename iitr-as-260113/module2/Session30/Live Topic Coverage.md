| Topic / Subtopic | Status | Remarks |
|---|---|---|
| Session narrative goal — Convert minimal architecture into a production-style RAG pipeline (multi-document ingestion through answer generation for e‑commerce scenario) | Covered | Framed upfront; live “advanced e‑commerce RAG” walkthrough with folder of policy PDFs, chunking → embeddings → ChromaDB → retrieve → prompted LLM response. |
| Expand the E‑Commerce Knowledge Base — Work with multiple policy documents and larger content sets | Covered | Compared prior string/list snippets to multiple real policy PDFs (return, refund, shipping); discussed scaling to many files in one folder. |
| Ingest Documents Using Document Loaders — PDFs | Covered | Demonstrated loading with Python `pypdf` (`PdfReader`); framing that companies usually store policies as PDFs. |
| Ingest Documents Using Document Loaders — Text files / webpages | Not covered | Instructor noted PDFs, TXT, DOC as possible formats; no text-file or webpage scraping/HTML loader walkthrough in this session. |
| Process and Organize Document Data — Clean and structure raw content | Covered | Parsing and cleaning explained (headers, footers, extra spaces, etc.); `clean`/`make_document` pattern in demo; OCR/images in PDFs discussed tangentially via Q&A. |
| Apply Chunking to Policy Documents — Split into meaningful chunks | Covered | Motivation vs whole-document retrieval; fixed-size chunking and word-based splitting in code discussion. |
| Configure Chunk Size and Overlap — Strategies for retrieval quality | Covered | Explicit chunk overlap concept (job handover analogy); practical ranges (e.g. ~120 words, overlap ~30 words, 10–20% overlap guidance). |
| Compare Chunking Outcomes — Analyze impact on search relevance | Covered | Iterate/tune chunk size and overlap; compare smaller vs larger chunks against answer quality. |
| Generate Embeddings for Policy Chunks — Vector representations | Covered | Embeddings explained; OpenAI `text-embedding-3-small` vs large model and dimension counts (e.g. 1536 vs 3072). |
| Store Policy Data in a Vector Database — Embeddings plus metadata such as policy type | Covered | ChromaDB persistent client, collection creation; embeddings stored with chunk text and metadata (file path, page, inferred policy type). |
| Build the Retrieval Layer for User Queries | Covered | Query → embedding → similarity search → top‑k chunks; tied to retrieval code path in session. |
| Construct Prompt Templates for Responses — Combine chunks with structured prompts | Covered | System/RAG prompt role; `build_prompt`-style pattern embedding context + query; customer-support instructions (use only policy context, avoid hallucinations). |
| Build an End‑to‑End Multi‑Document RAG System | Covered | Implemented pipeline across multiple PDFs in one project (dependencies, ingestion, chunking, embed, index, retrieve, generate). |
| Handle Updates to Policy Documents — Refresh knowledge base after add/modify | Not covered | Only briefly deferred to supplementary notes at close (delete/replace chunks and metadata concept); not taught or demoed step‑by‑step in session. |
| Extra (beyond listed LOs): requirements.txt bulk `pip install -r`; env vars for API keys; centralized model constants; virtualenv setup | Covered | Spent substantive time aligning with typical production Python workflow. |
| Extra: OCR — optical character recognition, LLM-assisted image text, enterprise email/image security anecdote | Covered | Substantial digression (~student question + instructor experience); instructional but not core RAG LO. |
