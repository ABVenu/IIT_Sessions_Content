# HTML Structure and Semantic Markup

## What You Will Learn in This Lesson

In the previous session, you practised **AI-assisted problem solving** for DSA — using tools like **ChatGPT** and **Claude** to clarify concepts, write **pseudocode**, trace algorithms step by step, and debug Python code on your local machine. You also reinforced **Git branching**, **merging**, and **collaboration** habits so experiments stay safe on feature branches.

In this lesson, you step into **web development** — the part of software users actually see and click. You will:

- Understand the **frontend developer's role** in building web applications
- Build **well-structured HTML pages** using headings, paragraphs, links, and images
- Write **semantic HTML** so pages are meaningful for browsers, search engines, and assistive tools
- Create **forms** with common **input types**, **labels**, and **buttons**

By the end, you will open a browser, view your own `.html` file, and explain why each tag exists — not just copy markup you do not understand.

---

## Introduction to Web Development and the Frontend Role

- **Official Definition:** **Web development** is building websites and web applications that run in a browser. **Frontend development** (client-side) focuses on everything the user sees, reads, and interacts with on screen.
- **In Simple Words:** If a website is a restaurant, the frontend is the dining area, menu design, and waiter — what guests experience directly.
- **Real-Life Example:** On Swiggy or Zomato, the buttons, photos, search box, and cart you tap are **frontend**. The kitchen and payment system behind the scenes are closer to **backend** work.

| Area | What it handles | Login page example |
|---|---|---|
| **Frontend** | Layout, text, buttons, forms | Email box, password field, "Login" button |
| **Backend** | Data storage, security, business rules | Checking if password matches account in database |
| **Full stack** | Both layers | Developer who builds the whole login flow |

**Frontend developer responsibilities:** turn designs into working pages; write **HTML** (structure), **CSS** (styling — later), and **JavaScript** (interactivity — later); support phones and laptops; care about **accessibility** for screen reader and keyboard users.

**Common doubt:** "Do I need to be artistic?" Not necessarily — HTML is about **meaning and organisation** more than decoration.

**How the browser fits in:** You enter a **URL** or click a link; the browser fetches an **HTML** file over **HTTP**, builds a **DOM** (Document Object Model — a tree of elements), and draws the page. Save `index.html` on your laptop and open it in Chrome — **no server needed** for early practice.

**Connecting idea:** HTML is your first frontend tool. Before colours and animations, you describe **what** is on the page in a way computers and humans both understand.

![Frontend is the dining area and menu guests interact with; backend is the kitchen and payment system behind the scenes — users see buttons, forms, and content built with HTML](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-01-frontend-backend-restaurant.png?v=20260721)

---

## HTML — The Skeleton of Every Web Page

- **Official Definition:** **HTML** (HyperText Markup Language) is a markup language that structures web content using **elements** made of **tags**.
- **In Simple Words:** HTML is labelled sections in a notebook — "Title here," "Paragraph here," "Image here" — so the browser knows what each piece is.
- **Real-Life Example:** A school exam paper has sections: Name, Roll Number, Questions. HTML tags are those printed section headings.

**Key ideas:** HTML **describes structure**, not step-by-step logic like Python. Tags usually come in **pairs** (`<tag>` … `</tag>`). Some tags are **self-closing** (`<img>`, `<input>`). Sloppy HTML causes layout and accessibility problems later.

**Logic to remember:** HTML answers **"What is this content?"** CSS answers **"How should it look?"** JavaScript answers **"What happens when the user clicks?"**

---

## The HTML Document Structure

- **Official Definition:** An **HTML document** uses **doctype**, **html**, **head**, and **body** to tell the browser which HTML version to use and where metadata vs visible content lives.
- **In Simple Words:** The **head** is backstage (title, settings); the **body** is the stage the audience sees.
- **Real-Life Example:** A wedding invitation envelope (head — small print) vs the inside card guests read (body — message, venue, RSVP).

Save as `my-first-page.html` and open in Chrome or Firefox:

```html
<!DOCTYPE html> <!-- Tells the browser this is HTML5 -->
<html lang="en"> <!-- Root element; lang helps screen readers -->
<head> <!-- Metadata — not shown as main content -->
  <meta charset="UTF-8"> <!-- Supports English and Indian language characters -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Mobile layout hint -->
  <title>My First Web Page</title> <!-- Text on the browser tab -->
</head>
<body> <!-- Everything visible goes here -->
  <h1>Welcome to Web Development</h1> <!-- Main heading — one per page -->
  <p>This is my first structured HTML page.</p> <!-- Paragraph -->
</body>
</html>
```

