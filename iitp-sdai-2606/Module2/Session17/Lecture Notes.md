# JavaScript Fundamentals I

In previous session, you practiced building page layouts using **CSS Flexbox and Grid**. Those skills helped you control *where* content appears on a page.  
In this session, you’ll add **JavaScript** so the page can *react*, *calculate*, and *manage data* in the browser.

You have already learned **Python** in module 1, so you can think like a programmer already.  
Now we’ll focus on the differences that matter in JavaScript, especially around variables, control flow, and data structures.

## What you will learn in this session

- How **JavaScript setup** works in a browser using `<script>` and the **Developer Console**
- How to declare **variables** using `let`, `const`, and `var`
- How JavaScript **data types** behave (and how they differ from Python expectations)
- How **control flow** works using conditions and loops
- How to use **strings**, **arrays**, and **objects** in small practical programs

## Why JavaScript is needed (even after learning Python)

![Python works like the kitchen manager behind the scenes; JavaScript is the waiter who serves guests in the browser dining hall](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session17/session17-01-python-kitchen-js-waiter.png?v=20260804)

If you can already write programs in Python, why add JavaScript?

- **JavaScript runs in the browser**  
  - *Official meaning:* **JavaScript** is the scripting language that browsers execute to build interactive web pages.  
  - *In simple words:* Your browser needs a language to respond to clicks, form input, and dynamic changes.  
  - *Real-life example:* CSS decides the furniture layout, but JavaScript is the person who moves furniture when you ask.

- **Python typically runs outside the browser**  
  - *Official meaning:* **Python** code usually runs on a server (backend) or in tools, not directly inside the browser.  
  - *In simple words:* Browser users cannot execute Python code on their page unless you connect a server API.  
  - *Real-life example:* Python is like the kitchen manager cooking food, while JavaScript is the waiter who brings food to tables at the right time.

- **Front-end interactivity requires a front-end language**  
  - *Official meaning:* To change the **Document Object Model (DOM)**, JavaScript is the standard tool.  
  - *In simple words:* DOM is the page structure, and JavaScript lets you change it.  
  - *Real-life example:* DOM is the blueprint; JavaScript is the worker who updates the blueprint live.

## Python vs JavaScript: variables (the “first difference that matters”)

![Side-by-side: Python uses simple name labels on jars; JavaScript uses let for refillable jars and const for sealed jars that cannot be reassigned](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session17/session17-02-python-vs-js-variables.png?v=20260804)

You already know this idea in Python: you assign values to names.  
In JavaScript, you still assign values to names, but you also choose *how the variable is scoped* and *whether it can be reassigned*.

### Python variable declaration (assignment)

```python
name = "Amit"  # Create a variable name and store a text value
age = 20  # Create a variable age and store an integer value
pi = 3.14  # Create a variable pi and store a floating-point value
is_student = True  # Create a boolean variable that stores True/False
```

**How the code works**

- Each Python line creates a variable by assigning a value.
- Python variables are flexible because you can reassign names later.
- The type (string, int, float, bool) is associated with the value at runtime.

### JavaScript variable declaration (`let` / `const`)

```javascript
let name = "Amit"; // Create a variable named `name` that can be reassigned
let age = 20; // Create a variable `age` that can be reassigned
const pi = 3.14; // Create a constant `pi` that cannot be reassigned
const isStudent = true; // Create a constant boolean variable
```

**How the code works**

- Each JavaScript line declares a variable and assigns an initial value.
- `let` allows reassignment, similar to “normal” assignment style you used in Python.
- `const` creates a variable that you cannot reassign, which helps prevent accidental bugs.

## JavaScript setup in the browser

![HTML page connected through a script doorway to app.js, with the browser Developer Console showing JS is connected](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session17/session17-03-js-html-script-console.png?v=20260804)

You will attach JavaScript to HTML and use `console.log()` to see what’s happening.  
This is the fastest way to learn because you get instant feedback.

### Key terms: `<script>` and the browser console

