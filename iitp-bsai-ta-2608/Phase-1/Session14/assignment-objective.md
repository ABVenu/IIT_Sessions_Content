# Objective Assignment: Tailwind CSS with React

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

Ananya installs Tailwind in a Vite React app and writes this JSX:

```jsx
<div className="bg-green-500">Mess open</div>
```

The words stay on a plain, uncoloured background. Which missing step is the most likely cause?

A. The `div` must use `class` instead of `className`  
B. Colour utilities also need an inline `style` attribute to work  
C. `src/index.css` never loads Tailwind with `@import "tailwindcss"`  
D. `npm install` alone turns every utility on, so the import is optional  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because installing the packages is not enough. The CSS file that the app already imports must contain `@import "tailwindcss"`. Without that line, names such as `bg-green-500` sit in the JSX and draw no colour.

A is incorrect because React uses `className`, not `class`. Switching to `class` would make the situation worse. B is incorrect because a colour utility stands on its own; a separate `style` attribute is not required. D is incorrect because `npm install` only downloads the packages. Vite still needs the plugin, and `index.css` still needs the import.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A hostel notice card uses this markup:

```jsx
<div className="p-4 bg-white rounded-lg">Quiet hours</div>
```

How much inner space does `p-4` add around the words?

A. 4 pixels on every side  
B. 16 pixels on every side  
C. 4 rem on the left only  
D. 16 pixels on the top only  

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the number in `p-4` is a step on Tailwind’s scale, not a raw pixel count. Step `4` is 1rem, which is 16 pixels, and `p` with no side letter applies that space on all four sides.

A is incorrect because step `1` is 4 pixels. Reading `4` as 4 pixels is a common slip. C is incorrect because `p-4` is not left-only padding, and the step is not 4rem. D is incorrect because top-only padding is `pt-4`.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

Kabir wants to attach Tailwind utilities to a React `h1`. Which attribute must he write on that element?

A. `className`  
B. `class`  
C. `styleName`  
D. `cssClass`  

**Correct Answer:** A

**Answer Explanation:**  
A is correct because JSX already uses `class` as a reserved word in JavaScript. The attribute that holds utility classes is `className`, with a capital N.

B is incorrect because `class` is the HTML name, not the React attribute. C and D are incorrect because they are not the React attribute for CSS classes.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A canteen heading is written like this:

```jsx
<h1 className="text-3xl font-bold text-blue-600">Hello</h1>
```

What does `text-blue-600` change?

A. The background behind the heading  
B. The outline around the heading  
C. The colour of the letters  
D. The font size of the heading  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because a colour utility names the role first. `text-` colours the letters. Shade `600` is a strong blue.

A is incorrect because the background role is `bg-`, as in `bg-blue-600`. B is incorrect because a border colour needs `border` plus a class such as `border-blue-600`. D is incorrect because size is `text-3xl`. `text-blue-600` does not set the size.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A library slip needs 16 pixels of padding on the left and the right only. The top and bottom should stay tight. Which class matches that request?

A. `px-4`  
B. `py-4`  
C. `p-4`  
D. `pt-4`  

**Correct Answer:** A

**Answer Explanation:**  
A is correct because `x` is the horizontal axis. `px-4` is left and right padding at step `4`, which is 16 pixels.

B is incorrect because `py-4` is top and bottom. C is incorrect because `p-4` pads every side. D is incorrect because `pt-4` pads only the top.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Meera already has a working name screen. The input uses `useState`, `value`, and `onChange`. She only adds Tailwind classes such as `mt-4 w-full p-3 border rounded-lg` on that input. What happens to the state logic?

A. `useState` is replaced, so typing no longer updates the greeting  
B. `value` and `onChange` must be removed for the utilities to apply  
C. The look changes; the stored name and the re-render stay  
D. `rounded-lg` stores the typed name, so `setName` is no longer used  

**Correct Answer:** C

**Answer Explanation:**  
C is correct because Tailwind only changes appearance through `className`. `useState`, `value`, and `onChange` keep working. A state update still re-renders the component.

