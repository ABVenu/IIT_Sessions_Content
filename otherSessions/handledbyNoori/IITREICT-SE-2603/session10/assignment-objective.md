# Objective Assignment — Advanced OOP in Python: Inheritance, Overriding & Overloading

---

## Question 1 — MCQ | Easy

Rohan is building a vehicle management system. He already has a `Vehicle` class with a `start()` method and wants to create a `Car` class that reuses it without rewriting any code. Which of the following correctly defines `Car` to inherit from `Vehicle`?

**A)** `class Car extends Vehicle:`
**B)** `class Car(Vehicle):`
**C)** `class Car inherits Vehicle:`
**D)** `class Vehicle(Car):`

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** In Python, inheritance is defined by placing the parent class name inside parentheses after the child class name: `class Car(Vehicle):`. This gives `Car` access to all of `Vehicle`'s methods and attributes.
- **A is incorrect.** `extends` is a keyword used in Java, not Python.
- **C is incorrect.** `inherits` is not valid Python syntax.
- **D is incorrect.** This reverses the relationship — it would make `Vehicle` inherit from `Car`, not the other way around.

---

## Question 2 — MCQ | Easy

Priya wrote the following code:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal:", self.name)

class Cat(Animal):
    def sound(self):
        print(self.name, "meows")

c = Cat("Whiskers")
c.info()
```

What will `c.info()` print?

**A)** `AttributeError: 'Cat' object has no attribute 'info'`
**B)** `Animal: Whiskers`
**C)** `Cat: Whiskers`
**D)** `None`

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** `Cat` inherits from `Animal`, so it gains access to `Animal`'s `info()` method. When `c.info()` is called, Python finds `info()` in the parent class `Animal` and runs it with `self.name = "Whiskers"`, printing `Animal: Whiskers`.
- **A is incorrect.** Python does not raise an error — inherited methods are fully accessible from child objects.
- **C is incorrect.** The `info()` method explicitly prints `"Animal:"` as the label, not the class name of the caller.
- **D is incorrect.** The `print()` inside `info()` produces visible output, not `None`.

---

## Question 3 — MCQ | Easy

Amit is learning about `super()`. Consider the code below:

```python
class Parent:
    def __init__(self):
        self.x = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.y = 20
```

What does `super().__init__()` do inside `Child`'s constructor?

**A)** Creates a completely new object of the `Parent` class
**B)** Calls `Parent`'s `__init__` method so that `self.x` is properly initialized on the `Child` object
**C)** Replaces `Child`'s `__init__` with `Parent`'s `__init__`
**D)** Returns a `Parent` object that can be stored in a variable

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** `super().__init__()` calls the parent class's constructor on the *same* object (`self`). This ensures `self.x = 10` is set before the child adds its own `self.y = 20`. No new object is created.
- **A is incorrect.** `super().__init__()` does not create a separate `Parent` object; it runs the parent's setup logic on the existing child object.
- **C is incorrect.** `Child`'s `__init__` is not replaced — both constructors run, with the parent's running first.
- **D is incorrect.** `super().__init__()` returns `None`; it is not used to get a returnable parent object.

---

## Question 4 — MCQ | Easy

Which type of inheritance is demonstrated in the code below?

```python
class University:
    def enroll(self):
        print("Enrolled in University")

class CSE(University):
    def specialize(self):
        print("Specializing in Computer Science")

class ECE(University):
    def specialize(self):
        print("Specializing in Electronics")
```

**A)** Single Inheritance
**B)** Multiple Inheritance
**C)** Multi-level Inheritance
**D)** Hierarchical Inheritance

**Correct Answer:** D

**Answer Explanation:**
- **D is correct.** In Hierarchical Inheritance, multiple child classes inherit from the same single parent class. Here, both `CSE` and `ECE` inherit from `University`. The children are siblings — they share the parent but have no relationship with each other.
- **A is incorrect.** Single Inheritance has exactly one parent and one child.
- **B is incorrect.** Multiple Inheritance is when one child inherits from more than one parent simultaneously.
- **C is incorrect.** Multi-level Inheritance is a chain (A → B → C), not a fan-out from one parent.

---

## Question 5 — MCQ | Moderate

Zara is building a simulation game. She writes the following class hierarchy and calls a method:

```python
class A:
    def attack(self):
        print("A attacks")

