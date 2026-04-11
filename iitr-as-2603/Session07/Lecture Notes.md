## Analytics, Python, and this session

You already know basic Python (variables, control flow, functions, data structures). Before we dive into **NumPy**, it helps to situate *why* numerical arrays matter: they are the workhorse behind **analytics** pipelines that power modern software—including **agentic** systems that plan, call tools, and act on data.

---

### What is analytics?

**Analytics** is the disciplined use of **data + computation + reasoning** to turn observations into **insights, predictions, or decisions**.

- **Descriptive analytics:** What happened? (summaries, trends, dashboards)
- **Diagnostic analytics:** Why did it happen? (comparisons, attributions)
- **Predictive analytics:** What is likely to happen next? (models, forecasts)
- **Prescriptive / decision analytics:** What should we do? (optimization, policies)

In code, analytics usually means: **load data → clean and transform it → compute aggregates or models → evaluate → deliver a result** (a report, a score, a recommendation, or an action). NumPy (and friends) make the *compute* steps fast and reliable on large arrays of numbers.

---

### How analytics helps in agentic system design

An **agentic system** is software where an **agent** (often LLM-driven) can **perceive** context, **reason** about a goal, **use tools** (APIs, databases, code), and **act** in a loop until the task is done.

Analytics supports that design in concrete ways:

| Role | How analytics fits |
|------|---------------------|
| **Grounding** | Agents need facts from data (metrics, logs, user behavior)—not only text guesses. Analytics extracts those facts. |
| **Tool outputs** | Many tools return **structured numbers** (scores, time series, embeddings as vectors). Processing them is numerical analytics. |
| **Memory & retrieval** | Rankings, similarity scores, clustering—often numeric pipelines feeding what the agent “remembers” or retrieves. |
| **Safety & quality** | Monitoring drift, anomaly detection, evaluation metrics—analytics for *determining* whether the system behaves well. |
| **Planning** | When the next step depends on measured cost, risk, or reward, analytics connects “what we measured” to “what we should do next.” |

You do not need a full “autonomous agent” to use analytics—but **agentic systems that touch real data** almost always depend on **fast numeric operations** on arrays and tables. That is where **NumPy** enters: it is the standard foundation for doing that math in Python efficiently.

---

### Why Python is widely used for analytics

Python is not always the fastest language *in the abstract*, but it is **extremely productive** for analytics workflows:

- **Readability** lowers the cost of teamwork and iteration (notebooks, scripts, production services).
- A **single ecosystem** connects **data loading → cleaning → modeling → visualization → deployment** with mature libraries.
- **Interoperability:** call fast native/C/Fortran libraries (e.g., linear algebra) from Python; the heavy lifting runs in optimized code while you orchestrate in Python.
- **Community and jobs:** tutorials, tooling (Jupyter, VS Code, Colab), and industry adoption are huge—skills transfer across domains.

For large-scale numeric kernels, libraries like NumPy (and frameworks built on it) bridge **ease of use** and **performance** via vectorized operations and compiled backends.

---

### Popular Python libraries used for analytics (overview)

Think of these as layers; many build on **NumPy** under the hood:

| Library | Typical role |
|---------|----------------|
| **NumPy** | N-dimensional arrays, element-wise math, linear algebra primitives—**numerical foundation**. |
| **pandas** | **Tables** (rows/columns), time series, joins, group-by—**data wrangling** on labeled data. |
| **SciPy** | **Scientific routines** (optimization, statistics, signal processing, sparse matrices). |
| **Matplotlib / Seaborn** | **Plotting** and exploratory visualization. |
| **scikit-learn** | **Classical ML** (classification, regression, clustering, preprocessing pipelines). |
| **Statsmodels** | **Statistical models** (regression, tests, time series stats). |
| **PyTorch / TensorFlow / JAX** | **Deep learning** and differentiable computation (often for embeddings, ranking, perception). |

This session focuses on **NumPy** so you can read, shape, and compute on arrays fluently—**pandas** and ML stacks assume that comfort.

---

### Simple use case: from raw numbers to a decision

**Scenario:** A small app logs **daily active users (DAU)** for 7 days: `[120, 118, 125, 130, 128, 135, 140]`.

**Analytics questions:**

1. What is the **average** DAU? (descriptive)
2. Is usage **trending up**? (e.g., compare mean of the **first 3** days vs the **last 3** days—simple diagnostic)