- **`<script>` tag**  
  - *Official meaning:* The `<script>` tag tells the browser which JavaScript code to load and execute.  
  - *In simple words:* It is the “door” between HTML and JavaScript.  
  - *Real-life example:* Like adding an electrician to a building plan so electricity can work.

- **Developer Console**  
  - *Official meaning:* The **console** is a panel in browser **DevTools** where you can inspect logs and errors.  
  - *In simple words:* It is where you ask the browser “what is going on?”.  
  - *Real-life example:* Like a shop’s billing screen showing what the system accepted.

### Small complete example: attach JS to HTML

Create an HTML file named `index.html` with the following complete content:

```html
<!doctype html> <!-- Tell the browser this is an HTML5 document -->
<html> <!-- Start the HTML document -->
  <head> <!-- The head section holds metadata and resources -->
    <meta charset="utf-8"> <!-- Use UTF-8 character encoding -->
    <title>JS Setup Demo</title> <!-- Set the page title -->
  </head> <!-- End of head section -->
  <body> <!-- The body contains visible content -->
    <h1>JavaScript Fundamentals I</h1> <!-- Display a heading on the page -->
    <script src="./app.js"></script> <!-- Load JavaScript from app.js -->
  </body> <!-- End of body section -->
</html> <!-- End the HTML document -->
```

Now create a JavaScript file named `app.js` with this complete content:

```javascript
console.log("JS is connected"); // Print a message to confirm JS runs

const year = 2026; // Store a number in a constant variable
console.log("Year:", year); // Print the label and the value

let clicks = 0; // Start click counter at 0 using a reassignable variable
console.log("Initial clicks =", clicks); // Show the initial value in the console
```

**How the code works**

- The HTML page loads `app.js` using the `src` attribute.
- The JavaScript file runs immediately when the browser loads it.
- `console.log()` writes messages into the console so you can verify execution.

### Debugging: read errors like a detective

When JavaScript breaks, the browser usually tells you:

- The **error type** (example: `ReferenceError`, `TypeError`, `SyntaxError`)
- The **line number** where it failed
- A helpful message about what went wrong

**Student activity**

- Open your page in the browser.
- Open DevTools and go to **Console**.
- Reload the page and confirm you see `JS is connected`.
- If you see nothing, check the `app.js` file path in the `<script src="./app.js">` line.

## Variables and data types in JavaScript

Now you will learn variables and primitive data types in a way that connects to Python.  
You already understand assignment in Python, so we’ll concentrate on JavaScript-specific rules.

## Variable declarations: `var`, `let`, and `const`

### `var`

- **Official meaning:** `var` is an older variable declaration keyword in JavaScript.  
- **In simple words:** It has function-level behavior that often leads to confusing bugs.  
- **Real-life example:** Like using an old shortcut that still works, but causes mistakes when traffic changes.

Because of this, modern JavaScript mostly avoids `var` in new projects.

### `let`

- **Official meaning:** `let` declares a block-scoped variable that you can reassign.  
- **In simple words:** You can update the value later, but the variable lives only in the block you declared it.  
- **Real-life example:** Like a label on a box that stays valid only inside the room you are using.

### `const`

- **Official meaning:** `const` declares a block-scoped variable that cannot be reassigned.  
- **In simple words:** You must set it once, but you can still change *contents* if it’s an object or array.  
- **Real-life example:** Like a fixed registration number on a vehicle: you cannot change the number, but the vehicle parts can be maintained.

### Side-by-side: reassignment rules

```javascript
let x = 10; // Declare x with let so it can be reassigned
x = 20; // Reassign x to a new value
console.log("x =", x); // Print x to confirm reassignment worked

const y = 5; // Declare y with const so it cannot be reassigned
// y = 6; // Uncommenting this would cause an error because const cannot be reassigned
console.log("y =", y); // Print y to show its value remains stable
```

**How the code works**

- `let` allows `x = 20` after the first assignment.
- `const` prevents reassignment, which catches accidental changes early.

### Where values are stored: names vs values

In JavaScript, you think like this:

- **Variable name** is a label you use.
- **Value** is the actual data.

