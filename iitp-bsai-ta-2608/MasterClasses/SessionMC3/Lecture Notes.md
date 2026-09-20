# Masterclass: DSA Problems

## What You Will Learn in This Session

In the previous session you learned to split a problem into **inputs**, **steps**, **outputs**, and **edge cases** before typing. You tallied items with a **frequency-counter** object, moved **two pointers** on a palindrome and a sorted pair-sum, and named **O(1)**, **O(n)**, and **O(n²)** in plain words. A method can be **correct** and still be too heavy once **n** grows. That is why **optimization** exists — not as a new JavaScript keyword, but as a choice of pattern. JavaScript programs in these notes can be run at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

---
## Why Optimization Is Needed

- **Official Definition:** **Algorithmic optimization** is rewriting the steps of a problem so the number of operations grows more slowly as the input size **n** grows, without changing the required output.
- **In Simple Words:** Same answer, less wasted walking. You stop redoing work you have already done.
- **Real-Life Example:** A clerk who ticks a register **once** finishes in a straight line with the number of names. A clerk who compares every student with every other student finishes much later, even though both can produce a correct count.

**Need:** The first translation of "find a pair" or "check every stretch" is often a loop inside a loop. For 5 items that feels instant. For 1,00,000 items the same idea grows like **n × n**.
**Logic:** Optimization **reuses** something: a tally you already built, an index you already visited, or a running sum of neighbours. The output stays the same. The walk gets shorter.
**Common doubt:** *"If nested loops give the right answer, why change?"* Correctness is not the same as **growth**. You already named that difference as **O(1)**, **O(n)**, and **O(n²)**.

Beginner list problems reuse work in a small family of patterns: **nested loops** (the unoptimized baseline), a **frequency-counter** object, **object lookup** of a stored index, **two pointers**, a **sliding window**, and **sort then two pointers**. Two pointers and sliding windows belong in that family — not the whole family. The frequency-counter object was the previous session's one-pass tally; object lookup stores **positions**, not counts. **Two pointers** and **sliding windows** reuse **indices**; sorting helps only when **values** matter more than original order.

### Merits, Demerits, and Typical Use Cases

| Technique | Typical use cases | Merits | Demerits |
|---|---|---|---|
| Nested loops | Tiny **n**; a first check that the answer is right | Easy to invent; matches the English sentence | Work grows like **n × n** or **n × k**; recounts shared items |
| Frequency counter | "How many times?", duplicates, anagrams | One pass, **O(n)** time | Extra memory for distinct keys; not a substitute for **contiguous** order |
| Object lookup | Unsorted pair of **indices**; "have I seen this value?" | **O(n)** time; keeps original positions | Extra memory; does not by itself find a **window** of neighbours |
| Two pointers | Palindrome; sorted pair-sum; reverse; compact / partition **in place** | **O(n)** time, often **O(1)** extra space | Meet-in-the-middle pair-sum needs sorted data; sorting first **destroys** adjacency |
| Sliding window | Subarray / substring of length **k**; longest or shortest stretch **such that** a rule holds | **O(n)** if neither index moves backwards; reuses the last sum or Set | Only **contiguous** data; shrinking left is unsafe when a **sum** may go down then up (negatives); a Set uses extra space |
| Sort, then two pointers | Unsorted numbers, answer is about **values** not original seats | Unlocks the "too small / too big" rule | Sorting itself is extra work; never use this when neighbours must stay in original order |

Optimization is a **fit**, not a badge. A nested loop on 8 marks is fine; the same nested loop on a lakh attendance rows is not. A sliding window on a **subsequence** (items may skip) is the wrong tool.

In this session, you will:

- See why nested loops feel natural, and when they **re-add work** you already did
- Use two pointer **shapes**: meet in the middle, and chase from the same side
- Know when **sorting** helps two pointers, and when sorting **destroys** the answer
- Grow and shrink a **sliding window** — fixed length **k**, or a **variable** stretch with a rule
- Pick **two pointers**, a **fixed window**, a **variable window**, or **neither** from the problem sentence

By the end, you will look at a list or string and say "this is a window" or "this is two pointers," then write an **O(n)** scan.

---
## Why Nested Loops Feel Natural

