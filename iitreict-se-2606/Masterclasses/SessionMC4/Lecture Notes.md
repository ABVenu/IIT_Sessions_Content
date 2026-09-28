# Masterclass: Evolution of the Web

A college circular PDF, a railway PNR check, and a UPI payment all sit “on the web,” but they are not the same kind of product. A circular only needs to be **read**. A PNR check needs **your** data. A payment needs a **shared register** that two phones cannot cheat.

![Same web, three kinds of product — a college circular you only read, a PNR check that needs your data, and a UPI payment that needs a shared register two phones cannot cheat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session03/session03-01-three-kinds-of-web.png?v=20260910)

If the web had stayed a folder of uploaded files, modern products would fail: no login, no live seats, no one attendance sheet for the class, no safe place for secrets. This lesson exists so you can see **why** the web had to evolve, **how** a browser turns an address into a page, and **where** frontend, server, and backend split the work.

This is a **concept lesson**. You will learn by definitions, tables, paper traces, and short notebook activities. You will not write or run programs in this lesson.

## What You Will Learn in This Lesson

In this lesson, you will learn:

- Why the web had to **evolve** beyond **static Web 1.0** pages
- The **demerits** of a site that never updates itself for the visitor
- How **Web 2.0** turned websites into **interactive, user-driven** platforms
- How a **browser** loads and **renders** a page for you
- How the **JavaScript runtime** inside the browser creates **dynamic** behaviour
- What a **server** is, and how it differs from **frontend**
- The role of **backend** in a web product: shared data, rules, and secrets
- How **frontend** and **backend** split the work, and how **APIs** and the **cloud** connect them
- What **Web 3.0** means at a **high level**

By the end, you will be able to name each web era, walk through a page load on paper, split one familiar app into frontend and backend, and explain why a tab is not a database.

---

## Why the Web Needed to Evolve

The **World Wide Web** began as a way to share documents. That was enough for research papers and simple notices. It was not enough for tickets, chat, payments, or live results.

- **Official Definition:** The **World Wide Web** is a system of **pages**, **links**, and **resources** that browsers request over the internet using addresses called **URLs**.
- **In Simple Words:** The web is a huge notice board of pages that your browser can open by typing an address.
- **Real-Life Example:** Opening `irctc.co.in` is like walking to a ticket counter, except the counter is a page on your phone.

The web did not appear as Flipkart and GPay on day one. It started as a publishing tool. Products came later, when more people and more phones used those same pages.

Four words get mixed in daily talk. Keep them separate.

- **Official Definition:** The **internet** is the global network of connected computers and cables that carry many kinds of traffic, not only web pages.
- **In Simple Words:** The internet is the roads. The web is one kind of shop you visit on those roads.
- **Real-Life Example:** WhatsApp calls use the internet. They are not always web pages inside Chrome.

- **Official Definition:** A **website** is a collection of related web pages and files published under a site name.
- **In Simple Words:** One shop with many rooms (home, about, login).
- **Real-Life Example:** A college site with home, admissions, and circulars is one website.

- **Official Definition:** A **web browser** is the program that requests those pages and draws them for you.
- **In Simple Words:** Chrome, Edge, Firefox, and Safari are the clerks who fetch the circular and show it on your desk.
- **Real-Life Example:** The same IRCTC website can open in Chrome on a laptop and in another browser on a phone.

**Need:** Early pages were like a printed college circular. Visitors only **read**. Modern products need **login**, **search**, **carts**, and **live status**.

**Logic:** When more people came online in India — cyber cafes, then cheap smartphones — “save a page file and hope” broke. The **content**, the **user**, and the **computer that stores data** all had to change.

| Pressure | What changed | Why a static circular failed |
|---|---|---|
| **More people** | Cyber cafes, then smartphones | One office file cannot serve crores of readers |
| **More jobs** | Tickets, UPI, results, shopping | Visitors needed to **do** work, not only **read** |
| **More speed** | Live status expected | A snapshot is already old for the next visitor |

**Common doubt:** “Is email a website?” Email *uses* the internet. Gmail in the browser is a **web** product. The same inbox on a mail app may not be a web page.

**Common doubt:** “Is WhatsApp the web?” WhatsApp uses the internet. The app is not the same as opening a WhatsApp page in Chrome.

**Activity — Four labels:**  
Write `internet`, `web`, `browser`, or `website`: (1) cables and towers, (2) Chrome, (3) irctc.co.in as a whole shop, (4) the system of pages and links. Expected: internet, browser, website, web. Then circle which of your weekly browser tasks would fail if the page could never change after upload.

Once you see that gap, look at the first websites: **static** pages you only read.

---

## Web 1.0: Static Pages You Only Read

**Web 1.0** is the first public era of websites. Pages were mostly **static documents**. The visitor was a **reader**, not a co-author.

- **Official Definition:** **Web 1.0** refers to early websites made mainly of **static HTML** files, published by a site owner and consumed in a **read-only** way.
- **In Simple Words:** Someone types a page, uploads it, and you read it. You do not write back on that same page.
- **Real-Life Example:** A temple website that only lists aarti timings, with no booking and no comments.

Typical Web 1.0 sites felt like **brochures**: college history, address, a photo, phone numbers. Useful. One-way.

