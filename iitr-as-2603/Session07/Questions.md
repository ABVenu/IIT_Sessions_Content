# Session 07 — Practice Questions
*Topics: Analytics context, NumPy fundamentals, array creation, attributes, indexing/slicing, random generation, stacking/splitting, and performance vs Python lists.*

---

## Objective Questions (8)

### Easy

**Q1 (Single Correct).** Which statement best describes **NumPy ndarray**?

- (A) It can store mixed Python objects of different types for speed.
- (B) It is a homogeneous, contiguous-memory array that supports vectorized operations.
- (C) It is only for plotting charts and graphs.
- (D) It is slower than Python lists for numerical math because it avoids C code.

**Answer:** **(B)**  
`ndarray` stores one dtype in contiguous memory and supports vectorized operations, which is why it is efficient for numerical computing.

---

**Q2 (Single Correct).** Which command correctly creates a 2x3 array of zeros?

- (A) `np.zeros(2, 3)`
- (B) `np.zeros((2, 3))`
- (C) `np.zeros([2:3])`
- (D) `np.zeros(2*3, dtype=(2, 3))`

**Answer:** **(B)**  
`np.zeros` expects a shape tuple for multidimensional arrays.

---

**Q3 (Multiple Correct).** Select all correct statements about basic array attributes.

- (A) `arr.shape` returns a tuple.
- (B) `arr.ndim` is the number of axes.
- (C) `arr.dtype()` is the correct way to access dtype.
- (D) `arr.size` gives total element count.

**Answer:** **(A), (B), (D)**  
`shape`, `ndim`, `dtype`, and `size` are attributes. `dtype()` is incorrect because `dtype` is not a method.

---

### Medium

**Q4 (Single Correct).** For `a = np.array([1, 2, 3, 4])`, what is the shape of `a.reshape(-1, 1)`?

- (A) `(4,)`
- (B) `(1, 4)`
- (C) `(4, 1)`
- (D) `(2, 2)`

**Answer:** **(C)**  
`reshape(-1, 1)` converts a 1D array into a column vector with one column.

---

**Q5 (Multiple Correct).** Choose all true statements comparing `np.arange` and `np.linspace`.

- (A) `np.arange` uses an exclusive stop.
- (B) `np.linspace` always excludes the stop value.
- (C) `np.linspace` is preferred when exact number of points is required.
- (D) Float-step `np.arange` can be sensitive to floating-point rounding.

**Answer:** **(A), (C), (D)**  
`linspace` includes stop by default and is often safer for controlled float grids.

---

**Q6 (Single Correct).** Given:
```python
arr = np.array([1, 2, 3, 4, 5])
s = arr[1:4]
s[0] = 99
```
What is `arr` afterward?

- (A) `[1, 2, 3, 4, 5]`
- (B) `[1, 99, 3, 4, 5]`
- (C) `[99, 2, 3, 4, 5]`
- (D) Error: NumPy slices are immutable

**Answer:** **(B)**  
Slices are views by default, so modifying `s` updates the original array.

---

### Hard

**Q7 (Multiple Correct).** You have:
```python
g1 = np.array([[1, 2], [3, 4]])   # shape (2, 2)
g2 = np.array([[5, 6], [7, 8]])   # shape (2, 2)
```
Select all operations that produce shape `(2, 4)`.

- (A) `np.concatenate([g1, g2], axis=1)`
- (B) `np.hstack([g1, g2])`
- (C) `np.vstack([g1, g2])`
- (D) `np.stack([g1, g2], axis=0)`

**Answer:** **(A), (B)**  
Horizontal join adds columns -> `(2, 4)`. `vstack` gives `(4, 2)`, and `stack` creates a new axis -> `(2, 2, 2)`.

---

**Q8 (Single Correct).** Why is NumPy usually much faster than Python lists for large numeric element-wise operations?

- (A) NumPy uses mixed data types in one array to reduce conversions.
- (B) NumPy operations are executed as vectorized compiled routines over contiguous memory.
- (C) NumPy always runs operations in parallel on GPU.
- (D) Python lists store raw integers without object overhead.

**Answer:** **(B)**  
Speed comes mainly from contiguous memory and C-level vectorized routines, avoiding Python-loop overhead.

---

## Subjective Question (1)

**Difficulty:** Medium to Hard  
**Type:** Implementation (coding)

**Q9.** Write a NumPy-based function to analyze 7-day DAU (Daily Active Users) data:

### Problem Statement
Given a Python list of daily DAU values:
```python
[120, 118, 125, 130, 128, 135, 140]
```
Implement a function:
```python
def analyze_dau(dau_list):
    ...
```
that returns:

1. Mean DAU of all 7 days.
2. Difference between mean of last 3 days and mean of first 3 days.
3. A Boolean `is_uptrend` which is `True` when the value from (2) is positive, else `False`.

### Constraints
- Must use NumPy arrays and vectorized operations (`np.array`, slicing, `.mean()`).
- Do not use explicit Python loops for calculations.
- Return values in a dictionary with keys: `mean_dau`, `trend_delta`, `is_uptrend`.

---

### Sample detailed solution

```python
import numpy as np

def analyze_dau(dau_list):
    # Convert input list to NumPy array for vectorized computation
    dau = np.array(dau_list, dtype=float)

    # Overall average across all days
    mean_dau = dau.mean()

    # Session logic: compare last 3 days with first 3 days
    first3_mean = dau[:3].mean()
    last3_mean = dau[-3:].mean()
    trend_delta = last3_mean - first3_mean

    # Positive delta means improving engagement trend
    is_uptrend = trend_delta > 0

    return {
        "mean_dau": mean_dau,
        "trend_delta": trend_delta,
        "is_uptrend": is_uptrend
    }

# Example usage
result = analyze_dau([120, 118, 125, 130, 128, 135, 140])
print(result)
```

### Explanation
- `np.array(..., dtype=float)` ensures numeric consistency.
- `dau.mean()` computes descriptive average DAU.
- `dau[:3]` and `dau[-3:]` are slices for first and last 3 days.
- Comparing these means gives a simple diagnostic trend signal.
- This mirrors session emphasis: array slicing + vectorized aggregation for analytics decisions.

### Expected output for the given input
- `mean_dau` = `128.0`
- `trend_delta` approx `13.3333` (positive)
- `is_uptrend` = `True`