When a problem says "find a pair" or "check every stretch," the first idea is often a loop inside a loop. That idea is not foolish. It is the most direct translation of the English sentence.

- **Official Definition:** A **nested loop** is a loop placed inside another loop, so the inner loop runs fully for every step of the outer loop.
- **In Simple Words:** You pick one item, then check it against every other item, then pick the next item and repeat.
- **Real-Life Example:** In a class of 40, you compare every student with every other student to find two marks that add to 150. You do a huge number of comparisons, even though many pairs share the same students.

The method can be **correct**. Nested work is not only "every pair." It also hides inside "every stretch of neighbours."

Suppose a kirana shelf has **order totals** in a row, and the offer is the best stretch of **3 consecutive** items.

```text
totals = [20, 90, 85, 10, 95],  k = 3
20 + 90 + 85 = 195
     90 + 85 + 10 = 185   (you added 90 and 85 again)
          85 + 10 + 95 = 190   (you added 85 and 10 again)
```

Two of the three numbers were already known. Nested summing refuses to reuse them. That reuse is the sliding-window idea you will code later in this session.

![Nested resum of every window of length k versus one sliding total that drops the leaving value and adds the entering value on array 20 90 85 10 95](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc3/sessionmc3-01-nested-vs-sliding-reuse.png)

### Activity: Count the Repeated Additions

On paper, write every stretch of length 3 for `[20, 90, 85, 10, 95]`. Circle every number that was added in the previous stretch as well. You should circle **90**, **85**, and then **85**, **10** — the wasted work a sliding total will skip.

---
## Two Pointers

Once you accept that recounting is wasteful, you need a cleaner walk. You already used **two pointers** on `"NITIN"` and on a sorted price list. This session names **two shapes** of the same idea.

- **Official Definition:** A **pointer** here is an integer **index** into an array or string. **Two pointers** means two indices whose movement is coordinated so each index walks the data a small number of times.
- **In Simple Words:** You keep two fingers on the list — a left finger and a right finger — and you move one finger at a time according to a rule.
- **Real-Life Example:** Two friends stand at the two ends of a sorted railway fare chart. If the sum is too small, the left friend steps toward costlier rows. If the sum is too large, the right friend steps toward cheaper rows — one rule, one step, until they meet.

![Two pointer shapes — meet in the middle on sorted array 2 7 11 15 with L and R moving inward, and slow-fast chase from the same side on array 0 0 1 1 2](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc3/sessionmc3-02-two-pointer-shapes.png)

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

Use this shape for a **pair sum** on sorted data, a **palindrome** check, or reversing a list in place.

### Pointers That Chase from the Same Side

Both pointers start on the left. **Fast** reads every item. **Slow** only moves when you want to **keep** a value.

```text
nums = [0, 0, 1, 1, 1, 2]
        S / F start together on the left
```

Fast walks the whole list. Whenever `nums[fast]` is a new value, copy it next to slow and move slow forward. Slow is the boundary of the "useful prefix."

Use this shape to **remove duplicates in place**, move zeroes to the end, or compact a list without building a second array.

### When Sorting Helps — and When It Destroys the Answer

Two pointers from the ends only work when moving a pointer changes the answer in a **predictable** direction. Sorting is the usual way to get that property — but sorting is not always allowed.

- **Official Definition:** A list is **sorted** when its values follow a known order, such as non-decreasing numbers. **Sorting** rearranges values into that order.
- **In Simple Words:** Sorted means "smaller to bigger" (or the reverse). Unsorted means the values can jump around.
- **Real-Life Example:** A result portal already sorted by roll number is easy to walk from both ends. A pile of hall tickets in random order is not. If you shuffle a shelf to sort by price, you also destroy the **shelf order**.

| Situation | What you should do |
|---|---|
| List is already sorted; you need a pair of **values** | Two pointers from the ends. Do not sort again. |
| List is unsorted; you need a pair of **values**, and original positions do not matter | Sort first, then two pointers. |
| You need a **contiguous** stretch (neighbours in the original order) | Do **not** sort. Use a sliding window. |
| You need a pair of **original indices** on an unsorted list | An **object** used as a lookup, not two pointers from the ends. |

**Common doubt:** *"Can I always sort, then use two pointers?"* Only when the problem cares about **values**, not **positions in the original order**. A "best three consecutive items" problem dies if you sort.

