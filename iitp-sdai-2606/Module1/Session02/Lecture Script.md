# Lecture Script: Operators & Conditional Statements

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include **many** worked examples and practice programs. The **same** document is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set that fits the clock—enough to make the idea click; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 50–55 minutes** of session clock time (after the **`elif`** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why programs need decisions (5 minutes)

- Greet; confirm everyone has **OneCompiler** (or IDE) open and can run a short Python program from Session 01.
- Recap in one line: last session they wrote straight-line programs—today programs **choose** different paths.
- State outcomes: **`if` / `elif` / `else`**, boolean conditions, logical operators inside conditions, nested checks, and the **STEP** method for thinking before coding.
- Show the **program decision-flow** image from the notes (railway platform / UPI / exam portal)—ask: *“Where have you seen an app say yes or no based on your input?”* Cold-call 2 students.
- **Check for thumbs up:** everyone can open Lecture Notes and see Session 02 images.

**Bridge:** “You already know comparisons from last time—let’s reconnect those before we write our first `if`.”

---

## 2. Quick recap: conditions and boolean values (10 minutes)

- One sentence each: **condition**, **boolean**, **True / False**.
- Flash the **comparison operators** table on screen for ~30 seconds—do not read every cell; ask students to name what `>=` means.
- Flash the **logical operators** table; live-evaluate `True and False`, `True or False`, `not True` in the REPL or a scratch cell.
- **Live / follow-along:** scholarship eligibility snippet (`marks >= 80` **and** `attendance >= 75`)—run with values that give `True`, then `False`.
- **Cold-call:** “What is the difference between `=` and `==`?”—pause for one answer before confirming.
- Show the **boolean conditions** diagram from the notes; highlight the `=` vs `==` warning.

**Bridge:** “Now that we can build a True/False check, let’s tell Python what to **do** when that check passes—that’s `if`.”

---

## 3. The `if` statement — run code only when True (12 minutes)

- Define `if` in plain English: “only do this when the check passes.”
- Show **basic syntax** on board: `if condition:` + indented block (4 spaces).
- Display the **`if` statement flow** image; trace: condition → colon → indented body → lines after always run.
- **Live / follow-along:** voting eligibility (`age = int(input(...))`, `if age >= 18:`)—run with 20 and 15 so the class sees message vs no message.
- Narrate **`int()`** before compare; mention **`TypeError`** if they forget (string vs number).
- **Quick activity — temperature check:** give students 3 minutes to type the hot-weather program (`temperature > 35`); circulate and spot-check indentation.
- **Pair-share (1 min):** partner explains why the warning did **not** print when they entered 30.

**Bridge:** “`if` handles the happy path—when the condition is false, we need an alternative. That’s `else`.”

---

## 4. The `else` statement — the otherwise branch (10 minutes)

- Define `else`: exactly **one** branch runs—never both, never neither.
- Show the **if/else branches** diagram (pass/fail and even/odd).
- **Live / follow-along:** pass or fail on `marks >= 40`—test 55 and 35; ask class to predict output before each run.
- **Live or student-led:** even/odd with `% 2`; cold-call: *“What does `number % 2` return for 7?”*
- **Check for thumbs up:** everyone’s pass/fail program prints exactly one of PASS or FAIL.

**Bridge:** “Many real problems have **more than two** outcomes—grades, bill slabs, ticket types. That’s where `elif` comes in.”

---

## 5. The `elif` statement — multiple outcomes in order (15 minutes)

- Define `elif`: checked **top to bottom**; **first True wins**; only **one** block runs.
- Write the **if / elif / else** skeleton on the board with comments for order.
- **Live / follow-along:** grade calculator—run marks **95**, **80**, and **35**; trace which conditions Python skips.
- **Common mistake demo (2 min):** briefly show wrong order (`>= 40` before `>= 90`) and ask why everyone gets Grade D—fix on screen.
- **Quick activity — electricity bill slab:** students type `units` program; circulate; verify `elif units <= 200` only makes sense after the first check failed.
- **Demo or read-along:** train ticket by age—one walkthrough (e.g. age 10 → CHILD, age 65 → SENIOR).
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break we’ll combine multiple checks in **one** condition using `and`, `or`, and `not`—then nest decisions inside each other.”

---

## 6. Combining logical operators inside conditions (12 minutes)

- State rule: `and` = both True; `or` = at least one True; `not` flips the value.
- **Live / follow-along:** scholarship program (`marks` and `attendance`)—same pattern as recap but now inside `if` / `else`.
- **Live / follow-along:** shop discount with `or` (amount > 1000 **or** membership `"yes"`)—test both triggers separately.
- Short demo: `not is_locked` login snippet—explain `not False` becomes True.
- **Cold-call:** “In the discount program, if amount is ₹800 and membership is `no`, which branch runs?”
- Remind: parentheses around comparisons in long conditions improve readability.

**Bridge:** “Sometimes the second check should run **only if** the first passed—that’s nesting, not a longer `elif` chain.”

---

## 7. Nested conditionals — decisions inside decisions (8 minutes)

- Define nested `if`: inner block runs only when outer condition is True (stadium ticket + VIP pass analogy from notes).
- **Live / follow-along:** username/password login—wrong username vs wrong password vs success; run three test cases.
- On board: trace indentation levels for outer `if`, inner `if`, inner `else`, outer `else`.
- **One-liner tip:** if nesting goes past 2–3 levels, refactor with `and` / `or` or `elif` for readability.

**Bridge:** “Before more practice, let’s name the bugs that trip up every beginner class—then use STEP to plan the next program.”

---

## 8. Common mistakes and the STEP method (10 minutes)

- Screen-share the **common mistakes** table—spend 30 seconds each on `=` vs `==`, missing colon, wrong indentation, string vs number, wrong `elif` order.
- Show `pass` as a placeholder in an empty block—replace with real logic in homework.
- Teach **STEP** (State, inputs, conditions/outcomes, Python)—cinema ticket example on board.
- **Guided activity (5 min):** shop discount (10% off above ₹500)—students write STEP in chat or notebook **first**, then code; circulate.
- **Pair-share:** partner reads their “E — conditions and outcomes” line aloud.

**Bridge:** “You’ve seen the patterns—let’s apply them on slightly bigger problems and finish with how to debug when output surprises you.”

---

## 9. Guided practice — conditional exercises (15 minutes)

- Set expectation: type code yourself in OneCompiler; test **boundary** values.
- **Exercise 1 (5 min):** positive / negative / zero—live-code together or staggered release; test `5`, `-3`, `0`.
- **Exercise 2 (7 min):** simple ATM withdrawal—emphasize checking failure cases **first** (`> balance`, `<= 0`), then success branch; circulate and fix indentation.
- **Optional if ahead (3 min):** skim leap year checker from notes—only stress **order** (`% 400`, then `% 100`, then `% 4`); assign full version as homework.
- **Cold-call:** “Why do we check insufficient balance before checking `<= 0`?” (accept either order discussion; note clarity of error messages.)

**Bridge:** “When output is wrong, don’t guess—let’s use two quick debug habits, then wrap with what comes next in the course.”

---

## 10. Debugging tips, takeaways, and close (7 minutes)

- **Live demo:** add `print("Condition result:", marks >= 40)` before `if`—delete the line after fixing.
- Mention `print(type(variable))` and boundary tests (39, 40, 90 for grade programs).
- Recite **Key Takeaways** from notes as a **five-bullet** closing strip (conditionals, operators, indentation, STEP, preview **loops**).
- Point to **Exercise 3–4** and complete student result program in notes for self-study.
- Assignments / lab pointer; thank-you; where to ask questions.

**Sum of numbered teaching segments:** 5 + 10 + 12 + 10 + 15 + 12 + 8 + 10 + 15 + 7 = **104 minutes** of teaching, plus **5–8 minutes** break ≈ **109–112 minutes** total session clock—trim Q&A in block 10 if your slot is exactly 110 minutes.

---

### Timing flex

- **If behind:** Shorten **2** (skip extra `not` REPL demos), **5** (grade calculator only—skip train ticket), or **9** (do Exercise 1 only; ATM as homework). Keep **6** (logical operators)—it underpins later sessions.
- **If ahead:** Add **5–8 minutes** in **9** (full **student result** program live, or leap year trace on board) or run a **2-minute** debug clinic on a deliberate indentation bug.
- **If `input()` is slow in a large room:** Pre-set variables (`age = 20`) for demos; say “in your homework, swap in `input()`.”
- **If students struggle with indentation:** Pause in **3** or **4** for a **60-second** “everyone align colons and bodies” reset—show IDE “show whitespace” if available.
