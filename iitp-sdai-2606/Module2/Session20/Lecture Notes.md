# Advanced DOM Manipulation

In the previous session, you learned **DOM basics** and **event handling**: selecting elements, reading content, listening for clicks and inputs, and making small updates on the page.  
Those skills let you change what already exists on the screen.  
In this session, you will **create elements at runtime**, style them with JavaScript, and build interactive UI pieces like lists, tabs, and modals.

Think of the page as a living notice board.  
Earlier you updated sticky notes that were already pinned.  
Now you will add new notes, remove old ones, change their look, and rearrange the board as the user interacts.

## What you will learn in this session

- How to **create**, **append**, **remove**, and **replace** DOM elements dynamically
- How to change **inline styles** and **CSS classes** with JavaScript
- How to **traverse** the DOM and update elements for interactive UIs
- How to build guided practice components: a **dynamic list**, **tabs**, and a **modal**

## Why advanced DOM skills matter

![Hostel notice board with sticky notes being added, pinned, and removed — the page is a living board that JavaScript updates without reloading](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session20/session20-01-notice-board-dynamic-dom.png?v=20260811)

Static HTML alone cannot keep up with apps that react to users.  
A shopping cart or task list must create and remove items as people use them.  
**Advanced DOM manipulation** is how JavaScript rebuilds parts of the page without reloading the whole site.

- **Dynamic element**  
  - *Official meaning:* An HTML element created or changed by JavaScript while the page is running.  
  - *In simple words:* A new piece of the webpage that appears because your code made it.  
  - *Real-life example:* A railway app showing a fresh ticket card after you book—created at that moment, not printed in advance.
- **Why this matters:** Reloading for every small change feels slow; creating elements works better when the count keeps changing.

## Creating DOM elements at runtime

![Blank sticky note in hand, then written task text, then pinned on the board — createElement, configure with textContent, appendChild to make it visible](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session20/session20-02-create-configure-append.png?v=20260811)

To add something new, follow three steps: **create**, **configure**, then **attach**.

- **`document.createElement(tagName)`**  
  - *Official meaning:* Creates a new HTML element of the given tag type (for example `"li"` or `"div"`).  
  - *In simple words:* Builds a blank piece of the page in memory.  
  - *Real-life example:* Cutting a blank card before writing a friend’s name on it.
- **`appendChild(child)` / `append(...)`**  
  - *Official meaning:* Adds a node as the last child of a parent element.  
  - *In simple words:* Pins your new card onto the board.  
  - *Need:* Until you append, the element exists only in memory and is not visible.
- Prefer **`textContent`** for plain text. Use **`innerHTML`** only when you need markup, and never with untrusted user input.

### Complete example: create and append a list item

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document and sets language to English -->
<head> <!-- Holds metadata and the page title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Create Element Demo</title> <!-- Shows the tab title in the browser -->
</head> <!-- Ends the head section -->
<body> <!-- Starts the visible page content -->
  <h1>My Tasks</h1> <!-- Page heading for the task list -->
  <ul id="taskList"></ul> <!-- Empty list that JavaScript will fill -->
  <button id="addBtn">Add Task</button> <!-- Button that creates a new task -->

  <script> // Starts the JavaScript section
    const list = document.getElementById("taskList"); // Selects the empty unordered list
    const addBtn = document.getElementById("addBtn"); // Selects the Add Task button

    addBtn.addEventListener("click", function () { // Runs every time the button is clicked
      const item = document.createElement("li"); // Creates a new list item in memory
      item.textContent = "Finish notes"; // Puts plain text inside the new list item
      list.appendChild(item); // Attaches the list item to the visible list
    }); // Ends the click event listener
  </script> <!-- Ends the JavaScript section -->
</body> <!-- Ends the body -->
</html> <!-- Ends the HTML document -->
```

**How the code works**

- `createElement("li")` builds a new list item that is not yet on the page.
- `textContent` sets safe plain text; `appendChild` makes the item visible under `#taskList`.
- Each click adds another item—this is dynamic creation at runtime.

### Student activity: create three city names

1. Create an empty `<ul id="cities">` and a button in HTML.
2. On button click, create three `<li>` elements with text `Delhi`, `Mumbai`, and `Bengaluru` and append them to the list.

## Removing and replacing elements

Interactive UIs also remove items (delete a task) or swap one element for another (replace a message).

