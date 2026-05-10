# Lecture Script: The ML Workflow & Habits

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian students; may have little or no tech background (comfort with Pandas/SQL/viz from prior sessions is assumed).

**Break rule:** After roughly 60–75 minutes of instruction, take one 5–8 minute pause (not timed as a numbered block). Students should step away from the screen, hydrate, and stretch.

**How to use this file:** This document is for **timing and facilitation only**. It is not a substitute for the Lecture Notes; use it to pace the room, manage devices, and cue engagement. Keep the Lecture Notes open for definitions, code, and diagrams.

---

## 1. Colab as the ML lab — setup & first runs (25 minutes)

**Facilitator**
- Screen-share `colab.research.google.com`; confirm everyone can sign in with a Google account.
- Narrate the “lab coat” analogy from the notes: browser-based, no local Python install.
- Walk through: New Notebook → rename to something like `Session13_ML_Workflow.ipynb` → Connect → point out RAM/disk when live.
- Show **Runtime → Change runtime type**; say CPU is fine today; GPU is for heavier work later.
- Display the interface table from the notes (code vs markdown, toolbar, Run, + Code / + Text).
- Live-code the first cell (`Hello from Google Colab!` + `sys.version`); run with **Shift + Enter**.
- Add the **imports** cell (`pandas`, `numpy`, `matplotlib`, `train_test_split`, `DummyClassifier`, `accuracy_score`); run and confirm “All libraries imported successfully!”
- Mention 2–3 shortcuts (`Ctrl + Enter`, `Ctrl + M B`) — avoid dumping the full list.

**Students**
- Open Colab, create notebook, connect runtime, run both starter cells.
- Raise hand or chat if import errors appear (rare in Colab).

**Engagement**
- **Thumbs up:** “Thumbs up when you see ‘All libraries imported successfully!’ on your screen.”
- Circulate; check 4–5 student screens for connection status and output.

**Bridge sentence:** “Colab is our kitchen; now we talk about what we’re actually cooking — what ML is and the recipe every serious practitioner follows.”

---

## 2. What ML is & the six-step workflow (22 minutes)

**Facilitator**
- Contrast **rules-first programming** vs **examples-first ML**; use dog/child analogy briefly.
- Show the diagram (regular programming vs ML) if projected.
- Walk the **three problem types** table (classification, regression, clustering) — one example each.
- Present the **six steps**: Frame → Collect & prepare → Engineer features → Split → Baseline → Evaluate.
- Clarify: today goes deep on framing, features/labels, splitting, baseline; data prep and full evaluation loops come later.
- Show the workflow diagram; stress “skipping a step = skipping a floor.”
- List the three beginner mistakes: **train on all data**, **skip baseline**, **peek at test early** — tie each to the workflow.

**Students**
- Note the step list in their notebook (markdown cell) or on paper.

**Engagement**
- **Cold-call (gentle):** “Name one business question that sounds like **classification**.” Rotate rows if needed.

**Bridge sentence:** “If the workflow is the blueprint, **problem framing** is writing the job description for the machine — what it predicts, from what, and how we score it.”

---

## 3. Framing problems, features & labels — with live `X` and `y` (28 minutes)

**Facilitator**
- State the framing definition; use the **doctor / diabetes** example.
- Write the three questions on the board or slide: **predict what?** (label), **from what data?** (features), **metric?**
- Walk the **template sentence**: “Given [inputs], predict [output], measure with [metric].”
- Go through 2–3 rows of the “vague vs well-framed” table quickly.
- **Quick activity:** Display the “Classification / Regression / Clustering” table; give 90 seconds.
- **Pair-share:** Pairs compare answers on the ambiguous row (*which city for next store* — regression vs clustering); debrief for 1 minute.
- Teach **label** vs **feature** with the student-performance story; show the features vs labels diagram.
- Screen-share or live-code: load `student_performance.csv` (ensure file is uploaded to Colab or use course-provided path), `columns`, `head`, then `y = df["result"]`, `X = df.drop(columns=["result"])`, print shapes.
- **Data leakage:** “Would you put the answer key in the question paper?” — label in `X`, derived columns; double-check `X`.

