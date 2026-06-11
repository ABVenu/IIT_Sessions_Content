# QC Report — Session22: ML Workshop - Model Selection & Comparison

## Iteration 1 (Align Notes Against Covered LOs — Release pass)

| Criteria | Rating / Result |
|---|---|
| Content Coverage | 5 / 5 |
| Creativity | 5 / 5 |
| Structural Adherence | 5 / 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/internal reference | True |

### Alignment actions (vs `Live Topic Coverage.md` + transcript)

**Removed (not covered in session):**
- Time-series-specific fair-comparison rule in metric tables (chronological holdout / MAPE row in quick activity) — time series was prior-session context only; this session focused on classification and regression comparisons.
- K-Means, PCA, and time-series rows from checklist Q1 — not discussed in this session's selection checklist walkthrough.
- SVM from "Start Simple, Go Complex" protocol — not taught in this session.
- Neural Networks row from complexity table — only briefly referenced in interpretability Q&A; table trimmed to models actively compared in demos.
- Separate scaler + model save pattern as primary approach — session taught saving the **full pipeline** instead.

**Retained (all metadata LOs covered):**
- Metric tables (classification + regression) with all 5 diagram images.
- Comparison by complexity (overfitting/underfitting, tree depth demo, Occam's Razor).
- Model persistence (joblib save/load, joblib vs pickle, security warning).
- Selection checklist (6 questions, fintech activity, start-simple protocol).

**Added (extra content taught in session):**
- **When Accuracy Alone Misleads** — confusion matrix, F1 priority, loan-default / hospital examples from live demo.
- **sklearn Pipelines** — new section with definition, rationale, and code; classification/regression tables updated to use pipelines.
- **Decision Tree** added as third classifier in metric table (LR, DT, RF as taught).
- **Hyperparameter Tuning with GridSearchCV** — `n_estimators` grid on California housing RF pipeline.
- **Gradio deployment** — web UI section loading persisted pipeline for end-user predictions.
- Persistence and selection protocol updated to `joblib.dump(pipeline)` pattern.
- Terminology table expanded: Pipeline, GridSearchCV, Gradio, confusion matrix, `n_jobs=-1`.

**Not included (session protocol, not lecture content):**
- Mentimeter / post-lecture quiz — correctly excluded.
- Kaggle practice recommendation at session close — optional homework, not core lecture content.

**Output:** `Lecture Notes Released.md` created in Session22 folder.

**Expected result:** All criteria met.

---

## Iteration 2 (Fresh QC verification pass)

| Criteria | Rating / Result |
|---|---|
| Content Coverage | 5 / 5 |
| Creativity | 5 / 5 |
| Structural Adherence | 5 / 5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/internal reference | True |

### Verification focus

**Content Coverage (5/5):**
All four metadata topics verified against transcript and `Live Topic Coverage.md`: Metric tables ✓; Comparison by complexity ✓; Model persistence ✓; Selection checklist ✓. All six extras from coverage report incorporated: evaluation metrics deep-dive, pipelines, GridSearchCV, Gradio, pickle security, Wisconsin breast cancer / California housing case studies (via `load_breast_cancer` and `fetch_california_housing` code).

**Creativity (5/5):**
Three student-facing quick activities retained (pick metrics, read the gap, walk the checklist). Relatable examples: cricket selector, loan default, hospital tumour screening, bank loan form, house-price web app. Activities written as student notes — no instructor "ask students" phrasing.

**Structural Adherence (5/5):**
- Starts with `# ML Workshop: Model Selection & Comparison` — no metadata header.
- `## Context of This Session` with bullet goals aligned to session delivery.
- Official / In Simple Words / Real-Life Example on all major new terms (metric table, F1, pipeline, GridSearchCV, Gradio, persistence, checklist).
- Six complete code blocks with per-line comments and "How the code works" lists.
- Key Takeaways (6 bullets) + terminology table at end.
- All 5 original diagram images retained.
- No Part/Section labels; 3-sentence paragraph rule followed.

**No Logical Mistakes (True):**
- Accuracy vs F1 trade-off for imbalanced classes stated correctly.
- Pipeline fit/predict order and persistence rationale correct.
- Train–test gap overfitting detection correct.
- GridSearchCV `model__` parameter prefix for pipeline steps correct.
- joblib preferred over pickle for sklearn; untrusted file security warning present.
- Occam's Razor / start-simple protocol consistent with session teaching.

**No Presentation Mistakes (True):**
- Consistent headings, tables, and bullet style matching Session21 released notes pattern.
- No "lite/light version" meta language.
- Image alt text present; URLs only in image paths.

**No Previous Session Number References (True):**
- Grep confirmed no "Session N" in prose. Image URLs contain batch paths only (acceptable).
- Uses "previous session" for time-series context without session numbers.

**No Metadata/internal reference (True):**
- No duration, target audience, lecture ID, or internal instructions in student-facing text.

**Expected result:** All criteria met — `Lecture Notes Released.md` ready for student release.
