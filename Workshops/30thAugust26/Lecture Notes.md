# Sliding Window Problem Solving

## What You Will Learn in This Session

In the **previous** session you learned **sliding window** as a pattern: a contiguous stretch of an array or string, scanned with two indices that only move forward. You saw two families — a **fixed** window whose length is always `k`, and a **variable** window whose length grows and shrinks with a rule.

That session built the picture. This session trains the **hand**: you will read a LeetCode-style statement, name the window, reject a nested-loop first draft when the input is large, then write an **O(n)** scan.

You already know **loops**, **lists**, **if/else**, and how to write a **function**. Today you will add a **set**, a **frequency map**, and a **frequency array of 26 letters**.

You will learn:

- What a **subarray** is, and why a pick that skips neighbours is not a subarray.
- Why a triple nested check is too slow when **n** is around **1,00,000**.
- How a **fixed window** moves: exclude the left value, include the new right value.
- How a **variable window** moves: expand `end` until the rule holds, then shrink `start` from the left.
- When a **set** is not enough and you need **counts**.
- How **anagrams** become “two frequency lists of length 26 are equal.”

By the end, you will look at a problem and say: “fixed window plus a map” or “variable window, shrink from the left” — then code it.

The programs below are in **Python**. The same steps work in C++, Java, or any language you use on LeetCode.

---

## What Is a Subarray

Almost every problem today asks for a **subarray** (or a **substring**, which is the same idea on a string). If this word is fuzzy, the rest of the session will feel like guessing.

- **Official Definition:** A **subarray** is a contiguous, non-empty sequence of elements taken from an array. Neighbours in the subarray were neighbours in the original array.
- **In Simple Words:** You keep a straight slice. You do not jump over a stall in the middle.
- **Real-Life Example:** Five consecutive shops on a market street — shop 2, 3, 4 — are a subarray. Shop 2 and shop 5 with the middle ones skipped are not.

Take this row:

```text
array = [1, 5, 4, 2, 9, 9, 9]
```

Which of these picks are subarrays?

| Pick | Subarray? | Why |
|---|---|---|
| `[1]` | Yes | One cell is contiguous. |
| `[1, 5]` | Yes | Neighbours. |
| `[5, 4]` | Yes | Neighbours. |
| `[5, 4, 2]` | Yes | Three neighbours in order. |
| `[4, 2, 9]` | Yes | Neighbours. |
| `[5, 9, 9, 9]` | **No** | After `5` the next values are `4` and `2`. Those were skipped. |

![Seven market stalls numbered 1, 5, 4, 2, 9, 9, 9 — a teal frame marks 5, 4, 2 as a valid subarray of neighbours; a red dashed jump from 5 to the 9s is labelled not a subarray](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/workshops/30th-august-26/workshop-30aug26-01-subarray-vs-skipped.png?v=20260903)

**Common doubt:** “Are duplicate values allowed inside a subarray?” Yes. `[9, 9, 9]` is a valid subarray. A **problem** may later say “only count subarrays whose values are all distinct.” That is a **filter**, not a new definition of subarray.

### Activity: Tick the Valid Slices

On paper, copy `[1, 5, 4, 2, 9, 9, 9]` and tick every contiguous slice of length 3.

You should get five slices: `[1,5,4]`, `[5,4,2]`, `[4,2,9]`, `[2,9,9]`, `[9,9,9]`.

If you wrote `[1,4,2]`, you skipped a neighbour — that is not a subarray.

---

## Recap: Fixed Window and Variable Window

A sliding window is just a subarray whose two ends you move with a rule, instead of restarting the sum from scratch every time.

- **Official Definition:** A **sliding window** is a pair of indices `[left, right]` that describe the current subarray. Both indices only move to the right. The values between them are the current window.
- **In Simple Words:** Two fingers on the list. The right finger includes a new item. The left finger drops an old item when the rule says so.
- **Real-Life Example:** A photo frame sliding along a row of cricket jerseys. The frame always covers a contiguous run of jerseys. You never lift the frame and place it on jersey 1 and jersey 8 together.

Two shapes appear in today’s problems:

| Shape | Length | How it moves | Typical ask |
|---|---|---|---|
| **Fixed window** | Always `k` | Exclude left, include right, same width | Sum of every block of `k`, anagrams of a word of length `m` |
| **Variable window** | Changes | Expand `end`; shrink `start` while a rule holds (or until it holds) | Shortest subarray with sum ≥ target, longest unique substring |

**Need:** Consecutive windows share almost the same cells. Recounting them with a nested loop wastes work.

**Logic:** Keep a running **summary** of the window — a sum, a set, or a frequency list. Update the summary in **O(1)** when one item enters and one item leaves.

**Common error:** Moving `left` backwards “to try another option.” That turns an **O(n)** walk into nested work again.

