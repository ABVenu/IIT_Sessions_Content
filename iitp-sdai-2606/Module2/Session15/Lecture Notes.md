# CSS Fundamentals – Selectors, Properties & Box Model

## What You Will Learn in This Lesson

In the previous session, you built the **structure** of web pages with **HTML** — headings, paragraphs, links, images, **semantic tags**, and **forms**. Those pages worked in the browser, but they looked plain: default black text, blue links, and stacked boxes with no spacing design.

In this lesson, you add **CSS** (Cascading Style Sheets) — the language that controls **how** HTML looks. You will:

- **Link and apply CSS** to HTML documents using inline, internal, and external stylesheets
- Use **element, class, and id selectors** with core properties for colour, typography, backgrounds, and borders
- **Explain and apply the CSS box model** — margin, padding, border, and content area
- **Style a complete HTML page** using the practice files you already created

By the end, your `profile.html`, `registration-form.html`, or `portfolio.html` will look like a real website — not a raw document.

---

## Introduction to CSS — Styling the Web

- **Official Definition:** **CSS** (Cascading Style Sheets) is a stylesheet language that describes the presentation of HTML documents — colours, fonts, spacing, layout, and visual design.
- **In Simple Words:** If HTML is the skeleton of a house, CSS is the paint, tiles, curtains, and furniture arrangement.
- **Real-Life Example:** A school notice board has the **text** (HTML) and the **coloured paper, borders, and font size** you choose (CSS). Same message, different look.

| Layer | Job | Simple analogy |
|---|---|---|
| **HTML** | Structure and meaning | Blueprint of rooms |
| **CSS** | Visual design | Paint, tiles, lighting |
| **JavaScript** | Behaviour and interactivity | Switches, doorbells, smart locks |

**Cascading explained:** When two rules target the same element, the browser picks a winner using specificity and source order.

**Connecting idea:** You already know **what** is on the page. CSS answers **how it should look**.

![HTML is the bare house skeleton — rooms and structure; CSS is the paint, curtains, tiles, and lighting that make the same house look finished and welcoming](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session15/session15-01-html-skeleton-css-paint-house.png?v=20260727)

---

## Three Ways to Add CSS to HTML

- **Official Definition:** CSS can be applied **inline** (on one element), **internally** (inside `<style>` in `<head>`), or **externally** (linked `.css` file).
- **In Simple Words:** Inline is a sticky note on one item; internal is a style sheet inside the notebook cover; external is a separate design booklet shared by many pages.
- **Real-Life Example:** A wedding hall — inline is one decorated chair; internal is decorations only for that hall today; external is the decorator's master theme used at every venue.

### Inline CSS

Style sits directly on a single tag using the **`style`** attribute.

```html
<h1 style="color: navy; text-align: center;">Welcome to CSS</h1> <!-- Inline on one heading -->
<p style="color: #333333; font-size: 18px;">Styled directly on this tag only.</p> <!-- Inline on paragraph -->
```

**When to use:** quick experiments only. **Downside:** repeating styles on many tags is painful; one colour change means editing every tag.

### Internal CSS

Rules live inside `<style>` in the `<head>` and apply to that one HTML file.

```html
<head> <!-- Page head section -->
  <title>Internal CSS Demo</title> <!-- Tab title -->
  <style> <!-- Internal stylesheet -->
    h1 { color: navy; text-align: center; } /* Every h1 on this page */
    p { color: #333333; font-size: 18px; line-height: 1.6; } /* Every paragraph */
  </style> <!-- End styles -->
</head>
```

**When to use:** single-page demos. **Downside:** ten HTML files means copying the same `<style>` block ten times.

### External CSS (recommended)

Styles live in a separate file linked from every HTML page. Add this inside `<head>`:

```html
<link rel="stylesheet" href="styles.css"> <!-- Link external CSS file -->
```

**How linking works:**

- `<link rel="stylesheet" href="styles.css">` tells the browser to download and apply `styles.css`
- The `href` path must match your folder — same folder or `css/styles.css` if nested
- Change `styles.css` once; every linked page updates on refresh
- External CSS is the professional default for multi-page sites

**Common mistakes:** wrong `href` path; forgetting `rel="stylesheet"`; saving CSS as `.txt` instead of `.css`.