In Python, you also do this, but JavaScript adds rules about *how* labels behave in blocks.

## Primitive data types you should know

JavaScript has primitive types that represent basic values.  
Some of these map nicely from Python, but the behavior may feel slightly different.

### `string`

- **Official meaning:** A **string** is text like `"hello"`.  
- **In simple words:** It’s a collection of characters.  
- **Real-life example:** Like the text on a poster.

### `number`

- **Official meaning:** A **number** stores numeric values such as `10` or `3.14`.  
- **In simple words:** It’s the mathematical quantity.  
- **Real-life example:** Like your temperature reading from a thermometer.

### `boolean`

- **Official meaning:** A **boolean** stores `true` or `false`.  
- **In simple words:** It represents “yes/no”.  
- **Real-life example:** Like a light switch state.

### `undefined` and `null`

- **`undefined`**  
  - *Official meaning:* `undefined` means a variable exists but has no value assigned yet.  
  - *In simple words:* It’s “nothing happened here”.  
  - *Real-life example:* Like an empty seat assigned but nobody sat yet.

- **`null`**  
  - *Official meaning:* `null` is intentionally “no value” set by you.  
  - *In simple words:* It’s “I meant empty”.  
  - *Real-life example:* Like writing “no student here” on a form.

### Quick type check with `typeof`

`typeof` helps you see the runtime type of a value.

```javascript
const s = "India"; // s is a string
console.log(typeof s); // Print the type of s

const n = 42; // n is a number
console.log(typeof n); // Print the type of n

const b = true; // b is a boolean
console.log(typeof b); // Print the type of b

let u; // Declare u without a value so it becomes undefined
console.log(u); // Print u to show its current value
console.log(typeof u); // Print the type of u

const empty = null; // empty is explicitly set to null
console.log(empty); // Print empty to show its value
console.log(typeof empty); // Print the type (note: typeof null is a known quirk)
```

**How the code works**

- `typeof` prints a string like `"string"` or `"number"`.
- Declaring `let u;` without assigning makes `u` become `undefined`.
- `null` is special and `typeof null` returns `"object"` which is a historical JavaScript behavior.

### Python connection: dynamic typing

In Python you know variables are dynamically typed.  
JavaScript is also dynamically typed, but you still must manage:

- which variable keyword you used (`let` vs `const`)
- and the scope where the variable is valid (blocks vs functions)

## Control flow: conditions and loops

![Campus path fork for if and else decisions, with a circular loop track for repeating steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session17/session17-04-control-flow-paths-loops.png?v=20260804)

Control flow is how you decide:

- **What to do now**
- **What to do next**
- **When to repeat**

You already used `if` and loops in Python.  
Now you’ll see the JavaScript syntax and a few operators.

## Operators (quick essentials)

### Common operators you will use daily

- **Arithmetic**
  - `+` addition  
  - `-` subtraction  
  - `*` multiplication  
  - `/` division  
  - `%` remainder  

- **Comparison**
  - `===` strict equality (value AND type)
  - `!==` strict not-equality
  - `>` greater than
  - `<` less than

- **Logical**
  - `&&` AND
  - `||` OR
  - `!` NOT

### Why `===` matters

In JavaScript, `==` is “loose equality” and can do type coercion.  
For fundamentals, we prefer **strict** comparisons using `===` and `!==`.

```javascript
const a = 5; // a is a number
const b = "5"; // b is a string

console.log(a == b); // Loose equality may convert types and return true
console.log(a === b); // Strict equality checks type too and returns false
```

**How the code works**

- `a == b` can be true because JavaScript tries to convert types.
- `a === b` is false because `5` (number) is not the same as `"5"` (string).

## Conditional statements: `if`, `else if`, `else`

### Structure

- `if (condition) { ... }` runs the block when the condition is true.
- `else if (condition) { ... }` checks the next condition.
- `else { ... }` runs when none of the previous conditions match.

### Example: decide based on age

```javascript
const age = 17; // Store age as a number

if (age >= 18) { // Check if age is 18 or more
  console.log("Eligible to vote"); // Print message when condition is true
} else { // Runs when age is not 18 or more
  console.log("Not eligible to vote yet"); // Print message when condition is false
} // End if/else block
```

