# Lecture Notes QC Report — Session 37: Open-Source LLMs

---

## QC Iteration 1

**Date:** 2026-05-15

**Evaluator:** Automated Self-Review

### Criteria Ratings

| Criteria | Rating (1–5) | Notes |
|---|---|---|
| **Content Coverage** | 5 | All 12 metadata subtopics covered: local vs cloud concept, install/verify, light model CLI, avoid heavy models, small-model trade-offs, Python local API, Ollama account/API key, cloud script, local vs cloud comparison, Ollama capabilities, model modalities, unified capstone script |
| **Creativity** | 5 | Indian analogies (Swiggy vs home cooking, chai machine, scooter vs truck, library shelves); 6 student activities; comparison tables; API flow image reused from prior session |
| **Structural Adherence** | 5 | Clean `#` title start; no metadata block at top; direct headings; context section with prior-session bridge; all “In Simple Words” blocks ≤3 sentences; Key Takeaways + Quick Reference Table present |
| **No Logical Mistakes** | True | Ollama CLI/API flow matches official docs (localhost:11434, cloud host https://ollama.com, Bearer auth); local vs cloud distinction accurate |
| **No Presentation Mistakes** | True | Full Python scripts with per-line comments and “How the code works” bullets; consistent formatting; no “Part 1” style headings |

### Issues Found

None. All criteria pass at level 5.

### Final Status: APPROVED ✓

The lecture notes meet all expected QC criteria. No further iterations required.

---

## Metadata Subtopic Checklist

| Subtopic (from metadata.md) | Covered in Lecture Notes |
|---|---|
| LLMs can run locally, not only paid cloud | ✓ § Cloud LLMs vs Local LLMs |
| Install Ollama and verify setup | ✓ § Installing Ollama |
| Pull light model + CLI prompt | ✓ § Pulling a Light Model |
| Avoid heavy models on regular laptops | ✓ § Pulling a Light Model (table + callout) |
| Trade-offs of very small models / hallucination | ✓ § Trade-offs of Very Small Local Models |
| Python script — local Ollama API | ✓ § Calling a Local Model from Python |
| Ollama account + free-tier API key | ✓ § Ollama Cloud |
| Update script for Ollama Cloud (host + key) | ✓ § Updating Python to Call Ollama Cloud |
| Compare local vs cloud on same prompt | ✓ § Comparing Local vs Ollama Cloud |
| Ollama capabilities: chat, generation, embeddings | ✓ § What Is Ollama + § Embeddings |
| Model types: text, vision, audio, video | ✓ § Model Types Available Through Ollama |
| One script for local or cloud | ✓ § One Python Script — Session Capstone |

---

## QC Iteration 2 — Lecture Notes Released (Post-Session Alignment)

**Date:** 2026-05-23

**Evaluator:** Post-session alignment against Live Topic Coverage + Transcript

### Criteria Ratings

| Criteria | Rating (1–5) | Notes |
|---|---|---|
| **Content Coverage** | 5 | Released notes match what was taught: full Ollama install/CLI/local trade-offs/modalities; Groq+Colab live path; OpenAI/Anthropic pattern parity; cloud same-prompt comparison; training-data bias; Gemini multimodal demo; enterprise on-prem. Removed not-covered items (Ollama API key creation, local vs Ollama Cloud comparison). Partially covered items retained (local Python Ollama, Ollama Cloud concept, embeddings as table mention only). |
| **Creativity** | 5 | Retained Indian analogies (Swiggy, chai machine, scooter vs truck); added bias spot-check and multimodal thought activities; provider comparison table. |
| **Structural Adherence** | 5 | Clean `#` title; prior-session bridge; Official Definition / In Simple Words / Real-Life Example pattern; Key Takeaways + terminology table; no session numbers; no Mentimeter/poll content. |
| **No Logical Mistakes** | True | Groq/OpenAI/Anthropic API shapes accurate; Ollama localhost:11434 correct; on-prem vs cloud trade-offs consistent with transcript; Ollama Cloud marked as concept-only where not demo'd live. |
| **No Presentation Mistakes** | True | Full code blocks with line comments and “How the code works”; images retained for covered sections (01–05, 07); removed images tied to cut sections (06 local-vs-Ollama-cloud, 08 embeddings, 09 capstone toggle). |

### Changes from Lecture Notes.md → Released

| Action | Section |
|---|---|
| **Removed** | Ollama account/API key walkthrough; full Ollama Cloud Python script; local vs Ollama Cloud comparison section + activity; embeddings deep-dive + image; unified capstone script + image; student cloud API key checklist |
| **Trimmed / reframed** | Intro and takeaways to include Groq; Ollama Cloud as concept-only; embeddings only in capabilities table |
| **Added** | Ollama GUI vs CLI; enterprise on-prem; training-data bias; Groq+Colab Secrets workflow; OpenAI/Anthropic patterns; cloud model comparison; Gemini Google Photos multimodal; tokens/compute notes in CLI section |

### Final Status: APPROVED ✓

Released notes aligned to session delivery. All QC criteria pass at level 5.