class B(A):
    def attack(self):
        print("B attacks")

class C(A):
    def attack(self):
        print("C attacks")

class D(B, C):
    pass

hero = D()
hero.attack()
```

What will be printed?

**A)** `A attacks`
**B)** `B attacks`
**C)** `C attacks`
**D)** `TypeError: ambiguous method resolution`

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** Python uses the C3 Linearization algorithm (MRO) to resolve method calls. For `class D(B, C)`, the MRO is `D → B → C → A → object`. Python searches left to right: `D` has no `attack()`, so it moves to `B`, which has `attack()` → it prints `"B attacks"` and stops.
- **A is incorrect.** Python finds `attack()` in `B` before reaching `A`.
- **C is incorrect.** `C` is checked after `B` in the MRO — since `B` already has the method, `C` is never reached.
- **D is incorrect.** Python does not raise an error for this scenario; MRO is designed precisely to handle it deterministically.

---

## Question 6 — MCQ | Moderate

Meera wants to simulate method overloading in Python. She uses default arguments:

```python
def greet(name, message="Hello"):
    print(message + ", " + name + "!")

greet("Meera")
greet("Meera", "Welcome")
```

What is the correct output?

**A)**
```
Hello, Meera!
Hello, Meera!
```

**B)**
```
Hello, Meera!
Welcome, Meera!
```

**C)**
```
Meera!
Welcome, Meera!
```

**D)** `TypeError: greet() takes 1 positional argument but 2 were given`

**Correct Answer:** B

**Answer Explanation:**
- **B is correct.** When `greet("Meera")` is called with one argument, `message` uses its default value `"Hello"`, printing `Hello, Meera!`. When called with two arguments, the second argument `"Welcome"` overrides the default, printing `Welcome, Meera!`. This is how Python simulates method overloading — one function handles different calling patterns through default arguments.
- **A is incorrect.** The second call explicitly passes `"Welcome"`, overriding the default.
- **C is incorrect.** The format string always prepends `message + ", "` before `name`, so `name` alone on a line is impossible here.
- **D is incorrect.** The function is defined with two parameters; passing two arguments is perfectly valid.

---

## Question 7 — MSQ | Moderate

Raj is reviewing a piece of code that uses Method Overriding. Which of the following statements about Method Overriding in Python are **correct**? *(Select all that apply.)*

**A)** The overriding method in the child class must have the same name as the parent class method it overrides.
**B)** When a child object calls an overridden method, Python executes the child's version, not the parent's.
**C)** Method overriding requires the `@override` decorator in Python.
**D)** You can still call the parent's original version of the method from inside the child class using `super()`.

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct.** Overriding works because the child class defines a method with the **same name** as the parent's. If the name is different, it is simply a new method, not an override.
- **B is correct.** Python always searches the **child class first**. If the method is found there, the parent's version is not called (unless explicitly done via `super()`).
- **C is incorrect.** Python does not have a mandatory `@override` decorator. Overriding happens automatically whenever a child class redefines an inherited method name.
- **D is correct.** `super().method_name()` lets you explicitly call the parent's version of an overridden method, which is a common pattern when you want to extend (not completely replace) the parent's behavior.

---

## Question 8 — MSQ | Moderate

Divya defines a class hierarchy using Multiple Inheritance:

```python
class Mother:
    def skill(self):
        print("Cooking")

class Father:
    def skill(self):
        print("Driving")

class Child(Mother, Father):
    pass

