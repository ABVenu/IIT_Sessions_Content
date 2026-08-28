# Masterclass: Algorithmic Thinking in JavaScript

## What You Will Learn in This Session

In the previous sessions you learned **variables**, **conditionals**, **loops**, **arrays**, **strings**, **objects**, and **functions**. You can now store data, repeat work, and wrap logic inside a reusable function.

That is enough syntax to *type* a program. This masterclass is about deciding *what* to type before you open **[One Compiler — JavaScript](https://onecompiler.com/javascript)**.

In this session, you will:

- Break a problem into **inputs**, **steps**, **outputs**, and **edge cases** before writing code
- Use an object as a **frequency counter** to tally items in one pass
- Use **two pointers** on an array (or string) instead of nested guessing
- Explain **O(1)**, **O(n)**, and **O(n²)** in plain language
- Follow a short **checklist** every time a new problem appears

By the end, you will plan a small JavaScript function on paper, choose a sensible pattern, and explain why one approach grows heavier as the data grows. Run every program and coding problem in this session at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)** — paste the code, click **Run**, and check the output.

---
## Why Pause Before You Type

You already know how to write a `for` loop and a function. The new skill is not another keyword. It is a way of thinking.

- **Official Definition:** An **algorithm** is a finite, clear sequence of steps that takes input and produces a correct output for a well-defined problem.
- **In Simple Words:** An algorithm is a recipe. Ingredients go in, steps are followed in order, and a dish comes out.
- **Real-Life Example:** Making chai is an algorithm: water, tea leaves, milk, sugar; boil; strain; serve. If you skip "strain," the output is wrong even if the ingredients were right.

**Algorithmic thinking** is the habit of writing that recipe *before* you light the stove.

