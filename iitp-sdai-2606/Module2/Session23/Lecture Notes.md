# Promises Basics & Fetch API – GET Requests

In the previous session, you learned the **client–server** model, the **HTTP** request–response cycle, methods such as **GET**, **status codes**, and **JSON** with `JSON.parse` / `JSON.stringify`.  
Those ideas describe *what* travels on the wire.  
This session answers the next question: **how** does JavaScript wait for that reply without freezing the page, and **how** do you ask a real URL for JSON from the browser?

Think of a Flipkart parcel.  
You place the order now; the packet is not in your hand yet.

The tracking page is a **Promise**: it starts as **pending**, becomes **fulfilled** when the parcel arrives, or **rejected** if the order is cancelled. **`fetch`** is how the browser places that order on the internet.

## What you will learn in this session

- What a **Promise** is, and why async work (timers, network) needs one
- The three states: **pending**, **fulfilled**, **rejected**
- How to wait with **`.then()`** and handle failure with **`.catch()`**
- How **`fetch()`** sends an HTTP **GET** from the browser
- How to read a **Response**, parse **JSON**, check **status**, and show results on the page

## Why a Promise exists

You already know **asynchronous** code from timers: `setTimeout` does not pause the next line.  
A network call is the same idea with a bigger wait: IRCTC may reply in 200 ms or 2 seconds.  
You cannot write “the trains are here” on the next line; you need an object that means **“I will finish later.”**

A Promise is that object.  
The rest of this session is: build one by hand, then use the one **`fetch`** gives you.

- **Promise**  
  - *Official meaning:* A JavaScript object that represents a value that may be available now, later, or never, because an async operation succeeded or failed.  
  - *In simple words:* A token that says “your result is on the way.”  
  - *Real-life example:* A canteen token: you hold the token now; the dosa arrives later, or the counter says “sold out.”
- Need: Callbacks from earlier work for one delay, but two or three waits nested inside each other become hard to read. A Promise gives one object you can attach **success** and **failure** to.
- Logic: The Promise does not store the dosa. It stores the *agreement* that you will be told when the kitchen is done.
- Common doubt: “Is a Promise the data?” No. The data (or the error) arrives when the Promise **settles**.
- A callback is a function you pass in. A Promise is an object you **keep**, then attach `.then` / `.catch` when you are ready to handle the result.
- You can pass that Promise to another function, return it, or chain it. That is awkward with a bare callback.
- Common error: writing the next line as if the dosa were already there. Until `.then` runs, you only have the token, not the food.

## The three states of a Promise

A Promise is like a railway reservation status.  
It is always in **exactly one** of three states.  
After it settles, that state does not change.

![Flipkart-style parcel story in three panels — Processing while the van is still on the road, Delivered at the hostel door, and Transaction declined when the order is cancelled](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session23/session23-01-promise-three-states.png?v=20260818)

- **Pending**  
  - *Official meaning:* The async work has started; neither success nor failure has been recorded yet.  
  - *In simple words:* Still waiting.  
  - *Real-life example:* UPI screen showing “Processing…”
- **Fulfilled** (also called **resolved**)  
  - *Official meaning:* The operation finished successfully; a result value is stored.  
  - *In simple words:* Done — here is the answer.  
  - *Real-life example:* “Payment successful” plus a UTR number.
- **Rejected**  
  - *Official meaning:* The operation failed; a reason (often an `Error`) is stored.  
  - *In simple words:* Failed — here is why.  
  - *Real-life example:* “Transaction declined” plus a bank message.
- **Settle** means “no longer pending” — either fulfilled or rejected.
- Logic: You attach `.then` for fulfilled and `.catch` for rejected. If you attach them while still pending, they simply wait.
- Common error: treating “no reply yet” as failure. Pending is not an error; it is the normal first state.

### Student activity: name the state

Write **pending**, **fulfilled**, or **rejected** for each story:

1. You tapped Search trains; the spinner is still showing.
2. The list of trains appeared.
3. The page shows “No internet” after the request could not leave the laptop.

Check: (1) pending (2) fulfilled (3) rejected.

## Creating a Promise and waiting with `.then()` / `.catch()`

JavaScript builds a Promise with `new Promise(...)`.  
You pass a function that receives **`resolve`** and **`reject`**.  
Call `resolve(value)` to fulfil, or `reject(reason)` to reject.

