# Objective Assignment: Dictionaries & HashMaps - Built-in Functions

## Question 1 - MCQ (Easy)

A contact app needs to store one phone number for each contact name. Which Python data structure is most suitable for this?

A. List  
B. String  
C. Dictionary  
D. Integer  

**Correct Answer:** C

**Answer Explanation:**  
A dictionary is most suitable because it stores data as key-value pairs, such as `"Maa": "9876543210"`. Option A is incorrect because a list mainly stores values by position, not by meaningful labels. Option B is incorrect because a string stores text characters. Option D is incorrect because an integer stores only a number, not labelled data.

---

## Question 2 - MCQ (Easy)

What will be printed by the following code?

```python
student = {
    "name": "Amit",
    "age": 21,
    "marks": 88
}

print(student["marks"])
```

A. `Amit`  
B. `21`  
C. `88`  
D. `marks`  

**Correct Answer:** C

**Answer Explanation:**  
The expression `student["marks"]` uses the key `"marks"` to access its mapped value, which is `88`. Option A is the value for the key `"name"`. Option B is the value for the key `"age"`. Option D is the key itself, not the value returned by dictionary access.

---

## Question 3 - MCQ (Easy)

Which syntax correctly creates an empty dictionary in Python?

A. `student = []`  
B. `student = {}`  
C. `student = ()`  
D. `student = ""`  

**Correct Answer:** B

**Answer Explanation:**  
`{}` creates an empty dictionary. Option A creates an empty list. Option C creates an empty tuple. Option D creates an empty string.

---

## Question 4 - MCQ (Easy)

What will be printed by the following code?

```python
prices = {
    "banana": 20,
    "apple": 40,
    "mango": 50
}

print(prices.get("watermelon"))
```

A. `0`  
B. `None`  
C. `KeyError`  
D. `watermelon`  

**Correct Answer:** B

**Answer Explanation:**  
`get("watermelon")` returns `None` because the key `"watermelon"` does not exist and no default value is provided. Option A would be correct only if the code used `get("watermelon", 0)`. Option C is incorrect because `get()` avoids a `KeyError`. Option D is incorrect because `get()` returns the mapped value, not the key.

---

## Question 5 - MCQ (Moderate)

A grocery billing program stores item prices in a dictionary:

```python
prices = {
    "mango": 20,
    "apple": 30,
    "banana": 10
}
```

Which expression returns the values in sorted order?

A. `sorted(prices)`  
B. `sorted(prices.values())`  
C. `prices.keys()`  
D. `prices.items()`  

**Correct Answer:** B

**Answer Explanation:**  
`sorted(prices.values())` returns the dictionary values in sorted order: `[10, 20, 30]`. Option A sorts the keys, not the values. Option C returns the keys without sorting them. Option D returns key-value pairs, not sorted values.

---

## Question 6 - MCQ (Moderate)

What will be printed by the following code?

```python
student = {
    "name": "Yash",
    "age": 29,
    "name": "Shubham"
}

print(student)
```

A. `{'name': 'Yash', 'age': 29, 'name': 'Shubham'}`  
B. `{'name': 'Yash', 'age': 29}`  
C. `{'name': 'Shubham', 'age': 29}`  
D. `KeyError`  

**Correct Answer:** C

**Answer Explanation:**  
Dictionary keys must be unique. When the same key appears again, Python keeps the latest value for that key. So `"name": "Shubham"` overwrites `"name": "Yash"`. Option A is incorrect because Python does not keep duplicate keys in the final dictionary. Option B keeps the old value, which is not how Python handles duplicate keys. Option D is incorrect because duplicate keys do not raise a `KeyError`.

---

## Question 7 - MSQ (Moderate)

A menu dictionary is created as follows:

```python
menu = {
    "Dosa": 60,
    "Idli": 40,
    "Vada": 35
}
```

Which statements are correct?

A. `menu.keys()` returns all dish names.  
B. `menu.values()` returns all prices.  
C. `menu.items()` returns key-value pairs.  
D. `menu.get("Tea", 0)` raises a `KeyError`.  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Option A is correct because `keys()` returns all keys, which are dish names. Option B is correct because `values()` returns all values, which are prices. Option C is correct because `items()` returns key-value pairs. Option D is incorrect because `get("Tea", 0)` returns `0` when `"Tea"` is missing; it does not raise a `KeyError`.

---

## Question 8 - MSQ (Moderate)

A dictionary is used to count characters in a word:

```python
counts = {}
char = "a"
counts[char] = counts.get(char, 0) + 1
```

Which statements are correct?

A. `counts.get(char, 0)` returns `0` if `char` is not already a key.  
B. After the code runs once, `counts` becomes `{"a": 1}`.  
C. The key stores the character and the value stores the count.  
D. The code cannot work because dictionary values cannot be numbers.  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Option A is correct because `get(char, 0)` uses `0` as the default value for a missing key. Option B is correct because the old count `0` becomes `1` and is stored under the key `"a"`. Option C is correct because the character is used as the key and its frequency is stored as the value. Option D is incorrect because dictionary values can be numbers, strings, lists, and other data types.

---

## Question 9 - MSQ (Hard)

A delivery app stores delivery charges by city:

```python
charges = {
    "Pune": 40,
    "Delhi": 60,
    "Mumbai": 50
}
```

Which expressions are logically correct for analysing this dictionary?

A. `len(charges)` returns `3`.  
B. `sorted(charges)` returns city names in sorted order.  
C. `max(charges.values())` returns `60`.  
D. `sum(charges.keys())` returns `150`.  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Option A is correct because the dictionary has three key-value pairs. Option B is correct because `sorted(charges)` sorts dictionary keys, so it returns sorted city names. Option C is correct because the highest value among `40`, `60`, and `50` is `60`. Option D is incorrect because `charges.keys()` contains strings, and `sum()` cannot add city names.

---

## Question 10 - MSQ (Hard)

Python dictionaries work like hashmaps for fast key-based lookup. Which statements are correct?

A. A dictionary stores data as key-value pairs.  
B. A dictionary lookup is generally fast because Python uses a hash value internally.  
C. A list can be safely used as a dictionary key because lists are flexible.  
D. Strings and integers can commonly be used as dictionary keys.  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Option A is correct because dictionaries store key-value pairs. Option B is correct because Python internally uses hashing to locate values efficiently. Option C is incorrect because lists are not hashable and cannot be used as dictionary keys. Option D is correct because strings and integers are common hashable key types.
