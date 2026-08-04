# JavaScript Fundamentals II – Functions & Scope

In the previous session, you learned **JavaScript basics**: connecting JS to HTML, declaring variables with `let` and `const`, writing conditions and loops, and working with strings, arrays, and objects.  
Those building blocks let you store data and control flow.  
In this session, you will package logic into **reusable functions** and understand **scope**—where each variable can be seen and used.

You already wrote functions in **Python**, so the idea will feel familiar.  
JavaScript has a few different styles for writing functions, and those differences matter when you build browser features later.

## What you will learn in this session

- How to write **function declarations** and **function expressions**
- How to pass **parameters**, send **arguments**, and use **return values**
- How **arrow functions** work and when they are a good choice
- How **global scope** and **block scope** decide which variables a function can access
- How to practice these ideas with small, complete programs

## Why functions matter

![One chai recipe card on a stall counter reused for every customer — a function is a reusable recipe you follow again and again](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session18/session18-01-functions-chai-recipe-reuse.png?v=20260804)

So far, your code often ran from top to bottom as one long script.  
That works for tiny demos, but real programs repeat the same logic many times.  
**Functions** solve that problem by letting you write a task once and reuse it.

- **Function**  
  - *Official meaning:* A **function** is a named (or anonymous) block of code that performs a task when you call it.  
  - *In simple words:* A function is a recipe you can cook again and again without rewriting the steps.  
  - *Real-life example:* Instead of explaining “how to make chai” every time a guest arrives, you keep one chai recipe and follow it whenever needed.

- **Why reuse helps**  
  - One bug fix inside the function helps every call; your program stays shorter and easier to read.
  - Common doubt: tiny scripts can skip functions, but repeated logic becomes messy quickly.

## Python functions vs JavaScript functions

You already know this Python pattern:

```python
def greet(name):  # Define a function named greet that accepts name
    message = "Hello, " + name  # Build a greeting string
    return message  # Send the greeting back to the caller

result = greet("Priya")  # Call greet and store the returned value
print(result)  # Display Hello, Priya
```

**How the code works**

- `def` creates a reusable function; `name` is an input; `return` sends a result back.
- JavaScript does the same job with different syntax: declarations, expressions, and arrows.

## Function declarations

A **function declaration** is the most direct way to create a named function in JavaScript.  
It looks close to the Python idea, so it is a comfortable starting point.

- **Function declaration**  
  - *Official meaning:* A function created with the `function` keyword and a name, such as `function add(a, b) { ... }`.  
  - *In simple words:* You give the recipe a clear name and write the steps inside curly braces.  
  - *Real-life example:* Labeling a notebook page as “Railway ticket steps” so anyone can find and follow it.

### Complete example: greet a student

```javascript
function greet(name) { // Declare a function named greet with one parameter called name
  const message = "Hello, " + name + "!"; // Build a greeting string using the name value
  return message; // Send the greeting text back to whoever called greet
} // End of the greet function

const result = greet("Asha"); // Call greet with "Asha" and store the returned string
console.log(result); // Print Hello, Asha! in the browser console
```

**How the code works**

- `function greet(name)` creates a reusable block; `name` holds the value you pass when calling.
- `return message` hands the result back; `greet("Asha")` runs the function once.

### Student activity: write your first declaration

Open your browser console or a small `app.js` file and try this:

1. Write a function named `double` that accepts one number.
2. Inside the function, return the number multiplied by `2`.
3. Call `double(7)` and print the result with `console.log`.

Expected console output: `14`.

## Function expressions

Sometimes you store a function inside a variable, just like you store a number or a string.  
That style is called a **function expression**.

- **Function expression**  
  - *Official meaning:* A function created as a value and assigned to a variable, for example `const greet = function(name) { ... };`.  
  - *In simple words:* The function itself becomes data stored in a named box.  
  - *Real-life example:* Keeping a printed recipe card inside a labeled folder; the folder name is how you find the recipe.

### Complete example: expression style

```javascript
const greet = function (name) { // Create a function value and store it in the constant greet
  const message = "Welcome, " + name; // Build a welcome message using the given name
  return message; // Return the message to the caller
}; // End of the function expression assigned to greet

const text = greet("Ravi"); // Call the function stored in greet with argument "Ravi"
console.log(text); // Print Welcome, Ravi in the console
```

**How the code works**

- `const greet = function (...)` stores a function as a value; you still call it with `greet("Ravi")`.
- Declarations are often easier for beginners; expressions help when you treat a function like a value.

## Parameters and arguments

![Chai stall menu shows empty labeled slots as parameters; the customer’s actual choices fill those slots as arguments](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session18/session18-02-parameters-arguments-chai-stall.png?v=20260804)

