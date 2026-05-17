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
