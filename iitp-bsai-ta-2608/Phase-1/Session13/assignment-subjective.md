# Subjective Assignment: Found Item Desk

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation (React)

---

## Scenario

The campus lost-and-found desk keeps one slip on screen for the item currently at the counter.

The slip has two text boxes and a claimed flag. Typing updates the boxes immediately. Marking the item claimed, or resetting the desk, changes only the state those buttons are responsible for. The lines under the buttons must follow that state.

## Task

Create a single file named `FoundItemDesk.jsx`.

Build one component named `FoundItemDesk` that holds this state:

| State | Starts as | What it stores |
| --- | --- | --- |
| `itemName` | `""` | Text in the item name box |
| `location` | `""` | Text in the location box |
| `isClaimed` | `false` | Whether the item has been marked claimed |

The screen must include:

1. A heading whose text is `Found item desk`.
2. An item-name input whose displayed text is `itemName`. Typing in it updates `itemName`.
3. A location input whose displayed text is `location`. Typing in it updates `location`.
4. A button labelled `Mark claimed`. Clicking it sets `isClaimed` to `true`. It does not change `itemName` or `location`.
5. A button labelled `Reset desk`. Clicking it sets `itemName` to `""`, `location` to `""`, and `isClaimed` to `false`.

Under the buttons, render these lines from state:

- If `isClaimed` is `true`, show `Status: Claimed`. Otherwise show `Status: Still at the desk`. Use a ternary.
- If `itemName` is `""`, show `No item name yet`. Otherwise show `Item: ` followed by the stored name. Use a ternary.
- If `location` is not `""`, show `Found at: ` followed by the stored location. If `location` is `""`, that line must be absent. Use `&&`.

Do not add a list of past items. This screen stores one slip at a time. Styling is optional. The visible text and the behaviour below are required.

## Sample walkthrough

Check the screen in this order. The inputs show the stored text after each step.

### Check A — page just opened

| On screen | Expected |
| --- | --- |
| Item name box | empty |
| Location box | empty |
| Status line | `Status: Still at the desk` |
| Item line | `No item name yet` |
| Location line | not shown |

### Check B — type a name only

Type `Blue bottle` into the item name box. Leave the location box empty. Do not click a button.

| On screen | Expected |
| --- | --- |
| Item name box | `Blue bottle` |
| Location box | empty |
| Status line | `Status: Still at the desk` |
| Item line | `Item: Blue bottle` |
| Location line | not shown |

### Check C — type a location

The item name is still `Blue bottle`. Type `Library steps` into the location box.

| On screen | Expected |
| --- | --- |
| Item name box | `Blue bottle` |
| Location box | `Library steps` |
| Status line | `Status: Still at the desk` |
| Item line | `Item: Blue bottle` |
| Location line | `Found at: Library steps` |

### Check D — mark claimed

Click **Mark claimed** once.

| On screen | Expected |
| --- | --- |
| Item name box | `Blue bottle` |
| Location box | `Library steps` |
| Status line | `Status: Claimed` |
| Item line | `Item: Blue bottle` |
| Location line | `Found at: Library steps` |

### Check E — reset

Click **Reset desk** once.

| On screen | Expected |
| --- | --- |
| Item name box | empty |
| Location box | empty |
| Status line | `Status: Still at the desk` |
| Item line | `No item name yet` |
| Location line | not shown |

### Check F — claim an empty slip

From the reset screen, click **Mark claimed** without typing.

| On screen | Expected |
| --- | --- |
| Item name box | empty |
| Location box | empty |
| Status line | `Status: Claimed` |
| Item line | `No item name yet` |
| Location line | not shown |

## Submission instructions

- Code all the points above in VS Code in a single `FoundItemDesk.jsx` file.
- Render `FoundItemDesk` in your Vite React app, run it, and verify Checks A to F.
- Submit the code in the code editor / answer box on the LMS.

---

## Answer Explanation

### Walkthrough

Use three `useState` values so each part of the slip can change on its own.

- `itemName` and `location` start as empty strings. Each input’s `value` is that state, and its `onChange` stores `event.target.value`. That is a controlled input: the box shows state, and typing updates state, which renders the component again.
- `isClaimed` starts as `false`. **Mark claimed** calls `setIsClaimed(true)` only. The name and location stay whatever they already were, which is why Check D keeps both sentences and Check F can show `Status: Claimed` with `No item name yet`.
- **Reset desk** calls all three setters. After the next render the boxes are empty, the status ternary is on the false branch, the item ternary is on the empty branch, and `location !== ""` is false, so the location line is not rendered.
- The status line and the item line use a ternary because each of those lines must always show one of two sentences. The location line uses `&&` because it should appear only when there is a location.
- A click that only calls a setter still updates the screen, because a state update re-renders the component. The lines read the state variables, so they show the new values.

### Complete code

```jsx
import { useState } from "react";

function FoundItemDesk() {
  const [itemName, setItemName] = useState("");
  const [location, setLocation] = useState("");
  const [isClaimed, setIsClaimed] = useState(false);

  return (
    <div>
      <h1>Found item desk</h1>

      <input
        value={itemName}
        onChange={(event) => setItemName(event.target.value)}
        placeholder="Item name"
      />

      <input
        value={location}
        onChange={(event) => setLocation(event.target.value)}
        placeholder="Location found"
      />

      <button onClick={() => setIsClaimed(true)}>Mark claimed</button>
      <button
        onClick={() => {
          setItemName("");
          setLocation("");
          setIsClaimed(false);
        }}
      >
        Reset desk
      </button>

      <p>{isClaimed ? "Status: Claimed" : "Status: Still at the desk"}</p>
      <p>{itemName === "" ? "No item name yet" : `Item: ${itemName}`}</p>
      {location !== "" && <p>Found at: {location}</p>}
    </div>
  );
}

export default FoundItemDesk;
```

To verify, render `<FoundItemDesk />` from the app entry you already use, then follow Checks A to F.

### Alternative approaches

- The click logic can live in named functions such as `markClaimed` and `resetDesk` instead of inline arrow functions. The setters and the rendered text stay the same.
- The empty-name check can be `itemName === ""` or `itemName.length === 0`. Both match this state, because the value is always a string.
- The three reset setters can be called in any order. The screen after that render is still empty name, empty location, and not claimed.
- Labels linked to the inputs with `htmlFor` and `id` can be added around the same controlled inputs. They do not change the state behaviour.