**Without NumPy** you can do it with Python lists and loops. **With NumPy**, the same computations are **short, clear, and scale** when you have millions of points or many metrics at once:

```python
import numpy as np

dau = np.array([120, 118, 125, 130, 128, 135, 140])
print("Mean DAU:", dau.mean())
print("Mean DAU — last 3 days minus first 3 days:",
      dau[4:].mean() - dau[:3].mean())
```

That tiny script is **analytics in code**: summarize the past, compare segments, inform a product decision (e.g., whether to keep a feature). In larger systems—**including agents**—the arrays might be **embeddings**, **scores**, or **sensor streams**, but the pattern stays: **array + vectorized math → insight or action**.

---

### Topics covered in this session (NumPy)

After this framing, we focus on NumPy skills you will reuse everywhere in analytics stacks:

- **Why NumPy?**
- **Creating arrays**
- **Basic array math**
- **Shape and reshape**
- **Multidimensional arrays**
- **Slicing NumPy arrays**
- **Performance vs Python lists**

---

## 1. What Is NumPy?

A factory inspecting 4,000 camera images per second can't use Python loops — each delay loses product. NumPy arrays are the foundation that makes computation this fast.


NumPy (Numerical Python) is the core library for numerical computation in Python. It provides the `ndarray` — a multi-dimensional array of a single data type stored in a contiguous block of memory.

Key characteristics of an `ndarray`:
- All elements must be the **same type** (homogeneous)
- Stored in **contiguous memory** (no pointer indirection per element)
- Supports **vectorized operations** — apply an operation to all elements at once without Python loops
- Fixed size once created (reshaping creates a new array or a view)


![What Is NumPy?](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_1.png)

## 2. Installing NumPy

**pip (standard Python environment):**
```bash
pip install numpy
```

**conda (Anaconda/Miniconda):**
```bash
conda install numpy
```

**Google Colab / Jupyter (pre-installed):** No installation needed. NumPy is available by default.

**Verify installation:**
```python
import numpy as np
print(np.__version__)  # e.g., 1.26.4
```

The standard alias is `np`. Always use `import numpy as np` — it's universal convention.

## 3. Creating a 1D Array

```python
import numpy as np

# From a Python list
arr = np.array([10, 20, 30, 40, 50])
print(arr)        # [10 20 30 40 50]
print(type(arr))  # <class 'numpy.ndarray'>
```

Notice: no commas in the printed output — that's the NumPy display format.

## 4. Creating a 2D Array

Pass a list of lists — each inner list becomes a row:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(matrix.shape)  # (3, 3) — 3 rows, 3 columns
```

Every inner list must have the same length, otherwise NumPy creates an array of Python objects (not a proper numeric ndarray).

## 5. Common Pitfalls

**Mixed types — NumPy upcasts silently:**
```python
arr = np.array([1, 2, 3.0])
print(arr.dtype)  # float64 — integers were promoted to float
```

**Ragged nested lists — avoid:**
```python
bad = np.array([[1, 2], [3]])   # rows of unequal length
# Results in an array of Python objects, not a numeric array
print(bad.dtype)  # object
```

**String vs number mixing — always object dtype:**
```python
mixed = np.array([1, "two", 3])
print(mixed.dtype)  # <U21 — all elements become strings
```

**Rule:** NumPy picks the single dtype that can represent all elements. When in doubt, pass `dtype=float` or `dtype=int` explicitly:
```python
arr = np.array([1, 2, 3], dtype=float)
print(arr)  # [1. 2. 3.]
```


---

## 1. .shape — Dimensions as a Tuple

Before computing anything on a dataset — multiplying matrices, feeding a model, stacking arrays — you must verify its shape, data type, and number of dimensions. A shape mismatch crashes silently or produces wrong results.


`.shape` returns a tuple indicating the size of the array along each dimension.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a.shape)   # (4,)   — 1D: 4 elements, one axis

m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.shape)   # (2, 3) — 2 rows, 3 columns

t = np.zeros((3, 4, 5))
print(t.shape)   # (3, 4, 5) — 3D: 3 × 4 × 5
```

**Common confusion:** A 1D array with 4 elements has shape `(4,)` — note the trailing comma. This is Python's way of distinguishing a 1-element tuple `(4,)` from the integer `4`.


