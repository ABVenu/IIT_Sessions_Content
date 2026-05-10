# Lecture Script: Loops and Iteration (While, For, Range, Break, Continue, Nested Loops)

**Session duration:** 2 hours 15 minutes  
**Audience:** Learners building on conditionals and basic Python; first structured exposure to iteration  

**Examples in the Lecture Notes:** The notes include **many** worked examples. The **same** document (or equivalent) is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set of examples that fits the clock and your group—enough to make the idea click; point learners to the rest in the notes for practice and deeper understanding.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, notebook, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 70–80 minutes** of session clock time (after the **range** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm IDE / Jupyter / Colab access and that everyone can run a short Python cell.
- State headline outcomes: **while** for condition-driven repetition, **for** for sequences, **range** for numeric iteration, **break** / **continue** for loop control, **nested loops** for grids and combinations.
- Preview rhythm: short live coding after each big idea; notes contain flowcharts—show them, do not read captions verbatim.
- Point to pre-read or bundle materials if your cohort uses them; defer long debugging to office hours.

---

## 2. While loops: concept, syntax, first runs (20 minutes)

- Motivate with **iteration** in one line: repeat code without copying it; tie to the **“power of repetition”** and optional real-life “while …” examples from the notes (laundry, dishes, traffic light).
- Display the **while-loop flowchart** from the notes; one sentence: condition checked **before** each body execution.
- Write **basic syntax** on board or share cell: `while condition:` indented body.
- **Live / follow-along:** **Example 1** (count to 5). Narrate: initialize, loop while true, **must** update (`count += 1`) so the condition can become false.
- **Live:** **Example 2** (password length validation)—or simulate with fixed strings if avoiding `input()` in a large room; emphasize **while** + validation pattern.
- Invite 1–2 verbal predictions before running: *What prints last? When does the loop stop?*
- Take 1–2 clarification questions; avoid extended history-of-programming unless someone asks.

---

## 3. Infinite loops and one real-world pattern (10 minutes)

- **Warning block:** show the **forgotten increment** bug; run or trace the bad version mentally, then the corrected version—stress **eventual falseness** of the condition.
- Either **ATM withdrawal** or **number guessing** from the notes as a **read-along or instructor demo** (8–9 minutes); highlight `break` lightly as “we’ll formalize next half” if you use quit logic.
- Recite **Key Takeaways** for while (from notes) as a **three-bullet closing strip**, not a paragraph.

---

## 4. For loops: sequences and readability (20 minutes)

- Contrast with **while**: manual counter vs **“for each item in sequence.”** Use the **for-loop flowchart** from notes briefly.
- **Syntax:** `for item in sequence:`.
- **Live:** iterate a **string** (letters); then a **list** (fruits)—learners type or mirror your notebook.
- **Side-by-side:** **for** with `range(5)` vs **while** counter—same output, different intent; when to choose which (known steps vs open-ended condition).
- Optional **2 minutes:** pairs name one collection from their domain (grades, names, SKU codes) and a one-line loop body—cold-call two ideas.
- **Skim** real-world snippets (**validate all inputs** with `break`, **process prices** with tax)—run one if time feels tight, or assign as post-class drill.
- Close with **for-loop takeaways** as a quick checklist.

---

## 5. The `range()` function (22 minutes)

- Motivate **lazy / on-demand** numbers—ticket-dispenser analogy; optional mention of Python 2 vs 3 in **one** sentence if helpful.
- Show the **range + for** diagram from notes.
- Teach **three forms** on the board: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`—stress **stop is exclusive**.
- **Live:** print loops for each form; add **countdown** with negative step.
- **Live or demo:** **multiplication table** for one fixed `num`, **year range**, or **step by 3**—pick two so learners see step and bounds.
- **`range(len(list))` vs direct iteration:** show index loop for `fruits`; note when index is needed (parallel lists, mutation positions)—avoid over-deep theory.
- **Key takeaways** for range: object not list, exclusive end, defaults, downward step.
- **Break timing:** this is a natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

---

## 6. Control loops with `break` (15 minutes)

- Define: **`break` exits the current loop immediately**; execution resumes after the whole loop. Show **break flowchart** from notes—do not read long captions aloud.
- Motivate: search / user quit / first error—**efficiency** in one phrase.
- **Live:** **linear search** with `while` + index, or **`while True`** + `input` quit—choose one short pattern learners can copy.
- **For-loop `break`:** **print until 6** example; optional **first match** by index.
- **Early exit on error** (divide by zero list): demo or trace—emphasize avoiding useless work after fatal case.
- Remind: **`break` only exits the innermost loop** (preview nested section); 30 seconds on **break vs loop condition** dual-style if notes show both.
- **Takeaways** as three bullets.

---

## 7. Control loops with `continue` (16 minutes)

- Define: **`continue` skips rest of current iteration**; loop **continues**. Contrast with **`break`** in one table or two sentences.
- Show **`continue` diagram**; optional **break vs continue** composite figure—learners skim silently ~20 seconds.
- **Live:** **skip evens** in **while** (counter placement—stress still advancing `count` to avoid accidental infinite loop).
- **Live:** **for** + **continue** to print odds or filter passing scores.
- **`continue` vs `break` side-by-side** snippet from notes—predict output before running.
- **Nested preview:** show snippet where **`break` only leaves inner loop**; state that **`continue`** also applies to innermost loop only—no new nested exercises yet unless group is fast.
- **Takeaways** four bullets max.

---

## 8. Nested loops (14 minutes)

- Motivate: **rows × columns**, combinations, graphics—use **book chapters / attendance row** analogy from notes briefly.
- Show **nested loops diagram** from notes.
- **Syntax:** outer `for`, inner `for`; inner **completes** for each outer step.
- **Live:** `i,j` double loop small ranges; trace **order of prints** on board once.
- **Patterns:** **rectangle of stars**; **multiplication table** OR **right triangle**—pick two live; third as homework if squeezed.
- Reiterate: **`break` / `continue` bind to innermost** enclosing loop.
- **Takeaways** five bullets skimmed.

---

## 9. Synthesis, practice hooks, and close (5 minutes)

- One screen or board: **decision guide**—open-ended condition → **while**; known sequence → **for**; integers → **range**; stop whole loop → **break**; skip one pass → **continue**; 2D / pairs → **nested**.
- Optional closing question: *Name one problem from your field that needs a loop—while or for?*
- Assignments / lab pointer; thank-you; where to ask questions next.

**Sum of numbered teaching segments:** 5 + 20 + 10 + 20 + 22 + 15 + 16 + 14 + 5 = **127 minutes** of teaching, plus **5–8 minutes** break ≈ **132–135 minutes** total session clock—adjust Q&A within block 9 if your institution requires exact 135-minute dismissal.

---

### Timing flex

- **If behind:** Shorten **3** (demo one app only), **4** (skip pair micro-task; one real-world skim), or **8** (one pattern live, two as reading).  
- **If ahead:** Add **6–8 minutes** in **5** (more `range` drills) or **9** (debug clinic: off-by-one in `range`, forgotten increment in `while`).  
- **If `input()` is awkward in lab:** Replace interactive examples with **preset strings** or **hard-coded “user” variables** and say “in homework you’d use `input()`.”
