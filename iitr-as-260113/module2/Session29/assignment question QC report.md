# Assignment Question QC Report
## Session 29 — RAG Architecture and Pipeline

---

## Part 1: Objective Assignment QC

| Q# | Type | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|----|------|-------------------|--------------------------------------|---------|
| Q1 | MCQ (Easy) | B) Retrieval-Augmented Generation | Yes | Question framed via relatable e-commerce scenario. All distractors are plausible-sounding but clearly incorrect. Correct answer directly maps to RAG definition taught in session. |
| Q2 | MCQ (Easy) | C) Retriever | Yes | Scenario-based question on the Retriever component. Distractors (Generator, Prompt Builder, Knowledge Source) are all real RAG terms from the session, making it non-trivial. Correct answer is unambiguous. |
| Q3 | MCQ (Easy) | C) Knowledge Sources | Yes | Applied scenario with the five policy documents. Distractors use real RAG vocabulary (Embeddings, Vector Chunks) to test precise understanding. Correct answer directly matches the session definition. |
| Q4 | MCQ (Easy) | D) `PersistentClient` | Yes | Practical scenario about data surviving across script runs. Distractors are either non-existent modes or in-memory modes. Correct answer (`PersistentClient`) is exactly the mode used in session code. |
| Q5 | MCQ (Moderate) | C) Only one chunk retrieved, missing context for one topic | Yes | Applied scenario testing understanding of `top_k` impact on multi-topic queries. Tests conceptual depth, not just recall. Correct answer reflects the core Top-K tradeoff explained in session. |
| Q6 | MCQ (Moderate) | C) Lower cosine distance = higher semantic similarity | Yes | Practical inspection scenario using `distance` values from session code output. Tests understanding of cosine distance interpretation. Distractors include common misconceptions (keyword count, token size). |
| Q7 | MSQ (Moderate) | A, B, D | Yes | Tests the `upsert` operation from `index_policy_documents()`. All three correct options are explicitly taught. Distractor C tests the distinction between `add` (which errors) and `upsert`. Distractor E is a clear misconception. |
| Q8 | MSQ (Moderate) | A, C, D | Yes | Tests chunking rationale from the session. Correct options map directly to stated reasons for chunking (precision, noise reduction, retrieval accuracy). Distractor B tests the anti-pattern (whole doc as one chunk). Distractor E is a common LLM misconception. |
| Q9 | MSQ (Hard) | A, B, C, E | Yes | Debugging scenario testing multiple root causes of retrieval failure. Requires integration of top_k, indexing, embedding quality, and phrasing concepts. Distractor D correctly identifies that cosine similarity has no category bias. High cognitive demand appropriate for Hard level. |
| Q10 | MSQ (Hard) | B, C, D, F | Yes | Tests deep understanding of `build_grounded_prompt()` function roles. Requires students to distinguish between what the prompt builder does vs. what the embedder and API caller do. All correct options map to explicit code behavior from session. |

---

## Part 2: Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Mentioned | Dataset Needed | Remarks |
|----|------|------------|----------------------------------|----------------|---------|
| Q1 | Coding Implementation (RAG Pipeline) | Medium | Yes — Case D (GitHub repo with module2/Session29 folder structure; `.gitignore`, `requirements.txt`, `README.md` specified) | No external dataset required — students write their own HR policy text | Creative applied scenario (HR domain vs. e-commerce from session). Requires building all 7 functions end-to-end. Side-by-side comparison task reinforces the grounded vs. ungrounded concept. Scope is well-bounded within session content. Fallback rule instruction and API key environment variable constraint add real-world rigor. |

---

## Part 3: Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Questions span all major session topics: RAG definition, Retriever, Knowledge Sources, ChromaDB PersistentClient, top_k, cosine distance, upsert, chunking rationale, retrieval debugging, and prompt builder. |
| Creativity | 5 | All questions are framed as applied scenarios (e-commerce startup, HR manager, debugging session). No dry recall-only questions. Even Easy questions use practical context. |
| Structural Adherence | 5 | Exactly 10 questions: 6 MCQs (4 Easy + 2 Moderate) + 4 MSQs (2 Moderate + 2 Hard). Questions ordered progressively Easy → Moderate → Hard. All answer explanations include correct answer rationale and explanation of why wrong options are incorrect. |
| No Logical Mistakes | True | All correct options are verifiable against session content. Distractors are plausible but clearly distinguishable with knowledge. No impossible scenarios or contradictory options. |
| No Presentation Mistakes | True | Consistent formatting across all questions. Question stems are complete sentences. All options are grammatically parallel. No spelling or grammar errors detected. |

### Subjective Assignment

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Task requires implementing all major pipeline components taught in session: embeddings, ChromaDB setup with PersistentClient, upsert indexing, retriever function, prompt builder with grounding rules, LLM generator, and complete RAG pipeline function. Top-K and RAG vs. no-RAG comparison also covered. |
| Creativity | 5 | Scenario shifts from e-commerce (session) to HR domain — students must independently design policy content, making it a true applied knowledge exercise. Side-by-side comparison deepens conceptual understanding beyond mechanics. |
| Structural Adherence | 5 | Single practical task as specified. Difficulty is Medium as required. Submission instructions follow Case D format exactly (module2/Session29 folder path, repo instructions, gitignore guidance). Model solution includes walkthrough, expected output, and alternative approaches. |
| No Logical Mistakes | True | All function specifications are technically accurate and consistent with session code patterns. Constraint on `OPENAI_API_KEY` as env variable is a real-world best practice. No conflicting requirements. |
| No Presentation Mistakes | True | Clear step-by-step structure (Step 1–4). Function table is clean and readable. Constraints and submission instructions are in separate labeled sections. No spelling or formatting errors. |

---

## QC Summary

| Assignment | Content Coverage | Creativity | Structural Adherence | No Logical Mistakes | No Presentation Mistakes |
|------------|-----------------|------------|----------------------|--------------------|--------------------------| 
| Objective  | 5/5             | 5/5        | 5/5                  | True               | True                     |
| Subjective | 5/5             | 5/5        | 5/5                  | True               | True                     |

**QC Result: PASSED** — All ratings are 5/5. No logical or presentation mistakes found. Both assignments are ready for platform upload.
