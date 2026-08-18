# GenAI Coding Lab II

In the previous session, you learned **Promises**, the three states **pending / fulfilled / rejected**, **`.then()` / `.catch()`**, and **`fetch()`** for browser **GET** requests.  
You parsed **JSON**, checked **`response.ok`**, and showed live data on the page.  
This session answers the next question: how do you use **AI coding assistants** to **build**, **debug**, and **refine** that same frontend — layout, JavaScript, and Fetch — without copying code you cannot explain?

Think of a college **Canva** poster.  
The tool drafts a banner in seconds; you still check spelling, club name, and whether the QR code works.  
**ChatGPT** or **Claude** is that designer for HTML, CSS, and JavaScript. You remain the student who must **read**, **run**, and **own** every line.

![Student at a hostel desk watching AI draft a college fest poster, then standing with a red pen and phone to check the date and scan the QR code — AI drafts, you own every line](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session24/session24-01-ai-canva-partner.png?v=20260818)

## What you will learn in this session

- How to write a **layout prompt** so AI returns usable **HTML** and **CSS** (Flexbox / Grid, semantic tags)
- How to ask AI for **basic JavaScript**: clicks, search, and DOM updates
- How to **debug** client-side **Fetch / API** problems with AI using error text, not “rewrite everything”
- How to **refine** AI-generated frontend code: loading and error states, names, accessibility, and leftover junk

## AI as a frontend coding partner

You already know enough HTML, CSS, JavaScript, the DOM, and Fetch to **judge** AI output.  
That is the point of this lab.  
AI is fast at first drafts; you are responsible for the page that actually runs in the browser.

- **AI coding assistant**  
  - *Official meaning:* A large language model (LLM) chat tool that turns natural-language instructions into explanations, HTML, CSS, or JavaScript.  
  - *In simple words:* A patient junior developer who types fast and still needs a review.  
  - *Real-life example:* A tailor who stitches a kurta from your measurements. If you said “blue festive kurta” and got a raincoat, the measurement note (the **prompt**) was weak.
- **Prompt**  
  - *Official meaning:* The instruction text you send to the model.  
  - *In simple words:* The order slip you hand the kitchen.  
  - *Real-life example:* “Two masala dosas, one less spicy, extra chutney” is a prompt. “Food” is not.
- Need: Typing a full notice-board page by hand is slow when you already know the pattern. AI drafts the skeleton so you spend time on **logic** and **bugs**.
- Logic: Treat every reply as a **first draft**. If you cannot explain a line in a viva, delete it and ask for a simpler version.
- Common doubt: “Is using AI cheating?” Using it to **learn and verify** is the lab skill. Pasting a full page you cannot defend is not.
- Common error: “Make a website” with no size, no colours, no data source. You get a random template that does not match Fetch or your HTML ids.
- Safe habit: never paste passwords, personal emails, or private API keys into a public chat.

**What AI helps with:** layout HTML/CSS, small JS features, reading a red console error, suggesting a **minimal** Fetch fix.

**What AI cannot replace:** opening DevTools, clicking the real button, checking **Network** status, and matching JSON field names (`title` vs `name`).

## The GenAI frontend lab workflow

Lock one loop before you open the chat.  
Every mini-page in this lab follows the same rhythm.  
Skipping a step is how you get pretty CSS and a blank list.

| Step | What you do | Why it matters |
|------|-------------|----------------|
| **1. Brief** | Write goal, layout, and data shape on paper | Stops AI from building a different app |
| **2. Layout** | Prompt for HTML + CSS only | Separates look from behaviour |
| **3. Review UI** | Check semantic tags, Flex/Grid, ids | Broken ids make later JS fail |
| **4. Behaviour** | Prompt for small JavaScript | One feature at a time is easier to test |
| **5. Integrate** | Wire **`fetch` GET** to the DOM | Reuses the Promise skill you already have |
| **6. Debug** | Paste **error + code + what you tried** | AI fixes faster when it sees the real failure |
| **7. Refine** | Loading, empty, error, names, accessibility | First draft is rarely submission quality |