- **Need:** Beginners often open [One Compiler](https://onecompiler.com/javascript) and start typing `let` immediately. The first idea that runs on 4 values often fails on empty lists, duplicates, or 4,000 values.
- **Logic:** A short paper plan saves a long evening of random `console.log` debugging.
- **Common doubt:** *"If I already know loops, why do I need a plan?"* A loop is a tool. The plan tells you *which* tool, *how many* passes, and *what* to do when the list is empty.

Imagine the exam cell at **Patna City College**. The clerk is asked: "How many students passed?" If the clerk ticks names without knowing the pass mark or what to do with absentees, the count will be messy. Programmers make the same mistake when they code before they name the rules.

---
## Break the Problem into Four Boxes

Every programming problem can be split into four boxes. If you skip a box, bugs hide there.

- **Official Definition:** **Problem decomposition** is the process of breaking a large problem into smaller, named parts that can be solved one at a time.
- **In Simple Words:** You do not swallow a thali in one bite. You separate dal, rice, sabzi, and roti, then eat with a plan.
- **Real-Life Example:** Booking an IRCTC ticket is not one blurry action. You choose date, train, class, passenger names, and payment. Each part has its own rules.

![Four boxes before coding — INPUT marks array, STEPS numbered plan, OUTPUT pass count 3, and EDGE CASES such as empty list and exact pass mark 40 on a student notebook at an exam cell desk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc1/sessionmc1-01-four-boxes-plan-before-code.png)

### Inputs

**Input** is the data the program *receives*. Write the type, an example, and extra rules.

For "How many students passed?":

- Type: an **array of numbers** (marks)
- Example: `[35, 67, 40, 88, 12]`
- Extra rule: pass mark is `40` (inclusive)

If you do not name the input, you might write a program that expects one number, while the teacher gives a whole list.

### Output

**Output** is what the program *must return or print*. Write the type and one expected answer.

- Type: a **number** (how many students passed)
- Example output for `[35, 67, 40, 88, 12]`: **3** (67, 40, and 88 are 40 or more)

Clear output prevents a common error: printing `"pass"` `"fail"` `"pass"` when the question asked for a **count**.

### Steps

**Steps** are the algorithm in plain English, not in JavaScript yet.

1. Start a counter at `0`
2. Look at each mark in the list, one by one
3. If the mark is greater than or equal to `40`, add `1` to the counter
4. After the last mark, the counter is the answer

These steps already tell you the pattern: **one loop**, one `if`, one running total. You do not need nested loops here.

### Edge Cases

- **Official Definition:** An **edge case** is an input at the boundary of the rules — empty data, exact limits, duplicates, or unusual but valid values.
- **In Simple Words:** Edge cases are the "what if?" questions that break a lazy program.
- **Real-Life Example:** A shop bill that works for 3 items may fail when the cart is **empty**, or when quantity is **0**.

Write these on paper *before* coding:

| Edge case | Example input | Sensible output | Why it matters |
|---|---|---|---|
| Empty list | `[]` | `0` | No student appeared |
| All failed | `[10, 20, 39]` | `0` | Counter must stay 0 |
| Exact pass mark | `[40]` | `1` | Use `>= 40`, not `> 40` |
| Single fail | `[22]` | `0` | Loop must work for length 1 |

**Common error:** Using `>` instead of `>=`. The student who scored exactly 40 is then counted as fail, which is wrong.

### Activity: Four Boxes on Paper

A hostel warden asks: **"What is the highest attendance count in this list?"** Sample: `[18, 22, 19, 22, 15]`

In your notebook write: **input** (type + example), **output** (the number you expect), **steps** in 4–6 plain English lines, and **two edge cases**.

Do not write JavaScript yet. The point is the four boxes. After the plan is ready, solve it at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

**Suggested answers:** Input is an array of numbers. Output is `22`. Steps: store the first value as highest so far, walk the rest, replace when you see a larger number. Edge cases: `[]`, and `[7, 7, 7]` (highest is `7`).

---
## From Paper Plan to a Small Function

The four boxes are useless if they stay in the notebook. Turn the steps into a **function** — the skill you practised in the previous session.

Open **[One Compiler — JavaScript](https://onecompiler.com/javascript)**, paste the program, and click **Run**.

```javascript
function countPassed(marks) {              // Define a function that receives an array of marks
  let passed = 0;                          // Start the pass counter at zero
  for (let i = 0; i < marks.length; i++) { // Walk every index from 0 to the last item
    if (marks[i] >= 40) {                  // Check if this mark meets the pass rule
      passed = passed + 1;                 // Increase the counter by one
    }                                      // End of the if block
  }                                        // End of the loop
  return passed;                           // Send the final count back to the caller
}                                          // End of the function

let examMarks = [35, 67, 40, 88, 12];      // Sample marks from one subject
let result = countPassed(examMarks);       // Call the function and store the returned number
console.log(result);                       // Print 3 because 67, 40, and 88 passed
console.log(countPassed([]));              // Print 0 for an empty list
console.log(countPassed([40]));            // Print 1 because 40 is a pass
console.log(countPassed([10, 20, 39]));    // Print 0 because nobody reached 40
```

**How the code works:**

- `passed` is a **running total**, like a clicker at a college gate
- The `for` loop visits each mark **once** — one pass over the list
- `>= 40` includes the exact pass mark; `return` sends the number out; extra logs **test** the happy path and edge cases

**Common doubt:** *"Can I `console.log` inside the function instead of `return`?"* You can print, but other code cannot reuse the number. Functions that **return** a value are easier to test.

Notice the order: boxes first, then code, then tests. That order is the whole masterclass in one example.

---
## Frequency-Counter Intuition Using Objects

Some problems look like they need two nested loops. They often need **one pass** and an **object used as a tally**.

- **Official Definition:** A **frequency counter** is a pattern that records how many times each distinct value appears, usually in an object, in a single pass over the data.
- **In Simple Words:** It is a tally chart. Each unique item gets a box. Every time you see that item, you add a stick in that box.
- **Real-Life Example:** The canteen at Patna City College sells tea, samosa, and idli. At closing time, the cashier does not compare every token with every other token. The cashier keeps a board: tea | samosa | idli, and adds a mark for each order.

You already know how to **create an object**, **read a property**, and **update a property**. That is the tally board.

![Canteen frequency counter — one-pass order tokens become a tally board with tea 3, samosa 2, and idli 1 instead of comparing every token with every other token](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc1/sessionmc1-02-frequency-counter-tally.png)

**Need:** "Which item was ordered most?" or "Does any name repeat?" Nested comparisons grow like n times n. A tally object grows like one walk through the list.

**Logic:** One loop reads each item. The object remembers counts. After the loop, you read the object.

**Common error:** Forgetting to start a count at `1` when the key is new. If `freq.tea` is `undefined` and you write `freq.tea + 1`, JavaScript gives `NaN`, and the tally breaks.

### Trace on a Tiny List

Orders: `["tea", "samosa", "tea", "idli", "samosa", "tea"]`

| Step | Item seen | Object after this step |
|---|---|---|
| Start | — | `{}` |
| 1 | tea | `{ tea: 1 }` |
| 3 | tea again | `{ tea: 2, samosa: 1 }` |
| 6 | last tea | `{ tea: 3, samosa: 2, idli: 1 }` |

Tea was ordered **3** times. You never needed a nested loop. Steps 2, 4, and 5 add samosa, then idli, then samosa again — the object grows one key or one count at a time.

### Full Code: Canteen Tally — paste into [One Compiler](https://onecompiler.com/javascript) and click **Run**

```javascript
function countOrders(orders) {                    // Define a function that receives an array of item names
  let freq = {};                                  // Start with an empty object that will hold counts
  for (let i = 0; i < orders.length; i++) {       // Visit every order from start to end
    let item = orders[i];                         // Store the current item name in a short variable
    if (freq[item] === undefined) {               // Check if this item has no box yet on the tally
      freq[item] = 1;                             // Create the box and put the first mark
    } else {                                      // The item already has a box
      freq[item] = freq[item] + 1;                // Add one more mark to the existing count
    }                                             // End of the if / else
  }                                               // End of the loop
  return freq;                                    // Return the finished tally object
}                                                 // End of the function

let canteen = ["tea", "samosa", "tea", "idli", "samosa", "tea"]; // Sample orders
let tally = countOrders(canteen);                 // Build the frequency object
console.log(tally);                               // Print { tea: 3, samosa: 2, idli: 1 }
console.log(tally.tea);                           // Print 3 — direct read of one count
console.log(countOrders([]));                     // Print {} — empty list means empty tally
```

**How the code works:**

- `freq` is a normal JavaScript **object**. Keys are item names. Values are numbers
- `freq[item]` uses **bracket notation** so the key can be whatever string is inside `item`
- The `if` handles the first time you see an item; the `else` handles repeats
- After one loop, `tally.tea` does not scan the list again; empty input returns `{}`

The same tally idea checks **anagrams** (`"listen"` and `"silent"`): if lengths differ, answer is no; count letters of the first word; spend those counts on the second word. Two loops **one after another** still walk the data about **n** times, not n times n. Try both words at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

### Activity: Build a Tally by Hand

Word: `"MASAI"`. Draw `{}` in your notebook. After each letter, rewrite the object.

Which letter has the highest count? **A** appears twice. The others appear once. Confirm by calling `countOrders(["M", "A", "S", "A", "I"])` at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

---
## Two-Pointer Intuition on Arrays

Frequency counting used **one finger** moving left to right. Some array problems are easier with **two fingers**.

- **Official Definition:** The **two-pointer technique** uses two indices that move through a sequence according to a rule, often from the ends toward the centre.
- **In Simple Words:** Put one finger on the start and one finger on the end. Move them by a rule until they meet.
- **Real-Life Example:** Checking whether a row of lockers is symmetric: look at the first and last, then the second and second-last. You do not compare every locker with every other locker.

**Need:** Palindromes, and "two numbers that add up to a target" on a **sorted** list. Nested loops can solve these, but they do extra work.

**Logic:** Each pointer visits items a small number of times. Total work stays close to one pass.

**Common error:** Using the pair-sum rule on a **jumbled** list. The "move left or right" rule is honest only when the array is already in order.

![Two pointers on a sorted price row and the word NITIN — left and right fingers move inward for palindrome checks or toward a target pair sum such as 10 plus 60 equals 70](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc1/sessionmc1-03-two-pointers-array.png)

### Palindrome Check

- **Official Definition:** A **palindrome** reads the same forwards and backwards.
- **In Simple Words:** The word looks unchanged if you reverse it.
- **Real-Life Example:** Words such as **NITIN**, **LEVEL**, and **MALAYALAM**. You still check characters from both ends.

Trace `"NITIN"`:

| Left index | Right index | Left char | Right char | Match? |
|---|---|---|---|---|
| 0 | 4 | N | N | Yes — move both inward |
| 1 | 3 | I | I | Yes — move both inward |
| 2 | 2 | T | T | Fingers meet — done |

If any pair mismatches, stop early. The word is not a palindrome. Paste the program below into **[One Compiler — JavaScript](https://onecompiler.com/javascript)** and click **Run**.

```javascript
function isPalindrome(text) {                     // Define a function that receives a string
  let left = 0;                                   // Left finger starts at the first character
  let right = text.length - 1;                    // Right finger starts at the last character
  while (left < right) {                          // Keep going until the fingers meet or cross
    if (text[left] !== text[right]) {             // Compare the two characters
      return false;                               // One mismatch is enough to say no
    }                                             // End of mismatch check
    left = left + 1;                              // Move the left finger one step right
    right = right - 1;                            // Move the right finger one step left
  }                                               // End of the while loop
  return true;                                    // All pairs matched
}                                                 // End of the function

console.log(isPalindrome("NITIN"));               // Print true
console.log(isPalindrome("PATNA"));               // Print false — P and A differ
console.log(isPalindrome("A"));                   // Print true — a single character
console.log(isPalindrome(""));                    // Print true — empty string has no mismatch; length 0 never enters the loop
```

**How the code works:** `left` and `right` are **indices**. The loop stops when they meet, so the middle character is not compared with itself. Length 0 and 1 never enter the loop, so they return `true`.

**Common doubt:** *"Should I reverse the string and compare?"* Reversing also works, but it often builds a new string. Two pointers can answer with two number variables and the original text.

### Pair Sum on a Sorted Array

Problem: In a **sorted** list of prices, do two **different** items add up to a target budget?

Example: `[10, 20, 35, 50, 60]`, target `70`. Yes — `10 + 60` and `20 + 50`. There is **no** pair for `90`.

Because the list is increasing:

- If the sum is **too small**, move `left` one step right
- If the sum is **too big**, move `right` one step left
- If it **matches**, you found a pair

This rule is valid **only when the array is already sorted**. If a question gives a jumbled list, do not blindly apply this pointer rule. Run the program at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

```javascript
function hasPairSum(sortedPrices, target) {       // Define a function for a sorted array and a target
  let left = 0;                                   // Left finger on the cheapest item
  let right = sortedPrices.length - 1;            // Right finger on the costliest item
  while (left < right) {                          // Two different items, so fingers must not sit on one index
    let sum = sortedPrices[left] + sortedPrices[right]; // Add the two current prices
    if (sum === target) {                         // Exact match
      return true;                                // A valid pair exists
    } else if (sum < target) {                    // Sum is too small
      left = left + 1;                            // Move toward larger values
    } else {                                      // Sum is too large
      right = right - 1;                          // Move toward smaller values
    }                                             // End of if / else if / else
  }                                               // End of the while loop
  return false;                                   // Fingers met with no matching pair
}                                                 // End of the function

let prices = [10, 20, 35, 50, 60];                // Already in increasing order
console.log(hasPairSum(prices, 70));              // Print true — 10 + 60
console.log(hasPairSum(prices, 90));              // Print false — no pair adds to 90
console.log(hasPairSum([], 10));                  // Print false — not enough items
console.log(hasPairSum([40], 40));                // Print false — need two different indices
```

**How the code works:** `left < right` guarantees two **different** positions. Each step moves **exactly one** finger. Empty and single-item arrays never enter the loop, so they return `false`.

### Activity: Move the Fingers

Sorted list: `[5, 8, 12, 20]`. Target: `25`. Write the sum at each step until you can say true or false. Then check with `hasPairSum` at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

**Suggested trace:** `5 + 20 = 25` — match on the first check, so **true**. Now try target `13`: `5 + 20 = 25` (too big, move right left) → `5 + 12 = 17` (too big) → `5 + 8 = 13` (**true**). Target `11` runs out of pairs (**false**).

---
## O(1), O(n), and O(n²) in Plain Words

You now have more than one way to solve some problems. You need a language to compare those ways *without* running them on one lakh rows. That language is **Big-O**, used here only as plain intuition.

- **Official Definition:** **Time complexity** describes how the number of operations grows as the input size **n** grows. **Big-O notation** names the dominant growth shape.
- **In Simple Words:** Big-O answers, "If the list becomes 10 times longer, does the work stay almost the same, grow in a straight line, or explode?"
- **Real-Life Example:** Checking one labelled locker is quick even in a huge hostel. Checking every locker grows with hostel size. Comparing every student with every other student grows much faster than that.

**n** is "how many items?" For an array, `n` is usually `array.length`.

**Common doubt:** *"Does O(n²) mean exactly n times n comparisons?"* No. It means the work **grows like a square**. `n × (n - 1) / 2` pair checks still sit in the **O(n²)** family.

![Big-O growth in plain words — O(1) stays flat like one labelled locker, O(n) rises in a straight line like checking a register once, and O(n squared) explodes like every student shaking hands with every other student](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc1/sessionmc1-04-big-o-growth.png)

### O(1) — Work Stays Almost the Same

- **Official Definition:** **O(1)** (constant time) means the number of steps does not grow with n.
- **In Simple Words:** Looking at one labelled box. The hostel can add 500 rooms; that one locker still takes one look.
- **Real-Life Example:** Opening your own named tiffin box in a rack. You do not inspect every box.

At this level, treat these as O(1): reading `marks[0]` when you know the index, reading `tally.tea` after the tally exists, and a few arithmetic steps that do not loop. Run the snippet at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

```javascript
function firstMark(marks) {                       // Define a function that receives an array
  return marks[0];                                // Read the value at index 0 and return it
}                                                 // End of the function

console.log(firstMark([80, 70, 90]));             // Print 80
```

**How the code works:** One index read happens whether the array has 3 items or 3,000. "What is the first mark?" is O(1), while "Is 90 anywhere?" is not O(1) if you must search. If the array is empty, `marks[0]` is `undefined` — O(1) is about step count, not safety.

### O(n) — Work Grows in a Straight Line

- **Official Definition:** **O(n)** (linear time) means the work grows in proportion to n.
- **In Simple Words:** If the list doubles, you roughly double the number of looks.
- **Real-Life Example:** The warden checking every student in a register, one name at a time.

Your `countPassed`, `countOrders`, `isPalindrome`, and `hasPairSum` functions are in this family. Each visits items about once.

5 marks need about 5 looks, and 5,000 marks need about 5,000 looks. Extra `if` checks inside the loop do **not** change the family. Two loops **one after another** are still O(n), because walking twice is `2n` and Big-O still calls that **O(n)**.

### O(n²) — Work Grows Like n Times n

- **Official Definition:** **O(n²)** (quadratic time) means the work grows in proportion to n multiplied by n.
- **In Simple Words:** For every item, you almost walk the whole list again.
- **Real-Life Example:** In a class of 30, every student shakes hands with every other student. In a class of 300, that counting becomes painful.

The usual coding shape is a loop **inside** another loop over the same list. Paste this into **[One Compiler — JavaScript](https://onecompiler.com/javascript)** and click **Run**.

```javascript
function hasDuplicateSlow(names) {                // Define a function that looks for a repeated name
  for (let i = 0; i < names.length; i++) {        // Pick each name as the "outer" name
    for (let j = i + 1; j < names.length; j++) {  // Compare it with every name after it
      if (names[i] === names[j]) {                // If two different positions hold the same text
        return true;                              // A duplicate exists
      }                                           // End of match check
    }                                             // End of inner loop
  }                                               // End of outer loop
  return false;                                   // No pair matched
}                                                 // End of the function

console.log(hasDuplicateSlow(["Riya", "Aman", "Riya"])); // Print true
console.log(hasDuplicateSlow(["Riya", "Aman", "Neha"])); // Print false
```

**How the code works:** For n = 3, the inner loop may run 3 comparisons; for n = 100, about 100 × 99 / 2. The result can be correct; the issue is **growth**. **Common error:** nesting loops "to be sure" when one pass plus an object would do.

| Family | Growth in simple words | Everyday picture | Typical code shape |
|---|---|---|---|
| **O(1)** | Stays almost the same as n grows | Opening one labelled locker | Direct index or one object key |
| **O(n)** | Grows in a straight line with n | Checking every name in a register once | One loop (or two loops in a row) |
| **O(n²)** | Grows like n times n | Every student compared with every other student | Loop inside a loop on the same list |

Big-O hides laptop speed and tiny extras such as `console.log`. For n = 5, an O(n²) method can still feel instant. The label matters when n becomes large.

---
## Same Problem, Two Speeds

Big-O is most useful when two methods solve **the same problem**. `hasDuplicateSlow` is the nested plan. Here is the frequency plan — run it at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**.

```javascript
function hasDuplicateFast(names) {                // Define a function that uses a tally object
  let seen = {};                                  // Object that remembers names we have already met
  for (let i = 0; i < names.length; i++) {        // Walk the list once
    let name = names[i];                          // Current name
    if (seen[name] === true) {                    // If this name is already in the tally
      return true;                                // Duplicate found
    }                                             // End of duplicate check
    seen[name] = true;                            // Mark this name as seen
  }                                               // End of the loop
  return false;                                   // Finished the list with all unique names
}                                                 // End of the function

console.log(hasDuplicateFast(["Riya", "Aman", "Riya"])); // Print true
console.log(hasDuplicateFast(["Riya", "Aman", "Neha"])); // Print false
console.log(hasDuplicateFast([]));                // Print false — nothing to duplicate
```

**How the code works:** Each name is processed once (**O(n)**). The object uses extra space for unique names. The first `"Riya"` is stored; the second returns `true` immediately.

Both functions can be correct. For 10 names you may not feel the difference. For 10,000 attendance rows, the nested plan does a huge number of pair checks; the frequency plan still does one pass.

This is why patterns matter. A frequency counter is not clever syntax. It is a way to stay in **O(n)** when a nested scan would be **O(n²)**.

### Activity: Name the Family

For each situation, write **O(1)**, **O(n)**, or **O(n²)** in your notebook.

1. Print the last item using `arr[arr.length - 1]`
2. Sum all marks with one `for` loop
3. For every student, loop through all students to find a namesake
4. Build a canteen tally with one loop, then read `tally.tea`
5. Check a palindrome with two pointers on a string of length n

**Suggested answers:** 1) O(1)  2) O(n)  3) O(n²)  4) building the tally is O(n); reading `tally.tea` after that is O(1)  5) O(n)

