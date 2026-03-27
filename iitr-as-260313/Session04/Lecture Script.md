# Lecture Script: Lists, Iteration, Comprehensions, and Functions

**Session duration:** 2 hours 15 minutes  
**Audience:** Learners who have conditionals and loops; first structured pass at **lists** as collections and **functions** as reusable units  

**Examples in the Lecture Notes:** The notes include **many** worked examples. The **same** document (or equivalent) is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set of examples that fits the clock and your group—enough to make the idea click; point learners to the rest in the notes for practice and deeper understanding.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, notebook, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 60–70 minutes** of session clock time (after **iterating through lists**), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm VS Code is opened and ready to learn
- State headline outcomes: **create and shape lists**, **index and slice** safely, **iterate** with `for` / `enumerate` / `zip`, **list comprehensions** for concise transforms, **`def` functions** with **parameters**, **`return`**, and **defaults** (including mutable-default caution).
- Preview rhythm: heavy **live coding** alongside the notes’ figures; connect back to Session 03 loops where notes do.
- Point to bundle or pre-read if your cohort uses them; defer long debugging to lab or office hours.

---

## 2. Creating and initializing lists (12 minutes)

- Motivate **ordered collections**: one name, many items; optional **playlist / building** analogies from the notes—keep under one minute.
- Show the **list creation diagram** from notes briefly.
- **Live / follow-along:** `[]`, `list()`, literals (ints, strings, mixed types if you want one example), **duplicates OK**.
- **`list(range(...))`**, **`list("hello")`**, **`split()`**—run two of three so learners see “from other types.”
- Quick **nested list** (mini matrix) and one **access** example (`matrix[0][1]`) to foreshadow iteration and slicing.
- Optional **10 seconds each:** `*` repeat and `+` concatenate—demonstrate or point to notes.
- Close with **Key Points** from notes as a **five-bullet** skim, not a lecture.

---

## 3. Accessing elements with indexing (12 minutes)

- Motivate **random access** vs walking the whole list; show **indexing figure** from notes.
- Emphasize **0-based** indexing with one mnemonic (**steps from start**); **negative indices** on the board with a tiny list.
- **Live:** read first, last, `[-1]`, out-of-range intentionally in a notebook to show error—then **`if index < len(...)`** or **exceptions** per your course policy.
- **`in`**, **`index`**, **safe find** patterns from notes—demo or read-along one short snippet.
- **Mutating by index** if the notes include a one-line example; remind that lists are **mutable**.
- 1–2 clarification questions; skip long FORTRAN history unless asked.

---

## 4. Slicing: sublists and slice assignment (18 minutes)

- Introduce **slice** as “sublist view / copy” pattern: `[start:stop:step]`; **stop exclusive**—say it three times in different words.
- Show slicing visuals or examples from notes; walk **omit start**, **omit stop**, **full copy** `[:]`.
- **Live:** positive and negative bounds, **step**, **reverse** a copy—learners predict outputs before running.
- **Slice assignment:** replace span, insert with empty slice, delete with `[]`; note **length rules** when step is not 1 (from notes) in one sentence.
- Optional quick **palindrome** or **chunking** idea from notes if time allows—otherwise homework.
- Summarize in four bullets (**exclusive stop**, **copy vs assign**, **step**, **mutation**).

---

## 5. Iterating through lists (18 minutes)

- Frame as **lists + loops**; show **iteration flowchart** from notes.
- **Live:** `for item in list`, **conditional inside loop**, **accumulator** (sum).
- **`enumerate()`**: index + value; **`start=1`** labeling; **in-place update by index** (`grades` example)—high value, do not skip.
- **`while` + index** when notes say manual control or early exit on condition; keep short.
- **`zip()`**: parallel names/scores; mention **shortest list wins**; optional **`dict(zip(keys,values))`** if cohort ready.
- **Critical warning:** **do not remove items while iterating** the same list—show **iterate copy** vs **new list** vs **index-based** fix from notes in under 90 seconds.
- **2D iteration** (rows, nested `for`, optional `break`/`continue`/`for-else` samples): demo one pattern or assign the rest.
- End with notes’ **summary bullets** on iteration.
- **Break timing:** after this section, take the **5–8 minute** pause per the rule at the top.

