# Lecture Notes QC Report — Open-Source LLMs

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-06-27  
**Iteration:** 1

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics covered: (1) Ollama install + laptop-appropriate light model validation via CLI health checks and install activity; (2) programmatic Python chat via `ask_ollama_local.py` and `from ollama import chat`; (3) local vs Ollama Cloud comparison on identical prompt with `USE_CLOUD` in `.env`; (4) secure credential handling via `.env`, `.env.example`, `.gitignore`, and `python-dotenv` in capstone script. Reused from iitr-as-260313 Session25 (same lecture). |
| **Creativity** | **5 / 5** | App store + player analogy; private placement notes; hostel whiteboard vs sticky note for `.env`; scooter vs truck for model size; train meeting problem for fair compare; campus breakfast prompt; IRCTC-style privacy framing retained. |
| **Structural Adherence** | **5 / 5** | `#` title only; context paragraph + bullet LOs aligned to metadata; Official/Simple/Real-life on new terms; full Python with per-line comments + "How the code works"; student-facing `[ Student Activity ]` blocks; Key Takeaways; Important Commands table; nine diagram images. |
| **No Logical Mistakes** | **True** | Local `chat()` → localhost:11434; cloud `Client` + Bearer token; model must be pulled before use; tiny models trade quality for speed; fair compare uses same prompt; `.env` excluded from Git; `USE_CLOUD` branch logic correct. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; paragraphs ≤3 sentences; professional documentation tone; activities not instructor-facing. |
| **No Previous Session Number References** | **True** | Uses **previous session** only; no `Session N` in student-facing text. Image URLs contain path segments only — not cited in prose. |
| **No Metadata/internal reference** | **True** | No session duration, "light model" as internal instruction label, or cohort-internal spillover notes in student text. |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC passed on iteration 1.

---

## Alignment Checklist (metadata subtopics → notes sections)

| Metadata subtopic | Section in notes |
|---|---|
| Ollama installation and validation with laptop-appropriate local model | Install Ollama and Validate; Pull a Light Model and Run Your First Prompt (CLI) |
| Programmatic chat completion against Ollama from Python | Call Ollama from Python (Local) — `ask_ollama_local.py` |
| Compare local vs Ollama Cloud on identical prompt with env-driven config | Compare Local vs Cloud — One Script, Two Modes — `ask_ollama.py` |
| Secure credential handling; secrets out of version control | Ollama Cloud and Secure Credentials |

## Cohort-Specific Adaptation (vs iitr-as-260313 Session25)

| Item | Change |
|---|---|
| Title | `Open-Source LLMs` (from Session27 metadata) |
| Context | Bridges from **previous** session on REST APIs, JSON, field mapping, and Groq — not ShopKart tool agent |
| Body tweak | Trade-offs section links prompt discipline to **mapping API facts into grounded prompts** |

**Approximate line count:** ~456 lines.

---

# Lecture Notes QC Report — Open-Source LLMs (Re-verification)

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-06-27  
**Iteration:** 2

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Re-verified all four subtopics and connecting flow: cloud vs local motivation → install → CLI → trade-offs → Python local → cloud + secrets → dual-mode capstone → takeaways. |
| **Creativity** | **5 / 5** | Analogies remain varied and India-relatable; comparison table and discussion table support lab reflection. |
| **Structural Adherence** | **5 / 5** | Prompt4 structure intact; no Part/Section labels; Key Takeaways forward-link to LangChain without session numbers. |
| **No Logical Mistakes** | **True** | Re-checked code paths, model tier guidance, and cloud auth pattern after context edits. |
| **No Presentation Mistakes** | **True** | Confirmed no duration, audience, or internal instruction leakage. |
| **No Previous Session Number References** | **True** | Confirmed — only "previous session" phrasing. |
| **No Metadata/internal reference** | **True** | Confirmed. |

**Outcome:** QC passed on iteration 2 — expected QC result achieved.

---

# Lecture Notes QC Report — Open-Source LLMs (Released Alignment)

**File reviewed:** `Lecture Notes Released.md`  
**Review date:** 2026-06-30  
**Iteration:** 3  
**Basis:** Live Topic Coverage report + session transcript alignment pass

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Aligned to what was taught: paid vs open-source models; LLM benchmarks; cloud vs local trade-offs (latency, privacy); Azure Foundry overview; Ollama install/validate; model library sizing; CLI pull/run; Python via **OpenAI-compatible** client (primary in-class pattern); Ollama Cloud + Groq vs Ollama Cloud speed compare; `.env` / `.gitignore` / Groq + Ollama keys. Removed uncovered dual-mode `USE_CLOUD` capstone and identical local-vs-cloud side-by-side script. Native `ollama import chat` kept as optional one paragraph (briefly shown in class). |
| **Creativity** | **5 / 5** | Netflix vs DVD; board exam mark sheets; Swiggy vs hostel kitchen; Tesla/bank privacy; sticky note vs whiteboard; scooter vs truck retained; timed cloud compare activity added. |
| **Structural Adherence** | **5 / 5** | `#` title; context + LO bullets; Official/Simple/Real-life on new terms; full Python with per-line comments + "How the code works"; student-facing activities; Key Takeaways; terminology table; four retained diagram images (dual-mode toggle image removed — topic not taught). |
| **No Logical Mistakes** | **True** | OpenAI client → localhost for local, `https://ollama.com/v1` + key for cloud; model must be pulled; tiny models trade quality for speed; `.env` excluded from Git; Groq/Ollama Cloud compare framed as provider speed demo, not false local-vs-cloud capstone claim. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; no Mentimeter/poll content; professional documentation tone; paragraphs scannable. |
| **No Previous Session Number References** | **True** | Uses **previous session** only; no `Session N` in student text. |
| **No Metadata/internal reference** | **True** | No internal alignment labels or instructor-only spillover in student text. |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC passed on iteration 3 — `Lecture Notes Released.md` ready for student release.

---

## Alignment Changes (vs pre-session `Lecture Notes.md`)

| Item | Action |
|---|---|
| Dual-mode `ask_ollama.py` + `USE_CLOUD` | **Removed** — not demonstrated live |
| Local vs cloud identical-prompt capstone | **Removed** — class compared Groq vs Ollama Cloud instead |
| Python local calling style | **Updated** — OpenAI-compatible client (in-class preference) |
| Native `from ollama import chat` as primary | **Demoted** to optional note |
| Paid vs open-source + benchmarks | **Added** — substantial class time |
| Azure Foundry enterprise path | **Added** |
| Ollama model library tour + sizing | **Added** |
| Groq vs Ollama Cloud speed section | **Added** |
| Dual-mode diagram (`session37-09`) | **Removed** |
| Poll / Mentimeter | **Excluded** — session protocol, not notes |

**Approximate line count:** ~430 lines.
