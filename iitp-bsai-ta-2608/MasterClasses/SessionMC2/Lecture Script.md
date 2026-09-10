# Lecture Script: Masterclass: Asynchronous JavaScript

**Session duration:** 1 hour 50 minutes  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**How to use this file:** This document is for **timing and facilitation only**. It is not a transcript or textbook. Use the numbered blocks to pace the room, manage screen-shares, check student screens, and trigger participation. Definitions, analogies, full code, tables, and activities live in **Lecture Notes.md** — share that with students and skim headings aloud rather than reading every bullet.

**Break rule:** After **roughly 55–65 minutes** of session clock time (after the **event loop** segment), take **one** pause of **5–8 minutes**, then continue. Do **not** list the break as a numbered block.

**Lab rule for every demo:** Students keep the same `async-lab` folder. **`index.html` and `styles.css` stay.** Only **`script.js` is replaced** as a whole file. Lesson output is **`console.log` in the browser Console** — not text on the page, not One Compiler.

---

## 1. Welcome, Why Later Work, and Session Arc (5 minutes)

- Welcome the cohort; frame this as a **browser masterclass** — how JavaScript keeps a page alive while slow work finishes **later**.
- One-line hook from notes: a `for` loop of five marks finishes in a blink; a **PNR check** cannot. If JS waited for PNR the same way it waits for the next loop line, the tab would **freeze**.
- State outcomes in plain language: **sync vs async**; **single-threaded but non-blocking**; **`setTimeout`**; **Promise** states; **`.then` / `.catch`**; **`async`/`await`** with **`try`/`catch`**; why **`fetch`** must be async — **before** they treat a network call like `return 42`.
- **Room action:** Ask everyone to open **Lecture Notes** for this masterclass and a blank folder on their computer (they will create `async-lab` next). Confirm they can see the session images.
- **Engagement — cold-call (2 students):** "Name one thing on your phone that would feel broken if the screen froze for 10 seconds while it waited." (UPI, IRCTC, result portal.)
- **Engagement — thumbs up:** Lecture Notes are open.

**Bridge sentence:** "The print order in the Console *is* the lesson — so we first build a tiny lab that can actually talk to the browser."

---

## 2. Build the Lab — HTML, CSS, Linked JS, Console (12 minutes)

- Screen-share the **lab setup** image (`sessionmc2-01-html-css-js-console.png`). Point: three files, one folder, output in **DevTools Console**.
- **Room action:** Students create a folder named `async-lab`. Same folder: `index.html`, `styles.css`, `script.js`.
- Live-type or paste the **starter HTML and CSS** from notes. Stress `<script src="script.js">` **before** `</body>`, and `<link rel="stylesheet" href="styles.css">` in `<head>`.
- First `script.js` can be a one-liner for the smoke test: `console.log("lab ready");` — they will replace the whole file in the next block.
- **How to open Console:** F12, or Ctrl+Shift+J (Windows), or Cmd+Option+J (Mac), or right-click → Inspect → Console. Double-click `index.html` in Chrome or Edge.
- **Circulate / spot-check screens:** white page with heading is fine; they must also have the Console panel open.
- **Common error (30 sec):** looking only at the page; **`script.js` in a different folder** → 404, nothing logs.
- **Engagement — thumbs up:** everyone sees `lab ready` (or any first log) in the Console after refresh.
- **Cold-call (1 student):** "After you save `script.js`, what do you do next?" (Refresh the page.)

**Bridge sentence:** "The lab is a browser tab with one clerk — next we watch that clerk finish three fast jobs in strict order."

---

## 3. Synchronous Execution — Chai in Order (7 minutes)

- Define **synchronous** in one sentence: each statement finishes before the next starts, on one **call stack**.
- Clerk / photocopy analogy in 20 seconds. **Call stack** = plates; top plate must finish first.
- **Room action:** Replace the **whole** of `script.js` with the three chai `console.log` lines from notes. Save, refresh, watch Console.
- **Engagement — activity: Predict sync order (2 min):** Before refresh, students write the three steps on paper. Then refresh. Expected: boil water → tea leaves → pour.
- **Cold-call (1 student):** "Was anything saved for later?" (No.)
- **Check for understanding (20 sec):** "If line 2 is slow, when does line 3 start?" (Only after line 2 finishes.)

