# Lecture Script: Regression — Linear Regression Fundamentals

**Duration:** 2 hours 15 minutes (135 minutes)  
**Audience:** Absolute beginners (Indian students; minimal prior tech background).

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm everyone can open **Google Colab** or your cohort IDE.
- State three outcomes: (1) regression vs classification, (2) **target** vs **feature** plus a trained linear model, (3) **train/test** and **residuals** in plain words.
- Preview: concepts and figures → short code → complexity → diagnostics; then one break after training.

**Bridge sentence:** _“Before we touch vocabulary, make sure the machine in front of you can run a notebook.”_

---

## 2. Open the notebook environment (7 minutes)

- New notebook, e.g. `session28_regression`; screen-share code cell, **Run** / Shift+Enter, where output appears.
- Circulate until everyone has a successful one-line `print` test.
- If stuck, pair for two minutes — peer shows the run button only.

**Bridge sentence:** _“If your machine can print a line, we’re ready to ask what number the computer should output.”_

---

## 3. Two buckets and five quick examples (14 minutes)

- Screen-share or board: _which group?_ vs _what number?_ — not a long lecture.
- Thumbs up if they’ve seen an app show an **exact fare in rupees** before booking; use the **cab** example from the notes in under one minute.
- Read once the five bullets — house price, exam score, delivery minutes, electricity bill, salary — checklist speed.
- Project **Figure 1** from the notes (classification vs regression); 30 seconds silent read; cold-call: one classification label and one regression number from daily life.

**Bridge sentence:** _“Every regression problem needs one column we’re guessing and several columns we use as clues.”_

---

## 4. Target, features, and the “numbers that lie” trap (12 minutes)

- Notes’ **Target** and **Feature**; write **y** and **x** on the board once.
- Optional: orders table from notes; then **Figure 2** (target vs features).
- Thumbs: _sale price_ predicted — are _bedrooms_ a feature? Is _customer ID_ a useful feature for price?
- Pair-share (90 sec): seniority coded 1, 2, 3 — regression target or category? One word answer: category.
- Cold-call one pair; close with the notes’ **beginner mistake** line.

**Bridge sentence:** _“Once we know what we predict and what we feed in, the simplest link is a straight line through points.”_

---

## 5. Best-fit line, intercept, and coefficient (16 minutes)

- Sketch study hours → exam score on board; two bad lines, one plausible — no formula derivation.
- **Figure 3** (best-fit line); caption once: vertical gaps are errors / residuals (formal name later).
- Taxi meter (₹30 + ₹ per km) and hotel ₹2,000 base from notes; cold-call: which part is _rate per unit_?
- One line: many features → same idea, more coefficients; hard to draw.

**Bridge sentence:** _“Knowing the line is not the same as making the computer find it — that’s training.”_

---

## 6. Training with `.fit` and `.predict` — live or follow-along (22 minutes)

- Screen-share first code block — 200 rows, `seed=42`, `reshape(-1, 1)`, `LinearRegression`, `fit`, `predict`, `new_student`.
- You run once; learners run; circulate for reshape errors.
- Stop at `model.fit(X, y)` — thumbs: learning happens in **fit** or **predict**?
- They read intercept and `coef_`; cold-call: near 40 and 7.5? why not exact?
- Optional whisper pair: two numbers stored — what did 200 rows compress into?

**→ Break here (5–8 minutes).** Write return time on the board.

**Bridge sentence:** _“When we’re back: why perfect on practice can still mean terrible on the exam.”_

---

## 7. Overfitting, underfitting, generalisation (14 minutes)

- No code. Short stories from notes: exam memorisation + delivery driver (overfit); cricket/weather or salary-from-city (underfit); doctor (generalisation).
- **Figure 4** (complexity + train-test); 20 seconds silent — three zones.
- Show of hands: train error low, test error much higher — which zone?
- Read once: _useful on future data, not perfect on past data._

**Bridge sentence:** _“We split data so the model doesn’t train on the questions it will be graded on.”_

---

## 8. Train–test split — live or follow-along (16 minutes)

- Second code block: `rng` seed 7, 300 rows, `train_test_split` 80/20, mean absolute errors, `if` gap less than 1.
- Run together; circulate for `sklearn.model_selection` import.
- Pair-share: why must `fit` see only `X_train`? One sentence.
- Cold-call: test error much larger than train — worry?

**Bridge sentence:** _“Average error is size; each mistake has a direction — that’s the residual.”_

---

## 9. Residuals — figure, intuition, third code block (14 minutes)

- **Figure 5** (residuals); board once: actual − predicted; positive ⇒ predicted too low.
- Notes’ pattern bullets — random vs biased vs outliers — under two minutes.
- Third code block: `seed=99`, `y - y_pred`, loop, mean, counts, `argmax`; circulate.
- Thumbs: average residual −6 marks — model biased high or low on scores?

**Bridge sentence:** _“Last minutes: lock the vocabulary.”_

---

## 10. Quick reference and close (8 minutes)

- Project the notes’ **Quick Reference** table; skim headers; take one volunteer row from chat or hands.
- Exit ticket: one situation where train **and** test error matter more than train alone.
- Next session pointer if applicable: MAE, RMSE, R²; run all three code cells before class.
- Thank-you; submission link or office hours.

---

_End of lecture script — Session 28._