---
## A Short Checklist Before You Code

You now have four thinking tools: decomposition, frequency counting, two pointers, and Big-O labels. Tie them with a checklist you can reuse on every new problem.

- **Official Definition:** A **problem-solving checklist** is a short, repeatable sequence of questions a programmer answers before writing code.
- **In Simple Words:** It is a pre-flight list, like a pilot checking fuel and flaps before take-off.
- **Real-Life Example:** Before a lab exam, you do not start wiring randomly. You read the question, list given values, write the expected output, and only then connect wires.

Use this list in order:

1. **Restate the problem** in one sentence, in your own words
2. **Inputs** — type, example, and extra rules (pass mark, sorted or not)
3. **Output** — type and one expected value for your example
4. **Edge cases** — empty, length 1, duplicates, exact boundary values
5. **Dry run** — trace a tiny example on paper
6. **Pattern guess** — one loop, frequency object, two pointers, or nested loops
7. **Growth in plain words** — will this stay kind if n becomes 10,000?
8. **Then code** a function, and run the example plus two edge cases

**Need:** Without the list, people jump from "I think I need a loop" to 40 messy lines.

**Common error:** Choosing two pointers on an unsorted pair-sum question, or nested loops for a simple count. The pattern must match the **rules** you wrote in step 2.

### Worked Checklist: Attendance Duplicates

