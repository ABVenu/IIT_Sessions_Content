## HDFC Life Claim Pipeline

Create a **Java console application** that moves HDFC Life claims through a **singly linked list**, a **stack**, a **circular queue**, and **worker threads**.

This is a **new project**. You do not need last week's repo.

Plain Java only. **No Spring. No Java Streams.** Compile and run with `javac` / `java`, or Maven/Gradle if you already use it.

You **may** use `java.util.concurrent` (`ExecutorService`, `Future`, `CompletableFuture`, `BlockingQueue`, `ArrayBlockingQueue`) and `java.util.PriorityQueue` where the section says so.

Do **not** use `java.util.LinkedList` or `java.util.Stack` for the linked-list and stack sections. Write your own nodes and your own stack. For BFS only, a `Queue` (including `LinkedList` used only as a `Queue`) is allowed.

Do not resubmit last week's array store. Two-pointer this week is **slow/fast on a linked list**.

---

### Seed data

Claim amounts in this order. Build the singly linked list with `addLast(...)` only.

```text
CLM-01  25000    HDFC-LIFE-1001  Anita Sharma   HIGH
CLM-02  18000    HDFC-LIFE-1002  Rahul Mehta    MEDIUM
CLM-03  42000    HDFC-LIFE-1005  Sneha Patel    HIGH
CLM-04  15000    HDFC-LIFE-1004  Vikram Singh   LOW
CLM-05  31000    HDFC-LIFE-1001  Anita Sharma   MEDIUM
CLM-06   9000    HDFC-LIFE-1003  Priya Nair     LOW
```

```text
25000 → 18000 → 42000 → 15000 → 31000 → 9000
```

Keep a **copy** of this seed list for reverse, middle, cycle, and later sections. Insert/delete demos must not change the list used by those algorithms.

Sum of the six amounts → **`140000`**.

---

### 1. Singly linked list — insert and delete

Class `ClaimLinkedList` with `ClaimNode` (`int amount`, `ClaimNode next`):

- `addLast(int amount)` — append
- `addFirst(int amount)` — insert at head (required API; you do not have to demo it in `main`)
- `insertAt(int index, int amount)` — 0-based; index `size` means append
- `deleteAt(int index)` — 0-based
- `nodeAt(int index)` — returns the node (needed to link a cycle)
- `toArray()` / print — amounts in list order
- `size()`

Rules:

- Do not back the list with an array or `ArrayList`. Nodes and `next` pointers only.
- Invalid index → `InvalidIndexException`
- `deleteAt` on an empty list → `EmptyListException`

In `main`:

1. Print the seed: `25000, 18000, 42000, 15000, 31000, 9000`
2. `insertAt(2, 22000)` and print  
   → `25000, 18000, 22000, 42000, 15000, 31000, 9000`
3. `deleteAt(2)` and print  
   → `25000, 18000, 42000, 15000, 31000, 9000`

Comment above `insertAt` and `deleteAt`: time **O(n)**, extra space **O(1)**.

---

### 2. Reverse — iterative and recursive

Reverse a **copy** of the seed. Implement **both**. Do not reverse in place on the seed used by later sections.

| Method     | Required complexity                                      |
| ---------- | -------------------------------------------------------- |
| Iterative  | **O(n)** time, **O(1)** extra space                      |
| Recursive  | **O(n)** time, **O(n)** extra space (call stack)         |

Both must print:

```text
9000, 31000, 15000, 42000, 18000, 25000
```

The recursive method must call itself. Do not write a loop that only looks recursive.

Comment Big-O above each method.

---

### 3. Middle and cycle — slow / fast pointers

Work on **copies**. Use Floyd's tortoise and hare. Do **not** compute `size()` and walk `size/2` steps. Do **not** use a `HashSet` / `HashMap` of nodes for `hasCycle` or for finding the cycle start.

**Middle** of the seed (even length → the **second** middle node, LeetCode 876 style):

```text
15000
```

**Cycle** on a copy:

1. Seed with no cycle → `false`
2. Link the tail to the node at index **`2`** (amount **`42000`**) → `true`
3. Cycle start amount → **`42000`**

After the cycle demo, **break the cycle** (`tail.next = null` or equivalent). Do not leave a cyclic list in memory for later sections.

Comment: detect **O(n)** time, **O(1)** extra space.

---

### 4. Add two numbers — digit linked lists

Digits are stored **least-significant first** (LeetCode Add Two Numbers). Walk both lists with a carry. Do **not** convert a whole list into an `int` / `long` / `BigInteger` / concatenated `String`.

```text
25000  →  0 → 0 → 0 → 5 → 2
18000  →  0 → 0 → 0 → 8 → 1
sum    →  0 → 0 → 0 → 3 → 4     (43000)
```

Print: `0, 0, 0, 3, 4`

Comment: **O(max(m, n))** time, **O(max(m, n))** extra for the result list.

---

### 5. Stack — array and linked list

