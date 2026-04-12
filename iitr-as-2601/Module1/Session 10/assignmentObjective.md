# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

Why are NumPy arrays significantly faster than Python lists for numerical computation?

A) NumPy uses Python loops internally
B) NumPy stores numbers as Python objects
C) NumPy uses contiguous memory and optimized C code
D) NumPy avoids using memory altogether

**Correct answer:** C

**Explanation:**
NumPy arrays store data in contiguous blocks of memory and perform operations using highly optimized C implementations. This avoids Python-level loops and object overhead, making numerical operations dramatically faster and more memory-efficient.

---

### **2. (MCQ)**

What is the most important restriction of a NumPy array compared to a Python list?

A) NumPy arrays cannot be resized
B) NumPy arrays must store elements of the same data type
C) NumPy arrays cannot perform arithmetic operations
D) NumPy arrays cannot be multidimensional

**Correct answer:** B

**Explanation:**
All elements in a NumPy array share the same data type (homogeneous). This restriction enables efficient storage and fast vectorized computation, which is the core reason NumPy exists.

---

### **3. (MCQ)**

Which line correctly squares every element of a NumPy array `arr`?

A) `arr.square()`
B) `square(arr)`
C) `arr ** 2`
D) `for x in arr: x**2`

**Correct answer:** C

**Explanation:**
NumPy supports **vectorized operations**, meaning arithmetic applies element-wise across the entire array. `arr ** 2` squares every element without using an explicit loop.

---

### **4. (MCQ)**

What is the shape of the following array?

```python
arr = np.array([1, 2, 3, 4])
```

A) `(1, 4)`
B) `(4, 1)`
C) `(4,)`
D) `(2, 2)`

**Correct answer:** C

**Explanation:**
This is a one-dimensional NumPy array with four elements. NumPy represents this shape as `(4,)`, indicating a single axis of length 4.

---

### **5. (MCQ)**

What does the following code produce?

```python
np.arange(0, 10, 2)
```

A) `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
B) `[0, 2, 4, 6, 8]`
C) `[2, 4, 6, 8, 10]`
D) `[0, 2, 4, 6, 8, 10]`

**Correct answer:** B

**Explanation:**
`np.arange(start, stop, step)` generates values starting at `start`, increasing by `step`, and stopping *before* `stop`. Here, values go from 0 to 8 in steps of 2.

---

### **6. (MCQ)**

Which rule must always be satisfied when reshaping a NumPy array?

A) The number of rows must equal the number of columns
B) The new shape must be square
C) The total number of elements must remain the same
D) The array must be one-dimensional

**Correct answer:** C

**Explanation:**
`reshape()` changes how data is viewed, not the data itself. Therefore, the total number of elements before and after reshaping must remain unchanged.

---

### **7. (MCQ)**

What is the shape of the following array?

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

A) `(3, 2)`
B) `(2, 3)`
C) `(6,)`
D) `(2,)`

**Correct answer:** B

**Explanation:**
The array has **2 rows and 3 columns**, so its shape is `(2, 3)`. This row-column interpretation is central to how NumPy represents multidimensional data.

---

### **8. (MCQ)**

Why is vectorization preferred over Python loops in AI and numerical pipelines?

A) Vectorized code uses more memory
B) Vectorized code is harder to read
C) Vectorized operations execute in optimized low-level code
D) Vectorized code only works for small arrays

**Correct answer:** C

**Explanation:**
Vectorized operations allow NumPy to delegate computation to optimized C routines, minimizing Python overhead and enabling large-scale numerical computation essential for AI workloads.