c = Child()
c.skill()
```

Which of the following statements are **correct**? *(Select all that apply.)*

**A)** `c.skill()` prints `Cooking`
**B)** `c.skill()` prints `Driving`
**C)** Python uses MRO to decide which `skill()` method to call
**D)** `Child.mro()` returns `[Child, Mother, Father, object]`

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A is correct.** The MRO for `class Child(Mother, Father)` is `Child → Mother → Father → object`. Python finds `skill()` in `Mother` first and calls it, printing `Cooking`.
- **B is incorrect.** `Father`'s `skill()` is only checked if `Mother`'s is not found. Since `Mother` comes first in the inheritance list, its version is called.
- **C is correct.** Python's C3 Linearization (MRO) is the mechanism that resolves method lookup order in all cases of inheritance, including Multiple Inheritance.
- **D is correct.** `Child.mro()` returns exactly `[<class 'Child'>, <class 'Mother'>, <class 'Father'>, <class 'object'>]`, reflecting the left-to-right order of the parent classes listed in the class definition.

---

## Question 9 — MSQ | Hard

Kiran builds the following class hierarchy with `super()` and Multiple Inheritance:

```python
class A:
    def __init__(self):
        super().__init__()
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

obj = D()
```

Which of the following statements are **correct**? *(Select all that apply.)*

**A)** The output order is: `A`, then `C`, then `B`, then `D`
**B)** Inside `B.__init__`, `super().__init__()` calls `C.__init__()` (not `A.__init__()`), because MRO places `C` after `B`
**C)** The MRO for `D` is: `D → B → C → A → object`
**D)** The output order is: `D`, then `B`, then `C`, then `A`

**Correct Answers:** A, B, C

**Answer Explanation:**
- **A is correct.** Each constructor prints *after* its `super().__init__()` call returns. The chain runs top-down (D → B → C → A) but prints bottom-up (A first, then C, then B, then D) because each `print` executes only after the `super()` chain unwinds.
- **B is correct.** MRO for `D` is `D → B → C → A`. When `super().__init__()` is called inside `B`, Python follows MRO and goes to `C` next (not `A`). This cooperative super-chaining ensures every class in the hierarchy is initialized exactly once.
- **C is correct.** Python's C3 Linearization produces `D → B → C → A → object` for `class D(B, C)` where both `B` and `C` inherit from `A`. You can verify with `D.mro()`.
- **D is incorrect.** The output is in the reverse order of method calls (A → C → B → D), not the call order (D → B → C → A), because `print` executes after the `super()` call returns at each level.

---

## Question 10 — MSQ | Hard

Sneha is designing a polymorphic system using Duck Typing and Operator Overloading concepts. She writes:

```python
def add(data_type, *args):
    if data_type == int:
        result = 0
    elif data_type == str:
        result = ""
    for item in args:
        result += item
    return result

print(add(int, 4, 11, 15))
print(add(str, "Masai", " ", "School"))
```

She also writes a second snippet:

```python
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())
```

Which of the following statements are **correct**? *(Select all that apply.)*

**A)** `add(int, 4, 11, 15)` returns `30`
**B)** `add(str, "Masai", " ", "School")` returns `"Masai School"`
**C)** `*args` captures `(4, 11, 15)` as a Python **list**
**D)** `perform_task()` works with both `Pen` and `Eraser` because Duck Typing requires only that the passed object has a `use()` method, regardless of its class

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct.** `data_type == int`, so `result` starts at `0`. The loop adds `4 + 11 + 15 = 30`.
- **B is correct.** `data_type == str`, so `result` starts as `""`. String concatenation gives `"" + "Masai" + " " + "School" = "Masai School"`.
- **C is incorrect.** `*args` captures positional arguments into a **tuple**, not a list. `args` would be `(4, 11, 15)` — a tuple.
- **D is correct.** Duck Typing means Python does not check the type of `tool`; it only cares that `tool.use()` exists and is callable. Both `Pen` and `Eraser` have a `use()` method, so `perform_task()` works for both without any type checking or inheritance relationship between them.
