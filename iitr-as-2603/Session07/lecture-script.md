# Lecture Script: NumPy — Numerical Foundations (Session 7)

**Session duration:** 2 hours 15 minutes (135 minutes), including one mid-session pause  
**Audience:** Learners who already know basic Python (variables, control flow, functions, lists, dicts).  
**Demo environment:** **VS Code** — instructor uses a **single Python file** (or `# %%` cell regions) in the editor, **Integrated Terminal** for `pip install` if needed, and **Run Python File** / **Run Selection** so students can mirror the same layout.

---

## How to use this document

For **timing and facilitation** only—not a substitute for `Lecture Notes.md`. Use the notes for definitions, full code, and figure URLs.

---

## Break rule (not a numbered block)

After roughly **60–75 minutes** (around end of **Block 5** or start of **Block 6**), one **5–8 minute** pause.

---

## 1. Set-up, analytics framing, Python ecosystem, and DAU demo (18 minutes)

**Facilitator actions**

- In **VS Code**: open a project folder, create `numpy_session_demo.py`, run `import numpy as np` and `print(np.__version__)`.
- Frame the arc: **analytics** → **why NumPy** → **arrays in real pipelines**.
- Walk the four analytics types from the notes (descriptive → prescriptive).
- **Agentic systems:** short definition + table from notes (grounding, tools, memory, safety, planning).
- **Why Python** and the **libraries table** (NumPy → pandas → SciPy / viz / sklearn / deep learning stacks). Stress: today is **NumPy** so later layers make sense.
- **Live code in VS Code** — DAU list from notes: build `dau`, `mean`, compare last three vs first three days; run the file.
- Preview the session topics (Why NumPy through performance vs lists).

**Thinking prompt (analytics — listen before defining):**  
“A metro card system logs **tap-in counts every hour**. You compute **average hourly load yesterday** vs **predicting tomorrow’s peak hour**. Which is mainly **descriptive** and which is mainly **predictive**—and what could go wrong if you confuse the two when reporting to operations?” (Give 60–90 seconds quiet think; debrief: yesterday’s average describes past; peak prediction needs a model or at least extrapolation—wrong label misallocates staff.)

**Student actions**

- Same file or their own: `import numpy as np`, run the DAU snippet.

**Bridge sentence:** “That pattern is **numbers in, vectorized math, decision out**—the engine is **NumPy’s `ndarray`**.”

---

## 2. What NumPy is, install sanity check, creating arrays, pitfalls (20 minutes)

**Facilitator actions**

- Motivate `ndarray` from notes (homogeneous, contiguous, vectorized); optional slide/diagram.
- In **terminal inside VS Code**: `pip install numpy` if needed; always `import numpy as np`.
- **Live-code** in the same `.py`: 1D `np.array`, 2D list-of-lists, `shape`; note print style (no commas).
- Pitfalls: int/float upcast, **ragged** rows → `object` dtype, string mixing.
- Explicit `dtype=float`.

**Thinking prompt (pitfalls — silent bug scenario):**  
“You read a CSV of student quiz scores row by row; one row has **only two scores** while others have **five**. You `np.array()` the nested list **without checking `.dtype`**. Later you compute a **mean across columns**. What can go silently wrong, and what’s the first attribute you should print after building the array?” (Answer sketch: object or ragged structure breaks numeric semantics; **always inspect `dtype` and `shape`**.)

**Student actions**

- Reproduce 1D / 2D creation; build a ragged list, print `.dtype`, then fix dimensions.

**Bridge sentence:** “**`shape` and `dtype`** are the truth before any math.”

---

## 3. Inspecting arrays — `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes` (16 minutes)

**Facilitator actions**

- **`(4,)` vs `(4, 1)`**: live reshape to column vector `reshape(3, 1)`.
- `.dtype`, `.ndim`, `.size`, `.nbytes`; upcasting rules; **`.shape` is not callable**.
- Quick **thumbs check**: `.size` of `(2, 3)` is 6.

**Student actions**

- `zeros` with `float32`, print `.nbytes` vs shape intuition.

**Bridge sentence:** “Next we **generate** sequences and grids instead of typing every element.”

---

## 4. Factory functions — `arange`, `linspace`, `zeros`, `ones`, `full` (14 minutes)

**Facilitator actions**

- `arange` vs `linspace` (stop exclusive vs inclusive; float step risk → prefer `linspace`).
- `zeros`, `ones`, tuple shapes; `full`.
- **Live bug:** `np.zeros(3, 4)` → `TypeError`; fix `np.zeros((3, 4))`.

**Student actions**

- `linspace(0, 10, 11)`; `(4, 4)` `zeros` with `dtype=int`.

**Bridge sentence:** “Simulations need controlled **random** draws—and a **seed** so results aren’t a mystery.”

---

## 5. Random numbers — `rand`, `randn`, `randint`, `seed`, `choice` (12 minutes)