**How the code works:**

- `<!DOCTYPE html>` enables modern **HTML5** rendering
- `<head>` holds meta information — title, charset, viewport — not the article body
- `<meta charset="UTF-8">` ensures regional scripts display correctly
- `<title>` appears on the tab — important for bookmarks and search
- `<body>` holds every visible element

**Common mistakes:** forgetting `<!DOCTYPE html>`; placing `<h1>` inside `<head>`; missing closing tags.

**Element anatomy (quick reference):**

```text
<p class="intro">Hello, learner!</p>
│   │            └── Content the user reads
│   └── Attribute (optional extra info)
└── Tag name
```

**VS Code workflow tip:** install the **Live Server** extension if available — it refreshes the browser when you save. Without it, manual refresh after each save works perfectly for this lesson.

![HTML head is backstage metadata like a wedding envelope label; body is the opened invitation card with headings and paragraphs the guest actually reads](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-02-html-head-body-structure.png?v=20260721)

### Practice Activity: Build and Inspect Your Skeleton

1. Create folder `web-practice` on your Desktop and open it in VS Code.
2. Create `my-first-page.html`, paste the full code above, save.
3. Open the file in Chrome; use **View Page Source** to match tags to the rendered page.
4. Change `<title>` and `<h1>`, save, refresh (**Cmd+R** / **Ctrl+R**), confirm updates.

---

## Headings, Paragraphs, Links, and Images

Structured pages use headings as chapter titles, paragraphs for text, links for navigation, and images for visuals.

### Headings and paragraphs

- **Official Definition:** **Heading elements** (`<h1>`–`<h6>`) define hierarchical titles; **`<p>`** wraps text blocks.
- **In Simple Words:** Headings are chapter names; paragraphs are explanations underneath.
- **Real-Life Example:** Newspaper: big headline (`<h1>`), section "Sports" (`<h2>`), article text (`<p>`).

**Rules:** one **`<h1>`** per page; do not skip heading levels for styling; use `<p>` instead of many `<br>` tags for spacing.

```html
<h1>IIT Patna — Agentic Systems Course</h1>
<h2>Module Overview</h2>
<p>This module introduces web technologies used in modern agentic applications.</p>
<h3>What You Need</h3>
<p>A laptop, VS Code, and a modern browser are enough to start.</p>
```

![HTML input on the left shows h1 through h6 tags; browser output on the right renders each heading at a different size — h1 largest, h6 smallest — so hierarchy is visible even before CSS](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-06-html-headings-input-output.png?v=20260721)

![HTML input shows p, strong, and em tags; browser output shows normal paragraph text, bold important words, and italic emphasized words — structure in code, appearance in the browser](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-07-html-paragraph-emphasis-input-output.png?v=20260721)

**Lists and emphasis:**

- **Official Definition:** **Unordered lists** (`<ul>`) group items without sequence; **ordered lists** (`<ol>`) require order; **`<li>`** marks each item.
- **In Simple Words:** `<ul>` is a grocery list in any order; `<ol>` is a recipe — step 2 follows step 1.
- **Real-Life Example:** Exam instructions 1–5 use `<ol>`; optional pizza toppings use `<ul>`.

```html
<h2>Frontend Learning Path</h2>
<ol>
  <li>Learn HTML structure</li>
  <li>Add CSS styling</li>
  <li>Add JavaScript interactivity</li>
</ol>
<ul>
  <li>VS Code</li>
  <li>Chrome DevTools</li>
  <li>Git for version control</li>
</ul>
```

![HTML input shows ul and ol with li items; browser output shows a bullet list and a numbered list — same content, two different list styles](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-08-html-lists-input-output.png?v=20260721)

- **`<strong>`** — strong importance (usually bold); **`<em>`** — spoken emphasis (usually italic) — use for meaning, not decoration
- **`<hr>`** — thematic break between sections, like a ruled line in a notebook

### Links

- **Official Definition:** The **anchor element** (`<a>`) creates a **hyperlink** via the **href** attribute.
- **In Simple Words:** Link text is the door label; `href` is the address behind it.
- **Real-Life Example:** A railway platform sign — the sign is the link text; the platform is the destination.

