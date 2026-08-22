# Two Pointers and Sliding Windows

## What You Will Learn in This Session

In the previous session you built an arithmetic expression evaluator. You saw that **recursion** and an **explicit stack** are two shapes of the same idea, and you practised thinking in **O(n)** versus slower nested work.

That session trained you to break a nested problem into small, well-defined steps. This session trains a different skill: looking at an array or string problem and choosing a **pattern** before you write nested loops.

You already know Python **loops**, **lists**, **if/else**, and how to write a **function**. Today you will use those tools to scan a list once, instead of checking every pair twice.

You will learn:

- Why nested loops feel natural, and when they **waste work** you have already done.
- How **two pointers** move from the ends, or chase from the same side.
- How a **sliding window** grows and shrinks across a contiguous stretch.
- When **sorting** helps two pointers, and when sorting destroys the answer.
- How to pick **two pointers**, a **fixed window**, a **variable window**, or **neither** from the problem statement alone.

By the end, you will look at a playlist-style list or a string and say: "This is a window" or "This is two pointers" — then write an **O(n)** scan with confidence.

---

## Why Nested Loops Feel Natural

When a problem says "find a pair" or "check every stretch," the first idea is often a loop inside a loop. That idea is not foolish. It is the most direct translation of the English sentence.

- **Official Definition:** A **nested loop** is a loop placed inside another loop, so the inner loop runs fully for every step of the outer loop.
- **In Simple Words:** You pick one item, then check it against every other item, then pick the next item and repeat.
- **Real-Life Example:** In a class of 40 students, you compare every student with every other student to find a pair whose marks add to 150. You do a huge number of comparisons, even though many pairs share the same students.

The method can be **correct**. The trouble starts when the list grows: for **n** items, nested pair checks grow like **n × n**, written as **O(n²)**.

- **Official Definition:** **O(n²)** (said "oh of n squared") is a time-complexity label meaning the work grows roughly like **n times n** as the input size grows.
- **In Simple Words:** If the list becomes 10 times longer, this kind of nested checking becomes about **100 times** heavier, not 10 times.
- **Real-Life Example:** Checking every student against every other student in a class of 10 is about 100 comparisons. In a class of 100 it is about 10,000 — the hall did not grow 100 times, but the work did.

### The Hidden Waste

Suppose a music app stores an **engagement score** for each play in a session. Product wants the best stretch of **3 consecutive** plays.

```text
scores = [20, 90, 85, 10, 95]
k = 3
```

A nested-style scan adds the first three, then the next three, then the next three:

```text
20 + 90 + 85 = 195
     90 + 85 + 10 = 185   (you added 90 and 85 again)
          85 + 10 + 95 = 190   (you added 85 and 10 again)
```

Two of the three numbers were already known. Nested summing refuses to reuse them.

- **Need:** You want the same answer with work that grows like **n**, not like **n × k** or **n × n**.
- **Logic:** Keep a running total. When the stretch moves one step right, **subtract** the score that left and **add** the score that entered.
- **Common doubt:** "If nested loops give the right answer, why change?" Because a session with 1,00,000 plays cannot afford recounting every stretch from scratch.

### Activity: Count the Repeated Additions

On paper, write every stretch of length 3 for `[20, 90, 85, 10, 95]`. Circle every number that was added in the previous stretch as well.

You should circle **90**, **85**, and then **85**, **10**. Those circled values are the wasted work a sliding total will skip.

---

## Two Pointers

Once you accept that recounting is wasteful, you need a cleaner way to walk a list. **Two pointers** is the first such pattern: two indices that move with a rule, not two free nested loops.

- **Official Definition:** A **pointer** in this lesson is an integer **index** into a list or string. **Two pointers** means two indices whose movement is coordinated so each index walks the data a small number of times.
- **In Simple Words:** You keep two fingers on the list — a left finger and a right finger — and you move one finger at a time according to a rule.
- **Real-Life Example:** Two friends stand at the two ends of a sorted railway reservation chart. If the sum of the two fares is too small, the left friend steps toward costlier rows. If the sum is too large, the right friend steps toward cheaper rows.

You never need both friends to jump randomly. One rule, one step, until they meet.

### Pointers That Meet in the Middle

Place **left** at index `0` and **right** at the last index. Move them toward each other.

```text
numbers = [2, 7, 11, 15]     target sum = 18
            L            R

2 + 15 = 17   too small   → move L right
7 + 15 = 22   too big     → move R left
7 + 11 = 18   exact match → stop
```

This shape needs a **sorted** list. You can only say "I need a bigger sum, so move left" if you know that values increase toward the right.

Use this shape for a **pair sum** on sorted data, a **palindrome** check, or "container with most water" style problems.

### Pointers That Chase from the Same Side

Both pointers start on the left. **Fast** reads every item. **Slow** only moves when you want to **keep** a value.

```text
nums = [0, 0, 1, 1, 1, 2]
        S
        F
```

Fast walks the whole list. Whenever `nums[fast]` is a new value, copy it next to slow and move slow forward. Slow is the boundary of the "useful prefix."

Use this shape to **remove duplicates in place**, move zeroes to the end, or compact a list without building a second list.

