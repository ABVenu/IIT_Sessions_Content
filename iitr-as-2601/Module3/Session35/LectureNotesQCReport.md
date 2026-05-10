# Lecture Notes QC Report — Session 35: GenAI Concepts for Beginners

---

## Iteration 1

### Criteria Evaluation

| Criteria | Rating / Result |
|---|---|
| Content Coverage | 5 / 5 |
| Creativity | 5 / 5 |
| Structural Adherence | 5 / 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

### Detailed Notes

**Content Coverage — 5/5**
All 10 subtopics from the metadata are addressed:
- Classical ML limitations on language ✅
- Word ambiguity and rule-based NLP failure ✅
- Neural network intuition (architecture + learning loop) ✅
- Rise of LLMs (Word2Vec → RNN → Transformer → ChatGPT + pre-training) ✅
- Tokens with live `tiktoken` code demo ✅
- Context windows with size comparison table and estimation activity ✅
- Probabilistic text generation with the sentence completion activity ✅
- Temperature with code demo and use-case table ✅
- Hallucinations with real-world examples and activity ✅
- Vocabulary recap embedded in Quick Reference Table ✅
- Previous session context added correctly (Session 34: ML Workshop — Model Selection & Comparison) ✅
- Module 3 preview added at the end ✅

**Creativity — 5/5**
- Activity 1 (tiktoken live demo): hands-on tokenisation with real code
- Activity 2 (context window estimation): makes an abstract concept concrete with arithmetic students can do in-class
- Activity 3 (sentence completion game): experiential understanding of probabilistic generation before explaining the concept
- Activity 4 (spot the hallucination): active learning exercise using real-world examples (Eiffel Tower, Python version, legal ruling)
- Comparison tables (LLM vs Search Engine, Temperature guide, Context Window sizes) add visual variety and quick-reference value
- Real documented incidents (fake legal citations, medical misinformation) used to ground the hallucination section

**Structural Adherence — 5/5**
- Notes start directly with `# Lecture Title` — no metadata header ✅
- Context of session section present with previous session recap and current session overview ✅
- 3-sentence rule followed throughout — no paragraph exceeds 3 sentences ✅
- Connecting sentences used between sections to bridge topics smoothly ✅
- Every new concept follows: Official Definition → In Simple Words → Real-Life Example ✅
- All code is complete (no partial snippets), every line has a comment, and "How the code works" bullet lists follow each code block ✅
- Key Takeaways section present with 5 bullets + link to next session ✅
- Quick Reference Table present at the end ✅
- No "Part 1 / Section A" style headings used ✅

**No Logical Mistakes — True**
- Word2Vec → RNN → Transformer timeline is historically correct
- Token count rule of thumb (1 token ≈ 0.75 words) is accurate
- Temperature range (0–2) is accurate for OpenAI API
- Context window sizes cited are accurate as of knowledge cutoff
- The distinction between pre-training and fine-tuning is correctly explained
- Hallucination Activity answers are accurate (1889 World Fair error identified, Python 4.0 non-existence confirmed)

**No Presentation Mistakes — True**
- All markdown tables render correctly (headers + alignment)
- Code blocks use correct Python syntax
- Bold formatting used consistently for key terms
- No broken links or missing image references
- Consistent heading hierarchy (##, ###) throughout
