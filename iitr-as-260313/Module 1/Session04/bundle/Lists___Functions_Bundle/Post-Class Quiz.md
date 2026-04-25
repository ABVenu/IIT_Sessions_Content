## Post-class Quiz: Creating and Initializing Lists in Python

### 
Which of the following creates an empty list?

A) `list = {}`
B) `list = []`
C) `list = ()`
D) `list = ""`

**Correct Answer: B**
*Explanation: [] creates an empty list. {} creates an empty dictionary, () creates an empty tuple, and "" creates an empty string*

---

### 
What is the output of `list(range(3, 8))`?

A) [3, 4, 5, 6, 7, 8]
B) [3, 4, 5, 6, 7]
C) [4, 5, 6, 7]
D) [3, 8]

**Correct Answer: B**
*Explanation: range(3, 8) starts at 3 and goes up to but not including 8, so it produces [3, 4, 5, 6, 7]*

---

### 
What does `"hello world".split()` return?

A) ['hello world']
B) ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
C) ['hello', 'world']
D) ['h', 'w']

**Correct Answer: C**
*Explanation: split() without arguments splits on whitespace, creating ['hello', 'world']. To get individual characters, use list("hello world")*

---

### 
Given `matrix = [[1, 2], [3, 4], [5, 6]]`, what is `matrix[1][1]`?

A) 1
B) 2
C) 3
D) 4

**Correct Answer: D**
*Explanation: matrix[1] selects the second inner list [3, 4], then [1] selects the second element 4*

---

### 
What is the output of `[1, 2] + [3, 4]`?

A) [1, 2, 3, 4]
B) [[1, 2], [3, 4]]
C) [4, 6]
D) Error

**Correct Answer: A**
*Explanation: The + operator concatenates lists, combining them into a single list [1, 2, 3, 4]*


---

## Post-class Quiz: Accessing List Elements Using Indexing

### 
Given `items = ['a', 'b', 'c', 'd', 'e']`, what is `items[-2]`?

A) 'c'
B) 'd'
C) 'e'
D) Error

**Correct Answer: B**
*Explanation: items[-2] accesses the second element from the end, which is 'd'. Negative indices count backward from the end*

---

### 
What happens when you try `lst[10]` on a list with only 5 elements?

A) Returns None
B) Returns the last element
C) Raises IndexError
D) Returns 0

**Correct Answer: C**
*Explanation: Accessing an index beyond the list bounds raises an IndexError. Valid indices for 5 elements are 0-4 or -5 to -1*

---

### 
Given `matrix = [[1,2], [3,4]]`, what is `matrix[0][1]`?

A) 1
B) 2
C) 3
D) [1, 2]

**Correct Answer: B**
*Explanation: matrix[0] gets [1,2], then [1] gets the second element, which is 2*

---

### 
How do you access the last element of a list without knowing its length?

A) `lst[len(lst)]`
B) `lst[-0]`
C) `lst[-1]`
D) `lst[last]`

**Correct Answer: C**
*Explanation: lst[-1] always accesses the last element regardless of list length. lst[len(lst)] would cause an error (out of bounds)*

---

### 
What does `lst.index(value)` return?

A) The value at that index
B) The first index where value is found
C) All indices where value appears
D) True if value exists

**Correct Answer: B**
*Explanation: .index(value) returns the first index position where the value is found. Raises ValueError if not found*


---

## Post-class Quiz: Extracting List Portions Using Slicing

### 
Given `lst = [10, 20, 30, 40, 50]`, what is `lst[1:4]`?

A) `[10, 20, 30]`
B) `[20, 30, 40]`
C) `[20, 30, 40, 50]`
D) `[10, 20, 30, 40]`

**Correct Answer: B**
*Explanation: lst[1:4] starts at index 1 (20) and stops before index 4. So it includes indices 1, 2, 3, which are [20, 30, 40]. Remember: stop index is exclusive*

---

### 
What does `numbers[::-1]` do?

A) Returns the first element
B) Returns the last element
C) Reverses the list
D) Returns every other element

**Correct Answer: C**
*Explanation: The step of -1 means move backwards through the list. Starting from the end and going to the beginning with step -1 effectively reverses the entire list*

---

### 
Given `data = [1, 2, 3, 4, 5, 6, 7, 8]`, what is `data[::2]`?

A) `[1, 2, 3, 4]`
B) `[2, 4, 6, 8]`
C) `[1, 3, 5, 7]`
D) `[1, 2]`

**Correct Answer: C**
*Explanation: [::2] means start at 0, go to the end, with step 2. This gives every second element starting from index 0: indices 0, 2, 4, 6 → [1, 3, 5, 7]*

---

### 
What happens when you do `lst[2:2] = [10, 20]`?

A) Replaces elements at index 2
B) Inserts [10, 20] at index 2
C) Deletes element at index 2
D) Causes an error

**Correct Answer: B**
*Explanation: lst[2:2] is an empty slice at position 2. Assigning to an empty slice inserts the new elements at that position without replacing anything*

---

### 
Given `lst = [0, 1, 2, 3, 4, 5]`, what is `lst[-3:-1]`?

