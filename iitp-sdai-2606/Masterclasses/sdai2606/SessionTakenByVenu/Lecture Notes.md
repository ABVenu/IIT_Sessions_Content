# Hands-On: Building a Complete Frontend Application

This lesson maps a normal web application, then builds one frontend page. You will split the work across frontend, backend, database, and API, see how JavaScript schedules clicks and timers, and save a Todo list in the browser.

If you have already seen how a browser draws a page, this lesson uses that page as a working program with state you can save.

## What You Will Learn in This Lesson

In this lesson, you will learn:

- How a web application splits work across **frontend**, **backend**, **database**, and **API**
- The working elements of **frontend engineering** and **backend engineering**
- How JavaScript runs **one job at a time**, and how the **event loop** runs timers and clicks
- How to build a **Todo** page that adds, completes, and deletes tasks and stores them in **Local Storage**

By the end, you will be able to name each layer, predict a short console order, and run a list that is still there after a refresh on the same browser.

---

## How a Typical Web Application Works

A web application has four parts. Each part has one job. The browser shows one of them. The other three sit behind the request.

- **Official Definition:** A **web application** is software used through a browser so that many people can read or change shared information.
- **In Simple Words:** A page that loads data, accepts an action, and shows an updated result.
- **Example:** A page with a task box, an Add button, and a list that changes after you click.

- **Official Definition:** The **frontend** is the part that runs in the browser: structure, appearance, and behaviour.
- **In Simple Words:** HTML, CSS, and JavaScript on the page the visitor sees.
- **Example:** The heading, the text box, the Add button, and the task list are frontend.

- **Official Definition:** The **backend** is the program on a server that receives requests, applies rules, and sends a response.
- **In Simple Words:** Code that runs outside the browser tab and decides what is allowed.
- **Example:** A program that rejects an empty task and writes the accepted task to storage.

- **Official Definition:** A **database** is an organised store that keeps data after the program stops, so the next request can read the latest facts.
- **In Simple Words:** The saved rows. Closing the page does not remove them.
- **Example:** A tasks table with columns `id`, `text`, and `done`.

- **Official Definition:** An **API** (Application Programming Interface) is the agreed set of requests and responses one program uses to ask another program to do something.
- **In Simple Words:** The exact shape of the ask and the exact shape of the answer.
- **Example:** `GET /tasks` returns a JSON array. `POST /tasks` sends `{ "text": "Revise the event loop" }`.

One request moves through the four parts in this order:

1. The visitor clicks a control on the **frontend**.
2. The browser sends an **HTTP request** to an API address.
3. The **backend** checks rules and reads or writes the **database**.
4. The backend sends a response, often **JSON**, back through the API.
5. The frontend updates the page from that response.

![How a web application is split — the browser frontend sends an HTTP request through an API to the backend, the database stores the row, and a JSON response returns to the page](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/sessionvenu/sessionvenu-01-web-layers.png?v=20260928)

- **Official Definition:** **HTTP** is the set of rules browsers and servers use to send a request and receive a response.
- **In Simple Words:** A request line plus headers and an optional body, then a status and a body in reply.
- **Example:** The browser sends `GET /tasks`. The server replies `200` and a JSON array.

- **Official Definition:** **JSON** (JavaScript Object Notation) is a text format for labelled data that both frontend and backend can read.
- **In Simple Words:** Text made of keys and values, arrays, and objects.
- **Example:** `{ "id": 1, "text": "Revise the event loop", "done": false }`.

**Need:** Shared data cannot live only inside one browser tab. Two visitors would each see their own copy. The database holds one copy. The API is the only way the page is allowed to read or change it.

**Logic:** Frontend asks. Backend decides. Database stores. API fixes the shape of the ask and the answer. When the page shows the wrong value, check which of those four is out of date.

| Step | Layer | What happens |
|---|---|---|
| Page is visible | Frontend | HTML, CSS, and JavaScript run in the browser |
| Visitor clicks Add | Frontend, then API | An HTTP request leaves the page |
| Task is stored | Backend + database | Rules run, then a row is written |
| List updates | Frontend | The page renders the JSON it received |