![.shape — Dimensions as a Tuple](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_3.png)

## 2. .reshape — New Shape, Same Elements

`.reshape` gives the **same elements** a **new shape**. The product of the new axes must equal `arr.size`, or NumPy raises `ValueError`. Use `arr.reshape(...)` or `np.reshape(arr, ...)`.

```python
import numpy as np

v = np.arange(6)
m = v.reshape(2, 3)              # (2, 3) — six elements, same grid size as matrix `m` in §1
print(m)
# [[0 1 2]
#  [3 4 5]]
print(m.reshape(-1).shape)        # (6,) flatten to 1D

a = np.array([1, 2, 3, 4])        # same 1D example as §1
print(a.reshape(1, -1).shape)     # (1, 4) — one axis can be -1 (inferred)
print(a.reshape(-1, 1).shape)     # (4, 1) column vector; contrast with shape (4,)
# v.reshape(3, 3)                  # ValueError: 6 elements cannot become 3×3
```

**Common confusion:** `(4,)` vs `(4, 1)` — see Pitfall 2 in §7. Reshape often returns a **view** (shared memory); call `.copy()` after reshaping if you must not alter the original.

## 3. .dtype — Element Data Type

`.dtype` reports the data type of every element in the array.

```python
a_int   = np.array([1, 2, 3])
a_float = np.array([1.0, 2.0, 3.0])
a_bool  = np.array([True, False, True])

print(a_int.dtype)    # int64
print(a_float.dtype)  # float64
print(a_bool.dtype)   # bool
```

**Setting dtype explicitly:**
```python
a = np.array([1, 2, 3], dtype=np.float32)
print(a.dtype)   # float32
print(a.nbytes)  # 12 (3 elements × 4 bytes)
```

**NumPy dtype upcasting rule:** when elements of different numeric types are mixed, NumPy chooses the most general type:
- `int` + `float` → `float64`
- Any numeric + `str` → Unicode string

## 4. .ndim — Number of Dimensions

`.ndim` returns the number of axes (dimensions):

```python
print(np.array([1, 2, 3]).ndim)            # 1
print(np.array([[1, 2], [3, 4]]).ndim)     # 2
print(np.zeros((2, 3, 4)).ndim)            # 3
```

Rule of thumb: ndim = length of the shape tuple.

## 5. .size — Total Element Count

`.size` returns the total number of elements across all dimensions:

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.size)    # 6   (2 × 3)
print(m.shape)   # (2, 3)
# size == product of all elements in shape
```

## 6. .nbytes — Memory Usage

`.nbytes` = `size × dtype_itemsize`:

```python
a32 = np.zeros(1_000_000, dtype=np.float32)
a64 = np.zeros(1_000_000, dtype=np.float64)

print(a32.nbytes)   # 4,000,000  (4 bytes × 1M)
print(a64.nbytes)   # 8,000,000  (8 bytes × 1M)
```

Use `.nbytes` to estimate memory before loading large datasets.

## 7. Common Attribute Pitfalls

**Pitfall 1 — Calling attributes as methods:**
```python
arr.shape()    # TypeError: 'tuple' object is not callable
arr.dtype()    # TypeError
```
These are attributes, not methods. Never use parentheses.

**Pitfall 2 — 1D shape vs. 2D column vector:**
```python
a = np.array([1, 2, 3])
print(a.shape)    # (3,)   — NOT (3, 1)
# To get a column vector:
col = a.reshape(3, 1)
print(col.shape)  # (3, 1)
```

**Pitfall 3 — Assuming default dtype is float:**
```python
np.array([1, 2, 3]).dtype      # int64   (all integers → int)
np.array([1.0, 2, 3]).dtype    # float64 (mixed → float upcast)
```


---

## 1. np.arange — Integer and Float Ranges

In ML you never type out 44,100 audio sample indices or 100 learning rates by hand. These factory functions generate exactly the structured sequences you need in one call.


```python
import numpy as np

# Syntax: np.arange(start, stop, step)
# stop is exclusive (like Python range())

