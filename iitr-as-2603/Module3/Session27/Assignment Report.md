# Assignment Report — Session 27 (Open-Source LLMs)

**Session folder:** `IIT_Sessions_Content/iitr-as-2603/Module3/Session27`  
**Source notes:** `Lecture Notes Released.md`  
**Reference session checked:** `IIT_Sessions_Content/iitr-as-2601/Module3/Session37`  
**Decision:** Fresh assignment set created for Session 27; Session 37 files used only as structural reference.

---

## 1. Session comparison summary

Both Session 27 (cohort 2603) and Session 37 (cohort 2601) share the title **Open-Source LLMs** and cover Ollama installation, light local models, cloud-vs-local trade-offs, and Python API access. They are **not identical**, so Session 37 assignments cannot be copied as-is.

| Topic area | Session 27 (2603) | Session 37 (2601) |
|------------|-------------------|-------------------|
| Previous context | REST APIs → LLM prompts | Prompt Engineering |
| Primary Python pattern | **OpenAI-compatible client** (`OpenAI` + `base_url`) | Groq SDK + native Ollama HTTP in subjective |
| Cloud comparison focus | **Ollama Cloud** (`https://ollama.com/v1`) | Groq + Colab Secrets |
| Credentials | `.env` / VS Code (taught; optional in assignment) | Colab Secrets + `GROQ_API_KEY` |
| Extra theory | **Benchmarks**, Azure Foundry | Training-data bias, **modalities**, Anthropic API |
| Subjective intent (metadata) | Local vs cloud on same prompt | Local Ollama vs Groq resume compare |

---

## 2. Session 37 reuse assessment

### Objective — partial reuse only (6/10 aligned)

| Q# | Session 37 topic | Reusable for Session 27? |
|----|------------------|--------------------------|
| Q1 | Local Ollama for privacy | Yes |
| Q2 | `ollama pull` before `run` | Yes |
| Q3 | 70B on 8 GB RAM risk | Yes |
| Q4 | Local vs Groq trade-offs | Yes (local vs cloud framing) |
| Q5 | Colab Secrets for `GROQ_API_KEY` | **No** — Session 27 uses VS Code / `.env` |
| Q6 | Anthropic `messages.create` | **No** — not in Session 27 notes |
| Q7 | Tiny-model trade-offs | Yes |
| Q8 | Fair model comparison | Yes |
| Q9 | Training-data bias | **No** — Session 27 emphasizes benchmarks |
| Q10 | Model modalities | **No** — not in Session 27 notes |

### Subjective — not reusable as-is

Session 37 subjective uses `requests` POST to `/api/chat` for local and **Groq SDK** for cloud. Session 27 teaches the **OpenAI-compatible client** and **Ollama Cloud** as the cloud engine. The resume-comparison **theme** is retained; implementation spec is rewritten for Session 27.

Per assignment direction: **`.env` and Groq are not required** in the subjective — local vs **Ollama Cloud** only, with optional `OLLAMA_API_KEY` via environment variable.

---

## 3. What was created for Session 27

| File | Description |
|------|-------------|
| `assignment-objective.md` | 10 fresh questions (4 Easy MCQ + 2 Moderate MCQ + 2 Moderate MSQ + 2 Hard MSQ) scoped to Session 27 notes |
| `assignment-subjective.md` | Resume generator: **local Ollama** vs **Ollama Cloud** via OpenAI-compatible client; same creative theme as Session 37 |
| `assignment question QC report.md` | Per-question QC and overall ratings |

---

## 4. Session 27 objective coverage map

| Question | Difficulty | Session 27 topic tested |
|----------|------------|-------------------------|
| Q1 | Easy MCQ | Open-source weights vs paid API-only models |
| Q2 | Easy MCQ | `ollama pull` vs `ollama run` |
| Q3 | Easy MCQ | Heavy model RAM risk on student laptops |
| Q4 | Easy MCQ | Benchmark choice (MMLU for broad knowledge) |
| Q5 | Moderate MCQ | Switching Groq-style code to local Ollama (`base_url`) |
| Q6 | Moderate MCQ | Privacy-driven local inference scenario |
| Q7 | Moderate MSQ | Trade-offs of very small local models |
| Q8 | Moderate MSQ | Fair local vs cloud comparison practices |
| Q9 | Hard MSQ | Paid API vs open-source / self-hosted characteristics |
| Q10 | Hard MSQ | Ollama Cloud vs local setup (endpoint, key, model availability) |

---

## 5. Session 27 subjective design

- **Theme:** Generate HTML resume twice — once with a **small local model**, once with **Ollama Cloud** — then compare quality in comments (same idea as Session 37).
- **API pattern:** `OpenAI` client with `chat.completions.create` for both modes; only `base_url`, `api_key`, and `model` change.
- **Excluded from mandatory scope:** `.env` file setup, Groq, Colab Secrets, native `/api/chat` HTTP.
- **Submission:** Case C — single `resume_generator.py` pasted into LMS answer box.

---

## 6. Sign-off

Session 37 assignments were **reviewed and rejected for direct reuse**. Session 27 has a **fresh objective set** and a **rewritten subjective** that keeps the resume local-vs-cloud theme while matching Session 27 lecture scope and the OpenAI-compatible calling pattern taught in class.