| Method | Where styles live | Best for |
|---|---|---|
| **Inline** | `style=""` on one tag | Quick one-off tests |
| **Internal** | `<style>` in `<head>` | Single-page prototypes |
| **External** | Linked `.css` file | Real websites and portfolios |

![Three ways to style a page — Inline is one decorated chair with a sticky note; Internal is decorations for one hall; External is a shared design booklet used across many venues](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session15/session15-02-inline-internal-external-css.png?v=20260727)

### Practice Activity: Compare All Three Methods

1. In your `web-practice` folder, create three small HTML files using inline, internal, and external CSS with the same navy heading and grey paragraph.
2. Change the heading colour to `#0d47a1` in each approach — notice which is fastest to update.
3. Keep `styles.css` — you will extend it through this lesson.

---

## CSS Selectors — Element, Class, and ID

- **Official Definition:** A **CSS rule** has a **selector** (what to style) and a **declaration block** (`property: value;` pairs). **Type selectors** match tag names; **class selectors** match `class` attributes; **ID selectors** match unique `id` attributes.
- **In Simple Words:** Element selector paints every chair; class selector paints chairs tagged "VIP"; ID selector paints the one chair with a nameplate.
- **Real-Life Example:** A coaching centre — "all benches" (element), "front-row benches" (class), "Director's chair" (id).

```css
p { /* Element selector — all paragraphs */
  color: #333333; /* Text colour */
  font-size: 18px; /* Text size */
  margin-bottom: 12px; /* Space below each paragraph */
}

.intro { /* Class selector — reusable highlight */
  font-size: 20px; /* Larger intro text */
  font-weight: bold; /* Bold emphasis */
  color: #1b5e20; /* Dark green text */
}

#content { /* ID selector — unique main wrapper */
  max-width: 800px; /* Limit line length for readability */
  margin: 0 auto; /* Centre the block horizontally */
}

a:hover { /* Pseudo-class — mouse over any link */
  text-decoration: underline; /* Show underline on hover */
}
```

**HTML examples for class and id:**

```html
<p class="intro">This opening paragraph stands out.</p> <!-- Reusable class -->
<button class="btn-primary">Submit</button> <!-- Same class on a button -->
<main id="content"><section id="about">About</section></main> <!-- Unique ids -->
```

**Specificity order (who wins):** inline style beats ID; ID beats class; class beats element. When equal, the **later** rule wins.

| Selector type | Syntax | Example use |
|---|---|---|
| **Element** | `tagname` | Style all `<p>` tags |
| **Class** | `.classname` | Reusable card, button, highlight |
| **ID** | `#idname` | One main wrapper, one hero banner |

![CSS selectors like a coaching centre — Element paints every bench; Class paints VIP-tagged front-row benches; ID paints the single Director chair with a nameplate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session15/session15-03-css-selectors-benches.png?v=20260727)

**Common mistakes:** using IDs when a class would work; duplicate IDs on one page; forgetting `.` or `#` in CSS.

### Practice Activity: Selector Lab

1. Create `selector-lab.html` with one `<h1>`, three `<p>` (two with `class="note"`), and `<div id="sidebar">`.
2. Link `selector-lab.css` — style all `p` grey, `.note` with yellow background, `#sidebar` with blue background and padding.
3. Add `class="note"` to another element and confirm the class rule applies without changing CSS.

---

## Core CSS Properties — Colour, Typography, Backgrounds, Borders

Selectors choose **who** gets styled. **Properties** choose **what** changes.

### Colour and typography

- **Official Definition:** **`color`** sets text colour; **`background-color`** fills behind an element. **Typography properties** control font family, size, weight, alignment, and line spacing.
- **In Simple Words:** `color` is ink; `background-color` is paper; typography is how neat, big, or bold your writing looks.
- **Real-Life Example:** A Holi flyer — pink headline on white paper; a newspaper headline is large and bold while body text is smaller with comfortable spacing.