### Activity: Name the Shape

For each task, write **meet in the middle** or **chase from the same side**:

1. Reverse the characters of `"NAMAN"` without building a new string.
2. From a sorted marks list, find two marks that add to 90.
3. Overwrite a sorted roll-number list so duplicates disappear from the front.

Suggested direction: (1) meet in the middle, (2) meet in the middle, (3) chase from the same side.

---

## Sorted Lists and Unsorted Lists

Two pointers from the ends only work when moving a pointer changes the answer in a **predictable** direction. Sorting is the usual way to get that property — but sorting is not always allowed.

- **Official Definition:** A list is **sorted** when its values follow a known order, such as non-decreasing numbers. **Sorting** rearranges values into that order.
- **In Simple Words:** Sorted means "smaller to bigger" (or the reverse). Unsorted means the values can jump around.
- **Real-Life Example:** A result portal already sorted by roll number is easy to binary-search. A pile of hall tickets in random order is not. If you shuffle a playlist to sort by score, you also destroy the **listening order**.

| Situation | What you should do |
|---|---|
| List is already sorted; you need a pair of **values** | Two pointers from the ends. Do not sort again. |
| List is unsorted; you need a pair of **values**, and original positions do not matter | Sort first, then two pointers. Remember that sorting costs about **O(n log n)**. |
| You need a **contiguous** stretch (items that sit next to each other in the original order) | Do **not** sort. Sorting breaks adjacency. Use a sliding window. |
| You need a pair of **original indices** on an unsorted list | A **hash map** (dictionary), not two pointers from the ends. |

**Common doubt:** "Can I always sort, then use two pointers?" Only when the problem cares about **values**, not **positions in the original order**. A "best three consecutive songs" problem dies if you sort.

---

## Sliding Windows

Two pointers from the ends hunt **pairs**. Many problems hunt a **stretch of neighbours** instead — a block of songs, a block of characters, a block of orders. That stretch is a **window**.

- **Official Definition:** A **sliding window** is a contiguous segment `[left, right]` that moves across a list or string. The right index grows the segment. The left index shrinks it when a **constraint** is broken.
- **In Simple Words:** Imagine a cardboard frame that covers a few tracks on a playlist. You slide the frame only to the right. You never jump backwards.
- **Real-Life Example:** A kirana shop runs a "any 3 consecutive items on this shelf" combo. The shopkeeper does not rebuild the combo from scratch. He drops the item that left the frame and adds the item that entered.

- **Official Definition:** A **constraint** is the rule that decides whether the current window is allowed.
- **In Simple Words:** The constraint is the "house rule" of the window — unique characters, no early skip, sum of length k, and so on.
- **Real-Life Example:** A combo offer is valid only while it contains exactly three consecutive shelf items. If a fourth item enters, the shopkeeper must drop the leftmost item. That "exactly three" rule is the constraint.

```text
playlist:  a  b  c  d  e  f
window:       [c  d  e]
              L     R
```

- **Right** always moves forward when you include a new item.
- **Left** moves forward only when the window has become **invalid**.
- Because neither index moves backwards, each position enters and leaves the window **at most once**. The scan is **O(n)**.

### Fixed-Size Window

The length is always **k**. Every step you drop one item from the left and add one item from the right.

Keywords you will see: *subarray of size k*, *every window of length k*, *maximum of every k consecutive*.

### Variable-Size Window

The length changes. You grow **right** freely, and you shrink **left** until the constraint holds again.

Keywords you will see: *longest substring such that*, *smallest window that covers*, *at most k distinct*, *product less than k*.

Two common goals:

| You want | What you record | How left moves |
|---|---|---|
| **Longest valid** stretch | Maximum length while the constraint is true | Shrink **just enough** to become valid, then record |
| **Shortest valid** stretch | Minimum length while the constraint is true | Grow until valid, then shrink **as much as possible** while still valid, then record |

**Common doubt:** "Is a window the same as two pointers?" A window **uses** two pointers (`left` and `right`). The extra idea is that the items **between** them must stay contiguous, and you maintain a running summary of that slice.

### Activity: Circle the Keywords

Read these three sentences. Write **fixed window**, **variable window**, or **not a window**.

1. Maximum sum of any **4 consecutive** orders.
2. Longest run of deliveries **without** a cancelled order.
3. Maximum sum if you may pick **any** orders, even if they are not next to each other.

Suggested direction: (1) fixed window, (2) variable window, (3) not a window — that is a subsequence problem, not a contiguous stretch.

---

## Time and Space in Plain Language

You now have two families of O(n) scans. Before you code, you should be able to say how much **work** and how much **extra memory** each family uses.

- **Official Definition:** **Time complexity** describes how the number of operations grows as the input size **n** grows. **Space complexity** describes how extra memory grows with **n**.
- **In Simple Words:** Time is "how much walking." Space is "how many extra notebooks."
- **Real-Life Example:** Counting every IRCTC passenger twice is extra time. Photocopying the whole reservation chart is extra space.