**Students**
- Follow along in Colab with the same dataset; fix path issues with help from peers or TA.

**Engagement**
- **Pair-share** as above; **circulate** during the `X`/`y` split.

**Bridge sentence:** “We’ve separated clues from the answer — next we decide **which** rows the model studies and **which** rows stay hidden for honest grading.”

---

## 4. Train / validation / test — splits, overfitting, and split-first rules (24 minutes)

**Facilitator**
- Use textbook / weekly test / board exam analogy for train / val / test.
- Show the-purpose table; explain **why three splits** (protect the test set).
- Define **overfitting** in one plain sentence; relate to “memorised last year’s paper.”
- Mention **60/20/20** and that ratios can vary with data size — don’t memorize only one recipe.
- Live-code or walk line-by-line: two-step `train_test_split` (20% test, then 25% of remainder for val); emphasize `random_state=42` and printing row counts.
- **Leakage during splitting:** scaling or imputing **before** split — say “split first, **fit** transforms on train only, then apply to val/test.”

**Students**
- Run the split code; verify train ≈ 60%, val ≈ 20%, test ≈ 20%.

**Engagement**
- **Thumbs up** when printed row counts look sane (no zeros, sums roughly match total).

**Bridge sentence:** “Before we build anything smart, we need the **dumbest fair score** in the room — that’s the baseline.”

---

## 5. Baselines, dummy models, and beating the floor (22 minutes)

**Facilitator**
- Define baseline; use **cricket par score** or “predict majority class” intuition.
- Why baselines matter: avoid celebrating noise, catch trivial problems, set comparison point.
- **Types table** — focus on **most_frequent** and **mean** for today.
- Live: `value_counts()` and normalized percentages on `y` **before** modeling — “What accuracy if we always guess the majority?”
- Fit `DummyClassifier(strategy="most_frequent")`, predict on test, `accuracy_score`; show `classification_report`.
- **Imbalance hook:** If notes example is ~72% Pass, connect accuracy to majority; preview that F1/recall matter when classes skew.
- Optionally run **baseline vs `DecisionTreeClassifier(max_depth=3)`** side-by-side; read improvement in percentage points.

**Students**
- Run baseline cells; copy reported accuracy into a markdown note: “My baseline today: ___.”

**Engagement**
- **Cold-call:** “If always predicting ‘No default’ gives 82% accuracy, is that always a good model? Why not?”

**Bridge sentence:** “Let’s wire those same habits into one story — a bank asking *will this borrower default?*”

---

## 6. Loan default thread, habits, recap & questions (14 minutes)

**Facilitator**
- Walk the **integrated Colab story** as **separate cells** (imports → framing comments → load/inspect → label distribution → `X`/`y` → 60/20/20 split → `DummyClassifier` + metrics).
- Pause on: class imbalance (e.g., 82% No), baseline accuracy, **recall for “Yes”** in the report — “accuracy can hide failure on the rare class.”
- Rapid-fire **good habits**: check label distribution, set `random_state`, don’t touch test until the end, start simple, document framing in markdown, version your notebook (GitHub if applicable).
- Summarise **takeaways** from the notes in 60–90 seconds; open floor for questions.

**Students**
- Optionally save notebook; submit or sync per course process.

**Engagement**
- Final **thumbs up:** “Thumbs up if you could explain to a friend what `X` and `y` are.”

**Bridge sentence:** (End of session) “Next sessions deepen data prep and evaluation — today you locked in environment, workflow, framing, splits, and baseline.”

---

## Timing flex (if running late)

- **Cut first:** Shorten block 6 — cover only cells 1–7 of the loan example plus habits list; assign remainder as async reading.
- **Cut second:** Skip live **DecisionTree** comparison in block 5; keep `DummyClassifier` + `classification_report` only.
- **Cut third:** Reduce pair-share in block 3 to one row + 30 seconds; keep `X`/`y` demo.
- **If ahead:** Add student challenge in block 3 — one pair writes a framing sentence for “fraud transaction” and reads aloud; in block 5, show **regression** `DummyRegressor` snippet without full execution.

---