---

## Why Nested Loops Fail for Large Inputs

Before any clever window, the honest first idea is: generate every subarray, check the condition, keep the best answer. That idea is often **correct**. It is often **too slow**.

- **Official Definition:** **Time complexity** describes how the running time grows as the input size **n** grows. **O(n²)** means the work grows roughly like **n × n**. **O(n)** means it grows roughly in a straight line with **n**.
- **In Simple Words:** If the list becomes 10 times longer, an **O(n)** scan becomes about 10 times heavier. An **O(n²)** nested check becomes about **100** times heavier.
- **Real-Life Example:** Checking every pair of students in a class of 10 is about 100 comparisons. In a class of 100 it is about 10,000. The hall did not grow 100 times. The work did.

A useful rule of thumb for coding platforms:

- If **n** can be **1,00,000** or **10,00,000**, an **O(n²)** solution will usually **time out**.
- Two nested loops that both walk the full array are **O(n²)**.
- A third loop that scans the cells between `i` and `j` makes it even heavier.

You do **not** need a full complexity course to use this rule. You only need to notice: “I have two or three loops over n, and n can be 1,00,000 — I must reuse the previous window instead of recounting.”

---

## Problem: Maximum Sum of Distinct Subarrays With Length K

Problem link: [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/)

This is the first classroom problem. It looks like a fixed window, plus one extra rule: the `k` values must all be **different**.

### The Statement

You are given an integer array `nums` and an integer `k`.

Return the **maximum sum** among all subarrays that satisfy **both**:

- the length is exactly **k**
- every value in that subarray is **distinct**

If no such subarray exists, return **0**.

### Walk the Sample

```text
nums = [1, 5, 4, 2, 9, 9, 9],  k = 3
```

All subarrays of length 3:

| Subarray | Sum | All distinct? | Keep? |
|---|---|---|---|
| `[1, 5, 4]` | 10 | Yes | Yes |
| `[5, 4, 2]` | 11 | Yes | Yes |
| `[4, 2, 9]` | 15 | Yes | Yes — best so far |
| `[2, 9, 9]` | 20 | No — `9` twice | No |
| `[9, 9, 9]` | 27 | No | No |

The largest **kept** sum is **15**, not 27. The problem is not “maximum sum of length k.” It is “maximum sum of length k **with unique values**.”

Second sample: `nums = [4, 4, 4]`, `k = 3`. The only window is `[4, 4, 4]`, which is not distinct, so the answer is **0**.

**Need:** For every window of length `k`, you must know **which values** sit inside it and **how many times** each value appears.

### Brute Force That You Should Be Able to Picture

Place `i` at the start of a window and `j` at `i + k - 1`. That pair is one window of length `k`. Then scan from `i` to `j` to test uniqueness and to add the sum.

```text
i = 0, j = 2  →  [1, 5, 4]
i = 1, j = 3  →  [5, 4, 2]
i = 2, j = 4  →  [4, 2, 9]
i = 3, j = 5  →  [2, 9, 9]
i = 4, j = 6  →  [9, 9, 9]
```

If you instead let `j` run from `i` all the way to `n - 1`, most of those slices are **longer than k**. You do not need them. Both ends must move together.

```python
def maximum_subarray_sum_brute(nums, k):  # nested check of every window of length k
    n = len(nums)  # store the length once
    best = 0  # 0 is the answer when no valid window exists
    for i in range(n - k + 1):  # i is the left end of a window of length k
        window = nums[i : i + k]  # slice of exactly k cells
        if len(set(window)) == k:  # a set drops duplicates; size k means all unique
            total = sum(window)  # add the k values
            if total > best:  # keep the largest valid sum
                best = total  # update the answer
    return best  # 0 if nothing valid was found


print(maximum_subarray_sum_brute([1, 5, 4, 2, 9, 9, 9], 3))  # expected output: 15
print(maximum_subarray_sum_brute([4, 4, 4], 3))  # expected output: 0
```

**How the code works**

- Each `i` is one window. `set(window)` has size `k` only when the k values are unique.
- The answer starts at `0` so a list with no valid window still returns `0`.
- For every window you rebuild the set and the sum from scratch. That is **O(n × k)** work. When **n** is **1,00,000**, this is not acceptable.

### Sliding the Same Window

Look at the move from `[1, 5, 4]` to `[5, 4, 2]`. You do **not** need to add `5` and `4` again.

- **Exclude** `1` (the value that left).
- **Include** `2` (the value that entered).

From `[5, 4, 2]` to `[4, 2, 9]`: exclude `5`, include `9`. That is the whole fixed-window move.

