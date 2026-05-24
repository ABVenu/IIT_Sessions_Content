# Lecture Script: Regression — Regularization and Evaluation

**Session Duration:** 2 Hours 15 Minutes  
**Audience:** Absolute beginners (Indian students, little or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Keep the detailed explanations, definitions, and code snippets in *Lecture Notes.md*; use this script to run the room, share screens, and check that learners are following on their machines.

---

## Break rule

After roughly **60–75 minutes** of session time, take **one** break of **5–8 minutes**. Do **not** treat the break as a numbered teaching block—announce it, pause the recording if applicable, and resume with the bridge into block 5.

---

## 1. Opening, recap, and session roadmap (12 minutes)

**Facilitator**

- Welcome the group; confirm everyone can open Google Colab (or your chosen environment).
- **Cold-call** one or two students: “In the **previous session**, what is a **residual**?” Accept: actual minus predicted.
- Recap the open questions from linear regression: models can **overfit**, and `.score()` alone is not enough to **defend** a model in a review.
- Bridge: today you add **control** (regularization) and **evidence** (MAE, RMSE, R², grouped error analysis).
- Project the session roadmap from the notes (five bullets: regularization, model comparison, metrics, error analysis, practical metric choice).

**Students**

- Connect today to California housing, Pipeline, mean baseline, and train–test splits from the previous session.

**Engagement**

- **Thumbs up:** “Thumbs up if you’ve ever seen a model look great in a notebook but worry you about using it on new data.”

**Bridge sentence:** “When a model gets too clever on training rows, **regularization** is the first tool we reach for — let’s define it before we touch code.”

---

## 2. Regularization, Ridge, and Lasso (18 minutes)

**Facilitator**

- Define **regularization** with the intern/manager analogy from the notes — accurate but not over-complicated.
- Explain **`alpha`**: higher alpha → stronger penalty → smaller coefficients.
- Teach **Ridge** (L2): shrinks weights, rarely zeros them — all features stay.
- Teach **Lasso** (L1): can zero coefficients — built-in **feature selection**, sparse model.
- **Screen-share** the Ridge vs Lasso coefficient diagram and the comparison table (Linear vs Ridge vs Lasso).
- Run the **Quick Activity** (25 columns, 8 noise — Lasso vs Ridge). Reveal answers.

**Students**

- Write one sentence each: when would you pick Ridge vs Lasso?

**Engagement**

- **Cold-call:** “Salary model with many useless survey columns — Ridge or Lasso for automatic dropping?”

**Bridge sentence:** “Definitions are clear — now we **fit all three models on the same split** and read the coefficient table, especially the deliberate noise column.”

---

## 3. Live code — compare Linear, Ridge, and Lasso coefficients (20 minutes)

**Facilitator**

- Narrate the dataset setup from the notes: **300 rows**, `seed=42`, five features including **`random_noise`**, target **`exam_score`**.
- Live-code the full block: imports → generate data → `train_test_split` → fit Linear, Ridge (`alpha=10`), Lasso (`alpha=1`) → print coefficient table.
- Pause on the **`random_noise`** row — this is the teaching moment.
- Emphasize: **fit on train only**; same split habit as before; never pass test data to `.fit()`.

**Students**

- Run the same cells; confirm their Lasso row shows `random_noise` at or near **0.0**.

**Engagement**

- **Check screens:** two volunteers read their `random_noise` coefficient for Linear vs Lasso aloud.
- **Pair-share (2 minutes):** “What did Lasso do that Linear regression did not?”

**Bridge sentence:** “Coefficients tell us *how* the model uses features — next we need standard numbers that say *how wrong* predictions are on unseen test rows.”

---

## 4. Evaluation metrics — MAE, RMSE, and R² (18 minutes)

**Facilitator**

- State the rule: report **more than one** metric; always on **test** predictions.
- Walk **MAE** — average absolute miss, same units as target (marks, ₹, minutes).
- Walk **RMSE** — penalises large errors more; if **RMSE ≫ MAE**, hunt outliers or weak segments.
- **Screen-share** the MAE vs RMSE diagram.
- Walk **R²** — variance explained vs mean baseline; link to `.score()` from the previous session.
- **Screen-share** the R² diagram. Stress: R² is **relative** — pair with MAE or RMSE for business readiness.
- Run the **Quick Activity** (Model A vs B — same MAE, different RMSE). Reveal: Model B has riskier large mistakes.

**Students**

- Note the three metrics in a revision table: what each answers, what each does *not* answer.

**Engagement**

- **Cold-call:** “R² = 0.85 but MAE = ₹12,000 on salary — is the model automatically deployment-ready?” Expected: not necessarily — check absolute error in rupees.

**Bridge sentence:** “You know what each metric means — now we wrap fit, predict, and all three scores into one reusable workflow.”

---

## 5. Live code — `evaluate_model` on Linear, Ridge, and Lasso (18 minutes)

**Facilitator**

- Live-code the **`evaluate_model`** helper from the notes (`seed=33`, three features, 500 rows).
- Narrate each line inside the function: `fit` → `predict` on test → `mean_absolute_error` → `np.sqrt(mean_squared_error(...))` → `r2_score`.
- Run all three models; compare printed MAE, RMSE, R² side by side.
- Interpret aloud: similar numbers → clean data; Ridge/Lasso slightly better RMSE → mild overfitting was trimmed.

**Students**

- Run the helper; screenshot or copy one model’s three-metric block for their notes.

**Engagement**

- **Thumbs up:** “Thumbs up if you wrote `y_test` before `y_pred` in every metric call — order matters.”

**Bridge sentence:** “A single MAE hides segment-level pain — the same way we read residual tables before, we now **group errors by feature bins**.”

---

## 6. Error analysis — grouped residuals with `pd.cut` (18 minutes)

**Facilitator**

- Define **error analysis** with the navigation ETA example — 4-minute average but 9 minutes in city traffic.
- Link to **residuals** from the previous session: `actual − predicted`, now aggregated by study-hour groups.
- Live-code the error analysis block (`seed=77`): train model → build results DataFrame → `pd.cut` into Low/Medium/High → `groupby` on `abs_error` and `residual`.
- **Screen-share** the error-analysis-by-group diagram from the notes.
- Walk **what to look for**: one group with high mean error; positive mean residual → under-prediction.

**Students**

- Run grouping cells; identify which study group has the highest mean absolute error in their output.

**Engagement**

- Run **Deployment Readiness** activity (R² = 0.80 but doubled MAE for junior hires). **Cold-call:** “Enough for HR rollout?”

**Bridge sentence:** “Global metrics plus grouped tables form a deployment story — we close with a short guide on **which metric to lead with** in different business cases.”

---

## 7. Practical perspective and deployment checklist (12 minutes)

**Facilitator**

- Walk the “when to prefer MAE / RMSE / R²” table from the notes in under 3 minutes.
- Read the **deployment checklist** aloud: test metrics only, stable train–test gap, acceptable MAE/RMSE in real units, no unchecked critical segment, compare Linear vs Ridge vs Lasso on **test** numbers.
- Tie back: best model = best **test** metrics for *your* use case, not the fanciest name.

**Students**

- Pick one scenario (delivery ETA vs hospital vitals vs model comparison) and name their lead metric plus one backup metric.

**Engagement**

- **Pair-share:** Partner A picks salary prediction; Partner B picks exam marks — each states MAE vs RMSE priority and why.

**Bridge sentence:** “You can now control complexity and defend regression results with numbers and segments — let’s lock in the takeaways.”

---

## 8. Recap, key takeaways, and close (12 minutes)

**Facilitator**

- Rapid-fire **key takeaways** from the notes (Ridge shrinks, Lasso zeros; MAE/RMSE/R² complementary; error analysis for segments; train–test discipline unchanged).
- Point learners to the **Important Commands** table — highlight `Ridge`, `Lasso`, `mean_absolute_error`, `r2_score`, `pd.cut`, `groupby`.
- Preview lightly: next session moves from numeric targets to **category** predictions — classification begins.
- Remind learners to complete any linked assignment or pre-read.

**Students**

- Skim the glossary table; star three items they will use in this week’s practice.

**Engagement**

- Final **cold-call:** “Name one reason Lasso might zero out a feature that Linear regression keeps.”

**Bridge sentence:** “Carry forward: **split first, fit on train, report metrics and grouped errors on test** — that habit is non-negotiable for every regression model you ship.”

---

## Timing flex — if you are running late

- **Cut first (save core demos):** Shorten pair-shares from 2 minutes to 1; trim extended Q&A in blocks 2 and 4; show MAE/RMSE/R² diagrams with brief labels instead of full walk-through.
- **Cut second:** In block 3, pre-load the data-generation cells and live-code only the fit + coefficient print; assign full regeneration as homework. In block 6, live-code `groupby` on `abs_error` only and describe residual bias check verbally.
- **Never skip:** Block 3 (coefficient comparison with `random_noise`) and block 5 (`evaluate_model` with MAE, RMSE, R² on **test** data) — these are the session’s core outcomes.
- **If ahead of schedule:** Add 5 minutes for students to try **`alpha=1`** vs **`alpha=20`** on Ridge and report how `random_noise` coefficient changes; or run a **mini-poll**: “Deployment report — lead with MAE or RMSE for a food-delivery ETA model?”
