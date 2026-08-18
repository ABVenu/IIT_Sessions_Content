# Asynchronous JavaScript

In the previous session, you learned **advanced DOM manipulation**: creating and removing elements, changing styles and classes, and building small UI pieces such as lists, tabs, and modals.  
Those skills update the page the moment the user clicks.  
This session adds a new skill: **waiting**—so a message can appear after a delay, a countdown can tick, and the page stays usable while time passes.

Think of a hostel canteen.  
If you stand at the counter until one dosa is fully cooked, everyone behind you waits.  
If you take a **token**, sit down, and get called when the dosa is ready, the counter keeps serving other people.

## What you will learn in this session

- How **synchronous** execution differs from **asynchronous** execution
- How **callback functions** let you say “run this later”
- How **`setTimeout`** runs code once after a delay
- How **`setInterval`** repeats code until you stop it
- How to combine timers with **DOM updates** for interactive pages

## Why waiting must not freeze the page

A website that freezes while it waits feels broken.  
If JavaScript could only work in a straight line, a 3-second wait would lock buttons, typing, and scrolling.  
**Asynchronous JavaScript** lets the browser keep the page alive while a delayed task finishes in the background.

- **Blocking**  
  - *Official meaning:* Code that stops everything else until it finishes.  
  - *In simple words:* The whole queue is stuck behind one slow order.  
  - *Need:* You want waits (countdowns, reminders, later network calls) without freezing the UI.
- Common doubt: “If I write three lines, do they always run in that visible order?” For normal lines, yes. For timers, the delayed line is scheduled, not frozen in place.

## Synchronous vs asynchronous execution

JavaScript reads your script from top to bottom.  
The difference is whether a line **must finish now** or can be **scheduled for later**.

![Kirana billing queue frozen behind one customer versus hostel canteen tokens — synchronous work blocks the line; asynchronous work lets others continue while the kitchen cooks](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session21/session21-01-sync-vs-async-canteen.png?v=20260818)

- **Synchronous execution**  
  - *Official meaning:* Each statement completes before the next statement starts.  
  - *In simple words:* One job at a time, in order, with no skipping ahead.  
  - *Real-life example:* A single billing counter at a kirana store—customer 1 finishes, then customer 2 starts.
- **Asynchronous execution**  
  - *Official meaning:* A task is started, other work continues, and a function runs later when the task is ready.  
  - *In simple words:* You place an order, keep talking, and get called when the food is ready.  
  - *Real-life example:* A railway counter token: you take a number, sit, and return when your number is displayed.
- JavaScript itself uses **one main line of work** (one call stack).  
  The **browser** holds timers; when the wait is over, your function is given back to JavaScript.

### Complete example: same story, two timings

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document and sets language to English -->
<head> <!-- Holds metadata and the page title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Sync vs Async</title> <!-- Shows the tab title in the browser -->
</head> <!-- Ends the head section -->
<body> <!-- Starts the visible page content -->
  <p>Open the console (Right click → Inspect → Console).</p> <!-- Tells the student where to look -->

  <script> // Starts the JavaScript section
    console.log("SYNC: take plate"); // Runs immediately and prints the first sync step
    console.log("SYNC: take rice"); // Runs immediately after the previous line finishes
    console.log("SYNC: take dal"); // Runs immediately after rice is logged

    console.log("ASYNC: order placed"); // Runs now; this is still synchronous code
    setTimeout(function () { // Asks the browser to wait, then run this function later
      console.log("ASYNC: dosa ready"); // Prints only after the delay, not in the middle of the next lines
    }, 2000); // Waits at least 2000 milliseconds (2 seconds) before the callback runs
    console.log("ASYNC: sit at table"); // Runs immediately; it does not wait for the dosa message
  </script> <!-- Ends the JavaScript section -->
