# Lecture Script: Masterclass: Algorithmic Thinking in JavaScript

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**How to use this file:** This document is for **timing and facilitation only**. It is not a transcript or textbook. Use the numbered blocks to pace the room, manage screen-shares, check student screens, and trigger participation. Definitions, analogies, full code, tables, and activities live in **Lecture Notes.md** — share that with students and skim headings aloud rather than reading every bullet.

**Break rule:** After **roughly 55–65 minutes** of session clock time (after the **frequency-counter** segment), take **one** pause of **5–8 minutes**, then continue. Do **not** list the break as a numbered block.

---

## 1. Welcome, Setup, and Session Arc (5 minutes)

- Welcome the cohort; frame this as a **thinking masterclass** — not new JavaScript syntax today, but **how to decide what to type** before opening One Compiler.
- Recap in one line: in previous sessions they learned **variables**, **conditionals**, **loops**, **arrays**, **strings**, **objects**, and **functions**.
- State outcomes in plain language: four boxes before code; **frequency counter** with objects; **two pointers** on arrays/strings; **O(1)**, **O(n)**, **O(n²)** in plain words; an **eight-step checklist** before every new problem.
- **Room action:** Ask everyone to open **[One Compiler — JavaScript](https://onecompiler.com/javascript)** in one tab and **Lecture Notes** for this masterclass in another. Confirm they can see the four session images.
- **Engagement — cold-call (2 students):** "When a new problem appears, do you usually plan first or start typing `let` immediately?"
- **Engagement — thumbs up:** One Compiler and Lecture Notes are both open.

**Bridge sentence:** "Good — today we slow down at the notebook before we speed up in the editor."

---

## 2. Why Pause Before You Type (8 minutes)

- One line: they already know loops and functions; today's skill is **algorithmic thinking** — writing the recipe before lighting the stove.
- Chai recipe analogy from notes: skip "strain" and the output is wrong even with correct ingredients.
- Patna City College exam-cell story: clerk counting passes without knowing pass mark or absentee rules → messy count. Same mistake when coding before naming rules.
- **Common doubt (30 sec):** "If I know loops, why plan?" — A loop is a tool; the plan picks **which** tool, **how many** passes, and what to do when the list is empty.
- **Engagement — chat poll:** "Which fails more often on small data but breaks on large data — missing edge cases or wrong variable name?" Reveal: missing edge cases is the bigger pattern today.
- **Check for understanding (30 sec):** "Is algorithmic thinking a new keyword?" (No — it is a habit.)

**Bridge sentence:** "That habit starts with four boxes on paper — input, steps, output, and edge cases."

---

## 3. Break the Problem into Four Boxes (15 minutes)

- Screen-share the **four boxes** image (`sessionmc1-01-four-boxes-plan-before-code.png`).
- Walk the **pass-count** example from notes at headline level:
  - **Input:** array of marks + pass mark `40` (inclusive)
  - **Output:** number `3` for sample `[35, 67, 40, 88, 12]`
  - **Steps:** counter at 0 → walk list → if `>= 40` add 1 → return counter
  - **Edge cases:** flash the table — empty list, all failed, exact pass mark, single fail
- Stress **common error:** `>` instead of `>=` for pass mark.
- Thali / IRCTC analogies in one sentence each — do not over-read.
- **Engagement — activity: Four Boxes on Paper (5 min):** Hostel warden problem — highest attendance in `[18, 22, 19, 22, 15]`. Students write input, output, steps, two edge cases in notebook. **Do not code yet.**
- Circulate / spot-check Zoom screens or walk the room.
- **Cold-call (2 students):** Read their output and one edge case aloud.
- Reveal suggested answers from notes: output `22`; edge cases `[]` and `[7, 7, 7]`.

**Bridge sentence:** "The four boxes are useless if they stay in the notebook — now we turn the pass-count plan into a real function."

---

## 4. From Paper Plan to `countPassed` — Live Code (14 minutes)

- **Room action:** Screen-share One Compiler. Paste or live-type `countPassed` from notes **slowly** — narrate `passed`, the `for` loop, `>= 40`, and `return`.
- Students type along; **do not rush**.
- Run the main call first; ask students to predict output **before** Run (**3**).
- Then run edge-case logs one by one: `[]` → **0**, `[40]` → **1**, `[10, 20, 39]` → **0**.
- **Common doubt (1 min):** `console.log` inside the function vs `return` — print shows; return lets other code reuse the number.
- **Engagement — thumbs up:** everyone's console shows `3`, then `0`, `1`, `0` for the edge tests.
- **Cold-call:** "What pattern did the four boxes already tell us — one loop or nested loops?" (One loop.)

**Bridge sentence:** "Some problems look like they need nested loops — but often one pass plus an object is enough. That pattern is a frequency counter."

---

## 5. Frequency-Counter Intuition Using Objects (16 minutes)

- Screen-share the **canteen tally** image (`sessionmc1-02-frequency-counter-tally.png`).
- Canteen board analogy: tea | samosa | idli — add a mark per order; do not compare every token with every other token.
- Connect to prior knowledge: they already know **create object**, **read property**, **update property**.
- Walk the **trace table** from notes on screen — orders `["tea", "samosa", "tea", "idli", "samosa", "tea"]` → `{ tea: 3, samosa: 2, idli: 1 }`.
- **Common error (30 sec):** new key starts at `1`; `undefined + 1` → `NaN`.
- **Live-code:** `countOrders` from notes in One Compiler. Run full demo; show `tally.tea` and empty list `{}`.
- Mention anagrams in **one sentence only** — same tally idea; two loops one after another is still about **n**, not n times n. Students can try `"listen"` / `"silent"` at home if time is tight.
- **Engagement — activity: Build a Tally by Hand (3 min):** Word `"MASAI"` — students rewrite the object after each letter in notebook. Cold-call: which letter wins? (**A**, twice.)
- Optional quick confirm: `countOrders(["M", "A", "S", "A", "I"])` in One Compiler if 2 minutes remain.

**→ Take the single break (5–8 minutes) here if you have hit ~55–65 minutes. Optional return prompt: "After break — two fingers on an array instead of one." ←**

**Bridge sentence:** "Frequency counting used one finger moving left to right — some problems are easier with two fingers from both ends."

---

## 6. Two-Pointer Intuition — Palindrome Check (10 minutes)

- Screen-share the **two pointers** image (`sessionmc1-03-two-pointers-array.png`).
- Locker-row / symmetric-check analogy from notes.
- Define **palindrome** in one line; trace `"NITIN"` using the table — left/right indices move inward.
- **Live-code:** `isPalindrome` from notes. Run `NITIN` → true, `PATNA` → false, `""` → true.
- **Common doubt (30 sec):** reverse string vs two pointers — reversing builds new string; pointers use two index variables on the original text.
- **Engagement — cold-call:** "If first and last characters mismatch, do we finish the whole word?" (No — stop early.)

**Bridge sentence:** "The same two-finger idea also finds a target sum — but only when the list is already sorted."

---

## 7. Two-Pointer Intuition — Pair Sum on a Sorted Array (10 minutes)

- State problem: two **different** prices add to target? Example `[10, 20, 35, 50, 60]`, target `70` — yes (`10 + 60`, `20 + 50`); target `90` — no.
- Walk the three rules aloud: sum too small → move `left` right; too big → move `right` left; match → found.
- **Common error (1 min):** jumbled list breaks the rule — do not apply pair-sum pointers on unsorted data.
- **Live-code:** `hasPairSum` from notes. Run target `70` → true, `90` → false, `[]` → false.
- **Engagement — activity: Move the Fingers (3 min):** List `[5, 8, 12, 20]`, target `25` — students write sums in notebook. Cold-call the first step (`5 + 20 = 25`, **true**). If time, mention target `13` trace from notes.

**Bridge sentence:** "You now have more than one way to solve problems — next we need plain language to compare how heavy each way becomes as data grows."

---

## 8. O(1), O(n), and O(n²) in Plain Words (14 minutes)

- Screen-share the **Big-O growth** image (`sessionmc1-04-big-o-growth.png`).
- One line: **Big-O** names the **growth shape**, not exact seconds. **n** = usually `array.length`.
- **O(1) (3 min):** labelled locker / tiffin box. Run `firstMark` snippet from notes. Clarify: "first mark?" is O(1); "is 90 anywhere?" is not if you must search.
- **O(n) (3 min):** warden checking register once. Link back: `countPassed`, `countOrders`, `isPalindrome`, `hasPairSum` — about one pass each. Two loops **in a row** still O(n).
- **O(n²) (4 min):** handshake analogy. **Live-code:** `hasDuplicateSlow` — nested loops. Run demo; stress result can be **correct** but **growth** is the issue.
- Flash the **Family** comparison table from notes.
- **Common doubt (30 sec):** O(n²) means grows like a square — not exactly n×n every time.

**Bridge sentence:** "Big-O is most powerful when two methods solve the same problem — let's compare duplicate detection two ways."

---

## 9. Same Problem, Two Speeds — `hasDuplicateFast` (8 minutes)

- One line recap: nested pairs = O(n²); tally object in one pass = O(n).
- **Live-code:** `hasDuplicateFast` from notes. Run `["Riya", "Aman", "Riya"]` → true and unique list → false.
- Stress the trade: a little extra object memory for much less repeated scanning.
- Scale story from notes: 10 names — no felt difference; 10,000 rows — nested plan hurts.
- **Engagement — activity: Name the Family (3 min):** Read the five situations from notes; students write O(1), O(n), or O(n²) in notebook. Cold-call #3 and #4. Reveal suggested answers from notes.

**Bridge sentence:** "Patterns and growth labels are useful only if you use them every time a new problem appears — that is the checklist."

---

## 10. Eight-Step Checklist and Vowel Problem (12 minutes)

- Pilot pre-flight analogy — do not wire randomly in a lab exam.
- Read the **eight steps** from notes once at pace; do not re-teach each step in depth.
- **Worked example (4 min):** Screen-share the **Attendance Duplicates** checklist table. Walk each row briefly — pattern is frequency object; growth O(n) vs nested O(n²).
- **Engagement — activity: Run the Checklist Once (5 min):** Vowel count in `"patna"` (answer **2**). Students fill all eight rows in notebook, then code in One Compiler if ready.
- Circulate; help students stuck on step 2 (input = string) or step 4 (`""` → `0`).
- Hint from notes: one O(n) loop over `a e i o u` — no two pointers needed.
- **Thumbs up:** at least steps 1–5 filled in notebook.

**Bridge sentence:** "If you can fill the checklist, you are ready to type — let's lock what we built today."

---

## 11. Key Takeaways and Close (4 minutes)

- Flash **Key Takeaways** from Lecture Notes; read the five bullets once — do not re-teach.
- One-line link forward: same checklist applies when they later **search**, **sort**, and attach JavaScript to **web pages**.
- **Exit ticket — cold-call (2 students):** "Name the four boxes before you code."
- **Exit ticket — cold-call (1 student):** "When do you use two pointers for pair sum?" (Sorted list only.)
- Point students to the **Important Commands, Libraries, Terminologies used** table and remind them: every program in this session runs at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.
- Thank the cohort.

**Bridge sentence:** "Plan first, pick a pattern, name the growth, then code — that is algorithmic thinking in JavaScript."

---

## Timing Flex

If the session is running late, cut in this order (keep the core path intact):

1. **Shorten Block 2:** Skip the chat poll; keep chai + exam-cell story only.
2. **Shorten Block 3:** Reduce paper activity to 3 minutes; cold-call one student instead of two.
3. **Shorten Block 5:** Skip live anagram mention and optional MASAI One Compiler confirm; keep trace + `countOrders` only.
4. **Shorten Block 7:** Skip the extra target `13` trace; keep target `25` only.
5. **Shorten Block 9:** Read Name the Family answers yourself instead of full notebook activity.
6. **Shorten Block 10:** Walk attendance checklist only; assign vowel problem as take-home using the same eight steps.
7. **Do not cut** Blocks 4, 6, and 8 core — `countPassed` live code, palindrome two pointers, and O(1)/O(n)/O(n²) with `hasDuplicateSlow` are the masterclass spine.
8. If you finish **5+ minutes early:** run a quick chat poll — "Duplicate names — nested loops or frequency object?" — then discuss one answer aloud. Or let students finish the vowel function and share outputs in chat.