```html
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML">MDN HTML Documentation</a>
<a href="about.html">About this course</a>
<a href="https://www.example.com" target="_blank" rel="noopener noreferrer">Visit Example Site</a>
```

**Common mistakes:** `href="www.google.com"` without `https://`; vague "click here" link text — screen readers lose context.

### Images

- **Official Definition:** The **img element** embeds an image using **src** (path) and **alt** (alternative text).
- **In Simple Words:** `src` is the photo file; `alt` is the description when the image cannot be seen.
- **Real-Life Example:** A Flipkart product photo with text below — if the photo fails, text still identifies the product.

```html
<img src="images/course-banner.png" alt="Banner showing web development tools on a laptop">
```

**Alt habits:** describe purpose, not "image of …"; use `alt=""` for purely decorative images.

**Path types for `src` and `href`:**

| Path type | Example | When to use |
|---|---|---|
| **Relative** | `images/photo.png` | File in your project folder |
| **Absolute URL** | `https://example.com/logo.png` | External hosted image |
| **Same-page anchor** | `#contact` | Jump to section on current page |

**Common mistake:** saving an image in `Images/` but writing `images/` in HTML — folder names are case-sensitive on many systems.

### Practice Activity: Personal Profile Mini-Page

Create `profile.html` with one `<h1>`, two `<h2>` sections ("About Me", "Useful Links"), two `<p>` paragraphs, two `<a>` links (MDN + local `hobbies.html`), and one `<img>` with meaningful `alt` text. Open in browser and test every link.

---

## Semantic HTML — Meaningful Page Structure

- **Official Definition:** **Semantic HTML** uses elements whose names describe **meaning** and **role** (`<nav>`, `<article>`, `<footer>`) rather than generic `<div>` alone.
- **In Simple Words:** Semantic tags are labelled trays in a tiffin carrier — dal, roti, rice — not anonymous boxes.
- **Real-Life Example:** Hospital signs say "Emergency," "OPD," "Pharmacy" — not "Room 1," "Room 2."

**Why semantics matter:** screen readers jump to `<nav>` or `<main>`; search engines identify main content; teammates read structure without guessing; CSS targets meaningful elements.

| Element | Purpose |
|---|---|
| `<header>` | Intro — logo, title |
| `<nav>` | Navigation links |
| `<main>` | Primary unique content (once per page) |
| `<section>` | Themed content group |
| `<article>` | Self-contained piece — blog post, news item |
| `<aside>` | Sidebar / related content |
| `<footer>` | Copyright, contact, closing info |

**`<div>` vs semantic tags:** `<div>` has **no meaning** — use only when no semantic tag fits.

![Semantic HTML is a labelled tiffin carrier with clear compartments for header, nav, main, and footer — not a confusing pile of identical unlabeled div boxes](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-03-semantic-html-tiffin-layout.png?v=20260721)

Save as `semantic-blog.html`:

```html
<!DOCTYPE html> <!-- HTML5 -->
<html lang="en"> <!-- Language -->
<head>
  <meta charset="UTF-8"> <!-- Encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Viewport -->
  <title>Semantic Blog Layout</title> <!-- Tab title -->
</head>
<body>
  <header> <!-- Site banner -->
    <h1>Learner's Web Journal</h1> <!-- Site title -->
    <p>Notes from my frontend journey</p> <!-- Tagline -->
  </header>
  <nav> <!-- Navigation -->
    <a href="index.html">Home</a> <!-- Home link -->
    <a href="profile.html">Profile</a> <!-- Profile link -->
    <a href="#contact">Contact</a> <!-- Same-page jump -->
  </nav>
  <main> <!-- Primary content -->
    <article> <!-- Standalone post -->
      <header> <!-- Article header -->
        <h2>Why Semantic HTML Matters</h2> <!-- Post title -->
        <p>Published on <time datetime="2026-07-21">21 July 2026</time></p> <!-- Date -->
      </header>
      <p>Semantic tags describe meaning, not just appearance.</p> <!-- Body text -->
      <p>They help screen readers and search engines understand your page.</p> <!-- More text -->
    </article>
    <section id="contact"> <!-- Contact section -->
      <h2>Contact</h2> <!-- Section title -->
      <p>Email: learner@example.com</p> <!-- Email line -->
    </section>
  </main>
  <aside> <!-- Sidebar -->
    <h3>Related Reading</h3> <!-- Sidebar heading -->
    <ul> <!-- Link list -->
      <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element">HTML element reference</a></li>
      <li><a href="profile.html">My profile page</a></li>
    </ul>
  </aside>
  <footer> <!-- Page footer -->
    <p>&copy; 2026 Learner's Web Journal. All rights reserved.</p> <!-- Copyright -->
  </footer>
</body>
</html>
```

