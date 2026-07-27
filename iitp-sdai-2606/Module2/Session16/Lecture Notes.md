# CSS Layout – Flexbox and Grid

## What You Will Learn in This Lesson

In the previous session, you learnt **CSS fundamentals** — linking stylesheets, **selectors**, core **properties**, and the **box model**. Your pages looked better, but content still stacked in one vertical column. Real websites place a header across the top, cards side by side, and a footer at the bottom.

In this lesson, you learn **CSS layout** with **Flexbox** and **Grid**. You will:

- Build **one-dimensional layouts** with Flexbox — rows and columns of items that align and space themselves
- Create **two-dimensional layouts** with CSS Grid — rows and columns at the same time
- Combine Flexbox and Grid to build **header**, **main**, and **footer** page sections
- Complete guided **layout exercises** and watch layouts adjust when you resize the browser window

By the end, you will arrange page sections like a floor plan — not a single long list of stacked boxes.

---

## Why Layout Matters

- **Official Definition:** **CSS layout** controls how elements are positioned and sized relative to each other and to the viewport.
- **In Simple Words:** Layout is furniture arrangement in a room — where the sofa, table, and chairs sit, and how they share the space.
- **Real-Life Example:** A railway reservation chart shows seats in rows and columns. Without layout, every seat name would print in one long vertical list.

**Default browser behaviour:** Block elements (`div`, `section`, `header`) stack top to bottom and stretch full width. Flexbox and Grid give you control over **direction**, **alignment**, and **space distribution**.

**Connecting idea:** You already style colours and spacing. Layout answers **where each block sits** and **how it shares the screen**.

---

## Introduction to Flexbox

- **Official Definition:** **Flexbox** (Flexible Box Layout) is a one-dimensional CSS layout model. You set a **flex container**, and its direct children become **flex items** that align along a main axis (row or column).
- **In Simple Words:** Flexbox is a row of seats in a bus — you decide facing direction, gaps between seats, and whether they stretch or sit centred.
- **Real-Life Example:** A school lunch queue — students stand in one line (one dimension). You can space them evenly or pack them to the left.

**When to use Flexbox:** nav bars, button groups, card rows, centring one item, or any layout that mainly flows in **one direction**.

![Flexbox is like a bus seat row — one main axis of items inside a container, with gaps and direction you control](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session16/session16-01-flexbox-bus-seats.png?v=20260727)

### Creating a flex container

```css
.nav { /* Navigation bar container */
  display: flex; /* Turn this element into a flex container */
  gap: 16px; /* Space between flex items */
}
```

**Key idea:** `display: flex` applies to the **parent**. Children automatically become flex items — you do not need `display: flex` on every child.

---

## Flex Direction and Wrapping

- **Official Definition:** **`flex-direction`** sets the main axis (`row` or `column`). **`flex-wrap`** allows items to move to the next line when space runs out.
- **In Simple Words:** Direction is whether the queue goes left-to-right or top-to-bottom. Wrap is letting overflow people start a new line.
- **Real-Life Example:** Books on a shelf (row). When the shelf fills, books continue on the next shelf (wrap).

```css
.row { /* Horizontal flex row */
  display: flex; /* Flex container */
  flex-direction: row; /* Main axis left to right (default) */
  flex-wrap: wrap; /* Items wrap to next line if needed */
  gap: 12px; /* Space between items */
}

.column { /* Vertical flex column */
  display: flex; /* Flex container */
  flex-direction: column; /* Main axis top to bottom */
  gap: 12px; /* Space between stacked items */
}
```

| Property | Common values | Meaning |
|---|---|---|
| `flex-direction` | `row`, `column` | Main axis direction |
| `flex-wrap` | `nowrap`, `wrap` | Stay on one line or wrap |
| `gap` | `12px`, `1rem` | Space between items |

**Common mistake:** setting `flex-direction` on a child instead of the parent container.

---

## Justify Content and Align Items

- **Official Definition:** **`justify-content`** distributes space along the **main axis**. **`align-items`** aligns items along the **cross axis**.
- **In Simple Words:** Justify is left/centre/right along the line. Align is how tall items sit relative to that line.
- **Real-Life Example:** Photos on a wall shelf — justify spreads them left to right; align decides if they sit on the bottom edge or float in the middle of the shelf height.

