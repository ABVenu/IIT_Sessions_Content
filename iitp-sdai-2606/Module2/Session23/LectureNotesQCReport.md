# Lecture Notes QC Report: Promises Basics & Fetch API – GET Requests

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Topics covered: Promise meaning and why async work needs one, pending/fulfilled/rejected, `.then()` / `.catch()`, chains, `fetch` GET, Response + `json()`, network vs HTTP errors, and displaying JSONPlaceholder results in the DOM.
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **424** lines.
- Presentation issues: executor / `.then` / `.catch` were missing real-life examples; glossary row for **settle** read as “left pending”; one bullet used “the next `.then` then receives.”
- Length and those presentation gaps needed a second pass before the expected QC result.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Expanded notes into the **480–500** band (final count: **481**): callbacks vs Promises, real-life examples for executor / `.then` / `.catch`, address-bar vs `fetch`, query strings, CORS, `Accept` header, body-read-once, nested `address.city`, collection vs resource, `ok` check + `.catch` pattern, DevTools Headers/Preview, button disable, and extra glossary rows.
- Corrected settle wording to “no longer pending,” and removed the doubled “then.”
- Re-checked every code sample for end-of-line comments, student-facing activities with check answers, no session-number references, and no internal metadata wording.
- Confirmed `fetch` fulfils on HTTP 404 (JSONPlaceholder `/users/999`), rejects on network failure, and that `return response.json()` is required for the second `.then`.

Expected QC result achieved.
