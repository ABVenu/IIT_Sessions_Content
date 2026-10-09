# Tailwind CSS with React

## What You Will Learn

In the previous session you built an interactive React screen. **useState** stored the values, controlled inputs showed those values in the boxes, and a state update re-rendered the component. Conditional rendering with `&&` and the ternary operator decided which lines appeared.

That screen already behaved correctly. A working screen can still look plain, because behaviour and appearance are two different jobs. React keeps the behaviour, and **Tailwind CSS** takes the appearance: spacing, colour, type, and layout, written as short class names on the JSX.

Today you will:

- Set up Tailwind in a Vite React project
- Style components with core utility classes
- Build a simple layout with flex utilities
- Apply the responsive prefixes `sm` and `md`
- Restyle an existing React component using Tailwind only

The React logic stays. Only the `className` values change.

## Why Utilities Sit on the JSX

A normal stylesheet keeps rules in a separate `.css` file, then connects them with a class name. That still works. Tailwind writes the same CSS ideas in a shorter form, directly on the element.

**Official definition:** A **utility-first CSS framework** is a set of small, single-purpose classes that you compose on an element instead of writing custom CSS rules.

**In simple words:** Each class does one job. You stack a few of them to get the look you want.

**Real-life example:** A thali already has named portions, so you take rice, dal, and sabzi by name. Tailwind classes are those named portions of CSS. You pick a ready class each time, the way you pick a named portion.

A separate `.css` file is still a valid way to style a page. Tailwind is the shorter path when the style belongs to one element and you want to read it beside the JSX.

![Separate CSS in a stylesheet versus Tailwind utilities stacked on className — both produce the same white rounded card](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/phase-1/session14/session14-01-css-vs-tailwind-utilities.png?v=20261003)

## The Card, Written Both Ways

Here is the same card the session compared. The CSS version names one class and describes three properties. The Tailwind version puts those three jobs straight on the element.

```css
.card { /* Class name that groups the three card styles */
  padding: 16px; /* Space inside the card, on every side */
  background-color: white; /* Paint the card white */
  border-radius: 8px; /* Round the corners by 8 pixels */
} /* End of the card rule */
```

**How the code works:**

- `.card` is one class name that hides three CSS properties inside a stylesheet.
- `padding: 16px` is the inner space around the content.
- `background-color: white` fills the box.
- `border-radius: 8px` softens the corners.

The same card in React uses `className`, with a capital **N**. JSX uses `className` because `class` is already a reserved word in JavaScript.

```jsx
function Card() { // A function component that returns one styled box
  return ( // Return the card to the screen
    <div className="p-4 bg-white rounded-lg"> {/* Padding, white fill, rounded corners */}
      Notes {/* Visible text inside the card */}
    </div> // Close the card
  ); // End of the return
} // End of Card

export default Card; // Let other files use this component
```

**How the code works:**

- `p-4` is padding on all sides. On Tailwind’s scale, **4 means 1rem, which is 16 pixels**.
- `bg-white` sets the background colour to white.
- `rounded-lg` sets the border radius to 8 pixels.
- `className` is the React attribute. Writing `class` here is a frequent slip, and the style will not attach the way you expect.

A frequent slip is reading `4` as 4 pixels. The number is a step on a scale, not a raw pixel count. The scale is explained with padding and margin below.

## Set Up Tailwind in a Vite React Project

You already have a Vite React app. Tailwind has to be installed, connected in the Vite config, and loaded from the CSS file. Skip any one of those and classes such as `bg-white` or `bg-green-500` will sit in the JSX and change nothing on the screen.

**Vite** is the tool that runs the React project in development. **Tailwind CSS** is the styling package. The **Vite plugin** `@tailwindcss/vite` is the bridge between them.

**In simple words:** Install the styling kit, tell Vite to use it, then import that kit from `index.css`.

**Real-life example:** Buying a new bulb is not enough. You also fit it in the holder and switch on the line. Install, plugin, and CSS import are those three steps.

