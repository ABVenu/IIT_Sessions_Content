# Lecture Notes QC Report: GenAI Coding Lab II

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Topics covered: AI layout generation (strong vs weak prompts, semantic HTML, Flex/Grid, id contract), AI JavaScript assistance (one-feature prompts, `render` / `current` / search), API integration debugging (evidence table, `ok` check, missing `return`, wrong shape/fields), and code refinement (six passes, loading/empty/error states, accessibility).
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **563** lines (three overlapping full HTML files).
- Presentation issues: Fetch complete example dropped `header` / `main` / `footer` and the search `label` taught in the layout section; one CSS comment was left unclosed (`/* Busy state`).
- Logical issue: the “missing `return`” activity said the page would be empty; with `.catch` in the complete example the status line shows an error instead.
- Length and those gaps needed a second pass before the expected QC result.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Trimmed into the **480–500** band (final count: **500**): removed the duplicate sample-data HTML page; kept layout-only complete file plus one full Fetch page that includes `render`, search, `ok` check, and comments on every line.
- Aligned the Fetch example with the layout file (semantic regions, visible `label`, matching hostel-green CSS). Closed the CSS comment.
- Corrected the debug activity so missing `return` predicts `undefined` data and `.catch`, not a silently empty board.
- Re-checked student-facing activities (layout prompt, Clear button, break-and-debug, refine passes), no session-number references, no duration/audience/internal “lite” wording, and 3-sentence paragraph rule.
- Confirmed JSONPlaceholder `/posts?_limit=6` is an array with `title` / `body`; `/postz` is a 404 teaching case; `fetch` still fulfils on HTTP errors so `response.ok` is required.

Expected QC result achieved.

## QC Iteration 3

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 3 (curriculum overlap + pedagogical flow):

- Next session (25) is backend / FastAPI setup (venv, first GET endpoint). This lab must stay on **client-side** HTML/CSS/JS and Fetch GET.
- **Logical / pedagogical leak:** Complete example used `forEach` / `.filter` / `indexOf` — array methods not taught in JS fundamentals (students have `for` loops and `includes` from form validation). Closing named “server side” and “when the code is an API,” which is the next module’s job.
- **Presentation / structure:** Notes had grown to **512** lines (max 500). CORS appeared in debug/glossary though enabling CORS is a later backend topic.

## QC Iteration 4

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 4:

- Card render and search now use a **`for` loop** plus **`includes`** (already taught). Note added: if AI writes `.filter`, ask it to use a `for` loop you know.
- Future link is generic (brief–generate–verify behind the page). No FastAPI, venv, or server GET endpoints. CORS dropped from debug/glossary.
- Trimmed to **500** lines. Layout, JS-with-AI, Fetch debug-with-evidence, and refinement passes still cover the four curriculum topics. Fetch remains GET on JSONPlaceholder.

Expected QC result achieved.