**How the code works**

- The code evaluates `age >= 18`.
- If it’s true, it prints the eligible message.
- Otherwise, it prints the not-eligible message.

### Student activity: test your own values

- Change `const age = 17` to `19`.
- Refresh the page and observe the console output changes.
- Now try `18` exactly and verify the boundary works correctly.

## Switch statement (optional but useful)

**Official meaning:** A **`switch`** is a conditional tool that checks the same expression against multiple cases.  
**In simple words:** It’s like “if-else ladder” but cleaner when you check one variable many times.  
**Real-life example:** Like choosing a menu item based on the menu number.

```javascript
const day = "Mon"; // Store a day string

switch (day) { // Start switch by checking `day`
  case "Mon": // If day is "Mon"
    console.log("Start of the week"); // Print Monday message
    break; // Stop switch after handling the match
  case "Fri": // If day is "Fri"
    console.log("Almost weekend"); // Print Friday message
    break; // Stop switch after handling the match
  default: // If no case matches
    console.log("Regular day"); // Print a fallback message
} // End switch
```

**How the code works**

- `switch` compares `day` against each `case`.
- `break` prevents falling into the next case by accident.
- `default` runs when no case matches.

## Loops: repeating tasks

Loops help you repeat code without copying it many times.  
In Python you used `for` and `while`.  
JavaScript gives you similar loop ideas with slightly different syntax.

## `while` loop

- **Official meaning:** A **`while`** loop repeats while a condition is true.  
- **In simple words:** It checks the condition first, then repeats.  
- **Real-life example:** Like continuously studying “until my understanding becomes clear”.

```javascript
let count = 1; // Start counting from 1

while (count <= 3) { // Repeat while count is 3 or less
  console.log("count =", count); // Print the current count
  count = count + 1; // Increase count to avoid an infinite loop
} // End while loop
```

**How the code works**

- The condition `count <= 3` is checked each time.
- The loop stops when the condition becomes false.
- Updating `count` ensures the loop eventually ends.

## `for` loop

- **Official meaning:** A **`for`** loop is a repeat loop with initialization, condition, and update in one line.  
- **In simple words:** It’s convenient when you know how many times you want to repeat.  
- **Real-life example:** Like counting pages from page 1 to page 20.

```javascript
for (let i = 0; i < 3; i = i + 1) { // Initialize i, check i < 3, then update i each round
  console.log("i =", i); // Print i each iteration
} // End for loop
```

**How the code works**

- `let i = 0` creates the loop variable.
- `i < 3` decides if another iteration should happen.
- `i = i + 1` updates i after each iteration.

## Loop control: `break` and `continue`

- **`break`**  
  - *Official meaning:* Stops the current loop immediately.  
  - *In simple words:* “Stop repeating now.”  
  - *Real-life example:* Like exiting the conversation when you got your answer.

- **`continue`**  
  - *Official meaning:* Skips the rest of the current iteration and goes to the next one.  
  - *In simple words:* “Skip this time, do next.”  
  - *Real-life example:* Like skipping one step in a routine.

```javascript
for (let i = 0; i < 5; i = i + 1) { // Loop i from 0 to 4
  if (i === 2) { // Check a specific value
    break; // Stop the loop completely when i is 2
  } // End if (i === 2)
  console.log("processed i =", i); // Print values for iterations before breaking
} // End for loop (break example)
```

**How the code works**

- The loop stops at `i === 2`.
- Values printed are for `i = 0` and `i = 1`.

## Data structures: strings, arrays, and objects

![An ordered spice shelf labelled array with slots 0, 1, 2; a labelled drawer cabinet labelled object with keys like name, age, and isActive](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session17/session17-05-arrays-objects-shelf-drawers.png?v=20260804)

Data structures help you store multiple values and represent real-world information.  
In Python you used lists and dictionaries.  
In JavaScript, you’ll use **strings**, **arrays**, and **objects** to achieve similar goals.

