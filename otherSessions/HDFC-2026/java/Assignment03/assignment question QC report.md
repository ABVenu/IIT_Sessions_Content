# Assignment Question QC Report

**File:** `Q.md`  
**Track:** HDFC Life 2026 — Java Backend  
**Week:** 24–28 August 2026 (26 Aug holiday)  
**Format:** Single subjective GitHub project (same pattern as Assignment02)

---

## Iteration 1 — findings (fixed in `Q.md`)

| Issue | Severity | Fix |
|---|---|---|
| Section 6 required printing circular `dequeue()` → `25000`, but the `main` print list skipped it | Presentation | Added as print line 15; later lines renumbered |
| `ClaimStack` methods had no types; parentheses needed chars on an `int[]` stack | Ambiguity | Specified `push/pop/peek` signatures; brackets pushed as `int` |
| Cycle demo had no API to reach index 2 | Ambiguity | Required `nodeAt(int index)` |
| Cycle start could still be cheated with a `HashSet` of nodes | Scope leak | Banned `HashSet`/`HashMap` of nodes for both detect and start |
| Layout had no `Claim` / `Runnable` types that sections 7–8 need | Presentation | Added `model/Claim, Urgency` and `SeedRunnable` |
| BFS vs “no `LinkedList`” and BFS vs int circular queue were easy to misread | Ambiguity | BFS uses `Queue<String>` only; `LinkedList`-as-`Queue` allowed for BFS only |
| Executor `shutdown` vs producer-consumer raw threads | Ambiguity | Shutdown applies to the Callable/cancel executor |
| `deleteAt(99)` on a list that still had a cycle could hang | Logic risk | Exception demo must use a **non-cyclic** copy |
| Additional Solving included Binary Tree Level Order (trees not taught this week) | Out of syllabus | Replaced with Implement Queue using Stacks + Palindrome Linked List |
| `ArrayDeque` was allowed in the intro but never required | Presentation | Removed from the allowed list |

All locked outputs were independently recomputed (insert/delete, reverse, Floyd middle + cycle start, add-two-numbers, parentheses, postfix, circular wrap, BFS, PriorityQueue). All match `Q.md`.

---

## Section-level QC

| Section | Type | Remarks |
|---|---|---|
| Seed | Data | Same six claim amounts as Assignment02. Sum `140000` verified. |
| 1. Linked list insert/delete | Practical | `insertAt(2, 22000)` / `deleteAt(2)` restore verified. O(n) comments required. |
| 2. Reverse iter + rec | Practical | Expected `9000, 31000, 15000, 42000, 18000, 25000` verified. Recursive must actually recurse. |
| 3. Middle + Floyd | Practical | LeetCode-876 second middle on even length → `15000`. Tail→index 2 start → `42000`. Simulated tortoise/hare. |
| 4. Add two numbers | Practical | LSD digit lists `25000`+`18000` → `0, 0, 0, 3, 4`. Integer-concat shortcut forbidden. |
| 5. Stack | Practical | Both implementations required. `((TERM)(ULIP))` true, `((TERM)(ULIP)` false, `([)]` false (count-only solutions fail). Postfix → `42000`. |
| 6. Circular queue + BFS | Practical | Wrap remaining `18000, 42000, 15000, 31000` verified. BFS order unique given left-to-right adjacency. |
| 7. PriorityQueue | Practical | HIGH then amount desc → `CLM-03, CLM-01, CLM-05, CLM-02, CLM-04, CLM-06`. All keys unique, so poll order is stable. |
| 8. Threads | Practical | NEW/TERMINATED, Callable `140000`, cancel, daemon, BlockingQueue FIFO order are deterministic if followed. `supplyAsync` cannot be proven from stdout alone (same as Big-O comments — grader reads code). |
| 9. README | Written | Complexity table + linked-list vs array paragraph. |
| Exceptions | Practical | Hierarchy extends `RuntimeException`. Three demos; empty-list / stack-full / queue-full are defined but not all printed (same as Assignment02). |
| Additional Solving | Optional | All links are list / stack / queue problems; `target="_blank"`. |

---

## Curriculum coverage (calendar, not detailed-curriculum row dates)

| Calendar session | Covered in `Q.md`? |
|---|---|
| 24 Aug — Arrays II, Linked Lists I | Two-pointer applied as slow/fast; list insert/delete. Array store from Assignment02 is explicitly not repeated. |
| 25 Aug — Linked Lists II, Stacks & Queues I | Reverse, Floyd, middle, Add Two Numbers, array+linked stack, parentheses, postfix, circular queue |
| 26 Aug — Holiday | Not included |
| 27 Aug — Stacks & Queues II, Threads I | BFS, PriorityQueue, Runnable, Callable, Future, lifecycle |
| 28 Aug — Threads II | CompletableFuture, cancel, daemon, BlockingQueue producer-consumer |

Not required (present in detailed topics, not needed for a 5 on core LOs): doubly linked list, explicit `Deque` lab.

---

## Assignment-level QC

| Criteria | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 (matches Assignment02: seed, numbered sections, locked stdout, exception tree, layout, GitHub submit, Additional Solving) |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True (only “last week’s repo / array store”, same wording family as Assignment02) |
| No Metadata / internal author notes in the student brief | True |

---

## Final QC Decision

**Passed** after Iteration 1 fixes.

- Content Coverage, Creativity, Structural Adherence are all 5.
- No remaining logical or presentation mistakes in the student-facing brief.
- Locked outputs recomputed and matched.
