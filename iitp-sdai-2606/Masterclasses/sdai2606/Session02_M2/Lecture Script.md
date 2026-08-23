# Lecture Script: Masterclass: Sorting Algorithms – Insertion Sort

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include card activities, traces, multiple Python demos, merits/demerits, and practice problems. The **same** document is **shared with students**. This script does **not** require covering every example live. For each topic, pick a **small, clear** set that fits the clock; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, full code, and diagrams stay with your **Lecture Notes** (slides, OneCompiler, or board). Skim headings aloud; let visuals and live code carry the structure.

**Break (only pause in this plan):** After **roughly 55–65 minutes** of session clock time (after the **hand-tracing** segment), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why another sort (6 minutes)

- Greet; confirm everyone has **OneCompiler** (or IDE) open and can run a short Python loop from earlier lessons.
- Recap in one line: they have already learnt **Binary Search**, **Bubble Sort**, and **Selection Sort** — today they learn another important sort: **Insertion Sort**.
- State outcomes: grow a **sorted subarray**, **traverse** and **shift**, implement with loops, **trace** each current element, then name merits, uses, and other sort names.
- **Cold-call 2 students:** “When you pick up playing cards, do you keep the hand sorted as each new card arrives?”
- **Check for thumbs up:** Lecture Notes for this masterclass are open.

**Bridge:** “Bubble and Selection already sort. Insertion Sort uses a different habit—keep a neat left side and insert the next value. Let’s see that with cards.”

---

## 2. The card-hand picture (8 minutes)

- One sentence: first card is already sorted; each new card is slipped into the correct place in the hand.
- Screen-share the **playing-cards** image from notes (sorted hand vs waiting cards).
- Walk `7, 2, 9, 4, 5` aloud: hand = sorted subarray; table = unsorted part.
- **Activity (3 min):** marks `45, 12, 78, 23, 56`—students cover all but the first, uncover one at a time, rewrite the left group. Final: `12, 23, 45, 56, 78`. Circulate / spot-check Zoom notebooks.
- **Cold-call 1 student** to read their left group after the third uncover.

**Bridge:** “That growing left group has a name—**sorted subarray**. Next we watch the boundary move on a real list.”

---

## 3. Sorted subarrays — the growing left side (10 minutes)

- One sentence: left part stays sorted; right part waits; only **one** new element finds a home each round.
- Temple-queue analogy from notes—token-order people vs new arrivals outside.
- Screen-share the **sorted subarray** image; build the `[29, 10, 14, 37, 13]` boundary table on board (start → insert `10` → `14` → `37` → `13`).
- Stress: after each outer step the left slice grows by **exactly one**.
- **Common mistake (30 sec):** thinking the whole right side is also being rearranged in the same round.
- **Activity (2 min):** `[8, 3, 6, 1]` after two outer steps (`i = 1` and `i = 2`)—chat the left part. Reveal **`[3, 6, 8]`**.
- **Check for thumbs up:** everyone can point to “sorted left / unsorted right.”

**Bridge:** “To grow that left side, the program must visit each remaining index. That walk is **array traversal**.”

---

## 4. Array traversal — every new element gets a turn (8 minutes)

- Define traversal: visit items in a planned order. Locker-row / teacher-from-roll-2 analogy.
- Board: **outer loop** `i = 1` to `n - 1` (current element); **inner loop** walks **left** from `i - 1`.
- **Why start at 1:** `arr[0]` is already a sorted subarray of length one.
- **Live / follow-along:** run the small print-only traversal on `marks = [45, 12, 78, 23, 56]`; students see `i`, current element, and `marks[:i]`.
- **Activity (1 min):** list of `6` elements—how many outer steps if we start at index `1`? Chat (**5**).
- **Cold-call:** “What happens if we start the outer loop at `0`?” (First round does nothing useful.)

**Bridge:** “Traversal tells you *which* element is current. The next skill is *how* it moves—**shifting**, not a random swap.”

---

## 5. Element shifting — opening a seat (12 minutes)

- One sentence: save the current value as **`key`**, slide larger left values one seat **right**, drop `key` in the gap.
- Cinema-row / bookshelf analogy from notes.
- Screen-share the **cinema shifting** image.
- Live board: insert `13` into `[10, 14, 29, 37, 13]`—write each shift row; name the landing index **1**.
- Mention **stability** in one line: use `>` not `>=` so equal values keep their original order.
- **Activity (3 min):** seats `20, 40, 60, 25`—students write every shift, then answer: would swapping only `60` and `25` finish the job? Chat yes/no. Reveal **No** (`20, 40, 25, 60` is still unsorted).
- **Pair-share (1 min):** partner says the difference between a **shift** and a **swap**.

**Bridge:** “You now have three blocks—sorted left side, traversal, and shifting. Next we lock the full steps and act like the computer on paper.”

---

## 6. How it works and trace by hand (16 minutes)