- **Official Definition:** **Hypertext** is text structured with **links** that readers can follow to other resources.
- **In Simple Words:** Writing that contains doors.
- **Real-Life Example:** “See also” on a web page. A printed footnote you cannot tap is not a web link.

Web 1.0 used hypertext well. It did not yet treat the visitor as a co-author.

Two roles appear from the first click. They stay with you for the rest of the web.

- **Official Definition:** A **client** is the program that **requests** a resource (usually your browser). A **server** is the program that **responds** with files or data.
- **In Simple Words:** You ask. The other computer answers.
- **Real-Life Example:** You (client) ask the photocopy shop (server) for a circular.

On Web 1.0, the server was often a simple **file cupboard**. It handed you the file. It did not calculate GST or look up *your* attendance. Later you will see a **backend** that also **decides** and **stores**.

A finished page is usually a team of three jobs. Web 1.0 used the first two heavily. Web 2.0 made the third job famous.

- **Official Definition:** **HTML (HyperText Markup Language)** describes the **structure** of a page using headings, paragraphs, and links.
- **In Simple Words:** HTML is the skeleton.
- **Real-Life Example:** Newspaper layout — headline here, column there.

- **Official Definition:** **CSS (Cascading Style Sheets)** describes **presentation**: colours, fonts, spacing, and layout.
- **In Simple Words:** HTML says what the parts are. CSS says how they look.
- **Real-Life Example:** Uniform colour and font on a college ID card. The name is HTML content.

CSS can also **stack** columns on a phone. That is still **look**, not a database. A pretty mobile page with no login is still a brochure with nicer clothes.

- **Official Definition:** **JavaScript** is the language that can change the page **after** it has loaded, in response to clicks, typing, and timers.
- **In Simple Words:** JavaScript is movement.
- **Real-Life Example:** Tapping “Show PIN” without opening a brand-new page.

| Language | Job | Web 1.0 | Web 2.0 |
|---|---|---|---|
| **HTML** | Structure | Almost the whole product | Still the skeleton |
| **CSS** | Look | Simple colours | Richer layout on phones |
| **JavaScript** | Behaviour | Little on many brochure sites | Clicks, search, likes, asking servers |

**Static** does not mean “ugly.” It means the **file does not rewrite itself** for each visitor. A fest gallery is still static if everyone sees the **same** photos.

- **Official Definition:** A **hyperlink** is a reference the browser can follow to another URL.
- **In Simple Words:** A door from this circular to the college home page.
- **Real-Life Example:** “Exam timetable” that opens a second sheet.

A link does **not** make the first page smart. The publisher only prepared a second file and wrote its address.

| Person | What they can do on a static site |
|---|---|
| **Publisher** | Edit the file, change “4 PM” to “5 PM”, upload again |
| **Visitor** | Read, click links, print. Cannot store a comment on that file |

Picture a college circular: heading, “Library closes at 4 PM”, “Issued by Admin”, and a “College home” link. Only the publisher can change 4 PM. Blue CSS does not store your likes.

| Piece on the page | Job | Who can change it |
|---|---|---|
| “Friday Circular” | Title | Publisher, by republishing |
| “Library will close at 4 PM” | News | Publisher |
| “College home” | Link to another file | Still a new file, not a living counter |

**Activity — Brochure or product:**  
Write `brochure` or `product`: (1) a hotel PDF menu, (2) booking a room with your dates, (3) a company About page, (4) tracking a food order. Expected: brochure, product, brochure, product. On paper, sketch the circular and write who can change 4 PM.

Static pages were a strong start and a weak product platform. Next come the **demerits**.

---

## Demerits of Static-Only Websites

A static-only website is a **finished printout** on a wall. These limits are why the web evolved. They are not insults to HTML. A **product** needs more than HTML files.

**Demerit 1 — No personal response.** Every visitor sees the **same** page. Login and “your attendance” need a lookup of **your** data. A printed railway timetable cannot show *your* PNR. Priya and Aman cannot see different library fines on one frozen file. Personal pages need **identity** and a **lookup**.

**Demerit 2 — Costly, slow updates.** A person edits a file and publishes it. Hundreds of prices cannot be rewritten by hand all day. Ten thousand page files, one per student, go stale overnight. Price, seats, and marks must live where programs can update them quickly — a **database**.

**Demerit 3 — Weak interaction.** A **form** has nowhere intelligent to send the answer unless a **server program** exists. Early forms often returned a **full new page**.

- **Official Definition:** A **form** is a set of fields the visitor fills so data can be sent somewhere.
- **In Simple Words:** The paper slip at a counter.
- **Real-Life Example:** “From station” and “To station” boxes.

On a static-only site, that slip has no clerk. Either nothing happens, or a whole new printout arrives.

**Demerit 4 — No living data.** Scores, UPI balances, and seat maps change every second. A static file is a **snapshot**.

- **Official Definition:** A **database** is an organised store of data that programs can **read** and **update**.
- **In Simple Words:** The ledger, not the printed receipt.
- **Real-Life Example:** The attendance register versus a photocopy of last Monday’s sheet.
- **Logic:** If the truth lives in a database, the page must **ask** for it at request time.

| Kind of truth | Static file | Living product |
|---|---|---|
| Library time this term | Can work if rare | Better as one office record |
| Train seats | Stale in minutes | Look up now |
| UPI balance | Dangerous if printed | Ask the bank systems |
| Marks for 4,000 students | 4,000 files | One register, many lookups |

