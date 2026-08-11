# DOM Basics & Event Handling

In the previous session, you learned **JavaScript functions**: declarations, expressions, parameters, return values, arrow functions, and scope.  
Those skills let you package logic into reusable pieces.  
In this session, you will connect that JavaScript to the **webpage itself**—selecting elements, reading and changing content, and responding when the user clicks or types.

The browser keeps a live model of the page called the **DOM**, and your functions can talk to that model.

## What you will learn in this session

- What the **DOM** is and how the **`document`** object represents the page
- How to select elements with **`getElementById`**, **`querySelector`**, and **`querySelectorAll`**
- How to **traverse** the DOM tree and read element content
- How to handle user actions with **`addEventListener`** for **click**, **input**, and **submit**
- How to **create, modify, and remove** elements and do basic **form validation**

## Why the DOM matters

Until now, much of your JavaScript printed results in the console.  
Real websites update what you see on the page: buttons change text, forms show errors, and lists grow when you add items.  
The **DOM** is the bridge between your JavaScript and the visible HTML.

![Railway station display board with one train slot being updated live — the DOM is the browser’s live map of the page that JavaScript can change without rebuilding the whole site](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session19/session19-01-dom-railway-display-board.png?v=20260811)

- **DOM (Document Object Model)**  
  - *Official meaning:* The **DOM** is a tree-like representation of an HTML document that browsers expose so programs can read and change the page.  
  - *In simple words:* The DOM is the browser’s live map of every tag on the page.  
  - *Real-life example:* Think of a railway station display board. The board (page) shows trains; staff update slots on the board (DOM changes) without rebuilding the whole station.

- **Why you need it**  
  - Without the DOM, JavaScript cannot change headings, buttons, or form messages on the page.
  - Common doubt: “Is the DOM the same as the HTML file?” The HTML file is the starting recipe; the DOM is the live dish the browser is serving right now.

## The document object

Every webpage has a special object named **`document`**—your main door into the DOM.  
Almost every selection and update starts from it.

- **`document`**  
  - *Official meaning:* The **`document`** object represents the whole HTML page loaded in the browser window.  
  - *In simple words:* `document` is the manager of the page—ask it to find an element and it points you to the right shelf.  
  - *Real-life example:* In a supermarket, `document` is the store map and the staff desk.

### Tiny check in the console

Open any webpage, open DevTools Console, and try:

```javascript
console.log(document); // Print the full document object for the current page
console.log(document.title); // Print the text shown in the browser tab title
console.log(document.body); // Print the body element that holds visible page content
```

**How the code works**

- `document` is provided by the browser; `title` and `body` read parts of the live page.

## Selecting one element: getElementById

Pages often give important elements a unique **`id`**.  
**`getElementById`** finds that one element quickly.  
Use it when you already know the exact id.

![College gate ID check — one student’s unique ID card number is matched directly, like getElementById finding one element by its id](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session19/session19-02-getElementById-college-id.png?v=20260811)

- **`getElementById`**  
  - *Official meaning:* A `document` method that returns the element whose `id` attribute matches the given string, or `null` if none exists.  
  - *In simple words:* You call someone by their unique roll number.  
  - *Real-life example:* In a college ID check, each student has one unique ID card number—no two share the same number.

### Complete HTML + JS example

```html
<!DOCTYPE html> <!-- Tell the browser this is an HTML5 document -->
<html lang="en"> <!-- Start the HTML root and set language to English -->
  <head> <!-- Start the head section for page metadata -->
    <meta charset="UTF-8" /> <!-- Set character encoding so text displays correctly -->
    <title>DOM Select Demo</title> <!-- Set the browser tab title -->
  </head> <!-- End the head section -->
  <body> <!-- Start the visible page body -->
    <h1 id="main-heading">Welcome</h1> <!-- Heading with a unique id for selection -->
    <p id="status">Waiting...</p> <!-- Paragraph that JavaScript will update -->
    <script> // Start an inline script so JS runs with this page
      const heading = document.getElementById("main-heading"); // Find the h1 by its id
      const status = document.getElementById("status"); // Find the paragraph by its id
      console.log(heading.textContent); // Read and print the heading text
      status.textContent = "Page loaded"; // Replace the paragraph text with a new message
    </script> <!-- End the script block -->
  </body> <!-- End the body -->
</html> <!-- End the HTML document -->
```

