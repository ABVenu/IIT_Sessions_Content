# Lecture Notes QC Report: Asynchronous JavaScript

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Topics covered well: sync vs async, callbacks, `setTimeout` / `setInterval`, and async + DOM practice.
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **447** lines.
- Presentation issue: `clearTimeout` was shown as a short JavaScript snippet instead of a full start-to-finish HTML example with comments on every line.
- Logical issue: the send-button toast used a nested hide timeout without storing/clearing its id, so a later send could be hidden by an earlier hide callback.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Expanded notes into the **480–500** band (final count: **484**): milliseconds, named vs anonymous callbacks, full `clearTimeout` page, snooze activity, and `createElement` in the async + DOM section.
- Replaced the `clearTimeout` snippet with a complete HTML example (Start / Cancel) and comments on every line.
- Stored `hideId` for the toast hide timeout and `clearTimeout(hideId)` on a new Send click.
- Re-checked every code sample for end-of-line comments, student-facing activities, no session-number references, and no internal metadata wording.

Expected QC result achieved.