---

## 6. List comprehensions (17 minutes)

- Contrast **imperative** (append loop) vs **declarative** (comprehension); show **syntax diagram** from notes.
- **Pattern 1:** `[expr for item in iterable]`—**live:** squares, uppercasing strings.
- **Pattern 2:** **filter** with trailing `if`—evens, then **filter + map** in one line.
- **Pattern 3:** **conditional expression** (`x if cond else y`)—**filter drops** vs **transform keeps length**; one side-by-side prediction exercise.
- **Nested:** pick **one** of matrix build, **flatten**, or **Cartesian product**—avoid doing all three if time is tight.
- **`zip` / `enumerate`** inside comprehensions: one short example.
- **Best practices:** comprehension vs **regular loop** when logic gets gnarly—show the “too complex” anti-example from notes.
- **Quick reference** strip: 30-second silent skim in room.

---

## 7. Defining functions: `def`, naming, calls, composition (15 minutes)

- Motivate **reuse, DRY, abstraction**; show **function machine** figure from notes.
- **Syntax:** `def name():`, colon, indent, **call with `()`**.
- **Live:** `say_hello`, then **multi-statement** body; run twice to show reuse.
- **Why functions** list from notes—read titles only.
- **Naming:** show **good vs bad** examples on screen; one line on **verbs** and clarity.
- **Calling multiple times** (`display_menu`)—optional learner duplicate call in notebook.
- **Functions calling functions** (`show_welcome`): trace call stack on board once—keeps “composition” intuitive.
- **Key takeaways** as four bullets.

---

## 8. Function parameters (11 minutes)

- Motivate **parameter slots**; show **parameters diagram** from notes if available.
- **Parameter vs argument** vocabulary—non-negotiable clarity moment.
- **Live:** one parameter (`greet(name)`), then **multiple** (`add_numbers` or `introduce`).
- **Order matters**—run `introduce("Alice", 25)` vs swapped args to show the bug.
- **Key takeaways** five bullets skimmed.

---

## 9. Return values (12 minutes)

- Motivate **input → process → output**; `return` completes the machine; show **return figure** from notes.
- **Live:** `add(a, b)` returning sum; assign to variable; use in expression.
- **`return` vs `print`:** the **`bad_add` / `result is None`** pattern from notes—run it; this is a common exam trap.
- **Multiple `return` paths** in branches (`check_number`).
- Emphasize **`return` exits immediately**; optional mention no code after return in same block.
- **Key takeaways** five bullets.

---

## 10. Default parameters and the mutable-default pitfall (7 minutes)

- Motivate **optional arguments** and sensible defaults; show **defaults diagram** from notes briefly.
- **Live:** `greet(name, greeting="Hello")` and **keyword** `greet(..., greeting="Hey")`.
- **Multiple defaults** (`create_user`)—table-style output is fine as **read-along** if clock is tight.
- **Must-cover:** **mutable default anti-pattern** (`items=[]`) vs **`None` + fresh list** inside—run **bad** then **good** so the surprise is visible; this is the single most important minute of this block.
- Close with **Key Takeaways**; one closing question: *Where will you use `return` instead of `print` first?*

**Sum of numbered teaching segments:** 5 + 12 + 12 + 18 + 18 + 17 + 15 + 11 + 12 + 7 = **127 minutes** of teaching, plus **5–8 minutes** break ≈ **132–135 minutes** total session clock. Use spare time in **10** for Q&A or a second comprehension pattern.

---

### Timing flex

- **If behind:** Trim **4** (one slice-assignment demo only), **6** (nested comprehension as reading), or **7–9** (one `return` example, print-vs-return demo only).  
- **If ahead:** Add minutes to **5** (2D + `zip` dict), **6** (dict-of-users patterns), or **10** (learners predict mutable-default output before reveal).  
- **If session block is shorter than 2h15:** Drop optional sub-bullets in **2**, **4**, and **6** first; keep **9–10** (`return` vs `print` + mutable defaults) intact.
