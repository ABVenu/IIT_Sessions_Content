# QC Report — Session 25: Ollama: Exploring Another World of LLMs

## QC Pass 1

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** Reused and adapted Session37 (iitr-as-2601) Ollama notes for iitr-as-260313 Module 3 Session25. **All four metadata subtopics covered:** (1) Ollama install + light model validation via CLI health checks and student install activity; (2) programmatic Python chat via `ask_ollama_local.py` and `from ollama import chat`; (3) local vs Ollama Cloud comparison on identical prompt with environment-driven `USE_CLOUD` toggle; (4) secure credential handling via `.env`, `.env.example`, `.gitignore`, and `python-dotenv` integrated into cloud and capstone scripts. **Adaptations:** title set to metadata title; context paragraph references previous Module 2 ShopKart tool agent (Groq) instead of Prompt Engineering-only framing; added dedicated **Secure Credential Handling** section; capstone script uses `load_dotenv()`. **Removed from source:** activity time durations (10/15/20/25/30 min), instructor-only spot-check line. **Retained:** all 9 diagram images, full code with per-line comments, Official/Simple/Example blocks, student activities in professional voice, Key Takeaways, terminology table. No session numbers or duration metadata in student-facing text.

**Pass 1 outcome:** PASS

---

## QC Pass 2 (Re-verification)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** Re-verified subtopic alignment against metadata.md — install/validate, Python API, local-vs-cloud compare, secrets out of version control. Confirmed connecting sentences between sections (cloud vs local → Ollama → install → CLI → trade-offs → Python → cloud → `.env` security → compare → modalities → embeddings → capstone). Paragraphs follow 3-sentence rule; headings are direct (no Part/Section labels). Groq references are accurate for this cohort’s prior work. Code paths are consistent: local uses default `chat()`, cloud uses `Client` with Bearer token, capstone branches on `USE_CLOUD`. Student activities use `[ Student Activity ]` blocks without “Ask students to…” phrasing. Key Takeaways link forward to LangChain without session numbers.

**Pass 2 outcome:** PASS — expected QC result achieved.

---

## QC Pass 3 (Trimmed for 1h50m scope)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** Reduced from ~801 to ~340 lines. **Removed** (not in metadata): embeddings deep-dive, modality/model-types section, open-source ecosystem section, duplicate `ask_ollama_cloud.py`, standalone `load_secrets.py`, separate trade-offs section (folded into light-model bullets). **Retained all 4 subtopics:** install/validate, Python API (`ask_ollama_local.py`), local-vs-cloud compare, `.env`/`.gitignore` security in capstone `ask_ollama.py`. Four key images kept. Length aligned with comparable 1h50m notes (~450 lines in Session26).

**Pass 3 outcome:** PASS

---

## QC Pass 4 (Expanded to ~450 lines)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** Expanded from ~350 to ~450 lines per request. **Added back:** per-OS install steps, pull/run image, trade-offs section, Ollama capabilities preview table, cloud setup (`signin`, terminal export), local-vs-cloud code comparison table, discussion table, secret-hygiene activity, expanded terminology. **Still excluded:** full embeddings lab, modality deep-dive, duplicate `ask_ollama_cloud.py` — not required by metadata. All four subtopics remain fully covered.

**Pass 4 outcome:** PASS

---

## QC Pass 5 (Fresh audit — current 451-line notes)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 4 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | False |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** **Content:** All four metadata subtopics and five topic areas covered — install/validate (`ollama --version`, `ollama list`, light model pull/run), Python API (`ask_ollama_local.py`), local-vs-cloud compare (identical prompt, `USE_CLOUD`, discussion table), secure credentials (`.env`, `.env.example`, `.gitignore`, `python-dotenv`). **Creativity:** Swiggy vs home cooking, chai machine, hostel whiteboard/drawer analogies; Indian context (Delhi–Mumbai prompt, college breakfast). **Structural gaps:** Capstone `ask_ollama.py` and local script missing **per-line comments** on several lines (prompt rule 5); Key Takeaways had **6 bullets** (prompt asks 3–5). **No session numbers, duration, or internal metadata** in student text. **Module 2** reference is module-level context only — acceptable. Logic and code paths verified correct.

**Pass 5 outcome:** FAIL — Structural Adherence & Presentation Mistakes below threshold. Fixes applied.

---

## QC Pass 6 (Re-verification after fixes)

| Criterion | Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |
| **No Previous Session Number References** | True |
| **No Metadata / Internal References in Student Notes** | True |

**Notes:** **Fixed:** Per-line English comments added to `ask_ollama_local.py` and `ask_ollama.py`; Key Takeaways trimmed to **5 bullets**. Re-verified: context paragraph links previous ShopKart/Groq work to Ollama entry point; connecting sentences between CLI → trade-offs → Python → cloud → `.env` → capstone; Official/Simple/Example blocks on Ollama, pull/run, cloud, `.env`; five student activities in professional voice; six images with alt text; terminology table complete; no duration or session-number leakage. Full capstone code with `load_dotenv`, `ask_local`, `ask_cloud`, `main`, and `if __name__` pattern intact.

**Pass 6 outcome:** PASS — expected QC result achieved.