![Tailwind in Vite React: npm install, register the plugin in vite.config.js, import tailwindcss in index.css, then the browser shows styled utilities](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/phase-1/session14/session14-02-vite-tailwind-setup-flow.png?v=20261003)

In the project folder, install both packages:

```bash
npm install tailwindcss @tailwindcss/vite # Install Tailwind and the Vite plugin
```

**How the code works:**

- `npm install` downloads packages into this project.
- `tailwindcss` is the framework that owns the utility classes.
- `@tailwindcss/vite` is the plugin Vite loads so those classes are available while the app runs.

Open `vite.config.js` and add the plugin next to the React plugin. This is the full file after the change.

```js
import { defineConfig } from 'vite'; // Helper that builds Vite's settings object
import react from '@vitejs/plugin-react'; // Lets Vite compile React JSX
import tailwindcss from '@tailwindcss/vite'; // Connects Tailwind to this Vite app

export default defineConfig({ // Settings Vite reads when the dev server starts
  plugins: [ // List of plugins Vite should run
    react(), // Keep React support switched on
    tailwindcss(), // Switch Tailwind on beside React
  ], // End of the plugin list
}); // End of the Vite config
```

**How the code works:**

- The React import stays in the file. Tailwind is added beside it.
- `tailwindcss()` sits inside `plugins`, so Vite runs both tools.
- Nothing else in this file needs a change for today’s setup.

Next, clear the old rules in `src/index.css` and load Tailwind. This is the full file.

```css
@import "tailwindcss"; /* Load every Tailwind utility into the app */
```

**How the code works:**

- `@import "tailwindcss"` replaces the old plain CSS in this file.
- After this line, names such as `p-4` and `bg-white` have a meaning.
- If this import is missing, a green or blue utility draws no colour at all.

`src/main.jsx` already contains `import './index.css'`, and that line brings `index.css`, and therefore Tailwind, onto the page. Leave that import as it is. `<App />` in that file is still the component from the previous work.

Start the app with `npm run dev` and open the local address Vite prints. This setup lives in `vite.config.js` and `index.css`.

## A First Styled Heading

With the setup saved, utilities work on any JSX element. This component matches the first demo: a large bold blue heading, then a softer paragraph with space above it.

```jsx
function App() { // The screen shown at the root of the app
  return ( // Return the heading and the paragraph
    <div> {/* Wrapper around the two lines */}
      <h1 className="text-3xl font-bold text-blue-600">Hello</h1> {/* Large, bold, blue heading */}
      <p className="mt-4 text-slate-600">This line sits under the heading.</p> {/* Space above, softer colour */}
    </div> // Close the wrapper
  ); // End of the return
} // End of App

export default App; // Vite renders this component from main.jsx
```

**How the code works:**

- `text-3xl` sets a large font size.
- `font-bold` sets a heavy font weight.
- `text-blue-600` sets the text colour to a strong blue.
- `mt-4` adds margin only on the top, so the paragraph moves down by 16 pixels.
- `text-slate-600` is a quieter grey-blue for body text.

Save the file. The dev server updates the page. If the heading stays black and small, check the plugin in `vite.config.js` and the import in `index.css` before changing the JSX again.

## Spacing with Padding

**Padding** is the space inside a box, between the border and the content.

**In simple words:** It keeps the words from touching the edge of the card.

**Real-life example:** The blank space inside a notebook page, before the writing starts, is padding. The gap between two notebooks on a desk is margin, which comes next.

![Padding sits inside the box with p-4; margin sits outside with mt-4 — inner cushion versus outer gap around the content](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/phase-1/session14/session14-03-padding-margin-box-model.png?v=20261003)

Tailwind writes padding as `p`, then an optional side letter, then a number. The session used step **4** as the normal unit.

| Class | Where the space goes | Size at step 4 |
| --- | --- | --- |
| `p-4` | All four sides, equally | 16px |
| `pt-4` | Top only | 16px |
| `pb-4` | Bottom only | 16px |
| `pl-4` | Left only | 16px |
| `pr-4` | Right only | 16px |
| `px-4` | Left and right together | 16px |
| `py-4` | Top and bottom together | 16px |