**Demerit 5 — Poor fit for many phones.** One file on one office PC cannot serve crores of smartphones at result time. Even a bigger machine still needs a **lookup** for personal results.

**Activity — Spot the freeze:**  
Imagine a food-delivery site as one page with last month’s prices. Write three actions that would break (order, coupon, live ETA) and which demerit each matches. Then mark `snapshot` or `must be live`: founding year, live cricket score, mess balance. Expected: snapshot, live, live.

These limits pushed the web from a library of files to **applications**. That shift is **Web 2.0**.

---

## Web 2.0: Interactive, User-Driven Platforms

**Web 2.0** is not a new internet cable. It is a new **habit**: people **write** as well as read, and pages **update** without a fresh printout every time.

- **Official Definition:** **Web 2.0** describes websites that behave like **applications**, with **user-generated content**, richer **interaction**, and data stored on **servers** that many clients share.
- **In Simple Words:** You post, comment, like, search, and see **your** version of the site.
- **Real-Life Example:** YouTube comments, Wikipedia edits, Flipkart reviews, Instagram posts.

The roads stayed. The **habit of the shop** changed. The visitor became a worker, not only a window-shopper.

What changed: **read-write** (reviews, uploads); **accounts** (“Priya’s cart”); **partial updates** (one card refreshes); **platforms** (a service used by millions).

- **Official Definition:** **User-generated content (UGC)** is material created by visitors and stored for others to see.
- **In Simple Words:** The customers write the catalogue.
- **Real-Life Example:** Flipkart reviews the company did not type.

**Need:** Marketplaces only work if users supply photos and ratings.

- **Official Definition:** An **account** is a stored identity plus related data (name, cart, orders) used after login.
- **In Simple Words:** A locker with your name behind the counter.
- **Real-Life Example:** Your IRCTC login is not your friend’s locker. Same website. Different lockers.

**Common doubt:** “Is a Google Form Web 2.0?” If answers are **stored**, the visitor is contributing. That is Web 2.0 behaviour.

- **Official Definition:** **AJAX** lets a page **request new data** and **update part of the screen** without a full reload. Today the data is often **JSON**, not XML.
- **In Simple Words:** The page whispers to the server, then changes one card, not the whole sheet.
- **Real-Life Example:** Search suggestions under the box while the header stays still.

**Full reload** is a new photocopy of the entire circular. **Partial update** is the clerk changing only “seats left.”

**Logic:** The browser became a **thin shopfront**. The **truth** lives on a server. **JavaScript** **paints** the latest truth.

**Common doubt:** “Did HTML die?” No. HTML is still the skeleton. CSS styles. JavaScript updates after load.

**Common error:** Calling every colourful site “Web 2.0.” A static brochure is still Web 1.0 in behaviour if you cannot log in or contribute.

| Question | Web 1.0-style | Web 2.0-style |
|---|---|---|
| Who writes content? | The owner | Owner **and** visitors |
| Does the page know me? | Usually no | After login, yes |
| Search | Often a whole new page | Often suggestions under the box |
| Where is the truth? | Page files | Servers / databases |

![Web 1.0 vs Web 2.0 — a read-only college brochure with static page files versus an interactive platform with accounts, user reviews, partial updates, and truth on servers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session03/session03-02-web1-vs-web2.png?v=20260910)

**Activity — Label the era:**  
Write `1.0` or `2.0`: (1) restaurant PDF menu, (2) Swiggy tracking, (3) aarti timings with no login, (4) a Google Form that stores answers. Expected: 1.0, 2.0, 1.0, 2.0. On a shopping site, type two letters: if the header stays while suggestions appear, that is a **partial update**. Write `UGC` or `owner`: Wikipedia article, college founding-year paragraph, YouTube comments. Expected: UGC, owner, UGC.

Web 2.0 pages still arrive through the **browser**. Next: how that browser **loads** and **renders** a page.

---

## How a Browser Loads and Renders a Page

A **browser** fetches web resources and turns them into something you can read and click.

- **Official Definition:** A **web browser** is a client that requests resources over **HTTP/HTTPS**, then **parses**, **lays out**, **paints**, and runs **JavaScript**.
- **In Simple Words:** Chrome and others **get** a page, then **draw** it.
- **Real-Life Example:** A clerk who brings a file from a godown, arranges the papers, and lets you tick boxes.

The browser is both **postman** and **artist**. It collects parcels, then draws a picture you can tap.

- **Official Definition:** A **URL** is the address of a resource on the web.
- **In Simple Words:** Protocol + site name + path, like a full door number.
- **Real-Life Example:** `https://www.irctc.co.in/nget/train-search`.

| Piece | Example | Meaning |
|---|---|---|
| Protocol | `https://` | How to talk; **S** means **encrypted** |
| Site name | `www.irctc.co.in` | Which shop |
| Path | `/nget/train-search` | Which counter inside the shop |

A **query** after `?` is extra sticky notes on the same counter, not a different building.

- **Official Definition:** **DNS** translates a human site name into a numeric address.
- **In Simple Words:** The phone book from shop name to shop number.
- **Real-Life Example:** You remember `google.com`. The network needs the machine address.

