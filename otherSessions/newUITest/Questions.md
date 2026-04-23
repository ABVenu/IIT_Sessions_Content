# Sample questions — **HTML forms & simple math (mixed)**

*Topic: basic form patterns (labels, inputs, methods) plus arithmetic and number sense. 6 objective + 1 subjective. Options are plain text.*

---

## Objective

### 1. (Easy, MCQ — single correct)

Mira is building a login page. She wants the word **Email** to be clickable so that focus moves to the text field when a keyboard or screen-reader user activates it. Which approach correctly ties the label to the field?

- A) Put “Email” only in a paragraph above the box, with no programmatic link to the input  
- B) Use a label whose “for” value matches the input’s id, and give the input that id (and use an email-type field)  
- C) Use a label and an input, but do not use a matching id on the input or “for” on the label  
- D) Put the word only in the field’s title and do not use a label element  

**Answer explanation (for platform):** **B** — The label’s “for” must match the input’s id so they are associated and focus moves correctly. A is not tied to the field; C is not associated as shown; D is a weak substitute for a proper label.

---

### 2. (Easy, MCQ — single correct)

Rohan’s form has an **optional** company name field. The field is empty, but he wants a short hint inside the box that goes away when the user types, and that is **not** sent as the field’s value if the user leaves it blank. What should he use?

- A) Default text in the box that can be submitted as the value if not changed  
- B) Hint text that is not the value and clears as the user types (placeholder)  
- C) A layer of text on top of the input using styling  
- D) Putting the label wording in the name attribute  

**Answer explanation:** **B** — Placeholder-style hint text is for display only; a default value (A) can be submitted. C is fragile; D misuses the name attribute.

---

### 3. (Easy, MCQ — single correct)

A shipping form must not submit until the user picks **one** delivery option: Standard, Express, or Overnight. What is the most appropriate control for “exactly one choice” in one group on the form?

- A) Three checkboxes, one per option  
- B) Radio buttons that all share the same name for the group  
- C) A single line where the user types options separated by commas  
- D) Three separate drop-down lists, one for each line  

**Answer explanation:** **B** — One name groups radios so only one can be selected. Checkboxes (A) allow many; (C) is not a standard pattern for this; (D) is the wrong pattern for one logical choice.

---

### 4. (Moderate, MCQ — single correct)

A shirt’s sale price is ₹400 after a **20% discount** on the original price. What was the original price in rupees? (The discount is 20% of the original price.)

- A) 480  
- B) 500  
- C) 520  
- D) 600  

**Answer explanation:** **B** — After a 20% cut, the customer pays 80% of the original, so original = 400 ÷ 0.8 = 500 rupees.

---

### 5. (Moderate, MSQ — multiple correct)

Select **all** the numbers that are **prime** numbers.

- A) 2  
- B) 9  
- C) 17  
- D) 21  

**Answer explanation:** **A and C** — 2 and 17 are prime. 9 and 21 are composite (9 = 3×3, 21 = 3×7).

---

### 6. (Hard, MSQ — multiple correct)

Which of the following are **equal to one half**? (Select all that apply.)

- A) 0.5  
- B) 2/4  
- C) 3/6  
- D) 1/3  

**Answer explanation:** **A, B, and C** — Each is the same as one half. 1/3 is not one half.

---

## Subjective

### 7. (Easy, short written answer)

A search form should show the search words in the **web address** so people can bookmark or share the link (like a question mark and q= in the address bar). In one or two sentences: should the form use the usual **GET** style or the usual **POST** style for this, and in plain words what happens to the field values? (You may name GET or POST.)

**Answer explanation (for platform):** Use **GET**. The browser adds the field names and values to the end of the URL, so the search appears in the address bar. With **POST**, those values are normally not shown in the URL in the same way for a typical form.

---