**Problem:** "Does this attendance array contain any repeated name?"

| Step | What you write |
|---|---|
| Restate | Return true if any name appears more than once |
| Input | Array of strings, e.g. `["Riya", "Aman", "Riya"]` |
| Output | Boolean; example should be `true` |
| Edge cases | `[]` → false; one name → false; two same at ends → true |
| Dry run | First `"Riya"` unseen; `"Aman"` unseen; second `"Riya"` seen → true |
| Pattern | Frequency object (`seen`) in one pass |
| Growth | O(n) time. Nested pairs would be O(n²) |
| Code | Use `hasDuplicateFast`, then test the edge cases |

If you cannot fill the table, you are not ready to type. Fill the table first.

### Activity: Run the Checklist Once

Problem: **"Return the number of vowels in a lowercase word."** Sample: `"patna"` (answer: **2**, letters `a` and `a`).

Fill all eight checklist rows in your notebook. Then solve the problem at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)** — write the function, click **Run**, and test `"patna"` and `""`.

**Hint:** Input is a string. Output is a number. `""` → `0`. A simple O(n) loop that checks `a e i o u` is enough. You do not need two pointers for this one.

---
## Key Takeaways

- **Algorithmic thinking** means writing inputs, steps, outputs, and edge cases before you type JavaScript. A function is the last step, not the first.
- A **frequency-counter** object tallies items in one pass. Use it for "how many times?" and for many duplicate checks.
- **Two pointers** use two indices that move by a rule. Palindromes and pair-sum on a **sorted** array are the beginner pictures. Do not apply the pair-sum rule on a jumbled list.
- **O(1)**, **O(n)**, and **O(n²)** are growth labels, not exam marks. Direct access stays flat, one loop grows in a line, nested loops over the same list grow like a square.
- Use the **eight-step checklist** on every new problem, then code and test at **[https://onecompiler.com/javascript](https://onecompiler.com/javascript)**. Later you will search, sort, and attach JavaScript to web pages. The same checklist still applies: name the data, pick a pattern, estimate growth, then code.

---
## Important Commands, Libraries, Terminologies used

| Term / syntax | Meaning in this session | Quick picture |
|---|---|---|
| **Algorithm** | Clear finite steps from input to output | A chai recipe |
| **Problem decomposition** | Split into inputs, steps, outputs, edge cases | Separating a thali |
| **Input / Output** | Data in; value returned or printed | Marks array → count `3` |
| **Edge case** | Boundary input that often breaks lazy code | `[]`, exact mark `40` |
| **Frequency counter** | Object that stores counts of each distinct value | Canteen tally board |
| **Bracket notation** `freq[item]` | Read or write a property whose name is in a variable | Opening a named locker |
| **Two pointers** | Two indices moving by a rule | Fingers on first and last locker |
| **Palindrome / pair sum** | Same forwards and back; two sorted items that add to a target | `NITIN`; `10 + 60 = 70` |
| **n / Big-O** | Input size; name of the growth shape | `array.length`; not exact seconds |
| **O(1) / O(n) / O(n²)** | Flat / straight line / n times n | `marks[0]` / one loop / nested loops |
| `===` / `!==` / `undefined` | Strict equal; missing property or index | Same type; empty locker |
| `return` | Send a value out of a function | Handing the count to the clerk |
| **[One Compiler — JavaScript](https://onecompiler.com/javascript)** | Online editor to run every program in this session | Paste code, click **Run** |
