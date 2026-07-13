# Lecture Script: Masterclass: Searching Algorithms – Binary Search

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include worked traces, multiple Python demos, and practice problems. The **same** document is **shared with students**. This script does **not** require covering every example live. For each topic, pick a **small, clear** set that fits the clock; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, full code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 55–65 minutes** of session clock time (after the **hand-tracing** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why searching matters (6 minutes)

- Greet; confirm everyone has **OneCompiler** (or IDE) open and can run a short Python function from earlier lessons.
- Recap in one line: earlier they learned to **sort** lists (Bubble / Selection)—today they learn to **search** fast on **sorted** data.
- State outcomes: explain **binary search**, write **iterative** Python code, analyse **O(log n)** time and **O(1)** space, and **trace** steps on paper.
- Screen-share the **searching** image (attendance sheet / dictionary / ticket) from notes.
- **Cold-call 2 students:** “Where have you searched for something in a long list—results, train number, product price?”
- **Check for thumbs up:** Lecture Notes for this masterclass are open.

**Bridge:** “Searching means ‘Is it there, and where?’ First let’s see the slow, honest method—**linear search**—so binary search feels special.”

---

## 2. Linear search — the slow baseline (10 minutes)

- One sentence: **linear search** checks items **one by one** from the start.
- Drawer / queue analogy from notes—no order required.
- **Live / follow-along:** paste or type `linear_search` from notes; run searches for `67` and `50` on the marks list.
- Ask students to predict outputs **before** you press Run.
- **Activity (2 min):** list `[10, 20, …, 80]`—find `80` mentally; how many checks? Cold-call for the answer (**8**).
- Stress: worst case checks **all n** items → **O(n)**.

**Bridge:** “Linear search always works—but binary search is smarter **only if** the list is already sorted. That rule comes next.”

---

## 3. Prerequisite — sorted data (8 minutes)

- State the hard rule: binary search needs **sorted** data (usually ascending).
- Screen-share the **sorted vs not sorted** image from notes.
- Flash the quick-check table: safe list / descending / unsorted.
- **Activity (2 min):** MCQ from notes—A, B, or C—which list is unsafe? Students type letter in chat; reveal **B**.
- **Cold-call:** “What can go wrong if we binary-search an unsorted list?”
- **Common mistake (30 sec):** unsorted input → wrong index or false “not found.”

**Bridge:** “Once the list is sorted, we can use the dictionary trick—open the middle, throw away half. That’s binary search.”

---

## 4. How binary search works (12 minutes)

- Dictionary / “guess 1 to 100” analogy—check middle, keep one half, repeat.
- Screen-share the **binary halving** image from notes.
- Introduce **`low`**, **`high`**, **`mid`** with the three-pointers table on screen or board.
- Walk the step-by-step logic aloud once (no full code yet): equal → found; mid too small → `low = mid + 1`; mid too big → `high = mid - 1`.
- **Activity — number-guessing warm-up (3 min):** students pick a secret from 1–50 in notebook; write guesses that cut the range in half; count guesses. Cold-call 2 for their count (aim ~6).
- **Check for thumbs up:** everyone can say “check middle, keep one half” in their own words.

**Bridge:** “Feeling the halvings is good—now we act like the computer on paper with **low**, **mid**, and **high**.”

---

## 5. Trace execution by hand (14 minutes)

- Screen-share the **trace pointers** image; write `arr = [3, 8, 15, 20, 27, 35, 42]`, target `27` on board.
- Build the first trace table **live** (3 steps to index **4**). Pause after each mid—ask “left or right?”
- Second trace: target `16` (not found)—show `low > high` → **-1**.
- Compare: binary used **3** checks for `27`; linear from the left would need **5**.
- **Guided activity (4 min):** list `[5, 10, …, 40]`, target `10`—students fill `low` / `high` / `mid` in notebook; circulate / spot-check Zoom screens.
- **Pair-share (1 min):** partner explains why we use `while low <= high`, not `<`.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break, we turn the same paper logic into a **`while` loop** in Python—**iterative binary search**.”

---

## 6. Iterative binary search in Python (18 minutes)

- Define **iterative**: `while` loop updating borders—not recursion today.
- **Live-code slowly** the `binary_search` function from notes; narrate every line (`//` for mid, `mid + 1` / `mid - 1`).
- Students type along in OneCompiler; **do not rush**.
- Run demos: prices list—`399`, `450`, `99`, `699`; pause for predictions.
- **Common mistakes board (3 min):** `/` vs `//`; `low < high` vs `low <= high`; forgetting `±1` (infinite loop); unsorted input.
- **Activity — predict then run (3 min):** `nums = [2, 4, 6, 8, 10]` → search `8` and `7`; students write answers in chat before Run (**3**, **-1**).
- **Check for thumbs up:** everyone’s function returns index or `-1` correctly on the demo.

**Bridge:** “The code works—now we answer the interview-style question: **why is this O(log n)?**”

---

## 7. Time complexity — why O(log n)? (12 minutes)

- One sentence: time complexity = how work grows as `n` grows.
- Screen-share the **linear vs binary speed** image from notes.
- Show the size table: 8→~3, 16→~4, 1,000→~10, 1,000,000→~20 checks.
- On board: `n → n/2 → n/4 → … → 1` = about **log₂(n)** steps.
- Best case **O(1)** (first mid hits); typical/worst **O(log n)**.
- **Activity (2 min):** for `n = 32`, how many cuts? Chat answers (**about 5**).
- **Cold-call:** “If the list grows from 1,000 to 1,000,000, does binary search need a thousand times more steps?”

**Bridge:** “Speed is half the story—**extra memory** for iterative binary search stays tiny. That’s space complexity.”

---

## 8. Space complexity O(1) and quick compare (8 minutes)

- Define **space complexity** as **extra** memory beyond the input list.
- Finger-on-timetable analogy: only `low`, `high`, `mid` → **O(1)**.
- **Cold-call:** “Does the original list count as O(n) space for the algorithm’s *extra* cost?” (Clarify: input yes; extra for iterative BS is still **O(1)**.)
- Flash the **Linear vs Binary** comparison table from notes (sorted need, time, space, when to use).
- **Pair-share (1 min):** “When would you still use linear search?”

**Bridge:** “Theory is locked—let’s apply the same loop to small real problems: roll numbers, scores, and edge cases.”

---

## 9. Problem solving with binary search (12 minutes)

- **Live / follow-along:** Problem 1—`find_roll_number` returning `True`/`False`; run `112` and `110`.
- Skim Problem 2—index of a unique score; stress “unique sorted list” (no first-occurrence variant today).
- **Live demo:** Problem 3 edge cases—`[]`, `[7]` hit, `[7]` miss—show empty list never enters the loop.
- **Activity (3 min):** bus fares `[15, 20, 25, 30, 40, 50]`, find `40`—paper trace then confirm with code; expected index **4**. Circulate.
- Spot-check 2–3 student screens for correct `mid` updates.

**Bridge:** “One more drill ties code, tracing, and step-counting together—then we close with takeaways.”

---

## 10. Full practice, takeaways, and close (8 minutes)

- Screen-share or paste `binary_search_with_trace` from notes; run successful search (`27`) and missing search (`21`).
- Ask students to watch how `steps` stays small as the range collapses.
- **Notebook summary (2 min):** three lines—(1) define binary search, (2) prerequisite, (3) time + space complexity.
- Flash **Key Takeaways** and the quick-reference table; remind them unfinished examples live in the notes.
- **Exit ticket cold-call (2 students):** “Say O(log n) and O(1) in one plain-English sentence each.”
- Thank the cohort; point to notes for revision before the next lesson.

**Bridge:** “You can now search sorted data the smart way—halve, code, trace, and explain the complexity in plain words.”

---

## Timing Flex

If the session is running late, cut in this order (keep the core path intact):

1. **Drop** the second hand-trace (`16` not-found) as a full board walk—leave it as “try in notes.”
2. **Skip live typing** of Problem 2; show only Problem 1 + edge cases.
3. **Shorten** Block 10: run one traced call only; assign the notebook summary as homework.
4. **Do not cut** Blocks 4–6 (intuition + trace + iterative code)—those are the masterclass spine.
5. If early by 5+ minutes: extra chat poll—“unsorted list + binary search: what happens?”—then one volunteer shares their `binary_search_with_trace` output.