**How the code works:** one `<main>` per page; `<nav>` wraps links only; `<article>` stands alone; `id="contact"` enables `#contact` jump links; nested `<header>` inside `<article>` is valid when scope differs.

**Common mistakes:** multiple `<main>` tags; `<div>` soup everywhere; `<section>` without a heading.

### Practice Activity: Semantic Page Audit

1. Open `semantic-blog.html` in the browser.
2. Temporarily replace semantic tags with `<div>` — note how **View Page Source** becomes harder to scan.
3. Restore semantic tags.
4. Add a second `<article>` with its own `<h2>` under `<main>`.
5. Confirm exactly one `<h1>`, one `<main>`, and headings in order.

**Self-check:** Without looking at notes, can you explain the difference between `<section>` and `<article>` in one sentence each?

---

## Forms and Input Elements

- **Official Definition:** An **HTML form** (`<form>`) collects user input and sends it via **action** and **method**. **Input elements** capture text, choices, and files.
- **In Simple Words:** A form is a website admission form — boxes to fill, options to tick, submit at the bottom.
- **Real-Life Example:** IRCTC booking — name, date, station dropdown, class preference, "Search Trains."

**Why forms matter:** login pages, search bars, surveys, checkout carts, and agentic prompt boxes all start as HTML forms.

| Element | Role |
|---|---|
| `<form>` | Container for inputs |
| `action` / `method` | Where and how data is sent (`get` or `post`) |
| `<label>` | Accessible name linked to input |
| `<input>` | Single-line control |
| `<textarea>` | Multi-line text |
| `<select>` / `<option>` | Dropdown |
| `<button>` | Submit or reset |

**GET vs POST:** **GET** puts data in the URL (fine for search, not passwords); **POST** sends data in the request body (standard for login). For local practice use `action="#"` — focus on structure first.

![HTML forms collect user input with labels, text fields, dropdowns, radio buttons, checkboxes, and submit — like a workshop registration form linked to every label for accessibility](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-04-html-form-inputs.png?v=20260721)

Save as `registration-form.html`:

```html
<!DOCTYPE html> <!-- HTML5 -->
<html lang="en"> <!-- Language -->
<head>
  <meta charset="UTF-8"> <!-- Encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Viewport -->
  <title>Course Registration Form</title> <!-- Tab title -->
</head>
<body>
  <header> <!-- Header -->
    <h1>Agentic Systems — Workshop Registration</h1> <!-- Title -->
    <p>Fill the form below to save your seat.</p> <!-- Instructions -->
  </header>
  <main> <!-- Main area -->
    <form action="#" method="post"> <!-- Form; # = local practice -->
      <fieldset> <!-- Field group -->
        <legend>Personal Details</legend> <!-- Group label -->
        <label for="full-name">Full Name</label> <!-- Label -->
        <input type="text" id="full-name" name="fullName" required placeholder="Enter your full name"> <!-- Text input -->
        <label for="email">Email Address</label> <!-- Email label -->
        <input type="email" id="email" name="email" required placeholder="you@example.com"> <!-- Email input -->
        <label for="phone">Mobile Number</label> <!-- Phone label -->
        <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" placeholder="10-digit number"> <!-- Phone input -->
      </fieldset>
      <fieldset> <!-- Second group -->
        <legend>Workshop Preferences</legend> <!-- Group label -->
        <label for="track">Preferred Track</label> <!-- Dropdown label -->
        <select id="track" name="track" required> <!-- Dropdown -->
          <option value="">Select a track</option> <!-- Default empty -->
          <option value="frontend">Frontend Foundations</option> <!-- Option 1 -->
          <option value="agents">Building AI Agents</option> <!-- Option 2 -->
        </select>
        <p>Session Mode</p> <!-- Radio question -->
        <label><input type="radio" name="mode" value="online" required> Online</label> <!-- Radio A -->
        <label><input type="radio" name="mode" value="offline"> Offline</label> <!-- Radio B -->
        <p>Topics (select all that apply)</p> <!-- Checkbox question -->
        <label><input type="checkbox" name="topics" value="html"> HTML &amp; CSS</label> <!-- Check 1 -->
        <label><input type="checkbox" name="topics" value="js"> JavaScript Basics</label> <!-- Check 2 -->
        <label for="notes">Additional Notes</label> <!-- Textarea label -->
        <textarea id="notes" name="notes" rows="4" placeholder="Any questions?"></textarea> <!-- Multi-line -->
      </fieldset>
      <button type="submit">Submit Registration</button> <!-- Submit -->
      <button type="reset">Clear Form</button> <!-- Reset -->
    </form>
  </main>
  <footer><p>Email used only for workshop updates.</p></footer> <!-- Footer -->
</body>
</html>
```