### Activity: Name the Shape

For each task, write **meet in the middle** or **chase from the same side**:

1. Reverse the characters of `"NAMAN"` without building a new string.
2. From a sorted marks list, find two marks that add to 90.
3. Overwrite a sorted roll-number list so duplicates disappear from the front.

**Suggested answers:** (1) meet in the middle, (2) meet in the middle, (3) chase from the same side.

---
## Sliding Windows

Two pointers from the ends hunt **pairs**. Many problems hunt a **stretch of neighbours** instead — a block of totals, a block of characters, a block of attendance marks. That stretch is a **window**.

- **Official Definition:** A **sliding window** is a contiguous segment `[left, right]` that moves across an array or string. The right index grows the segment. The left index shrinks it when a **constraint** is broken.
- **In Simple Words:** Imagine a cardboard frame that covers a few packets on a kirana shelf. You slide the frame only to the right. You never jump backwards.
- **Real-Life Example:** The shop runs an "any 3 consecutive items on this shelf" combo. The shopkeeper does not rebuild the combo from scratch. He drops the item that left the frame and adds the item that entered.
- **Official Definition:** A **constraint** is the rule that decides whether the current window is allowed.
- **In Simple Words:** The constraint is the house rule of the window — unique characters, sum of length k, no failed attendance, and so on.
- **Real-Life Example:** A combo is valid only while it contains exactly three consecutive shelf items. If a fourth item enters, the shopkeeper must drop the leftmost item. That "exactly three" rule is the constraint.

```text
shelf:  a  b  [c  d  e]  f     L on c, R on e
```

![Fixed sliding window of length k equals 3 — left and right indices on contiguous array cells, drop the leaving value and add the entering value without resumming the whole window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc3/sessionmc3-03-sliding-window-fixed-k.png)

- **Right** always moves forward when you include a new item.
- **Left** moves forward only when the window has become **invalid**.
- Because neither index moves backwards, each position enters and leaves the window **at most once**. The scan is **O(n)**.

A window **uses** two pointers (`left` and `right`). The extra idea is that the items **between** them must stay contiguous, and you keep a running summary of that slice.

### Fixed-Size Window and Variable-Size Window

In a **fixed-size** window the length is always **k**. Every step you drop one item from the left and add one item from the right.

Keywords: *subarray of size k*, *every window of length k*, *maximum of every k consecutive*. In a **variable-size** window the length changes. You grow **right** freely, and you shrink **left** until the constraint holds again.

Keywords: *longest substring such that*, *smallest window that covers*, *at most k distinct*. For a **longest valid** stretch, shrink just enough then record length. For a **shortest valid** stretch, grow until valid, then shrink as far as you can while still valid.

**Common doubt:** *"Is a window the same as two pointers?"* A window uses two pointers. The extra rule is **neighbours stay together**, plus a running summary (a sum, a Set, or a tally object).

You spend a small **Set** or object so you do not rescan the window on every step. Time stays **O(n)**. Extra memory (**space complexity**) grows with what you store inside the window.

### Activity: Circle the Keywords

Read these three sentences. Write **fixed window**, **variable window**, or **not a window**.

1. Maximum sum of any **4 consecutive** orders.
2. Longest run of deliveries **without** a cancelled order.
3. Maximum sum if you may pick **any** orders, even if they are not next to each other.

**Suggested answers:** (1) fixed window, (2) variable window, (3) not a window — that is a subsequence problem, not a contiguous stretch.

---
## How to Pick a Pattern from the Problem Statement

Read the statement once. Circle whether the answer must be **contiguous**. Then classify.

![Pattern picker — contiguous slice, fixed width k, grow-shrink constraint, sorted pair, object lookup for indices, and when negatives break a simple window](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc3/sessionmc3-04-pattern-picker.png)