![Fixed window of length 3 sliding from 1, 5, 4 to 5, 4, 2 — a red arrow drops 1 on the left and a green arrow adds 2 on the right so 5 and 4 are not added again](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/workshops/30th-august-26/workshop-30aug26-02-fixed-window-slide.png?v=20260903)

- **Official Definition:** A **set** stores unique values only. Inserting a value that is already present does not create a second copy.
- **In Simple Words:** A set is an attendance register. A name is either in the book or it is not.
- **Real-Life Example:** If “Asha” is already marked present, marking “Asha” again does not make two Ashas.

**Claim:** If you insert the `k` values of a window into a set, and **all** of them are unique, the set’s size will be **k**. If any value repeats, the size will be **smaller than k**.

That claim is true for **one** snapshot of a window. It becomes dangerous when you **slide**, because a set has no count.

Suppose the window is `[1, 2, 1]` and the left `1` leaves. If you `set.remove(1)`, the remaining window still holds a `1`, but the set has already forgotten it.

A set cannot tell “one copy left” from “zero copies left.”

**Logic:** Store **frequencies** (how many times each value appears), not only presence. When the map has **exactly k keys**, every value in a window of length k appears once.

- **Official Definition:** A **frequency map** (Python `dict` or `Counter`) maps each value to the number of times it currently sits in the window.
- **In Simple Words:** A tally sheet. `9` might appear twice. The sheet says `9 → 2`, not merely “9 is present.”
- **Real-Life Example:** A kirana shopkeeper’s daily tally: two packets of atta, one packet of sugar. Crossing out “atta” once still leaves one packet on the shelf.

```python
from collections import defaultdict  # dict that starts missing keys at 0


def maximum_subarray_sum(nums, k):  # maximum sum of a distinct window of length k
    freq = defaultdict(int)  # count of each value currently inside the window
    window_sum = 0  # running sum of the current window
    best = 0  # best valid sum found so far; 0 if none
    for i, value in enumerate(nums):  # i is the right end; value is nums[i]
        freq[value] = freq[value] + 1  # include the new right value in the tally
        window_sum = window_sum + value  # include it in the sum
        if i >= k:  # the window is now longer than k, so drop the left value
            left_value = nums[i - k]  # the value that just left the window
            freq[left_value] = freq[left_value] - 1  # one fewer copy in the tally
            window_sum = window_sum - left_value  # remove it from the sum
            if freq[left_value] == 0:  # no copies of this value remain
                del freq[left_value]  # drop the key so len(freq) is the distinct count
        if i >= k - 1 and len(freq) == k:  # window is full and all k values are unique
            if window_sum > best:  # this valid sum is better than what we had
                best = window_sum  # remember it
    return best  # 0 if no window was both length k and distinct


print(maximum_subarray_sum([1, 5, 4, 2, 9, 9, 9], 3))  # expected output: 15
print(maximum_subarray_sum([4, 4, 4], 3))  # expected output: 0
```

**How the code works**

- Each index `i` is visited once. Include `nums[i]`. When `i >= k`, exclude `nums[i - k]`.
- `len(freq) == k` means the current k cells hold k different keys, so they are distinct.
- Deleting a key whose count hit 0 is required. If you leave `9 → 0` in the map, `len(freq)` lies.
- Time is **O(n)**. Extra space is the number of distinct values in a window, at most **k**.

Trace of the first sample (`k = 3`):

```text
i=0  include 1     freq={1:1}           sum=1    (window not full)
i=1  include 5     freq={1:1, 5:1}      sum=6
i=2  include 4     freq={1:1, 5:1, 4:1} sum=10   distinct → best=10
i=3  include 2, drop 1                  sum=11   distinct → best=11
i=4  include 9, drop 5                  sum=15   distinct → best=15
i=5  include 9, drop 4                  sum=20   keys={2,9} size 2 → skip
i=6  include 9, drop 2                  sum=27   keys={9} size 1 → skip
answer 15
```

### Activity: Finish the Tally on Paper

Copy the table above and add one blank column for `len(freq)`. Fill that column for every `i`. Circle the rows where `len(freq) == 3` — those circled sums should be 10, 11, and 15.

---

## Problem: Minimum Size Subarray Sum

Problem link: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

The previous problem had a **fixed** length `k`. This one does not. You must find the **shortest** contiguous stretch whose sum is **at least** a target — that is a **variable** window.

### The Statement

Given an array of **positive** integers `nums` and a positive integer `target`, return the **minimum length** of a subarray whose sum is **greater than or equal to** `target`. If no such subarray exists, return **0**.

Sample:

```text
nums = [2, 3, 1, 2, 4, 3],  target = 7
```

Some subarrays whose sum is at least 7:

| Subarray | Sum | Length |
|---|---|---|
| `[2, 3, 1, 2]` | 8 | 4 |
| `[3, 1, 2, 4]` | 10 | 4 |
| `[1, 2, 4]` | 7 | 3 |
| `[2, 4, 3]` | 9 | 3 |
| `[4, 3]` | 7 | **2** — shortest |