- **Executor**  
  - *Official meaning:* The function given to `new Promise`; it starts the async work and later calls `resolve` or `reject`.  
  - *In simple words:* The kitchen that will shout “ready” or “sorry.”  
  - *Real-life example:* The canteen cook: work starts when you take the token; later the cook either plates the dosa or says sold out.
- **`.then(successFn)`**  
  - *Official meaning:* Registers a callback that runs with the fulfilled value.  
  - *In simple words:* “When it works, run this.”  
  - *Real-life example:* “When the SMS says delivered, open the parcel.”
- **`.catch(errorFn)`**  
  - *Official meaning:* Registers a callback that runs with the rejection reason.  
  - *In simple words:* “If it fails, run this.”  
  - *Real-life example:* “If the order is cancelled, show the refund message.”
- Need: Without `.catch`, a rejection can become an unhandled error in the console, and the user sees nothing useful on the page.
- `.then` and `.catch` do not start the work. The executor already started. They only **register** what to do after settle.
- Common error: calling `resolve` and then `reject` in the same run. The first settle wins; the second call is ignored.
- You will use `new Promise` to learn the idea. **`fetch` already returns a Promise**, so production GET code usually does not wrap `fetch` in another `new Promise`.

![Hostel canteen token in the student’s hand — the kitchen may plate a dosa for .then or return sold out for .catch, while other students keep sitting](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session23/session23-02-canteen-token-then-catch.png?v=20260818)

### Complete example: a canteen token Promise

This page does not use the internet yet.  
It wraps a **1-second timer** in a Promise so you can see `.then` and `.catch` clearly.  
Change `kitchenOk` to `false` to practise the failure path.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Canteen token Promise</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <h1>Hostel canteen</h1> <!-- Page heading -->
  <p id="status">Token taken — waiting</p> <!-- Shows pending, then result or error -->

  <script> // Starts JavaScript
    const statusEl = document.getElementById("status"); // Selects the paragraph to update
    const kitchenOk = true; // Set to false to practise reject and .catch

    const token = new Promise(function (resolve, reject) { // Creates a Promise; executor runs now
      setTimeout(function () { // Waits 1 second like a slow kitchen
        if (kitchenOk) { // Success path when the kitchen has food
          resolve("Masala dosa is ready"); // Fulfils the Promise with a message string
        } else { // Failure path when the kitchen cannot serve
          reject(new Error("Sold out")); // Rejects the Promise with an Error object
        } // Ends the kitchenOk check
      }, 1000); // Delay is 1000 milliseconds
    }); // Ends new Promise

    token // Starts the chain on the Promise object
      .then(function (message) { // Runs only if resolve was called
        statusEl.textContent = message; // Shows the fulfilled value on the page
      }) // Ends the .then callback
      .catch(function (err) { // Runs only if reject was called
        statusEl.textContent = "Could not serve: " + err.message; // Shows the rejection reason
      }); // Ends the .catch callback
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- The executor runs immediately and starts `setTimeout`. For that one second the Promise is **pending**.
- After 1 second, either `resolve` or `reject` **settles** it. `.then` or `.catch` then updates the paragraph.
- The heading and the first paragraph text appear at once. The page never freezes during the wait.
- You could attach `.then` after a delay and it would still run if the Promise already fulfilled. Late listeners still get the stored value.

### Student activity: flip the kitchen

1. Open the page, wait 1 second, and confirm the dosa message.
2. Set `kitchenOk` to `false`, refresh, and confirm the sold-out message from `.catch`.
3. Set it back to `true` before you continue.

## Promise chains: one wait after another

`.then` itself **returns a new Promise**.  
If the success function **returns a value**, the next `.then` receives that value.  
That is a **chain**: step 1 finishes, then step 2 runs.

- Need: Fetch will need two waits — first the HTTP **Response**, then the parsed **JSON**. A chain is the natural shape.
- Logic: `return` the next piece of data (or the next Promise) from `.then`. Forgetting `return` passes `undefined` to the next step.
- If you `return` a plain string or number, the next `.then` receives that value at once. If you `return` a Promise, the next `.then` waits for it.
- Common error: nesting `.then` inside `.then` like old callbacks. Prefer a flat chain: `.then(...).then(...).catch(...)`.
- One `.catch` at the end can handle a rejection from **any** earlier step in that chain.