Connecting idea: Steps 2–4 are where AI is fastest. Steps 5–7 are where **you** become the frontend developer. The same chain in one line is **Brief → Layout → Review → JS → Fetch → Debug → Refine**.

**Common mistake:** Asking “Give me a full website with API and animations” in one message. You cannot review 200 lines you did not request in pieces.

## Generate HTML and CSS layouts with AI

A **layout** is the arrangement of header, content, and footer — the railway station map, not the train times.  
You already practised **semantic HTML**, **Flexbox**, and **Grid**.  
Now you ask AI to produce that skeleton from a **brief**, then you inspect it like a code review.

![Railway station notice board labelled as a webpage — header name board, one-row toolbar with search and Load, empty two-column card platforms, footer announcements — a good brief builds the right station](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session24/session24-02-layout-station-map.png?v=20260818)

- **AI layout generation**  
  - *Official meaning:* Using an assistant to produce HTML structure and CSS layout rules from a written UI brief.  
  - *In simple words:* You describe the notice board; AI paints the first poster.  
  - *Real-life example:* You tell a carpenter “study table, 4 feet, two drawers, left shelf.” A good brief beats “make furniture.”
- Need: Blank `index.html` time is better spent on Fetch and bugs once the box model and navbar pattern are familiar.
- Logic: Ask for **HTML + CSS only** first. Mixing JS in the first prompt hides layout mistakes inside script errors.
- Common error: Accepting `<div>` soup with no `<header>`, `<main>`, or `<label>`. You already know semantic tags; reject the draft.
- Common error: AI invents class names in CSS that never appear in HTML. The page looks unstyled; the prompt must say “use only these class names.”

### Weak prompt vs strong layout prompt

Weak: `Make a nice college website with CSS.`

Strong:

```text
I am a beginner. Build ONE HTML file with internal CSS.
Page: Campus Notice Board for a hostel.
Layout:
- header with title "Campus Notices" and a short subtitle
- main area: a toolbar (search input + Load notices button) then a grid of cards
- footer with one line of helper text
Rules:
- Use semantic tags: header, main, footer, section
- CSS Grid for the cards; Flexbox for the toolbar
- Give ids: searchInput, loadBtn, noticeList, statusMsg
- No JavaScript yet
- No external libraries or images
- Keep CSS under 40 lines
- Add an HTML comment on every tag explaining its job
```

**Why this works:** you stated **level**, **one file**, **exact ids** (for later JS), **Flex vs Grid**, and **no JS yet**.

### Review checklist before you keep AI HTML

| Check | Question |
|-------|----------|
| **Ids match the brief** | Are `searchInput`, `loadBtn`, `noticeList`, `statusMsg` present and unique? |
| **Semantic structure** | Header / main / footer — or only nested divs? |
| **Layout method** | Toolbar is Flex; cards are Grid — or everything is `float`? |
| **You understand it** | Can you point to the element that will hold the list? |

If any row fails, reply: `Keep the same ids. Replace div soup with header, main, footer. Do not add JavaScript.`

### Complete example: layout-only notice board

Save as `notices.html`, open in the browser, and confirm the empty grid and toolbar **before** asking for JavaScript.