A is incorrect because adding classes does not replace React state. B is incorrect because those two attributes are what make the box controlled; they are not in the way of utilities. D is incorrect because `rounded-lg` only curves the corners. It does not store text.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

Which of the following statements about Tailwind spacing are true?

A. `p-4` adds 16 pixels of padding on all four sides  
B. `p-4` adds 4 pixels of padding on all four sides  
C. `p-6` adds 24 pixels of padding on all four sides  
D. `m-4` is the class for padding inside the box  
E. `px-4` adds 16 pixels of padding on the left and the right  

**Correct Answers:** A, C, E

**Answer Explanation:**  
A is correct because `p` with no side letter is every side, and step `4` is 16 pixels. C is correct because step `6` is 1.5rem, which is 24 pixels. E is correct because `x` is left and right, still at step `4`.

B is incorrect because 4 pixels is step `1`, not step `4`. D is incorrect because `m` is margin, the gap outside the box. Padding uses `p`.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A hostel notice bar should show `Hostel` at one end and `Profile` at the other end of a single horizontal row. Which utilities must sit on that parent so the two labels are pushed to opposite ends?

A. `flex`  
B. `justify-between`  
C. `flex-col`  
D. `pt-4`  
E. `text-3xl`  

**Correct Answers:** A, B

**Answer Explanation:**  
A is correct because `flex` turns the parent into a flex container. The default direction is a horizontal row. B is correct because `justify-between` pushes the first child to one end and the last child to the other end.

C is incorrect because `flex-col` stacks the labels top to bottom, so they are not at opposite ends of a row. D is incorrect because `pt-4` only adds top padding. E is incorrect because `text-3xl` only changes font size.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A campus page uses this parent:

```jsx
<div className="flex flex-col gap-4 p-4 md:flex-row">
  <div className="p-6 bg-blue-100">Main content</div>
  <div className="p-6 bg-slate-100">Side panel</div>
</div>
```

Which statements are true?

A. On a 500 pixel phone, the two panels stack in a column  
B. From 768 pixels upward, the two panels sit side by side in a row  
C. `md:flex-row` applies on every width, including a narrow phone  
D. `gap-4` applies only after the `md` width  
E. The unprefixed `flex-col` is the small-screen layout  

**Correct Answers:** A, B, E

**Answer Explanation:**  
A is correct because Tailwind is mobile first. With no matching `md:` prefix on a 500 pixel screen, `flex-col` stays in charge, so the panels stack. B is correct because `md:` starts at 768 pixels, and `md:flex-row` then switches the same parent to a row. E is correct because classes with no prefix are the phone style.

C is incorrect because a prefixed class joins in only from that breakpoint upward. A narrow phone keeps the column. D is incorrect because `gap-4` has no prefix, so the 16 pixel gap applies at every width.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

Riya restyles a working Welcome card. She keeps `useState` and the controlled input. The outer box uses `max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow`. The greeting paragraph uses `text-base sm:text-lg`. The main line of the card also uses `className="text-2xl font-bold text-slate-800"`. Which statements are true?

A. `mx-auto` centres the width-capped card with equal left and right margins  
B. `p-6` is 24 pixels of padding inside the card  
C. `sm:text-lg` enlarges the greeting from 640 pixels upward  
D. `text-2xl` and `font-bold` are the same class, so one of them can be dropped  
E. Adding these classes replaces `useState`, so the greeting stops updating  

**Correct Answers:** A, B, C

**Answer Explanation:**  
A is correct because `max-w-md` caps the width and `mx-auto` centres that box. B is correct because step `6` is 1.5rem, which is 24 pixels, and `p` applies it on every side. C is correct because `sm:` starts at 640 pixels, so the greeting stays `text-base` on a narrower phone and becomes `text-lg` from that width up.

D is incorrect because size and weight are separate. `text-2xl` only changes size. `font-bold` only changes weight. E is incorrect because restyling changes `className` only. The stored name and the re-render stay as they were.
