## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-numpy-assignment`).

3. Write **separate Python files** for each question inside this folder.

4. For each program:

   * Run the code in the **terminal**
   * Verify the **output**

5. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

6. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repo).

---

### **Question: NumPy-Based Data Normalization Pipeline**

**Task:**
Build a Python program using **NumPy** that simulates a small numerical preprocessing pipeline similar to those used in machine learning.

Your program must:

1. Create a NumPy array representing numeric data (e.g., feature values).
2. Compute:

   * Mean of the data
   * Standard deviation of the data
3. Normalize the data using the formula:

   ```
   normalized = (data - mean) / std
   ```
4. Reshape the normalized data into a **2D array** with a valid shape.
5. Print:

   * Original array
   * Mean and standard deviation
   * Normalized array
   * Reshaped array and its shape

**Requirements:**

* Use NumPy array operations (no Python loops for math)
* Use vectorized arithmetic
* Use `.shape` and `.reshape()`
* Write clean, readable code
* Import NumPy properly

**Sample Output (example):**

```
Original data: [10 20 30 40]
Mean: 25.0
Standard Deviation: 11.18
Normalized data: [-1.34 -0.45  0.45  1.34]
Reshaped data shape: (2, 2)
```