# Lecture Script: Data Prep — Handling Messy Data

**Session duration:** 2 hours 15 minutes  
**Audience:** Mixed background; aligns with Agentic Systems Easy Track  

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions and theory stay with Lecture Notes, slides, board, or readings.

**Break (only pause in this plan):** After roughly **70–80 minutes** of session clock time, take **one** pause of **5–8 minutes**, then continue with the next teaching segment. Numbered sections below are **teaching or activity**—the break is not a numbered block.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm access to Google Colab (or your chosen environment) and the session materials.
- State headline outcomes: learners can **inspect** raw data, **handle** missing values and duplicates, **encode** categoricals (label vs one-hot), **scale** features, and **avoid data leakage** before training.
- Preview rhythm: short **live/follow-along pandas** snippets, three recurring datasets (**car**, **student**, **e-commerce**), and figures from Lecture Notes; single mid-session pause per rule above.

---

## 2. Open Colab and pandas skeleton (8 minutes)

- Direct the group to [https://colab.research.google.com](https://colab.research.google.com); new notebook; clear filename (e.g. `session26-data-prep`).
- Everyone runs: `import pandas as pd` and builds or pastes a tiny `DataFrame` (`pd.DataFrame(data)` then `df`) so output renders as a table.
- Circulate: fix import errors and ensure everyone sees a printed `df`.

---

## 3. Why data preparation matters (7 minutes)

- Project or paraphrase **Section 1** of Lecture Notes: models only see numbers and patterns; messy data becomes “learned truth.”
- Use the **exam with bad notes** analogy; show **session26-01** (why prep matters).
- One line: prep is not a formality—it sets the ceiling for how reliable the system can be.

---

## 4. Three domains, same problems (5 minutes)

- Introduce the three datasets and what each illustrates (car price, student performance, orders/pricing).
- Show **session26-02** (three domains); stress: **same quality issues**, different domains—prep is universal.

---

## 5. Load and inspect—no fixing yet (10 minutes)

- Emphasize **observation before transformation**: `df`, scan columns, mental checklist (missing, duplicate, impossible values).
- Walk examples from notes: car (missing mileage, duplicate row, negative price); student (missing marks, grade −10); e-commerce (missing quantity, negative price).
- Show **session26-03**; invite 30 seconds silent skim of one messy table in notes or on screen.
- Take 1–2 quick questions; defer line-by-line pandas tours.

---

## 6. Handling missing data (12 minutes)

- Why models choke on missing values; **imputation** as one common path.
- Live or follow-along: `.fillna(..., median)` pattern from notes (e.g. `KMs_Driven`); one sentence on **median** vs mean (robustness to extremes).
- Show **session26-04**; bridge: completeness vs introducing wrong values—balance, don’t blindly zero-fill without thinking.

---

## 7. Duplicates and invalid values (10 minutes)

- `drop_duplicates()`—why repetition biases the model toward overrepresented rows.
- Filter invalids: e.g. `df = df[df["Price"] > 0]`; list three domain examples (price, grade, order price).
- Show **session26-05**; 1 minute: “if we skip this, what bias or fantasy pattern appears?”

---

## 8. Categorical data and encoding (18 minutes)

- **Need:** text columns (`Fuel`, `Brand`, `Grade`, `Product`)—models need numbers.
- **Label encoding:** `.map({...})` demo; show table Petrol/Diesel → 0/1; then grades A/B/C if time.
- **Hidden problem:** invented **order** where none exists (fuel) vs meaningful order (grades)—design choice.
- **One-hot:** `pd.get_dummies(df, columns=["Brand"])`; sparse columns, no false ordering.
- Show **session26-06**; optional 2-minute pair prompt: “Which encoding for **nominal** brand? For **ordinal** grade?”

---

### Break (5–8 minutes)

- Optional stretch; no new content. Resume with feature scaling.

---

## 9. Feature scaling (16 minutes)

- Motivate with **magnitude**: price vs year, marks vs attendance, price vs quantity—large columns dominate distance-based thinking in many models.
- **Normalization** (min–max to [0,1]) on one column; **standardization** (mean 0, std 1) on another—show formulas from notes, not proofs.
- Show **session26-07**; thinking layer in one sentence: scaling changes **perception**, not business meaning.
- Optional: quick poll—“Which feature dominated before scaling?”

---

## 10. Preventing data leakage (12 minutes)

- Define leakage: **test** (or future) information influencing **training**; good scores, false confidence.
- **Exam paper** analogy; show **session26-08**.
- Wrong pipeline vs right: split **after** conceptual design but **fit** imputers/scalers on **train only**, apply to test; show `train_test_split` sketch from notes.
- One question: *“Would this feature exist at prediction time?”*

---

## 11. Before vs after and reflection (9 minutes)

- Narrate **Section 9**: incomplete → complete, biased duplicates → fair, text → numeric, unbalanced scales → balanced.
- Show **session26-09**; give 2 minutes silent: list **one problem** and **one fix** per dataset from memory.
- Close loop: messy data → wrong patterns; clean data → meaningful relationships.

---

## 12. Agentic systems and clean data (7 minutes)

- Bridge from ML prep to **agentic systems** (observe, decide, act); show **session26-10**.
- Tie each dataset to a failure mode (wrong price recommendation, wrong student feedback, wrong commerce insight).
- One line: **Clean data → reliable models → reliable agents.**

---

## 13. Cheatsheet recap and close (8 minutes)

- Project or skim **Libraries / Functions / Concepts** cheat sheet from Lecture Notes (pandas, sklearn split, fillna, drop_duplicates, map, get_dummies, scaling, train_test_split).
- One closing prompt: *Which step will you always do **before** training on your next assignment?*
- Thank-you; submissions, office hours, pointer to next session.

---

### Timing flex

- If the first half runs long, trim **Section 4** (three domains) to a single slide or shorten **Section 5** (inspect) to one dataset demo.
- If **encoding** needs depth, borrow 3–4 minutes from **Section 13** or **Section 11** reflection.
- If you finish **Section 13** early, use spare minutes for Q&A on **when to use one-hot vs label encoding** or **leakage in feature engineering**, without turning it into a new lecture.
