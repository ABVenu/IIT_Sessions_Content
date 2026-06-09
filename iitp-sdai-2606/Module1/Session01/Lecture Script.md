# Lecture Script: Introduction to Programming & Python Basics

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include **many** worked examples and practice programs. The **same** document is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set that fits the clock—enough to make the idea click; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 55–60 minutes** of session clock time (after the **data types** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and what programming really means (7 minutes)

- Greet; confirm everyone has a laptop/phone with a browser and can open [onecompiler.com](https://onecompiler.com/).
- State outcomes: understand what **programming** is, run your first **Python** program in the browser, use **variables** and **data types**, apply **operators**, and talk to the user with **input()** and **print()**.
- One-line definition: programming = step-by-step instructions a computer follows exactly—no guessing.
- Show the **programming-as-recipe** image from the notes; ask: *“What happens if you forget a step in a recipe?”* Cold-call 2 students.
- Quick poll: *“Name one app you used today that probably runs on code.”* (UPI, WhatsApp, train booking, Netflix—validate any answer.)
- **Check for thumbs up:** everyone can see Lecture Notes for Session 01.

**Bridge:** “You don’t need to install anything scary today—we’ll use Python in the browser, and here’s why that language fits beginners.”

---

## 2. Why Python and what OneCompiler is (7 minutes)

- One sentence each: **Python** = readable language for humans and computers; used in software, data science, and AI.
- Show the **why Python for beginners** image—highlight plain-English syntax and browser-first setup.
- Define **online compiler** in one line: write code in the browser, click Run, see output—like an online form, no install.
- Introduce **OneCompiler**: free, save work, share links with instructor—recommend **sign in** from day one.
- **Pair-share (1 min):** partner explains to each other why an online compiler helps on day one.

**Bridge:** “Let’s open OneCompiler together and run the most famous first program in coding history.”

---

## 3. OneCompiler walk-through and Hello, World! (14 minutes)

- Screen-share: open [onecompiler.com](https://onecompiler.com/) → select **Python** → point out **editor**, **Run**, **Save**, **Share**.
- Show the **OneCompiler workflow** image while you click through each step on screen.
- **Live / follow-along:** type and run Hello, World:

```python
# This is my very first Python program
print("Hello, World!")
```

- Narrate: `#` comments are for humans; `print()` shows text; Python runs **top to bottom**.
- Show the **Hello, World flow** image; deliberately type `Print` once to show **case-sensitive** error, then fix.
- Warn about **smart quotes** from WhatsApp/Word—type straight `"` from the keyboard.
- **Check for thumbs up:** everyone’s output shows `Hello, World!` (or their variant).

**Bridge:** “You’ve run code—now change it so it says something about *you*.”

---

## 4. Hello with your name — activity and beginner mistakes (7 minutes)

- **Quick activity (4 min):** students print **name** and **city** on two separate lines (see notes); circulate and spot-check Run + output.
- Screen-share the **common beginner mistakes** list—30 seconds each: forgot Run, didn’t Save, wrong `print` spelling, curly quotes.
- **Cold-call:** “What button makes Python actually execute your code?”
- Remind: **Save** and note where to find **Share** link for help later.

**Bridge:** “Fixed text on screen is nice—but programs get useful when they **remember** values. That’s variables.”

---

## 5. Variables — storing and changing information (12 minutes)

- Analogy: labelled dabba / kirana bag—**name** is the label, **value** is what’s inside.
- Show the **variables as labelled boxes** image; stress `=` means **assignment** (“is assigned to”), not maths equality.
- **Live / follow-along:** `age = 22`, `name = "Priya"`, `print(age)`, `print(name)`.
- On board: naming rules—no leading digit, case-sensitive, descriptive names, avoid `print` as a variable name.
- **Live / follow-along:** wallet `balance = 500`, then `balance = balance - 120`, `print(balance)` → 380.
- **Cold-call:** “Can a variable’s value change after you create it? Show me with `balance`.”

**Bridge:** “Create three variables about yourself, print them, then we’ll label *what kind* of data each box holds.”

---

## 6. Personal info card activity and data types (8 minutes)

- **Quick activity (3 min):** personal info card—`my_name`, `my_age`, `fav_subject`, three `print()` lines; circulate.
- One sentence: **data type** = what kind of value is stored (number, text, true/false).
- Flash the **core data types** table—`int`, `float`, `str`, `bool`—do not read every cell; ask class which type fits “exam passed: yes/no.”
- **Live / follow-along:** four variables + `type()` for each; show mistake `"85"` vs `85` for maths.
- Show the **data types overview** image.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break we’ll make Python **calculate**, **compare**, and **combine** conditions—then ask the user real questions.”

---

## 7. Arithmetic operators (11 minutes)

- Define **operator** in one line: symbol that performs an action on values (`+`, `-`, `*`, …).
- Flash the **arithmetic operators** table—focus on `+ - * /`; mention `//`, `%`, `**` briefly with one example each.
- **Live / follow-along:** `a = 20`, `b = 6`—run addition through exponent; ask class to predict `a % b` before Run.
- **Live / follow-along:** dinner bill split (`total_bill = 1500`, `num_friends = 3`, `share = total_bill / num_friends`).
- Show the **arithmetic operators** image; note `/` gives a decimal in Python 3.
- **Pair-share (1 min):** partner explains difference between `/` and `//`.

**Bridge:** “Arithmetic gives numbers—sometimes we only need to **check** whether something is true or false.”

---

## 8. Comparison operators (7 minutes)

- State rule: comparisons return **True** or **False** only—they do not change variables.
- Flash comparison table; **cold-call:** “What does `==` do? What about `=`?”
- **Live / follow-along:** `math_marks` vs `passing_marks`—run `>`, `==`, `>=` examples from notes.
- Emphasize **`=` vs `==`** on board—most common beginner bug before `if/else` next session.

**Bridge:** “Real rules often need **two** checks together—marks *and* attendance, or this *or* that.”

---

## 9. Logical and assignment operators (9 minutes)

- Flash logical table: `and` (both True), `or` (at least one), `not` (flip).
- **Live / follow-along:** scholarship eligibility (`marks >= 80` **and** `attendance >= 75`); change values to get `False`.
- Short demo: `out_of_range` with `or` for number outside 1–100.
- Flash **assignment operators**—focus on `+=` and `-=`; **live:** `score = 0`, `score += 10`, `score += 5`, `score -= 3`, `print(score)`.
- Show the **comparison and logical operators** image; mention parentheses for readability.

**Bridge:** “Let’s chain these into one real expression—then build programs that **listen** to the user.”

---

## 10. Expressions and pocket money calculator (7 minutes)

- Define **expression**: values + variables + operators → one result.
- **Live / follow-along:** GST example (`price`, `gst_rate`, `total` with parentheses)—recite order: parentheses, `**`, `* / // %`, `+ -`.
- **Quick activity (4 min):** pocket money calculator (₹2000 − books − food); circulate; cold-call one student for their `remaining` value.

**Bridge:** “So far values were fixed in code—real apps **ask** questions. That’s `input()` and `print()`.”

---

## 11. Input, output, and the percentage program (11 minutes)

- Analogy: railway counter—user speaks (input), clerk prints ticket (output).
- Show the **input/output flow** image.
- **Live / follow-along:** `name = input("Enter your name: ")`, `print("Hello,", name)`.
- Stress: `input()` always returns a **string**—demo `int()` conversion before maths; mention `"22" + 5` error vs `22 + 5`.
- **Live / follow-along:** `print()` with commas; introduce **f-string** (`f"Sneha scored {marks} marks"`).
- **Live / follow-along:** full percentage program (subject, marks obtained, total marks)—run with sample numbers; trace formula `(obtained / total) * 100`.
- **Check for thumbs up:** everyone sees a sensible percentage in output.

**Bridge:** “You have all the pieces—let’s assemble one slightly bigger program and talk about what to do when something breaks.”

---

## 12. Capstone practice, debugging, and close (7 minutes)

- **Guided capstone (4 min):** start **mini student report card** together—collect name + three subject marks, compute total and average, print formatted lines; students finish styling if time is tight.
- Point to **EMI calculator** activity in notes as homework if not done live.
- **Debugging (2 min):** read the **last line** of an error; check spelling, quotes, `type()`; use `print()` mid-program to inspect variables.
- Recite **Key Takeaways** from notes as a **five-bullet** closing strip (programming, OneCompiler, variables/types, operators, input/output + preview **conditionals** in Session 02).
- Assignments / lab pointer; remind students to **Save** and **Share** OneCompiler links when submitting work; thank-you.

**Sum of numbered teaching segments:** 7 + 7 + 14 + 7 + 12 + 8 + 11 + 7 + 9 + 7 + 11 + 7 = **107 minutes** of teaching, plus **5–8 minutes** break ≈ **112–115 minutes** total session clock—trim Q&A in block 12 or shorten block 7 if your slot is exactly 110 minutes.

---

### Timing flex

- **If behind:** Shorten **2** (skip extended OneCompiler feature tour), **7** (bill split only—skip `//` `%` `**` demos), or **9** (scholarship `and` only—skip `or`/`not` and assignment shortcuts). Keep **3** and **11**—first run and first `input()` program are non-negotiable.
- **If ahead:** Add **4 minutes** in **12** (full **EMI calculator** live) or **5 minutes** in **5** (extra variable naming cold-calls). Run a deliberate **smart-quote** or `Print` typo fix as a 2-minute debug clinic.
- **If sign-in slows the room:** Let students run Hello World as guests first; assign account creation before next session.
- **If `input()` is slow in a large room:** Demo percentage program with pre-set variables; say “swap in `input()` for homework.”
- **If students struggle with `=` vs `==`:** Pause in **8** for a **60-second** board drill—write three lines, class shouts “assign” or “compare.”
