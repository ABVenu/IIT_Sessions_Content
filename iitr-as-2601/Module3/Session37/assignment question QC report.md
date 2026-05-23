# Assignment Question QC Report — Session 37 (Open-Source LLMs)

**Source notes:** `Lecture Notes Released.md`  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`

---

## Per-question QC table

| # | Type | Remarks |
|---|------|---------|
| Q1 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (local LLM / on-device privacy scenario). |
| Q2 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (`ollama pull` before `run`). |
| Q3 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (70B vs laptop RAM class warning). |
| Q4 | MCQ — Easy | Correct: **A**; relevancy: **Yes** (local cost/privacy vs Groq speed trade-off). |
| Q5 | MCQ — Moderate | Correct: **B**; relevancy: **Yes** (Colab `GROQ_API_KEY` secret naming/access). |
| Q6 | MCQ — Moderate | Correct: **A**; relevancy: **Yes** (Anthropic `messages.create` vs OpenAI-style). |
| Q7 | MSQ — Moderate | Correct: **A, C, D**; relevancy: **Yes** (tiny-model trade-offs; B is false trap). |
| Q8 | MSQ — Moderate | Correct: **A, C**; relevancy: **Yes** (fair model comparison). |
| Q9 | MSQ — Hard | Correct: **A, C, D**; relevancy: **Yes** (training-data bias builder view). |
| Q10 | MSQ — Hard | Correct: **A, B, C**; relevancy: **Yes** (modalities + pull/run; D false on embeddings depth). |
| Subjective | Python — local Ollama + Groq resume compare | Medium difficulty: **Yes**; submission (Case C): **Yes**; dataset required: **No**. `GROQ_API_KEY` via env/Colab Secrets mentioned; Ollama Cloud **not** required (aligned with Session 37 Groq focus). |

---

## Overall QC ratings (both assignments)

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Local vs cloud, Ollama CLI, RAM/heavy-model risk, Groq secrets, API pattern parity, bias, modalities; subjective compares local Ollama HTTP vs Groq `chat.completions.create` on same HTML resume prompt. |
| Creativity | 5 | Scenario stems (law college privacy, fair model test); subjective resume generator mirrors Session 34 pattern with Groq instead of Ollama Cloud. |
| Structural Adherence | 5 | 10 items: 4 Easy MCQ + 2 Moderate MCQ + 2 Moderate MSQ + 2 Hard MSQ; 1 subjective; Case C instructions; explanations included. |
| No Logical Mistakes | True | Keys verified against notes; Q7 B and Q10 D are intentional false options; subjective scope excludes Ollama Cloud. |
| No Presentation Mistakes | True | No “as taught in session” phrasing; grammar/spelling checked; progressive difficulty order. |

---

## Improvisation log

- **Round 1:** Initial wellness-bot subjective; objective unchanged.  
- **Round 2:** Subjective replaced with Session 34–style resume generator; **Groq** (`GROQ_API_KEY`) replaces Ollama Cloud; local Ollama HTTP unchanged. Subjective QC re-run — all criteria still meet thresholds.

---

**QC sign-off:** Expected result satisfied — Content Coverage, Creativity, and Structural Adherence are **not less than 5**; **No Logical Mistakes** and **No Presentation Mistakes** are **True**.
