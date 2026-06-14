# Lecture Script: DSA: Lists & Strings – Built-in Functions

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include **many** worked examples and practice programs. The **same** document is **shared with students** so they can read, rerun, and consolidate at their own pace. This script does **not** require covering every example in class. For each topic, choose a **small, well-chosen** set that fits the clock—enough to make the idea click; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 55–60 minutes** of session clock time (after the **list slicing** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why programs need lists and strings (5 minutes)

- Greet; confirm everyone has **OneCompiler** (or IDE) open and can run a short program with **`for` loops** from Session 03.
- Recap in one line: last session they **repeated** actions with loops—today they store **many values together** in **lists** and work with **text** as **strings**.
- State outcomes: create and change **lists**, **index** and **slice** lists and strings, format output with **f-strings**, and use **`len()`**, **`sorted()`**, **`min()`**, **`max()`**, **`sum()`**.
- Swiggy cart / WhatsApp status analogy from notes—ask: *“Where have you seen an app show a list of items or a line of text?”* Cold-call 2 students.
- **Check for thumbs up:** everyone can open Lecture Notes for Session 04.

**Bridge:** “One variable can hold many values in order—that’s a **list**. Let’s see how they differ from the single variables you used before.”

---

## 2. Lists — big picture and creating lists (10 minutes)

- One sentence each: **list** = ordered, **mutable** collection in `[ ]`; **string** = ordered, **immutable** text in `' '` or `" "`.
- Screen-share the **list vs single variable** table—order matters, lists can grow and shrink.
- **Live / follow-along:** create `fruits`, `marks`, and `mixed` lists from notes—print each; narrate comma separation and square brackets.
- **Live / follow-along:** empty `daily_tasks = []`, then three **`append`** calls—show list growing.
- **Common mistake (1 min):** show `( )` vs `[ ]`—parentheses make a tuple, not a list.
- **Cold-call:** “Why is an empty list `[]` useful before we know all the items?”

**Bridge:** “Creating a list is step one—next we **change** it with methods: add, remove, and sort.”

---

## 3. Essential list methods — `append`, `pop`, and `sort` (12 minutes)

- Define **list method**: action called with dot notation—`my_list.append(x)`.
- Train-queue analogy: **`append`** joins at back, **`pop`** leaves, **`sort`** rearranges.
- **Live / follow-along:** cricket team—`append("Jadeja")`, `append("Shami")`; print full list.
- **Live / follow-along:** `snacks.pop()` (last item) then `cities.pop(1)` (index 1)—print removed value and updated list.
- **Live / follow-along:** `marks.sort()`—show list changed in place; mention `reverse=True` for descending.
- Flash the **methods table** on screen; **common mistake demo:** mixing numbers and strings then calling `sort()` → `TypeError`.
- **Cold-call:** “Does `pop()` need an index, or is it optional?”

**Bridge:** “You can change the whole list—now let’s grab **one item** by its seat number: **indexing**.”

---

## 4. Quick activity — build and update a shopping list (8 minutes)

- Students type the **groceries** program from notes: empty list, four **`append`** calls, one **`pop`**, print before/after and **`len(groceries)`**.
- Circulate; spot-check that **`pop()`** removed **Bread** (last item) and length is 3.
- **Pair-share (1 min):** partner explains difference between **`append`** and **`pop`** in one sentence.
- **Check for thumbs up:** output shows list before pop, after pop, and item count.

**Bridge:** “Methods work on the whole list; **indexing** picks out a single item—counting starts at **zero**.”

---

## 5. Accessing list elements — indexing (10 minutes)

- Define **indexing**: position number starting at **0**; **negative** index **-1** = last item.
- Draw the **fruits index table** on board (0…3 and -4…-1).
- **Live / follow-along:** `fruits[0]`, `fruits[-1]`, `fruits[-2]`—predict before each run.
- **Live / follow-along:** change `marks[2] = 95`—stress lists are **mutable** (unlike strings later).
- **Common mistake demo (1 min):** `fruits[4]` on a 4-item list → **`IndexError`**; valid last index is **`len(list) - 1`**.
- **Cold-call:** “For a list of length 5, what is the last valid positive index?”

**Bridge:** “One index gives one item; **slicing** gives a **portion**—like taking two idlis from a plate of five.”

---

## 6. List slicing — getting a portion of a list (10 minutes)

- Define **slicing**: `list[start:stop:step]`—`start` inclusive, **`stop` exclusive**.
- **Live / follow-along:** seven-day `temps` list—run `temps[2:5]`, `temps[:3]`, `temps[-2:]`, `temps[::2]`, `temps[::-1]`; predict slice length before each run.
- Emphasize: slicing creates a **new list**; the **original is unchanged**.
- **Guided activity (3 min):** temperature quick activity from notes—first three days, last two, Thursday by index; circulate.
- **Common mistake:** `[0:3]` gives **3 items** (indices 0, 1, 2)—not index 3.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break, the same **indexing and slicing** rules work on **strings**—plus ways to join and format text.”

---

## 7. Strings — indexing, slicing, and concatenation (12 minutes)

- Define **string**: immutable sequence of characters; single or double quotes.
- **Live / follow-along:** `name = "Priya"`—`name[0]`, `name[-1]`; `word[1:4]` and `word[::-1]` on `"PYTHON"`.
- **Live / follow-along:** concatenation—`first_name + " " + last_name`; repetition—`"-" * 30`.
- Try **`name[0] = "p"`** (or explain)—**`TypeError`** because strings are **immutable**.
- Mention **`for char in word:`** visits each character—connect to Session 03 loops.
- **Common mistake:** `"Age: " + 25` → use **`str(25)`** or f-strings next.
- **Check for thumbs up:** everyone’s reversed `"PYTHON"` prints `NOHTYP`.

**Bridge:** “Concatenation works, but **`f-strings`** are cleaner when variables go inside sentences—that’s how real apps print receipts and reports.”

---

## 8. f-String formatting and personalised greeting (10 minutes)

- Define **f-string**: prefix **`f`**, placeholders **`{variable}`** evaluated at runtime.
- **Live / follow-along:** Deepa marks message; notebook bill with `{quantity * price}` inside braces.
- Show **`{percentage:.2f}`** for two decimal places.
- **Common mistake demo:** print without **`f`** prefix—`{name}` appears literally.
- **Quick activity (4 min):** personalised greeting (name, city, hobby, `years_left` calculation)—students type and share one line in chat.
- **Cold-call:** “Can you put `30 - 22` inside the curly braces?”

**Bridge:** “You can loop to process data—but Python also gives **built-in functions** that answer common questions in one line.”

---

## 9. Built-in functions — `len()`, `sorted()`, `min()`, `max()`, `sum()` (12 minutes)

- Define **built-in function**: ready-made tool, no import—`len(x)`, not `x.len()`.
- **Live / follow-along:** `len(fruits)`, `len(word)`; last item via `fruits[len(fruits) - 1]` or `fruits[-1]`.
- **Side-by-side demo:** `sorted(marks)` vs `marks.sort()`—original unchanged vs changed in place; note **`sort()` returns `None`**.
- **Live / follow-along:** `min`, `max`, `sum` on marks; average with f-string `{average:.2f}`.
- Flash the **function vs method** table—`sorted()` vs `sort()`, changes original or not.
- **Cold-call:** “Why does `sum()` fail on a list of strings like `['a','b']`?”

**Bridge:** “Lists, methods, indexing, strings, f-strings, and built-ins—let’s wire them together in one **class report** program.”

---

## 10. Putting it together — class report program (10 minutes)

- **Live / follow-along:** `students` and `marks` lists—`append` Karan and 64; compute total, average, top score.
- Trace **`marks.index(top_score)`** → matching **`students[top_index]`**—same order in both lists.
- Print report with **f-strings**; show **`sorted(marks)`** without destroying original.
- **Pair-share (1 min):** partner explains why names and marks lists must stay **in sync**.
- Warn: adding to one list without the other breaks the report logic.

**Bridge:** “You’ve seen the full toolkit—two short exercises, then debug habits and what comes next in the course.”

---

## 11. Guided practice, debugging, and close (10 minutes)

- Set expectation: type in OneCompiler; full **Exercise 1–3** in notes for homework if time is tight.
- **Exercise 1 (4 min):** analyse marks list—`sum`, average, `min`, `max`, `sorted` with f-strings; circulate.
- **Exercise 2 (3 min):** string `"AGENTIC"`—first, last, middle slice, reverse; cold-call predicted output for `[2:5]`.
- **Optional if ahead:** Exercise 3 formatted bill—one live trace.
- **Debug habits (1 min):** print list after each change; valid indices `0` to `len-1`; slice stop is exclusive; trace on 3-item lists first.
- Recite **Key Takeaways** from notes as a **five-bullet** closing strip (lists + methods, indexing/slicing, strings + f-strings, built-ins, preview **functions and dictionaries**).
- Assignments / lab pointer; thank-you; where to ask questions.

**Sum of numbered teaching segments:** 5 + 10 + 12 + 8 + 10 + 10 + 12 + 10 + 12 + 10 + 10 = **109 minutes** of teaching, plus **5–8 minutes** break ≈ **114–117 minutes** total session clock—trim Q&A in block 11 or shorten block 10 if your slot is exactly 110 minutes.

---

### Timing flex

- **If behind:** Shorten **2** (skip `mixed` list demo), **4** (instructor demos shopping list—students copy after break), **7** (skip `"-" * 30` repetition), or **11** (Exercise 1 only; string exercises as homework). Keep **5** (index 0 and `IndexError`) and **6** (stop exclusive)—these prevent the most common bugs.
- **If ahead:** Add **5–8 minutes** in **10** (students extend class report with **`min`** and lowest student name using **`index`**), or run **Exercise 3** live in **11**.
- **If students confuse index and length:** Pause in **5** for a **60-second** board drill—list of 4 items, indices 0–3, last index = `len - 1`.
- **If `sorted()` vs `sort()` is unclear:** Repeat the side-by-side demo in **9** with `print(marks)` immediately after each call.
- **If f-strings stall:** Fall back to **`print("Name:", name)`** for one demo, then retry with **`f"Name: {name}"`** so the benefit is visible.
