# Lecture Script: Loops & Iterations in Python

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include **many** worked examples and practice programs. The **same** document is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set that fits the clock—enough to make the idea click; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 55–60 minutes** of session clock time (after the **`range()`** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why programs need to repeat (5 minutes)

- Greet; confirm everyone has **OneCompiler** (or IDE) open and can run a short Python program from Sessions 01–02.
- Recap in one line: last session they wrote programs that **decide**—today programs **repeat** without copy-pasting the same line ten times.
- State outcomes: **`while`** and **`for`** loops, **`range()`**, **`break`** / **`continue`**, choosing the right loop, and the **LOOP** method for problem solving.
- Show the **loops big picture** image from the notes (temple prasad queue, UPI retries, exam results)—ask: *“Where have you seen an app do the same action again and again?”* Cold-call 2 students.
- **Check for thumbs up:** everyone can open Lecture Notes and see Session 03 images.

**Bridge:** “Conditionals decide **what** to do; loops decide **how many times**—let’s see the two main loop types before we write code.”

---

## 2. Understanding loops — the big picture (7 minutes)

- One sentence: a **loop** runs a block of code **repeatedly** until a condition fails or every item is processed.
- Screen-share the **while vs for** comparison table—`while` = repeat **until** something changes; `for` = repeat **for each** item or count.
- Introduce **`break`** (stop entirely) and **`continue`** (skip this round only) in one line each—full examples come later.
- Temple prasad / roll-call analogy from notes; ask class which loop type fits “for each person in the queue.”
- **Cold-call:** “If you don’t know how many password tries the user will need, which loop type sounds right—`while` or `for`?”

**Bridge:** “When the exit depends on a changing condition, we start with **`while`**—let’s write one and watch the condition check each round.”

---

## 3. The `while` loop — syntax and count 1 to 5 (12 minutes)

- Define `while` in plain English: “keep going **while** the check is True.”
- Show **basic syntax** on board: `while condition:` + indented body; stress the **colon** and **4-space indent**.
- Display the **while loop diagram** from the notes; trace condition → body → condition again.
- **Live / follow-along:** count 1 to 5 (`count = 1`, `while count <= 5:`, `print(count)`, `count = count + 1`)—narrate each round aloud.
- **Common mistake demo (2 min):** comment out `count = count + 1` and run—show infinite `1` prints; stop quickly and restore the update line.
- Emphasize **critical rule:** something inside must change so the condition can become `False`.
- **Pair-share (1 min):** partner explains what happens when `count` becomes 6.

**Bridge:** “`while` is perfect when you repeat **until input is valid**—password checks and savings goals work the same way.”

---

## 4. `while` in practice — password validation and savings goal (10 minutes)

- **Live / follow-along:** password validation (`password = ""`, `while len(password) < 8:`)—run with a short then valid password; explain `len()`.
- **Quick activity (4 min):** savings goal tracker (₹500/month until ₹5000)—students type the program from notes; circulate and verify `balance` updates each round.
- **Check for thumbs up:** savings program prints balance after each month and stops at or above ₹5000.
- **Cold-call:** “Why do we start `password` as an empty string instead of skipping the loop?”

**Bridge:** “When you already **have a list** or a fixed count, **`for`** is usually cleaner—Python visits each item for you.”

---

## 5. The `for` loop — lists and attendance counter (12 minutes)

- Define `for` in plain English: “do this **once for every** item in the sequence.”
- Show syntax: `for item in sequence:` + indented body; note `item` is just a variable name.
- **Live / follow-along:** print each fruit in `["mango", "banana", "apple"]`—trace `fruit` changing each round.
- **Common mistake (1 min):** show `print(fruit)` **outside** the loop—only last value prints; move it inside.
- **Guided activity (5 min):** class attendance counter—combine **`for`** with **`if`** from Session 02; circulate; expected output `Total present: 3`.
- **Cold-call:** “Which line runs more times—the `for` line or the `if` line inside it?”

**Bridge:** “To count 1 to 10 or print table rows, Python gives us **`range()`**—no manual counter for simple counting.”

---

## 6. The `range()` function and multiplication table (10 minutes)

- Explain `range()` in plain English: numbers one by one, like a token counter.
- Flash the **three forms** table (`range(stop)`, `range(start, stop)`, `range(start, stop, step)`)—stress **stops before** the second number.
- **Live / follow-along:** print numbers 1 to 5 with `for num in range(1, 6):`.
- Show the **for loop and range** diagram from notes; highlight off-by-one mistake (`range(1, 5)` vs `range(1, 6)`).
- **Live / follow-along:** multiplication table for 7—run full table; ask students to change `number = 7` to another value as homework.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break we’ll pick **`for` vs `while`** for real situations, then learn to **stop early** or **skip one round** with `break` and `continue`.”

---

## 7. Choosing the right loop — `for` vs `while` (7 minutes)

- Screen-share the **decision table** from notes (table rows → `for`; password until valid → `while`; menu until quit → `while True` + `break`).
- **Live side-by-side:** same output 0–4 with `for i in range(5)` vs `while count < 5`—ask which feels shorter for counting.
- Thali menu (`for`) vs cooker whistle (`while`) analogy—cold-call one match from the table.
- **Check for thumbs up:** everyone can state one problem for `for` and one for `while` in chat or aloud.

**Bridge:** “Sometimes you find what you need **before** the loop finishes—that’s when **`break`** exits immediately.”

---

## 8. The `break` statement — stop the loop early (10 minutes)

- Define `break`: exits the **innermost** loop right now; execution continues **after** the loop.
- **Live / follow-along:** menu with `while True` + `break` on `"quit"`—type `help`, then `quit`; trace jump to `print("Goodbye!")`.
- Name the pattern: **`while True` + `break`** for menus and games.
- **Live / follow-along:** find target `12` in a list—show that without `break` Python keeps checking; with `break` it stops at first match.
- **Cold-call:** “After `break`, does the line `print('Running command:', command)` still run for `quit`?”

**Bridge:** “`break` ends the whole loop; **`continue`** skips **only this round** and keeps going—useful for filtering.”

---

## 9. The `continue` statement — skip one round (8 minutes)

- Define `continue`: skip rest of **this** iteration; loop goes to **next** item.
- Show **break vs continue** table from notes (stop search vs skip one bad apple).
- **Live / follow-along:** print odd numbers 1–10 with `if num % 2 == 0: continue`.
- Brief warning: in **`while`** loops, update counters **before** `continue` or risk infinite loops—mention only; demo if time allows.
- **Read-along or live:** grade every student in `marks_list`—loop repeats, `if`/`else` decides pass/fail (no `continue` required, but shows loop + conditional pattern).

**Bridge:** “You’ve seen repeat, stop, and skip—now let’s use loops to **automate** totals and solve problems step by step.”

---

## 10. Automation, the LOOP method, and average marks (10 minutes)

- Show **shopping bill total** accumulator pattern: `total_bill = 0`, add each `price` in the loop, print **after** the loop.
- Name the pattern: **accumulator**—start at 0, build inside, use result outside.
- Teach **LOOP** method on board: **L**ist goal, **O**bserve repetition, **O**utline loop, **P**rocess inside loop.
- **Guided activity (5 min):** average marks calculator—students write loop for `total`, then `average = total / len(marks)` **outside**; circulate.
- **Common mistake demo:** move `average = total / count` **inside** the loop briefly—ask why that is wrong.
- Display the **LOOP method** and **accumulator** diagrams from notes.

**Bridge:** “You’ve got the patterns—let’s practice two short exercises, then wrap with debug habits and what comes next.”

---

## 11. Guided practice, debugging, and close (10 minutes)

- Set expectation: type in OneCompiler; test boundary values; full set of exercises stays in notes for homework.
- **Exercise 1 (4 min):** sum of first N natural numbers—live-code or staggered release; test `n = 5`.
- **Exercise 2 (4 min):** valid PIN with `while pin != "1234"`—emphasize comparing as **text**; circulate.
- **Optional if ahead:** skim Exercise 3 (first failing mark with `break`)—one trace on board; assign full version as homework.
- **Debug habits (1 min):** print loop variable inside loop; check off-by-one in `range()`; verify `while` condition variable updates.
- Recite **Key Takeaways** from notes as a **five-bullet** closing strip (`while`, `for` + `range`, `break`/`continue`, accumulator, preview **lists and functions**).
- Assignments / lab pointer; thank-you; where to ask questions.

**Sum of numbered teaching segments:** 5 + 7 + 12 + 10 + 12 + 10 + 7 + 10 + 8 + 10 + 10 = **101 minutes** of teaching, plus **5–8 minutes** break ≈ **106–109 minutes** total session clock—use extra minutes for Q&A in block 11 if your slot is exactly 110 minutes.

---

### Timing flex

- **If behind:** Shorten **2** (skip extended analogies), **4** (password live only—savings as homework), **9** (odd-numbers demo only—skip grade list), or **11** (Exercise 1 only; PIN as homework). Keep **3** (infinite-loop warning) and **6** (`range()` off-by-one)—these prevent the most common bugs.
- **If ahead:** Add **5–8 minutes** in **11** (full Exercise 3 with `break`, or live **grade list** with pass/fail), or run a **2-minute** infinite-loop fix clinic on a student’s `while` program.
- **If `input()` is slow in a large room:** Pre-set variables for demos (`password = "abc12345"` after one manual run); say “in homework, use `input()`.”
- **If students struggle with indentation:** Pause in **3** or **5** for a **60-second** “align colons and bodies” reset—show IDE “show whitespace” if available.
- **If `range()` confuses:** Spend an extra 3 minutes in **6** with `range(5)` vs `range(1, 6)` on the board before the multiplication table.
