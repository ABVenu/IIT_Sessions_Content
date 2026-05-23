# Assignment question QC report — Session 35

**Sources:** `OS_Assignment_Questions_GenerationPrompt.md`, `Lecture Notes Released.md`  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`  
**Revision:** Subjective shortened to **3 tasks** (Task 1 prompt · Task 2 chain + validation · Task 3 three lessons + loop)

---

## Per-question QC (objective)

| Question | Type | Remarks |
| --- | --- | --- |
| 1 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — real LLM apps need pre/post-processing, memory, retrieval, tools; framework value beyond one call. |
| 2 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — LangChain as backend orchestration layer on agentic stack. |
| 3 | MCQ (Easy) | Correct: **B**; relevancy: **Yes** — PromptTemplate runtime variables vs rewriting hard-coded strings. |
| 4 | MCQ (Easy) | Correct: **A**; relevancy: **Yes** — Runnable definition (invokable, composable unit). |
| 5 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — `limit` vs `word_count` key mismatch → missing variable error. |
| 6 | MCQ (Moderate) | Correct: **B**; relevancy: **Yes** — without StrOutputParser, rich AIMessage object vs plain string. |
| 7 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — templates, chains, provider abstraction; C false on model quality. |
| 8 | MSQ (Moderate) | Correct: **A, B, D**; relevancy: **Yes** — memory, indexes/RAG, embeddings; C false (agents ≠ fixed chain). |
| 9 | MSQ (Hard) | Correct: **A, B, C**; relevancy: **Yes** — packages, imports, string output; D false (API key still required). |
| 10 | MSQ (Hard) | Correct: **A, C, D**; relevancy: **Yes** — parallel independent steps, agent vs chain, LCEL pipe; B false on sequential chains. |

---

## Per-question QC (subjective)

| Item | Type | Remarks |
| --- | --- | --- |
| Task 1 | PromptTemplate | Medium; case **(c)**; one template with `{topic}`, `{audience}`, `{tone}`, `{limit}` + tone/analogy/word limit; relevancy: **Yes**. |
| Task 2 | LCEL + validation | `prompt \| llm \| StrOutputParser`; `validate_brief` keys + digit `limit`; relevancy: **Yes**. |
| Task 3 | Run loop | Three briefs from table; separator + invoke + length; keys match placeholders; relevancy: **Yes**. |
| Submission | case **(c)** | Single `.py`, run verified, paste in LMS; OPENAI_API_KEY via env; relevancy: **Yes**. |

---

## Overall QC — objective assignment

| Criterion | Rating / Result |
| --- | --- |
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

---

## Overall QC — subjective assignment

| Criterion | Rating / Result |
| --- | --- |
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Outcome:** All ratings ≥ 5; no logical or presentation issues after subjective shorten + 3-task restructure. No further revision required.

---

## OS prompt checklist (both assignments)

| OS requirement | Status |
| --- | --- |
| Exactly **2** assignments (objective + subjective) | Met |
| Objective: **10** Qs — 6 MCQ + 4 MSQ, Easy → Hard | Met |
| Subjective: **1** medium practical (3 clear sub-tasks in one file) | Met — `skillforge_explainer.py` |
| Scope limited to session notes | Met |
| Answer explanations | Met |
| QC table + overall ratings | Met |
