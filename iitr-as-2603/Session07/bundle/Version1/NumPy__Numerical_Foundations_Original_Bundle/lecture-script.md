---

## 1. NumPy and the ndarray

### Why

A factory vision system inspects 4,000 camera images per second — every millisecond of Python loop overhead causes missed defects and lost product. NumPy arrays store data in a single contiguous block of C memory and execute operations in compiled C code, making the difference between shipping a real-time system and not shipping it at all.

Ask the room: "Who here has written a Python for-loop over a list of numbers?" (Pause.) "You\'re about to write your last one for numerical work."
### What

NumPy's central object is the `ndarray` — N-dimensional array. Unlike a Python list (which is an array of pointers, each pointing to an individual Python object), a NumPy array stores raw numbers contiguously in memory.

Draw or show the S3 slide: Python list as boxes-with-pointers vs. NumPy array as a flat memory strip.

### How

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
```

Run this live. Point out: no commas in output, it prints as `[1 2 3 4 5]`. Ask: "Why no commas?" — because it's not a Python list. It's a different object.

---

## 2. Installing NumPy

### Why

"Most of you are probably in Colab or Anaconda — NumPy is already there. But in a production environment or a bare Python install, you'll need to handle this yourself."

### What

Installation pathways: pip, conda, and pre-installed environments (Colab, Jupyter). The import alias `np` is convention — not enforced, but universal. Code that uses any other alias will confuse your teammates.

### How

Walk through live in the terminal / notebook:

```bash
pip install numpy   # if not installed
```

```python
import numpy as np
print(np.__version__)
```

"If this line runs without error, you're ready. Version doesn't matter much for today's content — anything above 1.20 works."

---

## 3. Creating Arrays from Lists

### Why

"Everything in NumPy starts with an array. Before you index, slice, reshape, or compute — you need to know how to make one. `np.array()` is the Swiss Army knife for that."

### What

`np.array()` takes any Python sequence (list, tuple, nested list) and converts it to an ndarray. It infers the dtype automatically — but you can override it.

Key rule: all elements must be compatible types. NumPy will upcast when needed (int → float), and silently convert everything to strings if you mix strings with numbers.

### How

**1D array:**
```python
a = np.array([10, 20, 30])
print(a, a.dtype)  # [10 20 30] int64
```

**2D array:**
```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m)
print(m.shape)  # (2, 3)
```

**Explicit dtype:**
```python
f = np.array([1, 2, 3], dtype=float)
print(f)        # [1. 2. 3.]
print(f.dtype)  # float64
```

**Live debugging exercise:** Show this code and ask what's wrong:
```python
broken = np.array([[1, 2, 3], [4, 5]])
print(broken.dtype)
```
Answer: ragged list → object dtype. This is a silent failure — always watch for it.

Wrap up: "The next several LOs build directly on this. If you can't make an array, none of the rest works."


---

---

## 1. Shape

### Why

A GPS tracking system logs positions for 50,000 delivery vehicles, 24 times per day — before running any calculation, the engineer asks: how many rows? How many columns? What data type? A shape mismatch between two arrays crashes a pipeline silently, or worse, produces wrong results with no error. Checking `.shape`, `.dtype`, and `.ndim` before every operation is the first habit of production data engineers.

### What

`.shape` is a tuple where each element gives the size along that dimension. A 2D array with 5 rows and 3 columns has shape `(5, 3)`. A 1D array with 4 elements has shape `(4,)` — note the trailing comma, it's still a tuple.

### How

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a.shape)   # (4,)

m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.shape)   # (2, 3)
```

Show the diagram:

Ask: "What would the shape be for a colour image — 256 pixels wide, 256 tall, 3 colour channels?" Answer: `(256, 256, 3)`.

---

## 2. dtype

### Why

"dtype determines how much memory each element uses and what operations are valid on it. In production ML pipelines, using float32 instead of float64 cuts memory in half and often doubles GPU throughput. Using the wrong dtype in financial software can introduce rounding errors that compound over millions of rows."

### What

`.dtype` reports the data type: `int32`, `int64`, `float32`, `float64`, `bool`, `complex128`, etc. NumPy infers dtype automatically but you can override it.

### How

```python
a = np.array([1, 2, 3])
print(a.dtype)   # int64

b = np.array([1, 2, 3.0])
print(b.dtype)   # float64  (upcast)

c = np.array([1, 2, 3], dtype=np.float32)
print(c.dtype)   # float32
print(c.nbytes)  # 12
```

Live demo: show that `np.array([1, "2", 3]).dtype` prints a string dtype — then ask students to predict it before running.

