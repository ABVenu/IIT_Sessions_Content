| Topic / Sub topic | Status | Remarks |
| --- | --- | --- |
| Incremental indexing & updates | Not covered | No discussion of re-indexing, delta updates, or keeping indices in sync when documents change. Session covered hierarchical indexing (structure/relationships between chunks and documents), not incremental maintenance. |
| RAG evaluation metrics (relevance, faithfulness, context precision) | Not covered | No systematic treatment of RAG evaluation. The word “precision” appears only in the sense of retrieval/chunk granularity (small chunks vs large chunks), not evaluation metrics such as context precision or faithfulness. |
| Automated testing frameworks for RAG systems | Not covered | No mention of test harnesses, CI, golden sets, or RAG-specific automated testing tools. |
| A/B testing RAG systems | Not covered | No discussion of experiments, traffic splits, or comparing RAG variants. |
| Debugging retrieval issues | Not covered | No structured debugging workflow, logging/observability for retrieval, or systematic troubleshooting of bad retrievals. |
| Performance optimization techniques | Partially covered | End-of-session Q&A only: agents slow as conversations grow due to more text to process; caching and keeping information in memory mentioned as mitigation—not a broader optimization segment (latency, throughput, batching, etc.). |
| Production RAG best practices | Not covered | Passing references only (e.g., production applications, topic tracking not used alone in production). No consolidated production checklist, monitoring, or operational practices. |
| Query expansion and reformulation (extra) | Covered | Substantial time: definitions, LLM-assisted expansion/reformulation, combining both, conversation-aware reformulation. |
| Citations and source tracking (extra) | Covered | Substantial time: transparency/trust, metadata on chunks, document/section/page/line/inline citation levels, hallucination risk in citations. |
| Semantic chunking (extra) | Covered | Substantial time: vs fixed-size chunking, meaning-based splits, embedding similarity to merge adjacent chunks, topic-oriented chunking, tradeoffs and limitations. |
| Hierarchical indexing in RAG (extra) | Covered | Substantial time: chunk–document–section relationships, flat vs hierarchical retrieval, strategies and benefits/costs. |
| Prior-session retrieval strategies — recall (extra) | Covered | Short recap: similarity search limitations, MMR, hybrid (similarity + keyword). |
| Multi-modal RAG (extra) | Not covered | Explicitly deferred to a future session (time constraints). |