The answer is **2**.

### Nested Picture (Correct, Slow)

```text
for i from 0 to n-1:
    for j from i to n-1:
        sum the cells from i to j
        if that sum >= target:
            length = j - i + 1
            keep the smallest such length
```

**Common doubt:** Why is the length `j - i + 1`? Count the cells from index `i` through index `j`, including both ends — from 0 to 3 there are four cells, which is `3 - 0 + 1`.

This nested scan is **O(n²)** (or worse if you re-sum from `i` to `j` every time). The input size on the platform is large enough that you should not submit it.

### Two Claims That Unlock the Window

All values are **positive**. That fact is the engine. If a value could be negative, shrinking the left end would not reliably make the sum smaller.

**Claim 1 — stop expanding a window that is already valid.**

Grow from the left: `2` (too small), `2+3=5` (too small), `5+1=6` (too small), then `6+2=8` (≥ 7). You now have a valid window of length **l1**.

If you include one more value, the new length **l2** is bigger than **l1**, and you asked for the **minimum** length. There is no prize for a longer valid stretch.

**Claim 2 — once valid, try to shrink from the left.**

You may still drop prefix values if the sum **stays** ≥ target. That can only make the length smaller, which is what you want.

```text
window [3, 1, 2, 4], sum = 10, target = 7

drop left 3  →  [1, 2, 4] sum = 7   still valid, shorter — keep shrinking
drop left 1  →  [2, 4]    sum = 6   now too small — stop shrinking, expand again
```

![Variable window on 2, 3, 1, 2, 4, 3 with target 7 — expand until sum is at least 7, then move START right until the shortest valid slice 4, 3 of length 2](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/workshops/30th-august-26/workshop-30aug26-03-variable-window-shrink.png?v=20260903)

**Common error:** “I will look at both ends and drop whichever value is smaller.” That is **not** sliding window. The right end only **includes**; the left end only **excludes**.

If you remove from the right, you are walking an index backwards.

A short counter-example is `[10, 1, 1, 1]` with target `3`. The shortest valid slice is `[1, 1, 1]` on the right.

If you start from the whole array and always drop the smaller end, you nibble the `1`s on the right and can miss that slice. The legal move is: expand right, then shrink **left** while the sum is still enough.

### The O(n) Scan

Keep `start` at the left end, `end` at the right end, and `cur_sum` as the sum of `nums[start] … nums[end]`.

1. Include `nums[end]` and move `end` forward.
2. While `cur_sum >= target`, record `end - start + 1`, then exclude `nums[start]` and move `start` forward.
3. If you never found a valid window, return 0.

```python
def min_sub_array_len(target, nums):  # shortest subarray whose sum is at least target
    start = 0  # left end of the current window
    cur_sum = 0  # sum of nums[start] .. nums[end]
    ans = float("inf")  # “infinity” so the first valid length always wins
    for end in range(len(nums)):  # end is the right index we are including
        cur_sum = cur_sum + nums[end]  # expand: include the new right value
        while cur_sum >= target:  # the window is valid; try to make it shorter
            length = end - start + 1  # inclusive length of [start, end]
            if length < ans:  # this valid window is the shortest so far
                ans = length  # remember it
            cur_sum = cur_sum - nums[start]  # shrink: drop the left value from the sum
            start = start + 1  # move the left end one step right
    if ans == float("inf"):  # never entered the while loop with a valid window
        return 0  # the statement asks for 0 in that case
    return ans  # the shortest valid length


print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))  # expected output: 2
print(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # expected output: 0
```

**How the code works**

- `end` only increases. `start` only increases. Each index is included once and excluded at most once, so time is **O(n)**.
- The inner `while` is not a hidden **O(n²)** extra pass. `start` never resets to 0.
- Extra memory is **O(1)** — a few integers.

Dry run for `[2, 3, 1, 2, 4, 3]`, target `7`. Here `end` and `start` are **indices**:

```text
end=0 include 2   sum=2     2 < 7    no shrink
end=1 include 3   sum=5     5 < 7    no shrink
end=2 include 1   sum=6     6 < 7    no shrink
end=3 include 2   sum=8     8 >= 7   length=4, drop nums[0]=2, start=1, sum=6
end=4 include 4   sum=10    10 >= 7  length=4, drop nums[1]=3, start=2, sum=7
                      7 >= 7   length=3, drop nums[2]=1, start=3, sum=6
end=5 include 3   sum=9     9 >= 7   length=3, drop nums[3]=2, start=4, sum=7
                      7 >= 7   length=2, drop nums[4]=4, start=5, sum=3
done.  shortest length stored = 2
```

