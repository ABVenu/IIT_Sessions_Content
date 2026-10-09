# Objective Assignment: React State Management

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A reading log starts like this:

```jsx
function ReadingNote() {
  const [pages, setPages] = useState(0);

  return (
    <div>
      <p>Pages read: {pages}</p>
      <button onClick={() => setPages(3)}>Save</button>
    </div>
  );
}
```

The screen first shows `Pages read: 0`. Meera clicks **Save** once. What does the paragraph show after that click?

A. `Pages read:`  
B. `Pages read: 03`  
C. `Pages read: 3`  
D. `Pages read: 0`

**Correct Answer:** C

**Answer Explanation:**  
C is correct because `setPages(3)` replaces the stored number with `3`. React renders the component again, and `{pages}` prints that new number.

A is incorrect because the state is the number `3`, so the paragraph is not left blank. B is incorrect because the setter replaces `0`; it does not glue `0` and `3` into `03`. D is incorrect because that is the text from the first render, before **Save**.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A mess form keeps the dish name in state:

```jsx
const [dish, setDish] = useState("");

<input
  value={dish}
  onChange={(event) => setDish(event.target.value)}
/>
```

The box starts empty. Riya types the letter `P`. What is true right after that keystroke?

A. The box stays empty until the browser tab is refreshed  
B. `dish` becomes `"P"`, the component renders again, and the box shows `P`  
C. `dish` stays `""` because a text box can only change a prop  
D. `onChange` is skipped whenever `value` is already written on the input  

**Correct Answer:** B

**Answer Explanation:**  
B is correct because this input is controlled. The keystroke runs `onChange`, `setDish` stores `"P"`, and the next render puts `value={dish}` back into the box.

A is incorrect because the update is applied on the next render, without a refresh. C is incorrect because `setDish` changes this component’s state; the snippet does not read a prop. D is incorrect because `onChange` is what writes the new text into state. With both `value` and `onChange`, typing works.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A library card uses this state and markup:

```jsx
const [isLate, setIsLate] = useState(false);

return (
  <div>
    <p>Card status</p>
    {isLate && <p>Return the book today</p>}
  </div>
);
```

What is on the screen the first time this component renders?

A. `Card status` and `Return the book today`  
B. `Return the book today` only  
C. No text, because `useState(false)` stops the whole component  
D. `Card status` only  

**Correct Answer:** D

**Answer Explanation:**  
D is correct because `isLate` starts as `false`. `false && <p>Return the book today</p>` adds nothing. The first paragraph does not depend on `isLate`, so `Card status` still shows.

A is incorrect because the warning paragraph is rendered only when `isLate` is true. B is incorrect because `Card status` is outside the `&&` check. C is incorrect because `false` only makes that one `&&` expression render nothing. The component still returns the rest of the JSX.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A canteen screen starts like this:

```jsx
const [paid, setPaid] = useState(false);

return <p>{paid ? "Receipt ready" : "Waiting for payment"}</p>;
```

What text is visible at the start?

A. `Waiting for payment`  
B. `paid`  
C. `Receipt ready`  
D. `Receipt ready` followed by `Waiting for payment`  

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `paid` starts as `false`, so the ternary chooses the branch after the colon.

B is incorrect because the screen prints one of the two strings, not the variable name. C is incorrect because `Receipt ready` is the branch used when `paid` is `true`. D is incorrect because a ternary renders one branch, not both.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

Kabir writes a seat counter without `useState`:

```jsx
function SeatCounter() {
  let seats = 2;

  return (
    <div>
      <p>Seats left: {seats}</p>
      <button
        onClick={() => {
          seats = seats - 1;
        }}
      >
        Book one
      </button>
    </div>
  );
}
```

He clicks **Book one**. The paragraph still says `Seats left: 2`. Why?

A. `seats - 1` is invalid JavaScript, so the click is cancelled before it runs  
B. Every button click restores variables to the values written at the top of the function  
C. React refreshes a number on screen only when that number was created with `useState(0)`  
D. Assigning a new value to a plain `let` does not ask React to render the component again  

**Correct Answer:** D