**Facilitator actions**

- Contrast **`rand(d0,d1)`** (no tuple) vs **`zeros((d0,d1))`**.
- `randn`, `randint` (high exclusive), **`seed`**, `choice` with/without replacement—all in VS Code with short runs.

**Thinking prompt (reproducibility):**  
“Two students submit identical homework plots but **different random ‘noise’** each run. The rubric says results must **match the reference when the script is re-run**. What single line habit fixes the argument—and what does the habit *not* guarantee (e.g. different NumPy versions, parallel runs)?” (Debrief: **`np.random.seed(...)`** or Generator API for reproducibility; still need pinned library versions for strict parity.)

**Student actions**

- `np.random.seed(0)`; print five `rand` values; rerun file top-to-bottom and confirm match.

**Bridge sentence:** “Selection and slicing are where **silent view bugs** hide—next block is high stakes.”

---

## 6. Indexing and slicing (1D), views vs copies, assignment patterns (14 minutes)

**Facilitator actions**

- Indexing, negatives, **IndexError**; slicing `start:stop:step`; reversal.
- **Views:** slice assignment mutates parent; **`.copy()`** when independence matters.
- Assignment to slices (scalar broadcast).

**Thinking prompt (views — realistic bug):**  
“A teammate writes:  
`snapshot = prices[0:100]`  
then later `snapshot[0] = 0` to test a function. **Why might production `prices` now be wrong?** What one method should they have called on the slice?” (Answer: slice is a **view**; mutating it mutates `prices`; use **`.copy()`** for an isolated snapshot.)

**Student actions**

- Predict `arr[1:4]`, then run; `.copy()` drill.

**Bridge sentence:** “2D is **row, column**; 3D adds **batch / depth**—same rules, more indices.”

---

## 7. Multidimensional indexing — rows, columns, submatrices, 3D intuition (14 minutes)

**Facilitator actions**

- `m[row, col]`; `m[1]` vs `m[1, :]`; submatrix and stride slices.
- 3D: e.g. `np.arange(24).reshape(2, 3, 4)` and one indexing chain.
- Submatrix assignment into `zeros`.

**Student actions**

- Bottom-right `2×2` from a `4×4`; optional 3D “page” slice.

**Bridge sentence:** “Data arrives in chunks—we **join and split** along axes next.”

---

## 8. Concatenation, stacking, and splitting (12 minutes)

**Facilitator actions**

- `concatenate` axis 0 vs 1 with small matrices in VS Code; `vstack` / `hstack`; `stack` (new axis); `split` family—keep examples small.

**Thinking prompt (shapes — forces axis clarity):**  
“You have **January** sales as shape `(31, 5)` (31 days × 5 stores) and **February** as `(28, 5)`. You want one array **`all_months`** of shape `(59, 5)`. Which **axis** do you concatenate along—and why would `(31, 5)` and `(5, 28)` be a non-starter?” (Axis **0** stacks days; second pair fails non-time dimension match unless transposed.)

**Student actions**

- Vertical stack of two `(3, 2)` blocks; verify final `shape`.

**Bridge sentence:** “Lists are flexible; **ndarrays** are fast—last block makes the cost model concrete.”

---

## 9. Memory layout, benchmarking, vectorization, when to use lists vs arrays (12 minutes)

**Facilitator actions**

- Memory story: list of pointers vs contiguous buffer; optional `sys.getsizeof` vs `.nbytes`.
- **VS Code:** run `timeit` (or a simple loop with `time.perf_counter`) — list comprehension vs `np_arr * 2` at large `n`; stress **vectorization = compiled loop, not Python loop**.
- Element-wise ops; dtype homogeneity; **when list vs array** table.

**Thinking prompt (before showing numbers):**  
“For a million floats, you double each value. **Python list:** loop in Python touches every PyObject. **NumPy:** one `* 2` in C. **Which cost dominates**—the arithmetic, or **how data is stored and accessed**?” (Debrief: **storage and per-element overhead** dominate; NumPy avoids boxed objects and dispatches bulk work to native code.)

**Student actions**

- Run benchmark; reduce `n` if laptops struggle.

**Bridge sentence:** “Lock in **`shape–dtype–slice–view`** habits; next units stack **pandas** and models on this.”

---

## Timing flex — if you are running late

**Cut first:** Shorten **Block 1** thinking time → give answer quickly; trim **`choice`** in **Block 5**; **Block 8** demo only `concatenate` + `vstack`, assign `stack`/`split` as reading.

**Cut last:** **Block 2** pitfalls, **Block 6** views, **Block 9** benchmark—these prevent painful bugs.

**If early:** Extra minutes on **Block 6** (`.copy()`) or **Block 7** (submatrix on a fake “image” grid).

---

## Materials

- **VS Code** + Python interpreter; **`Lecture Notes.md`** for reference and image links.
