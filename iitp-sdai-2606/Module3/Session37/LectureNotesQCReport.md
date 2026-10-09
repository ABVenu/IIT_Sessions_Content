# Lecture Notes QC Report: GenAI Coding Lab III

## QC Iteration 1

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **4**
- No Logical Mistakes: **False**
- No Presentation Mistakes: **False**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Notes from QC Iteration 1:

- Lab assumed a thinner CRUD app and used `/students/by-city`, which would duplicate the assembled `?city=` filter.
- Drafts were not required to keep CORS, middleware, files, or `/hostels/summary`. Length was under 480.

## QC Iteration 2

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 2:

- Same `campus_api` context: prompt wrapper forbids removing CORS, middleware, files, or summary. Extra skeleton is **GET `/students/high-marks`**, not a second city route.
- Examples include `hostel_name`, Guest House `null` average, PUT full body, multipart upload. Checklist rejects list-in-memory and “simplify main.py.” Length is **480** or just above after the last keep-list lines.

Expected QC result achieved.

## QC Iteration 3

- Content Coverage (1 to 5): **5**
- Creativity (1 to 5): **5**
- Structural Adherence (1 to 5): **5**
- No Logical Mistakes: **True**
- No Presentation Mistakes: **True**
- No Previous Session Number References: **True**
- No Metadata/internal reference like “Keep is light”: **True**

Fix applied before QC Iteration 3: opened with **Flow of this session**, then **Ideal features** (keep-routes plus GET `/students/high-marks`). Duplicate keep-table later in the notes removed. Length **499** lines.

Expected QC result achieved.