```html
<!DOCTYPE html> <!-- Declares an HTML5 document -->
<html lang="en"> <!-- Starts the page; English language hint -->
<head> <!-- Holds title and CSS -->
  <meta charset="UTF-8" /> <!-- Sets character encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <!-- Makes layout readable on phones -->
  <title>Campus Notice Board</title> <!-- Tab title -->
  <style> /* Starts internal CSS */
    body { font-family: Arial, sans-serif; margin: 0; background: #f4f1ea; } /* Page background like old notice paper */
    header, footer { background: #1f4e3d; color: #fff; padding: 16px; text-align: center; } /* Hostel-green bars */
    main { max-width: 900px; margin: 20px auto; padding: 0 16px; } /* Centres the notice area */
    .toolbar { display: flex; gap: 12px; align-items: center; margin-bottom: 16px; } /* Search + button in one row */
    #searchInput { flex: 1; padding: 8px; } /* Search box grows to fill leftover space */
    #noticeList { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; } /* Two-column card grid */
    .card { background: #fff; padding: 12px; border-radius: 8px; } /* One notice card */
    #statusMsg { min-height: 1.5em; color: #333; } /* Status line does not jump the layout */
  </style> <!-- Ends CSS -->
</head> <!-- Ends head -->
<body> <!-- Visible page -->
  <header> <!-- Top bar -->
    <h1>Campus Notices</h1> <!-- Main heading -->
    <p>Hostel board — load live notices, then search by title</p> <!-- Subtitle -->
  </header> <!-- Ends header -->
  <main> <!-- Main content -->
    <p id="statusMsg">Click Load notices when you are ready.</p> <!-- Status for loading / errors -->
    <section class="toolbar" aria-label="Notice tools"> <!-- Flex toolbar -->
      <label for="searchInput">Search</label> <!-- Accessible label for the box -->
      <input id="searchInput" type="search" placeholder="Type a word from the title" /> <!-- Search field -->
      <button id="loadBtn" type="button">Load notices</button> <!-- Triggers Fetch later -->
    </section> <!-- Ends toolbar -->
    <section id="noticeList" aria-live="polite"></section> <!-- Grid that JS will fill -->
  </main> <!-- Ends main -->
  <footer> <!-- Bottom bar -->
    <p>Practice data comes from a public JSON API.</p> <!-- Helper text -->
  </footer> <!-- Ends footer -->
</body> <!-- Ends body -->
</html> <!-- Ends document -->
```

**How the code works**

- Semantic regions give the page a station map: board title, tools, card platform, footer.
- **Flex** puts search and button on one row; **Grid** prepares two columns for cards.
- Ids are the contract for JavaScript. Change an id here without changing the script and the page “does nothing.”
- There is still **no Fetch**. That is deliberate: confirm layout first.

### Student activity: write one layout prompt

On paper, brief a **Mess Menu** page: header, a Flex row with a **Veg / All** idea (just a button and a heading), a Grid of three empty cards, footer.

1. Write a strong prompt using the template above (level, one file, ids, Flex vs Grid, no JS).
2. Paste it into your AI tool and save the HTML.
3. Tick the review checklist. Mark any invented class or missing id in `[brackets]`.
4. Send one follow-up that only fixes the marked items.

Self-check: you can point to the element that will later hold menu cards without reading CSS.

## Create basic JavaScript functionality with AI

Layout is the empty canteen tray.  
**JavaScript** is the volunteer who fills trays when you tap a button.  
Ask AI for **one behaviour** at a time: load, then search — not both in the first JS prompt if you are still shaky.

