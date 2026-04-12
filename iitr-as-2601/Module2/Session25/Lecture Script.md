# Lecture Script: The ML Workflow & Habits

**Session duration:** 2 hours  
**Audience:** Mixed background; first exposure  

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—delivery of definitions and theory stays with your chosen slides, board, or readings.

**Break (only pause in this plan):** After **~60–75 minutes** of session clock time, take **one** pause of **5–8 minutes**, then continue with the next teaching segment. Every numbered section below is **teaching or activity**—there are **no** “break” sections in the list.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm everyone can access the session workspace (devices and any platform you use for the cohort).
- State the three headline outcomes: a shared workflow vocabulary, correct use of train/validation/test ideas, and the habit of comparing to a baseline.
- Preview the rhythm: short Colab practice first, then structured walk-through with figures; the single pause is timed by the **Break** rule at the top (not a numbered block in this list).

---

## 2. Open Colab and create a notebook (10 minutes)

- Direct the group to [https://colab.research.google.com](https://colab.research.google.com); sign-in as needed.
- Everyone creates a **New Notebook**; pick a clear filename (e.g. session topic + date).
- Circulate: confirm each person sees an empty notebook with at least one code cell.

---

## 3. Orient to the interface (5 minutes)

- Screen-share: distinguish **code cell** vs **Markdown cell**; give your own one-line labels if learners use different terms.
- Show where output appears after a run; demonstrate **Run** and a common shortcut (e.g. Shift+Enter) your setup supports.
- Give a short silent look at your on-screen summary of cells and outputs; answer logistics only (login, file rename).

---

## 4. First run and variable snippet (15 minutes)

- Everyone runs a one-line **print** hello-style example; confirm printed output below the cell.
- Everyone runs a tiny example with **three variables** (e.g. two counts and one score) and prints them; confirm three values appear.
- Pause 2 minutes for anyone stuck; use breakout or peer help if available.
- Bridge in one line only: *later topics reuse this habit—small change, run, read output.*

---

## 5. Walk the ML workflow section (18 minutes)

- Project **machine learning workflow** content: vocabulary people need for the rest of the day, then the ordered **stages** from problem → data → model build → evaluation, then your **workflow** figure or diagram.
- Read *nothing* line-by-line; skim aloud only headings or prompts; let the visual carry structure.
- Invite learners to skim any **analogy** table you use (e.g. cooking) silently (~30 seconds).
- Take 2–3 clarification questions; defer deep theory to office hours or readings.

---

## 6. Problem framing and problem classes (12 minutes)

- Move to **framing problems**: one numeric-prediction example and one category example side by side if you have both.
- Ask pairs (or the room): **which field is the thing you predict, not an input—would you have it in real life before you predict?** Keep discussion short; nudge with your framing checklist only if stuck.
- Cold-call one or two groups for a one-sentence answer; resist turning it into a full lesson.
- Optional: 3 minutes silent—everyone drafts a one-line problem statement + feature list + label name (on paper or in a cell).

---

## 7. Features vs labels (12 minutes)

- Show a **small table** with several input columns and one target column; show your **features vs label** figure if you have one.
- Quick poll: thumbs up/down—“In that table, is *Price* a feature?” Resolve by pointing to your written definitions on screen, not a long explanation.
- Optional paired task: same **feature vs label** marking on the category example from the previous block.
- If time allows: run a **parallel lists** snippet (e.g. lists of sizes, bedrooms, prices) together in Colab.

---

## 8. Data splits and the split figure (12 minutes)

- State **why** train and test must differ; name the three roles—**training**, **validation**, **test**. Ask which role fits a “final exam” before you reveal your comparison slide or table.
- Show the **train / validation / test** figure; read aloud once any short caption that decodes labels on the diagram (model, parameters, etc.) if your visual uses them.
- Mention typical percentage bands (e.g. rough thirds or 70/15/15 style) in one sentence; do not derive formulas.

---

## 9. Manual holdout code (6 minutes)

- Live or follow-along: two aligned lists (e.g. sizes and prices), slice first part into `train_*` and remainder into `test_*`; ask what changed between the two slices using learner output.
- One reminder only: **aligned rows**—same index means the same house in both lists.

---

## 10. Data leakage image and guideline (9 minutes)

- Show a **data leakage** visual; ask for one real-world “unfair hint” example from volunteers before you list common cases on screen.
- Read aloud once your **rule of thumb** on fitting preprocessors on training data only; do not add extra policy.

---

## 11. Baselines and closing loop (6 minutes)

- Show a **baseline** visual; run or display output of a **predict the average** (or majority class) toy example.
- If short on time, point to a short **baseline vs model** comparison as take-home reading.
- Display a **workflow checklist** (environment → problem → data → split → baseline → model); tick through mentally.
- Give a **recommended practices** strip as self-check; one closing question: *Which checklist step will you use first on the next assignment?*
- Thank-you; where to submit / next session pointer.

---

### Timing flex

If you need to recover time in the first half, trim **Problem framing and problem classes** (skip pair discussion) or **Manual holdout code** (instructor demo only). If you finish **Baselines and closing loop** early, use spare minutes for Q&A on **model vs parameters vs splits**, without turning it into a full lecture.