**Answer Explanation:**  
D is correct because `seats` is an ordinary variable. The click changes it inside that function, but React was not given a state update, so it does not render the component again. The paragraph keeps the `2` from the last render.

A is incorrect because `seats - 1` is valid JavaScript. The line `seats = seats - 1` runs; it just does not refresh the screen. B is incorrect because a click does not automatically replay `let seats = 2`. The screen is unchanged because there is no re-render. C is incorrect because `useState` can start at any value, including `2`. The missing piece here is a state setter, not a starting value of `0`.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A bus-pass screen looks like this:

```jsx
function BusPass() {
  const [name, setName] = useState("");
  const [showPass, setShowPass] = useState(false);

  return (
    <div>
      <input
        value={name}
        onChange={(event) => setName(event.target.value)}
      />
      <button onClick={() => setShowPass(true)}>Show pass</button>
      {showPass ? <p>Pass for {name}</p> : <p>Pass is hidden</p>}
    </div>
  );
}
```

Ananya types `Ananya` in the box, then clicks **Show pass**. What does the paragraph say?

A. `Pass is hidden`  
B. `Pass for Ananya`  
C. `Pass for`  
D. `Pass for name`  

**Correct Answer:** B

**Answer Explanation:**  
B is correct because each typed letter is stored with `setName`, so `name` is `"Ananya"`. The click sets `showPass` to `true`, the component renders again, and the ternary chooses `Pass for {name}`.

A is incorrect because that sentence is the `false` branch, and `showPass` is now `true`. C is incorrect because `name` is not empty after the typing. D is incorrect because `{name}` prints the stored text, not the word `name`.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A city box should display the text stored in state, and typing in the box should update that state. Which snippets do both?

A.

```jsx
const [city, setCity] = useState("");
<input value={city} onChange={(event) => setCity(event.target.value)} />
```

B.

```jsx
function CityField() {
  const [city, setCity] = useState("");
  return (
    <div>
      <p>City on file: {city}</p>
      <input onChange={(event) => setCity(event.target.value)} />
    </div>
  );
}
```

C.

```jsx
const [city, setCity] = useState("Pune");
<input value={city} onChange={(event) => setCity(event.target.value)} />
```

D.

```jsx
function CityField() {
  const [city, setCity] = useState("Pune");
  return (
    <div>
      <p>{city}</p>
      <input value="Pune" onChange={(event) => setCity(event.target.value)} />
    </div>
  );
}
```

E.

```jsx
const [city, setCity] = useState("");
<input value={city} />
```

**Correct Answer:** A, C

**Answer Explanation:**  
A is correct because `value={city}` shows the state and `onChange` writes each new string with `setCity`. The box starts empty. After a keystroke, the next render shows the stored text.

C is correct for the same reason. The only difference is the starting text `"Pune"`. Typing still replaces `city`, and the next render shows the new text in the box.

B is incorrect because the input has no `value`. The paragraph can show `city`, but the box itself is not displaying state. The browser keeps whatever was typed in the box.

D is incorrect because the box is locked to the fixed string `"Pune"`. `setCity` updates state, and the paragraph can change, but the box does not show `city`.

E is incorrect because the box shows `city`, but nothing updates `city` when the user types. The box stays `""`.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A pantry label uses this component:

```jsx
function Pantry() {
  const [item, setItem] = useState("Rice");

  function switchItem() {
    setItem("Dal");
    console.log(item);
  }

  return (
    <div>
      <p>{item}</p>
      <button onClick={switchItem}>Switch</button>
    </div>
  );
}
```

The screen first shows `Rice`. Which statements are true the first time **Switch** is clicked?

A. After React renders again, the paragraph shows `Dal`  
B. `console.log(item)` prints `Rice`  
C. `console.log(item)` prints `Dal` before the paragraph changes  
D. `useState("Rice")` runs again on the click and forces the paragraph to stay `Rice`  
E. The paragraph can change because `setItem` causes the component to render again  

**Correct Answer:** A, B, E

**Answer Explanation:**  
A is correct because `setItem("Dal")` stores `Dal`. On the next render, `{item}` is `Dal`.