**Bridge sentence:** "Three chai steps are honest — the problem starts when one job is slow, like a PNR phone call, and the clerk locks the whole window."

---

## 4. Blocking, One Thread, Still Non-Blocking (10 minutes)

- Token-window story: counting three tokens is fast; calling another city for **PNR** is slow. If the clerk stops the queue, the page feels **frozen**.
- Define **blocking** in one sentence. UPI that would not let you tap Cancel for 20 seconds.
- **Common error (30 sec):** an empty `for` loop that spins for two seconds still **blocks** — the clerk is busy counting.
- Screen-share the **one thread, still non-blocking** image (`sessionmc2-02-call-stack-event-loop.png`). Point to four stations: **Call Stack**, **Web APIs**, **Event Loop**, **Callback Queue**.
- Define **single-threaded**: one call stack; one JS instruction at a time. Not two clerks.
- Define **non-blocking**: start the slow wait, leave the stack free, come back later. Milk on the stove; next customer served.
- Flash the three-row table: single-threaded / blocking / non-blocking.
- **Common doubt (1 min):** "If there is only one thread, how can C run later while B already ran?" B ran on the thread; the wait was **off** the stack. Clicks are later jobs on the **same** thread — not multi-threaded JS.
- **Engagement — activity: One sentence (1 min):** Chat fill-in: "JavaScript is ____-threaded, but timers are ____-blocking." Reveal: **single**, **non**.
- **Pair-share (1 min):** Partner A says single-threaded; partner B says non-blocking — in one line each.

**Bridge sentence:** "You now have the two words people mix up — next we prove non-blocking with the smallest browser timer: `setTimeout`."

---

## 5. setTimeout — A, Then B, Then C (12 minutes)

- One-line async: start slow work, continue, handle the result **later**. Callback = "when the milk boils, call me."
- Define **`setTimeout`**: run a callback after **at least** *n* milliseconds. `1000` = 1 second; `2000` = 2 seconds.
- **Logic:** `setTimeout` does **not** pause the next line. It only **registers** the callback.
- **Room action:** Students replace the **whole** `script.js` with the milk / ginger / pour demo from notes. Console open. Refresh.
- **Engagement — activity: Predict the timer (3 min):** On paper, write A, B, C in print order **before** they see C appear. Circulate. Expected: **A, B, then C** — never A, C, B.
- Screen-share the **chai order** image (`sessionmc2-03-settimeout-chai-order.png`). Point to PRINT ORDER vs the crossed-out Never.
- Wait the two seconds live so the room hears the pause. Then show C.
- **Common error (30 sec):** expecting the script to sleep at `setTimeout` so B prints after C. That would be a blocking sleep.
- **Optional 1 min if time:** change `2000` to `0`, save, refresh. Still A, B, then C — later means after the current stack is clear.
- **Thumbs up:** Console shows A, then B, then C.

**Bridge sentence:** "Zero delay still putting C after B is not a bug — that rule has a name: the event loop."

---

## 6. The Event Loop — Stack Empty, Then the Queue (8 minutes)

- Define **event loop** in one sentence: run the call stack to empty, then pick up **later** jobs (timers, Promise reactions, clicks).
- Screen-share the **typical event loop** image (`sessionmc2-06-js-event-loop.png`). Walk the three arrows only: (1) hand timer to Web APIs, (2) timer done → C joins **Callback Queue**, (3) stack empty → move C onto the stack.
- Flash the now-vs-later table from notes: Now = A, register, B. Later = C.
- **Need / logic (30 sec):** without this picture, `setTimeout(..., 0)` looks broken. Zero still means *later queue*, not *this line*.
- **Cold-call (1 student):** "Where does the two-second wait live — on the call stack, or in Web APIs?" (Web APIs.)
- **Check for understanding (20 sec):** "Does the event loop run C while `console.log B` is still on the stack?" (No.)