![Railway platform where a student collects ticket stubs in order — PNR, then confirmed, then berth allotted — one wait after another](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session23/session23-03-promise-chain-pnr.png?v=20260818)

### Complete example: two-step chain

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Promise chain</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <h1>PNR chain</h1> <!-- Page heading -->
  <p id="out">Working…</p> <!-- Filled after both steps finish -->

  <script> // Starts JavaScript
    const out = document.getElementById("out"); // Selects the result paragraph

    function wait(ms, value) { // Helper: fulfils with value after ms milliseconds
      return new Promise(function (resolve) { // Returns a Promise so it can be chained
        setTimeout(function () { // Schedules the settle
          resolve(value); // Fulfils with the given value
        }, ms); // Uses the delay passed in
      }); // Ends new Promise
    } // Ends wait helper

    wait(400, "PNR 812345") // Step 1: after 400 ms we "have" a PNR string
      .then(function (pnr) { // Receives the fulfilled PNR
        return wait(400, pnr + " — confirmed"); // Step 2: wait again, then pass a longer string
      }) // Ends first .then
      .then(function (text) { // Receives the string from the previous return
        out.textContent = text; // Shows the final text on the page
      }) // Ends second .then
      .catch(function (err) { // Would run if any step rejected
        out.textContent = err.message; // Shows the error if the chain failed
      }); // Ends .catch
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- First `wait` fulfils with `"PNR 812345"`. The first `.then` **returns** another Promise.
- The second `.then` runs only after that second wait. The page shows `PNR 812345 — confirmed`.
- Remove `return` before the second `wait` and the next `.then` gets `undefined`. That is the usual chain bug.

### Student activity: add a third step

1. After `" — confirmed"`, add another `.then` that **returns** `text + " — berth allotted"`.
2. Show that longer string in `#out`.
3. In the first `.then`, `throw new Error("PNR invalid")` instead of returning `wait(...)`. Confirm `.catch` runs and the later `.then` does not.

## Fetch API: GET from the browser

You now have a way to wait.  
**`fetch`** is the browser’s built-in function that sends HTTP and **returns a Promise**.  
For this session you only send **GET**: “please give me this resource.”

![Student at a hostel desk sending a GET postcard while the same webpage stays open — a speed-post envelope comes back; the letter inside is the JSON](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session23/session23-04-fetch-get-envelope.png?v=20260818)

- **Fetch API**  
  - *Official meaning:* A browser interface for HTTP requests; `fetch(url)` returns a Promise that fulfils with a **Response**.  
  - *In simple words:* JavaScript’s way to visit a URL the way the address bar does, then handle the reply in code.  
  - *Real-life example:* Sending a postcard to a college office and getting an envelope back; you still have to **open** the envelope.
- Default method is **GET**. You may write `fetch(url, { method: "GET" })` to be explicit; omitting the second argument still means GET.
- Typing the same URL in the **address bar** also sends GET, but the browser **navigates** and paints a new page. `fetch` stays on **your** page and gives the reply to JavaScript.
- `fetch` is available in Chrome, Edge, Firefox, and other modern browsers. You do not install a library.
- Need: Hard-coding JSON in a variable (previous session) is practice. Real apps load live lists: users, trains, products.
- A **query string** still works: `https://jsonplaceholder.typicode.com/posts?_limit=5` is GET with a filter, the same `?` idea as before.
- Optional: `fetch(url, { method: "GET", headers: { "Accept": "application/json" } })` tells the server you prefer JSON. Many public GET APIs work without this.
- Practice APIs such as JSONPlaceholder are meant to be read from a student page. A random private URL may refuse the browser, and the console then shows `Failed to fetch`.
- Common doubt: “Does `fetch` return the JSON object?” No. It fulfils with a **Response**. Parsing the body is a **second** Promise (`response.json()`).
- Common error: expecting the next line after `fetch(url)` to already hold the data. `fetch` returns a Promise at once; the JSON arrives in `.then`.

Use a practice API so you do not need a login.  
**JSONPlaceholder** (`https://jsonplaceholder.typicode.com`) serves fake users and posts as JSON.  
A useful GET URL is `https://jsonplaceholder.typicode.com/users`.

