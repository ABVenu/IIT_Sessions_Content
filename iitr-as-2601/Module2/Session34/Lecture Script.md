# Lecture Script: ML Workshop — Model Selection & Comparison

**Session Duration:** 2 hours 15 minutes  

**Target Audience:** Learners from diverse backgrounds, including those without prior technical training (e.g. Indian students new to ML). Delivery should stay concrete, analogy-led, and define jargon before stacking it.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style.

**Break rule:** After 60–75 minutes of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

---

## 1. Welcome, Bridge From Time Series, and Learning Outcomes (10 minutes)

- Welcome the group; **bridge from Session 33:** row order mattered for **time series**, MAPE, rolling features — today we zoom out to a question learners already feel: “I trained several models… **which one do I ship?**”
- Share the objectives from “What you will learn”: **metric comparison table**, **complexity**, **save/load** models, **selection checklist**.
- **Engagement — cold-call:** “Have you ever compared two phones or two plans side by side — what columns did you look at?” (Relate to *multiple metrics*, not one number.)
- **Room action:** Open the lecture-notes outline on screen so they see the four pillars of today’s session.

**Bridge sentence:** “Before we argue about algorithms, every team puts numbers in **one sheet** — the metric comparison table.”

---

## 2. Metric Tables — Definitions, Analogies, and the Visual (8 minutes)

- **Official definition** vs **simple words** (“marksheet for models”); **cricket selectors** analogy from notes — no code yet.
- Show the **metric comparison table** figure; pause on **rows = models**, **columns = metrics**.
- **Thumbs check:** “If I only stared at Accuracy and ignored Recall, could I badly hurt a fraud or medical use case?” (Expect mixed; tease depth without solving full cost-sensitive learning.)
- **Room action:** Point at column headers in the slide image — align with terminology they learned earlier (Accuracy, Precision, Recall, F1).

**Bridge sentence:** “Same idea works in code — we loop models, append one row each, drop it into a DataFrame.”

---

## 3. Live Demo — Classification Metric Table (Breast Cancer) (13 minutes)

- **Live-coding (or staged notebook with pause points):** imports → `load_breast_cancer` → `train_test_split` → **`StandardScaler` fit on train only** → dictionary of three classifiers → loop: `fit`, `predict`, `append` metrics → `DataFrame`, `set_index("Model")`, `print`.
- Stress **why** scaling for Logistic Regression; **dictionary loop** pattern as reusable professional habit.
- Walk **sample output** table briefly: note **Logistic Regression** competitive on F1 despite simplicity — preview today’s complexity theme.
- **Room action:** Circulate — confirm beginners have **fitted scaler on train**, **transform** on test only; watch for swapping those lines.
- **Pair-share (90 sec):** “Name one mistake that makes the metric table meaningless.” (Leakage answers welcome; steer to honest split today, leakage session was broader.)

**Bridge sentence:** “Classification used discrete labels — now we flip the metric columns to **MAE, RMSE, R²**, same table pattern.”

---

## 4. Live Demo — Regression Metric Table (California Housing) (10 minutes)

- **Demo:** housing fetch → split → scale → three regressors → loop with **MAE, RMSE (sqrt MSE), R²**.
- Explicit line: **`np.sqrt(mean_squared_error(...))`** — sklearn gives MSE; RMSE needs the root.
- **Direction of good:** lower MAE/RMSE; R² nearer 1.0.
- Sample output: **Random Forest** dominates — emphasize “winner at a glance.”
- **Engagement — cold-call:** “Which single number would you *not* use alone to pick a regression model?” (Push toward “table + constraints,” not zealotry against one metric.)

**Bridge sentence:** “Tables hide *why* a simple model sometimes wins — so we introduce **complexity**: flexibility vs assumptions.”

---

## 5. Model Complexity — Spectrum, Table, Interpretability Stakes (11 minutes)