If DNS fails, the page never starts. That is a **network** failure, not a CSS failure.

- **Official Definition:** **HTTP** is the request–response protocol for web resources. **HTTPS** is HTTP with **encryption**.
- **In Simple Words:** “GET me this page.” HTTPS hides the talk from a stranger on cafe Wi-Fi.
- **Real-Life Example:** **GET** asks for the circular. **Status 200** means “here it is.”

Open cafe Wi-Fi is a shared road. HTTP is a postcard. HTTPS is an envelope. HTTPS does not prove the company is honest. It only makes the **pipe** harder to spy on. A fake similar name can still trick you.

- **Official Definition:** An **HTTP method** is the verb of the request. **GET** means “please give me this.” **POST** means “please accept this slip and act.”
- **In Simple Words:** GET reads the notice board. POST hands a filled form to the clerk.
- **Real-Life Example:** Opening results is usually GET. Pressing “Book ticket” is usually POST.

GET is usually safe to repeat with Refresh. POST often is not — the kitchen might cook the same order twice. Do not use a GET-style reread to **deduct money**.

| Verb | Intent | Repeat with Refresh? | Everyday picture |
|---|---|---|---|
| **GET** | Read a resource | Usually yes | Opening PNR status |
| **POST** | Submit a slip that may change stored data | Often no | Pressing Pay or Book |

**Activity — GET or POST:**  
Write `GET` or `POST`: (1) open the About page, (2) submit a ticket booking, (3) load a logo image, (4) send a Google Form, (5) view a static aarti PDF. Expected: GET, POST, GET, POST, GET.

| Status | Meaning | Picture |
|---|---|---|
| **200** | Success | Clerk hands you the circular |
| **404** | Not found | Wrong hostel room number |
| **500** | Server error | Kitchen computer crashed |

A request typically carries method, URL, **headers** (sticky notes on the envelope), and sometimes a body. A response carries status, headers, and a body (HTML or JSON).

Keep this load-and-render order. Do not jump from “I typed the URL” to “I saw the button.”

| Step | What happens | Student label |
|---|---|---|
| 1 | You type a URL or click a link | Start |
| 2 | **DNS** finds the server address | Phone book |
| 3 | Browser sends **HTTP GET** | Ask |
| 4 | **Server** replies with HTML (then CSS, images, scripts) | Answer |
| 5 | Browser **parses HTML** into a **DOM** tree | Structure |
| 6 | Browser **parses CSS** (often called a **CSSOM**) | Look |
| 7 | Structure + style become a **render tree** | What to draw |
| 8 | **Layout** (reflow) sets size and position | Positions |
| 9 | **Paint** fills pixels | Pixels |
| 10 | **JavaScript** may change the DOM; layout and paint may repeat | Update |

![How a browser loads and renders a page — URL pieces, DNS phone book, HTTPS GET envelope, DOM whiteboard, then layout and paint of the finished page](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session03/session03-03-browser-load-render.png?v=20260910)

The first reply is often HTML. HTML then **points** to other **resources** (CSS, images, scripts). One click can become many small asks. That is why photos on a news site can appear after the text.

- **Official Definition:** A **resource** is any file or data the browser fetches: HTML, CSS, an image, a script, or a JSON reply.
- **In Simple Words:** Each parcel the clerk brings from the godown.
- **Real-Life Example:** The IRCTC logo is a separate parcel from the search page HTML.

- **Official Definition:** **Headers** are extra key-value notes sent with a request or response (for example, what kind of content is in the body).
- **In Simple Words:** Sticky notes on the envelope, not the letter itself.
- **Real-Life Example:** “This packet is JSON” versus “This packet is an HTML circular.”

| Direction | Typical boxes | Beginner meaning |
|---|---|---|
| **Request** | Method, URL, headers, optional body | Verb + address + sticky notes + maybe a slip |
| **Response** | Status, headers, body | Stamp + notes + circular or packing list |

**Need:** If the body is JSON but someone treats it as a full newspaper, the drawing step goes wrong.

- **Official Definition:** The **DOM** is a tree-shaped in-memory model of the page that programs can read and change.
- **In Simple Words:** JavaScript talks to that family tree of tags, not to a paper file in a cupboard.
- **Real-Life Example:** The published file is the printed seating chart. The DOM is the **whiteboard** the usher updates.

**Logic:** Parse → tree → layout → paint. JavaScript is a **late guest** that can move furniture after the first drawing.

- **Official Definition:** A **cache** is a stored copy of a resource so it may not be fetched again immediately.
- **In Simple Words:** Yesterday’s photocopy in your bag.
- **Real-Life Example:** A college logo can be cached. Today’s cricket score must not.

A **tab** is one living whiteboard. Refresh rebuilds it. Close tab throws it away. A new tab does not inherit Like counts unless a **server** stored them.

**Common error:** Thinking the file on a laptop *is* the live page. The browser works on the **DOM**.

**Common doubt:** “Why is the page slow?” Large images and heavy scripts delay **paint**. Network wait (steps 1–4) is only half the story.

**Activity — Paper trace:**  
Copy the ten **Student labels**. Circle protocol, site name, and path in the IRCTC URL. Tick HTTPS if you would rather type a password there than on plain HTTP. Mark `GET` or `POST`: open About, submit a booking, load a logo, send a form. Expected: GET, POST, GET, POST. Mark `ok to cache` or `must be live`: college logo, UPI balance, seats left. Expected: cache, live, live.