![Hostel mess in two panels — empty trays and a blank Today's Mess board, then a class representative rings the bell, fills trays, and writes the notice while the student taps Load — one behaviour at a time, still check the spelling](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session24/session24-03-js-canteen-volunteer.png?v=20260818)

- **AI JavaScript assistance**  
  - *Official meaning:* Using an assistant to draft event listeners, DOM updates, and small functions from a behaviour brief.  
  - *In simple words:* You describe the click; AI types `addEventListener`.  
  - *Real-life example:* You tell a junior CR, “When someone taps the bell, write the next mess item on the blackboard.” You still check the spelling on the board.
- Need: You already know `getElementById` and clicks. AI saves typing; you still verify ids and `textContent`.
- Logic: Paste **your** HTML (or list the ids) in the prompt so AI does not invent `#btn1`.
- Common error: AI uses `innerHTML` with a search string. For practice data it may look fine; still prefer `textContent` when you only show titles, so surprise HTML in a title cannot break the page.
- Common error: Search runs before Load. An empty `#noticeList` is not a search bug; it is missing data.

### Strong prompt for one JS feature

```text
Here are my ids: loadBtn, searchInput, noticeList, statusMsg.
Add JavaScript at the bottom of the SAME file.
Feature 1 only: clicking Load notices shows three HARD-CODED cards
(title + body) inside noticeList using createElement (no innerHTML).
Update statusMsg to "Showing sample notices."
Do not use fetch yet.
Comment every JavaScript line in simple English.
```

After this works, a **second** prompt can add search: filter those cards by title as the user types.

Do not jump to Fetch until sample cards appear.  
If Load does nothing, the bug is **ids** or the script — not the API.  
Keep a `current` array that search reads; if you filter a hard-coded `sample` list later mixed with Fetch, the board will show the wrong notices.

**How this JS should work (check AI’s script against this):**

- `render(list)` clears `#noticeList` with `textContent = ""`, then `createElement` for each `title` and `body`.
- Load copies sample data into `current` and calls `render(current)`.
- Search on `input` filters `current` by title and calls `render` again.
- Prefer `textContent` over `innerHTML` for titles.

The **complete** file with `render`, search, and then live **GET** is in the next topic, so you see one full page from `<!DOCTYPE html>` to the last `</html>`.

### Student activity: one extra behaviour

Use your layout file (`notices.html`) after the sample-card prompt works.

1. Prompt AI: add a **Clear** button that empties `#noticeList`, resets `current` to `[]`, and sets status to `Board cleared.`
2. Demand **`getElementById`** and **`textContent`**, and **comments on every new line**.
3. Run it. Then hide the chat and explain the new handler aloud in two sentences.

Self-check: Clear after a search does not leave ghost cards.

## Debug client-side API integration with AI

Sample cards prove the board works.  
Live notices need **`fetch`**, a **Response**, **`response.json()`**, and **`response.ok`** — the previous session in a real layout.  
When the list is blank, AI helps only if you paste the **real error**, not a vague “it doesn’t work.”

- **API integration debugging**  
  - *Official meaning:* Finding why client-side HTTP code fails: wrong URL, missing `ok` check, parse mistakes, or DOM mismatches — often with an assistant that reads the error and the snippet.  
  - *In simple words:* You and AI play detective on the notice truck that never arrived.  
  - *Real-life example:* UPI failed. You send the support chat the **UTR**, the **time**, and the **bank SMS** — not “payment broken.” Same for Fetch.

![Split hostel-desk story — vague “it doesn’t work, rewrite everything” with no proof versus a clear debug brief with Console error, Network 404 stamp, JSON field names, and UPI-style UTR evidence](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session24/session24-04-debug-with-evidence.png?v=20260818)

- Need: AI guesses wildly without console text. DevTools **Console** and **Network** are the evidence.
- Logic: `fetch` **fulfils** on HTTP 404; it **rejects** on network failure. Checking only `.catch` misses many API bugs.
- Common doubt: “AI said the code is correct but Network shows 404.” Trust Network. The URL in the file is wrong or the resource does not exist.
- Common error: Asking “rewrite my app.” You lose the layout you already reviewed. Ask for a **minimal fix**.

### Evidence to copy into the debug prompt

| Evidence | Where you get it | Why AI needs it |
|----------|------------------|-----------------|
| Error message | Console (red text) | Distinguishes `Failed to fetch` from `undefined` |
| HTTP status | Network row | 200 vs 404 vs 500 |
| JSON Preview | Network Preview | Real field names (`title`, not `name`) |
| What you tried | Your notes | Stops AI repeating a failed idea |

### Strong debug prompt

```text
Goal: GET https://jsonplaceholder.typicode.com/posts?_limit=6
and show each post.title in #noticeList.

Code (paste the fetch function only).

Error: (paste the exact Console line)

Network: status ____ ; Preview shows an array / object (pick one).

I already tried: checked the URL; confirmed ids exist.

Task: Explain the cause in 3 bullets.
Then give a MINIMAL fix only — do not rewrite HTML or CSS.
Include response.ok handling.
```

### Bugs AI should help you name

- **Missing `return` before `response.json()`** — next `.then` gets `undefined`; cards cannot loop.
- **No `response.ok` check** — 404 HTML or error JSON is parsed as if it were posts.
- **Wrong shape** — `/posts/1` is one object; `forEach` fails. `/posts` is an array.
- **Wrong field** — users have `name`; posts have `title`. The card title looks empty.
- **`Failed to fetch`** — often offline, CORS, or a `file://` page; open via `http://localhost` if needed.
- **Search before load** — `current` is still `[]`. Not an API bug.

### Complete example: Fetch GET with `ok` check and status text

Use the same ids as the layout file.  
You need internet.  
JSONPlaceholder `/posts?_limit=6` returns an **array** of posts with `title` and `body`.

```html
<!DOCTYPE html> <!-- HTML5 document -->
<html lang="en"> <!-- Starts page -->
<head> <!-- Head -->
  <meta charset="UTF-8" /> <!-- Encoding -->
  <title>Campus Notice Board</title> <!-- Title -->
  <style> /* CSS */
    body { font-family: Arial, sans-serif; margin: 0; background: #f4f1ea; } /* Page */
    header, footer { background: #1f4e3d; color: #fff; padding: 12px; text-align: center; } /* Bars */
    main { max-width: 900px; margin: 16px auto; padding: 0 16px; } /* Centre */
    .toolbar { display: flex; gap: 8px; margin: 12px 0; align-items: center; } /* Toolbar */
    #noticeList { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; } /* Grid */
    .card { background: #fff; padding: 12px; border-radius: 8px; } /* Card */
    button:disabled { opacity: 0.6; } /* Busy state */
  </style> <!-- Ends CSS -->
</head> <!-- Ends head -->
<body> <!-- Body -->
  <header> <!-- Top bar, same regions as the layout file -->
    <h1>Campus Notices</h1> <!-- Heading -->
  </header> <!-- Ends header -->
  <main> <!-- Main content -->
    <p id="statusMsg">Ready.</p> <!-- Status -->
    <section class="toolbar"> <!-- Flex toolbar -->
      <label for="searchInput">Search</label> <!-- Visible label, not only a placeholder -->
      <input id="searchInput" type="search" placeholder="Filter by title" /> <!-- Search -->
      <button id="loadBtn" type="button">Load notices</button> <!-- Load -->
    </section> <!-- Ends toolbar -->
    <section id="noticeList" aria-live="polite"></section> <!-- List -->
  </main> <!-- Ends main -->
  <footer> <!-- Bottom bar -->
    <p>Practice GET from a public JSON API.</p> <!-- Helper text -->
  </footer> <!-- Ends footer -->
  <script> // JavaScript
    const loadBtn = document.getElementById("loadBtn"); // Load button
    const searchInput = document.getElementById("searchInput"); // Search box
    const noticeList = document.getElementById("noticeList"); // Card host
    const statusMsg = document.getElementById("statusMsg"); // Status line
    const url = "https://jsonplaceholder.typicode.com/posts?_limit=6"; // Practice GET URL
    let current = []; // Notices used by search
    function render(list) { // Draws cards
      noticeList.textContent = ""; // Clears old cards
      if (list.length === 0) { // Empty result
        statusMsg.textContent = "No notices match."; // Empty message
        return; // Stop drawing
      } // Ends empty check
      list.forEach(function (item) { // Each post
        const card = document.createElement("article"); // Card
        card.className = "card"; // Class
        const h = document.createElement("h2"); // Title tag
        h.textContent = item.title; // Post title
        const p = document.createElement("p"); // Body tag
        p.textContent = item.body; // Post body
        card.appendChild(h); // Add title
        card.appendChild(p); // Add body
        noticeList.appendChild(card); // Add card
      }); // Ends loop
    } // Ends render
    function loadNotices() { // Starts GET
      statusMsg.textContent = "Loading…"; // Pending UI
      loadBtn.disabled = true; // Blocks double clicks
      fetch(url) // Sends GET; returns a Promise
        .then(function (response) { // Envelope arrived
          if (!response.ok) { // HTTP error (404, 500, …)
            throw new Error("HTTP " + response.status); // Become a rejection
          } // Ends ok check
          return response.json(); // Second Promise: parsed JSON
        }) // Ends first then
        .then(function (data) { // data should be an array
          current = data; // Store for search
          render(current); // Draw cards
          statusMsg.textContent = "Loaded " + current.length + " notices."; // Success text
        }) // Ends second then
        .catch(function (err) { // Network failure or thrown HTTP error
          current = []; // Clear source list
          noticeList.textContent = ""; // Clear cards
          statusMsg.textContent = "Could not load: " + err.message; // User-facing error
        }) // Ends catch
        .then(function () { // Runs after success or failure
          loadBtn.disabled = false; // Re-enable the button
        }); // Ends final then
    } // Ends loadNotices
    loadBtn.addEventListener("click", loadNotices); // Load on click
    searchInput.addEventListener("input", function () { // Filter as you type
      const q = searchInput.value.toLowerCase(); // Query
      const filtered = current.filter(function (item) { // Filter titles
        return item.title.toLowerCase().indexOf(q) !== -1; // Match
      }); // Ends filter
      render(filtered); // Redraw
      if (current.length > 0 && filtered.length > 0) { // Avoid wiping a success message badly
        statusMsg.textContent = "Showing " + filtered.length + " of " + current.length + "."; // Count
      } // Ends status tweak
    }); // Ends search
  </script> <!-- Ends script -->
</body> <!-- Ends body -->
</html> <!-- Ends HTML -->
```

**How the code works**

- **Pending** is “Loading…” and a disabled button — the same Promise idea as a UPI spinner.
- **`ok` false** throws so `.catch` can show HTTP 404 instead of calling `forEach` on the wrong body.
- **`return response.json()`** is required so the next `.then` receives an array, not `undefined`.
- The last `.then` re-enables the button after **either** success or failure so the UI does not stay stuck.

### Student activity: break, then debug with AI

1. Change the URL path to `/postz?_limit=6` (typo). Load. Note Console and Network status.
2. Paste the strong debug prompt with that evidence. Accept only a **minimal** URL fix.
3. Restore a good URL, then remove `return` before `response.json()`. Predict: Network can still be 200, but `data` is `undefined` and `.catch` runs.
4. Ask AI why Preview looks fine while the page shows an error. Confirm it mentions **`return`**.

Check: (typo URL) HTTP error / 404; (missing `return`) the JSON Promise is not passed along, so the next `.then` gets `undefined`.

## Review and refine AI-generated frontend code

A working Load is not the finish line.  
AI often ships extra CSS, vague names (`data1`), missing labels, and no empty state.  
**Refinement** is the hostel warden’s inspection before the notice goes on the real board.

![Hostel warden and student at a Campus Notices board showing four cards — Loading, success titles, No notices match, and Could not load — same board, cleaner handwriting before it is pinned up](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session24/session24-05-warden-inspection.png?v=20260818)

- **Code refinement**  
  - *Official meaning:* Improving generated code for correctness, readability, accessibility, and consistent UI states without changing the product goal.  
  - *In simple words:* Same notice board, cleaner handwriting.  
  - *Real-life example:* Fest poster from Canva: you fix the club spelling, increase contrast, and remove clip-art you did not ask for.
- Need: First drafts impress in the chat window and fail in a viva (“What does `x` mean?”).
- Logic: Refine in passes — **ids and Fetch correctness**, then **UI states**, then **names and comments**, then **accessibility**.
- Common error: Asking AI to “make it professional” — you get animations and a new framework. Say “no new libraries; keep vanilla JS.”
- Common error: Leaving `console.log` of full user objects as the only “UI.” Users need **text on the page**.

### Refinement passes (use as a prompt list)

| Pass | Ask AI (and then verify yourself) |
|------|-----------------------------------|
| **1. Correctness** | Does every id exist? Is `ok` checked? Is the JSON an array? |
| **2. States** | Loading, success, empty search, network error — four different `statusMsg` texts |
| **3. Names** | `loadNotices`, `current`, `render` — not `foo`, `x`, `doStuff` |
| **4. DOM safety** | `textContent` / `createElement` for titles; no leftover unused CSS |
| **5. Accessibility** | `label for=`, `button type="button"`, `aria-live` on the list |
| **6. Comments** | Every line in simple English; delete comments that only repeat the code noise |

Follow-up prompt example: `Do not change the URL or ids. Rename unclear variables. Add a label for the search box. Remove unused CSS. Keep comments on every JS line.`

### Quality checks you run, not the chat

- Read the HTML aloud: header, main, footer still there after “improvements”?
- Disable the network in DevTools and click Load — do you see a human error, or a frozen “Loading…”?
- Search for `zzzz` after a successful load — empty state, not a blank white grid with no message.
- Hover every control: is there a visible label, or only a placeholder (placeholders disappear while typing)?

### Student activity: refine one AI draft

Take any layout AI gave you earlier.

1. Run the six passes on paper. Tick what already exists.
2. Send **one** refinement prompt covering only the failed ticks.
3. Diff by eye: URL and ids must be unchanged.
4. In your notes, write two lines: what AI over-built, and what you deleted.

Self-check: you can explain `render` and the Fetch chain without looking at the chat.

## Putting the lab together

Layout is the board.  
JavaScript is the volunteer.  
Fetch is the office that sends notices.  
Debug prompts are the complaint form with evidence. Refine is the final red pen.

- Brief → layout prompt → review ids.
- One JS feature on sample data → then Fetch.
- Console + Network go into the debug prompt; ask for a **minimal** fix.
- Four UI states and semantic HTML are part of quality, not extras.
- If the UI is blank, check three places: **URL**, **`ok` / status**, **`return response.json()`** — then field names (`title`).

### Mini lab (solo)

Build **Mess Alerts**: same workflow, JSONPlaceholder `/posts?_limit=4`.  
Header “Today’s Mess Alerts”, Flex toolbar, Grid cards, Load, search, `ok` check, disabled button while pending.  
Save prompts in a `prompts.md` file next to `index.html` so the chat is not your only memory.

## Key Takeaways

- **AI assistants** draft HTML, CSS, and JS quickly; **you** review ids, run the page, and explain every line.
- The lab loop is **brief → layout → review → behaviour → Fetch → debug → refine**; skipping review produces pretty pages that cannot load JSON.
- **Strong prompts** name the file, ids, Flex vs Grid, “no JS yet” or “minimal Fetch fix,” and your beginner level.
- **Debug with evidence:** Console error, Network status, JSON Preview, and what you already tried — not “rewrite everything.”
- **Refinement** adds loading, empty, and error states, clear names, semantic tags, and labels; first-draft AI CSS is not the finish line.

`console.log` is for you while learning. Hostel residents need **cards on the board**. In an upcoming session you will move to the **server** side; the same habit — brief, generate, verify, refine — still applies when the code is an API instead of a webpage.

## Important Commands, Libraries, Terminologies used

| Term | What it means / quick example |
|------|--------------------------------|
| AI coding assistant | Chat tool (ChatGPT, Claude) that drafts code from a prompt |
| Prompt | Your instruction; strong ones list ids, constraints, and format |
| Brief | Paper note of goal, layout, and data shape before chatting |
| AI layout generation | HTML/CSS first draft from a UI description |
| Semantic HTML | `header`, `main`, `footer`, `article` instead of only `div` |
| Flexbox | One-row toolbar (`display: flex`) |
| CSS Grid | Card columns (`grid-template-columns`) |
| `getElementById` | Find a node by the id you put in HTML |
| `addEventListener` | Run a function on `click` or `input` |
| `createElement` | Build a card in JS without `innerHTML` |
| `textContent` | Safe way to put plain text in a node |
| `fetch(url)` | Browser GET; Promise of a **Response** |
| `response.ok` | `true` for status 200–299 |
| `response.json()` | Parse body; **return** it in `.then` |
| JSONPlaceholder | Practice API, e.g. `/posts?_limit=6` |
| Collection vs resource | `/posts` array; `/posts/1` one object |
| Network error | `fetch` rejects (`Failed to fetch`, many CORS cases) |
| HTTP error | Response arrived but `ok` is false |
| Minimal fix | Change only the broken line, not the whole page |
| Loading state | “Loading…” plus `button.disabled` |
| Empty state | “No notices match.” after a search |
| `aria-live` | Screen reader hears list updates |
| DevTools Network | Status, Headers, Preview of JSON |
| Code refinement | Cleanup for names, states, accessibility, leftover CSS |
| Vanilla JS | No extra libraries; browser JavaScript only |