| You see in the statement | Likely pattern | Why |
|---|---|---|
| Pair that sums to a target, list sorted (or may be sorted) | Two pointers from the ends | The sum moves up or down in a predictable way |
| Remove, compact, or partition **in place** | Slow and fast pointers | Fast reads, slow writes |
| Subarray or substring of length **k** / max of every k consecutive | Fixed sliding window | Width never changes |
| Longest or shortest **contiguous** stretch **such that** a constraint holds | Variable sliding window | Width changes with the constraint |
| Any **subsequence** (items need not sit together) | Neither of today's patterns | A window requires neighbours |
| Subarray **sum equals k**, and numbers may be **negative** | Neither (running totals + an object) | Shrinking left does not always reduce the sum |
| Pair of **indices** on an unsorted list | Object lookup | Sorting would scramble the indices |

Walk this checklist in order: not contiguous means not a window; fixed width **k** means a fixed window; a grow-or-shrink rule means a variable window; a pair on **sorted** data means two pointers from the ends; anything else means do not force today's patterns.

### Activity: Classify Before You Code

Without writing code, label each sentence as **two pointers**, **sliding window**, or **neither**.

1. Find two numbers in a **sorted** list that add to `target`.
2. Longest substring with **at most 2** different characters.
3. Maximum **subsequence** sum (items may skip neighbours).
4. Move all zeroes to the end **in place**, keeping the order of non-zero values.
5. Count subarrays whose sum equals `k` when the list may contain **negatives**.
6. Maximum sum of any **k consecutive** elements.

**Suggested labels:** (1) two pointers, (2) sliding window, (3) neither, (4) two pointers, (5) neither for a window — **negatives** break "shrink left to make the sum smaller" — (6) sliding window.

---
## Reverse a List in Place

You now have the pattern map. The first program lets you **see** two pointers move, meet, and stop — with no extra constraint yet.

- **Official Definition:** An **in-place** algorithm updates the original array and uses only a small constant amount of extra memory.
- **In Simple Words:** You rearrange the same row of seats. You do not book a second row.
- **Real-Life Example:** Two students at the two ends of a bench swap bottles until they meet. The bench is reversed. No extra bench is needed.

**Common doubt:** Why is the loop `left < right` and not `left <= right`? For an odd-length list the middle item should stay put. Swapping an index with itself is wasted work, not an error.

```javascript
function reverseInPlace(arr) {                    // Define a function that reverses an array using two indices
  let left = 0;                                   // Left pointer starts at the first index
  let right = arr.length - 1;                     // Right pointer starts at the last index
  while (left < right) {                          // Continue until the two pointers meet or cross
    let temp = arr[left];                         // Store the left value so it is not lost in the swap
    arr[left] = arr[right];                       // Copy the right value into the left slot
    arr[right] = temp;                            // Put the saved left value into the right slot
    left = left + 1;                              // Move left one step toward the centre
    right = right - 1;                            // Move right one step toward the centre
  }                                               // End of the while loop
  return arr;                                     // The same array is now reversed; return it to print it
}                                                 // End of the function

console.log(reverseInPlace(["h", "e", "l", "l", "o"])); // Print [ 'o', 'l', 'l', 'e', 'h' ]
console.log(reverseInPlace(["I", "N", "D", "I", "A"])); // Print [ 'A', 'I', 'D', 'N', 'I' ]
```

**How the code works:**

- `left` and `right` start at the two ends and walk toward each other. Each swap places one pair into its final position
- The loop visits each index at most once, so the time is **O(n)** and extra memory is **O(1)**. Length 0 or 1 never enters the loop, so those arrays stay as they are
- `arr.slice().reverse()` also reverses, but it builds a **new** array. This version edits the original

### Activity: Trace on Paper First

Copy `["I", "N", "D", "I", "A"]` onto paper. Mark L and R, then write the list after every swap. Compare your trace with the program output.

---
## Finding a Pair Sum on a Sorted List

Reversing shows pointers moving. The next problem shows **why** you move only one pointer: the list is sorted, so the sum tells you the direction. In the previous session you returned `true` or `false`; here you return the **positions**.

**Problem:** You are given a **sorted** array of numbers and a **target**. Find two different positions whose values add to the target. Positions are numbered from **1**, not from 0.

```text
numbers = [2, 7, 11, 15],  target = 18
L=2, R=15  sum=17  too small  → move L right
L=7, R=15  sum=22  too big    → move R left
L=7, R=11  sum=18  match      → positions 2 and 3 (1-based)
```

**Logic:** If the current sum is too small, moving `right` left would make it even smaller, so that move cannot help. You must move `left` right. The opposite holds when the sum is too big.