```css
.toolbar { /* Top toolbar layout */
  display: flex; /* Flex container */
  justify-content: space-between; /* Push items to opposite ends */
  align-items: center; /* Vertically centre items in the bar */
  padding: 12px 20px; /* Inner spacing */
  background-color: #0d47a1; /* Blue bar background */
  color: #ffffff; /* White text */
}

.centre-box { /* Centre a single card on the page */
  display: flex; /* Flex container */
  justify-content: center; /* Centre horizontally */
  align-items: center; /* Centre vertically */
  min-height: 200px; /* Give the container some height */
  background-color: #e3f2fd; /* Light blue area */
}
```

**Useful `justify-content` values:**

| Value | Effect |
|---|---|
| `flex-start` | Pack items at the start |
| `center` | Pack items in the middle |
| `flex-end` | Pack items at the end |
| `space-between` | First at start, last at end, equal gaps between |
| `space-around` | Equal space around each item |

**Useful `align-items` values:** `stretch` (default), `flex-start`, `center`, `flex-end`.

![Justify-content spreads items along the shelf (main axis); align-items centres them on the shelf height (cross axis)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session16/session16-02-flex-justify-align-shelf.png?v=20260727)

**Common doubt:** "Why does `align-items: center` do nothing?" The container often needs a **height** larger than its children — otherwise there is no cross-axis space to centre into.

### Practice Activity: Flex Navbar

1. Create `flex-nav.html` with a `<nav class="toolbar">` containing a logo text and three links.
2. Style the nav with `display: flex`, `justify-content: space-between`, and `align-items: center`.
3. Resize the browser window slowly — notice how the bar stretches and items stay aligned without rewriting CSS.

---

## Flex Items — Grow, Shrink, and Basis

- **Official Definition:** **`flex-grow`**, **`flex-shrink`**, and **`flex-basis`** control how a flex item takes free space. The shorthand is **`flex`**.
- **In Simple Words:** Grow means "take extra space." Shrink means "give space back when tight." Basis is the starting size before growing or shrinking.
- **Real-Life Example:** Three siblings sharing leftover sweets — grow is who takes more extras; shrink is who reduces their share when sweets are few.

```css
.card-row { /* Row of equal cards */
  display: flex; /* Flex container */
  gap: 16px; /* Space between cards */
  flex-wrap: wrap; /* Wrap on narrow screens */
}

.card { /* Each card as a flex item */
  flex: 1 1 220px; /* Grow, shrink, start near 220px wide */
  padding: 16px; /* Inner spacing */
  background-color: #ffffff; /* White card */
  border: 1px solid #dde4ec; /* Light border */
  border-radius: 8px; /* Rounded corners */
}
```

**How `flex: 1 1 220px` works:**

- Items try to be about **220px** wide
- They **grow** equally to fill leftover space
- They **shrink** and **wrap** when the window gets narrow
- Resizing the browser shows the layout adjusting — no special breakpoint rules required

**Common mistakes:** forgetting `flex-wrap` when cards overflow; setting fixed `width` that fights `flex`.

---

## Introduction to CSS Grid

- **Official Definition:** **CSS Grid** is a two-dimensional layout system. A **grid container** defines **rows** and **columns**; children become **grid items** placed in cells.
- **In Simple Words:** Grid is a spreadsheet — rows and columns form cells where content sits.
- **Real-Life Example:** A cinema hall seating plan — row letters and seat numbers create a two-dimensional map.

**When to use Grid:** full page structure (header / sidebar / main / footer), image galleries, dashboards, or any layout that needs **both rows and columns**.

![CSS Grid is like a cinema seating chart — rows and columns form cells where each item sits in two dimensions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session16/session16-03-css-grid-cinema-seats.png?v=20260727)

**Flexbox vs Grid (quick guide):**

| Need | Prefer |
|---|---|
| One row of nav links | Flexbox |
| Cards in a wrapping row | Flexbox |
| Whole page zones (header, main, footer) | Grid |
| Photo gallery with neat columns | Grid |

**Connecting idea:** Flexbox masters one line of alignment. Grid masters the **floor plan** of the whole page.

---

## Grid Template — Rows, Columns, and Gaps

- **Official Definition:** **`grid-template-columns`** and **`grid-template-rows`** define track sizes. **`gap`** (or `row-gap` / `column-gap`) sets space between tracks.
- **In Simple Words:** Template columns decide how many vertical lanes you have and how wide each is. Gap is the aisle between lanes.
- **Real-Life Example:** Dividing a notebook page into three equal columns with ruled lines between them.