Functions become powerful when they accept inputs.  
Those inputs have two related names that students often mix up.

- **Parameter**  
  - *Official meaning:* A named placeholder listed in the function definition.  
  - *In simple words:* The empty slot waiting for a value.  
  - *Real-life example:* A chai stall menu says “sugar level”; that label is the parameter.

- **Argument**  
  - *Official meaning:* The actual value you pass when you call the function.  
  - *In simple words:* The real data you put into the slot.  
  - *Real-life example:* You say “less sugar”; that choice is the argument.

### Complete example: bill calculator with parameters

```javascript
function calculateBill(price, quantity) { // Declare calculateBill with two parameters: price and quantity
  const total = price * quantity; // Multiply unit price by how many items were bought
  return total; // Return the final bill amount to the caller
} // End of the calculateBill function

const notebookBill = calculateBill(40, 3); // Pass arguments 40 and 3, store returned total
const penBill = calculateBill(10, 5); // Pass arguments 10 and 5, store returned total
console.log("Notebook bill:", notebookBill); // Print Notebook bill: 120
console.log("Pen bill:", penBill); // Print Pen bill: 50
```

**How the code works**

- `price` and `quantity` are parameters; `40` and `3` are arguments for the first call.
- The same function calculates different bills with different arguments.

### Default parameters

Sometimes a caller may skip an argument.  
You can give a **default value** so the function still works safely.

```javascript
function createProfile(name, city = "Not shared") { // city gets "Not shared" if caller omits it
  const profile = name + " lives in " + city; // Build a simple profile sentence
  return profile; // Return the profile text
} // End of the createProfile function

console.log(createProfile("Neha", "Pune")); // Print Neha lives in Pune
console.log(createProfile("Karan")); // Print Karan lives in Not shared
```

**How the code works**

- When `city` is provided, JavaScript uses that argument; when missing, it uses `"Not shared"`.
- Defaults reduce crashes caused by missing inputs.

## Return values

![Ticket counter clerk hands back a printed ticket — the return value is the answer the function gives back to the caller](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session18/session18-03-return-value-ticket-counter.png?v=20260804)

A function can do work quietly, or it can **return** a result for later use.  
`return` is how a function sends an answer back to the caller.

- **Return value**  
  - *Official meaning:* The value produced by a `return` statement and received by the caller.  
  - *In simple words:* The answer the function hands back.  
  - *Real-life example:* You ask the ticket counter for a ticket; the ticket you receive is the return value.

### Complete example: using returned results

```javascript
function getDiscount(price, percent) { // Declare getDiscount with price and percent parameters
  const discountAmount = (price * percent) / 100; // Calculate how much money is discounted
  return discountAmount; // Return only the discount amount
} // End of the getDiscount function

const shirtPrice = 800; // Store the original shirt price
const saved = getDiscount(shirtPrice, 10); // Call getDiscount and store returned savings
const finalPrice = shirtPrice - saved; // Subtract discount from original price
console.log("You saved:", saved); // Print the discount amount
console.log("Final price:", finalPrice); // Print the price after discount
```

**How the code works**

- `getDiscount` focuses on one job: calculate savings; the caller decides what to do next.
- Returning values makes functions easy to combine, like building blocks.

### What happens if you forget `return`?

```javascript
function add(a, b) { // Declare add with two number parameters
  const sum = a + b; // Calculate the sum but do not return it
} // End of add without a return statement

const value = add(2, 3); // Call add and capture whatever comes back
console.log(value); // Prints undefined because nothing was returned
```

**How the code works**

- The function still runs, but without `return` the caller receives `undefined`.

### Student activity: mark calculator

Write a function named `getPercentage` that:

1. Accepts `scored` and `total` as parameters.
2. Returns `(scored / total) * 100`.
3. Calls the function with `scored = 42` and `total = 50`.
4. Prints the returned percentage.

Expected output: `84`.

## Arrow functions

![Regular function like a full notebook page with several steps; arrow function like a short sticky note — both can produce the same result](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session18/session18-04-arrow-vs-regular-function.png?v=20260804)

Modern JavaScript often uses a shorter style called an **arrow function**.  
It is popular in browser code and many libraries.

- **Arrow function**  
  - *Official meaning:* A compact function syntax using `=>`, such as `const add = (a, b) => a + b;`.  
  - *In simple words:* A shorter way to write simple functions.  
  - *Real-life example:* Writing a quick sticky note instead of a full notebook page when the task is small.

### Complete example: arrow vs regular function