- **`element.remove()`**  
  - *Official meaning:* Removes the element from the document.  
  - *In simple words:* Takes that sticky note off the board.  
  - *Common error:* Trying to remove something never appended—keep a clear reference.
- **`parent.replaceChild(newNode, oldNode)`**  
  - *Official meaning:* Replaces an existing child node with a new node.  
  - *In simple words:* Swaps an old card for a new card in the same spot.  
  - *When to use:* When the position must stay fixed and the content changes.

### Complete example: remove and replace

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds page metadata -->
  <meta charset="UTF-8" /> <!-- Sets UTF-8 character encoding -->
  <title>Remove and Replace</title> <!-- Browser tab title -->
</head> <!-- Ends head -->
<body> <!-- Starts visible content -->
  <p id="status">Status: Pending</p> <!-- Paragraph that we will replace later -->
  <button id="doneBtn">Mark Done</button> <!-- Button to replace the status text -->
  <button id="clearBtn">Clear Status</button> <!-- Button to remove the status element -->

  <script> // Starts JavaScript
    const doneBtn = document.getElementById("doneBtn"); // Selects the Mark Done button
    const clearBtn = document.getElementById("clearBtn"); // Selects the Clear Status button

    doneBtn.addEventListener("click", function () { // Runs when Mark Done is clicked
      const status = document.getElementById("status"); // Finds the current status each click
      if (!status) { // Stops if status was already cleared from the page
        return; // Exits early when there is nothing to replace
      } // Ends the missing-status check
      const newStatus = document.createElement("p"); // Creates a new paragraph element
      newStatus.id = "status"; // Keeps the same id so later code can still find it
      newStatus.textContent = "Status: Completed"; // Sets the updated status message
      status.parentElement.replaceChild(newStatus, status); // Swaps old paragraph with new one
    }); // Ends the Mark Done listener

    clearBtn.addEventListener("click", function () { // Runs when Clear Status is clicked
      const current = document.getElementById("status"); // Finds the current status element
      if (current) { // Checks that the element still exists before removing
        current.remove(); // Removes the status paragraph from the page
      } // Ends the if check
    }); // Ends the Clear Status listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `replaceChild` swaps the pending message for a completed message in the same place.
- `remove()` deletes the element when Clear is clicked; `if (current)` avoids errors if it is already gone.

### Student activity: delete one list item

1. Create a list with two items: `Milk` and `Bread`.
2. Add a `Remove Milk` button that calls `.remove()` on the Milk item.

## Style manipulation with JavaScript

![Same index card shown plain and highlighted — inline style paints one card; classList toggles a ready-made highlight theme on and off](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session20/session20-03-classlist-style-themes.png?v=20260811)

After create/remove, the next polish step is **look and feel**—via **inline styles** or **CSS classes**.

- **Inline style (`element.style`)**  
  - *Official meaning:* Directly sets CSS properties on an element through the `style` object.  
  - *In simple words:* Hand-painting one specific card right now.  
  - *Example:* `box.style.backgroundColor = "lightyellow";`
- **CSS class toggling (`classList`)**  
  - *Official meaning:* Adds, removes, or toggles class names on an element.  
  - *In simple words:* Switching a card between ready-made themes (active, hidden, highlighted).  
  - *Why prefer classes:* Styles stay in CSS; JavaScript only switches the label.
- Use **`classList.toggle`** for on/off switches and **`contains`** to check state.

### Complete example: inline style and class toggle

