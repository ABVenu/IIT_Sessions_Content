# Masterclass: Asynchronous JavaScript

A `for` loop that counts five marks finishes in a blink. A page that asks a railway computer for **PNR status** cannot. If JavaScript waited for that answer the same way it waits for the next line of a loop, the whole tab would freeze: no clicks, no typing, no “loading” text that actually moves.

**Asynchronous JavaScript** is how the browser keeps the page alive while slow work finishes **later**. Timers, **Promises**, and **`async`/`await`** are the tools. You need them **before** you ask the network for data, because a network ask is slow work.

In this lesson you run every demo in the **browser**. HTML is the page, CSS is the look, and JavaScript is a **linked script**. The **print order** appears in the **browser Console**, not as text on the page. The print order *is* the lesson.

## What You Will Learn in This Lesson

- How to link **HTML**, **CSS**, and **JS**, and how to read **`console.log`** in DevTools
- How **synchronous** work runs one line after another, and how **asynchronous** work is scheduled for later
- Why JavaScript is **single-threaded** and still **non-blocking**
- How **`setTimeout`** defers a job without freezing the rest of the program
- The three **Promise** states: **pending**, **fulfilled**, and **rejected**
- How **`.then` / `.catch`** and **`async`/`await`** with **`try`/`catch`** wait for a result
- Why a **network request** (the idea behind **`fetch`**) must be asynchronous

By the end, you will open a local page, read the Console, trace print order on paper, and explain why `fetch` cannot be treated like a normal `return`.

---

## How You Will Run the Demos

Create one folder on your computer named `async-lab`. Keep these three files **in the same folder**.

| File | Job |
|---|---|
| `index.html` | Structure of the page and the **links** to CSS and JS |
| `styles.css` | Look of the page (the Console still holds the lesson output) |
| `script.js` | JavaScript. **Replace this file’s contents** for each demo |

- **Official Definition:** An **external script** is a `.js` file loaded with `<script src="script.js"></script>`, so the browser runs that file after it has the HTML.
- **In Simple Words:** The page points to a separate notebook of JavaScript instead of stuffing all the code inside the HTML.
- **Real-Life Example:** A circular (HTML) plus a style sheet (CSS) plus a separate instruction slip (JS).

**Need:** Async behaviour is a **browser** story (timers, `fetch`, a tab that must stay alive). Practising only in a paste box hides that.

**How to open the Console**

1. Double-click `index.html` so it opens in Chrome or Edge.
2. Open DevTools: **F12**, or **Ctrl + Shift + J** (Windows), or **Cmd + Option + J** (Mac), or right-click → **Inspect** → **Console**.
3. Refresh the page after you save `script.js`. New `console.log` lines appear in order.

**Common error:** Looking only at the white page. This lesson’s answers are in the **Console**.  
**Common error:** Putting `script.js` in a different folder from `index.html`. The link then 404s and nothing logs.

![How this lab runs — a laptop with the webpage, DevTools Console, and three same-folder files: index.html, styles.css, and script.js](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-01-html-css-js-console.png?v=20260910)

Save this complete starter. You will **keep** `index.html` and `styles.css` for every demo. Only `script.js` changes.

```html
<!DOCTYPE html>  <!-- Tell the browser this is an HTML5 page -->
<html lang="en">  <!-- Root of the document -->
  <head>  <!-- Metadata and CSS link -->
    <meta charset="UTF-8" />  <!-- Character set -->
    <title>Async Lab</title>  <!-- Browser tab text -->
    <link rel="stylesheet" href="styles.css" />  <!-- Load the CSS file from the same folder -->
  </head>  <!-- End of head -->
  <body>  <!-- Visible page -->
    <h1>Asynchronous JavaScript</h1>  <!-- Page heading -->
    <p>Open the <strong>Console</strong> (F12). Output is logged there, not on this page.</p>  <!-- Student reminder -->
    <script src="script.js"></script>  <!-- Load JS last so the page HTML already exists -->
  </body>  <!-- End of body -->
</html>  <!-- End of document -->
```