---

## 3. ndim, size, nbytes

### Why

"ndim tells you how many indices you need to address an element. size gives you the total count — useful for loops and data validation. nbytes tells you the memory footprint before you load a 10 GB array."

### What

- `ndim` = number of axes = `len(arr.shape)`
- `size` = total elements = product of all shape values
- `nbytes` = `size × itemsize` (bytes per element for the dtype)

### How

```python
m = np.array([[1, 2, 3], [4, 5, 6]])

print(m.ndim)    # 2
print(m.size)    # 6
print(m.nbytes)  # 48  (6 elements × 8 bytes for int64)

# Cross-check
print(m.size * m.itemsize == m.nbytes)  # True
```

Wrap-up exercise: "Given an array `arr`, what is `arr.size` if `arr.shape` is `(4, 3, 2)`?" Answer: 24. Students should be able to compute this without running code.


---

---

## 1. arange

### Why

"In data science you constantly need sequences — indices, time steps, feature ranges. Writing `np.array([0, 1, 2, ..., 99])` by hand is never an option. `np.arange()` is NumPy's answer to Python's `range()` — but it gives you an actual array."

### What

`np.arange(start, stop, step)` creates an array from `start` up to but not including `stop`, incrementing by `step`. Like Python's `range()`, the stop is exclusive. Unlike `range()`, it supports float steps and returns an ndarray.

### How

```python
import numpy as np

print(np.arange(5))           # [0 1 2 3 4]
print(np.arange(2, 10, 2))    # [2 4 6 8]
print(np.arange(0.0, 1.0, 0.25))  # [0.   0.25  0.5   0.75]
```

Live gotcha — run this:
```python
print(len(np.arange(0, 1, 0.1)))
```
Ask students to predict: "10 or 11 elements?" The answer can surprise them (sometimes 11). This is float precision rounding. "This is exactly why `linspace` exists."

---

## 2. linspace

### Why

"If you're building a time axis for audio at 44,100 Hz, you need exactly 44,100 evenly spaced points between 0 and 1. With `arange`, you'd risk one extra or one missing point. With `linspace`, you specify the count — NumPy handles the math."

### What

`np.linspace(start, stop, num)` — generates exactly `num` points from `start` to `stop`, inclusive. You control element count, not step size. Stop IS included.

### How

```python
print(np.linspace(0, 1, 5))
# [0.   0.25  0.5   0.75  1.  ]

# Plotting axes
import numpy as np
x = np.linspace(0, 2 * np.pi, 100)
# 100 x-values for one full cycle of a sine wave
```

"Notice the last value is exactly `1.0` — the endpoint is included. With `arange(0, 1, 0.25)` the endpoint `1.0` would be excluded."

---

## 3. zeros / ones

### Why

"Before you fill a weight matrix with learned values, it starts as zeros. Before you apply a mask to an image, it starts as ones. Zeros and ones are the blank canvas of numerical computing."

### What

`np.zeros(shape)` and `np.ones(shape)` create float64 arrays filled with 0.0 and 1.0. Pass an int for 1D or a tuple for multi-dimensional.

### How

```python
print(np.zeros(4))          # [0. 0. 0. 0.]
print(np.ones((2, 3)))
# [[1. 1. 1.]
#  [1. 1. 1.]]

# With dtype
print(np.zeros((3, 3), dtype=int))
```

Common mistake to show and fix:
```python
np.zeros(3, 4)    # TypeError — not a tuple
np.zeros((3, 4))  # correct
```

"That extra pair of parentheses makes it a tuple argument. It's the number one `zeros` bug."

Wrap-up: "Between `arange`, `linspace`, `zeros`, and `ones`, you have a starting array for almost every data science task. Next we'll look at adding randomness."


---

---

## 1. Why Random Arrays

### Why

"Every ML model you'll ever train involves randomness: random weight initialisation, random data splits, random mini-batches, random dropout. Every simulation — stock prices, epidemic spread, particle physics — involves sampling from distributions. NumPy's random module is the engine behind all of it."

"And here's the paradox: computers can't be truly random. They use deterministic algorithms that *look* random. The upside: you can control them — which means your experiments are reproducible."

### What

NumPy's `random` module generates pseudorandom numbers from configurable distributions. The two most important are uniform (all values equally likely) and standard normal (values clustered around zero, tapering off at extremes).

### How

```python
import numpy as np

# Uniform [0, 1) — 5 values
print(np.random.rand(5))

# Standard normal (mean=0, std=1) — 5 values
print(np.random.randn(5))
```