```html
<!DOCTYPE html> <!-- Declares HTML5 document type -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds styles and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Style Demo</title> <!-- Browser tab title -->
  <style> /* Starts a small CSS block for class-based styling */
    .card { padding: 12px; border: 1px solid #ccc; margin-top: 10px; } /* Base card look */
    .highlight { background-color: #fff3cd; border-color: #e0a800; } /* Highlighted card look */
  </style> <!-- Ends the style block -->
</head> <!-- Ends head -->
<body> <!-- Starts visible content -->
  <div id="note" class="card">Revision reminder</div> <!-- Card that will be styled -->
  <button id="paintBtn">Paint Inline</button> <!-- Button for inline style change -->
  <button id="toggleBtn">Toggle Highlight</button> <!-- Button for class toggle -->

  <script> // Starts JavaScript
    const note = document.getElementById("note"); // Selects the note card
    const paintBtn = document.getElementById("paintBtn"); // Selects the Paint Inline button
    const toggleBtn = document.getElementById("toggleBtn"); // Selects the Toggle Highlight button

    paintBtn.addEventListener("click", function () { // Runs on Paint Inline click
      note.style.color = "navy"; // Changes text colour using an inline style
      note.style.fontWeight = "bold"; // Makes the text bold using an inline style
    }); // Ends the paint listener

    toggleBtn.addEventListener("click", function () { // Runs on Toggle Highlight click
      note.classList.toggle("highlight"); // Adds highlight if missing, removes if present
    }); // Ends the toggle listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `style.color` and `style.fontWeight` apply one-off inline changes.
- `classList.toggle("highlight")` switches a reusable CSS theme on and off.
- Prefer classes for repeated UI states; use inline styles for quick one-time tweaks.

### Student activity: active button style

1. Create two buttons: `Home` and `About`.
2. On click, remove `.active` from both, then add `.active` to the clicked button only.

## Traversing and updating the DOM

![Classroom desk row as a DOM tree — one bench is the parent, seats in the row are children, neighbouring seats are siblings; one seat highlighted as selected](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session20/session20-04-dom-traversal-classroom.png?v=20260811)

Real UIs often need you to **walk the tree**—find parents, children, or siblings—and update related pieces together.

- **DOM traversal**  
  - *Official meaning:* Moving between related nodes using `parentElement`, `children`, `firstElementChild`, and `nextElementSibling`.  
  - *In simple words:* Climbing the family tree of the page to find relatives of an element.  
  - *Real-life example:* From one classroom seat, finding the desk row (parent), neighbouring seats (siblings), and students in that row (children).
- Useful tools: `parentElement` (up), `children` (element kids), `querySelector` inside a parent.

### Complete example: update siblings from a clicked item

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts document -->
<head> <!-- Head section -->
  <meta charset="UTF-8" /> <!-- Character encoding -->
  <title>Traversal Demo</title> <!-- Tab title -->
  <style> .selected { background: #d1e7dd; } /* Soft green for the selected row */ </style> <!-- Ends styles -->
</head> <!-- Ends head -->
<body> <!-- Visible content -->
  <ul id="menu"> <!-- Parent list for menu items -->
    <li>Home</li> <!-- First menu item -->
    <li>Courses</li> <!-- Second menu item -->
    <li>Contact</li> <!-- Third menu item -->
  </ul> <!-- Ends the menu list -->

  <script> // Starts JavaScript
    const menu = document.getElementById("menu"); // Selects the parent list

    menu.addEventListener("click", function (event) { // Listens for clicks inside the list
      const clicked = event.target; // Finds the exact element that was clicked
      if (clicked.tagName !== "LI") { // Ignores clicks that are not on a list item
        return; // Stops early if the click was not on an LI
      } // Ends the tag check

      const items = menu.children; // Gets all LI children of the menu
      for (let i = 0; i < items.length; i++) { // Loops through every menu item
        items[i].classList.remove("selected"); // Clears selected style from each item
      } // Ends the loop

      clicked.classList.add("selected"); // Marks only the clicked item as selected
      console.log("Parent tag:", clicked.parentElement.tagName); // Logs parent tag for learning
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- Listening on the parent (`menu`) catches child clicks—this is **event delegation**.
- The loop clears old highlights; then only the clicked item gets `.selected`.

### Student activity: highlight next sibling

1. Create three paragraphs: `One`, `Two`, `Three` and a `Highlight Next` button.
2. On click, move to `nextElementSibling` and highlight it; wrap from last to first.

## Practice: dynamic list component

Combine create, remove, and style into a **dynamic task list**—the same pattern used in to-do apps and cart item lists.

### Complete example: add and delete tasks

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts document -->
<head> <!-- Head content -->
  <meta charset="UTF-8" /> <!-- Character encoding -->
  <title>Dynamic List</title> <!-- Tab title -->
  <style> .done { text-decoration: line-through; color: #888; } /* Marks completed tasks */ </style> <!-- Ends styles -->
</head> <!-- Ends head -->
<body> <!-- Visible page -->
  <h1>Task Board</h1> <!-- Heading -->
  <input id="taskInput" type="text" placeholder="Enter a task" /> <!-- Text box for new task -->
  <button id="addTask">Add</button> <!-- Button to add the task -->
  <ul id="tasks"></ul> <!-- Empty list for dynamic tasks -->

  <script> // Starts JavaScript
    const input = document.getElementById("taskInput"); // Selects the text input
    const addTask = document.getElementById("addTask"); // Selects the Add button
    const tasks = document.getElementById("tasks"); // Selects the task list

    addTask.addEventListener("click", function () { // Runs when Add is clicked
      const text = input.value.trim(); // Reads and trims the typed task text
      if (text === "") { // Checks for empty input
        alert("Please type a task"); // Shows a message if nothing was typed
        return; // Stops the function early
      } // Ends empty check

      const li = document.createElement("li"); // Creates a new list item
      li.textContent = text + " "; // Puts the task text inside the list item

      const doneBtn = document.createElement("button"); // Creates a Done button
      doneBtn.textContent = "Done"; // Labels the Done button
      doneBtn.addEventListener("click", function () { // Marks the task as done
        li.classList.toggle("done"); // Toggles the done style on the list item
      }); // Ends Done listener

      const delBtn = document.createElement("button"); // Creates a Delete button
      delBtn.textContent = "Delete"; // Labels the Delete button
      delBtn.addEventListener("click", function () { // Removes the task
        li.remove(); // Deletes this list item from the page
      }); // Ends Delete listener

      li.appendChild(doneBtn); // Adds the Done button inside the list item
      li.appendChild(delBtn); // Adds the Delete button inside the list item
      tasks.appendChild(li); // Attaches the finished list item to the list
      input.value = ""; // Clears the input box for the next task
    }); // Ends Add listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- Each task is a new `<li>` with its own Done and Delete buttons.
- `classList.toggle("done")` styles completion; `li.remove()` deletes that one task.

### Student activity: favourite cities list

Build a list where you type a city, click Add, and each row gets a Remove button.

## Practice: tabs component

![Browser UI with tab buttons and one active panel, plus a modal dialog above a dimmed page — classList switches tabs; overlay and dialog form a modal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session20/session20-05-tabs-modal-ui.png?v=20260811)

Tabs let users switch content panels without leaving the page—one tab looks active, and only its panel is visible.

### Complete example: three tabs

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts document -->
<head> <!-- Head section -->
  <meta charset="UTF-8" /> <!-- Character encoding -->
  <title>Tabs Demo</title> <!-- Tab title -->
  <style> /* Styles for tabs and panels */
    .tab { margin-right: 8px; } /* Spaces tab buttons apart */
    .tab.active { background: #0d6efd; color: #fff; } /* Highlights the active tab */
    .panel { display: none; margin-top: 12px; } /* Hides panels by default */
    .panel.active { display: block; } /* Shows only the active panel */
  </style> <!-- Ends styles -->
</head> <!-- Ends head -->
<body> <!-- Visible content -->
  <button class="tab active" data-panel="p1">Overview</button> <!-- First tab button -->
  <button class="tab" data-panel="p2">Syllabus</button> <!-- Second tab button -->
  <button class="tab" data-panel="p3">FAQ</button> <!-- Third tab button -->

  <div id="p1" class="panel active">Course overview text.</div> <!-- First panel content -->
  <div id="p2" class="panel">Syllabus details text.</div> <!-- Second panel content -->
  <div id="p3" class="panel">FAQ answers text.</div> <!-- Third panel content -->

  <script> // Starts JavaScript
    const tabs = document.querySelectorAll(".tab"); // Selects all tab buttons
    const panels = document.querySelectorAll(".panel"); // Selects all content panels

    tabs.forEach(function (tab) { // Loops through each tab button
      tab.addEventListener("click", function () { // Listens for a click on this tab
        tabs.forEach(function (t) { t.classList.remove("active"); }); // Clears active from every tab
        panels.forEach(function (p) { p.classList.remove("active"); }); // Clears active from every panel
        tab.classList.add("active"); // Marks the clicked tab as active
        const panelId = tab.getAttribute("data-panel"); // Reads which panel this tab controls
        document.getElementById(panelId).classList.add("active"); // Shows the matching panel
      }); // Ends click listener
    }); // Ends forEach over tabs
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `data-panel` links each button to its panel id.
- Clicking clears all active classes, then activates one tab and one panel.
- CSS `display` rules hide inactive panels so the UI stays clean.

### Student activity: two-tab profile

Create tabs named `Bio` and `Skills` with different text in each panel.

## Practice: modal component

A **modal** is a pop-up dialog above the page for a short task (confirm delete, show details).

- **Modal**  
  - *Official meaning:* An overlay UI that temporarily focuses the user on one action or message.  
  - *In simple words:* A temporary window that sits on top until you close it.  
  - *Real-life example:* The “Confirm order?” popup on a food delivery app.

### Complete example: open and close a modal

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts document -->
<head> <!-- Head section -->
  <meta charset="UTF-8" /> <!-- Character encoding -->
  <title>Modal Demo</title> <!-- Tab title -->
  <style> /* Styles for overlay and dialog */
    .overlay { /* Full-screen dim background */
      display: none; /* Hidden by default */
      position: fixed; /* Stays fixed over the viewport */
      inset: 0; /* Covers the full screen */
      background: rgba(0, 0, 0, 0.45); /* Semi-transparent dark overlay */
      align-items: center; /* Centers dialog vertically when flex is on */
      justify-content: center; /* Centers dialog horizontally when flex is on */
    } /* Ends overlay rule */
    .overlay.open { display: flex; } /* Shows overlay when open */
    .dialog { background: #fff; padding: 16px; width: 280px; } /* White dialog box */
  </style> <!-- Ends styles -->
</head> <!-- Ends head -->
<body> <!-- Visible page -->
  <button id="openModal">Open Modal</button> <!-- Button that opens the modal -->
  <div id="overlay" class="overlay"> <!-- Overlay container for the modal -->
    <div class="dialog"> <!-- Inner dialog box -->
      <p>Save your progress before leaving?</p> <!-- Modal message text -->
      <button id="closeModal">Close</button> <!-- Button that closes the modal -->
    </div> <!-- Ends dialog -->
  </div> <!-- Ends overlay -->

  <script> // Starts JavaScript
    const overlay = document.getElementById("overlay"); // Selects the overlay element
    const openModal = document.getElementById("openModal"); // Selects the Open button
    const closeModal = document.getElementById("closeModal"); // Selects the Close button

    openModal.addEventListener("click", function () { // Opens modal on button click
      overlay.classList.add("open"); // Adds the open class to show the overlay
    }); // Ends open listener

    closeModal.addEventListener("click", function () { // Closes modal on Close click
      overlay.classList.remove("open"); // Removes the open class to hide the overlay
    }); // Ends close listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- The overlay stays in HTML but stays hidden until `.open` is added.
- `classList.add` / `remove` controls visibility without recreating the dialog.

### Student activity: confirm delete modal

1. Show a Delete button on the page.
2. On click, open a modal asking “Delete this item?”
3. Add Yes and No buttons; No closes the modal, Yes closes it and shows `Item deleted`.

## Common mistakes (and how to avoid them)

- **Creating without appending:** the element exists in memory but never appears—always `append`.
- **Forgetting to clear old active classes:** tabs and menus look stuck on multiple items.
- **Using `innerHTML` with user typing:** prefer `textContent` for safety.
- **Removing the wrong node:** keep clear references; confirm with `console.log` before delete.
- **Inline style overload:** move repeated looks into CSS classes and toggle with `classList`.

## Key Takeaways

- **Create → configure → append** is the core pattern for dynamic elements.
- Use **`remove()`** and **`replaceChild`** when the UI must delete or swap parts of the page.
- Prefer **`classList`** for reusable visual states; use **`element.style`** for quick one-off tweaks.
- **Traversal** and parent-level listeners help you update related elements cleanly.
- Practice components—**lists**, **tabs**, and **modals**—reuse the same DOM tools in real UI shapes.

In an upcoming session, you will keep applying these DOM skills as your pages grow more interactive.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| `document.createElement("li")` | Creates a new element in memory |
| `appendChild` / `append` | Attaches a child node to a parent |
| `element.remove()` | Removes an element from the page |
| `replaceChild(newNode, oldNode)` | Swaps one child for another |
| `textContent` | Sets or reads plain text safely |
| `element.style` | Sets inline CSS properties in JS |
| `classList.add / remove / toggle` | Manages CSS classes from JavaScript |
| `parentElement` / `children` | Traverse up or into element children |
| `nextElementSibling` | Next element at the same level |
| Event delegation | Listening on a parent for child clicks |
| Dynamic list | UI that adds/removes items at runtime |
| Tabs | Switch visible panels with active states |
| Modal / overlay | Temporary dialog above the page |
| `data-*` attribute | Custom HTML data used by JavaScript |