**Common doubt:** “The page showed the number, so the page owns the data.” The page owns the **rendering**. The database owns the **stored value** when that value must be shared.

**Activity — Write the five steps:**  
On paper, write the five steps of one save, in order: click, HTTP request, backend rule, database write, JSON painted on the page. Label each step Frontend, API, Backend, or Database.

The Todo page later in this lesson uses the same order — load, change, save, draw — with Local Storage in place of a database.

---

## HTTP Methods on That Request

The API names the path. The **method** names the action.

- **Official Definition:** An HTTP **method** is the verb on a request that states what the client wants the server to do with a resource.
- **In Simple Words:** The action word. Read, create, replace, or delete.
- **Example:** `GET /tasks` reads the list. `POST /tasks` creates one task.

| Method | Action | Typical body | Match in today’s page |
|---|---|---|---|
| **GET** | Read data | None | `loadTodos` reads the saved string |
| **POST** | Create data | JSON object | `addTodo` appends one object |
| **PUT** or **PATCH** | Update data | Fields to change | `toggleTodo` flips `done` |
| **DELETE** | Remove data | Often none | `deleteTodo` removes one `id` |

- **Official Definition:** An HTTP **status code** is a three-digit number in the response that reports the result of the request.
- **In Simple Words:** The server’s short answer before the JSON body.
- **Example:** `200` means the request succeeded. `400` means the body was rejected, such as empty `text`. `404` means that path does not exist.

This Todo page does not send those HTTP calls. The same four actions are the functions in the script. A later backend would expose them as routes and return these status codes.

**Activity — Match four functions:**  
Write `loadTodos`, `addTodo`, `toggleTodo`, and `deleteTodo` beside GET, POST, PATCH, and DELETE. One function per method.

---

## Elements of Frontend Engineering

Frontend engineering is the work of making the page structure, appearance, behaviour, and on-screen data match.

- **Official Definition:** **HTML** (HyperText Markup Language) describes the structure of a page: headings, text boxes, buttons, and lists.
- **In Simple Words:** The elements on the page, and their order.
- **Example:** A heading, a label, a text input, an Add button, and an empty `ul`.

- **Official Definition:** **CSS** (Cascading Style Sheets) describes how that structure looks: font, spacing, and styles such as a line through finished text.
- **In Simple Words:** Rules that change appearance without changing the data.
- **Example:** `.done span { text-decoration: line-through; }` marks a finished task.

- **Official Definition:** **JavaScript** is the language browsers run to respond to actions and to change the page after it has loaded.
- **In Simple Words:** The code that runs when the visitor clicks or types.
- **Example:** The Add button calls `addTodo`, which updates the list.

- **Official Definition:** The **DOM** (Document Object Model) is the live tree of the page in browser memory. JavaScript reads and updates that tree.
- **In Simple Words:** The page as the browser holds it while the tab is open.
- **Example:** `renderTodos` clears `ul` and appends one `li` per task. The `.html` file on disk stays the same.

- **Official Definition:** An **event** is a signal that something happened, such as a click or a key press. An **event handler** is the function that runs in answer.
- **In Simple Words:** The signal, and the function registered for that signal.
- **Example:** A click on Add is the event. `addTodo` is the handler.

- **Official Definition:** **State** is the data the page is currently treating as true, held in variables while the page is open.
- **In Simple Words:** The variables the screen is drawn from.
- **Example:** The `todos` array is state. The `li` elements are a rendering of that array.

| Element | Question it answers | In the Todo page |
|---|---|---|
| **Structure (HTML)** | What is on the page? | Heading, label, input, button, list |
| **Presentation (CSS)** | How does it look? | Column width, struck-through done text |
| **Behaviour (JavaScript)** | What happens on an action? | Add, mark done, delete |
| **Events** | Which action? | Click Add, or press Enter |
| **State** | What is true right now? | The `todos` array |
| **DOM update** | What should the visitor see? | Rebuild the list from that array |
| **Client storage** | What should survive a refresh? | Local Storage |
| **Messages** | What if the list is empty or the input is blank? | The status paragraph |

