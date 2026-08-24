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

## QC Iteration 3

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 3 (curriculum overlap + pedagogical flow):

- Curriculum checked against `detailed_curriculum`: Session 22 is client–server, HTTP methods/status, JSON parse/stringify, and tracing a URL visit. Session 23 is Promises, `fetch` GET, `Response` / `response.json()`, and live API display.
- **Logical / pedagogical leak:** Hands-on treated typing a URL as returning a JSON train list, then ran a `fakeServer` click handler (method + path → status + JSON → parse → DOM). That is the Session 23 Fetch workflow without the name `fetch`. JSON.parse of the body was also framed as “next session.”
- **Presentation:** Notes said “you will not use `fetch` yet” and closed by naming **Fetch API** and **Promises** — introducing next-session tools the way a loops lesson should not introduce arrays. A first visit’s extra files were listed as CSS, images, **and JSON**, which mixes a document load with a later data request.
- Coverage of Session 22 topics was complete; the fail is extra next-session behaviour, not missing current topics.

## QC Iteration 4

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 4:

- Removed `fakeServer`, `fetch`, and **Promises** teaching. URL trace is now a **GET page** (`text/html`, Network document row). JSON is a **different body**; students unpack **copied** Network text with `JSON.parse` after reading status.
- Clarified data cycle vs page cycle on the HTTP-shape example; wrap-up no longer describes “GET → parse → show list” as what typing a URL does.
- Future link is generic (“send this kind of request from your own JavaScript”) with no next-session API names. Pre-read aligned: first visit is HTML; JSON is unpacked from text.
- Re-checked JSON samples in Python/`json.loads`; stringify round-trip matches the notes. Length **494** lines (band 480–500). Split remaining four-sentence connectors. Image URLs still use the S3 `session22` path only.

Expected QC result achieved.