```css
body { /* Default text for entire page */
  font-family: "Segoe UI", Tahoma, sans-serif; /* Font stack with fallbacks */
  font-size: 16px; /* Base reading size */
  line-height: 1.6; /* Comfortable line spacing */
  color: #222222; /* Near-black body text */
}

.highlight { /* Emphasised badge text */
  color: #ffffff; /* White text */
  background-color: #e65100; /* Deep orange background */
  padding: 4px 8px; /* Space so background does not touch letters */
}
```

**Colour formats:** named (`navy`), **hex** (`#1565c0`), **rgb** (`rgb(21, 101, 192)`). Hex is common in professional work.

**Accessibility note:** light grey text on white fails for many users — aim for strong contrast.

| Property | What it does |
|---|---|
| `font-family` / `font-size` | Which font and how large |
| `font-weight` / `line-height` | Boldness and line spacing |
| `text-align` | Left, centre, right |
| `color` / `background-color` | Text ink and fill behind content |

### Backgrounds and borders

- **Official Definition:** **`background-color`** and **`background-image`** fill the element box. **`border`** sets width, style, and colour; **`border-radius`** rounds corners.
- **In Simple Words:** Background is wallpaper; border is the photo frame on the wall.
- **Real-Life Example:** A Diwali sale banner with festive colour behind offer text; a ration card with a printed border separating it from the table.

```css
.card { /* White content card on grey page */
  background-color: #ffffff; /* White card surface */
  padding: 20px; /* Inner spacing */
  margin-bottom: 16px; /* Gap between stacked cards */
  border: 1px solid #dde4ec; /* Light card border */
  border-radius: 8px; /* Rounded corners */
}

input:focus, textarea:focus { /* Active form field */
  border: 2px solid #1565c0; /* Blue focus border */
  outline: none; /* Remove default if replacing with border */
}
```

**Focus reminder:** do not remove keyboard focus styles without replacing them — tab users need visible focus.

## The CSS Box Model — Margin, Padding, Border, Content

- **Official Definition:** The **CSS box model** describes every element as a rectangular box with **content**, **padding**, **border**, and **margin** layers from inside to outside.
- **In Simple Words:** Content is the gift; padding is bubble wrap; border is the cardboard box; margin is empty space before the next package on the shelf.
- **Real-Life Example:** A tiffin box — food (content), gap to the wall (padding), steel edge (border), space between boxes on the desk (margin).

| Layer | What it is | Analogy |
|---|---|---|
| **Content** | Text, image, or child elements | The gift inside |
| **Padding** | Space between content and border | Bubble wrap inside the box |
| **Border** | Visible edge around padding | Cardboard or steel walls |
| **Margin** | Space outside the border | Gap between boxes on a shelf |

![CSS box model as a tiffin box — food is Content, gap to the wall is Padding, steel rim is Border, and space between tiffins on the desk is Margin](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session15/session15-04-css-box-model-tiffin.png?v=20260727)

```css
.demo-box { /* Example box to visualise layers */
  width: 300px; /* Content area width */
  padding: 20px; /* Space inside border around content */
  border: 5px solid #1565c0; /* Visible blue border */
  margin: 30px auto; /* Space outside; auto centres horizontally */
  background-color: #e3f2fd; /* Light blue shows padding area */
}

* { /* Apply to every element */
  box-sizing: border-box; /* Width includes padding and border */
}
```

**DevTools tip:** Right-click → **Inspect** → box model diagram shows content, padding, border, and margin as coloured layers.

**`box-sizing: border-box`:** Without it, `width: 300px` grows wider when you add padding and border. With `border-box`, the total visible box stays 300px.

**Common mistakes:** using `<br>` for spacing; forgetting `border-box`; fighting width calculations.

### Practice Activity: Box Model Detective

1. Create `box-model.html` with three `<div class="demo-box">` blocks.
2. Change only `padding` on one, `margin` on another, `border-width` on the third — describe what moved.
3. Open DevTools box model and add `box-sizing: border-box` with `width: 250px` and `padding: 40px` — confirm total width stays 250px.

---

## Styling Your HTML Pages — Hands-On Project

You already have structured HTML from earlier practice. Attach a shared stylesheet and polish the full page.

**Step 1 — Link CSS in every HTML file** (inside `<head>`):

```html
<link rel="stylesheet" href="styles.css"> <!-- Shared design for this page -->
```

**Step 2 — Full `styles.css` for your practice site**