```css
body {  /* Style the whole page */
  font-family: Arial, sans-serif;  /* Clear font */
  max-width: 40rem;  /* Comfortable reading width */
  margin: 2rem auto;  /* Centre the block */
  color: #1a1a1a;  /* Dark text */
  background: #f7f4ee;  /* Light page background */
}  /* End of body rules */

h1 {  /* Style the heading */
  color: #1a4f8b;  /* Dark blue */
}  /* End of h1 rules */
```

The first `script.js` is in the next section.

---

## Synchronous Execution: One Line, Then the Next

Everyday JavaScript you already use — `let`, `if`, `for`, functions — is usually **synchronous**.

- **Official Definition:** **Synchronous** execution means each statement finishes before the next statement starts, on a single **call stack**.
- **In Simple Words:** JavaScript is a clerk who completes one slip fully before picking up the next slip.
- **Real-Life Example:** A photocopy machine that will not take the second page until the first page has come out.

- **Official Definition:** The **call stack** is the browser’s list of functions that are running right now, from the current function down to the starter.
- **In Simple Words:** A stack of plates. The plate on top is the function that must finish first.
- **Real-Life Example:** You cannot start packing the tiffin until the roti on the stove is done, if you have only one pan.

**Need:** If you do not name this “one-at-a-time” rule, later timers look like magic. They are not magic. They are *later* work.

**Logic:** A long synchronous loop occupies the clerk. Nothing else in that tab can run until the loop ends.

Replace the whole of `script.js` with this complete file. Save, refresh, watch the **Console**.

```javascript
console.log("Chai 1: boil water");  // First job at the stall — logs now
console.log("Chai 2: add tea leaves");  // Second job — only after water has "boiled" in this script
console.log("Chai 3: pour into the cup");  // Third job — only after leaves are added
```

**How the code works:**

- The three `console.log` calls run in **strict order**, like three steps of making chai
- The Console always shows boil, then leaves, then pour
- Nothing is saved for “later”

**Activity — Predict sync order:**  
Without refreshing, write the three chai steps in the order they will appear. Then refresh `index.html` and confirm in the Console. Expected: boil water, add tea leaves, pour into the cup.

Synchronous code is honest and simple. It becomes a problem when one job is **slow**. That problem sits next to another fact: JavaScript has **only one thread**, and yet a good page does **not** freeze.

---

## Why a Slow Job Must Not Block the Clerk

Imagine the clerk at a token window. Counting three tokens is fast. Calling another city to confirm a PNR is slow.

If the clerk **stops the whole queue** until that phone call ends, people behind you cannot even hear “next.” A web page that behaves like that feels **frozen**.

- **Official Definition:** **Blocking** means the call stack stays busy on one job, so the page cannot run other JavaScript (clicks, typing, timers) until that job finishes.
- **In Simple Words:** The clerk has locked the window for one long phone call.
- **Real-Life Example:** A UPI app that would not let you tap Cancel while it waited 20 seconds for the bank.

**Need:** Network, timers, and “wait 2 seconds” are slow compared with `1 + 1`. The page must still respond.

**Logic:** Finish the fast work. Hand the slow work to the browser’s **timer / network** tools. Come back when the result is ready.

**Common error:** Writing an empty `for` loop that spins until two seconds have passed. That still **blocks**. The clerk is busy counting. The page still freezes.

Synchronous waiting is the wrong tool for slow jobs. **Asynchronous** execution is the right one. First, name two words that students mix up: **single-threaded** and **non-blocking**.

---

## JavaScript Is Single-Threaded and Still Non-Blocking

JavaScript in the browser tab is **single-threaded**. That does **not** mean every wait must freeze the page. It is also **non-blocking** when you use timers, Promises, and `fetch`.

- **Official Definition:** **Single-threaded** means the JavaScript in that tab has **one call stack**: only one JS instruction runs at a time.
- **In Simple Words:** One clerk at the token window, not a team of clerks talking at once.
- **Real-Life Example:** One person at a photocopy shop. They cannot stamp two forms in the same instant.

