# Define Variables

## 
What does this code do?
```python
score = 100
```

**A)** Checks if score equals 100
**B)** Assigns 100 to the variable score
**C)** Creates a function called score
**D)** Prints 100

<details>
<summary>Answer</summary>

**B** - Assigns 100 to the variable score

The `=` operator creates/updates a variable with a value.
</details>

---

## 
What will be the final value of `x`?
```python
x = 5
x = 10
x = 15
```

**A)** 5
**B)** 10
**C)** 15
**D)** Error

<details>
<summary>Answer</summary>

**C** - 15

Variables can be reassigned. The final assignment wins.
</details>

---

## 
What's wrong with this code?
```python
print(temperature)
temperature = 72
```

**A)** Nothing, it works fine
**B)** Can't use temperature before creating it
**C)** temperature is a reserved word
**D)** 72 should be in quotes

<details>
<summary>Answer</summary>

**B** - Can't use temperature before creating it

Variables must be created before they're used. Swap the lines!
</details>

---

## 
What does `score = score + 10` mean?

**A)** Checks if score equals score + 10
**B)** Creates two variables
**C)** Adds 10 to current score value
**D)** Causes an error

<details>
<summary>Answer</summary>

**C** - Adds 10 to current score value

Python evaluates the right side first (gets current score, adds 10), then assigns result back to score.
</details>

---

## 
After this code runs, what are the values?
```python
a = 10
b = 20
a = b
```

**A)** a=10, b=20
**B)** a=20, b=10
**C)** a=20, b=20
**D)** Error

<details>
<summary>Answer</summary>

**C** - a=20, b=20

`a = b` copies b's value (20) into a. Both are now 20. The original value of a (10) is lost.
</details>

---

## Scoring
- **5/5**: Excellent! You've mastered variables
- **4/5**: Great! Review the missed question
- **3/5**: Good start, review lecture notes
- **<3**: Please review material and try again


---

# Apply Variable Naming Conventions

## Which is invalid?
A) `age`
B) `_value`
C) `2nd_place`  
D) `my_var`

<details><summary>Answer</summary>
C - Starts with number
</details>

## What's Pythonic style?
A) `studentName`
B) `student_name`
C) `StudentName`
D) `STUDENT_NAME`

<details><summary>Answer</summary>
B - snake_case for variables
</details>

## Which is a reserved keyword?
A) `name`
B) `value`
C) `for`
D) `count`

<details><summary>Answer</summary>
C - `for` is reserved for loops
</details>

## Case sensitive means?
A) Must use lowercase
B) `age` and `Age` are different
C) Cannot use uppercase
D) Python ignores case

<details><summary>Answer</summary>
B - Variables are case-sensitive
</details>

## Best name for a boolean?
A) `active`
B) `is_active`
C) `check_active`
D) `active_status`

<details><summary>Answer</summary>
B - Sounds like yes/no question
</details>


---

# Implement Integer Data Types

## What's an integer?
A) Any number
B) Whole number only
C) Decimal number
D) Text

<details><summary>Answer</summary>
B - Whole numbers with no decimals
</details>

## What does 15 // 4 return?
A) 3.75
B) 3
C) 4
D) 15

<details><summary>Answer</summary>
B - 3 (integer division drops decimal)
</details>

## What does 15 % 4 return?
A) 3
B) 4
C) 3.75
D) 15

<details><summary>Answer</summary>
A) 3 (remainder of 15 ÷ 4)
</details>

## What's the type of this?
```python
x = 10 / 2
```
A) int
B) float
C) str
D) bool

<details><summary>Answer</summary>
B - float (even though result is 5.0, `/` always returns float)
</details>

## Integer + float = ?
A) int
B) float
C) Error
D) string

<details><summary>Answer</summary>
B - float (mixed operations return float)
</details>


---

# Implement Float Data Types

## What's a float?
A) Whole number
B) Number with decimal
C) Text
D) True/False

<details><summary>Answer</summary>
B - Numbers with decimal points
</details>

## What's the type?
```python
x = 10 / 2
```
A) int  
B) float
C) str
D) bool

<details><summary>Answer</summary>
B - Division always returns float
</details>

## What prints?
```python
print(0.1 + 0.2)
```
A) 0.3 exactly
B) 0.30000000000000004
C) 0.2
D) Error

<details><summary>Answer</summary>
B - Binary precision limitation
</details>

## Int + float = ?
A) int
B) float
C) Error

<details><summary>Answer</summary>
B - Result is always float
</details>

## When to use float?
A) Counting students
B) Product price
C) Year
D) Age

<details><summary>Answer</summary>
B - Prices need decimal precision
</details>


---

# Implement String Data Types

## Valid string?
A) name = "Alice"
B) name = 'Alice'
C) name = `Alice`
D) Both A and B

<details><summary>Answer</summary>
D - Both single and double quotes work
</details>

## What prints?
```python
print("ha" * 3)
```
A) ha3
B) hahaha
C) ha ha ha

<details><summary>Answer</summary>
B - String repetition
</details>