</body> <!-- Ends the body -->
</html> <!-- Ends the HTML document -->
```

**How the code works**

- The three `SYNC` lines print in order because each `console.log` finishes at once.
- `setTimeout` does **not** pause the script; it books a later call and lets the next line run.
- Console order: `order placed`, then `sit at table`, then after about 2 seconds `dosa ready`.

### Student activity: predict the order

1. On paper, write the console order for: `A`, then `setTimeout` that prints `B` after 0 ms, then `C`.
2. Run it and check. `B` still comes after `C`, because even `0` means “after current code finishes.”

## How JavaScript waits without freezing

You already know the page can listen for clicks.  
A timer is similar: the browser watches the clock, and JavaScript only runs your function when it is free.

![Hostel canteen with one serving window, a kitchen clock, a ready-food shelf, and a waiter — call stack, browser timer, callback queue, and event loop as a working canteen](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session21/session21-02-event-loop-canteen.png?v=20260818)

- **Call stack**  
  - *Official meaning:* The list of functions JavaScript is running right now.  
  - *In simple words:* The one window at the office that can serve one file at a time.
- **Web API / browser timer**  
  - *Official meaning:* Browser features (such as timers) that work outside the main JavaScript stack.  
  - *In simple words:* The kitchen that cooks while the counter talks to the next student.
- **Callback queue**  
  - *Official meaning:* A waiting line of functions that are ready to run.  
  - *In simple words:* Plates kept on the “ready” shelf until the counter is free.
- **Event loop**  
  - *Official meaning:* The process that moves a ready callback onto the call stack when the stack is empty.  
  - *In simple words:* The waiter who brings food only when your hands are free.
- Logic: `setTimeout` hands the wait to the browser.  
  When time is up, the function stands in the queue.  
  It runs only after the current synchronous code is finished—so the page can still click and type during the wait.

## Callbacks: functions that run later

Timers need an answer to “what should happen when the wait is over?”  
That answer is a **callback**—a function you pass to someone else.

![Delivery rider receives a folded note saying when you reach, call this number — a callback is a packed instruction to run later](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session21/session21-03-callback-delivery-note.png?v=20260818)

- **Callback function**  
  - *Official meaning:* A function passed as an argument to another function, to be invoked later.  
  - *In simple words:* A packed instruction: “When you are done, run this.”  
  - *Real-life example:* Giving the delivery person a note: “On reaching, call this number.”
- You already used callbacks: `addEventListener("click", function () { ... })` is a callback for a click.
- **Named callback:** a function with a name (`function greet() {}`) that you pass as `greet`.
- **Anonymous callback:** a function written in place (`function () { ... }`) with no name.
- **Why callbacks matter for async work:** The delay is unknown. You cannot write the next line as if the wait already finished. You put the “after” steps inside the callback.
- Common error: writing `setTimeout(myFunction(), 1000)` with extra `()`.  
  That **calls** the function immediately and passes its return value. Pass the function name, or write `function () { ... }`.

### Complete example: a callback as a packed instruction

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Callback Demo</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <p>Open the console to see the callback run.</p> <!-- Hint for where output appears -->

  <script> // Starts JavaScript
    function greet(name) { // Defines a function that will be used as a callback
      console.log("Hello, " + name); // Prints a greeting using the name it received
    } // Ends the greet function

    function processUser(callback) { // Accepts another function as an input named callback
      const user = "Asha"; // Prepares the data that the callback will need
      callback(user); // Runs the passed-in function and gives it the user name
    } // Ends processUser

    processUser(greet); // Passes greet (not greet()) so processUser can call it later
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `greet` is a normal function; it becomes a callback only because it is passed in.
- `processUser(greet)` does not print by itself; it calls `greet("Asha")` from inside.
- This is the same idea as “when the timer finishes, run this function.”

### Complete example: callback in an async workflow

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts the document -->
<head> <!-- Holds title -->
  <meta charset="UTF-8" /> <!-- Sets encoding -->
  <title>Async Callback Flow</title> <!-- Tab title -->
</head> <!-- Ends head -->
<body> <!-- Starts body -->
  <p id="stage">Idle</p> <!-- Status text that the workflow will update -->

  <script> // Starts JavaScript
    function afterDelay(ms, callback) { // Helper: wait, then run the given callback
      setTimeout(callback, ms); // Schedules callback after ms milliseconds
    } // Ends afterDelay

    const stage = document.getElementById("stage"); // Selects the status paragraph

    stage.textContent = "Order placed"; // Shows the first stage at once
    afterDelay(1000, function () { // After 1 second, run this inner function
      stage.textContent = "Cooking"; // Updates the page to the cooking stage
      afterDelay(1000, function () { // After another 1 second, run the next step
        stage.textContent = "Ready to serve"; // Shows the final stage on the page
      }); // Ends the second afterDelay call
    }); // Ends the first afterDelay call
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `afterDelay` hides `setTimeout` so the steps read like a small workflow.
- Each next message lives **inside** the previous callback, because it must wait for that delay.
- Nested callbacks work for two or three steps; many nested layers become hard to read—you will learn cleaner patterns in an upcoming session.

### Student activity: greet after a wait

1. Write a function `showDone` that sets a paragraph to `Done`.
2. Pass `showDone` to `setTimeout` with a 1500 ms delay. Confirm the text changes after 1.5 seconds.

## setTimeout: run once after a wait

Now the timer API itself.  
**`setTimeout`** is how you book a **one-time** future action.

- **`setTimeout(callback, delay)`**  
  - *Official meaning:* Schedules `callback` to run after at least `delay` milliseconds.  
  - *In simple words:* “After this many thousandths of a second, do this once.”  
  - *Real-life example:* Setting a phone alarm for 10 minutes, not a repeating reminder.
- Delay is measured in **milliseconds** (ms): 1000 ms = 1 second, 2500 ms = 2.5 seconds, 0 ms = “as soon as current code finishes.”
- It returns a **timer ID** (a number) that you can use to cancel the wait.
- The delay is a **minimum**, not a promise of exact time. If JavaScript is busy, the callback may run a little later.
- `setTimeout(fn, 0)` still waits until current code finishes. It is not “run this instantly in the middle.”

### Complete example: delayed message on the page

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts the document -->
<head> <!-- Holds title -->
  <meta charset="UTF-8" /> <!-- Sets encoding -->
  <title>setTimeout Message</title> <!-- Tab title -->
</head> <!-- Ends head -->
<body> <!-- Starts body -->
  <p id="note">Please wait...</p> <!-- Placeholder text shown at the start -->
  <button id="startBtn">Start 3s reminder</button> <!-- Button that starts the delay -->

  <script> // Starts JavaScript
    const note = document.getElementById("note"); // Selects the message paragraph
    const startBtn = document.getElementById("startBtn"); // Selects the start button

    startBtn.addEventListener("click", function () { // Runs when the button is clicked
      note.textContent = "Reminder is ticking..."; // Immediate feedback so the user knows it started
      setTimeout(function () { // Schedules a one-time update after the wait
        note.textContent = "Time to revise JavaScript!"; // Replaces the waiting text after 3 seconds
      }, 3000); // 3000 milliseconds equals 3 seconds
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- The click handler updates the DOM at once, then books a later update.
- After about 3 seconds the callback runs and changes `textContent`.
- The button stays clickable during the wait—this is asynchronous behaviour with DOM.

### Stopping a timeout with clearTimeout

Sometimes the user changes their mind before the delay ends.

- **`clearTimeout(timerId)`**  
  - *Official meaning:* Cancels a timeout created by `setTimeout`, if it has not already run.  
  - *In simple words:* Turning off the alarm before it rings.  
  - *Need:* A “Cancel reminder” button should not still show the message later.

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts the document -->
<head> <!-- Holds title -->
  <meta charset="UTF-8" /> <!-- Sets encoding -->
  <title>clearTimeout Demo</title> <!-- Tab title -->
</head> <!-- Ends head -->
<body> <!-- Starts body -->
  <p id="msg">Ready</p> <!-- Status text for the reminder -->
  <button id="startBtn">Start 4s reminder</button> <!-- Starts the delayed message -->
  <button id="cancelBtn">Cancel</button> <!-- Cancels the reminder if still waiting -->

  <script> // Starts JavaScript
    const msg = document.getElementById("msg"); // Selects the status paragraph
    const startBtn = document.getElementById("startBtn"); // Selects the Start button
    const cancelBtn = document.getElementById("cancelBtn"); // Selects the Cancel button
    let reminderId = null; // Stores the timeout id so Cancel can use it

    startBtn.addEventListener("click", function () { // Runs when Start is clicked
      msg.textContent = "Waiting..."; // Immediate feedback that the reminder started
      clearTimeout(reminderId); // Clears any older reminder so only one is active
      reminderId = setTimeout(function () { // Books a one-time update and saves its id
        msg.textContent = "Done"; // Shows Done only if Cancel was not pressed in time
        reminderId = null; // Clears the stored id after the callback has run
      }, 4000); // Waits at least 4000 milliseconds (4 seconds)
    }); // Ends the Start listener

    cancelBtn.addEventListener("click", function () { // Runs when Cancel is clicked
      clearTimeout(reminderId); // Stops the scheduled callback if it has not run yet
      reminderId = null; // Forgets the old id
      msg.textContent = "Cancelled"; // Updates the page so the student sees the cancel
    }); // Ends the Cancel listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- Save the return value of `setTimeout`; `clearTimeout` needs that id.
- Cancel before 4 seconds and `Done` never appears. If the callback already ran, clearing does nothing useful.

### Student activity: snooze the reminder

1. Keep Start and Cancel as in the example above.
2. Add a `Snooze` button that cancels the current timeout and starts a **new** 4-second `setTimeout` that writes `Done after snooze`.
3. Confirm that clicking Snooze during the wait delays `Done` instead of showing it on the old schedule.

## setInterval: run again and again

`setTimeout` is a single bell.  
**`setInterval`** is a repeating metronome—perfect for clocks and countdowns.

![Phone alarm ringing once versus a wall clock and cricket scoreboard ticking every second — setTimeout runs once; setInterval repeats until you stop it](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session21/session21-04-settimeout-setinterval.png?v=20260818)

- **`setInterval(callback, delay)`**  
  - *Official meaning:* Repeatedly calls `callback` every `delay` milliseconds until cleared.  
  - *In simple words:* “Keep doing this every so often.”  
  - *Real-life example:* A wall clock advancing every second, or a cricket scoreboard refreshing.
- It also returns an id. **Always plan how it will stop.** An uncleared interval keeps running even if the user cannot see why.
- Common error: starting a new interval on every click without clearing the old one—numbers jump twice as fast.

### Complete example: countdown on the page

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts the document -->
<head> <!-- Holds title -->
  <meta charset="UTF-8" /> <!-- Sets encoding -->
  <title>Countdown</title> <!-- Tab title -->
</head> <!-- Ends head -->
<body> <!-- Starts body -->
  <h1 id="count">5</h1> <!-- Heading that shows the current number -->
  <button id="goBtn">Start countdown</button> <!-- Button that starts the interval -->

  <script> // Starts JavaScript
    const countEl = document.getElementById("count"); // Selects the countdown heading
    const goBtn = document.getElementById("goBtn"); // Selects the start button
    let timerId = null; // Holds the interval id so we can stop it later

    goBtn.addEventListener("click", function () { // Runs when Start countdown is clicked
      if (timerId !== null) { // Prevents two intervals if the user clicks again
        return; // Leaves the handler so a second countdown does not start
      } // Ends the already-running check

      let n = 5; // Local counter for this countdown
      countEl.textContent = n; // Shows 5 immediately on the page

      timerId = setInterval(function () { // Starts repeating every 1000 ms
        n = n - 1; // Moves one second closer to zero
        if (n <= 0) { // Checks whether the countdown has finished
          clearInterval(timerId); // Stops the repeating timer
          timerId = null; // Allows a new countdown if the button is clicked again
          countEl.textContent = "Go!"; // Final DOM update when time is up
        } else { // Still counting down
          countEl.textContent = n; // Writes the new number onto the page
        } // Ends the if/else
      }, 1000); // Repeats every 1000 milliseconds (1 second)
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- The page shows `5` at once; then each second it shows `4`, `3`, `2`, `1`, then `Go!`.
- `clearInterval` is required; without it the callback would keep running after `Go!`.
- `timerId` is set back to `null` so the student can start again without overlapping timers.

### clearInterval: stopping the repeat

- **`clearInterval(timerId)`**  
  - *Official meaning:* Stops a repeating timer created by `setInterval`.  
  - *In simple words:* Switching off the metronome.  
  - *When to use:* Countdown finished, user clicked Stop, or the component is no longer on the page.

### Student activity: stopwatch seconds

1. Show `0` and buttons `Start`, `Stop`, and `Reset`.
2. Start adds 1 to the number every second using `setInterval`.
3. Stop uses `clearInterval`. Reset sets the number back to `0` and clears any running interval.

## Combining async behaviour with DOM updates

You now have the two pieces from this module: **DOM skills** and **timers**.  
Together they make UI that feels alive—status text, toasts, and buttons that recover after a wait.

![Laptop page showing Sending status and a Message sent toast while the student can still use the screen — timers update the DOM without freezing the page](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session21/session21-05-async-dom-toast.png?v=20260818)

- Update **`textContent`** inside callbacks so the user sees progress.
- Toggle **`disabled`** or **`classList`** during the wait so people do not double-submit.
- Use **`createElement`** and **`append`** inside a timer to grow a list over time—same DOM tools as the previous session, now on a delay.
- Create or remove elements after a delay when a notice should appear and then leave.

### Complete example: send button, status, and auto-hide toast

```html
<!DOCTYPE html> <!-- Declares HTML5 -->
<html lang="en"> <!-- Starts the document -->
<head> <!-- Holds styles and title -->
  <meta charset="UTF-8" /> <!-- Sets encoding -->
  <title>Async DOM Practice</title> <!-- Tab title -->
  <style> /* Starts a small CSS block for the toast */
    #toast { display: none; margin-top: 12px; padding: 8px; background: #e6f4ea; } /* Hidden success box by default */
    #toast.show { display: block; } /* Visible when the show class is added */
  </style> <!-- Ends the style block -->
