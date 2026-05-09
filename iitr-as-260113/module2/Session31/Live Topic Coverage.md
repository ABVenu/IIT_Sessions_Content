| Topic / subtopic | Status | Remarks |
| --- | --- | --- |
| Identify failure cases in the e-commerce assistant (incorrect, incomplete, irrelevant answers) | Covered | Wrong policy dates (30 vs 7 days), refund vs delivery timeline confusion, low-star failure analysis, wrong document retrieval |
| Evaluate retrieval quality (correct policy sections retrieved) | Covered | Framework: correct document → correct chunk; sample evaluation datasets; 0–2 retrieval scoring; pre-processing before retrieval (e.g. order lookup for ambiguous product type) |
| Evaluate response accuracy (answers reflect company policies) | Covered | Accuracy as primary goal; star / numeric scales; warranty vs liquid damage scoring examples |
| Detect hallucinations (responses unsupported by retrieved content) | Covered | Coupon-on-delay example; approximate framework: flag claims (timelines, coupons, etc.) and verify against retrieved text |
| Improve grounding (answers rely only on retrieved business information) | Covered | Definition recap; cite policy sections / references; answers must come only from retrieved chunks |
| Tune retrieval parameters (e.g. top-k, filtering) | Covered | Top-K tuning workflow; trade-off low K misses context vs high K adds noise; ties to precision |
| Refine chunking strategy based on results (chunk size, overlap, retrieval performance) | Partially covered | Document vs chunk and “right chunk” checks in evaluation and indexing setup mentioned; no systematic tuning of chunk size/overlap from evaluation outcomes |
| Improve prompt design for policy-based answers | Covered | Weak vs strong templates; use-only-context; refuse when unknown (“I don’t know”) vs hallucinating |
| Apply metadata filtering for precision (e.g. returns vs shipping) | Covered | Restrict similarity search to refund-tagged documents example; pointer to prior implementation class |
| Balance precision vs recall in retrieval | Covered | Definitions, formulas/examples; precision vs recall trade-offs; top-K recall metric and semantic-search ordering caveat |
| Incorporate user feedback for improvement | Covered | Post-query ratings/thumbs; structured follow-up questions; using feedback after launch |
| Establish continuous evaluation practices | Covered | Subjective quality vs binary correctness; internal test loops (many runs); periodic re-evaluation with feedback cadence (daily/weekly) |
| **Extra (not listed as formal LOs but taught at length)** | Covered | Retriever vs generator and “garbage in, garbage out”; prioritize improving retriever; properties of a good RAG (accuracy, grounding, completeness, safety/privacy, freshness); embedding dimensions / semantic search nondeterminism discussion; COD vs online refund routing nuance |
