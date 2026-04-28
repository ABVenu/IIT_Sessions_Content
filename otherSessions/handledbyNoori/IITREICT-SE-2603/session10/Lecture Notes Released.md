# Advanced Object-Oriented Programming in Python: Inheritance, Overriding, and Overloading

## Context: What We Covered Before & What's Coming Today

In the previous session, we built a solid foundation of **Object-Oriented Programming (OOP)**. We learned what a **class** is, how to create **objects**, and how to work with two types of variables inside a class — **instance variables** (unique to each object) and **class variables** (shared among all objects). We also explored how **methods** are defined inside a class and how they can get, set, or compute values using `self`.

Today, we take that knowledge a step further into the most powerful features of OOP:

- **Inheritance** — Reusing code from existing classes
- **The `super()` keyword** — Talking to your parent class
- **Types of Inheritance** — Single, Multiple, Multi-level, Hierarchical
- **Method Overriding** — Redefining an inherited method
- **Method Resolution Order (MRO)** — How Python decides which version of a method to run
- **Method Overloading** — Making one function handle different inputs
- **Operator Overloading** — Giving custom meaning to operators like `+`

---

## Introduction to Inheritance

**Official Definition:** Inheritance is an OOP mechanism where a new class (called a **child** or **derived** class) acquires the attributes and methods of an existing class (called a **parent** or **base** class).

**In Simple Words:** Imagine you already wrote code for a class called `Animal`. Now you want to create a `Dog` class. A dog is *also* an animal — it shares many features like eating, moving, and making sound. Instead of writing all that code again from scratch, you simply "inherit" it from `Animal`. You get everything for free, and you just add what's unique to a dog.

**Real-Life Example:** Think of a government job application form. There's a common base form everyone fills (name, address, age). If you're applying for a specific department, they give you an additional sheet with department-specific questions. The base form is your **parent class**; the additional sheet combined with it is the **child class**.

**Why Inheritance?**
- **Avoid code duplication** — Write the common logic once, reuse it everywhere.
- **Model real-world relationships** — A `Cat` *is an* `Animal`. A `Dog` *is an* `Animal`. This relationship maps directly to inheritance.

**Key Terminology:**
- The class being inherited from → **Parent Class** (also called **Base Class**)
- The class that inherits → **Child Class** (also called **Derived Class**)

---

## Syntax of Inheritance in Python

The syntax is simple — write the parent class name inside parentheses when defining the child class.

```python
# Define the parent (base) class
class Animal:
    # Constructor sets the name for every animal object
    def __init__(self, name):
        self.name = name  # Instance variable — unique per object

    # A method to print the animal's name
    def info(self):
        print("Animal name:", self.name)

# Define the child (derived) class — Dog inherits from Animal
class Dog(Animal):
    # Dog adds its own method — Sound
    def sound(self):
        # self.name comes from the parent class Animal
        print(self.name, "barks")

# Create an object of the Dog class
d = Dog("Buddy")

# Calling info() — this method is inherited from Animal
d.info()   # Output: Animal name: Buddy

# Calling sound() — this method is defined in Dog itself
d.sound()  # Output: Buddy barks
```

**How the code works:**
- `Dog("Buddy")` calls `Animal`'s constructor because `Dog` inherited it.
- `d.info()` works even though `info` is not written inside `Dog` — it is **inherited** from `Animal`.
- `d.sound()` is `Dog`'s own method, using `self.name` that was set by `Animal`'s constructor.
- `d` is only an object of `Dog`, not `Animal` — but because of inheritance, it has access to `Animal`'s features.

---

## The `super()` Keyword

Now that we understand inheritance, a natural question comes up: what if the child class needs to **access or call something from the parent class**?

**Official Definition:** `super()` is a built-in Python function that returns a **proxy object** of the parent class, allowing the child class to call parent methods.

**In Simple Words:** Just like `self` refers to the current object, `super()` gives you a temporary handle to the *parent* object. With that handle, you can call any method or constructor of the parent.

**Real-Life Example:** Imagine you are a junior employee and you need to escalate a task to your manager. `self` is you. `super()` is your manager — you are borrowing their authority to get something done.

**Most common use of `super()`** — calling the parent constructor:

```python
class Parent:
    def __init__(self):
        self.a = "value from Parent"  # Parent sets its own variable

    def show(self):
        print("This is the Parent class method")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call Parent's constructor to initialize parent's variables
        self.b = "value from Child"  # Child sets its own variable

    def show(self):
        super().show()          # Call the parent's version of show()
        print("This is the Child class method")

obj = Child()
obj.show()
# Output:
# This is the Parent class method
# This is the Child class method
```