```css
/* Base reset and defaults */

* { /* All elements */
  box-sizing: border-box; /* Predictable width calculations */
}

body { /* Whole page */
  font-family: "Segoe UI", Tahoma, sans-serif; /* Clean readable font */
  font-size: 16px; /* Base text size */
  line-height: 1.6; /* Comfortable line spacing */
  color: #222222; /* Dark body text */
  background-color: #f0f4f8; /* Soft grey-blue background */
  margin: 0; /* Remove browser default margin */
  padding: 0; /* Zero padding on body */
}

/* Typography and links */

h1 { /* Main title once per page */
  color: #0d47a1; /* Deep blue brand colour */
  text-align: center; /* Centre page title */
  margin-top: 24px; /* Space from top */
  margin-bottom: 8px; /* Space before subtitle */
}

h2 { /* Section headings */
  color: #1565c0; /* Slightly lighter blue */
  border-bottom: 2px solid #bbdefb; /* Underline accent */
  padding-bottom: 8px; /* Space between text and line */
  margin-top: 32px; /* Space above sections */
}

p { /* Paragraphs */
  margin-bottom: 16px; /* Space between paragraphs */
}

a { /* Links */
  color: #0d47a1; /* Link colour matches headings */
  text-decoration: none; /* No underline by default */
}

a:hover { /* Mouse over link */
  text-decoration: underline; /* Underline on hover */
}

/* Layout regions */

header { /* Top banner area */
  background-color: #ffffff; /* White header bar */
  padding: 24px 20px; /* Inner spacing */
  border-bottom: 1px solid #dde4ec; /* Subtle separator */
  text-align: center; /* Centre header content */
}

main { /* Primary content wrapper */
  max-width: 720px; /* Readable line length */
  margin: 24px auto; /* Centre column with vertical gap */
  padding: 0 16px; /* Side padding on small screens */
}

footer { /* Bottom area */
  text-align: center; /* Centre footer text */
  padding: 20px; /* Inner spacing */
  color: #666666; /* Muted footer colour */
  font-size: 14px; /* Slightly smaller text */
}

nav { /* Navigation links row */
  text-align: center; /* Centre nav links */
  padding: 12px; /* Nav bar padding */
  background-color: #e3f2fd; /* Light blue nav background */
  margin-bottom: 16px; /* Space below nav */
}

/* Profile page */

.profile-photo { /* Class on profile image */
  display: block; /* Block so margin auto works */
  margin: 0 auto 20px auto; /* Centre image with space below */
  border: 3px solid #1565c0; /* Blue frame */
  border-radius: 50%; /* Circular photo */
  width: 140px; /* Fixed width */
  height: 140px; /* Fixed height */
  object-fit: cover; /* Crop neatly */
}

/* Form styling */

form { /* Form container */
  background-color: #ffffff; /* White form card */
  padding: 24px; /* Inner spacing */
  border-radius: 8px; /* Rounded corners */
  border: 1px solid #dde4ec; /* Light border */
}

fieldset { /* Grouped inputs */
  border: 1px solid #cccccc; /* Group border */
  border-radius: 6px; /* Rounded group box */
  padding: 16px; /* Space inside group */
  margin-bottom: 20px; /* Space between groups */
}

label { /* Input labels */
  display: block; /* Label on its own line */
  margin-top: 12px; /* Space above each label */
  margin-bottom: 4px; /* Small gap before input */
  font-weight: 600; /* Semi-bold labels */
}

input, select, textarea { /* All form controls */
  width: 100%; /* Full width of parent */
  padding: 10px; /* Comfortable click target */
  border: 1px solid #bbbbbb; /* Default border */
  border-radius: 4px; /* Slight rounding */
  font-size: 16px; /* Prevent zoom on mobile iOS */
  margin-bottom: 8px; /* Space below each control */
}

input:focus, textarea:focus, select:focus { /* Active field */
  border-color: #1565c0; /* Blue focus highlight */
}

button { /* Submit and reset buttons */
  padding: 12px 24px; /* Clickable padding */
  font-size: 16px; /* Readable button text */
  border: none; /* Remove default border */
  border-radius: 4px; /* Rounded button */
  cursor: pointer; /* Pointer on hover */
  margin-right: 10px; /* Space between buttons */
  margin-top: 12px; /* Space above button row */
}

button[type="submit"] { /* Submit button only */
  background-color: #1565c0; /* Blue primary action */
  color: #ffffff; /* White text */
}

/* Portfolio sections */

section { /* Content sections */
  background-color: #ffffff; /* White section cards */
  padding: 24px; /* Inner spacing */
  margin-bottom: 24px; /* Gap between sections */
  border-radius: 8px; /* Rounded cards */
  border: 1px solid #dde4ec; /* Light card border */
}

#contact { /* Contact section accent */
  border-left: 4px solid #1565c0; /* Left blue stripe */
}
```