**How the code works:**

- `<label for="id">` + matching `id` — clicking label focuses field (better on mobile)
- `name` becomes the key when data reaches a server
- `type="email"` gives free format validation; `required` blocks empty submit
- Radio buttons share `name="mode"` — only one choice; checkboxes allow many
- `<button type="submit">` sends data; `<button type="reset">` clears fields

**Common input types:**

| type | Use case |
|---|---|
| `text` | General single-line text |
| `email` | Email with basic validation |
| `password` | Hidden characters |
| `number` | Numeric values with min/max |
| `tel` | Phone numbers |
| `date` | Date picker |
| `radio` | Exactly one choice from a set |
| `checkbox` | Zero or more choices |
| `file` | Upload from device |

**`<fieldset>` and `<legend>`:** group related inputs visually and for screen readers — like boxed sections on a printed form labelled "Personal Details" and "Preferences."

**Common mistakes:** missing `name`; labels not tied to `id`; using `type="text"` for email when `type="email"` is free validation; `<button>` without `type` inside a form defaults to submit and may send half-filled data.

### Practice Activity: Build Your Own Feedback Form

Create `feedback.html` with name (`text`, required), email (`email`, required), rating (`select` 1–5), recommend yes/no (radio), two checkboxes, `<textarea>`, submit and reset. Submit empty to see `required` messages; fill and submit with `action="#"` (reload is expected without backend).

---

## Accessibility Best Practices in Semantic HTML

- **Official Definition:** **Web accessibility** means people with disabilities can perceive, navigate, and interact with content effectively.
- **In Simple Words:** Build a ramp alongside stairs — same building for everyone.
- **Real-Life Example:** Zebra crossings and audio traffic signals help visually impaired pedestrians; accessible HTML provides equivalent signals in code.

**Who benefits:** screen reader users, keyboard-only users, people with colour blindness, users on slow networks when images fail.

| Practice | Why it helps | Common error |
|---|---|---|
| One `<h1>` per page | Clear main topic | Multiple `<h1>` for styling |
| Logical heading order | Predictable outline | Skipping levels |
| `<label>` tied to inputs | Announces field purpose | Placeholder-only labels |
| Meaningful link text | Context for assistive tech | "Click here" everywhere |
| `alt` on informative images | Content when unseen | Missing or keyword-stuffed alt |
| Native `<button>` | Keyboard support | Fake `<div onclick>` buttons |

**Keyboard test:** open `registration-form.html`, press **Tab** through fields, **Space** on checkboxes, **Enter** to submit — every control should be reachable without a mouse.

**ARIA rule:** use native HTML first; add **Accessible Rich Internet Applications** attributes only when native elements cannot express the role.

**Common doubt:** accessibility is mostly good structure — labels, headings, alt text — which also helps teammates read your code.

**Colour and contrast note:** readable text contrast is part of accessibility — you will control colours with CSS later. For now, rely on browser defaults and avoid light grey text on white when you add custom styles.

**Landmark navigation:** screen reader users can jump between `<header>`, `<nav>`, `<main>`, and `<footer>` — another reason semantic HTML is not optional decoration.

![Web accessibility means building a ramp alongside stairs — keyboard users, screen readers, and meaningful labels reach the same website entrance as everyone else](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session14/session14-05-accessibility-ramp-stairs.png?v=20260721)

### Practice Activity: Accessibility Quick Audit

1. Open `profile.html` or `registration-form.html`.
2. Tab through every interactive element — can you reach all links, inputs, and buttons?
3. Read each link text aloud — does it make sense without surrounding context?
4. Check every `<img>` has appropriate `alt` and every input has a visible `<label>`.
5. Fix one issue you find and re-test.

---

## Putting It Together and Debugging

