# Lecture Notes QC Report: Client-Server Model, HTTP & JSON

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Topics covered: web architecture, client–server, request–response cycle, HTTP methods and status codes, JSON parse/stringify, and URL tracing with a simulated cycle.
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **455** lines.
- Presentation issues: some Logic bullets packed more than three sentences; URL tracing did not name the query string; HTTP headers (`Host`, `Accept`) and **401 vs 403** were too thin for a documentation-style pass; activity checks had no answer key.
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

- Expanded notes into the **480–500** band (final count: **483**): query string, resource, common headers, nested JSON, parse errors, 401 vs 403, activity check answers, extra glossary rows (`204`, `401`, `403`, `application/json`).
- Split long Logic bullets so no paragraph or bullet exceeds the three-sentence rule.
- Re-checked every code sample for end-of-line comments, student-facing activities, no session-number references, and no internal metadata wording.
- Confirmed `JSON.parse` / `JSON.stringify` examples match real JavaScript behaviour, and the fake server still checks **status** before treating a body as a train list.

Expected QC result achieved.