- **Official Definition:** **Non-blocking** means the program can **start** slow work and **leave the call stack free** until that work finishes, instead of standing idle on the stack.
- **In Simple Words:** The clerk starts the milk, serves the next customer, and comes back when the milk boils.
- **Real-Life Example:** You tap “Check PNR.” You can still scroll. The answer arrives later. The tab did not lock.

**Need:** “Single-threaded” sounds like “the page must freeze.” That is the blocking story, not the JavaScript story we want.

**Logic:** The **one thread** only runs JavaScript. Waiting for a clock or a network is handed to **browser Web APIs**. When they finish, the **event loop** gives the clerk the next slip. One clerk. No freeze.

| Idea | Meaning | If you get it wrong |
|---|---|---|
| **Single-threaded** | One JS clerk (one call stack) | Thinking two `console.log` lines run at the same instant |
| **Blocking** | That clerk stares at one slow job | A giant `for` loop; the page ignores clicks |
| **Non-blocking** | Slow wait happens *off* the stack | `setTimeout` / Promise / `fetch` — B can log before C |

![One thread, still non-blocking — call stack as one clerk, Web APIs holding the timer and fetch, event loop, then a callback queue for later jobs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-02-call-stack-event-loop.png?v=20260910)

**Common doubt:** “If there is only one thread, how can C run later while B already ran?”  
B ran on the thread. The two-second wait was **not** the thread sleeping. The thread was free. C is a later slip.

**Common error:** Calling JavaScript “multi-threaded” because the page stays clickable. Clicks are later jobs on the **same** thread, not a second JS clerk.

**Activity — One sentence:**  
Write: “JavaScript is ____-threaded, but timers are ____-blocking.” Expected: single, non.

The next `script.js` is the proof: **one** clerk, but ginger is cut **while** the milk boils.

---

## Asynchronous Execution: Schedule It, Keep Moving

- **Official Definition:** **Asynchronous** execution means the program **starts** a slow job, **continues** with the next lines, and **handles the result later** when the job finishes.
- **In Simple Words:** Put the milk on the stove, and cut ginger while it boils. Do not stare at the pot doing nothing.
- **Real-Life Example:** You submit an IRCTC search and can still move the mouse. Results appear when the server answers.

**Need:** The tab must stay alive. **Logic:** Slow work is handed to the browser. Your function returns. Later, a **callback** or a **Promise** runs.

- **Official Definition:** A **callback** is a function you pass in so it can be called later, when an event or timer completes.
- **In Simple Words:** A slip that says “when the milk boils, call me.”
- **Real-Life Example:** “Ring the bell when the photocopies are ready.” You do not stand at the machine in silence.

**Common doubt:** “Is asynchronous the same as two clerks?”  
In the browser, JavaScript still has **one** main clerk (one call stack). The *waiting* happens outside that clerk. When the wait ends, the clerk runs your later function.

The simplest later-function in the browser is **`setTimeout`**.

---

## setTimeout: Deferred Work

- **Official Definition:** **`setTimeout`** is a browser function that runs a callback **after** at least a given number of milliseconds.
- **In Simple Words:** “Do this, but not now — after a delay.”
- **Real-Life Example:** A reminder: “Call home in two minutes.” You can still pack your bag during those two minutes.

**Need:** To show that “later” is real. **Logic:** `setTimeout` does **not** pause the next line. It only **registers** the callback.

Time is in **milliseconds**. `1000` means one second. `2000` means two seconds.

Keep the same `index.html` and `styles.css`. Replace the whole of `script.js` with this complete file. Open the **Console**, then refresh.

```javascript
// One JS thread. A busy while-loop would freeze the tab. setTimeout does not.
console.log("A: put milk on the stove");  // Runs now — first Console line
setTimeout(function () {  // Hand the “milk boiled” job to the browser timer; do not stare at the pot
  console.log("C: milk boiled — pour chai");  // Runs later — third Console line
}, 2000);  // Delay of 2000 milliseconds (2 seconds)
console.log("B: cut ginger while it boils");  // Runs now — second Console line, before C
```