Dynamic behaviour still needs a worker inside the browser: the **JavaScript runtime**.

---

## JavaScript Runtime: Dynamic Behaviour in the Browser

**JavaScript** is the language browsers run to make pages **react**. **Java** is a different language. The similar name is a historical accident.

- **Official Definition:** **JavaScript** is a high-level language that browsers execute to update the **DOM**, handle **events**, and call **network APIs**.
- **In Simple Words:** HTML is the body. CSS is the clothes. JavaScript is the **movement**.
- **Real-Life Example:** The “Show PIN” eye icon toggling hidden text.

- **Official Definition:** A **JavaScript runtime** in the browser is the **engine** plus browser tools (DOM, timers, network).
- **In Simple Words:** The kitchen where JS recipes cook, plus the fridge (DOM) and the phone (network).
- **Real-Life Example:** Chrome’s engine is commonly **V8**. The recipe is the script; the engine is the cook.

The runtime gives you a **call stack** (one job at a time), an **event loop** (clicks and timers when the stack is free), and tools to listen for a click and later **ask a server**.

Python does **not** sit in this kitchen. The browser does not run your DSA Python files. Frontend in the browser is JavaScript. Backend on the server, in this course, is often Python. Two kitchens. Two jobs.

- **Official Definition:** An **event** is a signal (click, load, timer) attached to a **handler** — the work that runs when that signal arrives.
- **In Simple Words:** “When this button is pressed, run this recipe.”
- **Real-Life Example:** A doorbell is the event. The person who opens the door is the handler.

Common events: click (Like, Pay), typing in search, page load, a timer after two seconds.

**Need:** Without JavaScript, every change is a full new page.

**Logic:** Click → event queued → handler on the **call stack** → **DOM** changes → **paint**. The **event loop** lets a timer run later without freezing the page.

Walk through a **Like** button on paper, with no program:

| Moment | This visitor’s tab | Other visitors |
|---|---|---|
| Page opens | Likes show `0` | Their own `0` |
| This visitor clicks once | This screen shows `1` | Still `0` unless a **server** stores a shared count |
| This visitor closes the tab | The `1` is gone | Unchanged |

| Memory | Lives where | Survives closing the tab? |
|---|---|---|
| Values in this tab | Browser tab | No |
| DOM text you see | Same whiteboard | No |
| Shared college like-count | Server / database | Yes, if saved |

**Common doubt:** “Does Like reload the whole site?” On a Web 2.0 page, usually **no**. Only the number changes.

**Common error:** Treating a tab-only count as the product. Close the tab, and it forgets. A real product needs a **server** and a **backend**.

**Activity — Doorbell and Like:**  
Draw event (doorbell) and handler (person at the door). Write clicks 1, 2, 3 in **your** notebook. A classmate with **no** shared server still shows `0`. If you close the tab and the count is 0 again, tab memory died; the **server register** was missing.

The likes-in-one-tab limit is why the web split into **frontend** and **backend**.

A Like that only lives in JavaScript is a classroom demo of **movement**. A Like that the whole college can see is a **product** feature. The second kind needs a listening program and a register. That split is the next topic.

---

## Frontend, Backend, and the Server

A page that only lives on one laptop is a poster. Real apps need a **shared brain** that many users can trust.

- **Official Definition:** **Frontend** is the client-side layer in the **browser**: **HTML**, **CSS**, and **JavaScript**.
- **In Simple Words:** Everything the visitor **sees** and **taps**.
- **Real-Life Example:** On **Swiggy**, restaurant cards, search, and “Place order” are frontend.

- **Official Definition:** **Backend** is the server-side layer that receives **HTTP** requests, applies **business rules**, talks to storage, and returns a **response**.
- **In Simple Words:** The kitchen and accounts office behind the dining hall.
- **Real-Life Example:** Swiggy’s servers check whether the shop is open, calculate GST, and record the order. That work is not CSS.

- **Official Definition:** A **server** is a **listening program** that waits for requests, applies rules, and sends a response. Backend **runs on** a server process.
- **In Simple Words:** Frontend is the dining hall. The server is the kitchen window. Backend is the cook, the stock register, and the GST bill.
- **Real-Life Example:** IRCTC’s computers answering Chrome. A program on a laptop that **listens** is also a server for learning.

**Frontend is not the server.** Opening a page file by double-clicking is the browser reading a **local file**. Nobody else can call that file.

A **computer** is hardware. A **server program** is the listener. Prefer **listening program** when you mean backend.

| Role | What it is |
|---|---|
| **Client** | The program that asks — usually the browser |
| **Server** | The **listening program** that answers HTTP |
| **Frontend** | HTML, CSS, JS **in the browser** (almost always the client) |
| **Backend** | Rules, storage, responses **on the server** |

| Layer | Runs where | Typical job | Languages |
|---|---|---|---|
| **Frontend** | Browser | UI, forms, asking the server | HTML, CSS, JavaScript |
| **Backend** | Server process | Validate, decide, store, respond | Often **Python** (not in Chrome) |

![Frontend, server, and backend — shop window in the browser, kitchen window as a listening program on a port, and backend kitchen with rules, database, and secrets](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session03/session03-04-frontend-backend-split.png?v=20260910)