The letters are fixed: **t** top, **b** bottom, **l** left, **r** right, **x** horizontal, **y** vertical. No letter means every side.

The number is the same scale everywhere:

| Step | Size | Plain meaning |
| --- | --- | --- |
| `1` | 4px (0.25rem) | A small step |
| `4` | 16px (1rem) | One unit |
| `6` | 24px (1.5rem) | One and a half units |
| `8` | 32px (2rem) | Two units |

`p-6` is the same sides as `p-4`, with more room. `p-1` is the same sides, with less room. You change the step, not the meaning of `p`.

The opening card is the live `p-4` example: 16 pixels inside the box on every side, so the word never touches the rounded edge. Swap `p-4` for `pt-4` and only the top grows.

## Spacing with Margin

**Margin** is the space outside a box, between this element and its neighbours.

**In simple words:** Padding is the cushion inside. Margin is the gap outside.

**Real-life example:** Padding is the cloth inside a gift box. Margin is the space you leave between that box and the next gift on the table.

Margin uses the same letters and the same number scale. Only the first letter changes from `p` to `m`.

| Class | Where the gap goes | Size at step 4 |
| --- | --- | --- |
| `m-4` | All four sides | 16px |
| `mt-4` | Top only | 16px |
| `mb-4` | Bottom only | 16px |
| `ml-4` | Left only | 16px |
| `mr-4` | Right only | 16px |
| `mx-4` | Left and right | 16px |
| `my-4` | Top and bottom | 16px |

`x` is the horizontal axis, left and right. `y` is the vertical axis, top and bottom. When the gap belongs outside the box, the class starts with `m`.

The paragraph under the Hello heading already uses `mt-4`, which pushes that paragraph down by 16 pixels and leaves the inside of the text alone. `mb-4` pushes whatever comes after the element. `mx-auto`, on the name card later, centres a box that has a maximum width.

There are many more steps, such as `m-0`, `m-2`, and `m-10`, and the pattern stays the same. A class reference, sometimes called a cheat sheet, lists them. Remember `p` or `m`, the side letter, and the scale, then look up a rare step when you need it.

## Colour Utilities

**Official definition:** A **colour utility** sets one colour role: text, background, or border.

**In simple words:** The class names the role, the colour, and how light or dark that colour is.

**Real-life example:** Paint shops sell the same blue in light, medium, and deep tins. `blue-100` is a light tin, and `blue-600` is a deeper tin. The colour family stays blue.

These two classes were used together:

- `text-blue-600` colours the letters.
- `bg-blue-600` colours the background behind them.

The shade number runs from light to dark: **100** is a light wash such as `bg-blue-100` or `bg-gray-100`, and **600** is strong enough for text and buttons. Higher numbers such as **800** and **900** are darker. Families you can swap in the same pattern include `slate`, `gray`, `blue`, and `indigo`.

`border-blue-600` colours a border the same way, once the element also has `border`. White text on a strong background is `text-white`.

The Hello heading already uses `text-blue-600` for the letters, and the Save button uses `bg-blue-600` with `text-white` for a filled control. Changing `600` to `100` makes the same blue much lighter, while the role of `bg` or `text` stays the same. These classes stand on their own, so a separate `style` attribute is not required.

## Typography

**Typography** is the styling of text: size and weight.

**In simple words:** How large the letters are, and how heavy they look.

**Real-life example:** A newspaper uses a large heavy line for the headline and a smaller line for the story. `text-3xl` with `font-bold` is the headline. A smaller step is the story.

| Class | Role |
| --- | --- |
| `text-sm` | Small text |
| `text-base` | The normal body size |
| `text-lg` | Large |
| `text-xl` | Extra large |
| `text-2xl` | Two steps above extra large |
| `text-3xl` | A page heading size |
| `font-bold` | Heavy font weight |

Size and weight are separate classes. You can change one and leave the other.

