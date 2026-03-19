# Lecture Script: Introduction to Programming, Python Basics & Development Env Setup

**Session Duration:** 2 hours  
**Reference:** lectureNotes.md

---

## 1. Start with an Activity (5 minutes)

Present a scenario: a student wants to run a simple program that prints "Hello" and adds two numbers. They try using Notepad and double-clicking the file—nothing happens.

Ask: Why doesn't it work? What do we need to run code?

Discuss why a plain text editor and double-clicking are not enough—computers need an interpreter (Python) and a proper way to execute scripts (terminal).

Present a second scenario: student saves code as `document.txt` or `myfile` without `.py` extension; Python cannot run it.

Highlight the need for proper tools: a code editor, Python installed, and a way to execute scripts.

---

## 2. Introduce the Development Environment (10 minutes)

Define the development environment as the set of tools needed to write and run code professionally.

Introduce **VS Code** as a free code editor—like Word, but for code. Mention: syntax highlighting, Auto Save, "Open with Code" for folders.

Introduce **Python** as the programming language. Emphasise: download from python.org, **check "Add Python to PATH"** during installation—otherwise the terminal will not find Python.

Run `python3 --version` live to verify installation. If it fails, explain that PATH was likely skipped; re-run installer with that option.

---

## 3. Explain the Terminal and How to Run Code (15 minutes)

Explain that the **terminal** is a text-based interface where you type commands instead of clicking.

Describe what happens when you run `python3 index.py`: the terminal finds Python, loads the file, runs it line by line, and shows the output.

Use the analogy: *"The terminal is like a conversation with your computer—you type, it responds."*

Live demo:

- Create `index.py` with `print("Hello, World!")`
- Open terminal in VS Code (Terminal → New Terminal or Ctrl+` / Cmd+`)
- Run `python3 index.py`
- Show the output

Highlight the "No such file or directory" error: the terminal must be in the same folder as the `.py` file. Use `cd` to navigate. Right-click folder → "Open with Code" ensures the terminal starts in the right place.

---

## 4. Give an Analogy and Small Demo (5 minutes)

Use the **locker analogy** for understanding the terminal and file location:

- Imagine the terminal is "standing" in a hallway. The hallway is a folder.
- When you type `python3 index.py`, it looks for `index.py` in the folder where it is standing.
- If the file is in another room (another folder), it cannot find it. You must "walk" there with `cd`.

Run the wrong-folder scenario live: run `python3 index.py` from the wrong folder, show the error, then `cd` to the correct folder and run again. Connect this to the importance of knowing where the terminal is.

---

## 5. Introduce Syntax (10 minutes)

Bridge: *"Now that we can run code, we need to follow its rules. Code has grammar—break it and Python stops."*

Define **syntax** as the set of rules for writing code. The computer does not guess intent; it follows rules exactly.

List key rules: quotes around text, variable name on the left of `=`, indentation matters in Python, case-sensitive (e.g. `print` ≠ `Print`).

Live demo: show good vs bad examples—`name = "Alice"` works, `name = Alice` gives error. Show assignment direction: `score = 100` is correct, `100 = score` is wrong. Keep it brief.

---

## 6. Introduce Variables (15 minutes)

Bridge: *"Variables give programs memory. Without them, we couldn't store or reuse data."*

Use the **locker analogy**: the locker number is the variable name; the contents are the value. You can change what’s inside anytime.

Explain `=` as assignment, not equality—variable on the left, value on the right. Read `score = 100` as "score is assigned 100."

Introduce **snake_case**: Python uses underscores between words, e.g. `student_name`, `total_score`.

Live demo: create variables, reassign them, use them in calculations (`total = price * quantity`), show shorthand (`score += 50`). Mention the common mistake: using a variable before creating it.

---

## 7. Announce a Short Break (5 minutes)

Allow learners to absorb the concepts: setup, terminal, syntax, variables. Encourage them to try running a simple script on their machines if setup is complete.

---

## 8. Introduce Data Types (20 minutes)

Bridge: *"We can store data. But what kind? Numbers and text behave differently—you multiply prices, you join names."*

Use the **shopping app analogy**: product name is text, price has decimals, quantity is a whole number. If everything were one type, the computer wouldn't know whether `"19"` means the number 19 or the text "19"—and `"19" * 3` would repeat "19" three times instead of giving 57.

Introduce the four main types: `int` (whole numbers), `float` (decimals), `str` (text in quotes), `bool` (True/False).

Explain why int and float are separate: integers for counting (3 apples), floats for measurements (19.99 rupees, 5.5 feet).

Live demo: create one variable of each type, show `type()`. Demonstrate mixing error: `"Age: " + 25` fails; fix with `str(25)`. Show int + float → float.

---

## 9. Introduce Arithmetic Operators (15 minutes)

Bridge: *"We store data. Now we operate on it. Every app uses math—scores, prices, totals."*

List the seven operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`.

Emphasise the difference between `/` and `//`: `/` always returns a float (keeps decimals); `//` returns an integer (drops the decimal part). Use the **bill-splitting analogy**: 100 rupees among 3 people—33 each with `//`, remainder 1 with `%`.

For modulo (`%`): mention checking even/odd (remainder 0 = even, remainder 1 = odd).

Live demo: show `10 / 3` vs `10 // 3`, `10 % 3`, and a short calculation using variables.

---

## 10. Introduce Operator Precedence (10 minutes)

Bridge: *"We combine operations. But in `2 + 3 * 4`, what happens first—addition or multiplication? Without rules it's ambiguous."*

Introduce **PEMDAS**: Parentheses → Exponents → Multiply/Divide → Add/Subtract. Use the **traffic rules analogy**: everyone follows the same order, or we get chaos.

Live demo: run `2 + 3 * 4` (result 14, not 20). Show `(2 + 3) * 4` (result 20). When unsure, use parentheses to make intent clear.

---

## 11. Introduce Comparison Operators (15 minutes)

Bridge: *"Programs don't only calculate—they decide. ATMs check balance, games check health. Comparisons drive those decisions."*

List the six operators: `==`, `!=`, `>`, `<`, `>=`, `<=`. All return True or False.

Use the **bouncer analogy**: like checking age at a club—is it >= 21? Yes or no.

Explain that comparison results can be stored: `is_adult = age >= 18` gives a boolean.

Stress `==` for comparison vs `=` for assignment. Live demo: show that `if age = 18` causes SyntaxError; `if age == 18` is correct.

---

## 12. Conclude with Reflection (5 minutes)

Run the practice exercise from the lecture notes together: `score`, `bonus`, `total`, and `print("Passing?", total >= 60)`.

Ask students to reflect briefly on:

- How they would fix "No such file or directory" if it happens
- How they would avoid mixing strings and numbers
- The difference between `=` and `==` and when to use each
- Why `2 + 3 * 4` gives 14 instead of 20

Summarise common mistakes from the notes: wrong folder, `=` vs `==`, unquoted text, mixing types. Point to Key Takeaways and Quick Reference for self-study.
