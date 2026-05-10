# Lecture Notes QC Report — Session 13: The ML Workflow & Habits

---

## QC Round 1

**Date:** 2026-05-09

| Criterion | Rating / Result | Notes |
|---|---|---|
| Content Coverage | 5/5 | All 4 core topics covered — Problem Framing, Features vs Labels, Train/Val/Test Split, and Baselines — each with official definition, simple explanation, real-life example, and working code |
| Creativity | 5/5 | Strong Indian-context analogies: cricket par score for baseline, board exam for data splits, doctor diagnosing diabetes for problem framing, student marks for features/label identification |
| Structural Adherence | 4/5 | 3-sentence rule followed throughout; bold terms, bullet points, direct headings all in place; "How the code works" section present after each code block; Key Takeaways and Quick Reference Table included — deducted 1 point for inconsistency between stated split ratios and code |
| No Logical Mistakes | False | "Common Split Ratios" section listed 80/10/10 as "most common" but all code examples used a 60/20/20 split without explanation. This inconsistency could confuse a beginner. |
| No Presentation Mistakes | True | No formatting errors found |

**Action Taken:** Fixed the "Common Split Ratios" section to list 60/20/20 first with a note that it matches the code examples, and added a clear explanation of when each ratio is used. Proceeded to Round 2 QC.

---

---

## QC Round 3 — Post Restructure (Metadata Subtopic Alignment)

**Date:** 2026-05-09

**Reason for this round:** Notes were restructured to align with the 6 detailed subtopics listed in `metadata.md`. The previous version was missing the first subtopic entirely (Google Colab introduction) and used "Step X" heading prefixes which violate the prompt's direct-heading rule.

**Changes made:**
- Added a full **Getting Started with Google Colab** section covering: what Colab is, why it is used for ML, step-by-step setup, interface overview table, running first code cells, importing libraries, and Colab keyboard shortcuts.
- Renamed all headings from "Step 1/2/3/4" format to direct topic headings: "Framing ML Problems Effectively", "Differentiating Features and Labels", "Applying Data Splitting Strategies", "Establishing and Evaluating Baselines".
- Renamed "Introduction to Machine Learning" → "What Machine Learning Actually Is" and "The Standard ML Workflow" → "Defining the ML Workflow" to match the subtopic language.
- Added a **baseline vs real model comparison** code block using `DecisionTreeClassifier` to demonstrate what "beating the baseline" actually looks like.
- Added **Overfitting** explanation under the splitting section.
- Added **data leakage during splitting** subsection (scaler/imputer contamination warning).
- Expanded the end-to-end workflow demo to use Colab cell comments for better notebook hygiene.
- All 6 images preserved with original S3 URLs.

| Criterion | Rating / Result | Notes |
|---|---|---|
| Content Coverage | 5/5 | All 6 metadata subtopics covered in depth — Colab setup, ML workflow, problem framing, features vs labels, data splitting with leakage prevention, baselines with both classification and regression examples plus a baseline-vs-real-model comparison |
| Creativity | 5/5 | New analogy: chemistry lab for Colab (fully equipped lab in cloud); cricket par score for baseline; board exam + coaching institute for splits; multiple Indian-context examples (₹ pricing, student marks); practical Colab hygiene advice; "Good ML Habits" section |
| Structural Adherence | 5/5 | Clean `# Lecture Title` start, no metadata, context section present, all headings are direct (no Step/Part/Section prefixes), 3-sentence rule maintained, full code with line-by-line English comments on every line, "How the code works" after every block, 5-point Key Takeaways, Quick Reference Table with expanded rows |
| No Logical Mistakes | True | Split ratios in prose match code (60/20/20 explicit), leakage warnings placed correctly after feature-label section and within splitting section, baseline logic correct for both classification and regression |
| No Presentation Mistakes | True | All 6 images preserved with original S3 URLs, consistent markdown formatting, no broken tables or orphaned headers |

**Final Status: PASSED — All criteria at 5/5, no logical or presentation mistakes.**

---

## QC Round 2

**Date:** 2026-05-09

| Criterion | Rating / Result | Notes |
|---|---|---|
| Content Coverage | 5/5 | All topics from metadata covered in depth with code, activities, tables, and a full end-to-end workflow demonstration using a bank loan default scenario |
| Creativity | 5/5 | Multiple relatable analogies; activity table for problem framing practice; "Good ML Habits" section provides practical mindset beyond just theory; two complete dataset scenarios (student performance + house prices) |
| Structural Adherence | 5/5 | All prompt requirements met: clean start with `# Lecture Title`, no metadata, context section, direct headings, 3-sentence rule, full code with line-by-line English comments, "How the code works" after each code block, 5-point Key Takeaways, Quick Reference Table |
| No Logical Mistakes | True | Split ratios in prose now match the code. All code is syntactically and logically correct. DummyClassifier and DummyRegressor used appropriately. |
| No Presentation Mistakes | True | Consistent markdown formatting, no orphaned headers, no broken tables |

**Final Status: PASSED — All criteria met at expected level.**