## What's wrong?
```python
age = 25
msg = "Age: " + age
```
A) Nothing
B) Can't concatenate str and int
C) Wrong quotes

<details><summary>Answer</summary>
B - Need str(age) or use f-string
</details>

## What's len("Hello")?
A) 4
B) 5
C) 6

<details><summary>Answer</summary>
B - 5 characters
</details>

## What prints?
```python
name = "alice"
print(name.upper())
```
A) alice
B) ALICE
C) Alice

<details><summary>Answer</summary>
B - ALICE (all uppercase)
</details>


---

# Implement Boolean Data Types

## Valid boolean?
A) true
B) True
C) TRUE
D) boolean(1)

<details><summary>Answer</summary>
B - Must be capitalized: True
</details>

## How many boolean values?
A) 1
B) 2
C) Infinite
D) 3

<details><summary>Answer</summary>
B - Only True and False
</details>

## What type?
```python
x = True
```
A) int
B) str
C) bool
D) float

<details><summary>Answer</summary>
C - bool (boolean)
</details>

## Good boolean name?
A) status
B) is_active
C) active_flag
D) data_value

<details><summary>Answer</summary>
B - Sounds like yes/no question
</details>

## What's wrong?
```python
finished = "True"
```
A) Nothing
B) Should be True (no quotes)
C) Wrong capitalization
D) Variable name is invalid

<details><summary>Answer</summary>
B - Quotes make it string, not boolean
</details>


---

# Check Variable Types

`type()` function identifies variable data types in Python.

```python
age = 25
print(type(age))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

## Use Cases
- Debugging
- Validation
- Understanding code
- Type checking

## Key Points
- `type(variable)` returns the type
- Returns class object
- Helps identify type errors
- Essential for debugging


---

# Perform Arithmetic Operations

## What does 10 / 2 return?
A) 5
B) 5.0
C) Error
D) 5.00

<details><summary>Answer</summary>
B - 5.0 (division always returns float)
</details>

## What's 17 // 5?
A) 3
B) 3.4
C) 2
D) 4

<details><summary>Answer</summary>
A - 3 (integer division drops decimal)
</details>

## What's 17 % 5?
A) 2
B) 3
C) 3.4
D) 5

<details><summary>Answer</summary>
A - 2 (remainder: 17 = 5×3 + 2)
</details>

## What's 2 ** 4?
A) 8
B) 16
C) 6
D) 24

<details><summary>Answer</summary>
B - 16 (2⁴ = 2×2×2×2)
</details>

## After this code, what's x?
```python
x = 10
x += 5
x *= 2
```
A) 20
B) 25
C) 30
D) 15

<details><summary>Answer</summary>
C - 30 (10 + 5 = 15, then 15 × 2 = 30)
</details>


---

# Apply Operator Precedence

## What's 2 + 3 * 4?
A) 20
B) 14
C) 12
D) 24

<details><summary>Answer</summary>
B - 14 (multiplication first: 3*4=12, then 2+12=14)
</details>

## What's (2 + 3) * 4?
A) 14
B) 20
C) 12
D) 24

<details><summary>Answer</summary>
B - 20 (parentheses first: 2+3=5, then 5*4=20)
</details>

## What's 2 ** 3 + 4?
A) 128
B) 12
C) 12
D) 10

<details><summary>Answer</summary>
B - 12 (exponent first: 2**3=8, then 8+4=12)
</details>

## Precedence order?
A) + - * /
B) * / + -
C) ( ) ** * / + -
D) ** ( ) + - * /

<details><summary>Answer</summary>
C - Parentheses, Exponents, Mult/Div, Add/Sub
</details>

## Best practice?
A) Never use parentheses
B) Use parentheses for clarity
C) Memorize all rules
D) Always use spaces instead of parentheses

<details><summary>Answer</summary>
B - Parentheses make code clearer
</details>


---

# Use Comparison Operators

## What does `x == 5` do?
A) Assigns 5 to x
B) Checks if x equals 5
C) Changes x to 5
D) Adds 5 to x

<details><summary>Answer</summary>
B - Checks if x equals 5 (returns True or False)
</details>

## What's the output?
```python
age = 18
print(age >= 18)
```
A) True
B) False
C) 18
D) Error

<details><summary>Answer</summary>
A - True (18 is equal to 18, and >= includes equality)
</details>

## What's the difference?
```python
print(10 > 10)
print(10 >= 10)
```
A) Both True
B) Both False
C) False, then True
D) True, then False

<details><summary>Answer</summary>
C - False, then True (> doesn't include equal, >= does)
</details>

## What type is returned?
```python
result = 5 != 3
print(type(result))
```
A) int
B) bool
C) str
D) float

<details><summary>Answer</summary>
B - bool (comparisons always return boolean True/False)
</details>

## Which is correct?
A) Use `=` to check equality
B) Use `==` to check equality
C) Both work the same
D) Use `===` to check equality

<details><summary>Answer</summary>
B - Use `==` to check equality (`=` is for assignment)
</details>


---