## Strings in JavaScript

- **Official meaning:** A **string** is text.  
- **In simple words:** You store words and characters.  
- **Real-life example:** Like writing messages on a note.

### Key string operations you will use

- Access characters using bracket notation: `text[0]`
- Get length using `.length`
- Transform text using methods like `.toUpperCase()` and `.trim()`

```javascript
const text = "  hello js  "; // Store a string with spaces around it
console.log(text.length); // Print the total length including spaces

const trimmed = text.trim(); // Remove leading and trailing spaces
console.log(trimmed); // Print the trimmed result

const upper = trimmed.toUpperCase(); // Convert trimmed text to uppercase
console.log(upper); // Print the uppercase result

console.log(upper[0]); // Access the first character of the uppercase string
```

**How the code works**

- `.length` tells how many characters exist in a string.
- `.trim()` removes extra spaces at the start and end.
- `.toUpperCase()` returns a transformed new string.
- `upper[0]` reads a character by index.

## Arrays in JavaScript

- **Official meaning:** An **array** is an ordered list of values.  
- **In simple words:** It’s like a row of boxes where each box has a position (index).  
- **Real-life example:** Like a phone contacts list where each contact sits in a specific slot.

### Creating and using arrays

```javascript
const nums = [10, 20, 30]; // Create an array with three numbers
console.log(nums[0]); // Print first element at index 0
console.log(nums[2]); // Print third element at index 2

console.log(nums.length); // Print number of elements in the array
```

**How the code works**

- Arrays are zero-indexed, so the first element is at index `0`.
- `.length` gives the count of elements.

### Modifying arrays: push

**Official meaning:** `.push(value)` adds an element to the end of an array.  
**In simple words:** It appends a new box at the back.  
**Real-life example:** Like adding a new book to the last position on your shelf.

```javascript
const basket = ["apple", "banana"]; // Create an array of items
basket.push("mango"); // Add mango to the end of the array
console.log(basket); // Print the updated array
```

**How the code works**

- `.push()` changes the array by adding one more element.
- `console.log` shows the new array content.

### Looping over an array

You can use a `for` loop to read each value.

```javascript
const colors = ["red", "green", "blue"]; // Create array of strings

for (let i = 0; i < colors.length; i = i + 1) { // Loop over indices 0 to length-1
  console.log("color =", colors[i]); // Print the current element by index
} // End for loop over colors
```

**How the code works**

- The loop runs as long as `i < colors.length`.
- `colors[i]` picks the element at the current position.

## Objects in JavaScript

- **Official meaning:** An **object** is a collection of key-value pairs.  
- **In simple words:** It’s like a labeled drawer where each label points to a value.  
- **Real-life example:** Like a form where each field has a label like “Name” and “Age”.

### Creating an object

```javascript
const student = { // Create an object for student details
  name: "Asha", // Store the student's name under key "name"
  age: 19, // Store the student's age under key "age"
  isActive: true // Store whether the student is active under key "isActive"
}; // End of object literal

console.log(student.name); // Access the value of key "name" using dot notation
console.log(student["age"]); // Access value of key "age" using bracket notation
```

**How the code works**

- `{ ... }` creates an object literal with keys and values.
- Dot notation uses `student.name`.
- Bracket notation uses `student["age"]`.

### Updating object values

```javascript
const book = { // Create an object describing a book
  title: "JS Basics", // Set title property
  pages: 120 // Set pages property
}; // End of book object

book.pages = 130; // Update pages to a new number
console.log(book.pages); // Print updated pages value
```

**How the code works**

- Even if you store the object in a `const` variable, you can still modify the object’s properties.
- `const` protects the variable binding, not the internal object data.

## Practical mini-programs (combined topics)

Now you’ll combine setup + variables + control flow + data structures.  
These small programs are designed to feel like real student work.

### Mini-program 1: score summary using conditionals

