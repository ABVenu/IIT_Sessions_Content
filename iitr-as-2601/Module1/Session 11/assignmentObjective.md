# Assignment 1: Objective Type Questions

---

### **1. (MCQ)**

Why do AI models rely heavily on **multidimensional NumPy arrays**?

A) They reduce code length
B) They allow storing mixed data types
C) They represent real-world data in structured numerical form
D) They replace the need for algorithms

**Correct answer:** C

**Explanation:**
AI models operate on numerical data arranged in structured forms such as vectors, matrices, and tensors. Multidimensional NumPy arrays encode this structure (samples, features, pixels, channels), which directly affects correctness and learning behavior.

---

### **2. (MCQ)**

What does the shape `(2, 3)` of a NumPy array represent?

A) 2 elements, each with 3 bytes
B) 3 rows and 2 columns
C) 2 rows and 3 columns
D) A one-dimensional array with 6 elements

**Correct answer:** C

**Explanation:**
In NumPy, shape is expressed as `(rows, columns)` for 2D arrays. A shape of `(2, 3)` means the array has 2 rows and 3 columns.

---

### **3. (MCQ)**

What is the key performance characteristic of NumPy slicing?

A) It always creates a deep copy
B) It returns a Python list
C) It usually returns a view into the original array
D) It converts arrays to tuples

**Correct answer:** C

**Explanation:**
NumPy slicing typically returns a **view**, not a copy. This allows efficient memory usage and fast operations, but also means modifying the slice can modify the original array.

---

### **4. (MCQ)**

What will happen after executing the following code?

```python
slice_view = matrix[:2, :2]
slice_view[0, 0] = 999
```

A) Only `slice_view` changes
B) Only `matrix` changes
C) Both `slice_view` and `matrix` change
D) An error is raised

**Correct answer:** C

**Explanation:**
Because slicing returns a view, both `slice_view` and the original `matrix` reference the same underlying data. Modifying the slice modifies the original array as well.

---

### **5. (MCQ)**

Why is NumPy broadcasting essential for AI computations?

A) It removes the need for NumPy arrays
B) It allows operations on arrays of different but compatible shapes
C) It converts arrays into scalars
D) It preserves insertion order

**Correct answer:** B

**Explanation:**
Broadcasting allows NumPy to perform element-wise operations across arrays with compatible shapes without explicit loops. This is crucial for operations like bias addition, normalization, and scaling in ML pipelines.

---

### **6. (MCQ)**

Which condition must be satisfied for NumPy broadcasting to work?

A) All arrays must have the same shape
B) Dimensions must match exactly
C) From right to left, dimensions must match or one must be 1
D) Arrays must be one-dimensional

**Correct answer:** C

**Explanation:**
NumPy compares shapes from right to left. For each dimension, they must be equal or one of them must be `1`. If this rule is violated, broadcasting fails.

---

### **7. (MCQ)**

Why is setting a random seed important in AI experiments?

A) It increases randomness
B) It improves model accuracy
C) It ensures reproducibility of results
D) It speeds up random number generation

**Correct answer:** C

**Explanation:**
Setting a random seed ensures that randomly generated numbers remain the same across runs. This is essential for debugging, experimentation, and scientific reproducibility in AI workflows.

---

### **8. (MCQ)**

Which NumPy function is commonly used to initialize model weight matrices?

A) `np.arange()`
B) `np.zeros()`
C) `np.random.randn()`
D) `np.linspace()`

**Correct answer:** C

**Explanation:**
`np.random.randn()` generates values from a standard normal distribution and is widely used to initialize weights in machine learning and deep learning models.