**Logic:** Keep one array as the source of truth. Draw the list from that array after every change. If you edit only the `li` text and leave the array unchanged, the next `renderTodos` puts the old text back.

**Common doubt:** “I changed the text on the screen. Why did refresh undo it?” Refresh builds a new DOM from the file and from stored data. A change that existed only in memory is gone.

**Activity — Label the page:**  
Sketch five boxes: heading, status line, text input, Add button, list. Write HTML under each box. Write “event” under Add. The full page later in this lesson matches that sketch.

Those elements are the frontend. A shared list still needs a backend. This lesson names that backend and then builds only the frontend.

---

## Elements of Backend Engineering

Backend engineering is the work of answering many clients with one set of rules and one stored copy of the data. This lesson lists the parts. The exercise itself runs in the browser.

| Element | Responsibility | Direct meaning |
|---|---|---|
| **Server** | Listens for HTTP requests | A program that stays running and replies |
| **Route** | Names one operation | `GET /tasks`, `POST /tasks`, `DELETE /tasks/1` |
| **Validation** | Rejects a bad request | Empty `text` gets no new row |
| **Business rules** | Applies decisions the product must enforce | Only the owner may delete that row |
| **Database** | Stores the shared rows | The table that remains after the process stops |
| **Auth** | Identifies who is asking | The account on the request |
| **Response** | Returns a status and data | `200` and a JSON array, or `400` for a bad body |

- **Official Definition:** A **server** in this lesson means a program that listens on a machine and replies to HTTP requests.
- **In Simple Words:** The process that accepts the request. The machine is only where that process runs.
- **Example:** The process reads `POST /tasks`, checks the body, and returns JSON.

**Need:** Shared rows, passwords, and “who may delete this” do not belong only in a file the visitor can edit. The backend checks the rule, then writes the database.

**Logic:** For a shared Todo, the browser would send the task text to a route. The backend would check the login, reject a blank string, insert a row, and return JSON. The frontend would render that JSON. Today’s functions — `loadTodos`, `addTodo`, `toggleTodo`, `deleteTodo`, `saveTodos` — are the same steps, with Local Storage in place of the database.

**Common doubt:** “Saving in the browser means I built a backend.” That save is **client storage**. Another browser profile, another device, and a private window each have a separate store. A shared list would live in a database and come back as JSON for the logged-in account.

**Activity — Split one function:**  
Take Delete. Write one sentence for the frontend job: remove that id from the rendered list. Write one sentence for the backend job: allow the delete only for the owner, then update the stored row.

The next section is how the JavaScript on the frontend page runs.

---

## How JavaScript Usually Behaves

JavaScript on a page follows one rule: **your code runs one step at a time on a single call stack.** The browser can prepare other work outside that stack. Your functions still take turns.

- **Official Definition:** A **call stack** is the structure that tracks which function is running now, and which function is waiting for it to return.
- **In Simple Words:** A list of function calls. Only the function at the top runs.
- **Example:** `addTodo` calls `saveTodos` and waits for that return, then calls `renderTodos`. A second click waits until the first `addTodo` returns.

Typical behaviour in this lesson:

- The script runs **from top to bottom**.
- A function body runs **when it is called**. Writing the function does not run it.
- `addEventListener` **registers** a handler. It does not call that handler during registration.
- A later line does not wait for a timer. The timer is scheduled, and the script continues.
- `localStorage` reads and writes **finish before the next line**. They are synchronous.

**Common mistake:** `setTimeout(showDone(), 1000)` calls `showDone` immediately and passes its return value to the timer. Pass the function as `showDone`, or write `function () { showDone(); }`.

**Common doubt:** “Will two clicks run at the same moment?” On this page the first click handler runs to the end, and the next click waits until the stack is empty. A long loop keeps the stack busy, so clicks wait and the page feels frozen.

