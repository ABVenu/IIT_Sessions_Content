# Loops and iteration — session notes

Programs repeatedly perform the same *kind* of action: validate each field, process each line of a file, redraw each frame, or retry until input is acceptable. Duplicating source for each repetition breaks when the count changes or was unknown when you wrote the code. **Loops** say the logic once: an indented **body** runs again under a clear rule—while a condition holds, or once per element of a sequence.

**Iteration** means executing that block multiple times with something different each time (counter, next list element, new input). Below follows the lecture thread: motivation, **`while`**, **`for`**, **`range`**, **`break`** / **`continue`**, nested loops, pitfalls, and short traces.

## 1. Why loops matter (summary)

| Situation | Without a loop | With a loop |
| --- | --- | --- |
| Repeat `N` times | `N` copied blocks | One body; `N` from counter or `range` |
| Process each item | Manual index and branches | `for item in seq` |
| Retry until valid | Nested `if` ladders | `while` with an updating state |
| Stop when found | Always scan whole sequence | `break` after match |
| Rows and columns | Awkward to express | Nested loops |

One body implies one place to fix logic and keep behavior consistent across repetitions.

## 2. `while` loops

**Semantics.** The condition is evaluated **before** each iteration. True → run body → check again. False → continue **after** the whole `while` block.

**Progress.** Something in the body (or a `break`) must eventually make the condition false. Forgetting to advance a counter or refresh input while the condition still reads the old values yields an **infinite loop**.

**Validation.** “While this input is invalid, ask again” matches English and keeps the invariant visible: each pass may assign a new value the condition inspects.

```python
password = ""
while len(password) < 8:
    password = input("Password (min 8 chars): ")
```

**`while True` + `break`.** Idiomatic when several branches can exit (quit command, sentinel, found). Every execution path must reach `break` eventually.

```python
while True:
    cmd = input("Command (quit to exit): ")
    if cmd == "quit":
        break
    print(f"Running: {cmd}")
```

The same “until zero” loop can be written with an explicit `while x != 0` or with `while True` / `break`; pick what reads best to the next reader.

## 3. `for` loops over iterables

**Semantics.** Python pulls the next value from the **iterable** (string, list, `range`, …), binds your loop variable, runs the body once. You do not code “step to next item” yourself.

```python
for ch in "Hello":
    print(ch)

for price in [19.99, 29.99, 39.99]:
    print(price * 1.08)
```

**Choosing `for` vs `while`.** Prefer `for` for “each element of this collection.” Prefer `while` for “until this *state* changes,” especially when tries are not tied to walking a fixed sequence.

## 4. The `range` object

**Forms:** `range(stop)`; `range(start, stop)`; `range(start, stop, step)` with negative `step` for countdowns.

**Exclusive stop.** The upper bound is **not** included—aligned with slicing: `range(5)` → `0‥4`, `range(2, 7)` → `2‥6`.

```python
list(range(5))           # [0, 1, 2, 3, 4]
list(range(2, 7))        # [2, 3, 4, 5, 6]
list(range(0, 20, 3))    # 0, 3, 6, … 18
list(range(5, 0, -1))    # [5, 4, 3, 2, 1]
```

**Lazy iteration.** Python 3’s `range` does not allocate the full integer list; values are produced as you loop. `break` may realize only an initial prefix.

**Index and element.** Lecture pattern when you need position: `for i in range(len(items)): ... items[i] ...`. Later, `enumerate` often replaces this for clarity; the idea is unchanged.

```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
```

## 5. `break`: leave the current loop

**Effect.** Jump to the first line **after** the loop; the loop’s normal exit test is skipped for that departure.

**Uses:** first hit in a search, user quit, sentinel value, batch aborted on first fatal error.

```python
numbers = [3, 7, 2, 9, 5]
target, i = 9, 0
while i < len(numbers):
    if numbers[i] == target:
        print(f"Found at {i}")
        break
    i += 1

for num in [10, 20, 0, 40]:
    if num == 0:
        print("Aborting batch: zero")
        break
    print(100 / num)
```

## 6. `continue`: skip the rest of this iteration

**Effect.** Skip the remainder of the body; **`while`** re-tests the condition, **`for`** takes the next item.

**Uses:** filter bad values but keep scanning; guard clauses instead of huge nested `if`.

```python
for score in [95, 45, 87, 32, 91]:
    if score < 60:
        continue
    print(f"Passing: {score}")
```

**`while` caution.** Updates that must run every pass (increment, new `input`) must still run on branches that `continue`, or you can repeat the same failed state forever.

## 7. `break` vs `continue`; nesting

| Statement | After it runs, does the same loop continue? |
| --- | --- |
| `continue` | Yes — next iteration |
| `break` | No — exited that loop |

In **nested** loops, both bind to the **innermost** loop only. Leaving an outer loop from inside an inner one typically needs a flag, structured `break` placement, or a helper function—patterns you will meet as code grows.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break   # inner j-loop only
        print(i, j)
```

## 8. Nested loops

The inner loop finishes all its steps (unless inner `break`) **for each** outer step. With outer `R` and inner `C` and no early exit, inner body runs about **`R × C`** times. Pair `(outer, inner)` iteration is the Cartesian product—grids, tables, small combination sketches.

```python
for i in [1, 2, 3]:
    for j in ["A", "B"]:
        print(f"{i}{j}")
```

**Lecture patterns.** Rectangle: outer row, inner column, `print("*", end="")` then `print()` per row. Multiplication table: both indices `1..n`. Right triangle: inner `range(row)` so row width grows.

```python
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()
```

Doubling row and column counts **multiplies** work—recognize quadratic behavior in two-level nests when data scales.

## 9. Pitfalls (quick checklist)

1. `while` condition never becomes false (no progress in body).
2. Off-by-one: treating `range`’s stop as inclusive.
3. `break` intended to stop an **outer** loop—only innermost stops.
4. `continue` in `while` without advancing mandatory state.
5. Very deep nesting without structure—hard to read and debug.