**How the code works:**

- `A` prints immediately in the Console (milk is on)
- `setTimeout` **schedules** the inner function and returns at once (the clerk is free)
- `B` prints immediately after that (ginger while the milk boils)
- About two seconds later, `C` prints (milk boiled)
- Expected order: **A**, then **B**, then **C** — never A, C, B

![setTimeout print order — put milk on the stove, cut ginger while it boils, then pour chai: A then B then C, never A then C then B](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-03-settimeout-chai-order.png?v=20260910)

**Common error:** Expecting the script to “sleep” at `setTimeout` so `B` prints after `C`. That would be a blocking sleep. The browser does not do that here.

**Common doubt:** “Is the delay exact?”  
It is “at least” that many milliseconds. If the clerk is busy with a long loop, the callback waits a bit more.

**Activity — Predict the timer:**  
On paper, write A, B, and C in the order they print. Refresh and tick the Console. Then change `2000` to `0`, save, refresh. You still usually see A, B, then C, because C is **later**, even with a 0 ms delay. Later means “after the current stack is clear,” not “after you blink.”

That “after the current stack is clear” rule is the **event loop** in one sentence.

- **Official Definition:** The **event loop** is the browser’s habit of running the call stack to empty, then picking up **later** jobs (timers, Promise reactions, clicks).
- **In Simple Words:** Finish the plates that are already in your hands. Then check the bell for the next later job.
- **Real-Life Example:** Complete the current photocopy. Then look at the “ready” light. Do not drop the current page halfway.

| When | What runs |
|---|---|
| Now | Lines already on the call stack (`A`, then `setTimeout` registration, then `B`) |
| Later | The `setTimeout` callback (`C`), after the delay **and** after the stack is clear |

![The JavaScript event loop — call stack runs now, Web APIs hold the timer and fetch, callback C waits in the queue, event loop moves C onto the stack when the stack is empty](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-06-js-event-loop.png?v=20260910)

**Need:** Without this picture, `setTimeout(..., 0)` looks broken. **Logic:** Zero delay still means *later queue*, not *this line*.

`setTimeout` is one later job. Real products have many later jobs that can **succeed** or **fail**. That is what a **Promise** models.

---

## Promises: A Value That Arrives Later

- **Official Definition:** A **Promise** is an object that represents a value that may be available now, later, or never, and that settles into success or failure.
- **In Simple Words:** A token for “your chai is being made.” Later the token becomes a cup, or the stall says the gas is over.
- **Real-Life Example:** An IRCTC booking that is not “yes” or “no” in the same millisecond. It is *in progress*, then *confirmed* or *failed*.

**Need:** Callbacks inside callbacks become a knot. A Promise is one object you can wait on, with a clear success path and a clear failure path.

A Promise has **exactly three states**. It moves from the first to one of the last two, and then it **stays**.

| State | Meaning | Chai-stall picture |
|---|---|---|
| **Pending** | Not finished yet | Milk is still on the stove |
| **Fulfilled** (resolved) | Success; a result value is ready | Cup is handed over |
| **Rejected** | Failure; a reason is ready | Gas ended; no chai |

![A Promise has three states — pending ticket in the middle, fulfilled with resolve and then, rejected with reject and catch](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-04-promise-states.png?v=20260910)

- **Official Definition:** **Fulfill** (resolve) means the Promise succeeded and now holds a result. **Reject** means it failed and now holds a reason (often an **Error**).
- **In Simple Words:** Resolve = “here is the cup.” Reject = “sorry, cannot.”
- **Real-Life Example:** UPI **success** versus UPI **failed** — not a third forever-maybe after it has already failed.

**Logic:** You do not check a Promise with `if (promise === true)`. You **attach later work** with `.then` / `.catch` or `await`.

**Common error:** Treating a Promise like a ready string. `console.log(thePromise)` prints the Promise object, not the later message, if you log too early.

Replace the whole of `script.js` with this complete file. Refresh with the Console open.