| Approach | Time (simple view) | Extra space | When it fits |
|---|---|---|---|
| Nested loops over pairs or all stretches | O(n²) | O(1) | Tiny n, or a first correctness check |
| Two pointers on already sorted data | O(n) | O(1) | Pair / palindrome / compact-in-place |
| Sort, then two pointers | O(n log n) | depends on the sort | Values matter, original order does not |
| Sliding window plus a **set** or **dictionary** | O(n) | O(k) or O(alphabet) | You must remember what is inside the window |

- **Official Definition:** **O(n)** means the number of operations grows in a straight line with the input size **n**.
- **In Simple Words:** If the playlist becomes 10 times longer, you do about 10 times more steps — not 100.
- **Real-Life Example:** Walking once from the first coach to the last coach of a train is O(n). Walking every coach from every other coach is O(n²).

The usual trade-off: you spend a small **set** or **map** so you do not rescan the window on every step.

---

## How to Pick a Pattern from the Problem Statement

Read the statement once. Circle whether the answer must be **contiguous**. Then classify.

| You see in the statement | Likely pattern | Why |
|---|---|---|
| Pair that sums to a target, and the list is sorted (or may be sorted) | Two pointers from the ends | The sum moves up or down in a predictable way |
| Remove, compact, or partition **in place** | Slow and fast pointers | Fast reads, slow writes |
| Subarray or substring of length **k** | Fixed sliding window | Width never changes |
| Longest or shortest **contiguous** stretch **such that** a constraint holds | Variable sliding window | Width changes with the constraint |
| Maximum of every k consecutive items | Fixed window | Same width, sliding |
| Any **subsequence** (items need not sit together) | Neither of today's patterns | A window requires neighbours |
| Subarray **sum equals k**, and numbers may be **negative** | Neither (use prefix sums and a dictionary) | Shrinking left does not always reduce the sum |
| Pair of **indices** on an unsorted list | Dictionary lookup | Sorting would scramble the indices |

Walk this checklist in order:

1. Must the answer be a contiguous slice? If no, it is not a window.
2. Is the width fixed as **k**? If yes, use a **fixed window**.
3. Is there a constraint that tells you when to grow or shrink? If yes, use a **variable window**.
4. Are you hunting a pair on **sorted** data? If yes, use **two pointers from the ends**.
5. If none of these match, do not force today's patterns.

### Activity: Classify Before You Code

Without writing code, label each sentence as **two pointers**, **sliding window**, or **neither**.

1. Find two numbers in a **sorted** list that add to `target`.
2. Longest substring with **at most 2** different characters.
3. Maximum **subsequence** sum (items may skip neighbours).
4. Move all zeroes to the end **in place**, keeping the order of non-zero values.
5. Count subarrays whose sum equals `k` when the list may contain **negatives**.
6. Maximum sum of any **k consecutive** elements.

Suggested labels: (1) two pointers, (2) sliding window, (3) neither, (4) two pointers, (5) neither for a window, (6) sliding window.

If an AI tool marks (5) as sliding window, that is a useful mismatch to debate. **Negative** numbers break the idea "shrink left to make the sum smaller."

---

## Reverse a List in Place

You now have the pattern map. The first program is a warm-up so you can **see** two pointers move, meet, and stop — with no extra constraint yet.

- **Official Definition:** An **in-place** algorithm updates the original list and uses only a small constant amount of extra memory.
- **In Simple Words:** You rearrange the same row of seats. You do not book a second row.
- **Real-Life Example:** Two students stand at the two ends of a bench and swap water bottles until they meet in the middle. The bench is reversed. No extra bench is needed.

```text
letters = ['h', 'e', 'l', 'l', 'o']
            L                   R     swap → o e l l h
              L               R       swap → o l l e h
                L           R         L and R meet, stop
```

**Common doubt:** Why is the loop `left < right` and not `left <= right`? For an odd-length list the middle item should stay put. Swapping an index with itself is wasted work, not an error.

