# Assignment Question QC Report — Session 27 (Open-Source LLMs)

**Source notes:** `Lecture Notes Released.md`  
**Reference checked:** Session 37 assignments (not reused as-is)  
**Artifacts reviewed:** `assignment-objective.md`, `assignment-subjective.md`

---

## Per-question QC table

| # | Type | Remarks |
|---|------|---------|
| Q1 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (open-source downloadable weights / offline local run). |
| Q2 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (`ollama pull` before `run`). |
| Q3 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (70B vs laptop RAM class warning). |
| Q4 | MCQ — Easy | Correct: **A**; relevancy: **Yes** (MMLU for broad knowledge benchmark). |
| Q5 | MCQ — Moderate | Correct: **B**; relevancy: **Yes** (OpenAI-compatible client + `localhost:11434/v1`). |
| Q6 | MCQ — Moderate | Correct: **B**; relevancy: **Yes** (local inference for privacy scenario). |
| Q7 | MSQ — Moderate | Correct: **A, C, D**; relevancy: **Yes** (tiny-model trade-offs; B is false trap). |
| Q8 | MSQ — Moderate | Correct: **A, C**; relevancy: **Yes** (fair local vs Ollama Cloud comparison). |
| Q9 | MSQ — Hard | Correct: **A, B, D**; relevancy: **Yes** (paid API vs open-weight self-hosting). |
| Q10 | MSQ — Hard | Correct: **A, B, D**; relevancy: **Yes** (local vs cloud endpoints, key, dummy local key; C is false). |
| Subjective | Python — local Ollama + Ollama Cloud resume compare | Medium difficulty: **Yes**; submission (Case C): **Yes**; dataset required: **No**. `OLLAMA_API_KEY` via `export` mentioned; `.env` / Groq **not** required per assignment brief. |

---

## Overall QC ratings (both assignments)

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Open-source vs paid, benchmarks, Ollama CLI, RAM/heavy-model risk, OpenAI-compatible local/cloud endpoints, privacy, fair comparison; subjective compares local vs Ollama Cloud on same HTML resume prompt. |
| Creativity | 5 | Scenario stems (offline hackathon, health-tech privacy, fair engine test); subjective resume generator keeps Session 37 theme with Session 27 API pattern. |
| Structural Adherence | 5 | 10 items: 4 Easy MCQ + 2 Moderate MCQ + 2 Moderate MSQ + 2 Hard MSQ; 1 subjective; Case C instructions; explanations included. |
| No Logical Mistakes | True | Keys verified against Session 27 notes; Q7 B and Q10 C are intentional false options; subjective uses taught OpenAI-compatible client for both modes. |
| No Presentation Mistakes | True | No “as taught in session” phrasing; grammar/spelling checked; progressive difficulty order. |

---

## Session 37 reuse log

| Session 37 item | Session 27 decision |
|-----------------|---------------------|
| Q1–Q4, Q7–Q8 (similar topics) | **Not copied** — fresh wording aligned to Session 27 notes |
| Q5 (Colab Secrets) | **Replaced** — not in Session 27 scope |
| Q6 (Anthropic API) | **Replaced** — Q5 tests OpenAI-compatible `base_url` switch |
| Q9 (training-data bias) | **Replaced** — Q9 tests paid vs open-weight characteristics |
| Q10 (modalities) | **Replaced** — Q10 tests Ollama Cloud vs local setup |
| Subjective (Groq + native HTTP) | **Rewritten** — local vs **Ollama Cloud** via `OpenAI` client; resume theme retained |

---

## Improvisation log

- **Round 1:** Fresh objective set + subjective resume generator (local vs Ollama Cloud, OpenAI-compatible client). No `.env` or Groq mandatory scope. Full QC — all criteria meet thresholds.

---

**QC sign-off:** Expected result satisfied — Content Coverage, Creativity, and Structural Adherence are **not less than 5**; **No Logical Mistakes** and **No Presentation Mistakes** are **True**.
