# Assignment Question QC Report: Tailwind CSS with React

**Cohort:** iitp-bsai-ta-2608 / Phase-1 / Session14  
**Aligned to:** Session 14 metadata and `Lecture Notes Released.md` (Tailwind CSS with React). Earlier React state is used only as the host behaviour that Tailwind restyles.

---

## Per-Question QC

| Question number | Type | Remarks |
|---|---|---|
| 1 | Objective MCQ - Easy | Correct option: **C**. Relevancy: **Yes**. A utility such as `bg-green-500` draws no colour when `index.css` never imports Tailwind. |
| 2 | Objective MCQ - Easy | Correct option: **B**. Relevancy: **Yes**. Step `4` is 16 pixels, and `p` with no side letter applies all sides. |
| 3 | Objective MCQ - Easy | Correct option: **A**. Relevancy: **Yes**. JSX uses `className`, not `class`. |
| 4 | Objective MCQ - Easy | Correct option: **C**. Relevancy: **Yes**. `text-blue-600` colours the letters; size is `text-3xl` and fill is `bg-`. |
| 5 | Objective MCQ - Moderate | Correct option: **A**. Relevancy: **Yes**. `px-4` is left and right padding at 16 pixels. |
| 6 | Objective MCQ - Moderate | Correct option: **C**. Relevancy: **Yes**. Restyling changes `className` only; `useState`, `value`, and `onChange` stay. |
| 7 | Objective MSQ - Moderate | Correct options: **A, C, E**. Relevancy: **Yes**. `p-4` is 16px all sides, `p-6` is 24px all sides, `px-4` is left and right. B and D mix up the scale and `m` versus `p`. |
| 8 | Objective MSQ - Moderate | Correct options: **A, B**. Relevancy: **Yes**. Opposite ends of a row need `flex` and `justify-between`. `flex-col`, `pt-4`, and `text-3xl` do not do that job. |
| 9 | Objective MSQ - Hard | Correct options: **A, B, E**. Relevancy: **Yes**. Mobile first: column on 500px, row from 768px, unprefixed `flex-col` is the phone style. C and D treat prefixed classes as always-on. |
| 10 | Objective MSQ - Hard | Correct options: **A, B, C**. Relevancy: **Yes**. `mx-auto` centres, `p-6` is 24px, `sm:text-lg` starts at 640px. Size and weight stay separate, and state is not replaced. |
| 1 | Subjective - Medium Practical Task | Medium difficulty: **Yes**. Clear submission instructions: **Yes** (single `MessTokenCard.jsx`, run in the Vite React app, paste the code into the LMS answer box). Dataset needed: **No**. Covers the restyle card classes, a controlled name input, a greeting ternary, and `flex-col` plus `md:flex-row`. Checks A–E give exact text and layout. |

---

## Overall Assignment QC — Iteration 1

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Covers Vite Tailwind setup (`@import "tailwindcss"`), `className`, the spacing scale and side letters, colour roles, typography size versus weight, flex plus `justify-between`, mobile-first `sm`/`md`, and restyling without replacing `useState`. |
| Creativity | 4 | Scenarios (mess, hostel, library, canteen) are clear, but Question 6’s correct option was the longest line, which made the answer easier to guess. |
| Structural Adherence | 5 | Objective: 10 questions (6 MCQ: 4 Easy + 2 Moderate; 4 MSQ: 2 Moderate + 2 Hard), ordered Easy → Hard. Each item has the correct option(s), the reasoning, and why the other options are wrong. Subjective: one medium single-file task with exact checks. |
| No Logical Mistakes | True | Spacing steps, breakpoints (640 / 768), `px` versus `py`, and the restyle-versus-state split match the notes. |
| No Presentation Mistakes | True | No session-reference phrasing. Expected class lists and greeting text are stated. |

**Expected result:** Creativity below 5. Question 6 option lengths were shortened so the correct line is not the longest. QC rerun below.

---

## Overall Assignment QC — Iteration 2

| Criteria | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 | Same scope as Iteration 1. Nothing outside the notes (`hover`, `lg:`, `hidden`, Grid, or a new CSS file) is required. |
| Creativity | 5 | Mess open notice, hostel card, canteen heading, library slip, Welcome restyle, campus two-panel layout, and a mess token card. Correct letters vary (A, B, C) and are not a fixed position. Longest-option guessing is blocked after the Question 6 edit. |
| Structural Adherence | 5 | 10 objective items in the required mix and order. Subjective is one medium React + Tailwind file, case-c submission, full walkthrough, complete code, and alternatives. |
| No Logical Mistakes | True | Traces hold for `p-4` / `p-6` sizes, `px-4`, `md:flex-row` from 768px, `sm:text-lg` from 640px, and Checks A–E on `MessTokenCard`. |
| No Presentation Mistakes | True | Question 6 options are now similar in length. Spelling and option labels were rechecked. |

**Expected result:** All criteria met — **QC passed**. No further modification required.

---

## Scope Guardrails Applied

| Outside this session | Assignment treatment |
|---|---|
| `hover:`, `focus:`, `lg:`, `hidden`, and `block` | Not asked. |
| CSS Grid, arbitrary values, and a `tailwind.config.js` rewrite | Not asked. |
| Replacing `useState` or removing controlled inputs | Used only as wrong options. The subjective card keeps the name in state. |
| Building a multi-file app or a new Vite project from zero | Not asked. The subjective file runs in the existing Vite React app. |