The window **moves**: include, include, include, then exclude, exclude, include, exclude, exclude. That motion is the pattern. The exact integers in a printout matter less than seeing “grow until valid, shrink from the left while valid.”

### Activity: One More Trace

On paper, run the same function on `nums = [1, 4, 4]`, `target = 4`. You should hit length **1** when the window is the first `4`. Then confirm by running the program.

---

## Problem: Sums of Every Window of Size K

After the variable-window problem, return to a **fixed** window with no extra uniqueness rule. This is the cleanest “exclude left, include right” drill.

A typical statement (GeeksforGeeks sliding-window article, and the same idea as [Max Sum Subarray of size K](https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1)): given an array and an integer `k`, compute the sum of **every** contiguous block of length `k`. You can print those sums, or keep only the maximum.

```text
arr = [1, 2, 3, 4, 5, 6],  k = 3

windows:  [1,2,3]=6   [2,3,4]=9   [3,4,5]=12   [4,5,6]=15
```

**Logic:** Sum the first `k` cells once. For every later index `start`, the new sum is:

```text
new_sum = old_sum - arr[start - k] + arr[start]
```

After the first loop, `start` sits at index `k` (the first index **not** yet included). Then `arr[start - k]` is the leftmost value of the previous window, and `arr[start]` is the new right value.

```text
first loop includes indices 0, 1, 2.  start is now 3.  k is 3.
start - k = 0  →  that is the 1 you must drop.
arr[start] = 4 →  that is the value you must add.
new sum = 6 - 1 + 4 = 9  which is 2+3+4.
```

**Common doubt:** “Should it be `start - k + 1`?” After the first window, `start` is already `k`, not `k - 1`. Subtract **k**, not `k - 1`. Check with the numbers above before you memorise the formula.

```python
def window_sums(arr, k):  # return the sum of every contiguous block of length k
    n = len(arr)  # length of the array
    if n < k or k <= 0:  # cannot form a window of length k
        return []  # no sums to report
    sums = []  # list of window sums in left-to-right order
    window_sum = 0  # running sum of the current window
    for i in range(k):  # build the first window of length k
        window_sum = window_sum + arr[i]  # include arr[0] .. arr[k-1]
    sums.append(window_sum)  # record the first window
    start = k  # first index that has not yet entered a finished window as the new right
    while start < n:  # slide until the right end walks off the array
        window_sum = window_sum - arr[start - k]  # exclude the leftmost value
        window_sum = window_sum + arr[start]  # include the new right value
        sums.append(window_sum)  # record this window
        start = start + 1  # move the right end one step
    return sums  # e.g. [6, 9, 12, 15]


print(window_sums([1, 2, 3, 4, 5, 6], 3))  # expected output: [6, 9, 12, 15]
```

**How the code works**

- The first `for` is **O(k)**. The `while` is **O(n - k)**. Together **O(n)**.
- You never rescan three cells to get 9, 12, or 15. You only patch the previous sum.
- To solve “maximum sum of size k”, replace `sums.append` with `best = max(best, window_sum)`.

### Activity: Index Arithmetic

On paper, after the first window of `[1, 2, 3, 4, 5, 6]` with `k = 3`, write the value of `start`. Then compute `start - k` for the next three slides. You should get left indices 0, then 1, then 2 — the values 1, 2, and 3 being dropped.

---

## Problem: Find All Anagrams in a String

Problem link: [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/)

The last classroom problem is still a **fixed** window. The window length is `len(p)`. The summary of the window is not a sum — it is a **letter tally**.

### What Is an Anagram

- **Official Definition:** Two strings are **anagrams** if they contain the same characters with the same frequencies, in any order.
- **In Simple Words:** Same letters, same counts, possibly shuffled.
- **Real-Life Example:** The tiles `A`, `B`, `C` can be arranged as `ABC`, `ACB`, `BAC`, `BCA`, `CAB`, `CBA`. All six are anagrams of each other.

Quick checks:

| Pair | Anagram? | Why |
|---|---|---|
| `AB` and `BA` | Yes | Same two letters. |
| `ABC` and `CBA` | Yes | One each of A, B, C. |
| `ant` and `anta` | No | Lengths differ. |
| `amit` and `amiat` | No | Lengths differ, and the letter bags differ. |

**First shard:** lengths must be equal. A longer string cannot be an anagram of a shorter one.

**Second shard:** every character’s count in A must match that character’s count in B.

### The Statement

Given strings `s` and `p`, return the **starting indices** of all substrings of `s` that are anagrams of `p`. The order of indices in the answer does not matter on LeetCode; a left-to-right list is natural.

```text
s = "cbaebabacd"
p = "abc"

CBA at index 0  is an anagram of ABC  →  0
BAC at index 6  is an anagram of ABC  →  6
answer [0, 6]
```