```javascript
function squareRegular(n) { // Regular function declaration named squareRegular
  return n * n; // Return the square of n
} // End of squareRegular

const squareArrow = (n) => { // Arrow function stored in squareArrow
  return n * n; // Return the square of n
}; // End of the arrow function body

const squareShort = (n) => n * n; // Short arrow form: expression after => is returned automatically

console.log(squareRegular(5)); // Print 25 using the regular function
console.log(squareArrow(5)); // Print 25 using the long arrow form
console.log(squareShort(5)); // Print 25 using the short arrow form
```

**How the code works**

- All three styles calculate the same result; `(n) => n * n` returns automatically.

### Student activity: convert to arrow style

Rewrite `function isEven(number) { return number % 2 === 0; }` as an arrow function stored in `const`, then test it:

```javascript
const isEven = (number) => number % 2 === 0; // Arrow function that returns true for even numbers
console.log(isEven(8)); // Print true
console.log(isEven(9)); // Print false
```

## Scope: where variables live

![College main-gate notice visible campus-wide as global scope; classroom whiteboard visible only inside that room as local or block scope](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session18/session18-05-scope-campus-gate-classroom.png?v=20260804)

Functions do not only run code—they also create boundaries for variables.  
Those boundaries are called **scope**.

- **Scope**  
  - *Official meaning:* The region of a program where a variable name is visible and usable.  
  - *In simple words:* Scope decides “who is allowed to see this variable.”  
  - *Real-life example:* A classroom whiteboard is visible in that room (local); a notice on the college gate is campus-wide (global).

Understanding scope prevents accidental overwriting of values and “variable is not defined” errors.

## Global scope

A variable declared outside any function or block is in **global scope**.  
That means many parts of your program can read it.

```javascript
const collegeName = "Open Learning Campus"; // Global constant available across this script

function showCollege() { // Declare a function that reads the global value
  console.log("College:", collegeName); // Print the global collegeName from inside the function
} // End of showCollege

showCollege(); // Call the function and print College: Open Learning Campus
console.log(collegeName); // Also print the same global value outside the function
```

**How the code works**

- `collegeName` is global, so both the function and outside code can access it.
- Prefer keeping most variables inside functions; use globals only for truly shared settings.

## Block scope with `let` and `const`

In modern JavaScript, `let` and `const` are **block scoped**.  
A **block** is code inside `{ ... }`, including `if` blocks, loops, and function bodies.

- **Block scope**  
  - *Official meaning:* A variable declared with `let` or `const` exists only inside the nearest `{ ... }` block.  
  - *In simple words:* The variable lives only inside that pair of curly braces.  
  - *Real-life example:* Notes on a sticky pad in one meeting are not available in another meeting room.

```javascript
function checkScore(score) { // Declare checkScore with one parameter
  if (score >= 40) { // Start a block that runs for passing scores
    const result = "Pass"; // result exists only inside this if block
    console.log(result); // Print Pass while still inside the block
  } else { // Start the failing-score block
    const result = "Fail"; // A separate result variable for this else block
    console.log(result); // Print Fail while still inside this block
  } // End of if/else

  // console.log(result); // Would cause an error because result is not visible here
} // End of checkScore

checkScore(55); // Call with 55 and print Pass
checkScore(22); // Call with 22 and print Fail
```

**How the code works**

- Each `const result` lives only inside its own block; outside those braces it is not available.
- This protects you from accidentally reusing the wrong value later.

## Function scope in practice

Every function creates its own local world for variables.  
Local variables do not leak outside unless you return them.

```javascript
function makeGreeting(userName) { // Declare makeGreeting with parameter userName
  const greeting = "Namaste, " + userName; // Local variable exists only inside this function
  return greeting; // Return the local greeting so the caller can use it
} // End of makeGreeting

const message = makeGreeting("Isha"); // Capture the returned greeting in message
console.log(message); // Print Namaste, Isha
// console.log(greeting); // Would fail: greeting is not visible outside the function
```

**How the code works**

- `greeting` is local to `makeGreeting`; returning shares the *value*, not the local variable.
- The caller stores that value in `message`, which has its own scope.

### Shadowing: same name, different places

You can reuse a variable name inside a function.  
That inner name temporarily “covers” the outer one. This is called **shadowing**.

```javascript
const title = "Outer Title"; // Global title for this script

function printTitle() { // Declare printTitle with no parameters
  const title = "Inner Title"; // Local title shadows the outer title inside this function
  console.log(title); // Print Inner Title because local scope wins here
} // End of printTitle

printTitle(); // Call the function and see the inner title
console.log(title); // Print Outer Title because we are back in global scope
```

**How the code works**