The heading **My Portfolio** used `text-3xl font-bold` on an `h1`, where `text-3xl` only changes size and `font-bold` only changes weight. The Hello heading adds `text-blue-600` on top of that same pair. `text-lg` or `text-xl` is the same idea with a smaller step.

## Borders and Rounded Corners

**Border** draws the line around a box. **Border radius** curves the corners. Tailwind’s `rounded-lg` is the 8 pixel radius from the card example.

| Class | What you see |
| --- | --- |
| `border` | A default border on all sides |
| `rounded-lg` | Corners rounded by 8 pixels |
| `rounded-md` | A smaller curve |
| `rounded-full` | A full pill shape on a button, or a circle on a square |

`border` draws the line, and `rounded-lg` curves it with the same 8 pixel radius as the opening card. The name input later in these notes uses `border` and `rounded-lg` together. `rounded-full` on a wide button makes the ends fully round.

A button stacks the utilities you already have: margin, padding, colour, and radius.

```jsx
function SaveButton() { // A button styled only with utilities
  return ( // Return the button
    <button className="mt-4 bg-blue-600 px-4 py-2 text-white rounded-lg"> {/* Margin, blue fill, white text, curve */}
      Save {/* Label on the button */}
    </button> // Close the button
  ); // End of the return
} // End of SaveButton

export default SaveButton; // Export the button
```

**How the code works:**

- `mt-4` separates the button from the element above it.
- `bg-blue-600` and `text-white` set the colours.
- `px-4` pads the left and right. `py-2` pads the top and bottom with a smaller step.
- `rounded-lg` curves the button. `rounded-full` would make it a pill.

## Flex Utilities for a Simple Layout

**Official definition:** **Flexbox** is a CSS layout mode that lines up children in a row or a column and distributes space between them.

**In simple words:** `flex` turns a box into a line of items. Other utilities say how those items align and how far apart they sit.

**Real-life example:** People standing in a queue form the row. Even gaps between people are `gap`. Pushing the first person to one end and the last person to the other end is `justify-between`.

In plain CSS you would write `display: flex`, then more properties. Tailwind uses the short names on the same element.

| Class | Job in a row |
| --- | --- |
| `flex` | Turn the layout on. The default direction is a horizontal row |
| `items-center` | Align items on the cross axis, which is vertical in a row |
| `justify-between` | Push the first item to one end and the last item to the other |
| `gap-4` | Put 16 pixels between the children |
| `p-4` | Pad the whole row |

![A flex row with items-center and justify-between pushes Notes to one end and Profile to the other, with gap-4 between children](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/phase-1/session14/session14-04-flex-justify-between-row.png?v=20261003)

```jsx
function TopBar() { // A horizontal bar with the two ends pushed apart
  return ( // Return the bar
    <div className="flex items-center justify-between gap-4 p-4"> {/* Row, centred, ends apart, gap, padding */}
      <p>Notes</p> {/* First item, sits at the start */}
      <p>Profile</p> {/* Last item, sits at the end */}
    </div> // Close the bar
  ); // End of the return
} // End of TopBar

export default TopBar; // Export the bar
```

**How the code works:**

- `flex` is the short form of `display: flex`, so the layout turns on from that one class.
- `items-center` lines the text up in the middle of the row’s height.
- `justify-between` is the utility that sends the two labels to opposite ends. A footer with a copyright note at one end and icons at the other uses the same class.
- `gap-4` is the space between children, not the padding around the whole bar.
- `p-4` is the padding inside the bar, around the whole row.

`flex-col` changes the direction to a column, top to bottom. You will use that as the phone layout in the next section.

## Responsive Prefixes

**Official definition:** A **responsive prefix** limits a utility to a minimum screen width. Tailwind is **mobile first**: the class with no prefix is the small-screen style, and prefixed classes add changes as the screen gets wider.

**In simple words:** Style the phone first. Add `sm:` or `md:` only for the change that should appear from that width upward.

**Real-life example:** A newspaper stack on a small table sits in one pile, and on a wide table the same pages can lie side by side. The content stays the same. The width is what changes.