- **URL parts you will type:** scheme `https://`, host `jsonplaceholder.typicode.com`, path `/users` or `/users/1`, optional query `?_limit=5`.
- `/users` is a **collection** (an array). `/users/1` is **one resource** (one object). The JavaScript you write after parse must match that shape.
- GET should not change server data. You are only **reading**. Creating or updating belongs to other methods you already named; this session stays on GET.

## The Response object and parsing JSON

When the Promise from `fetch` fulfils, you hold a **Response**, not the train list yet.  
The envelope has arrived.  
You still read the stamp (**status**) and open the letter (**body**).

- **Response**  
  - *Official meaning:* The object representing the HTTP response: status, headers, and a body stream.  
  - *In simple words:* The envelope plus the unread letter inside.  
  - *Real-life example:* Speed-post packet: the sticker shows delivered; the invoice is folded inside.
- **`response.status`** — the HTTP status number (`200`, `404`, `500`, …).
- **`response.ok`** — `true` when status is **200–299**, otherwise `false`.
- **`response.headers`** — extra labels on the envelope, such as `Content-Type`. For JSON you often see `application/json`.
- **`response.json()`** — reads the body and parses it as JSON; **returns a Promise** for the JavaScript value.
- Logic: Previous session used `JSON.parse(text)` when you already had a string. With fetch you usually call `response.json()` so the browser reads the body and parses in one step.
- The body is a **stream**. You typically read it **once**. Calling `response.json()` and then `response.text()` on the same Response usually fails.
- Nested JSON is normal. A JSONPlaceholder user has `address.city`. After parse you write `users[0].address.city`, not a guess from the raw string.
- Common error: writing `JSON.parse(response)`. `response` is not a string. Use `response.json()` (or `response.text()` then `JSON.parse`).
- Common error: not **returning** `response.json()` from the first `.then`. The next `.then` receives `undefined`.

### Complete example: GET users and show names