np.arange(5)             # [0 1 2 3 4]       — stop only
np.arange(2, 8)          # [2 3 4 5 6 7]     — start + stop
np.arange(0, 10, 2)      # [0 2 4 6 8]       — with step
np.arange(1.0, 2.0, 0.3) # [1.  1.3  1.6  1.9] — float step
```

**Important:** With float steps, the number of elements is not always predictable due to floating-point rounding. `np.arange(0, 1, 0.1)` may produce 10 or 11 elements depending on platform.


![np.arange — Integer and Float Ranges](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_4.png)

## 2. np.linspace — N Evenly Spaced Points

```python
# Syntax: np.linspace(start, stop, num)
# stop is INCLUSIVE (unlike arange)
# num specifies exact count of elements

np.linspace(0, 1, 5)       # [0.   0.25  0.5   0.75  1.  ]
np.linspace(0, 10, 11)     # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10.]
np.linspace(0, 2*np.pi, 100)  # 100 points for trig functions
```

Use `linspace` when you need:
- Exactly N points (guaranteed)
- Stop point included
- Floating-point precision (plotting, signal processing)

## 3. np.zeros and np.ones — Initialisation Arrays

```python
# 1D
np.zeros(4)        # [0. 0. 0. 0.]
np.ones(3)         # [1. 1. 1.]

# 2D — pass a tuple
np.zeros((2, 3))
# [[0. 0. 0.]
#  [0. 0. 0.]]

np.ones((3, 3))
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# With explicit dtype
np.zeros((2, 2), dtype=int)
# [[0 0]
#  [0 0]]
```

Default dtype for `zeros` and `ones` is `float64`.

## 4. np.full — Fill with Any Value

```python
np.full((3, 3), 7)
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]

np.full(5, np.pi)
# [3.14159265 3.14159265 3.14159265 3.14159265 3.14159265]
```

## 5. arange vs. linspace — When to Use Which

| Feature | `arange` | `linspace` |
|---|---|---|
| You specify | step size | number of points |
| Stop included? | No | Yes |
| Float step safe? | No (rounding risk) | Yes |
| Integer sequences | Yes | Less natural |
| Plotting / signals | Risky | Preferred |

**Rule of thumb:** Use `arange` for integer sequences. Use `linspace` for any float range or when exact element count matters.

## 6. 2D Shape Arguments

Both `zeros` and `ones` accept an integer (1D) or a tuple (multi-dimensional):

```python
# Common mistake: passing two separate arguments instead of a tuple
np.zeros(3, 4)       # TypeError: wrong argument
np.zeros((3, 4))     # correct — (3, 4) is a tuple
```


---

## 1. np.random.rand — Uniform [0, 1)

Every ML model you train relies on randomness — weight initialisation, data shuffles, dropout. But "random" on a computer is actually pseudorandom: deterministic, and therefore reproducible with a seed.


Generates random floats uniformly distributed between 0 (inclusive) and 1 (exclusive):

```python
import numpy as np

# 1D array of 5 random values
np.random.rand(5)
# [0.37 0.95 0.73 0.60 0.16]  (example — varies each run)

# 2D array: pass shape as separate arguments (NOT a tuple)
np.random.rand(3, 4)   # 3×4 matrix, uniform [0, 1)
```

**Note:** Unlike `zeros((3, 4))`, `rand` takes separate dimension arguments, not a tuple: `rand(3, 4)` not `rand((3, 4))`.


![np.random.rand — Uniform [0, 1)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_5.png)

## 2. np.random.randn — Standard Normal Distribution

Generates random floats from a standard normal distribution (mean=0, std=1):

```python
np.random.randn(5)
# [-0.98  0.43  1.27 -0.32  0.85]  (example)

np.random.randn(2, 3)   # 2×3 matrix, normal(0, 1)
```

To generate normal values with a different mean and std:
```python
mean, std = 100, 15
iq_scores = mean + std * np.random.randn(1000)
# 1000 values ~ Normal(100, 15)
```

## 3. np.random.randint — Discrete Integers

Generates random integers from `low` (inclusive) to `high` (exclusive):

```python
# Single value between 0 and 9
np.random.randint(0, 10)

# Array of 8 random integers in [1, 7)
np.random.randint(1, 7, size=8)
# [3 5 1 6 2 4 5 3]

# 2D integer array
np.random.randint(0, 100, size=(3, 4))
```

## 4. np.random.seed — Reproducibility

Seeds the random number generator to a fixed state:

```python
np.random.seed(42)
print(np.random.rand(3))   # [0.374 0.951 0.732]

