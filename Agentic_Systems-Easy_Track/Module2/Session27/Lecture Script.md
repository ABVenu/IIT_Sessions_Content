# Lecture Script: Model Evaluation — Leakage, Imbalance, and Honest Metrics

**Session duration:** 2 hours 15 minutes  
**Audience:** Mixed background; aligns with Agentic Systems Easy Track  

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions and theory stay with Lecture Notes, slides, board, or readings.

**Break (only pause in this plan):** After roughly **75–85 minutes** of session clock time, take **one** pause of **5–8 minutes**, then continue with the next teaching segment. Numbered sections below are **teaching or activity**—the break is not a numbered block.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm Colab (or your environment) and access to Lecture Notes / figures.
- Headline outcomes: learners can **spot data leakage**, follow a **split-first workflow**, interpret **class imbalance**, see why **accuracy misleads**, use **precision and recall**, outline **balance strategies** (over/under/synthetic concepts), and use **cross-validation** for stabler scores.
- Preview: concepts tie to **car / student / e-commerce** style examples in notes; mix of diagrams (**session27-01** … **session27-09**) and short **sklearn** follow-along; single mid-session pause per rule above.

---

## 2. Environment check — imports and notebook (5 minutes)

- New notebook; filename e.g. `session27-evaluation`.
- Everyone runs imports from the notes cheat sheet: `pandas`, `train_test_split`, `StandardScaler`, optional `cross_val_score`, `LogisticRegression`.
- Confirm clean run; no long coding yet—setup only.

---

## 3. Why evaluation can be misleading (7 minutes)

- Paraphrase **Section 1**: high accuracy ≠ trustworthy model.
- Two traps: **data leakage** (sees what it shouldn’t) and **class imbalance** (easy to look good on paper).
- Student-exam analogies (seen the questions vs trivial exam); stress **silent** failure in production.
- Show **session27-01** (leakage / prediction-time overview).

---

## 4. Understanding data leakage (11 minutes)

- Core assumption: learn from past, apply to **unseen** future data.
- **Three students** analogy (textbook vs past papers vs answer key); model acts like the third when leaked.
- Walk three domains from notes: car (sale price after prediction), student (final marks as input), e-commerce (order confirmation before purchase decision).
- Internal effect: shortcuts vs real relationships; **thinking question** on screen: *Would this exist at prediction time?*

---

## 5. How leakage happens in practice (9 minutes)

- **Scenario 1:** impute/scale **before** split—test influences train statistics; quick car/student/e-commerce reminders.
- **Scenario 2:** features engineered from **target** (e.g. “is expensive” from price).
- **Scenario 3:** **duplicates** straddling train and test.
- Honest scores may **drop** after fixes—that is progress, not regression.

---

## 6. Data leakage guard — correct workflow and code (15 minutes)

- **Principle:** test set untouched until final evaluation; only **train** learns transformation parameters.
- Show **session27-02** (wrong order vs split-first).
- Live or follow-along **Section 4** snippet: `train_test_split` → `scaler.fit_transform(X_train)` → `scaler.transform(X_test)`; stress **fit** only on train.
- Optional cold-call: *What breaks if we `fit_transform` on full `X`?*

---

## 7. Understanding class imbalance (8 minutes)

- Definition: one outcome vastly outweighs the other; often **mirrors reality** (fraud, rare disease, no-purchase).
- Show **session27-03**; majority class becomes the “safe” default prediction.
- **95 predict “pass”** analogy—high score, wrong job.

---

## 8. Why accuracy is misleading with imbalance (7 minutes)

- **99 normal / 1 fraud** toy case: always “normal” → 99% accuracy, 0% fraud caught.
- Show **session27-04**; not all errors are equal—accuracy flattens that.
- Bridge: we need metrics that surface **minority class** behaviour.

---

## 9. Precision and recall (13 minutes)

- Show **session27-05**; define in plain language: precision = *trust when we say positive*; recall = *how many real positives we found*.
- Short examples: spam (precision), fraud (recall); healthcare / manufacturing one-liners from notes.
- **Trade-off:** stricter threshold vs looser; *which mistake is costlier here?*
- Optional 2-minute pair: given a scenario, pick which metric to prioritise.

---

### Break (5–8 minutes)

- No new concepts; resume with imbalance handling.

---

## 10. Handling class imbalance — oversampling and undersampling (11 minutes)

- Why handling: disrupts “always predict majority” shortcut.
- **Oversampling:** duplicate minority—fairer exposure; risk **overfitting** / memorisation.
- **Undersampling:** drop majority—balance; risk **losing information**.
- Show **session27-06**; **thinking layer:** goal is fair **learning opportunity**, not token equality of counts.

---

## 11. Synthetic data concepts (9 minutes)

- Limit of naive duplication: no new information.
- Idea: **neighbours** and **plausible blends** between minority points; paint-mixing analogy.
- Domains skim: healthcare / finance / e-commerce as in notes.
- Show **session27-07**; caveat: careless synthesis → unrealistic blends and noise.

---

## 12. Cross-validation (12 minutes)

- Single split: lucky or brutal test set; **teacher across many classes** analogy.
- k-fold idea: each chunk as test once; **mean** and **spread** of scores.
- Show **session27-08**.
- Live or demo **Section 10** `cross_val_score` snippet; read output range as stability check.

---

## 13. Connecting leakage, imbalance, and evaluation (9 minutes)

- **Section 11** synthesis: leakage inflates scores; imbalance hollows accuracy; single split = noisy story.
- Show **session27-09** (three pillars).
- 2-minute silent or jot: *one failure mode* for each pillar from memory.

---

## 14. Cheat sheet recap and close (6 minutes)

- Skim **Quick Reference**: libraries table, `fit_transform` vs `transform`, concepts grid (leakage, imbalance, precision, recall, sampling, synthetic, CV).
- Closing question: *Which check will you add first on your next model—split order, metric, or CV?*
- Thank-you; next session / submissions pointer.

---

### Timing flex

- If early sessions run long, trim **Section 4** (fewer domain examples) or **Section 9** (one domain only for precision, one for recall).
- If **cross-validation** needs depth, borrow 3–4 minutes from **Section 11** (synthetic) or **Section 14**.
- If you finish **Section 14** early, use spare minutes for Q&A on **when recall beats precision** or **leakage in time-series**, without expanding into a new lecture.