### Practice Activity: Portfolio Landing Page

Create `portfolio.html` combining structure, semantics, links, images, and a form:

1. `<header>` — your name and one-line tagline
2. `<nav>` — links to `#about`, `#projects`, `#contact`
3. `<main>` with three `<section>` blocks matching those ids
4. About section — one `<img>` plus two `<p>` paragraphs
5. Projects section — `<ul>` with two projects and short descriptions
6. Contact section — form with name, email, message, submit button
7. `<footer>` — copyright line; link to `profile.html`

**Quality checks:** **View Page Source** — is the outline readable without CSS? Run keyboard Tab test. Every `<img>` has `alt`; every input has `<label>`.

| Problem | Likely cause | Fix |
|---|---|---|
| Raw tags visible | Saved as `.txt` | Save as `.html`, UTF-8 |
| Broken image | Wrong `src` path | Check folder and filename |
| Link goes wrong | Missing `https://` | Full URL for external sites |
| Both radios selected | Different `name` values | Same `name`, different `value` |
| Form does nothing | No backend at `action` | Expected in practice |

Use **right-click → Inspect** in Chrome (**DevTools → Elements**) to compare live DOM with your VS Code file.

**Git habit for web practice:** create a folder `web-practice`, run `git init`, and commit after each working page — `my-first-page.html`, `profile.html`, `semantic-blog.html`, `registration-form.html`, `portfolio.html`. Same feature-branch discipline from earlier lessons keeps experiments organised.

### Quick Self-Check Before You Move On

- Can you write a valid HTML5 skeleton from memory — `<!DOCTYPE>`, `<head>`, `<body>`?
- Can you explain when to use `<section>` vs `<article>` vs `<main>`?
- Can you build a form with labels, email validation, radio, checkbox, and submit?
- Can you describe three accessibility habits you applied in your practice files?
- Did you open at least one page in the browser and inspect its source?

If any answer is "not yet," repeat one practice activity from this lesson before moving on.

---

## How This Fits Your Journey Ahead

You now speak the **structure language of the web**. Every agentic dashboard, chat UI, or tool interface sits on HTML bones — buttons, forms, text, navigation.

In upcoming lessons you will add **CSS** for layout and colour, and **JavaScript** for clicks and APIs. Semantic habits — labels, headings, meaningful tags — stay valuable when AI tools generate markup; you will judge whether output is professional or sloppy.

---

## Key Takeaways

- **Frontend developers** build what users see; **HTML** is the structural foundation beneath CSS and JavaScript.
- Valid documents use `<!DOCTYPE html>`, `<head>` for metadata, and `<body>` for visible content.
- **Semantic elements** describe meaning, improve accessibility, and make code maintainable.
- **Forms** need `<label>`, correct **input types**, and **`name`** attributes; link labels with `for` / `id`.
- **Accessibility** comes from logical headings, descriptive links, `alt` text, and keyboard-friendly native controls.

These skills let you read, write, and review real web pages — the same surfaces agentic applications show users every day.

---

## Important Commands, Libraries, Terminologies Used

| Term / Element | Meaning in Simple Words |
|---|---|
| **Web development** | Building websites and web applications |
| **Frontend** | User-facing layout, content, forms in the browser |
| **Backend** | Server, database, logic users do not directly see |
| **HTML** | HyperText Markup Language — structures content with tags |
| **Browser / DOM** | Software that renders HTML into a tree of elements |
| **`<!DOCTYPE html>`** | Declares HTML5 document |
| **`<head>` / `<body>`** | Metadata vs visible content |
| **`<h1>`–`<h6>` / `<p>`** | Headings and paragraphs |
| **`<a href>` / `<img src alt>`** | Links and images |
| **`<header>` / `<nav>` / `<main>` / `<footer>`** | Semantic layout regions |
| **`<section>` / `<article>` / `<aside>`** | Grouped, standalone, sidebar content |
| **`<form>` / `action` / `method`** | Form container and submission target |
| **`<label>` / `<input>` / `<textarea>` / `<select>`** | Form controls |
| **`<button type="submit">`** | Sends form data |
| **`required`** | Browser blocks empty required fields |
| **Semantic HTML** | Tags chosen for meaning, not only layout |
| **Accessibility (a11y)** | Designing for users with diverse abilities |
| **GET / POST** | HTTP methods for sending form data |
| **VS Code / View Page Source / DevTools** | Edit, view source, and inspect live pages |