np.random.seed(42)
print(np.random.rand(3))   # [0.374 0.951 0.732]  — identical
```

Always set a seed at the top of notebooks and scripts that use randomness. Use any integer as the seed value — the specific value doesn't matter, only that it's fixed.

## 5. np.random.choice — Sampling From an Array

```python
arr = np.array([10, 20, 30, 40, 50])

# Sample 3 elements with replacement
np.random.choice(arr, size=3)          # e.g., [30 10 30]

# Sample 3 without replacement
np.random.choice(arr, size=3, replace=False)  # e.g., [50 20 10]
```

## 6. rand vs. randn — Key Differences

| Feature | `rand` | `randn` |
|---|---|---|
| Distribution | Uniform [0, 1) | Standard normal (mean=0, std=1) |
| Range | 0 to 1 | Unbounded (tails go to ±∞) |
| Typical use | Uniform sampling, Monte Carlo | Noise simulation, weight init |
| Shape argument | Separate args `rand(3, 4)` | Separate args `randn(3, 4)` |


---

## 1. Basic Indexing

A logistics platform tracks 1,000 delivery times. The ops manager needs the last five, every other, and the slowest in the first 100 — each is one line of NumPy, not a loop.


Select a single element using its position (zero-based):

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # 10  — first element
print(arr[2])    # 30  — third element
print(arr[-1])   # 50  — last element
print(arr[-2])   # 40  — second-to-last
```

Negative indices count backwards from the end: `-1` = last, `-2` = second-to-last.

Out-of-range indexing raises an `IndexError`:
```python
arr[10]    # IndexError: index 10 is out of bounds for axis 0 with size 5
```


![Basic Indexing](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_8.png)

## 2. Slicing — start:stop:step

```python
arr = np.array([0, 10, 20, 30, 40, 50, 60])

arr[1:4]     # [10 20 30]  — indices 1, 2, 3 (stop excluded)
arr[2:]      # [20 30 40 50 60]  — from index 2 to end
arr[:3]      # [ 0 10 20]  — from start to index 2
arr[::2]     # [ 0 20 40 60]  — every other element
arr[1::2]    # [10 30 50]  — odd-indexed elements
arr[::-1]    # [60 50 40 30 20 10  0]  — full reversal
arr[4:1:-1]  # [40 30 20]  — backwards from index 4 to 2
```

**Stop is always exclusive.** `arr[1:4]` returns indices 1, 2, 3 — never index 4.

## 3. Omitting Start, Stop, or Step

| Slice | Meaning |
|---|---|
| `arr[:]` | All elements (view of full array) |
| `arr[2:]` | From index 2 to end |
| `arr[:5]` | From start to index 4 |
| `arr[::3]` | Every third element |
| `arr[::-1]` | Entire array, reversed |

## 4. Slices Are Views

```python
arr = np.array([1, 2, 3, 4, 5])
s = arr[1:4]
s[0] = 99

print(arr)   # [ 1 99  3  4  5]  — original changed
```

Always use `.copy()` when you need an independent subset.

## 5. Modifying Elements via Index

```python
arr = np.array([5, 10, 15, 20, 25])

arr[2]   = 99     # single element
arr[1:4] = 0      # broadcast 0 to a range
arr[::2] = -1     # every other element

print(arr)   # [-1  0 -1  0 -1]
```

Assignment to a slice broadcasts the right-hand side if it's a scalar, or requires matching shape if it's an array.


---

## 1. Element Access in 2D Arrays

A healthcare dataset has 10,000 patients and 50 biomarkers. Extracting patient 42's cholesterol is `data[42, 3]`; extracting all glucose readings across every patient is `data[:, 7]`.


Use `arr[row, col]` for a single element:

```python
import numpy as np

m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(m[0, 0])    # 10  — top-left
print(m[1, 2])    # 60  — row 1, col 2
print(m[-1, -1])  # 90  — bottom-right (negative indexing works)
print(m[2, 1])    # 80
```

**Avoid `m[1][2]`** — chaining brackets works but is slower and less idiomatic than `m[1, 2]`.


![Element Access in 2D Arrays](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_9.png)

## 2. Row and Column Selection

```python
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Full row
print(m[0, :])    # [1 2 3]  — first row
print(m[1])       # [4 5 6]  — shorthand: row index only, no column

# Full column
print(m[:, 0])    # [1 4 7]  — first column
print(m[:, -1])   # [3 6 9]  — last column
```