B is correct because `item` inside `switchItem` is still the value from the current render, which is `"Rice"`. The log runs before the next render.

E is correct because calling the setter is what asks React to render this component again with the stored value.

C is incorrect because the log reads the current `item`. It does not read the value that will appear on the next render. D is incorrect because the argument `"Rice"` is used as the initial state on the first render only. A later click does not replay that initial value.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A clinic desk uses two pieces of state:

```jsx
function TokenDesk() {
  const [token, setToken] = useState(1);
  const [patient, setPatient] = useState("");

  return (
    <div>
      <p>Now serving: {token}</p>
      <input
        value={patient}
        onChange={(event) => setPatient(event.target.value)}
      />
      <button onClick={() => setToken(token + 1)}>Next</button>
      {patient.length > 0 ? (
        <p>Calling {patient}</p>
      ) : (
        <p>Waiting for a name</p>
      )}
      {token > 1 && <p>Queue has moved</p>}
    </div>
  );
}
```

The page has just loaded. The clerk types `Isha`, then clicks **Next** once. Which statements are true after that click?

A. `Now serving: 2` is on the screen  
B. `Calling Isha` is on the screen  
C. `Calling Isha` and `Waiting for a name` are both on the screen  
D. `Queue has moved` is on the screen  
E. The input is empty because **Next** clears `patient`  

**Correct Answer:** A, B, D

**Answer Explanation:**  
A is correct because `token` starts at `1` and one click runs `setToken(token + 1)`, so the next render shows `2`.

B is correct because the controlled input stored `Isha` in `patient`. `patient.length > 0` is true, so the ternary renders `Calling Isha`.

D is correct because `token` is `2`, and `2 > 1` makes the `&&` branch render `Queue has moved`.

C is incorrect because the ternary renders one branch. `Waiting for a name` was the empty-name branch, and the name is no longer empty. E is incorrect because **Next** only calls `setToken`. `patient` stays `"Isha"`, so the input still shows that name.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

Each version below is a separate component. The paragraph starts as `Draft`. The user clicks **Keep** once.

Which versions show the text `Saved` in the paragraph after that click, without throwing an error?

A.

```jsx
function NoteA() {
  let note = "Draft";
  return (
    <div>
      <p>{note}</p>
      <button onClick={() => { note = "Saved"; }}>Keep</button>
    </div>
  );
}
```

B.

```jsx
function NoteB() {
  const [note, setNote] = useState("Draft");
  return (
    <div>
      <p>{note}</p>
      <button onClick={() => setNote("Saved")}>Keep</button>
    </div>
  );
}
```

C.

```jsx
function NoteC() {
  const [note, setNote] = useState("Draft");
  return (
    <div>
      <p>{note}</p>
      <button onClick={() => { note = "Saved"; }}>Keep</button>
    </div>
  );
}
```

D.

```jsx
function NoteD() {
  const [note, setNote] = useState("Draft");
  return (
    <div>
      <p>Draft</p>
      <button onClick={() => setNote("Saved")}>Keep</button>
    </div>
  );
}
```

E.

```jsx
function NoteE() {
  const [note, setNote] = useState("Draft");
  return (
    <div>
      <p>{note === "Saved" ? "Saved" : "Draft"}</p>
      <button onClick={() => setNote("Saved")}>Keep</button>
      {note === "Saved" && <p>Note is stored</p>}
    </div>
  );
}
```

**Correct Answer:** B, E

**Answer Explanation:**  
B is correct because `setNote("Saved")` stores the new text and React renders again. The paragraph reads `{note}`, so it shows `Saved`.

E is correct because the same setter runs. On the next render `note === "Saved"` is true, so the ternary prints `Saved`. The extra `&&` line also appears, and the first paragraph still shows `Saved`.

A is incorrect because `note` is a plain `let`. The click does not update state, so React does not render again, and the paragraph stays `Draft`.

C is incorrect because `note` from `useState` is a `const`. `note = "Saved"` throws a TypeError. The setter is never called, so the paragraph does not change to `Saved`.

D is incorrect because the setter does run and the component renders again, but the paragraph is the fixed text `Draft`. It does not read `note`, so the screen still says `Draft`.
