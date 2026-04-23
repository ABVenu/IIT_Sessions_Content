| Detailed subtopic | Coverage | Technical coverage in transcript |
| --- | --- | --- |
| Revisit how LLMs generate responses (pretrained knowledge) | Strong | Pre-trained models; trained on large public/internet data; user query → LLM processes prompt and generates response. |
| Limitations of LLM knowledge (static, domain context, external/real-time data) | Strong | Cutoff date; static knowledge; no private/internal policy docs in weights; no internet/external call unless integrated; policies change post-cutoff. |
| Hallucination (incorrect/fabricated answers; missing knowledge) | Strong | Defined as guessing/fabrication when answer unknown; contrast with refuse; undesirable; mitigation via context/RAG; RAG can still hallucinate if context missing. |
| Need for grounded AI (external, verifiable information) | Strong | Grounded = reliable/verifiable sources, not memory-only; Amazon checking policy docs; answers with sources/links; hallucinating system ≠ grounded. |
| Introduce RAG (retrieval + generation) | Strong | Full form; approach combining retrieval from external sources with natural-language generation. |
| Grounding in RAG (external data supports/justifies answers) | Strong | Context passed to LLM; Microsoft HR example; citations; “sugar-coating” policy into user-facing text while tied to retrieved text. |
| High-level RAG flow: query → retrieve → context → generate | Strong | Four steps and full pipeline: embed query, similarity search, top-k, provide documents/context to LLM, generate response. |
| LLM-only vs RAG-based responses | Strong | Comparison table: knowledge source, latest info (KB updates), private data, hallucination risk (high vs lower, with caveats). |
| RAG and vector search systems | Strong | Embeddings, nearest/top-k vectors, vector DB (e.g. ChromaDB), semantic meaning; metadata filter + similarity for relevance; chunking for long PDFs/docs. |
| Real-world use cases: enterprise knowledge assistants; document Q&A; domain-specific chat | Partial–strong | **Enterprise knowledge assistant** named explicitly; Microsoft Ask HR; long documents/PDFs and chunking support **document-style Q&A**; **Domain-specific** illustrated via banking/internal docs (e.g. American Express), not a broad list of verticals (e.g. medical/legal). |
| RAG in agentic systems (retrieval for knowledge and decisions) | Strong | Agents/chatbot agents retrieve policies; perceive–reason–act; wrong reasoning/hallucination before action → bad actions; RAG for more reliable decisions; enterprise bot extended with actions (leave/reimbursement). |
| Importance of retrieval for response quality | Strong | Stated as explicit subtopic; retrieval must be reliable/accurate; wrong flight info → wrong booking; better filtering + similarity → more accurate answers. |