```css
.gallery { /* Photo gallery grid */
  display: grid; /* Turn into a grid container */
  grid-template-columns: repeat(3, 1fr); /* Three equal columns */
  gap: 16px; /* Space between cells */
}

.page { /* Full page shell */
  display: grid; /* Grid container */
  grid-template-rows: auto 1fr auto; /* Header, flexible main, footer */
  min-height: 100vh; /* At least full viewport height */
  gap: 0; /* No gap between major regions */
}
```

**Units to know:**

| Unit / Function | Meaning |
|---|---|
| `1fr` | One fraction of free space |
| `auto` | Size based on content |
| `repeat(3, 1fr)` | Three equal columns |
| `minmax(200px, 1fr)` | At least 200px, grow up to 1fr |

**Fluid columns tip:** `grid-template-columns: repeat(auto-fit, minmax(220px, 1fr))` creates as many columns as fit. Widen or narrow the browser — columns reflow automatically.

```css
.cards-grid { /* Responsive card grid without breakpoints */
  display: grid; /* Grid container */
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* Fit as many 220px+ columns as possible */
  gap: 16px; /* Space between cards */
}
```

**Common mistakes:** forgetting `display: grid` on the parent; putting `grid-template-columns` on a child item.

### Practice Activity: Auto-Fit Gallery

1. Create `grid-gallery.html` with six `<div class="item">` boxes inside `<div class="cards-grid">`.
2. Apply the `auto-fit` + `minmax` rule above; give each item a background and padding.
3. Drag the browser edge from wide to narrow — count how columns drop from 3 → 2 → 1 as space shrinks.

---

## Grid Placement — Spanning Cells

- **Official Definition:** Grid items can span multiple tracks using **`grid-column`** and **`grid-row`**, or sit in named areas with **`grid-template-areas`**.
- **In Simple Words:** Placement is assigning each piece of furniture to specific floor tiles — a sofa may cover two tiles.
- **Real-Life Example:** A newspaper front page — the lead story spans two columns; side stories take one column each.

```css
.layout { /* Named areas for page structure */
  display: grid; /* Grid container */
  grid-template-columns: 1fr 1fr 1fr; /* Three columns */
  grid-template-rows: auto 1fr auto; /* Header, body, footer */
  grid-template-areas: /* Map regions to cells */
    "header header header"
    "main main aside"
    "footer footer footer";
  gap: 16px; /* Space between areas */
  min-height: 100vh; /* Fill the viewport height */
  padding: 16px; /* Page edge padding */
}

.layout header { grid-area: header; } /* Place header */
.layout main { grid-area: main; } /* Place main */
.layout aside { grid-area: aside; } /* Place sidebar */
.layout footer { grid-area: footer; } /* Place footer */
```

**How the code works:**

- The quoted strings define a map — each word is a named region
- Matching `grid-area` names place HTML elements into those regions
- `1fr` rows/columns grow and shrink as the window resizes
- Header and footer stretch across all three columns automatically

---

## Building Header, Main, and Footer Layouts

Semantic HTML regions become clear when layout tools place them. Start with a page shell, then nest Flexbox inside Grid cells for local alignment.

**Full practice page — `layout-practice.html`:**

```html
<!DOCTYPE html> <!-- HTML5 document -->
<html lang="en"> <!-- Page language -->
<head> <!-- Metadata -->
  <meta charset="UTF-8"> <!-- Character encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Viewport hint -->
  <title>Flex and Grid Layout Practice</title> <!-- Tab title -->
  <link rel="stylesheet" href="layout.css"> <!-- External stylesheet -->
</head>
<body class="page"> <!-- Full page grid shell -->
  <header class="site-header"> <!-- Top bar -->
    <div class="brand">Learner Portfolio</div> <!-- Logo text -->
    <nav class="site-nav"> <!-- Navigation links -->
      <a href="#about">About</a> <!-- About link -->
      <a href="#projects">Projects</a> <!-- Projects link -->
      <a href="#contact">Contact</a> <!-- Contact link -->
    </nav>
  </header>
  <main class="site-main"> <!-- Primary content -->
    <section id="about" class="hero"> <!-- Intro section -->
      <h1>Hello, I build web layouts</h1> <!-- Page title -->
      <p>This page uses Grid for structure and Flexbox for the header and cards.</p> <!-- Support text -->
    </section>
    <section id="projects" class="cards-grid"> <!-- Project cards -->
      <article class="card"><h2>Project One</h2><p>HTML structure practice.</p></article> <!-- Card 1 -->
      <article class="card"><h2>Project Two</h2><p>CSS styling practice.</p></article> <!-- Card 2 -->
      <article class="card"><h2>Project Three</h2><p>Layout with Flex and Grid.</p></article> <!-- Card 3 -->
    </section>
    <section id="contact" class="contact"> <!-- Contact block -->
      <h2>Contact</h2> <!-- Section title -->
      <p>Email: learner@example.com</p> <!-- Contact line -->
    </section>
  </main>
  <footer class="site-footer"> <!-- Page footer -->
    <p>&copy; 2026 Learner Portfolio</p> <!-- Copyright -->
  </footer>
</body>
</html>
```