The event loop is the mechanism that runs those waiting clicks and timers when the stack is empty.

---

## The Event Loop

The browser tracks timers and input while your script runs. When a timer finishes or a click happens, the callback joins a queue. The event loop places that callback on the stack only when the stack is empty.

![JavaScript event loop — while the script runs, C is on the call stack and B waits on the timer; after the stack is empty, the event loop runs B, so the console order is A, C, then B](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/sessionvenu/sessionvenu-02-event-loop.png?v=20260928)

- **Official Definition:** A **Web API** here means a browser feature outside your script, such as `setTimeout`, DOM events, or `fetch`, that can finish later and then hand a function back.
- **In Simple Words:** Browser features that do the wait, then queue your function.
- **Example:** `setTimeout(fn, 0)` queues `fn`. The next `console.log` in the current script still runs first.

- **Official Definition:** The **callback queue** (task queue) is the line of functions ready to run because a timer, a click, or similar browser work has finished.
- **In Simple Words:** Functions waiting for an empty call stack.
- **Example:** A click that happens during a long loop waits in this queue.

- **Official Definition:** The **event loop** checks whether the call stack is empty and, if it is, moves the next queued callback onto the stack.
- **In Simple Words:** The step that starts a queued function only after the current script has returned.
- **Example:** With a delay of `0`, the timer callback still prints after the current script’s last line.

- **Official Definition:** A **callback** is a function passed so that another function can call it later.
- **In Simple Words:** The function you hand over to be run at a later time.
- **Example:** The function inside `setTimeout`, and the function passed to `addEventListener`, are callbacks.

```html
<!DOCTYPE html> <!-- Marks this file as an HTML page -->
<html lang="en"> <!-- Root of the page; language is English -->
<head> <!-- Information about the page -->
  <meta charset="UTF-8"> <!-- So letters display correctly -->
  <title>Event Loop Order</title> <!-- Text on the browser tab -->
</head> <!-- End of page information -->
<body> <!-- What the visitor can see -->
  <p>Open the browser console. Read the order of the three lines.</p> <!-- Where the output appears -->
  <script> /* JavaScript for this demo starts here */
    console.log("A: start"); /* Prints immediately while this script is on the stack */
    setTimeout(function () { /* Asks the browser to queue this function */
      console.log("B: timer"); /* Prints only after the stack is clear */
    }, 0); /* The delay is 0 ms; the callback still waits for its turn */
    console.log("C: end"); /* Prints before B because it is still in this script */
  </script> <!-- End of the demo script -->
</body> <!-- End of the visible page -->
</html> <!-- End of the file -->
```

**How the code works:**

- `A: start` runs as a normal line, so it prints first.
- `setTimeout` schedules `B` and returns at once. It does not pause the script.
- `C: end` runs next, while this script is still on the stack.
- After the script ends, the stack is empty. The event loop then runs the timer callback, so `B: timer` prints last.
- Console order: **A**, then **C**, then **B**.

**Activity — Predict, then run:**  
Write the console order on paper before you open the file. Save it as `order.html`, open it, and check the console. If B printed before C, read the trace again: the current script finishes before a queued callback starts.

The Todo buttons use the same loop. `addEventListener` stores the callback. A click queues it later. `addTodo` runs when the stack is empty.

---

## A Todo Application in Local Storage

The page below is a complete frontend application. It adds a task, marks it done, deletes it, and shows the same list after a refresh. Storage is Local Storage in this browser.

![State is drawn onto the page — the todos array is the source, renderTodos paints that object into the DOM list, and the HTML file on disk stays the same](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/sessionvenu/sessionvenu-03-state-and-dom.png?v=20260928)

- **Official Definition:** **Local Storage** is a browser store that keeps string data for one origin on one browser profile, including after the tab closes, until that site’s data is cleared.
- **In Simple Words:** A key-value store in this browser for this site. Values are strings.
- **Example:** The key `study-todos` holds the task array as one JSON string. A phone browser does not have that entry.

Rules for this store:

- Local Storage stores **strings**. Turn an array into text with `JSON.stringify`. Turn that text back with `JSON.parse`.
- The store belongs to **this origin** (scheme, host, and port). Another site cannot read it.
- A **private window** and a **second browser** have separate stores.
- Two normal tabs of the same address share the stored string. Each tab redraws when code runs in that tab, or when you refresh it.
- Clearing site data, or calling `localStorage.removeItem`, deletes the entry.

**Data shape.** Each task is one object in an array: `id` (a number the page only increases), `text` (the typed string), and `done` (`true` or `false`). The first saved task is id `1`, text `Revise the event loop`, done `false`.

**Open the page over HTTP.** Save the file as `index.html` in a folder. In that folder, run:

`python3 -m http.server 5500`

Open `http://127.0.0.1:5500`. An editor Live Server button serves the same kind of address. Some browsers block or isolate Local Storage on a `file://` address.

```html
<!DOCTYPE html> <!-- Marks this file as an HTML page -->
<html lang="en"> <!-- Root of the page -->
<head> <!-- Information and styles live here -->
  <meta charset="UTF-8"> <!-- Correct display for the letters you type -->
  <title>Study Todos</title> <!-- Browser tab title -->
  <style> /* Look of the page */
    body { font-family: Arial, sans-serif; max-width: 520px; margin: 32px auto; } /* A readable narrow column */
    li { display: flex; gap: 8px; align-items: center; margin: 8px 0; } /* One task per row */
    .done span { text-decoration: line-through; } /* Finished task text looks completed */
  </style> <!-- End of the look rules -->
</head> <!-- End of page information -->
<body> <!-- Everything the visitor sees -->
  <h1>Study Todos</h1> <!-- Heading -->
  <p id="status">Loading your list...</p> <!-- Short status so the page is never silent -->
  <label for="taskInput">New task</label> <!-- Name for the box, tied to the input id -->
  <input id="taskInput" type="text" placeholder="Example: Revise the event loop"> <!-- Where you type a task -->
  <button id="addBtn" type="button">Add</button> <!-- Adds the task; type button avoids a form reload -->
  <ul id="taskList"></ul> <!-- JavaScript fills this list from the array -->
  <script> /* Behaviour of the page */
    const STORAGE_KEY = "study-todos"; /* Key used in Local Storage */
    let todos = []; /* The list in memory; the screen is drawn from this */
    let nextId = 1; /* The next id to give a new task */

    function loadTodos() { /* Read saved tasks when the page opens */
      const raw = localStorage.getItem(STORAGE_KEY); /* Saved text, or null if nothing is saved */
      if (!raw) { /* Nothing saved yet */
        todos = []; /* Start from an empty list */
        return; /* Stop this function */
      } /* End of the empty-storage check */
      try { /* Parsing can fail if the saved text is damaged */
        const parsed = JSON.parse(raw); /* Turn the text back into data */
        todos = Array.isArray(parsed) ? parsed : []; /* Keep it only when it is an array */
      } catch (error) { /* Damaged text should not freeze the page */
        todos = []; /* Fall back to an empty list */
      } /* End of the safe parse */
      todos.forEach(function (item) { /* Walk each saved task */
        if (item.id >= nextId) { /* This id is already used */
          nextId = item.id + 1; /* Keep the next id unused */
        } /* End of the id check */
      }); /* End of the walk */
    } /* End of loadTodos */

    function saveTodos() { /* Write the memory list into Local Storage */
      localStorage.setItem(STORAGE_KEY, JSON.stringify(todos)); /* Store the array as one string */
    } /* End of saveTodos */

    function renderTodos() { /* Draw the list from the array */
      const list = document.getElementById("taskList"); /* The ul on the page */
      const status = document.getElementById("status"); /* The message line */
      list.innerHTML = ""; /* Remove old rows before drawing again */
      if (todos.length === 0) { /* No tasks in memory */
        status.textContent = "No tasks yet. Add your first one."; /* Empty-state message */
        return; /* Nothing to draw */
      } /* End of the empty-list check */
      status.textContent = "Tasks saved in this browser: " + todos.length; /* Show the count */
      todos.forEach(function (item) { /* One row for each task */
        const li = document.createElement("li"); /* A new row */
        if (item.done) { /* This task is finished */
          li.className = "done"; /* Apply the struck-through style */
        } /* End of the done check */
        const label = document.createElement("span"); /* Holds the task words */
        label.textContent = item.text; /* textContent shows words without treating them as HTML */
        const toggleBtn = document.createElement("button"); /* Marks the task done or not done */
        toggleBtn.type = "button"; /* Does not submit a form */
        toggleBtn.textContent = item.done ? "Undo" : "Done"; /* The label matches the flag */
        toggleBtn.addEventListener("click", function () { /* Register the click; do not run it now */
          toggleTodo(item.id); /* Flip this id when the click later runs */
        }); /* End of the Done listener */
        const deleteBtn = document.createElement("button"); /* Removes the task */
        deleteBtn.type = "button"; /* Does not submit a form */
        deleteBtn.textContent = "Delete"; /* Visible label */
        deleteBtn.addEventListener("click", function () { /* Register the click */
          deleteTodo(item.id); /* Remove this id when the click later runs */
        }); /* End of the Delete listener */
        li.appendChild(label); /* Put the words in the row */
        li.appendChild(toggleBtn); /* Put Done or Undo in the row */
        li.appendChild(deleteBtn); /* Put Delete in the row */
        list.appendChild(li); /* Put the row into the ul */
      }); /* End of the draw loop */
    } /* End of renderTodos */

    function addTodo() { /* Create one task from the box */
      const input = document.getElementById("taskInput"); /* The text box */
      const text = input.value.trim(); /* Words with surrounding spaces removed */
      if (text === "") { /* A blank task is not worth saving */
        document.getElementById("status").textContent = "Type a task before you add."; /* Explain the miss */
        return; /* Leave memory and storage unchanged */
      } /* End of the blank check */
      todos.push({ id: nextId, text: text, done: false }); /* Add one object to the array */
      nextId = nextId + 1; /* Prepare a fresh id */
      input.value = ""; /* Clear the box */
      saveTodos(); /* Persist the array */
      renderTodos(); /* Draw from the array */
    } /* End of addTodo */

    function toggleTodo(id) { /* Flip done for one id */
      todos.forEach(function (item) { /* Look at each task */
        if (item.id === id) { /* This is the clicked task */
          item.done = !item.done; /* true becomes false, and the reverse */
        } /* End of the match */
      }); /* End of the search */
      saveTodos(); /* Persist the flip */
      renderTodos(); /* Draw again */
    } /* End of toggleTodo */

    function deleteTodo(id) { /* Remove one task */
      todos = todos.filter(function (item) { /* Build a new array of keepers */
        return item.id !== id; /* Keep every task whose id is different */
      }); /* End of the filter */
      saveTodos(); /* Persist the shorter list */
      renderTodos(); /* Draw again */
    } /* End of deleteTodo */

    document.getElementById("addBtn").addEventListener("click", addTodo); /* Add runs later, on a click */
    document.getElementById("taskInput").addEventListener("keydown", function (event) { /* Also listen to keys */
      if (event.key === "Enter") { /* Enter should do the same work as Add */
        addTodo(); /* Reuse one function so the rules stay in one place */
      } /* End of the Enter check */
    }); /* End of the key listener */
    loadTodos(); /* Read Local Storage before the first drawing */
    renderTodos(); /* Draw whatever was loaded, including an empty list */
  </script> <!-- End of the page behaviour -->
</body> <!-- End of the visible page -->
</html> <!-- End of the file -->
```