- **Official Definition:** A **port** is a numbered door on a machine. A server **listens** on a port.
- **In Simple Words:** Building = computer. Door = port. Counter inside = **path**.
- **Real-Life Example:** Public HTTPS often uses door **443**. A learning server on a laptop often uses **8000**. You may not see `:443` in the address bar.

HTTP is the same conversation: **GET**, **JSON**, status **200**. Frontend **sends**. Backend **answers**.

Every click that needs shared truth follows this loop:

1. The visitor taps something on the **frontend**.
2. The browser sends an **HTTP request** (GET to read, POST to submit a slip).
3. The **server** receives it. **Backend** rules run.
4. Backend may read or write a **database**.
5. Backend sends an **HTTP response** (status + data).
6. Frontend updates the **DOM**.

If step 3 never happens, you only have a poster.

Example: “Show my attendance.” Frontend draws the Attendance button. GET asks the server. Backend looks up **your** row in the database (step 4). JSON comes back. Frontend paints the numbers. The official sheet never lived only in JavaScript.

**Need:** **Python does not run inside the browser.** Asking from the page is still the **client**. Backend is the program that **answers**.

**Why frontend alone is not enough**

- **Shared data:** One attendance sheet, not a copy in each phone.
- **Rules:** Only the exam cell publishes marks — the visitor must not rewrite that on screen.
- **Secrets:** Passwords and payment keys must not travel as ordinary page text.
- **Many clients:** Phone, laptop, and a later app share **one** record.
- **Logic:** Frontend is the **shop window**. Backend is the **stock register**.

| Job HTML/CSS cannot safely do | Why |
|---|---|
| Official marks for the class | Each phone would tell a different story |
| Confirm UPI success | The visitor could fake a green “Paid” stamp |
| Hide the exam-cell password | Anything in the browser can be inspected |
| Stop the last seat selling twice | Two tabs would both think the seat is free |

A server can be written in more than one language.

| Language | Common style | Why you may hear it |
|---|---|---|
| **Python** | FastAPI, Django, Flask | Readable; strong for APIs and later AI |
| **JavaScript** | Node.js | Same language as the browser, but Node runs **on the server** |
| **Java** | Spring Boot | Common in large companies |

**Common doubt:** “Can JavaScript run on the server?” Yes — **Node.js**. This course still uses **Python** on the server so your Python skills transfer. Do not expect the browser to `import` Python. Two runtimes. Two places.

- **Official Definition:** A **backend developer** designs server-side logic and **APIs** that clients consume.
- **In Simple Words:** Builds the counters that take orders and send stamped replies — not the poster colours.
- **Real-Life Example:** Railway clerks check seats. They do not paint the waiting hall.

A **frontend developer** builds layout, interaction, and how the page talks to APIs.

Typical backend jobs: expose **endpoints** (path + method); return JSON with a correct status; keep **business rules** in one place; later, database and login.

What is **not** the backend’s job: pixel-perfect layout, button colours, or drawing the page. Frontend still does that.

- **Official Definition:** An **endpoint** is one concrete door: a path plus a method.
- **In Simple Words:** One labelled counter, not the whole station.
- **Real-Life Example:** “Give me PNR status” versus “Book this seat.”

**Common doubt:** “Is backend only databases?” No. A server can return a fixed message with **no** database.

**Common error:** Putting payment logic only on the page. **Common error:** Thinking backend means a cloud you cannot touch. A **listening program on a laptop** is a backend for learning.

Login memory is not a JavaScript number in one tab.

- **Official Definition:** A **cookie** is a small piece of data the browser can send back to the same site later. A **session** is the server’s record that this token belongs to this user for a while.
- **In Simple Words:** Cloakroom token versus the bag in the cloakroom.
- **Real-Life Example:** After college-portal login, Attendance opens without retyping the password. The **numbers** still live on the server.

If you delete cookies, the token is gone. The bag (tickets) may still exist until you log in again. A cookie is not the database.

| Thing | Lives mainly where | Survives a new phone? |
|---|---|---|
| Like count only in this tab | Tab memory | No |
| Login cookie | This browser, this site | No — new phone needs login |
| Your booked tickets | Backend database | Yes, after you log in |

**Activity — One app, two layers:**  
Pick IRCTC, GPay, or your college portal. **Frontend shows …** / **Backend must …** (something the browser cannot safely do alone). Then write `FE` or `BE`: (1) blue Book button, (2) check seat free, (3) hide PIN on tap, (4) store all bookings, (5) GST that the passenger cannot edit, (6) heading font. Expected: FE, BE, FE, BE, BE, FE. Write two lines: **Token is …** (cookie) and **Bag is …** (tickets). The bag is not the blue button text.

Once the work is split, the two sides need a **menu of questions**. That menu is the **API**. The rented machines that host the backend are often the **cloud**.

---

## APIs and the Cloud Shift

When the web became a platform, pages started **asking** servers for structured data instead of baking every fact into HTML.

- **Official Definition:** An **API** is a defined way for one program to request work or data from another program.
- **In Simple Words:** A **menu of counters**: this URL, this question, this reply.
- **Real-Life Example:** A weather app does not own the satellites. UPI apps talk to banks through APIs.