**How the code works:**
- `super().__init__()` ensures that the parent's constructor runs, so `self.a` is properly set.
- `super().show()` calls the parent's `show()` method first, then the child adds its own output.
- It is **recommended but not mandatory** to call `super().__init__()`. If the parent constructor requires arguments to set critical variables, then calling it becomes essential.

---

## Types of Inheritance

Now that we know what inheritance is and how `super()` works, let's see the four different *patterns* in which you can use inheritance.

### 1. Single Inheritance

**What it is:** One child class inherits from exactly one parent class.

```
Animal
  └── Dog
```

This is the most basic type — the `Animal → Dog` example we just saw is Single Inheritance. There is one parent and one child. Clean, simple, and the most common pattern.

---

### 2. Multiple Inheritance

**What it is:** One child class inherits from **more than one** parent class at the same time.

```
Mother    Father
    \       /
      Son
```

**Real-Life Example:** A `Son` naturally gets traits from both his `Mother` and his `Father`. Similarly, in code, a `Son` class can inherit attributes from both `Mother` and `Father` classes.

```python
# First parent class — Mother
class Mother:
    mother_name = ""  # Class variable

    def mother(self):
        print("Mother's name:", self.mother_name)

# Second parent class — Father
class Father:
    father_name = ""  # Class variable

    def father(self):
        print("Father's name:", self.father_name)

# Son inherits from BOTH Mother and Father — Multiple Inheritance
class Son(Mother, Father):
    def parents(self):
        print("Father:", self.father_name)
        print("Mother:", self.mother_name)

# Create a Son object
s1 = Son()
s1.father_name = "Ram"
s1.mother_name = "Sita"
s1.parents()
# Output:
# Father: Ram
# Mother: Sita
```

**How the code works:**
- `class Son(Mother, Father)` — the two class names in the parentheses tell Python to inherit from *both*.
- `s1` can access `father_name` from `Father` and `mother_name` from `Mother` directly.
- The order you write the parents — `(Mother, Father)` vs `(Father, Mother)` — matters during Method Resolution Order (explained ahead).

---

### 3. Multi-level Inheritance

**What it is:** Inheritance is chained — A is the parent of B, and B is the parent of C. So C inherits from B, which itself inherits from A.

```
Grandfather
    └── Father
          └── Son
```

**Real-Life Example:** Your grandfather taught your father certain values. Your father taught you the same values. You didn't learn them directly from your grandfather, but you still have them — through a chain.

```python
# Grandparent class
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name  # Store grandfather's name

# Father class — inherits from Grandfather
class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        self.father_name = father_name  # Store father's name
        # Manually call Grandfather's constructor to set grandfather_name
        Grandfather.__init__(self, grandfather_name)

# Son class — inherits from Father (which already inherits from Grandfather)
class Son(Father):
    def __init__(self, son_name, father_name, grandfather_name):
        self.son_name = son_name  # Store son's name
        # Call Father's constructor — which will also call Grandfather's
        Father.__init__(self, father_name, grandfather_name)

    def display(self):
        print("Son:", self.son_name)
        print("Father:", self.father_name)
        print("Grandfather:", self.grandfather_name)

# Create a Son object with all three names
s = Son("Arjun", "Pandu", "Bhishma")
s.display()
# Output:
# Son: Arjun
# Father: Pandu
# Grandfather: Bhishma
```

**How the code works:**
- `Son` only directly inherits from `Father`, but because `Father` inherits from `Grandfather`, `Son` gets access to `Grandfather`'s attributes as well.
- When you call `Father.__init__(self, ...)`, it chains up to `Grandfather.__init__()`, setting all variables correctly.
- This is the difference from Multiple Inheritance — here, one inherits from *one* at a time, in a chain, not simultaneously.

---

### 4. Hierarchical Inheritance

**What it is:** Multiple child classes all inherit from the **same single parent class**. The children are at the same level, with no relationship between them.

```
       Parent
      /      \
  Child1    Child2
```

**Real-Life Example:** A university has departments — Computer Science, Electronics, Mechanical. All departments share common "University" features (enrollment, fee structure, administration), but each has its own specialization. The university is the parent; each department is a child.