Run these twice. Ask: "Same results both times?" No — they change. That's the point of randomness.

---

## 2. randint and seed

### Why

"Sometimes you need random integers — simulating dice rolls, random array indices, discrete categories. And sometimes you need your randomness to be reproducible — for science, for sharing code, for debugging."

### What

`randint(low, high, size)` generates integers in `[low, high)`. `seed(n)` fixes the random generator's starting state — after seeding, every random call produces the same values.

### How

```python
# Random integers: 6-sided dice, 10 rolls
np.random.randint(1, 7, size=10)
# e.g., [3 1 4 1 5 9 2 6 5 3]  — different each time

# Reproducible — seed fixes the state
np.random.seed(0)
print(np.random.rand(3))   # [0.549 0.716 0.603]

np.random.seed(0)
print(np.random.rand(3))   # [0.549 0.716 0.603]  — identical
```

"Always set your seed at the top of a notebook. The number `42` is a meme in data science — pick any integer."

---

## 3. Distributions — rand vs. randn in Practice

### Why

"The choice of distribution is not cosmetic. Initialising neural network weights from a uniform [0, 1] distribution causes gradient vanishing in deep networks. Using a standard normal (scaled appropriately) keeps gradients healthy. The distribution shapes your model's learning dynamics."

### What

- `rand` — uniform: every value between 0 and 1 is equally likely. No concentration around any value.
- `randn` — normal: values cluster around 0. About 68% of values fall within ±1, 95% within ±2.

### How

```python
# Custom normal: scale and shift randn
mean, std = 170, 10
heights = mean + std * np.random.randn(1000)
# 1000 synthetic human heights (cm), ~Normal(170, 10)

# Verify
print(f"Mean: {heights.mean():.1f}")   # ~170
print(f"Std:  {heights.std():.1f}")    # ~10
```

Live demo: compute mean and std, show they match the target. "This is how synthetic datasets are generated for testing algorithms before real data is available."

Wrap up: "Five functions — `rand`, `randn`, `randint`, `seed`, `choice` — cover 95% of random array needs in data science. Next LO: we'll use these to understand copy vs. view semantics."


---

---

## 1. Basic Indexing

### Why

A logistics platform stores 1,000 delivery times in an array. The ops manager needs the last five deliveries, every other data point for a trend sample, and the slowest time in the first 100 entries — each is one line of NumPy indexing, not a loop. Slicing lets you describe *what* you want; NumPy computes *where* it lives in memory directly.

### What

Zero-based indexing: element 0 is first. Negative indexing counts from the end: `-1` is last. Accessing an out-of-range index raises `IndexError`.

### How

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[-2])   # 40
```

Ask: "What does `arr[-3]` return?" Answer: 30. Make students count backwards mentally before running.

---

## 2. Slicing

### Why

"Indexing gets one element. Slicing gets a range. Time-series analysis, train/test splits, windowed operations — all of these are slices. The syntax is compact enough that once you know it, you never want to write a loop again."

### What

`arr[start:stop:step]` — start (inclusive), stop (exclusive), step. Any part can be omitted. Negative step reverses direction.

### How

```python
arr = np.array([0, 10, 20, 30, 40, 50, 60])

print(arr[1:4])    # [10 20 30]
print(arr[::2])    # [ 0 20 40 60]  — every other
print(arr[::-1])   # [60 50 40 30 20 10  0]  — reversed
```

Live exercise: "Write a one-liner to get the last 3 elements." Multiple valid answers: `arr[-3:]` or `arr[4:]`. Both correct — which is more robust when array length changes? `-3:` is.

---

## 3. Slices as Views and In-Place Assignment

### Why

"Slices are views — we covered this in the Copy vs View LO. Here's why it matters for indexing: you can use slices on the left side of an assignment to modify a range of elements in one line. This is used constantly in data cleaning, signal processing, and ML preprocessing."

### What

Assignment to a slice writes values into the original array. A scalar broadcasts to the entire slice. An array must match the slice shape.

### How

```python
arr = np.array([1, 2, 3, 4, 5, 6])
arr[1:4] = 0        # zero out middle
print(arr)          # [1 0 0 0 5 6]

arr[::2] = -1       # alternate elements
print(arr)          # [-1  0 -1  0 -1  6]
```

"This is how you'd zero out a specific time window in a signal, or mark certain indices as invalid in a pipeline — single expressions, no loops."


---

---

## 1. Element Access in 2D

### Why

A healthcare dataset has 10,000 patients and 50 biomarkers — each patient is a row, each biomarker is a column. To get patient 42's cholesterol level you write `data[42, 3]`. To extract every patient's glucose reading for a model feature, you write `data[:, 7]`. NumPy's comma notation is the direct translation of "row, column" thinking into code.

### What

Two-dimensional indexing uses a single pair of brackets with two values separated by a comma: `arr[row, col]`. Both can be integers for a single element, or slices for ranges. Negative indexing applies to both dimensions independently.

### How

```python
import numpy as np