```text
s = "abab"
p = "ab"

AB at 0, BA at 1, AB at 2  →  [0, 1, 2]
```

**Claim:** every candidate substring in `s` must have length **equal to** `len(p)`. You only slide a window of that width.

If `p` is longer than `s`, no substring of `s` can be an anagram of `p`. Return an empty list immediately.

### Two Frequency Arrays of Length 26

English lowercase letters are 26 symbols. You can store counts in a list of 26 zeros. Index `0` is `a`, index `1` is `b`, …, index `25` is `z`.

- **Official Definition:** A **frequency array** of size 26 stores, at index `ord(ch) - ord('a')`, how many times that letter appears.
- **In Simple Words:** 26 counters in a row, one pigeonhole per letter.
- **Real-Life Example:** A cricket scorebook with 26 columns labelled A to Z. Each time you see a letter, you add a tally mark in its column.

Build `fp` from the whole of `p`. Build `fs` from the first window of `s`. If `fs == fp`, index `0` is an answer.

To slide from `cba` to `bae`:

- decrease the count of `c` (the letter that left)
- increase the count of `e` (the letter that entered)

Then compare `fs` with `fp` again. No need to rebuild either array from scratch.

```text
p = abc     fp = A:1 B:1 C:1  (and zeros elsewhere)

window cba  fs matches fp     → record 0
window bae  C dropped, E added → no match
window aeb  …                 → no match
…
window bac  fs matches fp     → record 6
```

```python
def find_anagrams(s, p):  # starting indices of anagrams of p inside s
    if len(p) > len(s):  # p cannot hide inside a shorter s
        return []  # empty answer
    fp = [0] * 26  # frequency of each letter in p
    for ch in p:  # scan every character of p
        fp[ord(ch) - ord("a")] = fp[ord(ch) - ord("a")] + 1  # one more tally for this letter
    wsize = len(p)  # window width equals the length of p
    fs = [0] * 26  # frequency of each letter in the current window of s
    for i in range(wsize):  # fill the first window s[0 .. wsize-1]
        fs[ord(s[i]) - ord("a")] = fs[ord(s[i]) - ord("a")] + 1  # tally the first window
    ans = []  # list of starting indices
    if fs == fp:  # first window is already an anagram
        ans.append(0)  # its start index is 0
    for i in range(wsize, len(s)):  # i is the new right index entering the window
        fs[ord(s[i]) - ord("a")] = fs[ord(s[i]) - ord("a")] + 1  # include s[i]
        left_ch = s[i - wsize]  # character that leaves the window
        fs[ord(left_ch) - ord("a")] = fs[ord(left_ch) - ord("a")] - 1  # exclude it
        if fs == fp:  # the window s[i-wsize+1 .. i] matches p
            ans.append(i - wsize + 1)  # record the new start index
    return ans  # all starting indices in left-to-right order


print(find_anagrams("cbaebabacd", "abc"))  # expected output: [0, 6]
print(find_anagrams("abab", "ab"))  # expected output: [0, 1, 2]
```

**How the code works**

- `fp` never changes after the first loop. `fs` is patched in **O(1)** per slide.
- Comparing two lists of 26 integers is **O(26)**, which is constant. Total time is **O(n)**.
- The start index of the window that **ends** at `i` is `i - wsize + 1`. Off-by-one here is the usual bug: using `i - wsize` records the left neighbour, not the start.
- Guard `len(p) > len(s)` before you index `s[i]` for `i` in `range(wsize)`. Otherwise you read past the end of `s`.

**Common error:** Forgetting the empty-answer guard when `p` is longer than `s`. The first window loop would then crash or read invalid indices.

### Activity: Patch One Slide by Hand

Write a 26-slot row for `abc` (only A, B, C are 1), then the row for window `cba`. Apply “C minus one, E plus one” and confirm the row no longer matches — that patch is the whole algorithm on one line of paper.

---

## Extra Practice on LeetCode

The four classroom problems are enough to see both shapes. The list below reuses the **same** two templates.

Name the pattern first, trace a tiny input on paper, then code.

### Fully Worked Extra: Maximum Average Subarray I

Problem link: [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/description/)

This is the fixed window of size `k` with a twist: you return the **maximum average**, not the maximum sum. For a constant `k`, the window with the largest **sum** is also the window with the largest **average**. Track the integer sum and divide **once** at the end.

```python
def find_max_average(nums, k):  # maximum average of any contiguous block of length k
    window_sum = 0  # running sum of the current window
    for i in range(k):  # first window
        window_sum = window_sum + nums[i]  # include nums[0] .. nums[k-1]
    best = window_sum  # best sum so far (average ranking matches sum ranking)
    for i in range(k, len(nums)):  # slide the right end
        window_sum = window_sum + nums[i] - nums[i - k]  # include right, exclude left
        if window_sum > best:  # this window sums higher
            best = window_sum  # keep it
    return best / k  # one division; k is a positive integer


print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # expected output: 12.75
```

