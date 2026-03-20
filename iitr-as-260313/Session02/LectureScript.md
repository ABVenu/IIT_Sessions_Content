# Lecture Script: Logical Operators, Conditionals, Input & F-strings

**Session Duration:** 2 hours  
**Reference:** LectureNotes.md

---

## 1. Start with an Activity (5 minutes)

Present a quick scenario: *“You can go to the concert if you have a ticket **and** you’re over 18—or if you’re staff.”* Ask how that maps to **both** vs **either** vs **not**.

Have learners predict the output of a tiny snippet (no IDE yet): `True and False`, `True or False`, `not False`—then reveal answers. Tie to the **truth tables** and diagram in the lecture notes (AND/OR/NOT image).

---

## 2. Introduce Logical Operators (22 minutes)

Bridge: *“Comparisons give True/False. Real programs combine them—`and`, `or`, and `not` are how we glue conditions together.”*

Explain **`and`**: both sides must be true. Walk through the **full truth table** in the notes. Live demo: `can_drive = age >= 18 and has_license`; add a case where homework wasn’t submitted so `score >= 60 and submitted` is `False`.

Explain **`or`**: at least one true. Use the table in the notes. Demo weekend vs holiday, and “both false ⇒ false” for bad weather.

Explain **`not`**: reverses a boolean. Demo `not form_submitted` for “can still edit.”

**Combining operators:** Work through the **registration** example from the notes—adult **or** (minor **with** consent **and** id). Stress **parentheses** so intent is obvious: `(age >= 18) or (age < 18 and ...)`.

**Precedence:** Order is parentheses → **`not`** → **`and`** → **`or`**. Live demo `True or True and False` vs `(True or True) and False`. Show **`can_proceed`** from the notes with `has_permit` and `has_supervisor` defined—avoid “magic” undefined names.

**Short-circuit:** Explain left-to-right and “stop when decided.” Show that `expensive_check()` is skipped when the first part of `and` / `or` already fixes the result. Show the **safe** pattern: `username is not None and len(username) > 0`.

**Common patterns:** Chained range `18 <= age <= 65`; validation with `len` and `!=`; **`name or "Guest"`** for a default (falsy left-hand side).

**Common mistakes:** `&`/`|` vs `and`/`or`; messy mixed `and`/`or`; `(age >= 18) == True` instead of `age >= 18`.

Close with the **practice exercise** in the notes (`a and b or c` vs precedence)—walk answers or have pairs compare.

---

## 3. Introduce `if` Statements (20 minutes)

Bridge: *“We can compute booleans. Now we decide what runs: `if` is the basic branch.”*

Define **`if condition:`** — colon, **indented block**, runs only when the condition is true. Mention **conditional jumps** as the low-level idea (notes)—same program, different path by data.

Live demo: age 20 vs 15; show **no output** when the condition is false.

**Indentation:** Python uses indentation as structure—**4 spaces** convention. Show a line **outside** the `if` that always runs. Show **`pass`** for an empty block.

**Conditions:** Demo comparisons, **logical** operators inside `if`, and **boolean variables** (`if is_logged_in:`).

**Multiple independent `if`s:** Use **`score = 85`** from the notes—several messages can print. Contrast with `elif` *later* (“only one branch”).

**Real-world patterns:** Age + premium tiers with `int(input(...))` as in the notes. Optional: **password feedback** with several `if`s on `len(password)` (short / OK / strong)—emphasise that **more than one** message may apply.

**Common mistakes:** Missing colon; no indent; **`=` vs `==`**; dedented line that student thinks is inside `if`.

Run the **`x = 10`** trace exercise from the notes (`A`, `B`, `D`—not `C`).

---

## 4. Announce a Short Break (5 minutes)

Let learners try one snippet on their machine: combining two comparisons with `and`, or fixing an `if` missing a colon.

---

## 5. Introduce `elif` (14 minutes)

Bridge: *“Many outcomes aren’t just yes/no. We need a chain: first match wins.”*

**Problem:** Several bare `if`s re-check everything; for **grades**, the last assignment can overwrite the right answer—walk the **broken grade** example from the notes.

**Solution:** `if` / `elif` / … — only the **first true** branch runs. Demo grade ladder and **age categories** (teen vs adult ordering).

