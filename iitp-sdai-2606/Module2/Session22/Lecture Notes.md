# Client-Server Model, HTTP & JSON

In the previous session, you learned **asynchronous JavaScript**: synchronous vs asynchronous execution, callbacks, `setTimeout`, `setInterval`, and updating the DOM after a delay.  
Those skills keep the page usable while something finishes later.  
This session answers the next question: **who** is the page waiting for, and **what** travels between your browser and a computer somewhere else?

Think of IRCTC.  
You sit at home (the **client**) and tap “Search trains.”

A computer in a data centre (the **server**) checks seats and sends back a list. The back-and-forth is the **request–response cycle**, and the common language is **HTTP** plus **JSON**.

## What you will learn in this session

- How the **web** is built on a **client–server** model
- How a **request** leaves the browser and a **response** comes back
- How **HTTP methods** (`GET`, `POST`, `PUT`, `DELETE`) and **status codes** describe the job and the result
- How **JSON** stores structured data, and how JavaScript **parses** and **stringifies** it
- How to **trace** what happens when you visit a URL

## How the web works

A website is not one file sitting only on your laptop.  
Your browser shows a page, but the **data** (train list, cart, marks) often lives on another machine.  
The web is a conversation: one side asks, the other side answers.

- **Web architecture**  
  - *Official meaning:* The arrangement of browsers, servers, and the rules they use to exchange information.  
  - *In simple words:* Who talks to whom, and in what format.  
  - *Real-life example:* A college office: you (student) submit a form; the clerk’s computer holds the records.
- Need: If every train timetable lived only on each student’s phone, IRCTC could never stay up to date. One **server** holds the truth; many **clients** ask for it.
- Common doubt: “Is the page I see the server?” No. The page is what the **client** (browser) built after the server sent files or data.

## Client and server

Once you see two roles, the rest of HTTP becomes easier.  
One role **asks**. The other role **serves**.

![Student searching trains on a laptop at home versus railway computers in a booking office — the client asks; the server holds the records and answers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session22/session22-01-client-server-irctc.png?v=20260818)

- **Client**  
  - *Official meaning:* A program that starts a request for a resource.  
  - *In simple words:* The side that says “please give me this.”  
  - *Real-life example:* You at a railway counter, or the Swiggy app on your phone.
- **Server**  
  - *Official meaning:* A program that listens for requests, does work, and sends a response.  
  - *In simple words:* The kitchen that receives the order slip and sends the plate.  
  - *Real-life example:* IRCTC’s computers, or the college exam cell that prints your hall ticket.
- A **browser** (Chrome, Edge, Firefox) is a client. A **mobile app** can also be a client. The server does not have to be in the same city as you.
- **Resource**  
  - *Official meaning:* A thing the server exposes at a path, such as a page, an image, or a train record.  
  - *In simple words:* The “file” or “record” you are asking about.  
  - *Real-life example:* `/trains` is the trains counter; `/trains/12951` might be one train.
- Logic: The client never “guesses” the full train list. It **requests**. The server never “paints” your screen; it **responds**.
- Your JavaScript and HTML turn that response into UI.

### Student activity: name the two sides

1. Pick one app you used today (UPI, Gmail, or a shopping site).
2. Write one line: **Client = …** and **Server = …**
3. Write one thing the client asks for (balance, inbox, product list).

## The request–response cycle

A **cycle** is one complete round trip. The client sends a **request**; the server sends a **response**. Then the client can ask again.

![Order slip GET /trains leaving a laptop and a stamped 200 train list coming back from the railway office — one request goes out; one response returns](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session22/session22-02-request-response-cycle.png?v=20260818)

- **Request**  
  - *Official meaning:* The message the client sends: what resource, which method, and optional data.  
  - *In simple words:* The order slip.  
  - *Real-life example:* “Show trains from Pune to Nagpur on 20 Aug.”
- **Response**  
  - *Official meaning:* The message the server sends back: a **status code** plus a **body** (HTML, JSON, or empty).  
  - *In simple words:* The plate that comes back—food, or a note “item not available.”