**How the code works**

- `getElementById("main-heading")` returns the `h1` element object.
- `textContent` reads or writes the plain text inside an element.
- If the id is wrong, the method returns `null`—always double-check spelling.

### Student activity: select by id

Create a small HTML file with one `h1` that has `id="greet"` and text `Hello`.

1. Use `getElementById("greet")` to select it.
2. Print its `textContent` in the console.
3. Change `textContent` to `Hello, DOM!`.

Expected page result: the heading shows `Hello, DOM!`.

## Selecting with querySelector and querySelectorAll

Ids are not always enough.  
Sometimes you select by **tag**, **class**, or a CSS-style path.  
**`querySelector`** and **`querySelectorAll`** use CSS selector syntax for that.

![Supermarket aisle — the shopkeeper points to the first matching shelf for querySelector, while many identical shelves behind represent querySelectorAll](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session19/session19-03-querySelector-supermarket-aisle.png?v=20260811)

- **`querySelector`**  
  - *Official meaning:* Returns the **first** element that matches a CSS selector string, or `null` if none match.  
  - *In simple words:* Find the first matching item on the page.  
  - *Real-life example:* In a queue at a ticket window, you pick the first person wearing a red cap.

- **`querySelectorAll`**  
  - *Official meaning:* Returns a **NodeList** of **all** elements that match a CSS selector.  
  - *In simple words:* Collect every matching item, not just the first.  
  - *Real-life example:* Listing every shop in a mall that sells mobile phones.

- **CSS selector reminders for beginners**  
  - `"h2"` → first or all `h2` tags  
  - `".card"` → elements with `class="card"`  
  - `"#price"` → element with `id="price"`  
  - `"form input"` → `input` elements inside a `form`

### Complete example: one vs many

```html
<!DOCTYPE html> <!-- Declare HTML5 document type -->
<html lang="en"> <!-- Open html root with English language -->
  <head> <!-- Open head for metadata -->
    <meta charset="UTF-8" /> <!-- Set UTF-8 encoding -->
    <title>Query Selector Demo</title> <!-- Set tab title -->
  </head> <!-- Close head -->
  <body> <!-- Open body for page content -->
    <p class="note">First note</p> <!-- First paragraph with class note -->
    <p class="note">Second note</p> <!-- Second paragraph with class note -->
    <p class="note">Third note</p> <!-- Third paragraph with class note -->
    <script> // Begin JavaScript
      const firstNote = document.querySelector(".note"); // Select only the first .note element
      const allNotes = document.querySelectorAll(".note"); // Select every .note element as a NodeList
      console.log(firstNote.textContent); // Print text of the first match: First note
      console.log(allNotes.length); // Print how many matches were found: 3
      allNotes.forEach(function (item) { // Loop through each matched paragraph
        item.style.color = "blue"; // Change text color of this paragraph to blue
      }); // End the forEach callback
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- `querySelector(".note")` stops at the first match.
- `querySelectorAll(".note")` gives a list you can loop with `forEach`.
- Common doubt: `querySelectorAll` is not a normal array, but `forEach` works on it in modern browsers.

### Student activity: first vs all

Add three `li` items inside a `ul`, each with class `task`.

1. Use `querySelector(".task")` and log its text.
2. Use `querySelectorAll(".task")` and log the length.
3. Change only the first task’s text to `Done`.

Expected console length: `3`. Expected first item text on page: `Done`.

## Reading content and traversing the DOM tree

Selecting one element is step one.  
Next, you often move to **parents**, **children**, or **siblings**, and you read what is inside an element.  
This is called **DOM traversal**.

- **DOM tree**  
  - *Official meaning:* The hierarchical structure of nodes where elements nest inside other elements.  
  - *In simple words:* Tags sit inside tags, like folders inside folders.  
  - *Real-life example:* A family tree: grandparents → parents → children.

- Useful reading properties  
  - **`textContent`** — plain text inside the element (ignores HTML tags as markup)  
  - **`innerHTML`** — text plus HTML markup inside the element  
  - **`value`** — current value of form controls like `input` and `textarea`

- Useful traversal properties  
  - **`parentElement`** — the element one level up  
  - **`children`** — live list of child elements  
  - **`firstElementChild` / `lastElementChild`** — first or last child element  
  - **`nextElementSibling` / `previousElementSibling`** — neighboring elements at the same level

### Complete example: read and walk the tree

```html
<!DOCTYPE html> <!-- HTML5 document declaration -->
<html lang="en"> <!-- Root html element -->
  <head> <!-- Metadata section -->
    <meta charset="UTF-8" /> <!-- Character encoding -->
    <title>Traversal Demo</title> <!-- Tab title -->
  </head> <!-- End head -->
  <body> <!-- Visible content -->
    <div id="box"> <!-- Parent container with id box -->
      <h2>Tasks</h2> <!-- First child: heading -->
      <ul id="list"> <!-- Second child: unordered list -->
        <li>Buy milk</li> <!-- First list item -->
        <li>Pay bill</li> <!-- Second list item -->
      </ul> <!-- End list -->
    </div> <!-- End box -->
    <script> // Start script
      const box = document.getElementById("box"); // Select the parent div
      const list = document.getElementById("list"); // Select the ul by id
      console.log(box.children.length); // Print number of direct children of box (2: h2 and ul)
      console.log(list.firstElementChild.textContent); // Print text of first li: Buy milk
      console.log(list.lastElementChild.textContent); // Print text of last li: Pay bill
      console.log(list.parentElement.id); // Print id of the parent of list: box
      const second = list.firstElementChild.nextElementSibling; // Move from first li to next sibling
      console.log(second.textContent); // Print Pay bill
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- `children` looks only one level down; it does not flatten the whole page.
- Sibling properties move sideways; parent properties move up.
- Prefer `textContent` for plain text updates; use `innerHTML` only when you intentionally need HTML tags.