Open **[OneCompiler Python](https://onecompiler.com/python)** or a local `.py` file, paste the program, and run it.

```python
def reverse_in_place(arr):  # define a function that reverses a list using two indices
    left = 0  # left pointer starts at the first index
    right = len(arr) - 1  # right pointer starts at the last index
    while left < right:  # continue until the two pointers meet or cross
        arr[left], arr[right] = arr[right], arr[left]  # swap the values at left and right
        left = left + 1  # move left one step toward the centre
        right = right - 1  # move right one step toward the centre
    return arr  # the same list is now reversed; return it so you can print it


letters = ["h", "e", "l", "l", "o"]  # sample list of characters
print(reverse_in_place(letters))  # expected output: ['o', 'l', 'l', 'e', 'h']
```

**How the code works**

- `left` and `right` start at the two ends and walk toward each other.
- Each swap places one pair of characters into their final positions.
- The loop visits each index at most once, so the time is **O(n)** and extra memory is **O(1)**.
- `arr[::-1]` also reverses, but it builds a **new** list. This version edits the original.

### Activity: Trace on Paper First

Copy `["I", "N", "D", "I", "A"]` onto paper. Mark L and R. Write the list after every swap. Then run the program and check that both traces match.

---

## Finding a Pair Sum on a Sorted List

Reversing shows pointers moving. The next problem shows **why** you move only one pointer: the list is sorted, so the sum tells you the direction.

**Problem:** You are given a **sorted** list of numbers and a **target**. Find two different positions whose values add to the target. Many platforms number positions from **1**, not from 0.

```text
numbers = [2, 7, 11, 15],  target = 18

L=2, R=15  sum=17  too small  → move L right
L=7, R=15  sum=22  too big    → move R left
L=7, R=11  sum=18  match      → positions 2 and 3 (1-based)
```

**Logic:** If the current sum is too small, moving `right` left would make it even smaller, so that move cannot help. You must move `left` right. The opposite holds when the sum is too big.

```python
def two_sum_sorted(numbers, target):  # find two 1-based positions that add to target
    left = 0  # start at the smallest value
    right = len(numbers) - 1  # start at the largest value
    while left < right:  # the two positions must be different
        total = numbers[left] + numbers[right]  # current pair sum
        if total == target:  # found the required pair
            return [left + 1, right + 1]  # convert 0-based indices to 1-based positions
        if total < target:  # sum is too small, need a larger left value
            left = left + 1  # move left toward bigger numbers
        else:  # sum is too big, need a smaller right value
            right = right - 1  # move right toward smaller numbers
    return []  # no pair found (the usual statement promises exactly one pair)


print(two_sum_sorted([2, 7, 11, 15], 18))  # expected output: [2, 3]
```

**How the code works**

- Each step moves exactly one pointer, so the loop runs at most **n** times.
- Because the list is sorted, "too small" and "too big" have only one legal repair.
- Extra memory is **O(1)**. You do not build a dictionary of seen values.

Compare with the nested baseline on the **same** input:

```python
def two_sum_brute(numbers, target):  # nested-loop version for the same pair-sum problem
    n = len(numbers)  # store the length once
    for i in range(n):  # choose the first index
        for j in range(i + 1, n):  # choose a later second index
            if numbers[i] + numbers[j] == target:  # check this pair
                return [i + 1, j + 1]  # 1-based positions, same as the fast version
    return []  # no pair found


print(two_sum_brute([2, 7, 11, 15], 18))  # expected output: [2, 3] — same answer, more work
```

**How the code works**

- The inner loop rechecks many pairs that two pointers would never need.
- For `n = 4` both programs print `[2, 3]`. For large **n**, the nested version is **O(n²)** and the pointer version is **O(n)**.

### Activity: One Input, Two Methods

Run both functions on `[1, 2, 3, 4, 6]` with target `6`. Confirm they print the same positions. Then write one sentence: "The nested version is slower because ____."

---

## Removing Duplicates from a Sorted List

Pair-sum used opposite ends. Duplicate removal uses the **chase** shape: fast reads everything, slow writes the unique prefix.

**Problem:** The list is **sorted**, so duplicates sit next to each other. Overwrite the list so the first **k** positions are unique. Return **k**. Do not build a second list.

```text
nums = [0, 0, 1, 1, 1, 2]
slow stays on the last kept unique value
fast walks: 0, 0, 1, 1, 1, 2
when nums[fast] != nums[slow]: move slow, copy nums[fast] there
unique prefix: [0, 1, 2, ...]   k = 3
```

```python
def remove_duplicates(nums):  # compact unique values to the front of a sorted list
    if not nums:  # empty list has no unique values
        return 0  # unique count is zero
    slow = 0  # slow is the index of the last unique value kept so far
    for fast in range(1, len(nums)):  # fast inspects every later index
        if nums[fast] != nums[slow]:  # a new unique value has appeared
            slow = slow + 1  # open the next slot in the unique prefix
            nums[slow] = nums[fast]  # copy the new unique value into that slot
    return slow + 1  # unique count is the last kept index plus one


sample = [0, 0, 1, 1, 1, 2]  # sorted list with duplicates
k = remove_duplicates(sample)  # compact in place and receive the unique count
print(k, sample[:k])  # expected output: 3 [0, 1, 2]
```

**How the code works**

- Fast always moves. Slow moves only when a **new** value appears.
- After the loop, values after index `k - 1` do not matter. Only the prefix of length **k** is the answer.
- Time is **O(n)**. Extra space is **O(1)**.

**Common doubt:** "Why not use `set(nums)`?" A set does not promise the original sorted order in every Python version's mental model for interviews, and it uses extra memory. The pointer version edits the same list.

### Activity: Dry Run

On paper, fill `slow` and `fast` for `[7, 7, 7, 8, 8, 9]`. Write the list after every copy. You should finish with prefix `[7, 8, 9]` and `k = 3`.

---

## Best Engagement Stretch (Fixed Window)

You can now compact and hunt pairs. The next pattern keeps a **contiguous** block of fixed length — the cardboard frame from the kirana example, applied to a music session.

A product team wants the highest-engagement block of **k consecutive plays** in a user's session. That block can power a "Your recent vibes" row, or an A/B test on queue quality.

Model each play as a score from 0 to 100:

| Signal | Score idea |
|---|---|
| Skip under 30 seconds | 0 |
| Played 30 seconds or more, but incomplete | 40–70 |
| Full listen | 80–90 |
| Full listen and save or like | 100 |

**Problem:** Given `scores` and `k`, return the **maximum sum** of any contiguous subarray of length **k**.

```text
scores = [20, 90, 85, 10, 95, 88, 0, 70]
k = 3
```

Eyeballing the big numbers is tempting. `[95, 88, 0]` looks hot at 183, while `[90, 85, 10]` is 185, `[85, 10, 95]` is 190, and `[10, 95, 88]` is 193.

Those later windows are interesting, but they are not the full list. Write **every** window of length 3:

```text
[20, 90, 85] = 195
[90, 85, 10] = 185
[85, 10, 95] = 190
[10, 95, 88] = 193
[95, 88,  0] = 183
[88,  0, 70] = 158
```

The maximum is **195**, from `[20, 90, 85]`. The lesson is the same as the nested-loop waste: humans skip windows; a loop does not.

Now slide a running total instead of resumming:

```text
start with 20+90+85 = 195     best = 195
drop 20, add 10  → 185        best = 195
drop 90, add 95  → 190        best = 195
drop 85, add 88  → 193        best = 195
drop 10, add  0  → 183        best = 195
drop 95, add 70  → 158        best = 195
```

```python
def max_sum_k_brute(scores, k):  # nested-style baseline: resum every window of length k
    n = len(scores)  # store the length
    if k > n or k <= 0:  # a window cannot be longer than the list, or empty
        return 0  # no valid window exists
    best = float("-inf")  # start below any possible sum
    for i in range(n - k + 1):  # every valid starting index
        total = sum(scores[i : i + k])  # add k values from scratch
        if total > best:  # keep the larger sum
            best = total  # update the answer
    return best  # maximum window sum


def max_sum_k_window(scores, k):  # fixed sliding window: reuse the previous sum
    n = len(scores)  # store the length
    if k > n or k <= 0:  # guard the same edge cases as the baseline
        return 0  # no valid window exists
    window_sum = sum(scores[:k])  # sum of the first window
    best = window_sum  # that sum is the best so far
    for i in range(k, n):  # i is the new right end of the window
        window_sum = window_sum + scores[i] - scores[i - k]  # add entering value, drop leaving value
        if window_sum > best:  # compare with the best sum seen
            best = window_sum  # update if this window is better
    return best  # maximum sum of any k consecutive scores


scores = [20, 90, 85, 10, 95, 88, 0, 70]  # engagement scores from the session story
print(max_sum_k_brute(scores, 3))  # expected output: 195
print(max_sum_k_window(scores, 3))  # expected output: 195 — same answer, less work
```

**How the code works**

- Both functions return **195** on this input, so you can trust the fast version against the baseline.
- The brute version calls `sum` on k elements for every start. That is about **O(n · k)** additions.
- The window version pays one full sum, then one add and one subtract per step. That is **O(n)**.
- If `k` is larger than the list, both return `0`. That edge case is easy to forget and crash on `sum(scores[:k])` without a guard.

### Activity: Compare the Two Functions

Add a counter of additions inside both functions (each `+` of a score counts as one). Run them on this `scores` list with `k = 3`. You should see many more additions in the brute version.

---

## Longest No-Skip Streak (Variable Window)

A fixed window always covers **k** plays. The next product question lets the length change: how long can the user stay "in the zone"?

Find the longest consecutive run of plays **without an early skip**. Session-quality tools use this streak to ask whether the radio mix is still working.

Each value in `plays` is **seconds listened**. Treat a play as a skip when it is under **30** seconds.

```text
plays = [45, 120, 12, 200, 95, 8, 150, 180, 210]
skip if seconds < 30
streaks of non-skips: [45, 120] length 2 | [200, 95] length 2 | [150, 180, 210] length 3
answer: 3
```

This is the **resetting** form of a variable window. The window is valid while every play is a non-skip. A skip collapses the window to empty.

```text
plays:  45  120  12  200  95   8  150  180  210
skip?:   n    n   Y    n   n   Y    n    n    n
streak:  1    2   0    1   2   0    1    2    3
best:    1    2   2    2   2   2    2    2    3
```

```python
def longest_no_skip_streak(plays, threshold=30):  # longest run of plays that are not early skips
    best = 0  # longest valid streak seen so far
    streak = 0  # current valid streak ending at this play
    for seconds in plays:  # walk the session in order
        if seconds >= threshold:  # this play is not an early skip
            streak = streak + 1  # grow the current window by one
            if streak > best:  # compare with the best streak
                best = streak  # update the answer
        else:  # this play is an early skip
            streak = 0  # the window collapses; start again after this skip
    return best  # length of the longest no-skip run


plays = [45, 120, 12, 200, 95, 8, 150, 180, 210]  # seconds listened, in order
print(longest_no_skip_streak(plays))  # expected output: 3
```

**How the code works**

- `streak` is the current window length. `best` remembers the longest window.
- A skip does not shrink by one. It resets, because one skip breaks the "no early skip" rule completely.
- Time is **O(n)**. Extra space is **O(1)**.

The next problem uses the same grow-and-shrink idea, but you can no longer reset to zero on a single "bad" item. A **repeat character** is only bad **inside the current window**. You must drop items from the left until that repeat is gone.

### Activity: Mark the Streaks

On paper, underline every non-skip in `plays`. Write the three streak lengths. Confirm the longest is 3 before you run the program.

---

## Longest Substring Without Repeating Characters

The no-skip streak used a yes/no rule on each item. Many string problems use a rule on the **whole window**: every character inside it must be unique.

**Problem:** Given a string `s`, return the length of the longest **substring** (contiguous) that contains no repeating character.

```text
s = "abcabcbb"

window grows: a | ab | abc          length 3
next is a, which is already inside  drop left a → bca
next is b, already inside           drop left b → cab
next is c, already inside           drop left c → abc
next is b, already inside           drop until unique → cb, then b
best length = 3
```

- **Official Definition:** A **set** is a collection of unique values with fast "is this already inside?" checks.
- **In Simple Words:** A set is an attendance notebook of characters currently inside the window. A character cannot be written twice.
- **Real-Life Example:** A railway coach window that may not contain two passengers with the same berth tag. If a duplicate tag arrives, passengers leave from the left until that tag is free.

```python
def length_of_longest_substring(s):  # longest contiguous unique-character substring
    seen = set()  # characters currently inside the window
    left = 0  # left edge of the window
    best = 0  # best length seen so far
    for right in range(len(s)):  # right edge grows one character at a time
        current = s[right]  # character that wants to enter
        while current in seen:  # window is invalid until this character is unique
            seen.remove(s[left])  # drop the leftmost character from the set
            left = left + 1  # shrink the window from the left
        seen.add(current)  # the new character is now unique; include it
        length = right - left + 1  # current valid window length
        if length > best:  # compare with the best length
            best = length  # update the answer
    return best  # length of the longest unique substring


print(length_of_longest_substring("abcabcbb"))  # expected output: 3
print(length_of_longest_substring("bbbbb"))  # expected output: 1
print(length_of_longest_substring("pwwkew"))  # expected output: 3
```

**How the code works**

- `right` walks the string once. `left` only moves forward, never backward.
- The inner `while` does **not** make this O(n²), because `left` across the whole run moves at most **n** times.
- `right - left + 1` is the length. Forgetting the `+ 1` is a common off-by-one error.
- Extra space is the set, at most the size of the alphabet in the string.

A nested baseline starts at every `i` and grows `j` until a duplicate. It is easier to invent and **O(n²)**. Run both on `"abcabcbb"` and confirm they agree.

### Activity: Trace `"pwwkew"`

Draw a row of characters. Under it, write the window after every `right` step. You should see windows such as `pw`, then `w`, then `wke`, then `kew`. The best length is 3.

---

## Checking a Palindrome with Two Pointers

Windows handle contiguous **sums** and **constraints**. Two pointers from the ends also handle a classic string question: does this sentence read the same forwards and backwards, if you ignore spaces and punctuation?

**Problem:** Return `True` if `s` is a palindrome after skipping non-alphanumeric characters and ignoring case.

```text
"A man, a plan, a canal: Panama"
compare A and a, m and m, a and a, ... until the pointers meet
```

```python
def is_palindrome(s):  # true if s is a palindrome ignoring spaces, punctuation, and case
    left = 0  # start at the first character
    right = len(s) - 1  # start at the last character
    while left < right:  # stop when the pointers meet
        while left < right and not s[left].isalnum():  # skip symbols from the left
            left = left + 1  # move left to the next character
        while left < right and not s[right].isalnum():  # skip symbols from the right
            right = right - 1  # move right to the previous character
        if s[left].lower() != s[right].lower():  # compare letters in lowercase
            return False  # one mismatch means it is not a palindrome
        left = left + 1  # this pair matched; move inward from the left
        right = right - 1  # this pair matched; move inward from the right
    return True  # all compared pairs matched


print(is_palindrome("A man, a plan, a canal: Panama"))  # expected output: True
print(is_palindrome("race a car"))  # expected output: False
```

**How the code works**

- The inner loops only skip junk characters. They do not change the palindrome logic.
- `.lower()` makes `"A"` and `"a"` equal.
- Time is **O(n)**. Extra space is **O(1)**. Building a cleaned copy of the string also works, but uses extra memory.

### Activity: Optional Second Pair Problem

Heights of walls: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`. The water a pair of walls can hold is `min(left_height, right_height) * (right_index - left_index)`.

Start at the two ends. At every step, move the pointer at the **shorter** wall, because width always shrinks and only a taller limiting wall can improve the area.

On paper, the best area for this input is **49**. If you finish early, code the same two-pointer loop and print `49`.

---

## Smallest Window That Covers a Target String

The unique-substring problem asked for the **longest** valid window. The covering problem asks for the **shortest** valid window.

**Problem:** Given strings `s` and `t`, return the smallest substring of `s` that contains every character of `t`, including duplicates. If no such substring exists, return the empty string.

Idea:

1. Grow `right` until the window **covers** `t`.
2. Then shrink `left` as far as you can while the window still covers `t`.
3. Remember the smallest such window. Repeat.

You keep a **need** count for characters in `t` and a `missing` counter so "covers `t`" is a cheap check. Extra copies in the window push `need` negative and do not change `missing`.

```python
from collections import Counter  # Counter builds a frequency dictionary from a string


def min_window(s, t):  # smallest substring of s that covers every character of t
    if not t or not s:  # empty target or empty source cannot form a covering window
        return ""  # return the empty string
    need = Counter(t)  # how many times each character of t must appear
    missing = len(t)  # how many required character copies are still missing
    left = 0  # left edge of the search window
    best_left = 0  # start index of the smallest covering window found
    best_len = float("inf")  # length of that window; inf means none found yet
    for right, ch in enumerate(s):  # grow the right edge across s
        if need[ch] > 0:  # this character is still required
            missing = missing - 1  # one required copy has been supplied
        need[ch] = need[ch] - 1  # consume one copy (goes negative for extras)
        while missing == 0:  # current window covers t; try to shrink it
            width = right - left + 1  # current covering window length
            if width < best_len:  # this covering window is the smallest so far
                best_len = width  # remember the new best length
                best_left = left  # remember the new best start
            left_ch = s[left]  # character that will leave if we shrink
            need[left_ch] = need[left_ch] + 1  # put that copy back into the need account
            if need[left_ch] > 0:  # the window no longer covers t
                missing = missing + 1  # one required copy is missing again
            left = left + 1  # shrink from the left
    if best_len == float("inf"):  # never found a covering window
        return ""  # return empty string
    return s[best_left : best_left + best_len]  # slice out the smallest covering window


print(min_window("ADOBECODEBANC", "ABC"))  # expected output: BANC
```

**How the code works**

- `need[ch] > 0` means `t` still requires this character. Extra copies push `need` negative and do not change `missing`.
- The inner `while` shrinks only while the window is still covering, which is the **shortest valid** flavour.
- Time is **O(n)**. Extra space is the alphabet used in `t`.

Trace `"ADOBECODEBANC"` and `"ABC"` on paper until you see `BANC`. Then run the program.

---

## Checking Edge Cases with Pytest

A pattern that works on the classroom example can still fail on an empty list, a single item, all duplicates, or a window longer than the list. **Pytest** is the tool you use to lock those cases.

- **Official Definition:** **Pytest** is a Python testing framework that runs functions named `test_...` and reports whether each `assert` passed.
- **In Simple Words:** Pytest is a checklist robot. You write expected answers. It reruns them after every change.
- **Real-Life Example:** Before a local train leaves, a guard does not "feel" that the doors are fine. A fixed checklist is checked every time, including the boring cases.

Copy these four functions into a file named `patterns.py`: `max_sum_k_window`, `longest_no_skip_streak`, `length_of_longest_substring`, and `remove_duplicates`. Save the tests below as `test_patterns.py` in the same folder. From that folder, run `pytest -q`.

```python
from patterns import (  # import the functions you wrote in patterns.py
    max_sum_k_window,  # fixed window maximum sum
    longest_no_skip_streak,  # variable window skip streak
    length_of_longest_substring,  # unique substring length
    remove_duplicates,  # in-place unique prefix
)


def test_max_sum_empty():  # empty list has no window
    assert max_sum_k_window([], 3) == 0  # expect zero


def test_max_sum_single():  # one element and k = 1 is that element
    assert max_sum_k_window([42], 1) == 42  # expect 42


def test_max_sum_window_larger_than_array():  # k cannot exceed the list
    assert max_sum_k_window([1, 2, 3], 5) == 0  # expect zero


def test_max_sum_engagement_example():  # classroom music-session example
    scores = [20, 90, 85, 10, 95, 88, 0, 70]  # engagement scores
    assert max_sum_k_window(scores, 3) == 195  # first window is the best


def test_no_skip_all_skips():  # every play is an early skip
    assert longest_no_skip_streak([10, 8, 0]) == 0  # expect zero


def test_no_skip_case_study():  # classroom no-skip example
    plays = [45, 120, 12, 200, 95, 8, 150, 180, 210]  # seconds listened
    assert longest_no_skip_streak(plays) == 3  # longest run is three full-ish plays


def test_longest_substring_all_duplicates():  # string of one repeated character
    assert length_of_longest_substring("aaaa") == 1  # expect one


def test_remove_duplicates_all_same():  # sorted list where every value is identical
    nums = [7, 7, 7, 7]  # all duplicates
    k = remove_duplicates(nums)  # compact in place
    assert k == 1  # only one unique value
    assert nums[0] == 7  # that value is 7
```

**How the code works**

- Each function name starts with `test_`, so Pytest collects it automatically.
- `assert` compares the function output with the expected value and fails the test on a mismatch.
- These eight cases cover empty input, a single element, all duplicates, and a window larger than the array — the edges nested-loop demos usually skip.

### Activity: Run the Checklist

From the folder that contains both files, run:

```bash
pytest -q  # run all tests quietly and show a short pass/fail summary
```

If a test fails, read the assertion. Fix the function, not the expected number, unless you find a genuine mistake in the expected value.

---

## Classifying New Problems with an AI Tool

You have implemented the patterns. The last classroom skill is to **name** the pattern from English alone, including when the answer is **neither**.

Open Cursor or ChatGPT and paste:

> Classify each of these 6 statements as two pointers, sliding window, or neither. Write one sentence why. Do not write code.

Then paste the six statements from the "Classify Before You Code" activity. Compare the model's labels with the suggested labels in that activity.

When the model disagrees, do not copy its label blindly. Check the contiguous test, the fixed-width test, and whether negatives are allowed. The debate is the learning.

---

## Extra Practice

After class, name the pattern first, trace a small input on paper, then code. Do not open an editorial until you have a trace.

| Problem | Pattern to try | What to notice |
|---|---|---|
| [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/) | Fixed window plus a frequency map | Width is always `k`, **and** every value in the window must be unique. Record a sum only when both are true. Return `0` if none exist. |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/) | Prefix sums plus a dictionary — **not** a window if negatives are allowed | Contiguous, yes. Shrink-left is unsafe when a value can be negative. |
| [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Variable window, at most 2 distinct values | Longest subarray with at most two different numbers. |
| [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | Variable window, at most `k` zeroes | You may flip at most `k` zeroes. The window is valid while zeroes inside it are ≤ `k`. |
| [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k) | Variable window (values are positive) | While the product is too big, divide out `nums[left]`. Each new `right` adds `right - left + 1` valid subarrays. |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Variable window plus a set | Re-solve from a blank file using today's trace. |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | Variable window | You may change at most `k` characters. Valid while `window_length - max_frequency <= k`. |
| [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string) | Fixed window plus two frequency maps | Window size is `len(p)`. Record start indices where the maps match. |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) | Variable window, shortest valid | Grow until `t` is covered, shrink to the minimum, repeat. |

After you have traced by hand, reuse the two shapes you already coded:

- **Fixed window:** one full sum of the first `k` items, then add the entering value and drop the leaving value — the engagement-stretch program.
- **Variable window (longest valid):** grow `right`, shrink `left` until the constraint holds, then record `right - left + 1` — the unique-substring program.
- Replace the running summary with a **sum**, a **set**, a **product**, or a **frequency map**, depending on the constraint.
- If you catch yourself moving `left` backwards, the O(n) guarantee is gone.

---

## Key Takeaways

- Nested loops are the natural first translation of "check every pair or stretch." They waste work when consecutive checks share almost the same items, and that waste becomes painful as **n** grows.
- **Two pointers** are two coordinated indices. They meet in the middle on **sorted** pair problems and palindromes, or chase from the same side when you compact a list **in place**.
- A **sliding window** is a contiguous `[left, right]` frame. **Fixed** windows keep length `k`. **Variable** windows grow and shrink with a constraint. Neither index should move backwards.
- Sorting unlocks two pointers only when **values** matter. If the answer must stay in the **original order**, sorting destroys the window.
- Name the pattern from keywords before you code: pair sum, longest substring, maximum of every k, or **neither**. Then compare your O(n) scan with a nested baseline on a small input.

This habit continues into later problem-solving work, where you will meet search problems that try a choice, explore, and undo. The first question stays the same: what is the pattern, and why does each pointer move?

---

## Important Commands, Libraries, and Terminologies

| Term | What it means | Analogy |
|---|---|---|
| **Nested loop** | A loop inside a loop; work often grows like n × n | Comparing every student with every other student |
| **O(n)** | Work grows in a straight line with n | One walk along a playlist |
| **O(n²)** | Work grows like n times n | Rechecking every pair |
| **O(n log n)** | Typical cost of sorting, then a cheaper scan | Arrange the chart, then walk it once |
| **Pointer** | An index you move with a rule | A finger on a reservation chart |
| **Two pointers** | Two coordinated indices | Friends at two ends of a sorted list |
| **In-place** | Edit the original list with little extra memory | Swap bottles on the same bench |
| **Slow / fast pointers** | Fast reads; slow writes the useful prefix | A scout and a clerk |
| **Contiguous / subarray / substring** | Neighbours in the original order | Consecutive songs, not a shuffled mix |
| **Sliding window** | A `[left, right]` frame that only crawls right | Kirana combo frame on a shelf |
| **Fixed-size window** | Length always k | Best 3 consecutive plays |
| **Variable-size window** | Length changes with a constraint | Longest no-skip streak |
| **Constraint** | The rule that makes a window valid or invalid | "No early skip" or "all characters unique" |
| **Set** | Unique values with fast membership tests | Attendance notebook inside the window |
| **Dictionary / map / Counter** | Keys to counts or last-seen indices | A tally of characters needed |
| **Prefix sum** | Running totals used when a window is the wrong tool | A different pattern if negatives appear |
| **Pytest** | Runs `test_...` functions and `assert` checks | A guard's door checklist |
| **Edge case** | Empty input, one item, all duplicates, k larger than n | The boring rows a demo skips |
| **`python3`** | Command to run Python 3 programs | The engine that executes your `.py` file |
| **`pytest -q`** | Quiet test run | Short pass/fail summary |
| **OneCompiler** | Browser tool to paste and run Python | [https://onecompiler.com/python](https://onecompiler.com/python) |