```javascript
function twoSumSorted(numbers, target) {          // Find two 1-based positions that add to target
  let left = 0;                                   // Start at the smallest value
  let right = numbers.length - 1;                 // Start at the largest value
  while (left < right) {                          // The two positions must be different
    let total = numbers[left] + numbers[right];   // Current pair sum
    if (total === target) {                       // Found the required pair
      return [left + 1, right + 1];               // Convert 0-based indices to 1-based positions
    }                                             // End of match check
    if (total < target) {                         // Sum is too small, need a larger left value
      left = left + 1;                            // Move left toward bigger numbers
    } else {                                      // Sum is too big, need a smaller right value
      right = right - 1;                          // Move right toward smaller numbers
    }                                             // End of too-small / too-big branch
  }                                               // End of the while loop
  return [];                                      // No pair found
}                                                 // End of the function

console.log(twoSumSorted([2, 7, 11, 15], 18));    // Print [ 2, 3 ]
console.log(twoSumSorted([1, 2, 3, 4, 6], 6));    // Print [ 2, 4 ] — values 2 + 4
console.log(twoSumSorted([40], 40));              // Print [] — need two different indices
```

**How the code works:**

- Each step moves exactly one pointer, so the loop runs at most **n** times. Extra memory is **O(1)**
- Because the list is sorted, "too small" and "too big" have only one legal repair
- A nested pair scan on the same input also finds `[2, 3]`, but that shape is **O(n²)**. This walk is **O(n)**

### Activity: Trace the Moves

On paper, run `[1, 2, 3, 4, 6]` with target `6`. Write the sum at each step until the pointers stop. Then compare your trace with `twoSumSorted`.

**Suggested trace:** `1 + 6 = 7` (too big) → `1 + 4 = 5` (too small) → `2 + 4 = 6` → positions **`[2, 4]`**.

---
## Removing Duplicates from a Sorted List

Pair-sum used opposite ends. Duplicate removal uses the **chase** shape: fast reads everything, slow writes the unique prefix.

**Problem:** The list is **sorted**, so duplicates sit next to each other. Overwrite the array so the first **k** positions are unique, and return **k**. Do not build a second array.

```text
nums = [0, 0, 1, 1, 1, 2]
slow stays on the last kept unique; fast walks; copy when values differ
unique prefix [0, 1, 2, ...], k = 3
```

```javascript
function removeDuplicates(nums) {                 // Compact unique values to the front of a sorted array
  if (nums.length === 0) {                        // Empty list has no unique values
    return 0;                                     // Unique count is zero
  }                                               // End of empty check
  let slow = 0;                                   // Slow is the index of the last unique value kept so far
  for (let fast = 1; fast < nums.length; fast++) { // Fast inspects every later index
    if (nums[fast] !== nums[slow]) {              // A new unique value has appeared
      slow = slow + 1;                            // Open the next slot in the unique prefix
      nums[slow] = nums[fast];                    // Copy the new unique value into that slot
    }                                             // End of new-value check
  }                                               // End of the for loop
  return slow + 1;                                // Unique count is the last kept index plus one
}                                                 // End of the function

let sample = [0, 0, 1, 1, 1, 2];                  // Sorted list with duplicates
let k = removeDuplicates(sample);                 // Compact in place and receive the unique count
console.log(k, sample.slice(0, k));               // Print 3 [ 0, 1, 2 ]
console.log(removeDuplicates([]));                // Print 0
```

**How the code works:**

- Fast always moves. Slow moves only when a **new** value appears
- After the loop, only the prefix of length **k** is the answer. Time is **O(n)**. Extra space is **O(1)**
- **Common doubt:** *"Why not build a new array of unique values?"* That uses extra memory. A frequency object also works, but this chase needs only two indices because the list is **sorted**

### Activity: Dry Run

On paper, fill `slow` and `fast` for `[7, 7, 7, 8, 8, 9]`. Write the list after every copy. You should finish with prefix `[7, 8, 9]` and `k = 3`.

---
## Maximum Sum of k Consecutive Values

You can now compact and hunt pairs. The next pattern keeps a **contiguous** block of fixed length — the cardboard frame from the kirana example.

**Problem:** Given `totals` and `k`, return the **maximum sum** of any contiguous subarray of length **k**.