### Student activity: sibling walk

Make a `ul` with three `li` items: `A`, `B`, and `C`.

1. Select the first `li`.
2. Use `nextElementSibling` twice to reach `C`.
3. Log `C`’s `textContent` and then set it to `Completed`.

Expected final third item text: `Completed`.

## Event handling with addEventListener

Selecting and reading is useful, but pages become interactive when they **react to the user**.  
An **event** is something that happens: a click, a key press, a form submit.  
You attach a function that runs when that event occurs.

![Guest presses a doorbell and someone inside opens the door — addEventListener waits for an event and then runs your function](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session19/session19-04-event-handling-doorbell.png?v=20260811)

- **Event**  
  - *Official meaning:* A signal from the browser that something happened in the document or on an element.  
  - *In simple words:* A notification that the user did something.  
  - *Real-life example:* A doorbell ringing when a guest arrives—you decide what to do when you hear it.

- **`addEventListener`**  
  - *Official meaning:* A method that registers a function to run when a named event occurs on an element.  
  - *In simple words:* “When this happens, run this function.”  
  - *Real-life example:* Setting a reminder: when the train arrives (event), send a message (listener function).

- Common events in this session  
  - **`click`** — user clicks an element  
  - **`input`** — user types or changes a field’s value  
  - **`submit`** — user submits a form

### Complete example: click event

```html
<!DOCTYPE html> <!-- HTML5 declaration -->
<html lang="en"> <!-- Root element -->
  <head> <!-- Head section -->
    <meta charset="UTF-8" /> <!-- Encoding -->
    <title>Click Demo</title> <!-- Title -->
  </head> <!-- End head -->
  <body> <!-- Body content -->
    <button id="count-btn">Click me</button> <!-- Button the user will click -->
    <p id="count-text">Clicks: 0</p> <!-- Paragraph that shows the click count -->
    <script> // Begin script
      let clicks = 0; // Start a counter at zero
      const button = document.getElementById("count-btn"); // Select the button
      const countText = document.getElementById("count-text"); // Select the paragraph
      button.addEventListener("click", function () { // Run this function on every button click
        clicks = clicks + 1; // Increase the counter by one
        countText.textContent = "Clicks: " + clicks; // Update the paragraph with the new count
      }); // End addEventListener call
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- `addEventListener("click", function () { ... })` waits for clicks; it does not run the function immediately.
- Each click updates both the variable and the visible text.
- Common mistake: writing `button.addEventListener("click", myFn())` with parentheses—that calls the function too early.

### Complete example: input event

```html
<!DOCTYPE html> <!-- HTML5 declaration -->
<html lang="en"> <!-- Root html -->
  <head> <!-- Head -->
    <meta charset="UTF-8" /> <!-- Encoding -->
    <title>Input Demo</title> <!-- Title -->
  </head> <!-- End head -->
  <body> <!-- Body -->
    <label for="name-input">Your name</label> <!-- Label linked to the input by id -->
    <input id="name-input" type="text" placeholder="Type here" /> <!-- Text box for typing -->
    <p id="live-preview">Hello, </p> <!-- Live preview paragraph -->
    <script> // Script start
      const nameInput = document.getElementById("name-input"); // Select the text input
      const preview = document.getElementById("live-preview"); // Select the preview paragraph
      nameInput.addEventListener("input", function () { // Fire on every change in the input
        preview.textContent = "Hello, " + nameInput.value; // Show Hello plus the current typed value
      }); // End listener
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- The **`input`** event runs as the user types, not only when they leave the field.
- `nameInput.value` always holds the current text inside the box.