```python
# Common parent class
class Parent:
    def function1(self):
        print("Parent class function")

# First child class
class Child1(Parent):
    def function2(self):
        print("Child 1 class function")

# Second child class — also inherits from Parent
class Child2(Parent):
    def function3(self):
        print("Child 2 class function")

# Create objects for both child classes
obj1 = Child1()
obj2 = Child2()

obj1.function1()  # From Parent
obj1.function2()  # From Child1

obj2.function1()  # From Parent
obj2.function3()  # From Child2

# Output:
# Parent class function
# Child 1 class function
# Parent class function
# Child 2 class function
```

**How the code works:**
- `Child1` and `Child2` have no relationship with each other — they're siblings.
- Both can use `function1()` from `Parent`, but each has its own unique method.

---

## Method Overriding

Now that we know how to inherit methods, what if you're **not happy** with the parent's version of a method? What if you want to **redefine** it in the child class?

**Official Definition:** Method Overriding means a child class provides its **own specific implementation** of a method that it already inherited from the parent class. The method name and parameters stay the same — only the body (logic) changes.

**In Simple Words:** You inherited a function from your parent. But you want it to behave differently in your context. So you write the function again inside your class with a new definition. Now your version will be used instead of the parent's version.

**Real-Life Example:** A general `Animal` class has a `move()` method that just says "the animal moves." But a `Dog` class overrides it to say "the dog runs on four legs." The name is the same, but the behavior is specific to the dog.

```python
# Parent class
class Parent:
    def __init__(self):
        self.value = "inside Parent"  # Parent sets its own value

    def show(self):
        print("Value:", self.value)  # Parent's version of show()

# Child class — overrides the show() method
class Child(Parent):
    def __init__(self):
        super().__init__()         # Call parent constructor to set parent's value
        self.value = "inside Child" # Child overrides the value too

    def show(self):
        print("Hi +", self.value)  # Child's OWN version of show()

# Parent object uses Parent's show()
obj1 = Parent()
obj1.show()  # Output: Value: inside Parent

# Child object uses Child's overridden show()
obj2 = Child()
obj2.show()  # Output: Hi + inside Child
```

**How the code works:**
- `obj2.show()` calls the `Child` version of `show()`, NOT the `Parent` version.
- Python always looks for a method **in the current class first**, before going to the parent.
- If the child does NOT define `show()`, Python automatically falls back to the parent's version.
- This is powerful — it lets you customize inherited behavior without rewriting everything.

---

## Method Resolution Order (MRO)

As inheritance gets complex — especially with Multiple Inheritance — a problem can arise. If the same method exists in multiple parent classes, Python needs a rule to decide **which version to run**. This rule is called the **Method Resolution Order**.

**Official Definition:** MRO is the order in which Python searches through a class and all its parent classes to find the definition of a method being called.

**In Simple Words:** When you call a method on an object, Python checks classes one by one — like checking floors of a building — until it finds the method. MRO defines the exact order of those floors.

**The Diamond Problem** — This is the classic case MRO solves:

```
     A
    / \
   B   C
    \ /
     D
```

If `A`, `B`, and `C` all define a method `foo()`, and `D` inherits from both `B` and `C`, which `foo()` does Python pick when you call it on a `D` object?

**Python's MRO Rule (C3 Linearization):**
1. **First:** Check the class of the object itself (D).
2. **Then:** Follow the inheritance order left-to-right (B before C, since D inherits as `class D(B, C)`).
3. **Finally:** Check the common parent (A) last.

So the MRO for `class D(B, C)` is: **D → B → C → A**

```python
# Base class A
class A:
    def fun(self):
        print("In class A")

# B inherits from A, overrides fun()
class B(A):
    def fun(self):
        print("In class B")

# C inherits from A, overrides fun()
class C(A):
    def fun(self):
        print("In class C")

# D inherits from both B and C
class D(B, C):
    def no_fun(self):
        print("D's own method")

# Create object of D
a = D()
a.fun()         # Output: In class B  (Python found fun() in B first)

# Check the MRO order explicitly
print(D.mro())
# Output: [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

**How the code works:**
- `a.fun()` → Python checks D (no `fun`), then B (found `fun`!) → prints "In class B"
- `D.mro()` shows the exact search order Python uses
- You can also check `D.__mro__` — the difference is `mro()` returns a **list**, `__mro__` returns a **tuple**

**`super()` and MRO together** — When you call `super()` inside a class, Python uses MRO to decide which class to jump to next. This is how you can chain constructor calls across all parent classes in Multiple Inheritance:

```python
class A:
    def __init__(self):
        super().__init__()   # Pass the chain up (safe to call even at the top)
        print("Initializing A")

class B(A):
    def __init__(self):
        super().__init__()   # MRO says: after B, go to A
        print("Initializing B")

