### **Q1. What is the output of the following code?**

```python
name = "alice"
print(name.upper())
```

A. alice
B. ALICE
C. Alice
D. Error

**Answer:** B

---

### **Q2. Which statement about strings is correct?**

A. Strings can be modified in place
B. Strings are immutable
C. Strings cannot store Unicode characters
D. Strings do not support slicing

**Answer:** B

---



### **Q3. What happens when duplicate keys are used in a dictionary?**

```python
data = {'x': 1, 'y': 2, 'x': 5}
```

A. Error occurs
B. Both values are stored
C. The last value overwrites the previous one
D. The first value is preserved

**Answer:** C

---

### **Q4. Which of the following is a valid way to create an empty dictionary?**

A. `[]`
B. `()`
C. `{}`
D. `set()`

**Answer:** C

---

### **Q5. What will the following code return?**

```python
student = {'name': 'Alice'}
print(student.get('age', 18))
```

A. Error
B. None
C. 18
D. 'age'

**Answer:** C

---


### **Q6. Which of the following correctly checks if a key exists in a dictionary?**

A. `'key' in dict`
B. `'key' in dict.keys()`
C. `dict.get('key')`
D. `dict['key']`

**Answer:** A


---



### **Q7. What does the following code demonstrate?**

```python
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
```

A. Function definition
B. Class creation and method call
C. Dictionary usage
D. Loop execution

**Answer:** B

---

### **Q8. What is true about objects created from a class?**

A. All objects share the same memory
B. Each object has its own independent data
C. Objects cannot store data
D. Only one object can be created from a class

**Answer:** B

---


### **Subjective Question**

Follow the instructions below and complete all tasks:

1. Create a folder named **Agentic Systems Design** on your computer (if created continue in the same folder)
2. Inside it, create a subfolder **Module 1** (if created continue in the same folder)
3. Inside that, create another folder **Session 5 – Strings and Dictionaries**
4. Open this folder in VS Code
5. Create a Python file named **strings_dictionaries.py**
6. Write code to solve all the questions given below
7. Run the code using the terminal (`python3 strings_dictionaries.py`) and verify the output
8. Once everything works correctly, copy and paste your complete code into the answer box, one below another

---

### **Tasks**

1. Create a string `"  python programming  "` and print the string after applying **strip() and title() methods**.

2. Write a program to check whether a given email (string) **starts with "user" and contains "@"**.

3. Create a dictionary `student = {'name': 'Alice', 'age': 22}` and:

   * Print all **keys**, **values**, and **items** separately.

4. Given a dictionary `config = {'theme': 'dark'}`, safely access the key `'font_size'` using **get()** and print a default value if it does not exist.

5. Create a nested dictionary for a user with name and city, and safely access the **city** using chained **get()** methods.

---

```
# Task 1
text = "  python programming  "
print(text.strip().title())

# Task 2
email = "user@example.com"
print(email.startswith("user") and "@" in email)

# Task 3
student = {'name': 'Alice', 'age': 22}
print(student.keys())
print(student.values())
print(student.items())

# Task 4
config = {'theme': 'dark'}
print(config.get('font_size', 14))

# Task 5
user = {
    'name': 'Alice',
    'address': {
        'city': 'Mumbai'
    }
}

city = user.get('address', {}).get('city', 'Unknown')
print(city)
```