m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(m[1, 2])     # 60  — row 1, column 2
print(m[-1, -1])   # 90  — bottom-right
```

Ask: "What does `m[0, -1]` return?" Answer: 30 (first row, last column). Quiz-style before running.

---

## 2. Row and Column Extraction

### Why

"Extracting a column from a dataset is one of the most common operations in data science — selecting a feature, a target variable, a time series from a larger table. In pandas you'd do `df['column_name']`. In NumPy, you use `arr[:, col_index]`."

### What

The `:` colon means "all along this axis". `arr[0, :]` = entire first row. `arr[:, 2]` = entire third column. Either axis can be a slice or a single index.

### How

```python
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(data[1, :])    # [4 5 6]  — row 1
print(data[:, 1])    # [2 5 8]  — column 1
print(data[1])       # [4 5 6]  — shorthand for row
```

"Pull up a mental spreadsheet. Row 1 is the horizontal band. Column 1 is the vertical strip. Both are single-expression extractions."

---

## 3. Submatrix Slicing and Assignment

### Why

"In image processing, you patch a region of pixels. In signal processing, you zero out a frequency band in a spectrogram. In ML, you extract a batch of samples with specific features. All of these are 2D submatrix operations."

### What

Combine row and column slices: `arr[r_start:r_stop, c_start:c_stop]`. The result is a 2D view. Assignment to this slice modifies the original array in place.

### How

```python
m = np.zeros((5, 5))
m[1:4, 1:4] = 7    # fill inner 3×3 block

print(m)
# [[0. 0. 0. 0. 0.]
#  [0. 7. 7. 7. 0.]
#  [0. 7. 7. 7. 0.]
#  [0. 7. 7. 7. 0.]
#  [0. 0. 0. 0. 0.]]
```

"This is exactly how image watermarking, convolution padding, and masking work at the array level."


---

## 1. Array Concatenation

### Why
In data science pipelines, data almost never arrives completely packaged. It arrives in 12 monthly CSV files, or it arrives with X (features) in one file and Y (labels) in another file. Before we can train a model, we must stitch these separate variables back into a single unified grid. 

### What
`np.concatenate()` takes a list or tuple of matrices and glues them together end-to-end. The crucial parameter is `axis`. `axis=0` glues them along the row dimension (stacking data top-to-bottom). `axis=1` glues them along the column dimension (stacking data left-to-right side-by-side).

### How
Demonstrate combining two 1D arrays, and then two 2D arrays along both axes.

```python
import numpy as np

# 1D concatenation is simple end-to-end glue
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate([a, b])) # [1, 2, 3, 4, 5, 6]

# 2D matrices have choices!
grid1 = np.array([[1, 2], [3, 4]])
grid2 = np.array([[5, 6], [7, 8]])

# Stack vertically (axis=0) -> 4 rows, 2 columns
print(np.concatenate([grid1, grid2], axis=0))

# Stack horizontally (axis=1) -> 2 rows, 4 columns
print(np.concatenate([grid1, grid2], axis=1))

# What happens if they don't match?
# np.concatenate([grid1, a], axis=0) # ERROR: shape mismatch!
```

---

## 2. Stacking Convenience Functions

### Why
Typing `np.concatenate([a, b], axis=1)` every time gets repetitive and visually cluttered. We need readable, expressive shorthand for the most common operations.

### What
`np.vstack()` (vertical stack) and `np.hstack()` (horizontal stack) do exactly what `concatenate` does, but they bake in the `axis` parameter implicitly. Furthermore, `np.stack()` creates an entirely *new* physical dimension (e.g. turning two 2D images into one 3D array), instead of gluing them on existing edges.

### How
Show `vstack` and `hstack` quickly.

```python
print(np.vstack([grid1, grid2])) # Same as axis=0
print(np.hstack([grid1, grid2])) # Same as axis=1
```

Then demonstrate why `np.stack()` is special. This blows students' minds if they don't visually grasp 3D structures.

```python
# We have two 2D grids (representing 2 grayscale images)
img1 = np.ones((2, 2))
img2 = np.zeros((2, 2))

# We want a 3D dataset shaped (2 images, height, width).
combined_3d = np.stack([img1, img2], axis=0)