- Skim the six ascending steps from notes (`key`, `j`, shift, `arr[j + 1] = key`).
- 30-second warning: without `j >= 0`, Python `arr[-1]` means the **last** item—wrong comparison.
- Trace `arr = [29, 10, 14, 37, 13]` live: `i = 1` (`10` → index **0**), `i = 2` (`14` → index **1**), `i = 3` (`37` already home), `i = 4` (`13` → index **1`).
- Screen-share the **trace one insertion** image when you reach inserting `13`.
- Pause after each outer step—ask “What is the current element? Where does it land?”
- **Guided activity (4 min):** `[5, 2, 4, 6]` for `i = 1` and `i = 2` only; expected `[2, 5, 4, 6]` then `[2, 4, 5, 6]`. Circulate / spot-check Zoom screens.
- **Check for thumbs up:** everyone can name `key` and the landing index for one step.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break, we turn the same paper tables into a `for` plus a `while`—**Insertion Sort in Python**.”

---

## 7. Implement Insertion Sort in Python (16 minutes)

- One sentence: outer `for` picks `key`; inner `while` compares and shifts; last write places `key`.
- **Live-code slowly** `insertion_sort` from notes; narrate `key`, `j >= 0 and arr[j] > key`, and `arr[j + 1] = key`.
- Students type along in OneCompiler; **do not rush**.
- Run `[29, 10, 14, 37, 13]`, then `[7]`, then `[]`; pause for predictions.
- **Common mistakes board (3 min):** `>=` vs `>` (stability); `j > 0` vs `j >= 0`; forgetting `j = j - 1`; losing `key` before shifting.
- **Activity — predict then run (3 min):** `insertion_sort([4, 3, 2, 1])` and `insertion_sort([1, 2, 3, 4])`; students write answers in chat before Run (both `[1, 2, 3, 4]`; second does almost no shifting).
- **Check for thumbs up:** everyone’s function prints the sorted scores list.

**Bridge:** “The code works—now we answer how the work grows, and when this sort is a wise choice.”

---

## 8. Complexity, merits, and demerits (10 minutes)

- One sentence: time = how walking and sliding grow with `n`; extra space = a few integers → **O(1)**.
- Flash the complexity table: already sorted **O(n)**; reverse / random **O(n²)**; extra space **O(1)**.
- Exam-papers analogy: almost in roll order vs reverse order.
- **Activity (2 min):** `[1, 2, 4, 3, 5]`—how many shifts to place `3`? Walk **left** from `4`. Chat (**1**).
- Merits (board, short): simple, in-place, stable, adaptive, good for small / online inserts.
- Demerits (board, short): slow on large shuffled data; many shifts; not the main engine for huge `n`.
- **Cold-call:** “Bicycle on a short lane vs a 400 km highway—when is Insertion Sort the bicycle?”

**Bridge:** “Strengths and limits decide *where* we use it. Let’s look at real jobs and the other sort names you will hear.”

---

## 9. Practical applications and other sort names (8 minutes)

- Screen-share the **where it is used** image (leaderboard, price tag, marks list, attendance sheet).
- Skim five uses: small lists, nearly sorted data, live ordered lists, online insertion, small runs inside bigger library sorts.
- **Activity (2 min):** A = one crore random product IDs; B = one new fare into six sorted bus fares. Chat A or B. Reveal **B**.
- Read the **names only** (no logic today): **Merge Sort**, **Quick Sort**, **Heap Sort**, **Shell Sort**, **Counting Sort**, **Radix Sort**, **Bucket Sort**, **Timsort**. They already know Bubble and Selection.
- **Pair-share (1 min):** “Name two merits and one place you would use Insertion Sort.”
- **Check for thumbs up:** everyone can say one merit and one other sort name.

**Bridge:** “Theory is locked—let’s apply the same insert idea to marks, a new price, and edge cases.”

---

## 10. Problem solving with Insertion Sort (10 minutes)

- **Live / follow-along:** Problem 1—`sort_marks`; run `[45, 12, 78, 23, 56]` and `[88, 88, 70]`; point out equal `88`s stay in order.
- Problem 2—`insert_into_sorted` on prices; run `249`, `50`, `600`. Stress: this is **one outer step**.
- Skim Problem 3 edges: `[]`, `[42]`, already-sorted `[10, 20, 30]`—loop is quiet but safe.
- **Activity (3 min):** tokens `[11, 18, 25, 40]`, new token `20`—paper shifts then confirm with `insert_into_sorted`. Expected `[11, 18, 20, 25, 40]`. Circulate.
- Spot-check 2–3 student screens for the landing index of `20`.

**Bridge:** “One more drill ties traversal, shifting, and tracing together—then we close with takeaways.”

---

## 11. Full practice, takeaways, and close (6 minutes)

- Screen-share or paste `insertion_sort_with_trace` from notes; run `[29, 10, 14, 37, 13]` and match it to the paper trace.
- Ask students to watch **current element**, **sorted left**, and landing **index**.
- **Notebook summary (2 min):** three lines—(1) define Insertion Sort, (2) what a sorted subarray is, (3) shift vs swap.
- Flash **Key Takeaways** and the quick-reference table; remind them unfinished examples live in the notes.
- **Exit ticket cold-call (2 students):** “One merit and one demerit, in one sentence each.”
- Thank the cohort; point to notes for revision before the next lesson.

**Bridge:** “You can now grow a sorted left side, shift to open a seat, code Insertion Sort, and say when it is the right tool.”

---

## Timing Flex

If the session is running late, cut in this order (keep the core path intact):

1. **Drop** the full board walk of inserting `37` (already home)—say it in one line and move on.
2. **Skip live typing** of Problem 1; show Problem 2 (insert one value) + one edge case.
3. **Shorten** Block 9: read only three other-sort names (Merge, Quick, Timsort); assign the rest as notes.
4. **Shorten** Block 11: run the traced script once; assign the notebook summary as homework.
5. **Do not cut** Blocks 2, 5, 6, and 7 (card intuition + shifting + trace + Python code)—those are the masterclass spine.
6. If early by 5+ minutes: extra chat poll—“already-sorted list: about how much work?”—then one volunteer shares their `insertion_sort_with_trace` output.