Interface `ClaimStack`:

```text
void push(int value)
int pop()
int peek()
boolean isEmpty()
```

Implement **both**:

- `ArrayClaimStack` — fixed `int[]`, capacity at least `32`
- `LinkedClaimStack` — nodes, grow as needed

For balanced brackets, `push` / `pop` the bracket **character as an `int`**.

`pop` / `peek` on empty → `StackEmptyException`  
`push` when the array stack is full → `StackFullException`

**Balanced brackets** using `ArrayClaimStack` (characters `()[]{}` only; ignore letters):

| Input              | Result  |
| ------------------ | ------- |
| `((TERM)(ULIP))`   | `true`  |
| `((TERM)(ULIP)`    | `false` |
| `([)]`             | `false` |

**Postfix** using `LinkedClaimStack`. Tokens are separated by spaces. Operators: `+ - * /` (integer division).

```text
25000 18000 + 1000 -
```

Result → **`42000`**

Do not use `java.util.Stack` or `ArrayDeque` inside these two checkers. They must call **your** stack.

Comment push/pop: **O(1)** time.

---

### 6. Circular queue and BFS

**Circular array queue** `CircularClaimQueue`:

- capacity **exactly `4`** for the demo (constructor takes capacity)
- `enqueue`, `dequeue`, `isFull`, `isEmpty`
- wrap the tail index with `% capacity`
- do not shift elements on dequeue

In `main`, in this order:

1. `enqueue(25000)`, `enqueue(18000)`, `enqueue(42000)`
2. `dequeue()` → **`25000`**
3. `enqueue(15000)`, `enqueue(31000)`
4. Print remaining front-to-back → `18000, 42000, 15000, 31000`

`enqueue` when full → `QueueFullException`  
`dequeue` when empty → `QueueEmptyException`

Comment: enqueue/dequeue **O(1)** time, **O(1)** extra space besides the array.

**BFS** of HDFC Life branches. Use a `Queue<String>` (your own queue or `java.util.Queue`). Do not use recursion for BFS. Do not use the int circular-claim-queue for branch names.

Adjacency (left-to-right is enqueue order):

```text
MUMBAI     → PUNE, DELHI
PUNE       → HYDERABAD
DELHI      → KOLKATA
HYDERABAD  → CHENNAI
KOLKATA    → (none)
CHENNAI    → (none)
```

BFS from `MUMBAI`:

```text
MUMBAI, PUNE, DELHI, HYDERABAD, KOLKATA, CHENNAI
```

---

### 7. Priority queue

Use `java.util.PriorityQueue` of the six seed claims.

Order: urgency **HIGH before MEDIUM before LOW**, then **amount descending**.

Poll order of claim ids:

```text
CLM-03, CLM-01, CLM-05, CLM-02, CLM-04, CLM-06
```

Do not sort an `ArrayList` and pretend it is a heap. `poll()` must drive the print.

---

### 8. Threads — Runnable, Callable, Future

Use real threads. Do not fake this with a sequential loop on the main thread.

The NEW / TERMINATED demo must use a **named class that `implements Runnable`** (not only a lambda). `ClaimTotalCallable` must `implement Callable<Integer>`.

| Piece | What it must do |
| ----- | --------------- |
| `Thread.getState()` before `start()` | **`NEW`** |
| Same thread after `join()` | **`TERMINATED`** |
| `Callable<Integer>` submitted to an `ExecutorService` | Sum of the six seed amounts → **`140000`** via `Future.get()` |
| `future.isDone()` after `get()` | **`true`** |
| `CompletableFuture.supplyAsync(...)` | Same sum → **`140000`** (must run async, not `complete` on main) |
| `cancel(true)` on a `Callable` that `Thread.sleep`s at least 30 seconds | `isCancelled()` → **`true`** |
| Daemon thread, `setDaemon(true)`, print `isDaemon()` | **`true`** (you do not have to `start` it) |

**Producer–consumer** with `ArrayBlockingQueue<Integer>` of capacity **`2`** and **two threads**:

- Producer `put`s `25000`, then `18000`, then `42000`
- Consumer `take`s three values into a list
- `join` both, then print → `25000, 18000, 42000`

Producer and consumer may be raw `Thread`s. Shut down the `ExecutorService` used for the `Callable` / cancel demo. Do not leave non-daemon workers running.

Comment above the Callable: the blocking `get()` waits for the worker; the extra space is the worker's stack, not an extra O(n) array.

---

### 9. Complexity in the README

`README.md` must have a table with **time** and **extra space** for:

- linked-list `insertAt` / `deleteAt`
- reverse iterative vs recursive
- cycle detect
- middle (slow/fast)
- add-two-numbers
- stack push/pop
- circular enqueue/dequeue
- BFS

Use the right notation (you may write `O(...)` only; if you mention Ω or Θ, use them correctly).

Also add **one short paragraph** (4–6 lines) answering:

> A claim queue can grow to millions of entries. When would you store it in a linked list instead of a fixed array? When would you still prefer an array?

---

### Exception handling

All of these must extend **`RuntimeException`**:

```text
PipelineException
  ├── InvalidIndexException
  ├── EmptyListException
  ├── StackEmptyException
  ├── StackFullException
  ├── QueueEmptyException
  └── QueueFullException
```

Do not empty-catch. Print the exception message in `main`.

`main` must demonstrate:

- `deleteAt(99)` on a **non-cyclic** copy of the seed (or an equivalent invalid index)
- `pop()` on a new empty `ArrayClaimStack`
- `dequeue()` on a new empty `CircularClaimQueue`

---

### Suggested layout

```text
hdfc-life-claim-pipeline/
  src/com/hdfclife/
    Main.java
    model/       Claim, Urgency
    list/        ClaimNode, ClaimLinkedList, ListReverser,
                 CycleDetector, DigitListAdder
    stack/       ClaimStack, ArrayClaimStack, LinkedClaimStack,
                 ParenthesesChecker, PostfixEvaluator
    queue/       CircularClaimQueue, BranchBfs, ClaimPriorityDesk
    thread/      SeedRunnable, ClaimTotalCallable, ProducerConsumer
    exception/   PipelineException, InvalidIndexException, EmptyListException,
                 StackEmptyException, StackFullException,
                 QueueEmptyException, QueueFullException
  README.md
  .gitignore
```

You may merge small helpers, but do not put every algorithm in `Main`.

---

### `main` must print (in this order)

1. Seed list → `25000, 18000, 42000, 15000, 31000, 9000`
2. After `insertAt(2, 22000)` → `25000, 18000, 22000, 42000, 15000, 31000, 9000`
3. After `deleteAt(2)` → `25000, 18000, 42000, 15000, 31000, 9000`
4. Reverse iterative → `9000, 31000, 15000, 42000, 18000, 25000`
5. Reverse recursive → `9000, 31000, 15000, 42000, 18000, 25000`
6. Middle of seed → **`15000`**
7. `hasCycle` on seed → **`false`**
8. `hasCycle` after linking tail to index `2` → **`true`**
9. Cycle start amount → **`42000`**
10. Add-two-numbers → `0, 0, 0, 3, 4`
11. Balanced `((TERM)(ULIP))` → **`true`**
12. Balanced `((TERM)(ULIP)` → **`false`**
13. Balanced `([)]` → **`false`**
14. Postfix `25000 18000 + 1000 -` → **`42000`**
15. Circular `dequeue()` → **`25000`**
16. Circular queue after wrap → `18000, 42000, 15000, 31000`
17. BFS from `MUMBAI` → `MUMBAI, PUNE, DELHI, HYDERABAD, KOLKATA, CHENNAI`
18. PriorityQueue poll ids → `CLM-03, CLM-01, CLM-05, CLM-02, CLM-04, CLM-06`
19. Thread state before start → **`NEW`**
20. Thread state after join → **`TERMINATED`**
21. Callable `Future.get()` sum → **`140000`**
22. `isDone` after get → **`true`**
23. `CompletableFuture.supplyAsync` sum → **`140000`**
24. Cancelled future → **`true`**
25. Daemon flag → **`true`**
26. Producer-consumer takes → `25000, 18000, 42000`
27. Caught message for invalid list index `99`
28. Caught message for empty stack `pop`
29. Caught message for empty queue `dequeue`

---

### Submission Guidelines

Submit the **GitHub repository link**.

- Push the full Java project (`src`, `README.md`, `.gitignore`)
- Repo must be **public**
- Do **not** commit `.class` files or `out/` / `bin/` / `target/`
- Submit the GitHub repo URL as your answer

### Additional Solving

- <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank" rel="noopener noreferrer">Reverse Linked List</a>
- <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank" rel="noopener noreferrer">Linked List Cycle</a>
- <a href="https://leetcode.com/problems/linked-list-cycle-ii/" target="_blank" rel="noopener noreferrer">Linked List Cycle II</a>
- <a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank" rel="noopener noreferrer">Middle of the Linked List</a>
- <a href="https://leetcode.com/problems/add-two-numbers/" target="_blank" rel="noopener noreferrer">Add Two Numbers</a>
- <a href="https://leetcode.com/problems/valid-parentheses/" target="_blank" rel="noopener noreferrer">Valid Parentheses</a>
- <a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/" target="_blank" rel="noopener noreferrer">Evaluate Reverse Polish Notation</a>
- <a href="https://leetcode.com/problems/design-circular-queue/" target="_blank" rel="noopener noreferrer">Design Circular Queue</a>
- <a href="https://leetcode.com/problems/implement-queue-using-stacks/" target="_blank" rel="noopener noreferrer">Implement Queue using Stacks</a>
- <a href="https://leetcode.com/problems/palindrome-linked-list/" target="_blank" rel="noopener noreferrer">Palindrome Linked List</a>