The frontend does not need to know how the kitchen stores stock. It needs the **menu**. One backend can serve Chrome, a phone app, and later another company. The **UI** changes. The **endpoint** can stay.

- **Official Definition:** **JSON** is a text format for structured data using keys and values.
- **In Simple Words:** A labelled packing list, not a full HTML newspaper.
- **Real-Life Example:** `train` = Shatabdi, `status` = On time, `platform` = 5 is easier for a program than a paragraph.

**Logic:** HTML is not the database. JSON is a convenient reply. Status **200** means the ask succeeded.

Frontend JavaScript can **ask** an API (often named **`fetch`**). You do not write that ask in this lesson. The page is still the **client**. The answerer is **backend**.

**Common error:** Calling the ask “the backend.”

- **Official Definition:** **Cloud computing** is on-demand use of **remote computers** run by a provider.
- **In Simple Words:** You **rent** a godown of computers instead of building one for a college fest.
- **Real-Life Example:** A startup in Pune can host a backend in Mumbai without buying a rack.

- **Official Definition:** A **data centre** is a building of networked computers, power, and cooling.
- **In Simple Words:** A warehouse of machines, not the principal’s laptop.

Why the shift: many clients, one truth; **scale** at exam or IPL peak; frontend shapes the shopfront while backend owns the register; renting peak hours can beat buying idle machines.

**Common doubt:** “Is the cloud someone else’s computer?” For a beginner, yes — with rental and scaling. A backend on **your laptop** is local learning, not cloud. A brochure on one office PC is not cloud just because it is online.

A **CDN** keeps copies of images closer to users. That is delivery. It does not replace the backend register.

**Activity — Packing list and scale:**  
Add a row `late_by_minutes` = 10 to the train packing list. Circle who **asks** (page) and who **answers** (server). Then write `cloud idea` or `office PC`: IPL scores for crores of phones; one circular on a staff laptop; UPI at 8 PM; a temple PDF. Expected: cloud, office, cloud, office. Write one sentence: Chrome and the phone app can both ask **GET PNR** and receive the same JSON; only the **frontend** painting differs.

APIs and cloud explain **today’s** web. **Web 3.0** is the next label — a high-level map, not a new browser.

---

## Web 3.0 at a High Level

**Web 3.0** is a loose name, not one company product. Both meanings sit **on top of** HTML, browsers, frontend, and backend.

**Meaning 1 — A smarter, more connected web**

- **Official Definition:** Early **Web 3.0** talk (the **Semantic Web**) meant data published so **machines** can interpret meaning, not only humans reading paragraphs.
- **In Simple Words:** Labels so software can connect “Chennai” the city with trains and weather, not only the letters.
- **Real-Life Example:** Search cards that show train time, rating, and address from **structured** facts.

This is close to JSON: labelled facts travel better than paragraphs.

**Meaning 2 — More user control of identity and data**

Some products use **decentralised** networks (often discussed with **blockchains**) so records are not only in one company’s database.

- **In Simple Words:** “You hold more of the keys.”
- **Real-Life Example:** A shared attendance ledger many offices can verify — as an *idea*, not a tool you must install today.

**What Web 3.0 is not:** it did **not** delete Web 2.0; it is **not** required to understand a Like button; it does **not** mean every site must use crypto.

**Logic:** Web 1.0 published documents. Web 2.0 published **platforms**. Web 3.0 tries to publish **meaning** and, in some designs, **shared ownership of records**.

| Era | Visitor’s job | Where the truth lives | Typical click |
|---|---|---|---|
| **Web 1.0** | Read | Static page files | Open another page |
| **Web 2.0** | Read and participate | Servers, databases, APIs | Like, search, login, ask an API |
| **Web 3.0** | Read, participate, more control (goal) | Structured data; sometimes shared networks | Same browser tools, extra ideas |

**Activity — Era test:**  
Web 1.0 = “I read.” Web 2.0 = “I participate.” Web 3.0 = “Data is structured / control is more shared.” Place: aarti PDF = 1.0; Flipkart cart = 2.0; a search card that already knows Chennai is a city = 3.0-idea. GPay, Swiggy, and LMS attendance are still **2.0** if they only need frontend + a company database.

---

## How the Pieces Fit

This walk uses terms you already learnt. It does not add new definitions.

1. Type a **URL** in a **browser** (client).
2. **DNS** finds the shop. **HTTPS GET** asks for the page.
3. A **server** answers with **HTML**, then **CSS** and **JavaScript**.
4. The browser builds a **DOM**, **lays out**, and **paints** (**frontend**).
5. The visitor types stations. **JavaScript** handles **events** and may **ask an API**.
6. **Backend** checks seats in a **database**, returns **JSON**.
7. Frontend paints “2 seats left.” That number was not in the original HTML file.
8. **POST** would submit a booking. Backend must stop double-booking.
9. **Cloud** keeps that backend up when crores try at 10 AM.
10. None of this required **Web 3.0**.

![How the pieces fit — tap on frontend, HTTP request, backend rules, database lookup, JSON packing list, DOM paint; API as a menu of counters; cloud as rented machines](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session03/session03-05-api-json-cloud-loop.png?v=20260910)

The same loop applies to UPI: frontend shows Pay; an **event** must not print success alone; backend talks to banks; only then paint “Paid.” A green stamp with no server check is unsafe.