**How the code works:**

- Base `body` rules set fonts and background for every linked file
- Semantic regions get spacing without extra `<div>` wrappers
- `.profile-photo` styles only tagged images
- `max-width` and `margin: auto` create a centred readable column

### Practice Activity: Style Your Practice Pages

1. Add `<link rel="stylesheet" href="styles.css">` to `profile.html`, `registration-form.html`, and `portfolio.html`.
2. On `profile.html`, add `class="profile-photo"` to your image; add `.intro` in `styles.css` for the first paragraph.
3. On `registration-form.html`, confirm form card, inputs, and submit button; tab through fields to test focus.
4. On `portfolio.html`, confirm section cards and `id="contact"` accent border; compare before/after in the browser.

### Debugging CSS — Quick Fixes

| Problem | Likely cause | Fix |
|---|---|---|
| No styles applied | Wrong `href` path | Check filename and folder |
| Rule ignored | Typo in selector | Match class/id spelling exactly |
| Layout too wide | No `box-sizing` | Add `* { box-sizing: border-box; }` |
| Text unreadable | Low contrast | Darken text or lighten background |

**DevTools habit:** **Inspect** → **Styles** panel shows active rules and crossed-out overrides.

### Quick Self-Check Before You Move On

- Can you explain inline, internal, and external CSS?
- Can you write element, class, and ID rules from memory?
- Can you name the four box model layers inside to outside?
- Did you link `styles.css` to at least two HTML pages?

If any answer is "not yet," repeat one practice activity before moving on.

---

## How This Fits Your Journey Ahead

You now control both **structure** (HTML) and **presentation** (CSS). Together they form the visible face of every web app, dashboard, and agent interface.

In upcoming lessons you will add **layout techniques**, responsive design, and **JavaScript** for interactivity. External stylesheets, reusable classes, and `border-box` stay central as UIs grow more advanced.

---

## Key Takeaways

- **CSS** separates visual design from HTML — colours, fonts, spacing, and borders live in stylesheets.
- Link CSS **externally** with `<link rel="stylesheet" href="styles.css">` for maintainable multi-page sites.
- **Selectors** target elements (tag), groups (`.class`), or unique items (`#id`); classes are reusable, IDs unique per page.
- The **box model** layers content → padding → border → margin; use `box-sizing: border-box` for predictable widths.
- Styling **profile**, **form**, and **portfolio** pages proves one shared CSS file can make plain HTML look professional.

These skills let you read, write, and debug styles on any frontend — the same surfaces agentic tools present to users every day.

---

## Important Commands, Libraries, Terminologies Used

| Term / Property | Meaning in Simple Words |
|---|---|
| **CSS** | Cascading Style Sheets — controls visual design of HTML |
| **Inline / Internal / External CSS** | `style=""` on tag; `<style>` in head; linked `.css` file |
| **Selector** | Pattern choosing which elements to style |
| **Element / Class / ID selector** | `p`, `.classname`, `#idname` |
| **`color` / `background-color`** | Text colour and fill behind content |
| **`font-family` / `font-size` / `line-height`** | Font choice, size, line spacing |
| **`border` / `border-radius`** | Edge frame and rounded corners |
| **`padding` / `margin`** | Space inside vs outside the border |
| **Box model** | Content + padding + border + margin |
| **`box-sizing: border-box`** | Width includes padding and border |
| **`:hover` / `:focus`** | Styles on mouse hover or keyboard focus |
| **DevTools** | Browser inspect tool for styles and box model |