class C(B, A):
    def __init__(self):
        super().__init__()   # MRO says: after C, go to B
        print("Initializing C")

obj = C()
# Output (constructors run in reverse MRO order):
# Initializing A
# Initializing B
# Initializing C
```

**How the code works:**
- When `C()` is called, its `__init__` runs → calls `super().__init__()` → goes to B's `__init__`
- B's `__init__` calls `super().__init__()` → goes to A's `__init__`
- A prints first, then B, then C — because the `print` statements execute *after* the `super()` calls return
- Using `super().__init__()` in every class is the **recommended pattern** to ensure all parent constructors run in Multiple Inheritance

---

## Method Overloading

So far, we've seen **Method Overriding** — same name, same parameters, different body. Now let's look at **Method Overloading** — same name, but **different parameters**.

**Official Definition:** Method Overloading means defining multiple methods with the same name in a class, but each method accepts a different number or type of parameters.

**In Simple Words:** Imagine a `calculate()` function. If you pass two numbers, it should add them. If you pass three, it should multiply them. Same function name, different behavior based on inputs.

**Important Note — Python's Limitation:** Unlike Java or C++, **Python does not natively support method overloading**. If you define two functions with the same name in a class, the second definition simply overwrites the first. Python solves this problem using two techniques:

### Technique 1: Default Arguments

```python
def add(a, b, c=0):  # c has a default value of 0
    return a + b + c

print(add(10, 20))       # Output: 30  (called with 2 args)
print(add(10, 20, 30))   # Output: 60  (called with 3 args)
```

**In Simple Words:** Give some parameters a default value. If the caller doesn't pass that argument, the default kicks in. This lets one function handle different call signatures.

### Technique 2: Using `**kwargs` (Keyword Arguments)

`**kwargs` is a special Python keyword that captures any number of **named (keyword) arguments** into a dictionary. It acts like a "catch-all bucket" for extra parameters.

```python
class A:
    def __init__(self, a, **kwargs):  # 'a' is captured, rest go into kwargs
        self.a = a
        super().__init__(**kwargs)    # Pass remaining kwargs to next class in MRO

class B(A):
    def __init__(self, b, **kwargs):  # 'b' is captured, rest go into kwargs
        self.b = b
        super().__init__(**kwargs)    # Pass remaining kwargs further up

class C(B, A):
    def __init__(self, a, b, c):
        self.c = c
        # Pass a and b as keyword arguments to parent classes via MRO
        super().__init__(a=a, b=b)

obj = C(10, 20, 30)
print(obj.a, obj.b, obj.c)  # Output: 10 20 30
```

**How the code works:**
- `C`'s constructor receives all three values: `a=10, b=20, c=30`
- It stores `c=30` itself, then passes `a=10, b=20` as `kwargs` to `super()`
- MRO sends this to B → B captures `b=20`, passes `a=10` further
- A captures `a=10`, done. All three attributes are properly set.

### Technique 3: Duck Typing

**Official Definition:** Duck Typing is a Python concept where the type of an object is determined by its behavior (what methods it has), not by its class declaration.

**In Simple Words:** "If it walks like a duck and quacks like a duck, it's a duck." If an object has a `use()` method, you can call `use()` on it — you don't care what class it belongs to.

**Real-Life Example:** A `perform_task()` function that works with any "tool" — a pen, an eraser, or a marker. Each tool has a `use()` method, but the behavior is different.

```python
# Pen class — has a use() method
class Pen:
    def use(self):
        return "Writing"  # Pen's use is writing

# Eraser class — also has a use() method
class Eraser:
    def use(self):
        return "Erasing"  # Eraser's use is erasing

# This function works with ANY object that has a use() method
def perform_task(tool):
    print(tool.use())  # Calls use() on whatever is passed