**How the code works**

- Same include/exclude as the GeeksforGeeks window-sum drill.
- Dividing inside the loop is unnecessary and, in some languages, truncates. Python `/` is a float divide, but one divide at the end is still cleaner.

### Fully Worked Extra: Permutation in String

Problem link: [Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)

This is **Find All Anagrams** with a yes/no answer: does `s2` contain any anagram of `s1`? Same two frequency arrays. Return `True` on the first match.

```python
def check_inclusion(s1, s2):  # True if s2 contains any permutation (anagram) of s1
    if len(s1) > len(s2):  # a longer pattern cannot sit inside a shorter text
        return False  # no permutation possible
    fp = [0] * 26  # frequency of s1
    fs = [0] * 26  # frequency of the current window of s2
    wsize = len(s1)  # window width
    for ch in s1:  # fill fp
        fp[ord(ch) - ord("a")] = fp[ord(ch) - ord("a")] + 1  # tally s1
    for i in range(wsize):  # first window of s2
        fs[ord(s2[i]) - ord("a")] = fs[ord(s2[i]) - ord("a")] + 1  # tally s2[:wsize]
    if fs == fp:  # first window already matches
        return True  # done
    for i in range(wsize, len(s2)):  # slide
        fs[ord(s2[i]) - ord("a")] = fs[ord(s2[i]) - ord("a")] + 1  # include new right
        fs[ord(s2[i - wsize]) - ord("a")] = fs[ord(s2[i - wsize]) - ord("a")] - 1  # exclude left
        if fs == fp:  # this window is a permutation of s1
            return True  # first hit is enough
    return False  # no window matched


print(check_inclusion("ab", "eidbaooo"))  # expected output: True  (window "ba")
print(check_inclusion("ab", "eidboaoo"))  # expected output: False
```

**How the code works**

- Identical motion to `find_anagrams`. You stop at the first `fs == fp` instead of collecting indices.
- Time **O(n)**. Space **O(1)** (two lists of 26).

### Fully Worked Extra: Longest Substring Without Repeating Characters

Problem link: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

This is a **variable** window. The constraint is “all characters in the window are unique.” Expand `right`. If a duplicate sits inside the window, jump `left` to one past the previous copy.

```python
def length_of_longest_substring(s):  # length of the longest substring with unique characters
    last_seen = {}  # map from character to its latest index
    left = 0  # left end of the current unique window
    best = 0  # longest valid length so far
    for right, ch in enumerate(s):  # expand the right end
        if ch in last_seen and last_seen[ch] >= left:  # this copy sits inside the window
            left = last_seen[ch] + 1  # shrink: start after the previous copy of ch
        last_seen[ch] = right  # record that ch was last seen at right
        length = right - left + 1  # current unique window length
        if length > best:  # longer than the best so far
            best = length  # update
    return best  # 0 for the empty string


print(length_of_longest_substring("abcabcbb"))  # expected output: 3  ("abc")
print(length_of_longest_substring("bbbbb"))  # expected output: 1
print(length_of_longest_substring("pwwkew"))  # expected output: 3  ("wke")
```

**How the code works**

- `last_seen[ch] >= left` means the previous `ch` is still inside the window. If it is to the left of `left`, it is already outside and does not force a shrink.
- `left` only moves right. Time **O(n)**.

### More Problems to Solve After Class

Name the pattern, then open the link. Do not read an editorial until you have a paper trace.