```javascript
function checkPnr(pnr) {  // Real-life helper: ask IRCTC-style PNR; succeed later or fail now
  return new Promise(function (resolve, reject) {  // Create a Promise; resolve = confirmed, reject = failed
    if (!pnr) {  // Guard: empty PNR is invalid, like a blank form at the window
      reject(new Error("PNR missing — cannot check"));  // Fail the Promise with a reason
      return;  // Stop this function; do not start a timer
    }  // End of the missing-PNR check
    setTimeout(function () {  // After a short delay, the “railway computer” answers
      resolve("PNR " + pnr + " confirmed — seat 14B");  // Succeed and store this status as the result
    }, 1000);  // 1000 ms = one second of “in progress”
  });  // End of the Promise executor
}  // End of checkPnr

console.log("Before PNR check");  // Prints now in the Console
const ticket = checkPnr("1234567890");  // Start the check; ticket is a Promise, not the seat number yet
console.log("After calling checkPnr");  // Prints now, while the Promise is still pending
console.log(ticket);  // Prints the Promise object (pending at this moment)
```

**How the code works:**

- `new Promise` runs the inner function **now**
- `setTimeout` schedules the **resolve** (PNR confirmed)
- `checkPnr("1234567890")` **returns immediately** with a Promise still **pending**
- “Before PNR check” and “After calling checkPnr” print first in the Console
- After about 1 second the Promise becomes **fulfilled**, but this script does not yet *use* that status string

You have a ticket. Next you must **collect the confirmation** with `.then` and **hear bad news** with `.catch`.

**Activity — Name the state:**  
For each moment, write `pending`, `fulfilled`, or `rejected`: (1) just after `const ticket = checkPnr("1234567890")`, (2) after 1 second on a valid PNR, (3) immediately after `checkPnr("")` starts. Expected: pending, fulfilled, rejected.

---

## then and catch: Collect Success or Failure

- **Official Definition:** **`.then`** registers a function to run when the Promise is **fulfilled**. **`.catch`** registers a function to run when the Promise is **rejected**.
- **In Simple Words:** `.then` = “when the cup is ready, do this.” `.catch` = “if it fails, do this instead.”
- **Real-Life Example:** SMS “ticket confirmed” versus SMS “payment failed.”

**Need:** Without `.then` / `.catch` (or `await`), the later value is unused. **Logic:** Those functions run **later**, on the event loop, when the Promise settles.

Replace the whole of `script.js` with this complete file. Refresh and read the Console order.

```javascript
function payUpi(pinIsCorrect) {  // Real-life helper: UPI pay — later success, or fail at once
  return new Promise(function (resolve, reject) {  // Create the Promise
    if (!pinIsCorrect) {  // Wrong PIN, like a failed UPI
      reject(new Error("UPI failed — wrong PIN"));  // Failure path
      return;  // Do not start a timer
    }  // End of guard
    setTimeout(function () {  // Bank takes a moment
      resolve("UPI success — Rs 80 paid to chai stall");  // Result string
    }, 800);  // 800 ms delay
  });  // End of Promise
}  // End of payUpi

console.log("1. start payment");  // First Console line

payUpi(true)  // Correct PIN — will succeed after ~800 ms
  .then(function (message) {  // When fulfilled, receive the bank SMS
    console.log("3. success:", message);  // Print the later message
  })  // End of then
  .catch(function (err) {  // If this pay had rejected, run here instead
    console.log("failure:", err.message);  // Print the error text
  });  // End of catch

payUpi(false)  // Wrong PIN — fails at once
  .then(function (message) {  // Will not run, because this Promise rejects
    console.log("would succeed:", message);  // Not printed
  })  // End of then
  .catch(function (err) {  // Runs because the PIN is wrong
    console.log("4. caught:", err.message);  // Print UPI failed — wrong PIN
  });  // End of catch

console.log("2. still using the app");  // Second Console line — before the 800 ms success
```

**How the code works:**

- Console shows **1. start payment**, then **2. still using the app** immediately
- The wrong-PIN `payUpi(false)` rejects **now**, so **4. caught** appears soon
- After about 800 ms, **3. success** appears
- `.then` does not run on a rejected Promise; `.catch` does not run on a fulfilled one (unless you chain further)