A) `[3, 4, 5]`
B) `[3, 4]`
C) `[4, 5]`
D) `[2, 3, 4]`

**Correct Answer: B**
*Explanation: lst[-3] is index 3 (value 3), lst[-1] is index 5 (value 5). Slice [-3:-1] goes from index 3 up to (but not including) index 5, giving indices 3 and 4 → [3, 4]*


---

## Post-class Quiz: Iterating Through Lists Using Loops

### 
What does `enumerate(['a', 'b', 'c'])` return when used in a for loop?

A) Just the values: 'a', 'b', 'c'
B) Just the indices: 0, 1, 2
C) Tuples of (index, value): (0,'a'), (1,'b'), (2,'c')
D) A dictionary: {0:'a', 1:'b', 2:'c'}

**Correct Answer: C**
*Explanation: enumerate() returns an iterator of tuples where each tuple contains (index, value). In a for loop, you typically unpack these as `for i, val in enumerate(list):`*

---

### 
Given `list1 = [1, 2, 3]` and `list2 = [4, 5]`, what happens with `for a, b in zip(list1, list2):`?

A) Error because lists have different lengths
B) Loops 3 times, using None for missing b value
C) Loops 2 times, stopping at shortest list
D) Loops 3 times, repeating last b value

**Correct Answer: C**
*Explanation: zip() stops when the shortest input iterable is exhausted. Here it will only process (1,4) and (2,5), ignoring the 3 from list1*

---

### 
What is wrong with this code?
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
```

A) Nothing, it works correctly
B) It modifies the list while iterating, causing unpredictable behavior
C) remove() doesn't work in a for loop
D) The condition is wrong

**Correct Answer: B**
*Explanation: Modifying a list while iterating over it can cause elements to be skipped. When you remove an element, the iterator doesn't adjust, so it may skip the next element. Use `for num in numbers[:]` to iterate over a copy, or use list comprehension instead*

---

### 
How do you iterate through a list and get a 1-based position number?

A) `for i in range(len(lst)):`
B) `for i, val in enumerate(lst, start=1):`
C) `for i, val in enumerate(lst) + 1:`
D) `for i in lst.index():`

**Correct Answer: B**
*Explanation: enumerate() accepts a start parameter. enumerate(lst, start=1) will begin counting from 1 instead of 0. You can unpack as `for i, val in enumerate(lst, start=1):`*

---

### 
What is the output?
```python
lst = [1, 2, 3]
for i, val in enumerate(lst):
    lst[i] = val * 2
print(lst)
```

A) `[1, 2, 3]` - unchanged
B) `[2, 4, 6]` - doubled
C) Error - can't modify while iterating
D) `[1, 4, 9]` - squared

**Correct Answer: B**
*Explanation: It's safe to modify list elements by index while iterating. enumerate() gives us the index i, and we use it to update lst[i]. Each value gets doubled, resulting in [2, 4, 6]*


---

## Post-class Quiz: Using List Comprehensions

### 
What is the output of `[x * 2 for x in range(3)]`?

A) `[0, 2, 4]`
B) `[2, 4, 6]`
C) `[1, 2, 3]`
D) `[0, 1, 2]`

**Correct Answer: A**
*Explanation: range(3) gives [0, 1, 2]. Multiplying each by 2 gives [0, 2, 4]. The expression is evaluated for each element from the iterable*

---

### 
Which list comprehension correctly filters even numbers from `nums = [1, 2, 3, 4, 5, 6]`?

A) `[x for x in nums where x % 2 == 0]`
B) `[x if x % 2 == 0 for x in nums]`
C) `[x for x in nums if x % 2 == 0]`
D) `[x for x in nums and x % 2 == 0]`

**Correct Answer: C**
*Explanation: The correct syntax for filtering is [expression for item in iterable if condition]. The 'if' comes after the 'for' clause. Python doesn't use 'where' and option B has incorrect syntax*

---

### 
What does `[x if x > 0 else 0 for x in [-2, 3, -1, 5]]` produce?

A) `[3, 5]`
B) `[-2, 3, -1, 5]`
C) `[0, 3, 0, 5]`
D) Error

**Correct Answer: C**
*Explanation: This uses a conditional expression (ternary). For each element: if x > 0, keep x, else use 0. So -2 becomes 0, 3 stays 3, -1 becomes 0, 5 stays 5, giving [0, 3, 0, 5]*

---

### 
What is the result of `[x for row in [[1,2], [3,4]] for x in row]`?

A) `[[1, 2], [3, 4]]`
B) `[1, 2, 3, 4]`
C) `[(1, 2), (3, 4)]`
D) Error

**Correct Answer: B**
*Explanation: This is a flattening comprehension. It iterates over each row, then over each x in that row, creating a flat list. The order is: for row in matrix, then for x in row, giving [1, 2, 3, 4]*

---

### 
When should you avoid using list comprehensions?

A) When transforming simple data
B) When filtering lists
C) When logic is complex and spans multiple conditions
D) When working with small lists

**Correct Answer: C**
*Explanation: List comprehensions are great for simple transformations and filters, but when logic becomes too complex (multiple nested conditions, complex calculations), a regular for loop is more readable and maintainable*


---