**→ Take the single break (5–8 minutes) here if you have hit ~55–65 minutes. Optional return prompt: "After break — a ticket that can succeed or fail: Promises." ←**

**Bridge sentence:** "A timer is one later job with no fail path in our demo — real products need a ticket that can become success or failure. That ticket is a Promise."

---

## 7. Promise States — Pending, Fulfilled, Rejected (10 minutes)

- Define **Promise** in one sentence: a value that may be available now, later, or never; it settles into success or failure. IRCTC booking: in progress, then confirmed or failed.
- Screen-share the **Promise states** image (`sessionmc2-04-promise-states.png`). Pending in the middle; **resolve** / `.then` left; **reject** / `.catch` right. After it settles, it **does not go back**.
- Flash the three-row chai-stall table: pending / fulfilled / rejected.
- **Room action:** Replace whole `script.js` with **`checkPnr`** from notes. Refresh. Point at the Console: "Before PNR check" and "After calling checkPnr" print **now**; `ticket` logs as a **Promise object**, still pending.
- **Common error (30 sec):** `console.log(thePromise)` too early is the object, not the later seat string. You do not write `if (promise === true)`.
- **Engagement — activity: Name the state (3 min):** Students write pending / fulfilled / rejected for: (1) just after `checkPnr("1234567890")`, (2) after 1 second on a valid PNR, (3) immediately after `checkPnr("")`. Reveal: pending, fulfilled, rejected.
- **Cold-call (1 student):** Read state (3) and why (empty PNR rejects **now**, no timer).

**Bridge sentence:** "You have a ticket — next you collect the confirmation with `.then` and hear bad news with `.catch`."

---

## 8. then and catch — UPI Success and Wrong PIN (12 minutes)

- Define **`.then`** / **`.catch`** in one breath: fulfilled → `.then`; rejected → `.catch`. SMS "ticket confirmed" vs "payment failed."
- **Room action:** Replace whole `script.js` with **`payUpi`** from notes. Console open. Refresh.
- Narrate expected order **before** the 800 ms success lands: **1. start payment**, **2. still using the app**, **4. caught** (wrong PIN, now), then **3. success**.
- Wait live for the success line. Tick the order on a board if you can.
- **Common error (30 sec):** forgetting `.catch` → unhandled rejection in the Console.
- **Common doubt (20 sec):** you *can* use `.then` without `.catch`, but failures are easy to miss — pair them while learning.
- **Engagement — activity: Two outcomes on paper (3 min):** Two boxes — fulfilled / rejected. Under fulfilled: `payUpi(true)` message. Under rejected: `payUpi(false)` message. Circulate.
- **Thumbs up:** Console shows 1, 2, 4, then 3.

**Bridge sentence:** "`.then` and `.catch` work — for several steps they still look nested. `async`/`await` is the same machine in straighter lines."

---

## 9. async / await with try / catch — Result Portal (12 minutes)

- Define **`async` function** + **`await`**: the function always returns a Promise; `await` pauses **that function** until settle — **without locking the whole page**.
- Chai-stall token: you wait for *your* cup; other customers still order.
- **Common error (30 sec):** `await` outside `async` in beginner scripts. `console.log(openPortal())` logs a Promise, not the marksheet.
- **Room action:** Replace whole `script.js` with **`checkResult` / `openPortal`** from notes. Refresh.
- Predicted order on board: `before calling openPortal`, **A**, **B**, then later **C**, **D**, **E**. Stress: **B** ("you can still scroll") prints while the portal is waiting — `await` did not freeze the tab.
- Walk `try`/`catch`: happy `await checkResult("roll-12")` → C; blank roll rejects → D; then E.
- Flash the comparison table: `.then`/`.catch` vs `async`/`await` — two spellings of the same wait.
- **Engagement — activity: Trace async/await (3 min):** Students number before, A, B, C, D, E on paper, then tick the Console. If anyone has C before B, they still think `await` blocks the page.
- **Cold-call (1 student):** "`.then` is to fulfilled as `await` is to ____ inside an async function." (The next line after the wait; `catch` if it rejects.)
- **Pair-share (1 min):** "Can you still scroll the HTML page while C is pending?" (Yes.)