**Common error:** Forgetting `.catch`. A rejected Promise with no handler can show an **unhandled rejection** in the Console.

**Common doubt:** “Can I use `.then` without `.catch`?”  
You can, but then failures are easy to miss. Pair them while you learn.

**Activity — Two outcomes on paper:**  
Draw two boxes: **fulfilled** and **rejected**. Under fulfilled, write what `payUpi(true)` prints in `.then`. Under rejected, write what `payUpi(false)` prints in `.catch`. Refresh and tick both in the Console.

`.then` / `.catch` work. For several steps in a row they still look nested. **`async`/`await`** lets you write later work in a shape closer to ordinary lines.

---

## async and await: Later Work in Straight Lines

- **Official Definition:** An **`async` function** always returns a **Promise**. Inside it, **`await`** pauses **that function** until a Promise settles, without blocking the rest of the page.
- **In Simple Words:** `await` means “stay on this line of *this* recipe until the cup arrives, but do not lock the whole canteen.”
- **Real-Life Example:** You wait at the chai stall for *your* token. Other customers can still order.

**Need:** Reading `payUpi().then().then().catch()` is tiring. `async`/`await` is the same machine with clearer steps.

**Logic:** `await checkResult("roll-12")` **does not** freeze other JavaScript. It only holds **this async function** until the Promise fulfills or rejects.

**Common error:** Writing `await checkResult("roll-12")` **outside** an `async` function in beginner scripts. Put `await` inside `async function ...`.

**Common error:** Forgetting that `async function` returns a Promise. `console.log(openPortal())` logs a Promise, not the marksheet string, unless you `await openPortal()` from another `async` function or use `.then`.

Failures use **`try` / `catch`**, the same pair you use for ordinary errors, but here they catch **rejected** Promises from `await`.

- **Official Definition:** **`try`/`catch`** around `await` runs the `catch` block if the awaited Promise **rejects** (or if a normal error is thrown).
- **In Simple Words:** Try to collect the cup. If the stall says no, handle it in `catch`.
- **Real-Life Example:** Try to pay UPI. If it fails, show “try again,” do not crash the whole app.

Replace the whole of `script.js` with this complete file. Refresh with the Console open.

```javascript
function checkResult(rollNo) {  // Real-life helper: college result portal — later marksheet, or fail
  return new Promise(function (resolve, reject) {  // Create the Promise
    if (!rollNo) {  // Guard: blank roll number
      reject(new Error("Roll number missing — cannot open result"));  // Failure
      return;  // Stop
    }  // End of guard
    setTimeout(function () {  // Portal takes a moment
      resolve("Result for " + rollNo + ": Pass — 78%");  // Success value
    }, 700);  // Delay
  });  // End of Promise
}  // End of checkResult

async function openPortal() {  // async so we are allowed to use await inside
  console.log("A: open result portal");  // Logs after this function actually starts
  try {  // Try the happy path
    const ok = await checkResult("roll-12");  // Pause this function until the marksheet arrives
    console.log("C: got", ok);  // Logs after ~700 ms
    const bad = await checkResult("");  // Blank roll — jump to catch
    console.log("would not print", bad);  // Skipped
  } catch (err) {  // Runs when any await in try rejects
    console.log("D: handled", err.message);  // Logs Roll number missing
  }  // End of catch
  console.log("E: close the portal tab");  // Logs after catch, still inside openPortal
}  // End of openPortal

console.log("before calling openPortal");  // First Console line
openPortal();  // Start the async function; it returns a Promise at once
console.log("B: you can still scroll the page");  // Logs while openPortal is waiting on checkResult
```

**How the code works:**

- `openPortal` starts, logs **A**, then `await checkResult("roll-12")` schedules later work
- **B** logs next, because the rest of `script.js` is not waiting
- After ~700 ms, **C** logs, then `checkResult("")` rejects, **D** logs, then **E**
- Typical Console order: `before calling openPortal`, **A**, **B**, then later **C**, **D**, **E**

