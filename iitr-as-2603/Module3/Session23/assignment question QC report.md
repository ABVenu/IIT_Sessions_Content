# Assignment Question QC Report — GenAI Concepts for Beginners

## Objective + Subjective QC Table

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (GenAI creates new text vs spam filter classifies) |
| Q2 | MCQ (Easy) | Correct option: A; relevancy to question: Yes (OTP flow suits rule-based deterministic logic) |
| Q3 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (token = smallest LLM text unit) |
| Q4 | MCQ (Easy) | Correct option: B; relevancy to question: Yes (rule-based = identical; LLM = may vary) |
| Q5 | MCQ (Moderate) | Correct option: B; relevancy to question: Yes (context overflow → truncation/loss) |
| Q6 | MCQ (Moderate) | Correct option: C; relevancy to question: Yes (4096 − 600 − 200 = 3296 usable input) |
| Q7 | MSQ (Moderate) | Correct options: A, B, D; relevancy to question: Yes (URL/Hinglish/Indian script token patterns) |
| Q8 | MSQ (Moderate) | Correct options: B, D, E; relevancy to question: Yes (probabilistic generation, OTP rules, deterministic rules) |
| Q9 | MSQ (Hard) | Correct options: A, B, C, D; relevancy to question: Yes (failure-mode scenario matching) |
| Q10 | MSQ (Hard) | Correct options: A, B, E; relevancy to question: Yes (tiktoken measure, reserve reply/buffer, split large docs) |
| Q1 | Subjective (Medium) | Medium difficulty: Yes; clear submission instructions (case c, single `.py`): Yes; dataset requirement: N/A — exact inline strings provided in question; token math verified (`"refund" * 4500` → 4500 tokens, overflow 1204) |

## Overall QC Ratings

| QC Parameter | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

## QC Outcome

All assignment files meet the expected quality threshold:

- **Structure:** 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Hard.
- **Scope:** Covers released notes — classical ML vs GenAI, rule-based vs LLM, tokens, context windows, `check_context_fit` math, hallucinations/failure modes, probabilistic generation. Transformer/RNN history tested at easy/surface level only (not in subjective). Temperature omitted (not in released notes).
- **Subjective:** ClearCart e-commerce scenario — `tiktoken` audit on English/Hinglish/long draft + context-fit checker + recommendation line; medium difficulty, single-file submission (case c). Reference solution token counts verified with `cl100k_base`.
- **Explanations:** Every objective question includes correct answer(s) and distractor reasoning; subjective includes walkthrough, full code, alternatives, and grading notes.
- **Professional wording:** No “as taught in the session” phrasing in stems.
- **Ratings:** Content Coverage, Creativity, Structural Adherence all 5; no logical or presentation mistakes.

## Iteration 1 Notes

- Subjective long-draft string corrected from `"refund " * 4500` (4501 tokens) to `"refund" * 4500` (exactly 4500 tokens) after `tiktoken` verification.
- Q2/Q4 distractors updated to remove temperature reference (not in released notes).

## Iteration 2 (Post-fix verification)

| QC Parameter | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

**Expected result:** All criteria met — assignments ready for platform upload.

---

## Iteration 3 (Subjective guided mini-lab + objective presentation fix)

| QC Parameter | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |

### Changes applied

**Objective:**
- Removed bold formatting from Q6 option C (was leaking the correct answer in the stem).

**Subjective:**
- Refactored to **guided mini-lab** with starter code and three TODOs (matches beginner audience and lab style).
- Token **piece list** required only for two short messages — not 4,500 tokens for the long draft (fixes impractical output requirement).
- Split `SHORT_SAMPLES` vs `LONG_POLICY_DRAFT` for clearer task boundaries.
- Submission remains case c (single `.py` in LMS).

| Question Number | Type | Remarks |
|---|---|---|
| Q1 (Subjective) | Subjective (Medium) | Medium difficulty: Yes; guided TODO format: Yes; submission case c: Yes; dataset: inline strings only; long-draft math verified (4500 / 3296 / 1204) |

**Expected result:** All criteria met — assignments ready for platform upload.
