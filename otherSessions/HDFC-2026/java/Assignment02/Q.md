## HDFC Life Claim Amount Algorithms

Create a **Java console application** that stores one week of claim amounts in a **fixed array** and solves the problems below with the stated algorithms.

This is a **new project**. You do not need last week's repo.

Plain Java only. **No Spring. No Java Streams.** Compile and run with `javac` / `java`, or Maven/Gradle if you already use it.

Do not use `ArrayList` for the claim amounts. Use a raw `int[]` plus a `size` field so insert and delete actually **shift** elements.

---

### Seed data

Daily claim amounts (day order). Load these with `add(...)` only — do not pre-size the data with an array literal of length 6 as your store.

```text
Day 1  25000    HDFC-LIFE-1001  Anita Sharma   (TERM)
Day 2  18000    HDFC-LIFE-1002  Rahul Mehta    (ULIP)
Day 3  42000    HDFC-LIFE-1005  Sneha Patel    (ULIP)
Day 4  15000    HDFC-LIFE-1004  Vikram Singh   (TERM)
Day 5  31000    HDFC-LIFE-1001  Anita Sharma   (TERM)
Day 6   9000    HDFC-LIFE-1003  Priya Nair     (ENDOWMENT)
```

```text
[25000, 18000, 42000, 15000, 31000, 9000]
```

Keep a **copy** of this seed for the algorithm sections. Insert/delete demos must not change the array used by pair-sum, partition, and sliding window.

---

### 1. Array insert and delete (shifting)

Class `ClaimAmountStore`:

- `int[] data`
- `int size`
- capacity at least `16`
- `add(int amount)` — append
- `insert(int index, int amount)` — shift right, then write
- `delete(int index)` — shift left
- `toArray()` — returns a copy of length `size`

Rules:

- Insert and delete must move elements with a loop. Do not build a new array and copy everything except the gap unless you still shift in place on `data`.
- Invalid index → `InvalidIndexException`
- `insert` when `size == data.length` → `StoreFullException`

In `main`:

1. Print the seed: `25000, 18000, 42000, 15000, 31000, 9000`
2. `insert(2, 22000)` and print  
   → `25000, 18000, 22000, 42000, 15000, 31000, 9000`
3. Print how many elements were shifted → **`4`**
4. `delete(2)` and print  
   → `25000, 18000, 42000, 15000, 31000, 9000`

Comment above `insert` and `delete`: time **O(n)**, extra space **O(1)**.

---

### 2. Pair sum — brute force vs two-pointer

Target **`57000`**. Work on a **copy** of the seed.

Implement **both** methods. Do not use Streams.

| Method                                     | Required complexity                                              |
| ------------------------------------------ | ---------------------------------------------------------------- |
| Nested loops                               | **O(n²)** time, **O(1)** extra space                             |
| Sort a copy, then two-pointer (left/right) | **O(n log n)** time (sort dominates), **O(n)** extra if you copy |

Both must print the pair **`15000 + 42000`**.

If no pair exists, throw `PairNotFoundException`.  
`main` must also try target **`1`** and print the caught message.

Comment Big-O above each method.

---

### 3. Palindrome — two-pointer

Check whether a number is a palindrome using two pointers on its **digits** (char array or `int[]` of digits).

Do **not** use `StringBuilder.reverse()`, `StringBuffer`, or compare the number to its reverse built as a new string.

| Input   | Result  |
| ------- | ------- |
| `12321` | `true`  |
| `18500` | `false` |

Complexity: **O(d)** time for `d` digits, **O(d)** extra if you store digits (state this in the comment).

---

### 4. Partition — two-pointer

Rearrange a **copy** of the seed around pivot **`20000`**:

- left side: amounts **`<= 20000`**
- right side: amounts **`> 20000`**

Use this exact algorithm (Hoare-style) so everyone’s output matches:

```text
left = 0, right = n - 1
while left <= right:
    while left <= right AND arr[left]  <= pivot: left++
    while left <= right AND arr[right] >  pivot: right--
    if left < right: swap arr[left] and arr[right]; left++; right--
```

Expected array:

```text
9000, 18000, 15000, 42000, 31000, 25000
```

Complexity: **O(n)** time, **O(1)** extra space besides the copy. Comment it.

---

### 5. Sliding window — max sum of size k

Use the seed array and **`k = 3`**.

Windows:

```text
25000 + 18000 + 42000 = 85000
18000 + 42000 + 15000 = 75000
42000 + 15000 + 31000 = 88000
15000 + 31000 +  9000 = 55000
```

Return **`88000`**.

Rules:

- After the first window, add the new right element and subtract the element that left the window
- **O(n)** time, **O(1)** extra space
- Do **not** re-sum all `k` elements for every window
- If `k <= 0` or `k > n`, throw `InvalidWindowException`