`m[1]` is shorthand for `m[1, :]` — selecting a row without specifying columns.

## 3. Submatrix Slicing

```python
m = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])

# Rows 0-1, columns 1-2
print(m[0:2, 1:3])
# [[2 3]
#  [6 7]]

# Last two rows, last two columns
print(m[-2:, -2:])
# [[ 7  8]
#  [11 12]]

# Every other row, every other column
print(m[::2, ::2])
# [[ 1  3]
#  [ 9 11]]
```

## 4. 3D Array Indexing

For 3D arrays (e.g., batches of images), use three indices: `arr[batch, row, col]`:

```python
cube = np.arange(24).reshape(2, 3, 4)

print(cube[0])           # first 3×4 "slice" (block 0)
print(cube[1, 2, :])     # row 2 of block 1: [20 21 22 23]
print(cube[:, 0, :])     # first row of every block
```

## 5. Submatrix Assignment (Views)

```python
m = np.zeros((4, 4))
m[1:3, 1:3] = 5     # fill inner 2×2 with 5

print(m)
# [[0. 0. 0. 0.]
#  [0. 5. 5. 0.]
#  [0. 5. 5. 0.]
#  [0. 0. 0. 0.]]
```

2D slices are views — assignment modifies the original in place.


---

## 1. Array Concatenation

Data arrives in separate pieces — 12 monthly CSV files, or features and labels in different files. Before training a model, these must be stitched into one array. Concatenate and stack are the stitching tools.


Concatenating means gluing arrays together end-to-end. We use `np.concatenate([array1, array2, ...], axis=0)` for this.

**Requirement:** All input arrays must have the **exact same shape**, except in the dimension corresponding to `axis`, where they are being joined.

### 1D Arrays
Joining multiple flat arrays together creates a longer flat array.
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8])

combined = np.concatenate([x, y, z])
print(combined) # Output: [1 2 3 4 5 6 7 8]
```

### 2D Arrays (Matrices)
When dealing with grids, `axis` defines the direction of the glue. 
- `axis=0`: Glues the rows together (stacking vertically, adding new rows to the bottom).
- `axis=1`: Glues the columns together (stacking horizontally, adding new columns to the right).

```python
grid1 = np.array([[1, 2], 
                  [3, 4]]) # Shape (2, 2)
grid2 = np.array([[5, 6], 
                  [7, 8]]) # Shape (2, 2)

# Glue vertically (Default axis=0) -> Adds rows
v_joined = np.concatenate([grid1, grid2], axis=0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]] -> Shape (4, 2)

# Glue horizontally (axis=1) -> Adds columns
h_joined = np.concatenate([grid1, grid2], axis=1)
# [[1 2 5 6]
#  [3 4 7 8]] -> Shape (2, 4)
```


![Array Concatenation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_17.png)

## 2. Stacking Arrays (`np.vstack` & `np.hstack`)

While `concatenate` is technically all you need, NumPy provides convenience functions so you don't have to remember `axis=0` vs `axis=1`.

- `np.vstack([a, b])`: Vertically stacks (equivalent to `axis=0`).
- `np.hstack([a, b])`: Horizontally stacks (equivalent to `axis=1`).

```python
# Shorthand for vertical stacking
v_joined = np.vstack([grid1, grid2])

# Shorthand for horizontal stacking
h_joined = np.hstack([grid1, grid2])
```
*Tip:* You can horizontally stack a 1D column array onto a 2D matrix, but you must first ensure the 1D array is explicitly morphed into a column vector shape via reshaping or `np.newaxis`.

## 3. Creating a New Dimension (`np.stack`)

Sometimes you don't want to glue two 2D grids into a bigger 2D grid. You want to stack them perfectly on top of one another to create a 3D block (like stacking completely separate pages in a book).

Use `np.stack()`. This **creates a new axis**. The input arrays must have the exactly identical shape.

```python
page1 = np.array([[1, 2], [3, 4]])
page2 = np.array([[5, 6], [7, 8]])