| Problem | Pattern | What to notice |
|---|---|---|
| [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Fixed window | Window size is `k`. Keep a count of vowels. Include/exclude one character per slide. |
| [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Variable window | You may flip at most `k` zeros. The window is valid while zeros inside it are `<= k`. Shrink from the left when zeros exceed `k`. |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Variable window | You may change at most `k` letters. Valid while `window_length - max_frequency <= k`. |
| [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Variable window | Longest subarray with **at most two** distinct values. Same shape as a frequency map plus shrink. |
| [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Variable window (positives) | While the product is too big, divide out `nums[left]`. Each new `right` adds `right - left + 1` valid subarrays. |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Variable window, **shortest** valid | Grow until `t` is covered. Shrink to the minimum covering window. Repeat. |
| [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Fixed-width neighbourhood | Two equal values whose indices differ by at most `k`. A window of width `k + 1` plus a set of values currently inside it. |
| [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Fixed window | Same include/exclude sum. Count windows whose average ≥ threshold. Compare `window_sum >= threshold * k` to stay in integers. |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Fixed window, harder | You need the **max** of every window of size `k`. A running sum is not enough. The usual tool is a **deque** of useful indices. Attempt this after the others. |

Reuse these two skeletons:

- **Fixed:** sum (or tally) the first `k` items, then `include right` and `exclude left` for the rest.
- **Variable:** `for right in range(n): include; while invalid (or while still valid, if you want the shortest): exclude left; update the answer.`

If a problem allows **negative** numbers and asks for a subarray **sum equal to k**, do **not** shrink from the left as in the minimum-length problem. That is a different pattern (prefix sums). The contiguous test is not enough by itself.

### Activity: Classify Before You Open the Editor

Without looking at the table, label each of these as **fixed**, **variable**, or **neither**:

1. Longest substring with all unique characters.
2. Maximum average of any `k` consecutive marks.
3. Count subarrays whose sum equals `k` when the array may contain negatives.
4. Starting indices of anagrams of `p` in `s`.

Suggested labels: (1) variable, (2) fixed, (3) neither — prefix sums, (4) fixed, width `len(p)`.

---

## How This Shows Up in Interviews

Platforms and company interviews care first about **how you think**, then about whether the code compiles.

A typical round looks like this:

1. You are given a statement. You restate it and ask about empty input, negatives, and whether the stretch must be contiguous.
2. You name the pattern: nested loops (correct, slow), then the window, and why **n = 1,00,000** forbids **O(n²)**.
3. You walk a sample with two fingers. You say when `start` moves and when `end` moves.
4. Only then you write code in **C++**, **Java**, or **Python** — whichever you can type correctly under pressure.

Knowing one of those three languages is enough. The interviewer has usually already decided the algorithm is sound before you type the first line. A fully working function in your preferred language is the last step, not the first.

When you use a **set**, a **map**, or a **frequency array of 26**, say **why**: uniqueness, counts, or a tiny alphabet. That sentence is worth more than a clever one-liner.

The next major pattern you will meet is **recursion**: a function that solves a smaller copy of the same problem. Sliding window stays linear and iterative.

Recursion will train a different muscle — call, smaller case, return — which later unlocks backtracking and trees. The habit stays the same: name the pattern before you write the loop or the recursive call.

---

## Key Takeaways

- A **subarray** is a contiguous slice. Duplicates may appear in a subarray. A problem may still **filter** for distinct values.
- Nested loops that rebuild each window are often correct and **O(n²)**. When **n** is around **1,00,000**, reuse the previous window: exclude left, include right.
- A **fixed** window has length `k` (or `len(p)`). A **variable** window expands `end` and shrinks `start` from the left. Neither index should move backwards.
- A **set** tells you uniqueness for one snapshot. A **frequency map** is the safe structure when you slide, because it knows how many copies remain.
- **Anagrams** are equal frequency arrays. Sliding them is the same include/exclude move as a running sum, with 26 counters instead of one integer.

Keep practising the extra LeetCode list with a paper trace first. When you later learn recursion, you will still start every problem with the same question: what is the pattern, and which index is allowed to move?

---

## Important Commands, Libraries, and Terminologies

| Term | What it means | Analogy |
|---|---|---|
| **Subarray** | Contiguous, non-empty slice of an array | Consecutive shops on a street |
| **Substring** | Contiguous slice of a string | Consecutive letters in a name |
| **Sliding window** | `[left, right]` frame that only crawls right | A photo frame on a row of jerseys |
| **Fixed window** | Length always `k` | Every block of 3 consecutive tests |
| **Variable window** | Length changes with a constraint | Shortest run of days whose rain total ≥ target |
| **O(n)** | Work grows in a straight line with n | One walk along the list |
| **O(n²)** | Work grows like n × n | Rechecking every pair of ends |
| **Set** | Unique values only | Attendance register |
| **Frequency map** | Value → count inside the window | Kirana tally of packets |
| **Frequency array (26)** | Counts for `a`…`z` | 26 columns in a scorebook |
| **Anagram** | Same characters with the same counts | Tiles `A,B,C` shuffled |
| **`defaultdict(int)`** | Dict whose missing keys start at 0 | A tally sheet that creates a row on first use |
| **`ord(ch) - ord("a")`** | Map a lowercase letter to index 0…25 | Column number of that letter |
| **`float("inf")`** | A starter “worse than any real length” | An empty best-so-far for a minimum |
| **LeetCode** | Practice site for the problems in this session | [https://leetcode.com](https://leetcode.com) |
| **GeeksforGeeks** | Articles and practice for the size-`k` window sum | [Window Sliding Technique](https://www.geeksforgeeks.org/dsa/window-sliding-technique/) |
| **`python3`** | Command to run Python 3 programs | The engine for the `.py` files |
| **OneCompiler** | Browser tool to paste and run Python | [https://onecompiler.com/python](https://onecompiler.com/python) |