- Typical steps:
  - You type a URL or click a button.
  - The browser builds an HTTP request.
  - The request travels to the server.
  - The server reads the method and path, does work (search, save, delete).
  - The server sends an HTTP response.
  - The browser reads the status and body, then updates the page.
- This wait is **asynchronous** for the user: you can still scroll while the reply is on the way. That is why the previous session’s “do not freeze the page” idea matters here.
- Common error: thinking one page load is “just HTML.” The first response may be HTML, then the browser may send **more requests** for CSS, JavaScript files, and images.

### Student activity: order-slip story

1. Write four boxes on paper: **You → Browser → Server → Browser**.
2. Label the arrows: **request** going right, **response** coming left.
3. In the request box write `GET /trains`. In the response box write `200` and `[{ "train": "Duronto" }]` as a **data** packing list (not the HTML page).

## Tracing what happens when you visit a URL

Open a new tab and type a site address.  
That one action is not magic. It is a **traceable** path.

- **URL (Uniform Resource Locator)**  
  - *Official meaning:* The address of a resource on the web.  
  - *In simple words:* The full house address, not just the city name.  
  - *Real-life example:* `https://www.irctc.co.in/nget/train-search` is like “building + floor + room.”
- Pieces you should recognise:
  - **Scheme:** `https://` means “use HTTP, but encrypted.”
  - **Host:** `www.irctc.co.in` — which computer (via DNS, a phone-book for names).
  - **Path:** `/nget/train-search` — which “counter” or page on that computer.
  - **Query string:** the part after `?`, such as `from=Pune&to=Nagpur`. It is still on the **request**, but it is not the path. It filters or extra-describes the resource.
- Trace for a first visit:
  - You press Enter.
  - The browser resolves the host name to find the server.
  - It sends `GET` for that path (often `/` for the home page).
  - The server responds with status `200` and an HTML body (if the page exists).
  - The browser parses HTML, then may request CSS, JavaScript, and images—each is another cycle.
- **DevTools Network tab:** Right click the page → **Inspect** → **Network**, then reload. The first row is often the **document**; columns show **method**, **status**, and **type**.
- Common doubt: “Why so many rows for one site?” Because one page is many files. Each file is its own request–response pair.

### Student activity: read one network row

1. Open any public site you are allowed to use in class.
2. Open **Inspect → Network**, reload, and click the first **document** row.
3. Note **method** (usually `GET`), **status** (often `200`), and the **path**. Write those three on paper.

## HTTP: the language of the request

**HTTP** is the agreed format of that conversation.  
Without a shared format, the server would not know if you wanted to *read* a ticket or *cancel* it.

- **HTTP (Hypertext Transfer Protocol)**  
  - *Official meaning:* The application protocol browsers and servers use to transfer resources.  
  - *In simple words:* The grammar of web messages.  
  - *Real-life example:* The printed format of a money-order form—everyone fills the same boxes.
- **HTTPS** is HTTP sent through an encrypted tunnel. Same methods and status codes; safer on public Wi-Fi.
- A request has:
  - A **start line:** method + path + HTTP version (example: `GET /trains HTTP/1.1`).
  - **Headers:** extra labels (`Host`, `Accept`, `Content-Type`).
  - An optional **body:** data for `POST` or `PUT` (often JSON). `GET` and `DELETE` usually have no body.
- Headers you will see often:
  - **`Host`:** which site this request is for (required on modern HTTP).
  - **`Content-Type`:** the format of the body (`application/json` or `text/html`).
  - **`Accept`:** what format the client hopes to receive.
- A response has:
  - A **status line:** version + **status code** + short phrase (`HTTP/1.1 200 OK`).
  - **Headers:** (`Content-Type: application/json`).
  - A **body:** the HTML page or the JSON data.

### Complete example: request and response as JavaScript objects

This page does **not** call a real server. It shows the **shape** of one cycle so you can read it in the console.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document and sets language to English -->
<head> <!-- Holds metadata and the page title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding so Indian names display correctly -->
  <title>HTTP Message Shape</title> <!-- Shows the tab title in the browser -->