**Bridge sentence:** "Timers and Promises were practice — a real server ask uses the same shape. That is why `fetch` cannot be a normal `return`."

---

## 10. Why fetch Must Be Asynchronous (10 minutes)

- Define **network request** in one sentence: ask another computer; reply may be slow or fail. Exam results / train list.
- Define **`fetch`**: starts HTTP, **returns a Promise**, does **not** return JSON on the same line like `return 42`. Token, not packing list.
- **Need:** a server in another city is not `marks[i] + 1`. Blocking `fetch` would freeze the tab.
- Screen-share the **fetch pipeline** image (`sessionmc2-05-fetch-async-pipeline.png`). Walk: page stays usable → `fetch` → `await response` (envelope) → `await response.json()` (packing list) → `data.title`. Point at the frozen-tab vs non-blocking strip.
- **Two common errors (1 min):** `const data = fetch(url)` then `data.title`; and `await fetch` without `await response.json()`.
- **Room action:** Replace whole `script.js` with **`loadExamCircular`**. Console open. Refresh. `"query sent to the result office"` should appear **before** `"circular title:"` if the network is slow. If offline, `catch` is the lesson — do not panic.
- **Engagement — activity: Why not a loop? (2 min):** Students write two lines: (1) what if the page blocked 10 seconds on a slow result server? (2) where does `try`/`catch` sit? Reveal: frozen tab; around the awaits, inside the `async` function.
- **Thumbs up:** they saw either the title or a caught network error — both count.

**Bridge sentence:** "If you can say why `fetch` returns a Promise, you are ready to lock today's ladder."

---

## 11. Key Takeaways and Close (4 minutes)

- Flash the **Putting the Pieces in Order** ladder from notes — seven rungs, one breath each. Do not re-teach.
- Flash **Key Takeaways**; read once: lab trio + Console; single-threaded and non-blocking; sync vs async; Promise states; `fetch` must be async.
- Point to the **terminology table** for revision.
- **Exit ticket — cold-call (2 students):** "JavaScript is ____-threaded, but `setTimeout` is ____-blocking."
- **Exit ticket — cold-call (1 student):** "Why can't `const data = fetch(url)` give you `data.title` immediately?" (Because `fetch` returns a Promise, not the JSON.)
- Thank the cohort. Remind them: keep `async-lab`; replace only `script.js`; answers live in the **Console**.

**Bridge sentence:** "Start the slow job, keep the page alive, collect success or failure later — that is asynchronous JavaScript."

---

## Timing Flex

If the session is running late, cut in this order (keep the core path intact):

1. **Shorten Block 1:** Skip the second cold-call; keep PNR-vs-loop hook and outcomes only.
2. **Shorten Block 3:** Skip paper predict; run the three chai logs and move on.
3. **Shorten Block 4:** Skip pair-share; keep the image + fill-in sentence.
4. **Shorten Block 5:** Skip the `2000` → `0` experiment; keep A, B, then C live.
5. **Shorten Block 8:** Skip the paper boxes; keep live UPI order 1, 2, 4, then 3.
6. **Shorten Block 9:** Skip pair-share and the one-sentence rewrite; keep the live `openPortal` trace.
7. **Shorten Block 10:** If the network is slow or blocked, do not wait — walk the image and the two common errors; assign the `fetch` file as take-home.
8. **Do not cut** Blocks **2**, **5** (core A-B-C), **7** (three states), and **9** (await does not freeze B) — lab + timer + Promise + `async`/`await` are the masterclass spine. Keep a **minimum** of `fetch` as "same shape, real network" even if you only screen-share the pipeline image.
9. If you finish **5+ minutes early:** chat poll — "Will `setTimeout(..., 0)` print C before B?" — then one volunteer changes the delay live. Or let students retry `fetch` and paste `circular title` or the catch message in chat.