**Activity — Trace async/await:**  
On paper, number the Console lines: before, A, B, C, D, E. Refresh. If C appeared before B, you still thought `await` blocked the whole page. It does not. You can still scroll the HTML page while the marksheet is pending.

`.then` and `await` are two spellings of the same wait.

| Style | Success | Failure | Feel |
|---|---|---|---|
| **`.then` / `.catch`** | function in `.then` | function in `.catch` | Extra functions after the Promise |
| **`async`/`await`** | next line after `await` | `catch` block | Ordinary top-to-bottom *inside* the async function |

Both need a Promise. Neither turns `fetch` into a normal `return 42`.

**Activity — Same job, two spellings:**  
Rewrite in one sentence: “`.then` is to fulfilled as `await` is to ____ inside an async function.” Expected: the next line after the wait (and `catch` if it rejects).

You now have timers, Promise states, `.then`/`.catch`, and `async`/`await`. Network asks use the same idea. That is why **`fetch` needs async**.

---

## Why Network Requests Need Asynchronous Code

- **Official Definition:** A **network request** asks another computer for data over the internet (or a local server) and must wait for a reply that may take a long time or fail.
- **In Simple Words:** You phone another office. They may answer in 0.2 seconds, 8 seconds, or never.
- **Real-Life Example:** Loading exam results or a train list. The page cannot know the answer until the other computer speaks.

- **Official Definition:** **`fetch`** is a browser function that **starts** an HTTP request and **returns a Promise**. It does not return the JSON in the same line like `return 42`.
- **In Simple Words:** `fetch` gives you a token, not the packing list yet.
- **Real-Life Example:** You ask for PNR. The clerk says “we have sent the query.” The status arrives later.

**Need:** A server in Mumbai cannot answer as fast as `marks[i] + 1`. If `fetch` were synchronous and blocking, the tab would freeze until the reply — or until the request timed out.

**Logic:** `fetch` is built on Promises. You **`await fetch(...)`** (inside `async`) or use `.then`. Then you often **`await response.json()`**, because turning the body into JSON is *another* later job.

![fetch returns a Promise, not the JSON — page stays usable, fetch starts HTTP, await the envelope, await json, then the value; blocking tab versus non-blocking fetch](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/masterclasses/sessionmc2/sessionmc2-05-fetch-async-pipeline.png?v=20260910)

**Common error:** Writing `const data = fetch(url)` and then using `data.title`. `data` is a **Promise**, not the JSON object.

**Common error:** Using only `await fetch(url)` and forgetting `await response.json()`. The first await is the **response envelope**. The second is the **packing list** inside.

**Common doubt:** “Can I skip Promises and just use `fetch`?”  
`fetch` *is* a Promise. Skipping async means you would have to freeze the clerk. The browser does not let you do that with `fetch`.

`checkPnr` / `payUpi` / `checkResult` are the same shape: start now, finish later, succeed or fail. A real `fetch` adds a URL, HTTP, and JSON. The browser is the right place to practise `fetch` (it needs the network).

Replace the whole of `script.js` with this complete file. Keep Console open. If the request fails, that failure is also a lesson: use `try`/`catch`.

```javascript
async function loadExamCircular() {  // async because we will await fetch and json
  try {  // Happy path — like opening a result / notice from another office
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");  // Start GET; wait for the envelope
    if (!response.ok) {  // HTTP error such as 404 is not always an automatic throw
      throw new Error("HTTP status " + response.status);  // Turn a bad status into a catch
    }  // End of status check
    const data = await response.json();  // Second wait: parse the body as JSON (the packing list)
    console.log("circular title:", data.title);  // Log one field, as if the notice heading arrived
  } catch (err) {  // Network fail, bad JSON, or the throw above
    console.log("office did not answer:", err.message);  // Show a reason in the Console
  }  // End of catch
}  // End of loadExamCircular

loadExamCircular();  // Start the request; the HTML page stays usable (non-blocking)
console.log("query sent to the result office");  // Logs before the title, because fetch is async
```

