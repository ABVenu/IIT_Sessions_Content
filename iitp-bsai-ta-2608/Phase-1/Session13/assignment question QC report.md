# Assignment Question QC Report: React State Management

**Cohort:** iitp-bsai-ta-2608 / Phase-1 / Session13  
**Aligned to:** Session 13 metadata and `detailed_curriculum` (Session 13: React State Management). Session 12 is used only as prior knowledge for JSX, function components, and rendering a component in a Vite app.

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **C**. Relevancy: **Yes**. `setPages(3)` replaces `0` with `3`, and the next render shows `Pages read: 3`. |
| 2 | Objective MCQ - Easy | Correct option: **B**. Relevancy: **Yes**. A controlled box stores `event.target.value` and shows that state after the re-render. |
| 3 | Objective MCQ - Easy | Correct option: **D**. Relevancy: **Yes**. `false && <p>…</p>` renders nothing, so only `Card status` shows on the first render. |
| 4 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. `paid` starts `false`, so the ternary shows `Waiting for payment`. |
| 5 | Objective MCQ - Moderate | Correct option: **D**. Relevancy: **Yes**. Changing a plain `let` does not schedule a re-render, so the paragraph stays `Seats left: 2`. |
| 6 | Objective MCQ - Moderate | Correct option: **B**. Relevancy: **Yes**. The controlled input stores `Ananya`, then `setShowPass(true)` selects `Pass for Ananya`. |
| 7 | Objective MSQ - Moderate | Correct options: **A, C**. Relevancy: **Yes**. Both bind `value` to state and update that state in `onChange`. B, D, and E do not do both. |
| 8 | Objective MSQ - Moderate | Correct options: **A, B, E**. Relevancy: **Yes**. The first click stores `Dal`, logs the current `Rice`, and the next render shows `Dal`. C and D are wrong. |
| 9 | Objective MSQ - Hard | Correct options: **A, B, D**. Relevancy: **Yes**. After typing `Isha` and one **Next** click, token is `2`, the ternary shows `Calling Isha`, and `token > 1` shows `Queue has moved`. C and E are wrong. |
| 10 | Objective MSQ - Hard | Correct options: **B, E**. Relevancy: **Yes**. Only the versions that call `setNote("Saved")` and then read `note` in the paragraph show `Saved` without throwing. A, C, and D do not. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (single `FoundItemDesk.jsx`, run in the Vite React app, paste the code into the LMS answer box). Dataset needed: **No**. Covers three `useState` values, two controlled inputs, a ternary for status, a ternary for the item name, `&&` for the location line, and button updates that re-render the screen. Checks A–F give exact expected text. |

---

## Overall Assignment QC — Iteration 2

Iteration 1 drafted the full set. Iteration 2 rechecked option length on Question 7 so the two longest snippets are not both correct, and clarified the Question 5 explanation so the JavaScript line is not called an “assignment.”

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers `useState` for a number, strings, and a boolean; replacing state with the setter; a state update re-rendering the component; the value in the current click handler staying the old value; controlled inputs (`value` plus `onChange`); `&&` when the condition is false or true; a ternary choosing one branch; and one interactive screen. Stays inside Session 13, using Session 12 only to host the component. |
| Creativity | 5 | Reading log, mess form, library card, canteen, seat counter, bus pass, city field, pantry label, clinic token desk, and a campus lost-and-found slip. The subjective task uses the same ideas on one desk screen with an empty-slip check. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Each objective item has the correct option(s), the reasoning, and why the other options are wrong. Subjective: one medium React component, exact checks, single-file submission, full walkthrough, and complete code. Correct letters are not a fixed position. |
| No Logical Mistakes | True | Traces were checked for the reading count, the bus-pass text, the token desk after one click (`token` 2, patient `Isha`), the pantry log (`Rice` then screen `Dal`), and Found Item Desk checks A–F. Wrong patterns (plain `let`, assigning to `const` state, hardcoded paragraph, unbound input, frozen `value`) do not satisfy the questions. |
| No Presentation Mistakes | True | No session-reference phrasing. Constraints, starting values, and expected text are stated. Spelling and option labels were rechecked after the Question 7 edit. |

**Expected result:** All criteria met — **QC passed**. No further modification required.

---

## Scope Guardrails Applied

| Outside this session | Assignment treatment |
|---|---|
| `useEffect`, fetching, and loading flags | Not asked. |
| React Router, Tailwind, and deployment | Not asked. |
| Lifting state, context, or a shared store | Not asked. The subjective screen keeps state inside one component. |
| Storing a list of items, or updating an object or array in state | Not asked. The desk holds one slip. |
| `useRef` and uncontrolled inputs as the required pattern | Not asked. Question 7 uses an unbound box only as a wrong option. |