**How the code works:**

- `todos` is the source of truth in memory. `renderTodos` draws that array and does not invent tasks.
- `loadTodos` runs once at the bottom of the script, before the first draw, so a refresh can show the saved list.
- `saveTodos` runs after add, toggle, and delete. A change that skips `saveTodos` is gone after refresh.
- `JSON.stringify` turns the array into text. `JSON.parse` turns that text back into data. Damaged text is caught, and the page starts from an empty array.
- `list.innerHTML = ""` removes old rows. Task text is set with `textContent`, so the typed string is shown as text.
- Each button **registers** a callback. The event loop runs `toggleTodo` or `deleteTodo` when that click reaches an empty stack.
- `addTodo` trims spaces and returns on an empty string. A backend route should apply the same check.
- `filter` keeps every object whose `id` is not the deleted one, then assigns that new array to `todos`.

![Save in the browser, then load on refresh — Add updates the todos array, localStorage stores the study-todos string, the list renders, and refresh runs getItem, JSON.parse, then render list](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/sessionvenu/sessionvenu-04-local-storage-loop.png?v=20260928)

**Trace.** Start with an empty store. Type `Revise the event loop` and click Add.

| Step | `todos` in memory | Local Storage | Screen |
|---|---|---|---|
| Page opens | `[]` | empty | “No tasks yet…” |
| Add | `[{ id: 1, text: "Revise the event loop", done: false }]` | that array as text | one row, button says Done |
| Click Done | same object, `done: true` | updated text | task text is struck through, button says Undo |
| Refresh | `loadTodos` rebuilds the array | unchanged until the next edit | the struck-through task is back |