# Same function, different behavior based on the object
perform_task(Pen())     # Output: Writing
perform_task(Eraser())  # Output: Erasing
```

**How the code works:**
- `perform_task()` doesn't know or care whether it receives a `Pen` or `Eraser` object.
- As long as the object has a `use()` method, it works — this is Duck Typing.
- This is a very common pattern in large Python projects for achieving flexible, polymorphic behavior.

---

## Operator Overloading

We saw how to overload methods. Now, Python lets you do the same with **operators** like `+`, `-`, `<`, `==`, etc. This is called **Operator Overloading**.

**Official Definition:** Operator Overloading means redefining the behavior of a standard Python operator for custom class objects, using special methods called **Magic Functions** (or **Dunder Methods**).

**In Simple Words:** By default, `+` adds numbers. But what does `+` mean for two `Student` objects? Python lets you define that. You tell Python: "When someone does `student1 + student2`, do THIS."

**Real-Life Example:** In mathematics, complex numbers have a real part and an imaginary part. `(3+2i) + (1+4i) = (4+6i)`. You can define this custom addition using operator overloading in Python.

**Magic Functions — How operators map to method names:**

| Operator | Magic Function | Example |
|----------|---------------|---------|
| `+` | `__add__(self, other)` | `obj1 + obj2` |
| `-` | `__sub__(self, other)` | `obj1 - obj2` |
| `<` | `__lt__(self, other)` | `obj1 < obj2` |
| `==` | `__eq__(self, other)` | `obj1 == obj2` |
| `*` | `__mul__(self, other)` | `obj1 * obj2` |

**How Python translates `obj1 + obj2`:**

When you write `obj1 + obj2`, Python internally converts it to:
```
obj1.__add__(obj2)
```
So `obj1` is accessed via `self`, and `obj2` is the argument `other`. You can now access both objects' data and define what "addition" means.

**Example — Simulating type-based addition using `*args`:**

```python
# A flexible add function using *args
def add(data_type, *args):  # First arg sets type, rest are values to combine
    if data_type == int:
        result = 0              # Start with integer identity value
    elif data_type == str:
        result = ""             # Start with empty string

    # Loop through all values and combine them
    for item in args:
        result += item          # += means add for int, concatenate for str

    return result

# Adding integers: 15 + 61
print(add(int, 15, 61))           # Output: 76

# Adding strings: "Dear" + "Students"
print(add(str, "Dear ", "Students"))  # Output: Dear Students
```

**How the code works:**
- `*args` captures all positional arguments (after `data_type`) into a tuple.
- Based on `data_type`, the initial `result` is set appropriately (`0` for int, `""` for str).
- The `for` loop iterates over all values in `args` and adds them to `result`.
- Same function — totally different behavior based on the type passed. This is the foundation of overloading in Python.

**Note:** In the next session, we will see the complete class-based operator overloading using magic functions like `__add__` directly inside a class definition.

---

## Key Takeaways

- **Inheritance** lets one class reuse code from another class, avoiding duplication and modeling real-world "is-a" relationships. The class that inherits is the **child/derived** class; the class being inherited from is the **parent/base** class.
- **`super()`** gives access to the parent class from inside the child class. It is most importantly used to call the parent constructor during initialization, especially in multi-level and multiple inheritance chains.
- **Method Overriding** lets a child class redefine an inherited method — same name, same parameters, different body. Python always searches the child class first, so the child's version takes priority.
- **Method Resolution Order (MRO)** is Python's algorithm (D → B → C → A pattern) that determines which class's method gets called when the same method exists in multiple parent classes. Use `ClassName.mro()` to inspect it.
- **Method Overloading and Operator Overloading** extend flexibility — Python achieves overloading through default arguments, `**kwargs`, duck typing, and magic functions (`__add__`, `__lt__`, etc.) rather than native overloading like Java. These concepts directly lead into **Polymorphism**, which we will explore in the next session.

---

## Important Commands, Libraries & Terminologies

| Term / Syntax | Meaning |
|---|---|
| `class Dog(Animal):` | Dog inherits from Animal (Single Inheritance) |
| `class Son(Mother, Father):` | Son inherits from both Mother and Father (Multiple Inheritance) |
| `super().__init__()` | Calls the parent class's constructor |
| `super().method_name()` | Calls a method defined in the parent class |
| `ClassName.mro()` | Returns the Method Resolution Order as a list |
| `ClassName.__mro__` | Returns the Method Resolution Order as a tuple |
| **Method Overriding** | Child redefines an inherited method (same name, same params) |
| **Method Overloading** | Same method name, different parameter list (Python uses `*args`/`**kwargs`) |
| `*args` | Captures any number of positional arguments into a tuple |
| `**kwargs` | Captures any number of keyword arguments into a dictionary |
| **Duck Typing** | Python determines behavior by method availability, not by class type |
| **Operator Overloading** | Custom behavior for operators using magic functions |
| `__add__(self, other)` | Magic function for `+` operator |
| `__lt__(self, other)` | Magic function for `<` operator |
| **Dunder Methods** | Methods with double underscores — e.g., `__init__`, `__add__` (also called Magic Methods) |
| **Diamond Problem** | Ambiguity when two parent classes share a common grandparent — solved by MRO |
| **Base / Parent Class** | The class being inherited from |
| **Derived / Child Class** | The class that inherits from a parent |