```text
totals = [20, 90, 85, 10, 95, 88, 0, 70]    k = 3
windows: 195, 185, 190, 193, 183, 158
slide 195 → 185 → 190 → 193 → 183 → 158; best stays 195
```

The maximum is **195**, from `[20, 90, 85]`. Humans skip windows; a loop does not.

A nested scan would add k values from scratch for every start — about **O(n · k)** additions. The following function reuses the previous sum instead.

```javascript
function maxSumKWindow(totals, k) {               // Fixed sliding window: reuse the previous sum
  let n = totals.length;                          // Store the length
  if (k > n || k <= 0) {                          // A window cannot be longer than the list, or empty
    return 0;                                     // No valid window exists
  }                                               // End of the guard
  let windowSum = 0;                              // Running sum of the current window
  for (let i = 0; i < k; i++) {                   // Build the first window
    windowSum = windowSum + totals[i];            // Add each of the first k values
  }                                               // End of the first-window loop
  let best = windowSum;                           // That sum is the best so far
  for (let i = k; i < n; i++) {                   // i is the new right end of the window
    windowSum = windowSum + totals[i] - totals[i - k]; // Add entering value, drop leaving value
    if (windowSum > best) {                       // Compare with the best sum seen
      best = windowSum;                           // Update if this window is better
    }                                             // End of comparison
  }                                               // End of the slide loop
  return best;                                    // Maximum sum of any k consecutive values
}                                                 // End of the function

let totals = [20, 90, 85, 10, 95, 88, 0, 70];     // Consecutive order totals on a shelf
console.log(maxSumKWindow(totals, 3));            // Print 195
console.log(maxSumKWindow([1, 2, 3], 5));         // Print 0 — k longer than the list
console.log(maxSumKWindow([], 3));                // Print 0 — empty list
```

**How the code works:**

- The first loop pays one full sum of k items. Each later step adds the entering value and subtracts the leaving value, so the time is **O(n)**
- If `k` is larger than the list, or `k` is not positive, the function returns `0`. That edge case is easy to forget
- A nested resum of every window is still correct. It does extra additions that this slide skips

### Activity: Count the Additions

On paper, count additions for this `totals` list with `k = 3`. Resumming six windows of length 3 is 18 additions; the window version adds 3 once, then one add and one subtract per slide. The function returns `195`.

---
## Longest Substring Without Repeating Characters

A fixed window always covers **k** items. The next question lets the length change. Many string problems use a rule on the **whole window**: every character inside it must be unique.

- **Official Definition:** A **Set** is a collection of unique values with fast "is this already inside?" checks.
- **In Simple Words:** A Set is an attendance notebook of characters currently inside the window. A character cannot be written twice.
- **Real-Life Example:** A railway coach window that may not contain two passengers with the same berth tag. If a duplicate tag arrives, passengers leave from the left until that tag is free. This is the same *tally* idea as the frequency-counter object, used as a membership check.

**Problem:** Given a string `s`, return the length of the longest **substring** (contiguous) that contains no repeating character.

```text
s = "abcabcbb"
grows a | ab | abc (length 3); next a, b, c already inside → bca, cab, abc
next b already inside → drop until unique → cb, then b; best length = 3
```

```javascript
function lengthOfLongestSubstring(s) {            // Longest contiguous unique-character substring
  let seen = new Set();                           // Characters currently inside the window
  let left = 0;                                   // Left edge of the window
  let best = 0;                                   // Best length seen so far
  for (let right = 0; right < s.length; right++) { // Right edge grows one character at a time
    let current = s[right];                       // Character that wants to enter
    while (seen.has(current)) {                   // Window is invalid until this character is unique
      seen.delete(s[left]);                       // Drop the leftmost character from the Set
      left = left + 1;                            // Shrink the window from the left
    }                                             // End of the shrink loop
    seen.add(current);                            // The new character is now unique; include it
    let length = right - left + 1;                // Current valid window length
    if (length > best) {                          // Compare with the best length
      best = length;                              // Update the answer
    }                                             // End of comparison
  }                                               // End of the for loop
  return best;                                    // Length of the longest unique substring
}                                                 // End of the function

console.log(lengthOfLongestSubstring("abcabcbb")); // Print 3
console.log(lengthOfLongestSubstring("bbbbb"));   // Print 1
console.log(lengthOfLongestSubstring("pwwkew"));  // Print 3
```

