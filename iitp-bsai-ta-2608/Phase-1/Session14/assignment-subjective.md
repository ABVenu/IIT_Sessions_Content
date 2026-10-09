# Subjective Assignment: Mess Token Card

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation (React + Tailwind)

---

## Scenario

The hostel mess already has a working name slip. Typing a name updates the greeting at once. The slip behaves correctly, but it still looks plain.

Your job is to keep that behaviour and dress the slip with Tailwind utilities only. Do not write a new `.css` rule for this card. Do not replace `useState`.

## Task

Create a single file named `MessTokenCard.jsx`.

Build one component named `MessTokenCard` that holds this state:

| State | Starts as | What it stores |
| --- | --- | --- |
| `name` | `""` | Text in the name box |

The screen must include:

1. An outer card whose `className` is exactly `max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow`.
2. A heading whose text is `Mess token` and whose `className` is exactly `text-2xl font-bold text-slate-800`.
3. A name input whose displayed text is `name`. Typing in it updates `name`. Its `className` is exactly `mt-4 w-full p-3 border rounded-lg`. Its placeholder is `Enter your name`.
4. A greeting line that uses a ternary:
   - If `name` is `""`, show `Please enter your name`.
   - Otherwise show `Hello, ` followed by the stored name.
   - The greeting paragraph `className` is exactly `mt-4 text-slate-600`.
5. Under the greeting, a row with two short labels whose visible text is `Counter` and `Token`. That row’s `className` is exactly `flex flex-col justify-between gap-4 mt-4 md:flex-row`.

Do not add extra buttons. Do not add a second name. The React logic stays in this one component. Styling must use the class lists above, not a separate stylesheet for the card.

## Sample walkthrough

Check the screen in this order. The input shows the stored text after each step. Resize the browser when a check mentions width.

### Check A — page just opened

| On screen | Expected |
| --- | --- |
| Name box | empty |
| Heading | `Mess token` |
| Greeting line | `Please enter your name` |
| Row labels | `Counter` and `Token` |
| Card look | centred white card, 24px inner padding, 8px corners, drop shadow |

### Check B — type a name

Type `Kabir` into the name box.

| On screen | Expected |
| --- | --- |
| Name box | `Kabir` |
| Greeting line | `Hello, Kabir` |
| Row labels | still `Counter` and `Token` |

### Check C — clear the name

Delete the text so the box is empty again.

| On screen | Expected |
| --- | --- |
| Name box | empty |
| Greeting line | `Please enter your name` |

### Check D — narrow window

Set the window width below 768 pixels, for example 500 pixels.

| On screen | Expected |
| --- | --- |
| `Counter` and `Token` | stacked in a column (`flex-col`) |

### Check E — wider window

Widen the window past 768 pixels.

| On screen | Expected |
| --- | --- |
| `Counter` and `Token` | sit in one row (`md:flex-row`) |

If the greeting stops updating, put `value` and `onChange` back and leave the look in `className`.

## Submission instructions

- Code all the points above in VS Code in a single `MessTokenCard.jsx` file.
- Render `MessTokenCard` in your Vite React app (Tailwind already set up), run it, and verify Checks A to E.
- Submit the code in the code editor / answer box on the LMS.

---

## Answer Explanation

### Walkthrough

This card is the same kind of name screen as a controlled input, with Tailwind classes on the JSX.

- `name` starts as `""`. The input’s `value` is that state, and `onChange` stores `event.target.value`. Typing still re-renders the component. The utilities on the input (`mt-4 w-full p-3 border rounded-lg`) only space, stretch, pad, and outline the box.
- The greeting ternary is unchanged by Tailwind. An empty name shows `Please enter your name`. A typed name shows `Hello, ` plus that name. `mt-4 text-slate-600` only spaces and colours that line.
- The outer card uses `max-w-md` so it does not stretch across a wide monitor, `mx-auto` to centre it, `mt-10` to drop it from the top, `p-6` for 24 pixels of inner space, then `bg-white`, `rounded-lg` (8 pixel corners), and `shadow`.
- The heading uses size and weight as two classes: `text-2xl` and `font-bold`, plus `text-slate-800` for a dark colour.
- The label row is mobile first. `flex flex-col` stacks `Counter` and `Token` on a phone. `md:flex-row` places them side by side from 768 pixels upward. `justify-between` and `gap-4` stay on at every width.

No new CSS file is needed for these looks. If a class shows no effect in the host app, the usual setup check is the Vite plugin plus `@import "tailwindcss"` in `index.css`.

### Complete code

```jsx
import { useState } from "react";

function MessTokenCard() {
  const [name, setName] = useState("");

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow">
      <h1 className="text-2xl font-bold text-slate-800">Mess token</h1>
      <input
        className="mt-4 w-full p-3 border rounded-lg"
        value={name}
        onChange={(event) => setName(event.target.value)}
        placeholder="Enter your name"
      />
      <p className="mt-4 text-slate-600">
        {name ? `Hello, ${name}` : "Please enter your name"}
      </p>
      <div className="flex flex-col justify-between gap-4 mt-4 md:flex-row">
        <p>Counter</p>
        <p>Token</p>
      </div>
    </div>
  );
}

export default MessTokenCard;
```

To verify, render `<MessTokenCard />` from the app entry you already use, then follow Checks A to E.

### Alternative approaches

- The empty-name check can be `name === "" ? "Please enter your name" : \`Hello, ${name}\``. That matches the same two strings.
- The `onChange` handler can live in a named function such as `handleNameChange`. The setter and the `className` lists stay the same.
- `items-center` can be added on the label row if you also want vertical centring in the row. It is extra. It does not replace `flex`, `flex-col`, or `md:flex-row`.
