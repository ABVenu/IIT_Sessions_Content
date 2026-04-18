# Lecture Script: Classification Models and Evaluation Metrics

**Session Duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners (Indian students, limited or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Use it to pace the room, manage screen-sharing and live coding, and plan engagement checks. Teach from `Lecture Notes.md` for definitions, formulas, and full code.

---

## Break rule (not a numbered block)

After roughly **60–75 minutes** of instruction and demos, take **one** pause of **5–8 minutes**. Do not schedule multiple breaks in this script. If energy is low earlier, move the break up by one block and trim the preceding segment slightly rather than skipping a whole topic.

---

## 1. Opening — Why accuracy lied to us (10 minutes)

**Facilitator actions**

- Screen-share the session title: *Classification Models and Evaluation Metrics*.
- Recap Session 30 in one minute: Logistic Regression, confusion matrix, accuracy.
- Tell the “always predict Pass” story: 90% pass rate → naive model gets 90% accuracy but catches **zero** at-risk students.
- State today’s outcomes: two new models (Decision Tree, Random Forest) and metrics (Precision, Recall, F1, ROC-AUC) plus threshold tuning.

**Student actions**

- Write one sentence: “What does accuracy *not* tell you?” (optional quick chat poll).

**Engagement**

- **Cold-call:** “If everyone passes, can accuracy still look high?” (Yes — if the model always says Pass.)

**Bridge sentence**

“Accuracy is a starting point; the first model that thinks in plain rules is the Decision Tree — a flowchart learned from data.”

---

## 2. Decision Trees — Rules, vocabulary, Gini, max_depth (14 minutes)

**Facilitator actions**

- Define Decision Tree in plain language: yes/no questions, flowchart; bank loan analogy from notes.
- Walk through **root**, **branch**, **internal node**, **leaf**, **depth** — point at the tree visualization image.
- Explain intuition only: algorithm tries splits that make groups “purer”; **Gini** = purity score (0 = pure, 0.5 = messy for binary).
- Stress **overfitting**: unlimited depth memorizes noise → **`max_depth`** is the main brake.

**Student actions**

- Point to the diagram: “Where is a leaf?” (any bottom decision.)

**Engagement**

- **Thumbs up:** “Thumbs up if depth = 1 means at most one question before an answer.”

**Bridge sentence**

“We’ve named the pieces; now we train a real tree on the same student dataset we used last session and read what it learned.”

---

## 3. Live coding — Decision Tree, importances, predictions (22 minutes)

**Facilitator actions**

- Reuse the 400-student, 3-feature setup (seed 7, 80/20 split) — align with notes so outputs match expectations.
- Live-code or step through: `DecisionTreeClassifier(max_depth=4, random_state=42)`, `fit`, `predict`, `predict_proba`.
- Print **feature importances** with the bar character trick; narrate: study_hours should dominate (matches data formula).
- Show 8 test rows: Actual vs Pred vs P(Pass); print accuracy.
- Mention: leaf probabilities = class mix in that leaf (no deep math).

**Student actions**

- Run alongside or verify importances order matches intuition.

**Engagement**

- **Check screens / chat:** “Type ‘ok’ when your importances print and study_hours is highest.”

**Bridge sentence**

“One tree is easy to explain but wobbly if data shifts — next we put many trees in a room and take a vote.”

---

## 4. Random Forest — Ensemble, trade-offs, side-by-side code (20 minutes)

**Facilitator actions**

- Explain **bagging** (bootstrap rows), **random features at splits**, **majority vote** — cricket analysts analogy.
- Trade-off in one line: forest = harder to draw as one flowchart, usually better accuracy and stability.
- Show the Random Forest image from notes.
- Live-code: `RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)`, `fit`, compare accuracies Tree vs RF.
- Print side-by-side predictions for 8 students; comment when RF P(Pass) is smoother.

**Student actions**

- Notice RF feature importances are averaged — more stable than a single tree.

**Engagement**

- **Pair-share (90 seconds):** “Name one job where you must show the exact rules (tree) vs one where raw accuracy matters more (forest).”

**Bridge sentence**

“We can compare models by accuracy — but we need language for *who* gets hurt when the model is wrong: Precision and Recall.”

---

## 5. Precision, Recall, F1 — Definitions, trade-off, `evaluate_classifier` (24 minutes)

**Facilitator actions**

- **Precision:** of everyone we called Pass, how many really passed? → FP costly contexts (spam false alarm nuance: sometimes precision = not flagging good email as spam — adapt language to “positive class” as Pass).
- **Recall:** of everyone who really passed, how many did we catch? → FN costly contexts (disease, fraud).
- Draw TP / (TP+FP) and TP / (TP+FN) on board; link to Session 30 confusion matrix.
- **Trade-off:** lower threshold → recall up, precision down (echo Session 30).
- **F1:** harmonic mean — why average misleads (use notes example).
- Live-code: train **Logistic Regression** on same split; define `evaluate_classifier`, run for LR, Tree, RF; print summary table.
- Show `classification_report` for RF; explain **support** and per-class rows.

**Student actions**

- For one metric, restate the question it answers in their own words.

**Engagement**

- **Cold-call:** “High precision but low recall — is the model generous or stingy with Pass?” (Stingy — misses many real passes.)

**Bridge sentence**

“Precision and Recall use one threshold — usually 0.5. Next we measure how well the model ranks Pass above Fail at *every* threshold: ROC-AUC.”

---

## 6. ROC-AUC — Concepts, plot, full metric table (20 minutes)

**Facilitator actions**

- **ROC:** x = FPR, y = TPR (recall) at each threshold; factory inspector analogy from notes.
- **AUC:** area 0–1; interpret bands (0.9+ excellent, 0.5 random) — show interpretation table.
- Emphasize: **always-Pass** model can have high accuracy but AUC ≈ 0.5 — exposes useless ranking.
- Live-code: `roc_auc_score` for LR, Tree, RF using `predict_proba[:, 1]`; `roc_curve`; **one** combined matplotlib plot with diagonal baseline; legend with AUC.
- Run the “Full Metric Summary” loop: Acc, Prec, Rec, F1, AUC — this is the “portfolio” row for each model.

**Student actions**

- Identify which curve hugs the top-left best.

**Engagement**

- **Thumbs up:** “Thumbs up if you agree AUC uses probabilities, not hard 0/1 predictions.”

**Bridge sentence**

“AUC tells you how good the ranking is across thresholds; in deployment you still pick *one* threshold — so we close with data-driven threshold tuning.”

---

## 7. Threshold tuning — Precision–recall curve and best F1 threshold (15 minutes)

**Facilitator actions**

- Frame: business asks “maximize F1” or “recall ≥ 90%” — threshold is the dial.
- Show precision–recall trade-off image briefly.
- Live-code: `precision_recall_curve` on `y_prob_rf`; compute F1 along thresholds; `argmax` for best threshold; print default 0.5 vs optimised Precision / Recall / F1.
- Keep focus on **pattern**: optimised threshold may differ from 0.5; metrics shift together.

**Student actions**

- Read the printed comparison table aloud with you (one row per metric).

**Engagement**

- **Quick poll (chat):** “Would you ever deploy 0.5 without checking?” (Expected: often no for high-stakes.)

**Bridge sentence**

“We’ve compared three models with a full metric stack — let’s lock in terms you’ll reuse and preview how you’ll practise.”

---

## 8. Closing — Quick reference, homework mindset, Q&A (10 minutes)

**Facilitator actions**

- Flash the Quick Reference table; suggest screenshot for revision.
- Tie together: tree = interpretable; forest = robust; metrics = who suffers; AUC = ranking quality; threshold = business fit.
- Optional: mention precision–recall curve as alternative when classes are very imbalanced (notes flag — don’t expand unless time).
- Take 2–3 questions.

**Student actions**

- Note one metric they will check first on their next classification assignment (personal).

**Engagement**

- **Exit ticket (optional):** “In one line: Precision answers which question?” (Of predicted positives, how many were correct.)

**Bridge sentence**

“Next sessions build on this toolkit — bring your confusion matrix, ROC, and threshold vocabulary every time you compare classifiers.”

---

## Timing flex — If the session is running late

**Cut order (prefer top first)**

1. Shorten **pair-share** in block 4 to 45 seconds; shorten **opening** block 1 by 2 minutes.
2. In **block 3**, pre-run data setup and live-code only from `DecisionTreeClassifier` through importances (skip printing all 8 rows — show 4).
3. In **block 4**, show accuracy comparison and **one** side-by-side row block (4 students not 8).
4. In **block 5**, derive Precision/Recall on whiteboard verbally; run `evaluate_classifier` for **two** models (RF + LR) if needed, then mention Tree matches notes async.
5. In **block 6**, show **one** ROC curve (e.g., RF) plus AUC table for all three — or plot all three without animation commentary.
6. In **block 7**, print best threshold and F1 only; skip default-vs-optimised table if critical.
7. Move **Quick Reference** to async reading; keep **2 minutes** for Q&A only in block 8.

**If ahead of schedule**

- Add 5 minutes in block 5: students compute Precision manually from printed TN, FP, FN, TP for one model.
- Add 5 minutes in block 6: explain why diagonal = random (coin flip) in ROC space.

---

*End of delivery script.*
