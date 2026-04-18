# Lecture Script: Classification — Logistic Regression Fundamentals

**Session Duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners (Indian students, limited or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Use it to pace the room, manage screen-sharing and live coding, and plan engagement checks. Teach from `Lecture Notes.md` for definitions and code detail.

---

## Break rule (not a numbered block)

After roughly **60–75 minutes** of instruction and demos, take **one** pause of **5–8 minutes**. Do not schedule multiple breaks in this script. If the cohort is tired earlier, you may move this break up by one block—shorten the preceding block slightly rather than skipping content.

---

## 1. Opening — From regression to “which category?” (12 minutes)

**Facilitator actions**

- Screen-share the session title slide or first section of lecture notes: *Classification: Logistic Regression Fundamentals*.
- In plain language, recap: last sessions were **regression** (predicting a number) and metrics like MAE, RMSE, R².
- Pose the pivot question: “When the question is pass/fail, spam/not spam, fraud/genuine — are we still predicting a number?” Cold-call one student for a one-line answer.
- Show the regression vs classification image from notes; give students 30 seconds to read the caption quietly.
- Introduce today’s promise: we move from “how much?” to “which label?” and build the first classification model with code.

**Student actions**

- Listen and answer the cold-call; optionally note one real-life “category” question (bank, email, exam) for a later pair-share.

**Engagement**

- **Thumbs up:** “Thumbs up if you can name one situation where the answer is a category, not a number.”

**Bridge sentence**

“Now that we see why ‘which bucket?’ is different from ‘how much?’, let’s pin down what classification is and why our old linear regression trick doesn’t work for labels.”

---

## 2. Classification basics — Binary vs multi-class, why not linear regression (15 minutes)

**Facilitator actions**

- Walk through the official definition in simple words; use the bank fraud example from notes.
- Show the binary vs multi-class image; emphasize this session is **binary-first**.
- Display the real-world use cases table; ask students to pick one row and say the two categories aloud (quick round-robin, 4–5 students).
- Explain clearly: linear regression can output 1.73 or −0.4 — invalid when labels are only 0 and 1; we need probabilities and a clean decision. Do not derive formulas yet.

**Student actions**

- Match “binary” vs “multi-class” to one example each (verbally or in chat).

**Engagement**

- **Pair-share (2 minutes):** In pairs, one gives a binary example, the other a multi-class example from daily life.

**Bridge sentence**

“We’ve named the problem. Next we meet the algorithm that outputs a probability first — then turns it into a category — and we clear up why it still has ‘regression’ in the name.”

---

## 3. Logistic Regression in plain language + the sigmoid (18 minutes)

**Facilitator actions**

- Address the naming confusion: classification algorithm, “regression” refers to the math (logistic function), not the output type.
- Contrast in one sentence: linear regression asks “how much?”; logistic asks “how likely?” then maps to a class.
- Introduce **raw score** = same weighted sum as before (link to ridge/lasso intuition: coefficients × features).
- Introduce **sigmoid**: squeezes any number to (0, 1); show the sigmoid image and the formula on screen; explain 0 → 0.5 probability without heavy calculus.
- Point to the S-shape: sensitive in the middle, confident at extremes — connect to “borderline students” preview.

**Student actions**

- Trace with finger on the curve: “Where is the model most unsure?” (middle.)

**Engagement**

- **Cold-call:** “If raw score is very negative, does probability go toward 0 or 1?”

**Bridge sentence**

“We’ve seen the engine; now we put it in the car — one feature, pass/fail labels, and real sklearn code.”

---

## 4. Live coding — One feature, train/test, predict and predict_proba (22 minutes)

**Facilitator actions**

- Set up IDE / notebook with large font; ensure `numpy`, `sklearn` available.
- Narrate the story: 300 students, study hours → simulated scores → pass if score ≥ 70.
- Type or paste **live** through: imports, seed, data generation, `pass_fail` line-by-line — pause on `(scores >= 70).astype(int)` and ask why that creates labels.
- Run class distribution printout; comment if balance looks reasonable.
- `train_test_split`, `LogisticRegression()`, `fit`, `predict`, `predict_proba` — run and show first 8 rows table from notes.
- Read accuracy aloud; tie to “fraction correct.”
- Circulate or ask in chat: “Did anyone’s run differ?” (should not if seed matches.)

**Student actions**

- Run the same code locally or follow on screen; check P(Fail) + P(Pass) ≈ 1 for one row.

**Engagement**

- **Check screens:** “Show me a green check / thumbs up when your script prints accuracy without errors.”

**Bridge sentence**

“Labels are easy to report — but the business often needs confidence. Let’s separate `predict` from `predict_proba`, then add two more features.”

---

## 5. Labels vs probabilities + three-feature logistic regression (22 minutes)

**Facilitator actions**

- Two-minute concept: same label can hide different confidence (0.92 vs 0.51 both “Pass”) — scholarship / review analogy from notes.
- Live code block 2: build 3-feature dataset, `column_stack`, train, loop first 10 test students with Actual / Pred / P(Pass) / Correct.
- Print coefficients with the provided loop; ask “Which feature increases chance of passing?” (study_hours expected positive; distractions negative.)
- Keep pace: students should see coef signs, not memorize numbers.

**Student actions**

- Change one feature in a test row mentally: “Would P(Pass) go up or down?”

**Engagement**

- **Thumbs up / down:** “Thumbs up if you think raising distractions should lower P(Pass).”

**Bridge sentence**

“sklearn uses 0.5 as the default cut-off — but real decisions aren’t always 50–50. Next we change the threshold on purpose and count who gets hurt.”

---

## 6. Decision threshold — Trade-offs and manual threshold code (18 minutes)

**Facilitator actions**

- Show threshold image; hospital screening example: high threshold vs low threshold in one sentence each.
- Live code: extract `y_prob_pass = predict_proba[:, 1]`, loop thresholds `[0.3, 0.5, 0.7]`, print predicted pass counts, accuracy, FP, FN.
- After output, narrate the pattern: lower threshold → more Pass predictions, FN down, FP up — **accuracy is not the only moral of the story.**

**Student actions**

- In chat or aloud: one scenario where false negative is worse than false positive (and vice versa).

**Engagement**

- **Pair-share (90 seconds):** “Loan approval vs disease screening — which error is worse for each?”

**Bridge sentence**

“Accuracy tells you how often we’re right overall; it doesn’t tell you *how* we’re wrong — that’s what the confusion matrix is for.”

---

## 7. Confusion matrix — Concept + sklearn code + rates (22 minutes)

**Facilitator actions**

- Draw or show the 2×2 table: TP, TN, FP, FN; use memory trick True/False vs Positive/Negative from notes.
- Live code: `confusion_matrix`, extract `tn, fp, fn, tp`, print readable layout, manual accuracy, FP rate, FN rate.
- Short story: COVID / 1000 people — model always predicts negative → high accuracy but TP = 0. Emphasize why matrix beats a single accuracy number.
- Quick tie-back: if FP high → consider raising threshold; if FN high → consider lowering (link to block 6).

**Student actions**

- Point to one cell: “Which cell is ‘too optimistic’?” (FP.)

**Engagement**

- **Cold-call:** “If FN is huge, are we missing passes or failing students?” (Missing real passes — predicted Fail when Actual Pass.)

**Bridge sentence**

“We’ve closed the loop from probability to threshold to error types — let’s land the plane with a roadmap and terms you’ll reuse every week.”

---

## 8. Closing — Quick reference, next session, Q&A (10 minutes)

**Facilitator actions**

- Flash the Quick Reference table; invite students to screenshot for revision.
- Preview next session (from notes): Decision Trees, Random Forests, Precision, Recall, F1, ROC-AUC — **do not teach these today**; only set expectation.
- Take 2–3 questions; if time, one rapid-fire: “Name one output of `predict_proba` shape for binary case.” (Two probabilities per row.)

**Student actions**

- Submit remaining questions in chat or verbally.

**Engagement**

- **Exit ticket (optional):** One sentence — “What is one thing logistic regression outputs before it becomes a class label?” (Probability.)

**Bridge sentence**

“Thank you; next time we grow the model family and the metrics — bring your confusion matrix intuition with you.”

---

## Timing flex — If the session is running late

**Cut order (prefer top of list first)**

1. Shorten **pair-shares** in blocks 2 and 6 to 60 seconds each.
2. In **block 4**, paste pre-written code for data generation and spend extra time only on `fit`, `predict`, `predict_proba`, and the printed table.
3. In **block 5**, run the 3-feature loop for **5 students** instead of 10; still show coefficients.
4. In **block 6**, demonstrate **two** thresholds (e.g., 0.5 and 0.3) instead of three if needed.
5. In **block 7**, derive FP/FN rates on screen only if time; otherwise print confusion matrix and accuracy, assign rates as reading.
6. Skip the **COVID imbalance story** in block 7 and give one sentence only; keep TP = 0 example.
7. Move **block 8** quick reference to “async read” — share that students review the table at home; use 5 minutes for Q&A only.

**If ahead of schedule**

- Add 5 minutes in block 4: students tweak `n` or noise and observe accuracy drift.
- Add 5 minutes in block 7: sketch sklearn layout `[[TN, FP], [FN, TP]]` on whiteboard and quiz the room.

---