| What you do on IRCTC | Web idea | Layer |
|---|---|---|
| Type irctc.co.in | URL, DNS, HTTPS | Browser as client |
| See the search form | HTML, CSS | Frontend |
| Suggestions while typing | Event, JS, partial update, API | Frontend asking backend |
| See seats | JSON painted into the DOM | Backend truth, frontend drawing |
| Log in | Account, cookie / session | Token in browser, bag on server |
| Book a seat | POST, rules, database | Backend |
| Tatkal peak | Scale | Cloud |
| About-history paragraph | Can be almost static | Brochure inside a product |

**Activity — Map one product:**  
Circle the IRCTC row that still works as Web 1.0 (About). Circle a row that **must** have backend (book). Then fill one line each for Swiggy: Frontend, Backend, API, Event, Cloud. Write why “seats left stored only as text on the page” lets two passengers buy the same seat.

---

## Common Mix-Ups

| People say | More accurate here |
|---|---|
| “The internet is down” for one site | That **website** or **DNS** may have failed |
| “The server” | Hardware **or** a **listening program** — say which |
| “Frontend” = the whole company site | Frontend is the **browser** layer only |
| “Backend” = the database | Database is **one** backend tool |
| “I fetched, so I built backend” | The ask is still **frontend** |
| Java and JavaScript | Different languages |
| Python in the browser | Browser runs **JavaScript** |
| “Cloud” = any site online | Cloud is **rented remote machines** |
| “Web 3.0” = a modern look | Look is CSS |
| Refresh updates the class register | Refresh rebuilds **this** whiteboard |

**Activity — Correct the sentence:**  
“I stored all marks in JavaScript so the whole class can see them.” Correct: marks belong in a **backend database**; JavaScript can only **ask** and **paint**.

**Notebook check (try first):** internet vs web; Web 1.0 vs 2.0 job; HTML / CSS / JS; client vs server; ten load labels; DOM; tab memory vs register; frontend vs backend; GET vs POST; 200 / 404 / 500; JSON; API vs fetch; cloud vs office PC; cookie vs bag; port vs path.

Suggested answers in short: roads vs pages; read vs participate; structure / look / movement; asks vs listens; Start…Update; in-memory tree; tab vs database; browser vs server process; read vs submit slip; success / missing / kitchen error; packing list; menu vs client ask; rented machines vs staff laptop; token vs tickets; door vs counter.

---

## Key Takeaways

- **Web 1.0** published **static HTML** that visitors mostly **read**. Links opened new files. They did not make the first file smart.
- Static-only sites cannot personalise, scale, or show **live** data. **Web 2.0** made the web a **user-driven platform**.
- A browser **loads** with DNS and HTTP, then **renders** a **DOM** and **paints**; **JavaScript** can change the DOM — still inside **one tab** until a server is involved.
- **Frontend** runs in the browser. A **server** is a **listening program**. **Backend** holds shared data, rules, and secrets. Opening a local page file is not a backend. Python does not run in the browser.
- **APIs** and **JSON** connect shopfront and kitchen. The **cloud** rents machines for many clients. **GET** rereads; **POST** acts. **Web 3.0** is a high-level name for smarter data and some decentralised experiments. You will use these ideas as products and backends grow.

One-breath summary: the **browser** draws **frontend** from HTML, CSS, and JavaScript; a **server** **listens**; **backend** holds the register; **APIs** carry **JSON**; the **cloud** hosts that kitchen when a crowd arrives.

**Say-aloud checks:** Why is a pretty aarti PDF still Web 1.0-style? Why is a Like that dies when you close the tab not a product feature yet? Why is the API ask not “the backend”? Why must payment success be decided on the server? Why does HTTPS not prove the company is honest?

If any answer is shaky, reread that heading. You are ready for upcoming backend lessons when these five answers are short and clear.

---

## Important Commands, Libraries, Terminologies Used

| Term / Idea | Meaning (quick revision) |
|---|---|
| **Internet vs web** | Roads vs pages and links in a browser |
| **Website / browser** | A shop of pages / the clerk that fetches and draws |
| **Client / server** | Asks / listening program that answers |
| **Frontend / backend** | HTML, CSS, JS in the browser / rules and storage on the server |
| **URL / DNS / port / path** | Address / phone book / door / counter |
| **HTTP / HTTPS / GET / POST** | Protocol; encrypted pipe; read; submit a slip |
| **Status 200 / 404 / 500** | Success / not found / kitchen problem |
| **HTML / CSS / JavaScript** | Structure / look / movement |
| **Hyperlink / static page / form** | Door to another URL / same file for all / fields to send a slip |
| **Database / cookie / session** | Ledger / cloakroom token / locker record on the server |
| **Web 1.0 / Web 2.0 / UGC / account** | Read / participate / visitors write / named locker |
| **AJAX / DOM / cache / tab** | Partial update / in-memory tree / stored copy / one whiteboard |
| **JS runtime / event / handler** | Engine plus browser tools / signal / work that answers |
| **Endpoint / API / JSON / `fetch`** | One counter / menu / packing list / client asking |
| **Cloud / data centre / CDN** | Rented machines / warehouse / copies closer to users |
| **Node.js** | JavaScript **on the server**, not in Chrome |
| **Web 3.0** | High-level: semantic data and, in some talks, shared control |