print(combined_3d.shape) # (2, 2, 2)
# We now have a true 3D tensor!
```

---

## 3. Array Splitting

### Why
The opposite scenario! You finally have a massive 100,000 row dataset. But before you build a model, standard practice dictates splitting the data: 80% to "train" the model, and 20% to "test" the model. Or maybe you need to chop the dataset into 10 equal "batches" because your GPU RAM is too small to handle it all at once. We need a way to slice arrays precisely.

### What
`np.split()` divides an array. You can pass it an integer `N` (it will try to split it into precisely `N` equal chunks and throws an error if it doesn't divide evenly). Or, much more powerfully, you can pass it a list of index numbers, and NumPy will "drop the knife" at those exact indices.

### How
Show splitting by equal chunks, then show splitting by specific indices. Just like `vstack`, mention the `vsplit` and `hsplit` convenience wrappers for multidimensional grids.

```python
data = np.arange(10) # [0,1,2,3,4,5,6,7,8,9]

# 1. Equal chunks
chunks = np.split(data, 2)
print("Chunk 1:", chunks[0]) # [0,1,2,3,4]
print("Chunk 2:", chunks[1]) # [5,6,7,8,9]

# 2. Split by specific indices (Train/Validation/Test split!)
# Let's say we want:
# index 0 to 6 in array A (Train)
# index 6 to 8 in array B (Val)
# index 8 to end in array C (Test)

# We drop the knife at index 6 and index 8
train, val, test = np.split(data, [6, 8])

print("Train:", train) # [0 1 2 3 4 5]
print("Val:", val)     # [6 7]
print("Test:", test)   # [8 9]
```


---

---

## 1. Performance

### Why

"You've built a list, you know how to loop over it. So when does it matter that NumPy is faster? The answer: the moment your data has more than a few thousand rows."

Tell the fintech story: 10 million transactions, 47 minutes with a loop, 11 seconds with NumPy. Ask: "Same CPU, same logic, same data — what changed?"

### What

Python lists store pointers to Python objects. Each element in a list is a full Python object with 28 bytes of overhead for a simple integer. When you iterate, Python interprets each object one at a time at the Python VM level.

NumPy stores raw numeric values in a contiguous memory block. Operations are dispatched to pre-compiled C/Fortran routines. The CPU processes multiple values per clock cycle using SIMD instructions.

### How

Live benchmark:
```python
import numpy as np, timeit

py_list = list(range(1_000_000))
np_arr  = np.array(py_list)

t_list = timeit.timeit(lambda: [x * 2 for x in py_list], number=10)
t_np   = timeit.timeit(lambda: np_arr * 2, number=10)
print(f"Speedup: {t_list/t_np:.0f}x")
```

Run this live. Let students see the number. "This is why your ML library isn't built in pure Python."

---

## 2. Vectorization

### Why

"Imagine needing to scale 10 million sensor readings by a calibration factor. With a list you'd write a comprehension or loop. With NumPy, you write one expression — and it's not just cleaner, it's executing entirely in compiled C."

### What

Vectorization = applying an operation to an entire array at once, without Python-level iteration. The operation is "mapped" over the array by a C routine, not a Python for-loop.

### How

```python
arr = np.array([1.0, 2.0, 3.0, 4.0])

print(arr * 2)      # [ 2.  4.  6.  8.]
print(arr + arr)    # [ 2.  4.  6.  8.]
print(arr ** 2)     # [ 1.  4.  9. 16.]
```

Compare to:
```python
result = [x * 2 for x in arr]  # still works, but defeats the purpose
```

Ask: "What's wrong with the second version?" — It loops in Python, bypassing NumPy's speed. Always operate on the array directly.

---

## 3. Memory

### Why

"If your dataset is 500 MB as a Python list, it might be 150 MB as a NumPy array. That's the difference between fitting in RAM and crashing your notebook."

### What

Python list memory = pointer array + per-element Python objects (~28 bytes overhead each). NumPy array memory = `n × dtype_size` bytes. For int64: 8 bytes per element. For float32: 4 bytes.

### How

```python
import sys
import numpy as np

py_list = list(range(1_000_000))
np_arr  = np.array(py_list)

print(sys.getsizeof(py_list))  # pointer array only: ~8 MB
print(np_arr.nbytes)           # 8 MB (int64)
# Actual list memory: ~35 MB (including all PyInt objects)
```

Wrap up: "Every time you write `np.array(...)`, remember you're not just calling a constructor — you're moving your data from Python-world into a tight, low-level memory format that everything fast in data science is built on."


---