| Prefix | Applies from | Typical use in this session |
| --- | --- | --- |
| *(none)* | Every width, including a phone | `flex-col` so blocks stack |
| `sm:` | 640 pixels and wider | A slightly larger text size |
| `md:` | 768 pixels and wider | `flex-row` so blocks sit side by side |

Unprefixed classes always apply, and a prefixed class joins in at that breakpoint and stays on for wider screens. `md:flex-row` starts once the width reaches the `md` size. A narrow phone keeps the unprefixed column.

![Mobile first: flex-col stacks panels on a phone; from the md width upward, md:flex-row places main and side content side by side](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-bsai-ta-2608/phase-1/session14/session14-05-mobile-first-md-breakpoint.png?v=20261003)

```jsx
function ResponsivePanels() { // Stack on a phone, sit side by side from the md width
  return ( // Return the two panels
    <div className="flex flex-col gap-4 p-4 md:flex-row"> {/* Column first, row from md */}
      <div className="p-6 bg-blue-100"> {/* Main area, light blue, with inner padding */}
        <p className="text-base sm:text-lg">Main content</p> {/* Phone size, larger from sm */}
      </div> {/* Close the main area */}
      <div className="p-6 bg-slate-100"> {/* Side area, light slate */}
        <p>Side panel</p> {/* Label of the side area */}
      </div> {/* Close the side area */}
    </div> // Close the layout
  ); // End of the return
} // End of ResponsivePanels

export default ResponsivePanels; // Export the layout
```

**How the code works:**

- `flex flex-col` is the mobile layout: main content first, side panel under it.
- `gap-4` and `p-4` apply at every width.
- `md:flex-row` switches the same flex container to a row from 768 pixels upward.
- `text-base` is the phone size. `sm:text-lg` bumps that paragraph up from 640 pixels upward.
- `p-6` and `bg-blue-100` style the main panel. `bg-slate-100` keeps the side panel lighter and neutral.

Check this by dragging the browser window: a narrow window shows one column, and a wider window past the `md` width shows one row. If the row never appears, the `md:` prefix is missing or it sits on the child instead of the flex parent.

## Restyle an Existing React Component

The name screen from the earlier React work already stores a name and updates the greeting. Restyling it means adding Tailwind classes only. **useState**, `value`, and `onChange` stay as they are.

**In simple words:** The form still listens. The classes only dress it.

**Real-life example:** Repainting a scooter leaves the engine as it is. The ride is the same. The look is new.

This is the full component after the restyle from the session: a centred card, a bold welcome line, a full-width input, and a line that still depends on state.

```jsx
import { useState } from 'react'; // The state hook from the previous screen

function App() { // Name screen, restyled with utilities only
  const [name, setName] = useState(''); // Store the text box value, starting empty

  return ( // Return the card
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow"> {/* Centred card */}
      <h1 className="text-2xl font-bold text-slate-800">Welcome</h1> {/* Large dark heading */}
      <input className="mt-4 w-full p-3 border rounded-lg" value={name} onChange={(event) => setName(event.target.value)} placeholder="Enter your name" /> {/* Controlled name box: margin, full width, padding, border, curve */}
      <p className="mt-4 text-slate-600"> {/* Spaced, softer greeting line */}
        {name ? `Hello, ${name}` : 'Please enter your name'} {/* Empty state or Hello plus the name */}
      </p> {/* Close the greeting */}
    </div> // Close the card
  ); // End of the return
} // End of App

export default App; // Same component, new class names
```

**How the code works:**

- `max-w-md` stops the card from stretching across a wide monitor.
- `mx-auto` centres that card with equal left and right margins.
- `mt-10` drops it down from the top of the page. `p-6` is the inner space, 24 pixels.
- `bg-white`, `rounded-lg`, and `shadow` give the white card, the 8 pixel corners, and a soft drop shadow.
- `text-2xl font-bold text-slate-800` styles the welcome line without touching its words.
- The input uses `mt-4 w-full p-3 border rounded-lg`. `w-full` makes it as wide as the card.
- `value` and `onChange` are unchanged, so the box is still controlled and the component still re-renders on each key.
- The ternary is unchanged. An empty name shows “Please enter your name”. A typed name shows “Hello, ” plus that name.
- `mt-4 text-slate-600` only spaces and colours that message.