### Student activity: click to toggle text

Create a button and a paragraph that starts as `Hidden message`.

1. On click, if the paragraph text is `Hidden message`, change it to `Message revealed`.
2. On the next click, change it back to `Hidden message`.
3. Keep toggling on every click.

Expected behavior: each click flips the message.

## DOM manipulation: create, modify, remove

Now you can change more than text.  
You can **build new elements**, attach them to the page, update attributes, and remove nodes you no longer need.  
This is **DOM manipulation**.

- **Create** — `document.createElement("tagName")` builds a new element in memory  
- **Modify** — set `textContent`, `className`, `id`, or attributes with `setAttribute`  
- **Attach** — `parent.appendChild(child)` places the new element into the live page  
- **Remove** — `element.remove()` takes an element off the page

### Complete example: add and remove list items

```html
<!DOCTYPE html> <!-- HTML5 declaration -->
<html lang="en"> <!-- Root -->
  <head> <!-- Head -->
    <meta charset="UTF-8" /> <!-- Encoding -->
    <title>List Manip Demo</title> <!-- Title -->
  </head> <!-- End head -->
  <body> <!-- Body -->
    <input id="task-input" type="text" placeholder="New task" /> <!-- Input for new task text -->
    <button id="add-btn">Add</button> <!-- Button to add a task -->
    <ul id="task-list"></ul> <!-- Empty list that will grow -->
    <script> // Script
      const taskInput = document.getElementById("task-input"); // Select the text input
      const addBtn = document.getElementById("add-btn"); // Select the Add button
      const taskList = document.getElementById("task-list"); // Select the ul container
      addBtn.addEventListener("click", function () { // When Add is clicked, run this function
        const text = taskInput.value.trim(); // Read input and remove extra spaces at ends
        if (text === "") { // Check whether the user typed nothing useful
          alert("Please type a task"); // Show a simple warning and stop
          return; // Exit the function early
        } // End empty check
        const li = document.createElement("li"); // Create a new list item element in memory
        li.textContent = text; // Put the typed text inside the new li
        const removeBtn = document.createElement("button"); // Create a Remove button for this item
        removeBtn.textContent = "Remove"; // Label the button
        removeBtn.addEventListener("click", function () { // When Remove is clicked for this item
          li.remove(); // Delete this li from the page
        }); // End remove listener
        li.appendChild(removeBtn); // Place the Remove button inside the li
        taskList.appendChild(li); // Attach the finished li to the visible list
        taskInput.value = ""; // Clear the input so the user can type the next task
      }); // End add listener
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- `createElement` only builds the node; `appendChild` makes it visible.
- Each item gets its own Remove button with its own listener.
- Clearing `taskInput.value` improves the typing flow after every add.

## Basic form validation with submit

Forms often need a check before data is accepted.  
The **`submit`** event is the right place for that check.  
You can stop the default page refresh and show a clear message.

![Signup form at a counter — empty fields marked in red and valid fields in green, like basic form validation before submit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session19/session19-05-form-validation-signup-counter.png?v=20260811)

- **Form validation (basic)**  
  - *Official meaning:* Checking user input against rules before accepting or sending the form.  
  - *In simple words:* Confirm the form is filled correctly before moving ahead.  
  - *Real-life example:* A bank form that refuses empty account fields before accepting an application.

- **`event.preventDefault()`**  
  - *Official meaning:* Cancels the browser’s default action for that event.  
  - *In simple words:* Stop the normal “refresh the page” behavior of form submit.  
  - *Real-life example:* Pausing an auto-closing lift door so people can enter safely.

### Complete example: validate a simple signup field

```html
<!DOCTYPE html> <!-- HTML5 declaration -->
<html lang="en"> <!-- Root -->
  <head> <!-- Head -->
    <meta charset="UTF-8" /> <!-- Encoding -->
    <title>Form Validation Demo</title> <!-- Title -->
  </head> <!-- End head -->
  <body> <!-- Body -->
    <form id="signup-form"> <!-- Form that will be validated on submit -->
      <label for="email">Email</label> <!-- Label for email field -->
      <input id="email" type="text" /> <!-- Email text input -->
      <button type="submit">Sign up</button> <!-- Submit button -->
    </form> <!-- End form -->
    <p id="form-message"></p> <!-- Paragraph for success or error messages -->
    <script> // Script
      const form = document.getElementById("signup-form"); // Select the form
      const email = document.getElementById("email"); // Select the email input
      const message = document.getElementById("form-message"); // Select the message paragraph
      form.addEventListener("submit", function (event) { // Listen for form submit
        event.preventDefault(); // Stop the page from refreshing on submit
        const value = email.value.trim(); // Read and trim the typed email
        if (value === "") { // Rule 1: email must not be empty
          message.textContent = "Email is required"; // Show error text
          message.style.color = "red"; // Make the error easy to notice
          return; // Stop here when validation fails
        } // End empty check
        if (value.includes("@") === false) { // Rule 2: email must contain @
          message.textContent = "Email must include @"; // Show format error
          message.style.color = "red"; // Keep error styling
          return; // Stop here when format is wrong
        } // End @ check
        message.textContent = "Form looks good. Welcome!"; // Show success text
        message.style.color = "green"; // Use green for success
      }); // End submit listener
    </script> <!-- End script -->
  </body> <!-- End body -->