- **Official definition** + **shirt tailoring** analogy; teacher-grading analogy for simple vs heavy rules.
- Display **complexity spectrum** figure; walk the **comparison table**: Logistic/Linear ↔ Neural Nets across training speed and interpretability.
- Anchor **who needs explanations:** loan officer vs recommender engine — ties to stakeholder reality.
- **Check for thumbs up:** “Interpretability matters for every project — yes or no?” (Debrief: **context-dependent.**)

**Bridge sentence:** “Complex models can memorize noise — that twin enemy pair is **underfitting** and **overfitting**.”

---

## 6. Overfitting vs Underfitting — Language, Imagery, Intuition (10 minutes)

- Read definitions once carefully; reinforce with **exam-memorization** vs **only two chapters studied** analogy.
- **Weather model** analogy for under- vs overfit from notes.
- Show **three-curve diagram** slide; learners only name curves, you label.
- No code yet — keep cognitive load on **train vs test** story.

**Bridge sentence:** “We make that story measurable by printing **training accuracy beside test accuracy** and watching the gap.”

---

## 7. Live Demo — Tree Depth vs Train–Test Gap (11 minutes)

- **Demo:** breast cancer scaled data → loop `DecisionTreeClassifier` **max_depth** in `{1, 3, 5, 10, None}` → train_acc, test_acc, **gap** column → `DataFrame`.
- Narrate depth 5 “sweet spot” vs **Unlimited**: train hits 100%, test falls — textbook overfitting signature.
- **Engagement — cold-call:** “If train is 99% and test is 76%, where is your first debugging instinct?” (Complexity / regularization direction.)
- **Room action:** Have them run once locally or follow your screen — verify **`None`** displays as Unlimited in notes’ convention (string formatting in snippet).

**Bridge sentence:** “Metrics plus gap tell us *whether* extra complexity buys anything — next are **rules of thumb**: when simplicity wins.”

---

## 8. Golden Rules of Complexity — Occam’s Razor (6 minutes)

- Rapid bullets: **simple when** — small data, explainability, good enough scores, latency; **complex when** — large data, accuracy-first, nonlinear signal, compute budget.
- Quote **Occam’s Razor for ML**: simplest adequate model wins for most production decisions.
- **Pair-share (60 sec):** “One situation from work or campus where explainability beats 1% accuracy.”

**Bridge sentence:** “Selecting a champion is pointless if every deploy restarts training from zero — Enter **model persistence**.”

---

**→ Take the single break (5–8 minutes) here if cumulative teaching time sits near 60–75 minutes.←**

---

## 9. Model Persistence — Concept and `joblib` Walkthrough (13 minutes)

- **Why:** retraining per request absurd at scale — **spam filter** deployment story from notes.
- Show **pipeline figure** train → save → load → predict.
- **Live demo:** train `RandomForestClassifier` → **`joblib.dump(model, …)`** and **critical second dump: `joblib.dump(scaler, …)`** → separate cell “new session” **`joblib.load` both** → `transform` **with loaded scaler**, then `predict`.
- STOP and spotlight: fresh `StandardScaler()` on new rows = silent disaster.
- **Thumbs poll:** “Is saving only the `.joblib` file enough if you used scaling?”

**Bridge sentence:** “Pickle exists for completeness — same idea, slightly different ergonomics.”

---

## 10. Pickle Alternative, Comparison Table, and Security Note (8 minutes)

- **Walk `pickle` snippet** emphasizing `'wb'` / `'rb'` and context managers — no need to memorize bytes, just **why binary**.
- Flash **joblib vs pickle** comparison table — official sklearn recommendation lands on **joblib**.
- **Security:** never load pickles/joblibs from strangers — executes code narrative in plain language without fear-mongering.
- **Engagement:** “Why might joblib beat pickle for forests?” → large numpy internals.

**Bridge sentence:** “Real teams also version artifacts and preprocessors — bundle habits before the checklist ties it together.”

---

## 11. Persistence Hygiene — Four Practical Tips (5 minutes)