book = np.stack([page1, page2], axis=0) 
print(book.shape) 
# Output: (2, 2, 2)  <- 2 pages, 2 rows, 2 columns
```

## 4. Array Splitting (`np.split`, `np.vsplit`, `np.hsplit`)

The inverse of stacking/concatenation is splitting. You provide an array, and the *number* of equal chunks you want, or an array of *indices* where to cut.

```python
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Split into exactly 4 equal chunks
chunks = np.split(x, 4)
print(chunks)
# Output: [array([10, 20]), array([30, 40]), array([50, 60]), array([70, 80])]
```

If you provide a list of integers, NumPy treats them as index slices where the "knife" should drop.
```python
# Cut AT index 2, and cut AT index 6
parts = np.split(x, [2, 6])
print(parts)
# Output: 
# [array([10, 20]),            <- Elements before index 2
#  array([30, 40, 50, 60]),    <- Elements from index 2 to 5
#  array([70, 80])]            <- Elements from index 6 to end
```

Similar to stacking, there are convenience functions for 2D grids:
- `np.vsplit(grid, N)`: Splits the grid vertically (cuts horizontally across rows).
- `np.hsplit(grid, N)`: Splits the grid horizontally (cuts vertically across columns).


---

## 1. Memory Layout: Lists vs. Arrays

A fintech fraud scan of 10 million transactions took 47 minutes with Python loops — and 11 seconds with NumPy. The difference comes down to how memory is laid out.


**Python list** stores a contiguous array of *pointers*, each pointing to a separate Python object on the heap:

```
list = [1, 2, 3]
→ [ptr→PyInt(1)] [ptr→PyInt(2)] [ptr→PyInt(3)]
   Each PyInt object: 28 bytes overhead + 8 bytes for the value
```

**NumPy array** stores raw values in a single contiguous block:
```
np.array([1, 2, 3])
→ [8 bytes] [8 bytes] [8 bytes]   (int64: 8 bytes each)
   Total: 24 bytes — no per-element overhead
```

Memory comparison for 1 million integers:
```python
import sys
import numpy as np

py_list = list(range(1_000_000))
np_arr  = np.array(py_list)

print(sys.getsizeof(py_list))  # ~8,000,056 bytes (~8 MB, pointers only)
print(np_arr.nbytes)           # 8,000,000 bytes (8 MB, raw int64 values)
# Python list total (including objects): ~35 MB
```


![Memory Layout: Lists vs. Arrays](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/numpy-fundamentals/lo_14_1_2.png)

## 2. Performance: Benchmarking the Difference

```python
import numpy as np
import timeit

py_list = list(range(1_000_000))
np_arr  = np.array(py_list)

# Python loop
t_list = timeit.timeit(lambda: [x * 2 for x in py_list], number=10)

# NumPy vectorized
t_np   = timeit.timeit(lambda: np_arr * 2, number=10)

print(f"List comprehension: {t_list:.3f}s")
print(f"NumPy operation:    {t_np:.3f}s")
print(f"Speedup: {t_list / t_np:.0f}x")
# Typical output: NumPy is 20x–100x faster
```

The speedup is not from a faster loop — there is no Python-level loop in the NumPy call. The `* 2` operation dispatches to a compiled C function.

## 3. Vectorization

Vectorization means applying an operation to all elements of an array without writing an explicit Python loop.

```python
import numpy as np

arr = np.array([1.0, 2.0, 3.0, 4.0])

# Element-wise operations (no loop needed)
print(arr + 10)       # [11. 12. 13. 14.]
print(arr * 3)        # [ 3.  6.  9. 12.]
print(arr ** 2)       # [ 1.  4.  9. 16.]
print(arr + arr)      # [ 2.  4.  6.  8.]  — two arrays, element-wise

# Equivalent Python (what you'd have to write with lists)
# result = [x ** 2 for x in py_list]  ← slow, verbose
```

Vectorization also makes code more readable — the mathematical intent is clear without loop boilerplate.

## 4. Type Homogeneity

Python lists hold mixed types. NumPy arrays enforce one dtype:

```python
py_list = [1, "two", 3.0, True]      # valid Python list
np_arr  = np.array([1, "two", 3.0])  # dtype becomes '<U32' — all strings

# NumPy's type inference rule:
# int + float → float64
# numeric + string → string (silent coercion — always check .dtype)
```

This constraint is a feature: it guarantees that any arithmetic you perform operates on predictable types at C speed.

## 5. When to Use Each

| Situation | Use |
|---|---|
| Numerical computation | NumPy array |
| Mixed data types | Python list |
| Frequent `.append()` / `.pop()` | Python list |
| Large-scale math / ML / data science | NumPy array |
| Small, non-numeric sequences | Python list |


---