- Inside the function, local `title` is used; outside, global `title` is unchanged.
- Shadowing is legal, but clear names are usually safer for beginners.

## Scope practice: complete mini-programs

Now combine functions, returns, and scope in small programs you can run end to end.

### Mini-program 1: reusable tax helper

```javascript
function addTax(amount, taxPercent) { // Declare addTax with amount and tax percent
  const tax = (amount * taxPercent) / 100; // Calculate tax from the given percent
  const total = amount + tax; // Add tax to the original amount
  return total; // Return the final payable total
} // End of addTax

const bookTotal = addTax(500, 5); // Calculate total for a 500 rupee book with 5% tax
const bagTotal = addTax(1200, 12); // Calculate total for a 1200 rupee bag with 12% tax
console.log("Book payable:", bookTotal); // Print Book payable: 525
console.log("Bag payable:", bagTotal); // Print Bag payable: 1344
```

**How the code works**

- One function handles many products; local `tax` and `total` stay private inside `addTax`.
- Only the final number is returned to the caller.

### Mini-program 2: arrow function + array loop

```javascript
const scores = [70, 45, 88, 33]; // Create an array of student scores

const isPass = (score) => score >= 40; // Arrow function returns true when score is passing

for (let i = 0; i < scores.length; i++) { // Loop through each index in the scores array
  const score = scores[i]; // Read the current score into a block-scoped variable
  if (isPass(score)) { // Call the arrow function to check pass/fail
    console.log(score, "=> Pass"); // Print Pass for scores that meet the rule
  } else { // Runs when the score is below 40
    console.log(score, "=> Fail"); // Print Fail for low scores
  } // End of if/else
} // End of for loop
```

**How the code works**

- `isPass` is a reusable arrow rule; the loop walks the array; `score` stays block-scoped.

### Mini-program 3: expression function for formatting

```javascript
const formatCity = function (city, state) { // Function expression stored in formatCity
  const line = city + ", " + state; // Join city and state into one display string
  return line; // Return the formatted address line
}; // End of formatCity expression

function showTicket(passenger, city, state) { // Declaration that uses formatCity
  const place = formatCity(city, state); // Call another function and store its return value
  const ticket = passenger + " travelling to " + place; // Build the final ticket text
  return ticket; // Return the ticket message
} // End of showTicket

console.log(showTicket("Ananya", "Jaipur", "Rajasthan")); // Print Ananya travelling to Jaipur, Rajasthan
```

**How the code works**

- `formatCity` handles formatting; `showTicket` builds the message—splitting work makes testing easier.

### Student activity: shopping cart helper

Create one complete script with these requirements:

1. Write a function declaration named `lineTotal(price, qty)`.
2. Return `price * qty`.
3. Write an arrow function named `withDelivery` that adds `50` to any amount.
4. Calculate a shirt line total for price `499` and qty `2`.
5. Pass that total into `withDelivery` and print the final amount.

Expected final output: `1048`.

## Common mistakes (and how to avoid them)

These mistakes appear often when students move from Python-style thinking into JavaScript functions.

- **Parameters vs arguments:** parameters are placeholders in the definition; arguments are real values in the call.
- **Forgetting `return`:** if the console shows `undefined`, check whether the function returns a value.
- **Block-scope leaks:** a `const` declared inside an `if` block cannot be read after that block ends.
- **Too many globals:** globals cause accidental overwrites; prefer local variables and clear return values.

## Key Takeaways

- **Functions** let you write logic once and reuse it safely across your program.
- JavaScript supports **declarations**, **expressions**, and **arrow functions**—choose the style that keeps your code clear.
- **Parameters** receive inputs; **return** sends results back to the caller.
- **Scope** controls where variables are visible: global for shared values, block/function for local safety.
- Practice by writing small helpers (`calculate`, `format`, `check`) and combining them into mini-programs.

In the next session, you will continue building on these function skills as you work with more interactive browser behavior.  
Strong function and scope habits will make those features easier to organize and debug.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| `function name() { }` | Function declaration with a clear name |
| `const fn = function() { }` | Function expression stored in a variable |
| `(a, b) => a + b` | Arrow function that returns an expression |
| Parameter | Placeholder in the function definition |
| Argument | Actual value passed during a function call |
| `return` | Sends a value back to the caller |
| Default parameter | Fallback value when an argument is missing |
| Scope | Region where a variable name is visible |
| Global scope | Variable available across the script |
| Block scope | Variable limited to a `{ ... }` block (`let` / `const`) |
| Local variable | Variable that exists only inside a function |
| Shadowing | Inner variable with the same name as an outer one |
| `undefined` | Result when a function has no `return` value |
| `console.log(...)` | Print output while testing functions |