**Full stylesheet — `layout.css`:**

```css
* { /* All elements */
  box-sizing: border-box; /* Predictable widths */
}

body { /* Page defaults */
  margin: 0; /* Remove default margin */
  font-family: "Segoe UI", Tahoma, sans-serif; /* Readable font */
  color: #222222; /* Dark text */
  background-color: #f0f4f8; /* Soft page background */
}

.page { /* Outer page shell */
  display: grid; /* Two-dimensional page layout */
  grid-template-rows: auto 1fr auto; /* Header, main, footer */
  min-height: 100vh; /* Fill the screen height */
}

.site-header { /* Header uses Flexbox */
  display: flex; /* One-dimensional header row */
  justify-content: space-between; /* Brand left, links right */
  align-items: center; /* Vertical centre */
  padding: 16px 24px; /* Header padding */
  background-color: #0d47a1; /* Blue header */
  color: #ffffff; /* White text */
}

.site-nav { /* Nav link group */
  display: flex; /* Links in a row */
  gap: 16px; /* Space between links */
  flex-wrap: wrap; /* Links wrap if window is narrow */
}

.site-nav a { /* Each nav link */
  color: #ffffff; /* White links */
  text-decoration: none; /* No underline */
  font-weight: 600; /* Slightly bold */
}

.site-main { /* Main content column */
  max-width: 960px; /* Readable max width */
  width: 100%; /* Shrink on smaller windows */
  margin: 24px auto; /* Centre the column */
  padding: 0 16px; /* Side padding */
  display: flex; /* Stack sections vertically */
  flex-direction: column; /* Top to bottom */
  gap: 24px; /* Space between sections */
}

.hero, .contact, .card { /* Shared card look */
  background-color: #ffffff; /* White surface */
  padding: 20px; /* Inner spacing */
  border-radius: 8px; /* Rounded corners */
  border: 1px solid #dde4ec; /* Light border */
}

.cards-grid { /* Project cards as grid */
  display: grid; /* Grid container */
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* Fluid columns */
  gap: 16px; /* Space between cards */
}

.site-footer { /* Footer bar */
  text-align: center; /* Centre footer text */
  padding: 16px; /* Footer padding */
  background-color: #1565c0; /* Blue footer */
  color: #ffffff; /* White text */
}
```

**How the code works:**

- **Grid** on `.page` creates header / main / footer bands that fill the viewport
- **Flexbox** on `.site-header` and `.site-nav` aligns brand and links in one row
- **`auto-fit` + `minmax`** on `.cards-grid` lets cards reflow as the window width changes
- **`width: 100%`** and **`max-width`** keep main content readable on wide screens and usable on narrow ones
- Resize the browser during practice — watch cards and nav wrap without changing the CSS file

**Common mistakes:** applying Grid and Flexbox to the same element when nesting is clearer; forgetting `min-height: 100vh` so the footer floats mid-page on short content.

---

## Combining Flexbox and Grid — Decision Guide

Use both tools on one page by nesting them:

| Region | Tool | Why |
|---|---|---|
| Full page shell | Grid | Clear header / main / footer rows |
| Header bar | Flexbox | Brand and links on one axis |
| Card collection | Grid (`auto-fit`) | Neat columns that reflow |
| Button group inside a card | Flexbox | Horizontal controls |

**Logic to remember:** Grid for the **map**; Flexbox for the **row**. Nest Flexbox inside a Grid cell (or Grid inside a Flex item) when one tool is not enough.