Save this file, open it in the browser, and click **Load users**.  
You need a working internet connection.  
If the page is opened as a `file://` URL and you see “Failed to fetch”, serve the folder with a simple local web server and try again.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Fetch GET users</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <h1>Practice users</h1> <!-- Page heading -->
  <button id="loadBtn">Load users</button> <!-- Starts the GET when clicked -->
  <p id="status">Click the button to fetch</p> <!-- Shows waiting / error text -->
  <ul id="list"></ul> <!-- Filled with user names after JSON is parsed -->

  <script> // Starts JavaScript
    const loadBtn = document.getElementById("loadBtn"); // Selects the button
    const statusEl = document.getElementById("status"); // Selects the status paragraph
    const list = document.getElementById("list"); // Selects the empty list
    const url = "https://jsonplaceholder.typicode.com/users"; // Practice GET endpoint

    loadBtn.addEventListener("click", function () { // Runs fetch only when the user clicks
      statusEl.textContent = "Loading…"; // Shows pending state on the page
      list.innerHTML = ""; // Clears old list items from a previous click

      fetch(url) // Sends HTTP GET; returns a Promise of a Response
        .then(function (response) { // Runs when the Response envelope arrives
          return response.json(); // Starts reading and parsing the JSON body
        }) // Ends first .then; must return the json Promise
        .then(function (users) { // Runs when parsing finishes; users is an array
          statusEl.textContent = "Loaded " + users.length + " users"; // Confirms success
          for (let i = 0; i < users.length; i++) { // Loops through each user object
            const li = document.createElement("li"); // Creates a list item
            li.textContent = users[i].name + " — " + users[i].email; // Uses parsed fields
            list.appendChild(li); // Adds the item to the page
          } // Ends the loop
        }) // Ends second .then
        .catch(function (err) { // Runs on network failure or a throw in the chain
          statusEl.textContent = "Could not load: " + err.message; // Shows a usable error
        }); // Ends .catch
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- Click → `fetch(url)` → Promise **pending** while the request is on the network.
- First `.then` receives the **Response** and **returns** `response.json()`. Second `.then` receives the array.
- Each user object has `name` and `email` (and nested `address`). The loop writes name and email onto the DOM.
- This first fetch example is the **happy path**. It does not yet check `response.ok`. The next topic adds that check so a 404 is not treated as a user list.

### Student activity: one user, not ten

1. Change `url` to `https://jsonplaceholder.typicode.com/users/1`.
2. Click Load. The JSON is now **one object**, not an array. Using `users.length` will be wrong.
3. Show `users.name` and `users.email` in the paragraph (or wrap the object in an array of one) so the page still makes sense.
4. Optional: add `users.address.city` to the text. That field is nested inside `address`.

Check for the list URL: you should see ten names. For `/users/1` you should see one name (Leanne Graham) and must not use `.length` as if it were an array.

## Basic error handling: network vs HTTP

`.catch` does **not** mean “any unhappy status code.”  
**`fetch` rejects mainly on a network problem** (offline, or the request never completed).  
A **404** or **500** still **fulfils** the fetch Promise with a Response, so you must check **`response.ok`** (or `status`) yourself.

![Split scene: Wi-Fi off so no envelope arrives versus an envelope on the desk stamped 404 NOT FOUND — network failure rejects; HTTP errors still arrive and need the stamp checked](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session23/session23-05-network-vs-http-stamp.png?v=20260818)

- Need: If you skip the check, you may call `.json()` on an error body and then treat `{"error":"..."}` as a user list.
- Logic: Envelope can arrive with a red stamp. Arrival is not the same as “the office found your file.”
- **Network error** → Promise **rejected** → `.catch`. The message is often `Failed to fetch`.
- **HTTP 404 / 500** → Promise **fulfilled** → inspect `ok` / `status`, then decide.
- `throw new Error("HTTP " + response.status)` inside `.then` **rejects** the rest of the chain so one `.catch` can handle both network and HTTP problems.
- Common error: showing “Server down” for every failure. `404` means the path or id was not found. `Failed to fetch` often means the request never completed.

### Complete example: check `ok` before trusting JSON

JSONPlaceholder returns **404** for a missing user id such as `/users/999`.  
This page fetches that URL on purpose so you can see the stamp.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Fetch error handling</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <h1>User lookup</h1> <!-- Page heading -->
  <button id="goBtn">Fetch user 999</button> <!-- Triggers the GET -->
  <p id="out">Click to try a missing id</p> <!-- Status or parsed name -->

  <script> // Starts JavaScript
    const goBtn = document.getElementById("goBtn"); // Selects the button
    const out = document.getElementById("out"); // Selects the result paragraph
    const url = "https://jsonplaceholder.typicode.com/users/999"; // GET that should be 404

    goBtn.addEventListener("click", function () { // Starts the request on click
      out.textContent = "Loading…"; // Shows pending on the page

      fetch(url) // Sends GET; network success still fulfils even if status is 404
        .then(function (response) { // Receives the Response envelope
          if (!response.ok) { // Treats any non-2xx status as a problem
            throw new Error("HTTP " + response.status); // Rejects the chain so .catch runs
          } // Ends the ok check
          return response.json(); // Parses JSON only after a successful status
        }) // Ends first .then
        .then(function (user) { // Runs only when ok was true and JSON parsed
          out.textContent = user.name; // Would show the name for a real user
        }) // Ends second .then
        .catch(function (err) { // Catches network errors and the thrown HTTP error
          out.textContent = "Lookup failed: " + err.message; // Shows HTTP 404 or a network message
        }); // Ends .catch
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `fetch` fulfils for `/users/999` because the server answered. `response.ok` is `false` and `status` is `404`.
- `throw new Error("HTTP 404")` turns that into a rejection so the existing `.catch` can update the page.
- Change the path to `/users/1`, click again, and you should see a name such as `Leanne Graham`.
- The same `.catch` also handles offline mode. You do not need two different catch blocks for this pattern.

### Student activity: compare two URLs

1. Run the page with `/users/999`. Confirm the message includes `HTTP 404`.
2. Change only the URL to `/users/1`. Confirm a name appears.
3. Turn on airplane mode (or unplug Wi-Fi), click again, and note that `.catch` now shows a **network** style message, not `HTTP 404`.

## Hands-on: fetch, parse, and display

Put the pieces in one flow you can reuse.  
**GET** → wait for **Response** → check **ok** → **`json()`** → loop → **DOM**.  
The practice API is still JSONPlaceholder; the pattern is the same for any JSON GET.

- Click should set a **Loading…** message so pending is visible.
- Optional: set `button.disabled = true` at the start of the click and set it back to `false` in both the success `.then` and `.catch`, so a double-click does not fire two GETs.
- Empty the list before filling it, or old rows stack up.
- Use `createElement` / `appendChild` (or `textContent` for one record) so the user sees data on the page, not only in the console.
- Keep `.catch` on the chain so a failed GET does not fail silently.
- Check `response.ok` before `json()`, then loop fields such as `name`, `email`, or `title`.
- Open **DevTools → Network**, click Load, and find the `users` row: method **GET**, status **200**, type **json**. That is the same trace you practised conceptually in the previous session, now triggered by JavaScript.
- In that row, open **Headers** and **Preview** (or **Response**). Headers show status and `Content-Type`; Preview shows the parsed JSON the same way your `.then` sees it after `json()`.

### Student activity: posts instead of users

1. Point `fetch` at `https://jsonplaceholder.typicode.com/posts?_limit=5`.
2. Each item has `id` and `title`. Show `id + ": " + title` in the list.
3. Confirm Network shows **GET** and **200**, then break the path (`/missing`) and confirm your `ok` check plus `.catch` still explain the failure.

Check: five list items such as `1: sunt aut facere...`; Network method is GET; `/missing` should not look like a post list.

## Putting Promises and GET together

A Promise is the waiting tool.  
`fetch` is the GET tool.  
JSON parse and the DOM are how the user sees the answer.

- **Pending** while the request travels; **fulfilled** with a Response; **rejected** on network failure.
- Always **return** `response.json()` so the next `.then` receives real data.
- Always read **status / ok** before you treat the body as the list you wanted.
- Match the JSON **shape**: an array needs a loop; a single object needs `user.name`, not `users[0]` unless you wrapped it.
- `.then` / `.catch` replace “freeze the page until the trains arrive.” The rest of the UI stays usable.
- If the UI is blank, check three places: the URL, `ok` / status in Network, and whether you returned `json()`.

## Key Takeaways

- A **Promise** is a later result: **pending**, then **fulfilled** or **rejected**.
- **`.then()`** runs on success; **`.catch()`** runs on failure; chains pass values with **`return`**.
- **`fetch(url)`** sends **GET** and fulfils with a **Response**, not with JSON yet.
- **`response.json()`** is a second Promise; check **`response.ok`** because HTTP errors do not auto-reject `fetch`.
- Show **Loading…**, then render parsed fields in the **DOM**, and keep a **`.catch`** for network problems.

`console.log` is for you while learning. Users need **text on the page**. If Network shows 200 but the list is empty, your loop or field names (`name` vs `title`) are the first place to look.

In an upcoming session, you will reuse this same GET-and-display flow on fuller frontend pages — still reading **status** first, then unpacking **JSON**.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| Promise | Object for a value that arrives later |
| Pending | Not settled yet (spinner / “Processing”) |
| Fulfilled / resolved | Success; value is ready |
| Rejected | Failure; reason is ready |
| Settle | No longer pending (fulfilled or rejected) |
| `new Promise(executor)` | Create a Promise; call `resolve` / `reject` |
| `resolve(value)` | Fulfil with `value` |
| `reject(reason)` | Reject with `reason` |
| `.then(fn)` | Run `fn` with the fulfilled value |
| `.catch(fn)` | Run `fn` with the rejection reason |
| Promise chain | `.then().then().catch()` with `return` |
| Fetch API | Browser HTTP helper |
| `fetch(url)` | GET `url`; Promise of a **Response** |
| Response | Status + headers + body (the envelope) |
| `response.status` | e.g. `200`, `404`, `500` |
| `response.ok` | `true` if status is 200–299 |
| `response.json()` | Read body and parse JSON (returns a Promise) |
| `response.text()` | Read body as a string (returns a Promise) |
| JSONPlaceholder | Practice API, e.g. `/users` |
| Collection vs resource | `/users` is an array; `/users/1` is one object |
| Query string | Filters after `?`, e.g. `posts?_limit=5` |
| `{ method: "GET" }` | Optional fetch options; GET is the default |
| `Accept` header | Tells the server you prefer JSON |
| `application/json` | Typical `Content-Type` for a JSON body |
| Network error | `fetch` rejects (offline, request never completed) |
| HTTP error | Response arrived but `ok` is false |
| DevTools Network | Inspect GET, status, and JSON payload |
| Headers / Preview | Status and `Content-Type`; parsed JSON view |
| `button.disabled` | Block extra clicks while a GET is pending |
| Nested field | e.g. `user.address.city` after parse |
| `Failed to fetch` | Typical message when the request never completed |