</html> <!-- End html -->
```

**How the code works**

- Always call `preventDefault()` first if you want to stay on the same page and show messages.
- Validation rules run in order; early `return` stops later success logic.
- This is basic validation for learning—real apps often add more rules and server checks later.

### Student activity: mini feedback form

Build a form with a `textarea` (`id="feedback"`) and a submit button.

1. On submit, prevent the default refresh.
2. If feedback length is less than 5 characters, show `Please write a longer message` in red.
3. Otherwise show `Thanks for your feedback!` in green.

Expected: short text fails; longer text succeeds.

You now have the full loop: **select → listen → update**. Reuse the list and form examples above as templates for small interactive pages.

## Key Takeaways

- The **DOM** is the browser’s live tree of the page; **`document`** is your entry point to select and change elements.
- Use **`getElementById`** for unique ids; use **`querySelector`** / **`querySelectorAll`** for CSS-style selection of one or many elements.
- **Traversal** properties (`parentElement`, `children`, siblings) help you move through the tree and read content with `textContent` or `value`.
- **`addEventListener`** connects user actions (`click`, `input`, `submit`) to your functions so the page can respond.
- **DOM manipulation** creates, updates, and removes elements; pair it with basic **form validation** and `preventDefault()` for interactive forms.

These skills turn static HTML into interactive pages. In upcoming sessions, you will build on this foundation with richer UI behavior and more structured front-end patterns.

## Important Commands, Libraries, Terminologies used

| Term / API | Quick meaning |
| --- | --- |
| DOM | Live tree model of the HTML page in the browser |
| `document` | Object representing the whole page |
| `getElementById` | Select one element by unique id |
| `querySelector` | Select the first match for a CSS selector |
| `querySelectorAll` | Select all matches for a CSS selector |
| `textContent` | Read or write plain text inside an element |
| `innerHTML` | Read or write HTML markup inside an element |
| `value` | Read or write the current value of an input |
| `parentElement` / `children` | Move up or down one level in the DOM tree |
| `nextElementSibling` | Move to the next sibling element |
| `addEventListener` | Attach a function to an event |
| `click` / `input` / `submit` | Common user-interaction events |
| `createElement` | Create a new element in memory |
| `appendChild` | Attach a child element to a parent |
| `remove` | Delete an element from the page |
| `preventDefault` | Stop the browser’s default event action |
| Form validation | Checking input rules before accepting a form |
