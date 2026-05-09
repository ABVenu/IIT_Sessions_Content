# Assignment Question QC Report
**Session:** Session31 — Evaluating and Improving RAG Systems
**Module:** module2

---

## Objective Assignment QC

| Q# | Type | Correct Option | Correct Option Relevant to Question? | Remarks |
|----|------|---------------|--------------------------------------|---------|
| Q1 | MCQ (Easy) | B — The Retriever | Yes | Tests the librarian analogy and core principle of fixing retriever first. Correct option is directly supported by session content. Distractors (LLM, Embedding Model, VectorDB) are plausible but clearly distinguishable. |
| Q2 | MCQ (Easy) | C — Outdated policy document retrieved | Yes | Tests the Freshness failure case. Scenario is grounded in the session's 7-days vs. 30-days example. Distractors are meaningful wrong paths students might take. |
| Q3 | MCQ (Easy) | C — Grounding | Yes | Tests identification of the Grounding property. Response example cites a document section, which is the definition of grounding from the session. Distractors are other valid RAG properties. |
| Q4 | MCQ (Easy) | C — Score 0, completely irrelevant document | Yes | Tests the 0–2 Retrieval Scale. Session explicitly uses refund-vs-shipping as the Score 0 example. Distractors probe common misconceptions (partial relevance, any retrieval = success). |
| Q5 | MCQ (Moderate) | B — Precision 75%, Recall 50% | Yes | Tests application of Precision and Recall formulas. Arithmetic is verified: 3/4 = 75%, 3/6 = 50%. Distractors are plausible transpositions/wrong calculations. Scenario uses a new domain (cancellation) to avoid direct recall of the textbook example. |
| Q6 | MCQ (Moderate) | C — Score 1, partial (hallucination present) | Yes | Tests application of 0–3 Response Accuracy Scale with a hallucination scenario. Hallucinated claim (tracking upgrade) is specific and concrete — clearly Score 1, not Score 2. Explanation differentiates Score 1 vs. Score 2 clearly. |
| Q7 | MSQ (Moderate) | A, B, C, E — Accuracy, Freshness, Grounding, Completeness | Yes | Tests recall of the 5 essential RAG properties. Distractor D (Response Speed) is not in the session's list. Safety & Privacy was included conceptually but dropped from options to keep it at 4 correct answers — replaced with a clear non-answer. Note: Safety & Privacy is a valid 5th property but not tested here to keep question manageable. |
| Q8 | MSQ (Moderate) | A, B — Decrease top-K, Apply metadata filtering | Yes | Tests knowledge of precision improvement techniques. Session explicitly lists exactly these two methods. Distractors (increase K, more test queries, consistency runs) are related activities but do not improve precision. |
| Q9 | MSQ (Hard) | A, B, D, E — Grounded first part, hallucination identified, payroll doc scored 0/1, response scored 1 | Yes | Tests multi-layered analysis: grounding identification, hallucination detection, retrieval scoring, and response accuracy scoring simultaneously. Scenario is novel (HR/legal context) — tests genuine understanding, not recall. Distractor C (Score 3) is a clear wrong answer; requires students to correctly rule it out by identifying the hallucination. |
| Q10 | MSQ (Hard) | B, C, D, E, F — All systematic improvement steps except replacing the LLM | Yes | Tests knowledge of the complete evaluation and improvement loop. Distractor A (replace LLM) directly contradicts the session's core principle: fix the retriever before blaming the LLM. All 5 correct options map to specific framework steps from the session. |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Mentioned | Dataset/Special Resources Needed | Remarks |
|----|------|-----------|----------------------------------|----------------------------------|---------|
| Q1 | Applied Theory (Document Design Task) | Medium | Yes — Google Doc with public sharing link | No external dataset required; student creates their own evaluation scenarios | Question requires genuine application of core session concepts across 4 sections: evaluation dataset, failure case analysis, prompt template design, and continuous improvement plan. Not a direct recall question — requires synthesis and creative design in a new domain (healthcare). Submission format is appropriate for a structured document with tables and diagrams. |

---

## Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Content Coverage | 5/5 | All major session concepts covered: Retriever role, Freshness failure, Grounding, 0–2 Retrieval Scale, Precision/Recall formulas, 0–3 Response Accuracy Scale, RAG properties, Precision improvement techniques, Hallucination detection, Continuous improvement loop |
| Creativity | 5/5 | Questions use novel scenarios (HR chatbot, travel startup, fintech, legal assistant) beyond the session's e-commerce examples. Scenarios are relatable and realistic. No question is a direct restatement of a session example. |
| Structural Adherence | 5/5 | Exactly 10 questions: 4 Easy MCQ + 2 Moderate MCQ + 2 Moderate MSQ + 2 Hard MSQ. Ordered Easy → Moderate → Hard. Each question has correct answers and full answer explanations with why incorrect options are wrong. |
| No Logical Mistakes | True | All Precision/Recall calculations verified (Q5: 3/4=75%, 3/6=50%). All scoring scale applications verified against session definitions. All correct options confirmed against session content. |
| No Presentation Mistakes | True | All questions are clearly worded. No grammatical or spelling errors. Options are unambiguous. All scenario contexts are consistent within each question. |

### Subjective Assignment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Content Coverage | 5/5 | All major session topics are tested through the 4-section plan: evaluation dataset (Section 1), failure case analysis (Section 2), prompt template design (Section 3), continuous improvement loop (Section 4) |
| Creativity | 5/5 | Uses a healthcare domain (MediAssist) — completely different from the session's e-commerce context — requiring genuine transfer of knowledge. Multiple sections require original design (prompt template, metadata categories, failure scenarios) rather than copying session examples. |
| Structural Adherence | 5/5 | 1 subjective question as required. Difficulty is medium (analysis + design, not basic recall). Submission instructions follow Case B format (Google Doc with public sharing). No coding required — appropriate for a pure theory session. |
| No Logical Mistakes | True | Scoring scale instructions (0–2 and 0–3) are correctly referenced. Submission instruction pathway is correctly matched to the question type (document-style theory question → Google Doc). |
| No Presentation Mistakes | True | All six sections are clearly labeled with precise deliverables. The "Answer Explanation (for Evaluators)" section gives concrete guidance on what a strong submission looks like without being prescriptive to learners. No grammatical or spelling errors. |
