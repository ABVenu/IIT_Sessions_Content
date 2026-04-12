# Lecture Script: Regression — Regularization and Evaluation

**Duration:** 2 hours 15 minutes (135 minutes)  
**Audience:** Absolute beginners (Indian students; minimal prior tech background).

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm **Google Colab** or cohort IDE works.
- **Recap Session 28 in one minute:** linear regression, train–test, residuals — then pose the two questions from the notes: *what do we do when the model overfits?* and *how do we measure quality in a trustworthy single number?*
- Today’s outcomes: (1) **regularization** (Ridge vs Lasso, **alpha**), (2) **MAE, RMSE, R²** plus baseline, (3) **error analysis** by groups and picking metrics for the job.

**Bridge sentence:** *“Open a fresh notebook — we’ll compare three models on the same data before lunch on metrics.”*

---

## 2. Open the notebook environment (5 minutes)

- New notebook, e.g. `session29_regularization_eval`; confirm **Run** / Shift+Enter and imports will work (`numpy`, `sklearn`, later `pandas`, `matplotlib`).
- Quick `print` check; circulate; two-minute peer assist if needed.

**Bridge sentence:** *“Overfitting means weights got too clever — regularization is the manager who says ‘stay simple.’”*

---

## 3. Regularization: Ridge, Lasso, and alpha (16 minutes)

- **No code yet.** Intern / over-customised report analogy from notes — one sentence.
- **Ridge:** shrinks all coefficients, **none** to exactly zero; dishes on the menu with lower weight — good when many features all matter a bit. **`alpha`** higher → stronger penalty → smaller coefficients.
- **Lasso:** can zero out useless features; talent-show elimination — **sparse** model. **`alpha`** higher → more zeros.
- Project **Figure: Ridge vs Lasso coefficients** from `LectureNotes.md`; 20 seconds silent.
- Walk the **comparison table** (Linear vs Ridge vs Lasso) — penalty, zeros, feature elimination, “best when” — under 3 minutes; cold-call: “Which one drops features entirely?”

**Bridge sentence:** *“We’ll fabricate five columns — one is pure noise — and watch Lasso zero it out.”*

---

## 4. Comparing Linear, Ridge, and Lasso — live or follow-along (22 minutes)

- Screen-share the **first code block**: `seed=42`, **300** rows, **five** features (`column_stack`), score uses real drivers **except `random_noise`**; `train_test_split` 80/20; `LinearRegression`, `Ridge(alpha=10)`, `Lasso(alpha=1)`.
- Run; circulate for import and shape errors.
- **Focus discussion:** coefficient row for **`random_noise`** — Linear nonzero, Ridge smaller, Lasso **0.0**; thumbs: did Lasso eliminate the junk column?
- Optionally skim first three test predictions across models — no deep dive.

**Bridge sentence:** *“Coefficients tell *who* the model trusted; next we ask *how wrong* it is on average.”*

---

## 5. MAE and RMSE — intuition (12 minutes)

- **MAE:** average absolute gap — same units as target (rupees, marks, minutes); treats errors **fairly**; **gentle** to outliers — delivery ETA story from notes.
- **RMSE:** square errors before averaging, then square root — **punishes** big misses; hospital / blood-pressure example; if **RMSE ≫ MAE**, a few points are way off.
- Project **Figure: MAE vs RMSE** from notes; read caption once.

**Bridge sentence:** *“MAE and RMSE say how big mistakes are; R² says how much of the spread we explained versus guessing the mean.”*

---

## 6. R² and the baseline idea (12 minutes)

- **R²:** improvement over **always predict training mean**; 0 = as bad as that baseline; negative = worse; **cannot** replace MAE/RMSE for “are we good enough in rupees?”
- Project **Figure: R² visualization** from notes; skim **R² bands table** silently (excellent / good / weak) — no memorization drill.
- One cold-call: “If R² is 0.85, how would you say that in plain words to a stakeholder?”

**→ Break here (5–8 minutes).** Write return time on the board.

**Bridge sentence:** *“After the break we compute all three metrics in code and beat the mean baseline on MAE.”*

---

## 7. MAE, RMSE, R², and baseline — live or follow-along (18 minutes)

- **Second code block:** `seed=21`, **400** rows, single feature, split, `mean_absolute_error`, `mean_squared_error` + `np.sqrt` for RMSE, `r2_score`, `np.full` baseline MAE.
- Run; circulate; confirm argument order **y_true, y_pred**.
- Optional: **matplotlib** scatter actual vs predicted — if environment stalls, **you** show output only.
- Pair-share (60 sec): why is baseline MAE a fair sanity check?

**Bridge sentence:** *“One global MAE hides *where* we fail — next we slice errors by study-hour groups.”*

---

## 8. Error analysis with pandas — live or follow-along (16 minutes)

- **Navigation app** example from notes — highway vs city; average hid the bug.
- Project **Figure: error analysis by study hour group** from notes.
- **Third code block:** `seed=77`, **500** rows, **heteroscedastic** noise (harder for low study hours), `DataFrame`, `pd.cut` buckets, `groupby` + `agg`, `nlargest(5)`, bias-by-group.
- Run; circulate for **`observed=True`** in groupby if needed; ask: which group has higher **avg_error**?
- Quick read: *what to look for* bullets — one group worse, residual sign bias, worst five clustered.

**Bridge sentence:** *“Metrics score the model; error analysis tells you what to fix — last we tie metric *choice* to business risk.”*

---

## 9. Which metric when + multi-model evaluation (18 minutes)

- **Practical guide** from notes — three bullets: MAE (explain to boss), RMSE (big errors costly), R² (compare models, scale-free story).
- **Fourth code block:** `evaluate_model` helper, `seed=33`, Linear vs `Ridge(alpha=5)` vs `Lasso(alpha=0.5)`, summary table.
- Run; cold-call: if RMSE drops but MAE flat, what might be true?
- Closing line from notes: best model = **best numbers on *your* data and use case**, not the fanciest name.

**Bridge sentence:** *“We’ll pin vocabulary to the wall and you’re done.”*

---

## 10. Quick reference and close (10 minutes)

- Project **Quick Reference** table; skim **Term / Tool** column; take two volunteer rows (e.g. **alpha**, **sparse model**, **`pd.cut`**).
- Exit ticket: “Name **one** situation where you’d pick **RMSE** over **MAE**.”
- Assign: rerun all **four** code blocks before next class; thank-you and submission pointer.

---

_End of lecture script — Session 29._