Comment the complexity above the method.

---

### 6. Sliding window — longest substring without repeating characters

Claim batch code:

```text
TERMULIPTERM
```

Find the length of the longest substring with **all unique characters**.

Answer → **`8`** (`TERMULIP`).

Use a sliding window (start/end indexes) plus a `HashMap` or `HashSet` of characters in the current window.  
**O(n)** time.

Do not use a nested loop that restarts a full scan from every index (that is O(n²)).

---

### 7. Recursive binary search

Sort a **copy** of the seed:

```text
[9000, 15000, 18000, 25000, 31000, 42000]
```

Implement **recursive** binary search (no loop inside the search method except the two recursive calls / base case).

| Search  | Result      |
| ------- | ----------- |
| `15000` | `found`     |
| `999`   | `not found` |

Comment: **O(log n)** time, **O(log n)** extra space because of the call stack.

---

### 8. Complexity in the README

`README.md` must have a table with **time** and **extra space** for every method above.

Use the right notation in the table (you may write `O(...)` only; if you mention Ω or Θ, use them correctly).

Also add **one short paragraph** (4–6 lines) answering:

> For 1,000,000 daily claim amounts, would you use brute-force pair-sum or two-pointer pair-sum? Why?

---

### Exception handling

All of these must extend **`RuntimeException`**:

```text
AlgorithmException
  ├── InvalidIndexException
  ├── StoreFullException
  ├── PairNotFoundException
  └── InvalidWindowException
```

Do not empty-catch. Print the exception message in `main`.

`main` must demonstrate:

- `insert(99, 1)` on the seed store (or an equivalent invalid index)
- pair-sum target `1`

---

### Suggested layout

```text
hdfc-life-claim-algorithms/
  src/com/hdfclife/
    Main.java
    store/       ClaimAmountStore
    algo/        PairSumSolver, PalindromeChecker, PartitionSolver,
                 SlidingWindowSolver, UniqueSubstringSolver, BinarySearcher
    exception/   AlgorithmException, InvalidIndexException, StoreFullException,
                 PairNotFoundException, InvalidWindowException
  README.md
  .gitignore
```

You may merge small helpers, but do not put every algorithm in `Main`.

---

### `main` must print (in this order)

1. Seed array → `25000, 18000, 42000, 15000, 31000, 9000`
2. After `insert(2, 22000)` → `25000, 18000, 22000, 42000, 15000, 31000, 9000`
3. Shift count for that insert → **`4`**
4. After `delete(2)` → `25000, 18000, 42000, 15000, 31000, 9000`
5. Brute-force pair for `57000` → `15000 + 42000`
6. Two-pointer pair for `57000` → `15000 + 42000`
7. Palindrome `12321` → `true`
8. Palindrome `18500` → `false`
9. Partition around `20000` → `9000, 18000, 15000, 42000, 31000, 25000`
10. Sliding-window max for `k=3` → **`88000`**
11. Longest unique substring of `TERMULIPTERM` → **`8`**
12. Binary search `15000` → `found`
13. Binary search `999` → `not found`
14. Caught message for invalid insert index `99`
15. Caught message for pair target `1`

---

### Submission Guidelines

Submit the **GitHub repository link**.

- Push the full Java project (`src`, `README.md`, `.gitignore`)
- Repo must be **public**
- Do **not** commit `.class` files or `out/` / `bin/` / `target/`
- Submit the GitHub repo URL as your answer

### Additional Solving

- <a href="https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/" target="_blank" rel="noopener noreferrer">Maximum Sum of Distinct Subarrays With Length K</a>
- <a href="https://leetcode.com/problems/subarray-sum-equals-k/description/" target="_blank" rel="noopener noreferrer">Subarray Sum Equals K</a>
- <a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank" rel="noopener noreferrer">Fruit Into Baskets</a>
- <a href="https://leetcode.com/problems/max-consecutive-ones-iii" target="_blank" rel="noopener noreferrer">Max Consecutive Ones III</a>
- <a href="https://leetcode.com/problems/subarray-product-less-than-k" target="_blank" rel="noopener noreferrer">Subarray Product Less Than K</a>
- <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters" target="_blank" rel="noopener noreferrer">Longest Substring Without Repeating Characters</a>
- <a href="https://leetcode.com/problems/longest-repeating-character-replacement" target="_blank" rel="noopener noreferrer">Longest Repeating Character Replacement</a>
- <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string" target="_blank" rel="noopener noreferrer">Find All Anagrams in a String</a>
- <a href="https://leetcode.com/problems/minimum-window-substring" target="_blank" rel="noopener noreferrer">Minimum Window Substring</a>