**Activity — Check storage:**  
Add two tasks. Mark one done. Refresh. Both tasks should return, and the done task should stay struck through. Open the same address in a private window. That window’s list should start empty. Return to the normal window and confirm the two tasks are still there.

**Activity — Blank input and delete:**  
Click Add with an empty box. The status line should say to type a task, and the list should stay the same length. Delete one task, refresh, and confirm it is still gone.

When the page matches the table, the frontend loop is complete: event, update state, save, render.

---

## Key Takeaways

- A web application splits **frontend** (the page), **API** (the request and response shape), **backend** (the rules), and **database** (the shared rows).
- Frontend work is HTML, CSS, events, state, and rendering the DOM from that state. Backend work is listening, validating, applying rules, and storing shared data.
- JavaScript runs one step at a time on the **call stack**. Timers and clicks wait in a queue. The **event loop** runs them when the stack is empty, so a `0` ms timer still prints after the current script.
- The Todo page keeps an array in memory and a string in **Local Storage**. Refresh restores this browser’s copy. Another device has its own store.
- The same load, change, save, and render steps are what a later API will do against a database when more than one browser must share one list.

---

## Important Commands, Libraries, Terminologies Used

| Term | Meaning (quick revision) |
|---|---|
| **Frontend** | HTML, CSS, and JavaScript in the browser |
| **Backend** | The program that applies rules and talks to storage |
| **Database** | Shared storage that remains after the process stops |
| **API** | The agreed shape of requests and responses |
| **HTTP method** | Verb on a request: GET, POST, PATCH, DELETE |
| **Status code** | `200` success, `400` rejected body, `404` unknown path |
| **Origin** | Scheme, host, and port; Local Storage is separate per origin |
| **JSON** | Text of keys and values; `JSON.stringify` and `JSON.parse` |
| **HTML / CSS / JavaScript** | Structure / appearance / behaviour |
| **DOM** | Live page tree that script updates |
| **Event / handler** | A signal / the function registered for that signal |
| **State** | The `todos` array the screen is drawn from |
| **Call stack** | The list of functions running now; the top one runs |
| **Web API** | Browser features for timers, clicks, and network calls |
| **Callback queue** | Ready functions waiting for an empty stack |
| **Event loop** | Moves the next queued callback onto the empty stack |
| **Callback** | A function passed so it can run later |
| **`setTimeout(fn, 0)`** | Queues `fn`; it runs after the current script ends |
| **Local Storage** | String store for this origin on this browser profile |
| **`localStorage.getItem` / `setItem`** | Read one key / write one key |
| **`textContent`** | Sets task text as text |
| **`Array.isArray`** | Checks that parsed storage is an array |
| **`filter`** | Returns a new array of the tasks you keep |