![A complete page shell — Grid places Header, Main, and Footer; Flexbox aligns brand and links in the header; cards sit in a fluid grid that can reflow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module2/session16/session16-04-page-layout-header-main-footer.png?v=20260727)

### Practice Activity: Build the Full Layout Page

1. Save `layout-practice.html` and `layout.css` in your `web-practice` folder.
2. Open the HTML file in Chrome and confirm header, cards, and footer appear correctly.
3. Slowly resize the window from wide laptop width to a narrow phone-like width.
4. Observe: header links wrap; cards drop from three columns to two to one; footer stays at the bottom of the page shell.
5. Change `minmax(220px, 1fr)` to `minmax(280px, 1fr)` and refresh — fewer columns appear at the same width.

### Practice Activity: Flex + Grid Mini Challenge

1. Create `dashboard.html` with a Grid page: header, a main area with two side-by-side panels, and a footer.
2. Make the header a Flex row with title left and two buttons right.
3. Inside main, use `grid-template-columns: 2fr 1fr` for a wide content panel and a narrow sidebar.
4. Resize the window and note how `fr` units share space proportionally.

---

## Debugging Layout Issues

| Problem | Likely cause | Fix |
|---|---|---|
| Items still stacked | Missing `display: flex` / `grid` | Add it on the **parent** |
| Align centre does nothing | Parent has no height | Set `min-height` on the container |
| Cards overflow sideways | No wrap / no auto-fit | Add `flex-wrap: wrap` or `auto-fit` |
| Footer not at bottom | No full-height page shell | Use Grid rows `auto 1fr auto` + `min-height: 100vh` |
| Uneven card widths | Fixed widths fighting flex/grid | Prefer `flex` or `fr` / `minmax` |

**DevTools habit:** Inspect a container → look for **Flex** or **Grid** badges in Chrome. Click them to visualise tracks, gaps, and item boundaries while you resize the window.

### Quick Self-Check Before You Move On

- Can you turn a parent into a flex container and centre its children?
- Can you explain when to choose Flexbox vs Grid in one sentence each?
- Can you write `repeat(auto-fit, minmax(220px, 1fr))` and explain what happens when the window shrinks?
- Did you build a page with Grid for structure and Flexbox for the header?

If any answer is "not yet," repeat one practice activity before moving on.

---

## How This Fits Your Journey Ahead

You can now control **structure** (HTML), **appearance** (CSS properties), and **arrangement** (Flexbox and Grid). Together these skills let you design pages that stay organised as the browser window changes size.

In upcoming lessons you will add **JavaScript** for interactivity — clicks, form behaviour, and dynamic updates. Clean layout habits make interactive UIs easier to understand and maintain.

---

## Key Takeaways

- **Flexbox** is one-dimensional — ideal for nav bars, toolbars, and wrapping card rows.
- **`justify-content`** and **`align-items`** control spacing and alignment on the main and cross axes.
- **CSS Grid** is two-dimensional — ideal for page shells and multi-column structures.
- **`auto-fit` with `minmax`** and Flex **`wrap`** let layouts reflow as the screen width changes.
- Combine **Grid for page structure** and **Flexbox for local rows** to build complete header / main / footer pages.

These layout skills are the foundation of every dashboard, portfolio, and agent interface you will style next.

---

## Important Commands, Libraries, Terminologies Used

| Term / Property | Meaning in Simple Words |
|---|---|
| **Flexbox** | One-dimensional flexible layout model |
| **`display: flex`** | Makes an element a flex container |
| **Flex item** | Direct child of a flex container |
| **`flex-direction`** | Row or column main axis |
| **`flex-wrap`** | Allow items to wrap to next line |
| **`justify-content`** | Distribute space on the main axis |
| **`align-items`** | Align items on the cross axis |
| **`flex` / grow / shrink / basis** | How items share free space |
| **CSS Grid** | Two-dimensional row-and-column layout |
| **`display: grid`** | Makes an element a grid container |
| **`grid-template-columns` / `rows`** | Define column and row tracks |
| **`gap`** | Space between flex or grid items |
| **`1fr` / `minmax` / `auto-fit`** | Flexible track sizing that reflows |
| **`grid-template-areas` / `grid-area`** | Named placement of page regions |
| **`min-height: 100vh`** | At least full viewport height |
| **DevTools Flex / Grid overlay** | Visualise layout tracks while inspecting |