</head> <!-- Ends the head section -->
<body> <!-- Starts the visible page content -->
  <p>Open the console (Right click → Inspect → Console).</p> <!-- Tells you where the logs appear -->

  <script> // Starts the JavaScript section
    const request = { // Builds an object that models one HTTP request
      method: "GET", // Names the HTTP method: read data, do not change the server
      path: "/trains", // Names the resource path the server should handle
      headers: { // Groups request headers in a nested object
        Accept: "application/json" // Tells the server the client prefers JSON
      } // Ends the headers object
    }; // Ends the request object

    const response = { // Builds an object that models one HTTP response
      status: 200, // Stores the numeric status code meaning success
      headers: { // Groups response headers
        "Content-Type": "application/json" // Tells the client the body is JSON text
      }, // Ends the headers object
      body: '[{"train":"Duronto","from":"Pune"}]' // Stores the body as a JSON string, as the network would
    }; // Ends the response object

    console.log("REQUEST", request.method, request.path); // Prints the method and path of the request
    console.log("RESPONSE status", response.status); // Prints the status code of the response
    const trains = JSON.parse(response.body); // Converts the JSON string into a real JavaScript array
    console.log("First train", trains[0].train); // Reads one field after parsing
  </script> <!-- Ends the JavaScript section -->
</body> <!-- Ends the body -->
</html> <!-- Ends the HTML document -->
```

**How the code works**

- `request` and `response` are teaching models. Real HTTP is text on the network; JavaScript objects help you see the parts.
- `response.body` is a **string**. You cannot write `response.body[0].train` until you **parse**.
- `JSON.parse` turns the string into an array of objects. Then `trains[0].train` is `"Duronto"`.
- This models a **data** cycle (JSON body). Typing a URL in the address bar is usually a **page** cycle (HTML body). Both use the same HTTP parts.

## HTTP methods: the verb on the order slip

The **path** says *which* resource. The **method** says *what to do* with it.

Four methods cover most beginner work. They map to **CRUD**: Create, Read, Update, Delete.

![Four railway ticket counters labelled GET show me, POST add a new one, PUT replace fully, and DELETE remove this — same office, four different jobs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session22/session22-03-http-methods-counter.png?v=20260818)

- **GET**  
  - *Official meaning:* Retrieve a representation of a resource. Should not change server data.  
  - *In simple words:* “Show me.”  
  - *Real-life example:* Opening your UPI passbook to **see** the balance.
- **POST**  
  - *Official meaning:* Submit data to create a resource or trigger processing.  
  - *In simple words:* “Add a new one.”  
  - *Real-life example:* Submitting a new IRCTC ticket booking.
- **PUT**  
  - *Official meaning:* Replace an existing resource with the data you send.  
  - *In simple words:* “Overwrite this record with this full new version.”  
  - *Real-life example:* Updating your delivery address by sending the complete address again.
- **DELETE**  
  - *Official meaning:* Remove the named resource.  
  - *In simple words:* “Remove this.”  
  - *Real-life example:* Cancelling a saved UPI beneficiary.
- Logic: Same path, different method, different job. `GET /orders/12` reads order 12; `DELETE /orders/12` removes it.
- Mixing those methods is a common production bug.
- Common error: using `GET` to delete “because it is easier to type in the address bar.” `GET` can be cached or prefetched. Changing data belongs on `POST`, `PUT`, or `DELETE`.

### Student activity: pick the method

For each action, write `GET`, `POST`, `PUT`, or `DELETE`:

1. Load the list of trains for a date.
2. Book a new ticket.
3. Replace the passenger mobile number on an existing booking (full passenger object sent).
4. Cancel that booking.

Check: (1) `GET` (2) `POST` (3) `PUT` (4) `DELETE`.

## Status codes: the result stamp

After the server finishes, it stamps the response with a **number**.  
Your JavaScript should read that number before trusting the body.

![College exam cell stamping files 200 success, 201 created, 404 not found, and 500 printer jammed — status codes are the result stamp on the reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session22/session22-04-status-stamps-exam-cell.png?v=20260818)

- **HTTP status code**  
  - *Official meaning:* A three-digit code on the response that classifies success, redirection, client error, or server error.  
  - *In simple words:* The rubber stamp on the file: approved, missing, or office error.  
  - *Real-life example:* Exam cell: 200 = marksheet printed; 404 = roll number not found; 500 = printer jammed.
- Families (remember the first digit):
  - **2xx success:** `200 OK` (found and sent), `201 Created` (new resource made, typical after `POST`).
  - **3xx redirect:** “Look somewhere else” (the browser often follows this for you).
  - **4xx client error:** The request was wrong or not allowed. `400` bad input, `401` not logged in, `403` logged in but forbidden, `404` no such resource.
  - **401 vs 403:** `401` is “who are you?” (no valid login). `403` is “we know you, but this counter is not for you” (student portal vs admin portal).
  - **5xx server error:** The server failed. `500` is the generic “something broke on our side.”
- Logic: A `404` is still a completed HTTP cycle. The network worked; the path did not match a resource.
- That is different from “no internet.”
- Common error: showing “Server down” for every failure. `404` means “this id does not exist.” `500` means “try again or contact support.”

### Student activity: match the stamp

Match each story to a code (`200`, `201`, `400`, `404`, `500`):

1. Train list returned and shown.
2. New ticket created.
3. You searched a train number that does not exist.
4. The booking form sent an empty passenger name.
5. The server program crashed while saving.

Check: (1) `200` (2) `201` (3) `404` (4) `400` (5) `500`.

## JSON: the data inside the body

HTML is for **pages**. JSON is for **structured data**.  
When Swiggy sends your cart, it does not send a full newspaper. It sends a compact list of items.

![A messy paragraph versus a neat railway reservation chart and labelled tiffin boxes — JSON is a packing list, not a story](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session22/session22-05-json-reservation-chart.png?v=20260818)

- **JSON (JavaScript Object Notation)**  
  - *Official meaning:* A text format for structured data, based on objects, arrays, strings, numbers, booleans, and `null`.  
  - *In simple words:* A written packing list that both the browser and the server can read.  
  - *Real-life example:* A railway reservation chart: columns for name, age, berth—not a paragraph of story.
- Why JSON: It is smaller than HTML for data, easy for programs to parse, and language-neutral (JavaScript, Python, and others all speak it).
- Syntax rules you must follow:
  - Keys in **double quotes**: `"name"`, not `name`.
  - Strings in **double quotes**: `"Pune"`, not `'Pune'`.
  - No trailing comma after the last item.
  - No comments inside JSON.
  - Values: string, number, `true` / `false`, `null`, object `{ }`, array `[ ]`.
- **JavaScript object vs JSON:** In your script, `{ name: "Asha" }` is a JS object (keys need not be quoted). JSON is **text**. On the wire it looks like `'{"name":"Asha"}'`.
- Nested JSON is normal: an object can hold another object or an array. Example text: `{"train":"Duronto","stops":["Pune","Nagpur"]}`. After parse, `data.stops[0]` is `"Pune"`.
- **`JSON.parse(text)`** turns a JSON string into a JS value. **`JSON.stringify(value)`** turns a JS value into a JSON string.
- If the text is invalid JSON, `JSON.parse` **throws** an error and the next lines do not run. Fix quotes and commas; do not ignore the red console message.
- Common error: calling `JSON.parse` on something that is already an object, or forgetting to parse a string and then seeing `undefined` for `.train`.

### Complete example: parse JSON and show it on the page

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Parse JSON</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <h1>PNR passengers</h1> <!-- Page heading -->
  <ul id="list"></ul> <!-- Empty list that JavaScript will fill -->

  <script> // Starts JavaScript
    const jsonText = '[{"name":"Ravi","berth":"LB"},{"name":"Meera","berth":"UB"}]'; // JSON string as if a server sent it
    const passengers = JSON.parse(jsonText); // Converts the string into a JavaScript array of objects
    const list = document.getElementById("list"); // Selects the ul so items can be appended

    for (let i = 0; i < passengers.length; i++) { // Loops through each passenger object
      const li = document.createElement("li"); // Creates a new list item element
      li.textContent = passengers[i].name + " — " + passengers[i].berth; // Sets visible text from parsed fields
      list.appendChild(li); // Adds the item to the page
    } // Ends the loop
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `jsonText` is one string. Until `JSON.parse`, there is no `.name` property.
- After parse, `passengers` is a normal array. The loop reads `name` and `berth`.
- DOM skills from earlier sessions (`createElement`, `appendChild`) display the data.

### Complete example: stringify data before “sending”

The server expects a **string** in the body, not a live JS object.  
`JSON.stringify` packs the object for the trip.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Stringify JSON</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <p id="out"></p> <!-- Paragraph that will show the JSON string -->

  <script> // Starts JavaScript
    const booking = { // Creates a JavaScript object in memory
      from: "Pune", // Sets the boarding station
      to: "Nagpur", // Sets the destination station
      date: "2026-08-20" // Sets the journey date as a string
    }; // Ends the booking object

    const body = JSON.stringify(booking); // Converts the object into a JSON text string
    document.getElementById("out").textContent = body; // Shows the packed string on the page
    console.log(typeof body); // Confirms the type is string, not object
    console.log(JSON.parse(body).from); // Parses back and reads one field to prove the round trip
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `booking` is a JS object. `typeof booking` would be `"object"`.
- `JSON.stringify` produces `'{"from":"Pune","to":"Nagpur","date":"2026-08-20"}'`.
- A real `POST` would put that string in the HTTP **body** with header `Content-Type: application/json`.
- `JSON.parse(body).from` is `"Pune"` again. Parse and stringify are inverse operations when the data is valid JSON.
- Common doubt: “Can I send the JS object as it is?” Not on the network — HTTP body is text, so stringify first and parse when it comes back.

### Student activity: valid or invalid JSON

On paper, mark each line **valid** or **invalid**. Then check with `JSON.parse` in the console (wrap the text in quotes carefully, or use a template you already parsed).

1. `{"city":"Pune"}`
2. `{city:"Pune"}` (keys without quotes)
3. `{"city":"Pune",}` (trailing comma)
4. `[{"id":1},{"id":2}]`

Invalid lines throw in the console. That error is useful: it means the **text** is not JSON yet, so the server or your quotes need a fix.

## Hands-on: one URL, full trace

Put the pieces in order.  
Typing an address is a **GET** for a **page**. The Network tab records that cycle.

1. User types `https://www.example.com/train-search?from=Pune`.
2. **Client** = browser. **Method** = `GET`. **Path** = `/train-search`. Query `from=Pune` is extra filter text on this request.
3. Server sends status `200`, `Content-Type: text/html`, and an HTML body.
4. Browser paints the page, then may request CSS, JavaScript, and images — each file is another cycle.
5. A wrong path still completes the cycle with `404`. That is not “no internet.”

