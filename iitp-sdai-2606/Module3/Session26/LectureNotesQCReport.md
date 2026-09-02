# Lecture Notes QC Report: FastAPI Deep Dive – Request/Response & Full CRUD

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Four curriculum topics were present: FastAPI request/response (`Request`, `JSONResponse`, status stamps), CRUD on GET/POST/PUT/DELETE, JSON bodies via `Body(...)`, and Postman tests for every route including 400/404.
- Grew the previous session’s `campus-api` (venv, Uvicorn, GET `/` and `/health`) instead of a new stack. Hostel notice board used as the CRUD example, not as the definition of FastAPI.
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **413** lines.
- Next-session overlap was controlled: no Swagger `/docs`, no Pydantic `BaseModel`, no query parameters as a taught feature. `{notice_id}` appears only so PUT/DELETE follow HTTP (DELETE has no body), with a pointer that richer URL slots come later.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Expanded to the **480–500** band (final count: **480**): POST round-trip, sample 201/400/404 JSON, POST vs PUT vs 405, extra Postman 422/Params boundary, troubleshooting and glossary rows.
- Re-checked student-facing activities (envelope, predict statuses, pick the verb, run the board). No session numbers, duration, audience, or “lite” wording. No images (held until notes approval).
- In-memory `notices` list, `JSONResponse` for 201/400/404, Postman desktop + raw JSON, order of tests (empty GET → POST → GET → PUT → DELETE).

Expected QC result achieved.