```javascript
const studentScore = 72; // Store a score from 0 to 100
let grade; // Declare grade but do not assign yet

if (studentScore >= 90) { // Check for A range
  grade = "A"; // Assign grade when condition matches
} else if (studentScore >= 80) { // Check for B range
  grade = "B"; // Assign grade when next condition matches
} else if (studentScore >= 70) { // Check for C range
  grade = "C"; // Assign grade when next condition matches
} else { // This runs when score is below 70
  grade = "D"; // Assign grade D for lower scores
} // End if/else grading chain

console.log("Score =", studentScore); // Print score for context
console.log("Grade =", grade); // Print computed grade
```

**How the code works**

- `grade` is updated using an `if / else if / else` chain.
- Exactly one branch runs because conditions are checked in order.

### Mini-program 2: array processing with a loop

```javascript
const marks = [10, 20, 30, 40]; // Create an array of marks
let total = 0; // Start total sum at 0

for (let i = 0; i < marks.length; i = i + 1) { // Loop through each mark
  total = total + marks[i]; // Add the current mark to total
} // End marks loop

console.log("Total marks =", total); // Print final sum
console.log("Average marks =", total / marks.length); // Compute average using division
```

**How the code works**

- The loop visits every element in the array.
- `total` accumulates results across iterations.

### Mini-program 3: object + condition

```javascript
const user = { // Create a user object with required fields
  name: "Ravi", // Store user name
  plan: "free", // Store user's subscription plan
  loginCount: 3 // Store how many times user logged in
}; // End of user object

if (user.plan === "premium") { // Check plan using strict equality
  console.log("Welcome premium user,", user.name); // Print premium message
} else { // Runs when user is not premium
  console.log("Welcome free user,", user.name); // Print free message
} // End premium/free plan conditional

if (user.loginCount > 0) { // Check loginCount is positive
  console.log("You have logged in before."); // Print a helpful message
} else { // Runs when loginCount is 0
  console.log("First time login detected."); // Print message for new users
} // End loginCount conditional
```

**How the code works**

- The program reads values from an object.
- Conditions decide which message to print.

## Common mistakes (and how to avoid them)

These mistakes are normal when you come from Python to JavaScript.  
Learning them early saves time later.

### Mistake 1: confusing `===` with `==`

Use `===` in fundamentals to avoid surprising type conversion.  
If you see unexpected results, check whether your values are strings or numbers.

### Mistake 2: forgetting to update loop variables

If a `while` loop condition never changes, the loop becomes infinite.  
Always confirm the loop eventually reaches a condition where it will stop.

### Mistake 3: assuming `const` means “data cannot change”

`const` prevents reassignment of the variable.  
It does not stop you from mutating object properties or array elements stored in that variable.

### Mistake 4: using variables before declaring them

Read console errors carefully.  
If you get a `ReferenceError`, find where the variable is first used and ensure it is declared before use.

## Key Takeaways

- **JavaScript** is needed for browser interactivity, while **Python** usually runs outside the browser.
- Variables in JavaScript use **`let`** and **`const`**, which control reassignment and block scope.
- Use **`if / else`** and loops (`for`, `while`) to control what your program does next.
- **Strings**, **arrays**, and **objects** are your core building blocks for real data.
- Debug with **`console.log()`** and the browser console to quickly find where logic goes wrong.

In the next session, you will continue building on these foundations to write more structured programs and work with browser interactions.  
You’ll also see how these fundamentals connect to writing cleaner code for bigger features.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| `console.log(...)` | Print messages to the browser console for debugging |
| `<script src="...">` | Load a JavaScript file inside an HTML page |
| `let` | Declare a block-scoped variable that can be reassigned |
| `const` | Declare a block-scoped variable that cannot be reassigned |
| `var` | Older declaration keyword with confusing behavior; usually avoid |
| `typeof` | Return the runtime type of a value |
| `if / else` | Run code depending on a condition |
| `for` | Loop with initialization, condition, update |
| `while` | Loop that repeats while a condition is true |
| `break` | Exit the loop immediately |
| `continue` | Skip to the next loop iteration |
| `string` | Text value like `"hello"` |
| `array` | Ordered list like `[1, 2, 3]` |
| `object` | Key-value collection like `{ name: "Asha" }` |

