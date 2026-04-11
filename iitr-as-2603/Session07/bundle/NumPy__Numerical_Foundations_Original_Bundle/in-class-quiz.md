## Question 1

Which of the following correctly imports NumPy using the standard convention?

A. `import numpy`

B. `import numpy as np`

C. `from numpy import *`

D. `include numpy as np`

**Answer:** B

## Question 2

What is the data type (`dtype`) of the array created by `np.array([1, 2, 3.0])`?

A. int64

B. object

C. float64

D. str

**Answer:** C


---

## Question 1

What does `np.array([[1, 2, 3], [4, 5, 6]]).shape` return?

A. `(6,)`

B. `(2, 3)`

C. `(3, 2)`

D. `6`

**Answer:** B

## Question 2

What is the default `dtype` of `np.array([1, 2, 3])`?

A. float64

B. int32

C. int64

D. object

**Answer:** C


---

## Question 1

What does `np.arange(1, 10, 2)` return?

A. `[1, 3, 5, 7, 9, 11]`

B. `[1, 3, 5, 7, 9]`

C. `[2, 4, 6, 8, 10]`

D. `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

**Answer:** B

## Question 2

How many elements does `np.linspace(0, 1, 5)` produce?

A. 4

B. 6

C. 5

D. Depends on floating-point precision

**Answer:** C


---

## Question 1

Which NumPy function generates random values from a standard normal distribution (mean=0, std=1)?

A. `np.random.rand()`

B. `np.random.randint()`

C. `np.random.randn()`

D. `np.random.normal_dist()`

**Answer:** C

## Question 2

What is the purpose of `np.random.seed(42)`?

A. Generates exactly 42 random numbers

B. Sets the random generator to a fixed state so that subsequent random calls produce the same values

C. Limits random values to the range [0, 42]

D. Speeds up random number generation by a factor of 42

**Answer:** B


---

## Question 1

Given `arr = np.array([5, 10, 15, 20, 25])`, what does `arr[1:4]` return?

A. `[10 15 20 25]`

B. `[10 15 20]`

C. `[5 10 15 20]`

D. `[15 20 25]`

**Answer:** B

## Question 2

Given `arr = np.array([5, 10, 15, 20, 25])`, what does `arr[-1]` return?

A. `5`

B. An IndexError

C. `25`

D. `20`

**Answer:** C


---

## Question 1

Given `m = np.array([[1,2,3],[4,5,6],[7,8,9]])`, what does `m[1, 2]` return?

A. 5

B. 8

C. 6

D. 4

**Answer:** C

## Question 2

Given `m = np.array([[1,2,3],[4,5,6],[7,8,9]])`, what does `m[:, 1]` return?

A. `[1 2 3]`

B. `[4 5 6]`

C. `[2 5 8]`

D. `[2 6]`

**Answer:** C


---

## Question 1

Which function takes two `(4, 4)` 2D matrices and returns a completely new `(2, 4, 4)` 3D tensor?

A. `np.concatenate`

B. `np.vstack`

C. `np.hstack`

D. `np.stack`

**Answer:** D

## Question 2

What will be the output of `np.split([10, 20, 30, 40, 50, 60], [2, 5])`?

A. `[ [10, 20], [30, 40, 50], [60] ]`

B. `[ [10, 20, 30], [40, 50, 60] ]`

C. `[ [10, 20], [30, 40], [50, 60] ]`

D. A `ValueError` because 6 is not divisible by 2 and 5.

**Answer:** A


---

## Question 1

Which of the following best explains why NumPy array operations are faster than equivalent Python list operations?

A. NumPy uses a faster Python interpreter

B. NumPy stores elements as raw values in contiguous memory and calls compiled C routines

C. NumPy arrays have fewer elements than Python lists for the same data

D. Python lists require network I/O, which slows them down

**Answer:** B

## Question 2

What does "vectorization" mean in the context of NumPy?

A. Storing array elements as 2D vectors

B. Converting arrays to mathematical vectors for linear algebra

C. Applying an operation to all elements of an array without writing an explicit Python loop

D. Using GPU acceleration for array operations

**Answer:** C


---