</head> <!-- Ends head -->
<body> <!-- Starts body -->
  <button id="sendBtn">Send</button> <!-- Button that starts the fake send -->
  <p id="status">Ready</p> <!-- Live status text -->
  <div id="toast">Message sent</div> <!-- Toast that appears after success -->

  <script> // Starts JavaScript
    const sendBtn = document.getElementById("sendBtn"); // Selects the Send button
    const status = document.getElementById("status"); // Selects the status paragraph
    const toast = document.getElementById("toast"); // Selects the toast box
    let hideId = null; // Stores the toast-hide timeout so a new send can cancel it

    sendBtn.addEventListener("click", function () { // Runs when Send is clicked
      sendBtn.disabled = true; // Prevents a second click during the wait
      status.textContent = "Sending..."; // Immediate DOM feedback
      toast.classList.remove("show"); // Hides any old toast from a previous send
      clearTimeout(hideId); // Stops an older hide callback from hiding a later toast

      setTimeout(function () { // Pretends the send takes 2 seconds
        status.textContent = "Sent"; // Updates status when the wait is over
        toast.classList.add("show"); // Shows the toast on the page
        sendBtn.disabled = false; // Allows another send

        hideId = setTimeout(function () { // Books a hide, and saves the id
          toast.classList.remove("show"); // Hides the toast after it has been visible
        }, 2000); // Toast stays visible for 2 seconds
      }, 2000); // Fake sending delay of 2 seconds
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- Click → disable button → `Sending...` at once (synchronous DOM update).
- After 2 seconds the send callback updates status, shows the toast, and re-enables the button.
- `hideId` stores the hide timeout; a new click clears it so an old hide cannot cover a new toast.

### Student activity: auto-adding list items

1. Start with an empty `<ul id="log">` and a `Start` button.
2. Every second, `createElement("li")`, set text to `Tick 1`, `Tick 2`, … and `append` it.
3. After 5 ticks, `clearInterval` and append one last item: `Stopped`.

### Student activity: delayed highlight

1. Create a note `<div>` and a button `Highlight in 2s`.
2. On click, wait 2 seconds with `setTimeout`, then `classList.add("highlight")`.
3. After 2 more seconds, `classList.remove("highlight")`.

## Common mistakes (and how to avoid them)

- **Thinking `setTimeout` pauses the next line:** the next line runs immediately; delayed work belongs in the callback.
- **Writing `setTimeout(fn(), 1000)`:** the extra `()` runs `fn` now. Pass `fn` or `function () { fn(); }`.
- **Forgetting `clearInterval`:** the timer keeps firing and can speed up if you start another interval.
- **Treating the delay as exact:** it is a minimum wait; a busy page can be slightly late.
- **Starting timers in a loop with `var`:** all callbacks may share one final value. Prefer `let` for the loop variable.
- **Updating the DOM only in the console:** users need `textContent` / `classList` changes on the page.

## Key Takeaways

- **Synchronous** code runs in order and waits; **asynchronous** code schedules work and keeps the page free.
- A **callback** is a function you pass so it can run later—on a click, or when a timer finishes.
- **`setTimeout`** runs once after a delay; **`clearTimeout`** cancels it.
- **`setInterval`** repeats until **`clearInterval`**; always decide when the repeat should stop.
- Timers plus DOM updates (`textContent`, `classList`, `createElement`) make countdowns, toasts, and delayed UI.

In an upcoming session, you will use this same “start now, finish later” idea when the browser talks to a server and waits for data.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| Synchronous | Each line finishes before the next starts |
| Asynchronous | Work is scheduled; other code continues |
| Callback | Function passed in to be called later |
| Call stack | Functions JavaScript is running now |
| Event loop | Moves ready callbacks onto the stack |
| `setTimeout(fn, ms)` | Run `fn` once after at least `ms` ms |
| `clearTimeout(id)` | Cancel a scheduled timeout |
| `setInterval(fn, ms)` | Run `fn` every `ms` ms |
| `clearInterval(id)` | Stop a repeating interval |
| Timer id | Number returned by timeout/interval |
| `button.disabled` | Block clicks during a wait |
| `classList.add / remove` | Show or hide UI after a delay |
| `createElement` / `append` | Add list items from inside a timer |