On the wire (text, not JavaScript) the request can start `GET /train-search?from=Pune HTTP/1.1` with a `Host` header.  
The page reply starts `HTTP/1.1 200 OK` and `Content-Type: text/html`.

A **JSON** packing list is a different kind of body.  
Typing a normal website address does not by itself give you a train array.

This session you **read** JSON text as if you copied it from Network. Sending that data request from your own JavaScript belongs in an upcoming session.

A copied JSON reply would show `Content-Type: application/json` and a body such as `[{"train":"Duronto"},{"train":"Shatabdi"}]`.

### Complete example: unpack a body copied from Network

The status and body below are already in the file, as if you copied one Network row.  
The script does **not** send a request. It only **reads the stamp**, then **parses**.

```html
<!DOCTYPE html> <!-- Declares this file as an HTML5 document -->
<html lang="en"> <!-- Starts the HTML document -->
<head> <!-- Holds metadata and title -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <title>Unpack Copied JSON</title> <!-- Browser tab title -->
</head> <!-- Ends the head -->
<body> <!-- Starts visible content -->
  <button id="unpackBtn">Unpack the copied body</button> <!-- Starts parse after you click -->
  <p id="stamp"></p> <!-- Will show the copied status code -->
  <p id="result"></p> <!-- Will show train names or an error string -->

  <script> // Starts JavaScript
    const stamp = document.getElementById("stamp"); // Selects the status paragraph
    const result = document.getElementById("result"); // Selects the result paragraph
    const unpackBtn = document.getElementById("unpackBtn"); // Selects the unpack button
    const copiedStatus = 200; // Stands in for the status column in Network (try 404 in the activity)
    const copiedBody = '[{"train":"Duronto"},{"train":"Shatabdi"}]'; // JSON text as if copied from the response body

    unpackBtn.addEventListener("click", function () { // Runs unpack only when you click
      stamp.textContent = "Status " + copiedStatus; // Shows the stamp before trusting the body
      const data = JSON.parse(copiedBody); // Converts the copied JSON string into a JavaScript value
      if (copiedStatus === 200) { // Only treats the body as trains when the stamp is success
        result.textContent = "Trains: " + data[0].train + ", " + data[1].train; // Reads fields after parse
      } else { // Handles an error-shaped packing list
        result.textContent = data.error; // Shows the error string from JSON
      } // Ends the status check
    }); // Ends the click listener
  </script> <!-- Ends JavaScript -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- `copiedStatus` and `copiedBody` are stand-ins for **one Network row**. Nothing here talks to the internet.
- You still **read status first**. Then **parse**. Then use fields.
- With `200` and a train array, names appear. With `404` and `{"error":"Not found"}`, the error string appears.
- If the text is invalid JSON, `JSON.parse` throws. Practise that in the **console**, not by breaking this file.

### Student activity: stamp first, then unpack

1. Set `copiedStatus` to `404` and `copiedBody` to `'{"error":"Not found"}'`. Refresh and click. Confirm the result is `Not found`, not train names.
2. Restore `200` and the train array. Confirm both names appear.
3. In the console, run `JSON.parse('{city:"Pune"}')` and read the red error — keys need double quotes.

## Putting HTTP and JSON together

You now have the full picture for one round trip.  
The **client** speaks HTTP. A **page** body is often HTML. A **data** body is often JSON.

- Visit a URL: usually **GET** + HTML, then extra cycles for CSS and images.
- Data packing list: JSON **text** → read **status** → `JSON.parse` → show fields.
- Create (`POST`) → `JSON.stringify` the form data → server replies `201` and maybe the new object as JSON.
- Update (`PUT`) → stringify the full new record → expect `200`.
- Remove (`DELETE`) → often an empty body and `200` or `204`.
- Skipping status is how a `{"error":"..."}` packing list gets treated as a train.

## Key Takeaways

- The **web** is a **client–server** conversation: the browser asks, the server answers.
- One **request–response** cycle uses **HTTP**: method + path out, **status code** + body back.
- **`GET` / `POST` / `PUT` / `DELETE`** are the four verbs that match read, create, replace, and remove.
- **JSON** is text; **`JSON.parse`** and **`JSON.stringify`** move between text and JavaScript values.
- Visiting a URL is a traceable `GET`; DevTools **Network** shows method, status, and path for each file.

In an upcoming session, you will send this same kind of HTTP request from your own JavaScript and wait for the reply — still reading **status** first, then unpacking **JSON**.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| Client | Program that sends the request (browser, app) |
| Server | Program that listens, works, and responds |
| Request–response cycle | One ask + one answer |
| URL | Address: scheme + host + path + optional query |
| Query string | Extra filters after `?`, e.g. `from=Pune` |
| Resource | A path the server knows, e.g. `/trains` |
| HTTP | Protocol for web requests and responses |
| HTTPS | HTTP inside an encrypted connection |
| Header | Extra label, e.g. `Content-Type: application/json` |
| Body | Optional payload; often JSON text |
| `GET` | Read a resource |
| `POST` | Create / submit new data |
| `PUT` | Replace an existing resource |
| `DELETE` | Remove a resource |
| Status `200` | OK — success with a body |
| Status `201` | Created — typical after `POST` |
| Status `204` | Success with no body (often after `DELETE`) |
| Status `400` | Bad request — client input wrong |
| Status `401` | Unauthorised — not logged in |
| Status `403` | Forbidden — logged in but not allowed |
| Status `404` | Not found — path or id missing |
| Status `500` | Server error |
| JSON | Text format for objects and arrays |
| `JSON.parse(text)` | String → JavaScript value |
| `JSON.stringify(value)` | JavaScript value → JSON string |
| `application/json` | Content-Type value for a JSON body |
| Network tab | DevTools view of each HTTP cycle |
