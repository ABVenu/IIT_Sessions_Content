# Lecture Script: Classification — Logistic Regression Fundamentals

**Session Duration:** 1 Hour 50 Minutes  
**Audience:** Absolute beginners (Indian students, little or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Keep the detailed explanations, definitions, and code snippets in *Lecture Notes.md*; use this script to run the room, share screens, and check that learners are following on their machines.

---

## Break rule

After roughly **55–65 minutes** of session time, take **one** break of **5–8 minutes**. Do **not** treat the break as a numbered teaching block—announce it, pause the recording if applicable, and resume with the bridge into block 6.

---

## 1. Opening, recap, and session roadmap (10 minutes)

**Facilitator**

- Welcome the group; confirm everyone can open Google Colab (or your chosen environment).
- **Cold-call** one or two students: “What did we measure in the **previous session** when a regression model made numeric predictions — name one metric.” Accept MAE, RMSE, or R².
- Bridge from regression to today: last time every answer was a **number**; today the answer is a **category** — pass/fail, spam/not spam, fraud/genuine.
- Project the session roadmap from the notes (five bullets: classification basics, logistic regression + sigmoid, labels vs probabilities, threshold, confusion matrix).

**Students**

- Connect today’s topic to Ridge/Lasso and train–test splits from the previous session.

**Engagement**

- **Thumbs up:** “Thumbs up if you’ve ever received a yes/no decision from an app — loan approved, spam folder, OTP fraud alert.”

**Bridge sentence:** “Let’s name that kind of problem properly — **classification** — and see how it differs from the regression work we just finished.”

---

## 2. Classification basics and regression vs classification (12 minutes)

**Facilitator**

- Define **classification** in plain language: pick a label from a fixed list, not a number on a scale.
- **Screen-share** the regression vs classification diagram from the notes.
- Walk the comparison table (how much vs which category). Mention **binary** (two classes) vs **multi-class** (three or more) — today focuses on binary.
- Explain **why linear regression fails** for pass/fail: outputs like −0.4 or 1.73 are meaningless; no built-in probability.
- Flash the use-case table (banking, email, HR, education).

**Students**

- Run the **Quick Activity** from the notes (R or C for four prompts). Give 2 minutes on paper or in chat.

**Engagement**

- **Cold-call:** “Item 2 — loan approved or rejected — regression or classification?” Then item 3 (exact score).

**Bridge sentence:** “When the output must be a box, not a scale, we need a classifier — and the first one we meet is **Logistic Regression**.”

---

## 3. Logistic regression intuition and the sigmoid (15 minutes)

**Facilitator**

- Clarify the naming trap: says “regression,” predicts **categories** — do not let the name confuse the room.
- Walk the three-step core flow: raw score → **sigmoid** → threshold → class 0/1.
- **Screen-share** the sigmoid diagram. Narrate: large positive score → probability near 1; large negative → near 0; zero → 0.5.
- Use the tap/water-flow analogy from the notes — probability always between 0 and 1.
- One-line link to previous session: same **coefficient** idea as linear/Ridge/Lasso, but sigmoid converts the score into a probability.

**Students**

- Sketch a rough S-curve in their notebook and label “uncertain in the middle, confident at the ends.”

**Engagement**

- **Pair-share (2 minutes):** Partner A explains “how much?” vs “how likely?” in one sentence each; Partner B gives a real-life example of each.

**Bridge sentence:** “The sigmoid gives us probability — now we train a model in code and read both the **label** and the **confidence** behind it.”

---

## 4. Live code — train Logistic Regression, predict labels and probabilities (20 minutes)

**Facilitator**

- Open a fresh Colab cell. Narrate the scenario: **study hours** → **Pass (1)** if score ≥ 70, else **Fail (0)**.
- Live-code block from the notes **line by line**: imports → `seed=42` data → `(scores >= 70).astype(int)` → `train_test_split` → `LogisticRegression()` → `fit` → `predict` → `predict_proba`.
- Pause after `predict_proba` output. Point at `[P(Fail), P(Pass)]` — columns always sum to 1.0.
- Run the print loop for the first 5 test students. Highlight one high-hours student (P(Pass) near 1) and one borderline student (P(Pass) near 0.5).
- Run `accuracy_score`; state what it means in plain language.

**Students**

- Run the same cells in their notebook. **Check screens** — confirm everyone has a printed table and an accuracy line.

**Engagement**

- **Cold-call:** “What does `predict()` give you vs `predict_proba()`?” Expected: label vs probability pair.

**Bridge sentence:** “Two students can both be labelled Pass — but their probabilities tell very different stories; let’s practice reading that before we move to thresholds.”

---

## 5. Labels vs probabilities — confidence in decisions (8 minutes)

**Facilitator**

- Contrast use cases: `predict()` for a single action (approve/flag); `predict_proba()` when confidence tiers matter (auto-approve above 0.9, manual review 0.5–0.9).
- Walk the **Quick Activity** table (Students A and B at thresholds 0.7 and 0.5). Reveal answers.
- Stress: same label, different risk — P(Pass) = 0.92 vs 0.51 both say Pass at default threshold.

**Students**

- Answer the threshold activity in chat or notebook before you reveal.

**Engagement**

- **Thumbs up:** “Thumbs up if you’d treat a 51% pass prediction differently from a 92% pass prediction in a scholarship decision.”

**Bridge sentence:** “The default cut-off is 0.5 — but that line is a **business choice**, not a law of nature; next we move it and watch mistakes change.”

---

## 6. Decision threshold — trade-offs in FP and FN (15 minutes)

**Facilitator**

- Define **decision threshold** in one sentence: probability line that turns “maybe” into Pass or Fail.
- **Screen-share** the threshold effect diagram from the notes.
- Walk the table: lower threshold → more Pass, fewer FN, more FP; raise threshold → opposite.
- Live-code the threshold loop from the notes on the **same model** from block 4 — thresholds 0.3, 0.5, 0.7; print FP and FN counts.
- Narrate the output pattern: accuracy may barely move while FP/FN swap — accuracy alone hides the story.

**Students**

- Run the threshold cells; compare FP/FN across the three thresholds in their output.

**Engagement**

- **Cold-call:** “For **fraud detection**, would you generally lower or raise the threshold — and why?” Accept lower if missing fraud is costly.

**Bridge sentence:** “Threshold tuning names two error types — **false positive** and **false negative** — and the **confusion matrix** puts all four outcomes in one table.”

---

## 7. Confusion matrix — TP, TN, FP, FN (18 minutes)

**Facilitator**

- Open with the COVID test story from the notes: 90% accuracy but TP = 0 if always predicting Negative.
- **Screen-share** the confusion matrix diagram. Walk the 2×2 table slowly — TP, TN, FP, FN.
- Teach the memory trick: True/False = correct? Positive/Negative = what did the model predict?
- Live-code `confusion_matrix`, extract tn/fp/fn/tp, print the readable layout, compute accuracy manually, verify with `accuracy_score`.
- Connect back to block 6: high FP → model too generous (raise threshold); high FN → too strict (lower threshold).

**Students**

- Run confusion matrix cells on the same test split. Label each cell in plain English in a comment or notebook markdown cell.

**Engagement**

- Run the **Spot the Risk** activity (fraud model: FN = 105 vs FP = 5). **Pair-share:** which error is worse for the bank?

**Bridge sentence:** “You now have the full beginner classifier toolkit — probability, threshold, and a matrix that tells the truth accuracy hides.”

---

## 8. Recap, key takeaways, and close (10 minutes)

**Facilitator**

- Rapid-fire **key takeaways** from the notes (classification vs regression; sigmoid + predict vs predict_proba; threshold trade-off; confusion matrix always alongside accuracy; train–test discipline unchanged).
- Point learners to the **Important Commands** table for revision.
- Preview lightly: later work adds more classifiers and metrics like precision and recall — no session numbers needed.
- Remind learners to complete any linked assignment or pre-read for the next class.

**Students**

- Skim the glossary table; star three commands (`predict_proba`, threshold line, `confusion_matrix`).

**Engagement**

- Final **cold-call:** “Name one cell of the confusion matrix — what does **False Negative** mean in the pass/fail example?”

**Bridge sentence:** “Carry forward the same honest split habit: **fit on train, read probabilities and mistakes on test** — that discipline does not change when we switch from numbers to categories.”

---

## Timing flex — if you are running late

- **Cut first (save core demos):** Shorten pair-shares from 2 minutes to 1; trim extended Q&A in blocks 2 and 3; show sigmoid and regression-vs-classification diagrams briefly instead of full narration.
- **Cut second:** In block 4, live-code through `fit` and `predict` only; assign `predict_proba` print loop as a follow-along after class. In block 5, do the threshold activity verbally without waiting for all chat responses.
- **Never skip:** Block 4 (`fit` / `predict` / `predict_proba` on a held-out test set) and block 7 (confusion matrix with TP/TN/FP/FN) — these are the session’s core outcomes.
- **If ahead of schedule:** Add 5 minutes for students to change threshold to **0.4** and **0.6** independently and report how FP/FN shift; or run a **mini-poll**: “Loan approval — which error is costlier, FP or FN?”