**How the code works:**

- `right` walks the string once. `left` only moves forward, never backward
- The inner `while` does **not** make this O(n²), because `left` across the whole run moves at most **n** times. `right - left + 1` is the length; forgetting `+ 1` is a common off-by-one error
- Extra space is the Set. You could use an object (`seen[ch] = true`) the way you used a frequency counter; `Set` is the same idea with `.has`, `.add`, and `.delete`

### Activity: Trace `"pwwkew"`

Draw a row of characters. Under it, write the window after every `right` step. You should see windows such as `pw`, then `w`, then `wke`, then `kew` — the best length is 3.

---
## Extra Practice

Name the pattern first, trace a small input on paper, then write the JavaScript. Do not open an editorial until you have a trace.

| Problem | Pattern to try | What to notice |
|---|---|---|
| [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/) | Fixed window plus a frequency object | Width is always `k`, **and** every value in the window must be unique. Record a sum only when both are true. |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/) | Prefix sums plus an object — **not** a window if negatives are allowed | Contiguous, yes. Shrink-left is unsafe when a value can be negative. |
| [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Variable window, at most 2 distinct values | Longest subarray with at most two different numbers. |
| [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii) | Variable window, at most `k` zeroes | The window is valid while the number of zeroes inside it is ≤ `k`. |
| [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k) | Variable window (values are positive) | While the product is too big, divide out `nums[left]`. Each new `right` adds `right - left + 1` valid subarrays. |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | Variable window plus a Set | Re-solve from a blank file using the trace in this session. |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | Variable window | Valid while `window_length - max_frequency <= k`. |
| [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string) | Fixed window plus two frequency objects | Window size is the length of `p`. Record start indices where the maps match. |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) | Variable window, shortest valid | Grow until `t` is covered, shrink to the minimum, repeat. |

---
## Key Takeaways

- **Optimization** means the same correct output with work that grows more slowly as **n** grows. Nested loops are the natural first translation; frequency counters, object lookup, two pointers, sliding windows, and sort-then-scan are different fits — not one badge for every problem.
- **Two pointers** are two coordinated indices. They meet in the middle on **sorted** pair problems, palindromes, and in-place reverse, or chase from the same side when you compact a list **in place**.
- A **sliding window** is a contiguous `[left, right]` frame. **Fixed** windows keep length `k` and add/drop one item per step; **variable** windows grow `right` and shrink `left` with a constraint. Neither index should move backwards.
- Sorting unlocks two pointers only when **values** matter. If the answer must stay in the **original order**, sorting destroys the window.
- Name the pattern from keywords before you code: pair sum, longest substring, maximum of every k, or **neither**. Later you will search and sort longer lists — the first question stays the same: is the answer **contiguous**, and why does each pointer move?

---
## Important Commands, Libraries, Terminologies used

| Term / syntax | Meaning in this session | Quick picture |
|---|---|---|
| **Optimization** | Same output, slower growth of work as **n** grows | Same chai, fewer wasted steps |
| **Nested loop** | A loop inside a loop; work often grows like n × n | Comparing every student with every other student |
| **Pointer** / **two pointers** | One or two indices moved by a rule | Fingers on a fare chart |
| **In-place** / **slow–fast** | Edit the original array; fast reads, slow writes | Swap bottles; a scout and a clerk |
| **Contiguous / subarray / substring** | Neighbours in the original order | Consecutive shelf items, not a shuffled mix |
| **Sliding window** | A `[left, right]` frame that only crawls right | Kirana combo frame on a shelf |
| **Fixed-size window** | Length always k | Best 3 consecutive totals |
| **Variable-size window** | Length changes with a constraint | Longest unique substring |
| **Constraint** / **Set** | Window rule; unique values with `.has` / `.add` / `.delete` | House rule; attendance notebook inside the window |
| **O(n)** / **O(n²)** / **space complexity** | Straight-line walk / nested pairs / extra memory | One walk / rechecking every pair / extra notebooks |
| `left < right` / `right - left + 1` | Two different indices; window length | Fingers meet; packets inside the frame |