**Order matters:** Show **score = 95** with **`>= 60` before `>= 90`** — “Excellent” never runs. Rule: **specific before general**.

**Applications:** **BMI bands** from the notes; **traffic light** string → action (introduces `else` for unknown—preview next section).

**Practice:** **`points` / `tier`** “gold vs silver” pitfall from the notes—separate `if`s vs `elif` for exclusive tiers.

---

## 6. Introduce `else` (12 minutes)

Bridge: *“Sometimes we need a guaranteed answer when nothing else matched—that’s `else`.”*

**Syntax:** `else` has **no condition**; it is **last**; never place **`else` before `elif`** (SyntaxError). Show simple **can vote** vs **cannot**.

**Full chain:** `A`…`F` with **`else: grade = "F"`** from the notes.

**When to skip `else`:** It’s OK if silence is acceptable; contrast with UX where users need **invalid credentials** or default price **`0`** for under-5 (login + ticket pricing examples in the notes).

**Mistakes:** `else score < 60:`; wrong keyword order—show corrected **`if` / `elif` / `else`** chain from the notes.

---

## 7. Introduce Nested Conditionals (14 minutes)

Bridge: *“Sometimes the *next* question only matters if the first answer was yes—that’s nesting.”*

Define **nested `if`**: inner block runs only if outer is true. Demo **age + license** and **username then password** from the notes.

**Deeper example:** Score / submitted / on_time ladder from the notes—read as a **tree**.

**Nested vs `and`:** Show **equivalent** “can drive” with nested `if` vs single `if age >= 18 and has_license:`. Explain **when nesting helps**: different actions at each level; when **`and`** is enough**: one combined condition, one outcome.

**Application:** **Layered discount** (threshold → member → coupon) from the notes.

**Pitfalls:** **Too deep**—prefer `and`/`or`, helpers, or **early return** in functions; bad indentation on inner `if`.

---

## 8. Introduce `input()` (11 minutes)

Bridge: *“Static variables aren’t enough—programs should react to the user.”*

Explain **input → processing → output**; **`variable = input("prompt")`** pauses until Enter.

**Critical rule:** **`input` always returns a `str`**—even if the user types digits. Demo `type(...)` after reading age.

**Conversion:** `int(...)`, `float(...)`; pattern **`int(input("Age: "))`**. Mini **calculator** with two `float` inputs from the notes.

**Why strings first:** Safety and flexibility—explicit conversion is intentional (briefly: validation before convert in real apps).

Optional: Mention **batch vs interactive** history from the notes in one sentence—CLI and forms are still the same pipeline.

---

## 9. Introduce F-strings (11 minutes)

Bridge: *“We’re building strings for users. F-strings are the readable default in modern Python.”*

Mention the **evolution table** in the notes (`+`, `%`, `.format()`, **`f"..."`**)—don’t dwell; stress **readability**.

**Basics:** Prefix **`f`**, embed **`{name}`**, **`{age}`**.

**Expressions in braces:** `price * quantity`, **`name.upper()`**, **`age >= 18`**.

**Format specifiers:** `:.2f`, **`,`** for thousands, width/alignment (`:<`, `:^`)—match the **receipt** / **report** examples in the notes.

**Literals:** **`{{` / `}}`** when you need real braces; matching quotes inside `{...}`—as in the notes.

Quick **°C → °F** one-liner from the notes if time.

Contrast one line of **concatenation** vs **f-string**—point to “Zen” takeaway in notes.

---

## 10. Conclude with Reflection (8 minutes)

**Integrating demo:** Walk or live-code the **“Putting the session together”** example from the notes: read age, **`if` / `elif` / `else`** for group, logical **`can_vote`**, one **`print` with an f-string**.

Ask students to reflect briefly:

- When do you choose **several `if`s** vs **`if` / `elif`**?
- Why does **`input`** force **`int`** before arithmetic?
- Why is **`else`** written without a condition, and why must it be **last**?
- When is **nesting** better than **`and`**?

Point to **Key takeaways** per section, the **concept checklist**, **vocabulary**, **common errors** table, and **optional self-drills** in Lecture Notes.md for self-study.

---