**How the code works:**

- `fetch` returns a Promise; `await` holds **this function** until the HTTP response arrives
- `response.ok` is false for many HTTP errors; we throw so `catch` can handle them
- `response.json()` returns another Promise; we await that too
- `"query sent to the result office"` appears in the Console **before** `"circular title:"` when the network is slow
- If there is no internet, `catch` logs `office did not answer: ...`

**Activity — Why not a loop?**  
Write two lines: (1) What would happen if the page **blocked** for 10 seconds on a slow result server? (2) Where should `try`/`catch` sit when you `await fetch`? Expected: (1) frozen tab, no clicks; (2) around the awaits, inside the `async` function.

---

## Putting the Pieces in Order

Keep this ladder. Each rung uses the one below.

| Rung | What it is | What you practised in the Console |
|---|---|---|
| 1 | Linked HTML / CSS / JS | Folder `async-lab`, DevTools Console |
| 2 | Synchronous lines | Chai 1, 2, 3 |
| 3 | Later callback | Milk on stove, cut ginger, pour chai |
| 4 | Ticket for later success/fail | Promise **pending / fulfilled / rejected** |
| 5 | Collect the ticket | `.then` / `.catch` |
| 6 | Straight-line later work | `async`/`await` + `try`/`catch` |
| 7 | Network as later work | `fetch` returns a Promise; JSON is a second await |

**Activity — One-line definitions:**  
Without looking up, write one line each for: `script src`, Console, single-threaded, non-blocking, synchronous, `setTimeout`, Promise, `await`, why `fetch` is async.

---

## Key Takeaways

- Run this lesson as **`index.html` + `styles.css` + `script.js`**. Read **`console.log`** in the **browser Console**, then refresh after each save.
- JavaScript is **single-threaded** (one call stack) and still **non-blocking**: timers and `fetch` wait *off* the stack, so the page can keep running.
- **Synchronous** code finishes each line before the next. A slow synchronous wait would **block** the tab.
- **Asynchronous** code **starts** slow work and **continues**. **`setTimeout`** is the smallest demo: milk on the stove, ginger, then pour.
- A **Promise** is **pending**, then **fulfilled** or **rejected**. Use **`.then`/`.catch`** or **`async`/`await`** with **`try`/`catch`**.
- **`fetch`** starts a network request and returns a Promise, so it **must** be used asynchronously. You will use this shape whenever a page asks a server for data.

---

## Important Commands, Libraries, Terminologies Used

| Term / Idea | Meaning (quick revision) |
|---|---|
| **`index.html` / `styles.css` / `script.js`** | Page structure / look / linked JavaScript |
| **`<link rel="stylesheet">`** | Loads the CSS file |
| **`<script src="script.js">`** | Loads the external JS file (place before `</body>`) |
| **Console / `console.log`** | DevTools panel where this lesson’s output appears |
| **Synchronous** | Each statement finishes before the next starts |
| **Asynchronous** | Start now, continue, handle the result later |
| **Single-threaded** | One JS clerk / one call stack in that tab |
| **Non-blocking** | Slow wait happens off the stack; the clerk stays free |
| **Blocking** | Call stack stays busy; the page cannot run other JS |
| **Call stack** | Functions running right now (one main clerk) |
| **Event loop** | After the stack is empty, run later jobs (timers, Promise reactions) |
| **Callback** | A function stored to be called later |
| **`setTimeout`** | Run a callback after at least *n* milliseconds |
| **Millisecond** | `1000` = one second |
| **Promise** | Object for a later success value or failure reason |
| **Pending / fulfilled / rejected** | Not settled / success / failure |
| **`resolve` / `reject`** | Fulfill or fail a `new Promise` |
| **`.then` / `.catch`** | Run on success / run on failure |
| **`async` / `await`** | Function that returns a Promise / pause that function until settle |
| **`try`/`catch`** | Handle thrown errors and rejected `await`s |
| **`fetch` / `response.json()`** | HTTP Promise / second Promise that parses JSON |
| **`response.ok`** | False for many HTTP error statuses |
