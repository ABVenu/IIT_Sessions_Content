# Lecture Notes QC Report: FastAPI Dynamic Routes, Parameters & Swagger Docs

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Four curriculum topics were present: path parameters (dynamic segments, `int`/`str`, 422 vs 404), query parameters (optional `limit`/`q`, required `keyword`, defaults), OpenAPI auto-generation, Swagger UI `/docs` with Try it out.
- Grew previous `campus-api` notices CRUD instead of a new stack. Path vs query used hostel/IRCTC-style examples after official definitions, not as the definition of FastAPI.
- Structural Adherence dropped because Session Notes Length must be **480–500 lines**, and the first draft was **392** lines.
- Next-session overlap avoided: no Pydantic `BaseModel` / response_model; POST body stays `dict` + `Body(...)`. Postman not re-taught; `/docs` is the tester.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Expanded to the **480–500** band (final count: **480**): two path slots, path-vs-query decision table, browser GET examples, OpenAPI JSON keys, Swagger empty-`limit` 422, activities for `in: path` vs `in: query`.
- Re-checked complete `main.py` with comments on every line, student-facing activities, no session numbers, no duration/audience/lite wording. No images (held until notes approval).
- 422 = type/missing required query; 404 = valid int, no row. `/notices/wifi` explained as hitting GET-one, not the filter.

Expected QC result achieved.