If the greeting stops updating, the state was edited by mistake. Put `value` and `onChange` back, and leave the new look in `className`.

## Try This on Your Screen

Use your Vite React app after the Tailwind setup. In `App.jsx`, build one profile card and check it in the browser.

- Put your name in a heading with `text-2xl` and `font-bold`.
- Put one sentence under it with `mt-4` and `text-slate-600`.
- Wrap both in a white card: `max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow`.
- Under the sentence, add a flex row with two short labels, `Notes` and `Profile`, using `flex`, `justify-between`, and `gap-4`.
- On a narrow window those two labels can stay in a column: add `flex-col` and `md:flex-row` on that row.
- Type nothing new in a CSS file. If a class shows no effect, check `@import "tailwindcss"` and the Vite plugin first.

## Key Takeaways

- Tailwind is a utility-first CSS framework. Short classes on `className` replace long rules in a separate file for the styles you used today.
- Setup is three links: install `tailwindcss` and `@tailwindcss/vite`, register the plugin in `vite.config.js`, and `@import "tailwindcss"` in `index.css`.
- `p` and `m` share one scale. Step `4` is 16 pixels. Side letters `t`, `b`, `l`, `r`, `x`, and `y` choose the edge.
- `flex`, `items-center`, `justify-between`, and `gap-4` build a simple row. `flex-col` plus `md:flex-row` stacks that row on a phone and places it side by side from the `md` width.
- Restyling a React component changes classes only. `useState`, controlled inputs, and conditional rendering keep working as before.

In an upcoming session you will keep this split: React for what the screen does, utilities for how the screen looks, including layouts that must work on both a phone and a wider window.

## Important Commands, Libraries, and Terminologies

| Name | Meaning |
| --- | --- |
| `npm install tailwindcss @tailwindcss/vite` | Install Tailwind and the Vite plugin |
| `npm run dev` | Start the Vite dev server |
| `@tailwindcss/vite` | Plugin added in `vite.config.js` |
| `@import "tailwindcss"` | Line in `src/index.css` that loads the utilities |
| `className` | JSX attribute for classes. Capital N |
| Utility class | One class, one CSS job, composed on the element |
| `p-4` | Padding on all sides, 16px |
| `pt-4`, `pb-4`, `pl-4`, `pr-4` | Padding on one side |
| `px-4`, `py-4` | Horizontal padding, vertical padding |
| `m-4`, `mt-4`, `mb-4`, `mx-4`, `my-4` | The same map for margin |
| Spacing step `4` | 1rem, 16 pixels |
| Spacing step `6` | 1.5rem, 24 pixels |
| `bg-blue-600` | Background colour, blue shade 600 |
| `text-blue-600`, `text-slate-600`, `text-white` | Text colours |
| `bg-blue-100`, `bg-slate-100` | Light background washes |
| `text-3xl`, `text-2xl`, `text-lg`, `text-base` | Font sizes, large to normal |
| `font-bold` | Heavy font weight |
| `border` | Default outline |
| `rounded-lg` | 8 pixel corner radius |
| `rounded-full` | Pill or circle radius |
| `shadow` | Drop shadow on the card |
| `max-w-md` | Cap the card width |
| `mx-auto` | Centre a width-capped box |
| `w-full` | 100 percent of the parent width |
| `flex` | Horizontal flex row |
| `flex-col` | Flex column |
| `items-center` | Cross-axis centring |
| `justify-between` | First and last items at opposite ends |
| `gap-4` | 16 pixels between flex children |
| `sm:` | Apply from 640px upward |
| `md:` | Apply from 768px upward |
| Mobile first | Unprefixed classes are the phone style |
| `useState` | Unchanged by Tailwind. It still stores the name and re-renders |