- Bullet through: **always save preprocessing objects**, **version filenames**, **sanity-check load predictions**, **untrusted files**.

**Bridge sentence:** “Persistence answers *how we ship* — the checklist answers *what we tried first and why*.”

---

## 12. Model Selection Checklist — Questions 1–2 (9 minutes)

- Framing diagram: checklist as **doctor intake** metaphor.
- **Q1 Problem type** grid — Classification vs Regression vs Clustering vs Time Series branch.
- **Q2 Data volume** tiers — reinforce small-data bias toward simpler models.
- **Cold-call:** “Why can’t I default to Random Forest on 200 rows?” (Overfit / Memorization hook.)

**Bridge sentence:** “Stakeholder and latency questions shave the option list further.”

---

## 13. Checklist Questions 3–6 and Decision Flow (11 minutes)

- **Q3 Interpretability**, **Q4 Speed**, **Q5 Linearity**, **Q6 Noise/outliers** — fast table talk, relate back to Decision Tree robustness bullets.
- Project **ASCII decision flow** on slide; narrate branching **supervised → regression vs classifier → …** without reading every line mechanically.
- **Pair-share:** “Walk your partner down the chart for predicting house prices (regression, medium-large data). Where do you exit?”

**Bridge sentence:** “Whatever the checklist says, we enforce a repeatable training loop — baseline upward with a complexity filter.”

---

## 14. The Full Protocol — Compare, Filter, Save (13 minutes)

- Present **five-step Start Simple, Go Complex** list verbally.
- **Code walk (live or scrolled):** ordered dict three models ascending complexity → compute test **F1** → `best_f1` → earliest model within **0.02** gap wins → **`joblib.dump` model + scaler**.
- Interpret **insertion-order loop** selects simplest qualifying model explicitly.
- **Room action:** Invite them to tweak threshold in chat/discussion — “Would 0.01 change real life?” qualitative only.

**Bridge sentence:** “Everything today clicks into pipelines next — recap locks it in.”

---

## 15. Takeaways, Glossary Pulse, Next-Session Hook (7 minutes)

- Rapid-fire **five key takeaways** from notes — metric tables, complexity + gap, start simple, **joblib + scaler**, checklist.
- Optional 60-second skim of **Important Commands** table on screen — no row-by-row reading.
- Tease upcoming **end-to-end ML pipelines**.
- **Exit ticket:** “Two bullet points in chat: (1) one sign of overfitting, (2) one object besides the model you must save.”
- Thank learners; redirect to notebooks and assets in Session 34 folder.

**Bridge sentence:** (Closing line if needed.) “Professional ML is comparing honestly, resisting useless complexity, and shipping artifacts — not rerunning folklore in isolation.”

---

## Timing Flex — If the Session Is Running Long

- **First trims (save ~8–12 minutes):** Shorten both **pair-shares** to 45–60 seconds; show **classification** and **regression** tables as screenshots + narrate loops instead of line-by-line typing; deliver **golden rules + Occam** as three spoken bullets without extended discussion.
- **Second trims (save ~10–15 minutes):** Run **tree-depth** demo as executed notebook scroll only (no typing); collapse **pickle segment** into “exists, use joblib for sklearn”; read **decision-flow ASCII** as top half only assign bottom half reading.
- **Last resort:** Make **protocol code** asynchronous reading — in session, verbally state **baseline → ladder → threshold → dump** without executing; keep **live** the **classification table** AND **joblib+scaler** (non-negotiable hands-on pillars).
- **If ahead of time:** Add poll — “Higher train accuracy alone proves the better model — T/F”; extra Q&A on **when Precision beats Accuracy** using medical/fraud anecdotes from earlier modules.

**Never cut:** the idea of **side-by-side metric tables** (not single-score decisions); **train–test gap** as overfitting signal; **`joblib` + paired preprocessing save**; the **spirit** of checklist before algorithm roulette.

---
