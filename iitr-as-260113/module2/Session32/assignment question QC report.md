# Assignment Question QC Report
**Session:** Session 34 — Working with APIs and JSON
**Course:** iitr-as-260113 | Module 2

---

## Section 1: Objective Assignment QC

| Q# | Type | Correct Option | Correct Option Relevant to Question? | Remarks |
|----|------|----------------|--------------------------------------|---------|
| Q1 | MCQ (Easy) | C) GET | Yes | Tests HTTP method selection in a practical fetch scenario. Distractors are distinct HTTP methods. All options are clearly incorrect for the scenario. |
| Q2 | MCQ (Easy) | D) Resource does not exist | Yes | Tests status code interpretation in a real browsing scenario. 404 is directly taught in session. Distractors map to other common codes (200, 401, 500). |
| Q3 | MCQ (Easy) | B) Use json.loads() | Yes | Tests json.loads() usage in a realistic API response parsing scenario. Distractor A confuses loads/dumps direction. Distractor C tests Python type awareness. |
| Q4 | MCQ (Easy) | C) Backend | Yes | Tests three-layer architecture with a practical Swiggy scenario. Option D (JSON layer) is a creative wrong option that tests whether learners conflate a data format with an architecture layer. |
| Q5 | MCQ (Moderate) | C) PATCH /members/42 | Yes | Tests REST design + correct HTTP method for partial update. Option B (PUT) is a strong distractor testing PATCH vs PUT distinction. Option A tests action-in-URL anti-pattern awareness. |
| Q6 | MCQ (Moderate) | C) Headers (authentication token) | Yes | Tests understanding of token-based auth and request structure. Practical portal login scenario. Distractors test common misconceptions about credential storage. |
| Q7 | MSQ (Moderate) | A, C, D | Yes | Tests HTTP status code family knowledge. Option B (401 vs 403 confusion) is the key discriminator — correctly identified in explanation. All correct options validated against session content. |
| Q8 | MSQ (Moderate) | A, B, C | Yes | Tests JSON-to-Python type mapping after json.loads(). Option D tests string+int concatenation TypeError — a practical Python pitfall. All data types from session table are covered. |
| Q9 | MSQ (Hard) | A, C, D, E, F | Yes | Tests full FE→API→BE→DB→JSON→FE flow understanding. Option B (scraping) tests a real misconception. Covers AI agent placement in backend layer implicitly. |
| Q10 | MSQ (Hard) | A, B, D, F | Yes | Tests OpenAI API as standard API call + backend layer placement. Option C (JSON irrelevance) and Option E (full rewrite needed) test two common AI-specific misconceptions covered in session. |

---

## Section 2: Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Mentioned | Dataset / Input Provided | Remarks |
|----|------|------------|-----------------------------------|--------------------------|---------|
| Q1 | Practical Coding — Flight Deal Finder | Medium | Yes (Case C — single .py file, run and verify, submit in code editor/LMS) | Yes — full JSON string with 5 flight records is embedded in the question | Creative applied scenario (TripZen travel startup). Tests json.loads(), list filtering, min() with lambda, dictionary building, and json.dumps(). Expected output (3 available flights, cheapest at ₹3600) is verified correct. |

---

## Section 3: Overall Assignment Quality Ratings

### Objective Assignment

| Criteria | Rating (1–5) | Notes |
|----------|-------------|-------|
| Content Coverage | 5 | Covers all major topics: APIs, 3-layer architecture, REST design, all 5 HTTP methods, request structure (URL/method/headers/body), HTTP status code families (2xx/4xx/5xx), JSON structure, json.loads(), json.dumps(), and LLM-as-API concept. |
| Creativity | 5 | All questions use practical scenario-based framing (food delivery, hotel booking, cricket scores, gym app, travel booking, AI resume screener). No dry theoretical prompts. |
| Structural Adherence | 5 | Exactly 10 questions: 6 MCQs (4 Easy + 2 Moderate) + 4 MSQs (2 Moderate + 2 Hard). Ordered Easy → Moderate → Hard. All questions have answer explanations including reasoning for wrong options. |
| No Logical Mistakes | True | All correct answers verified against session content. Distractor options are plausible but definitively incorrect. Q7 Option B (401 vs 403) explicitly explained in answer. |
| No Presentation Mistakes | True | Consistent formatting, no spelling errors, all tables and code blocks properly formatted. |

### Subjective Assignment

| Criteria | Rating (1–5) | Notes |
|----------|-------------|-------|
| Content Coverage | 5 | Covers json.loads(), json.dumps(), Python list operations, dictionary construction, and the concept of backend data processing for API responses — all core session topics. |
| Creativity | 5 | Real-world startup context (TripZen), multi-step problem with a realistic business use case. Not a textbook exercise. Intentional discrepancy in expected output encourages careful reading. |
| Structural Adherence | 5 | 1 practical coding task at medium difficulty. Submission instructions follow Case C format. Input data is embedded. Ideal solution + alternative approach provided in explanation. |
| No Logical Mistakes | True | Expected output shows 3 available flights (AI-201, UK-444, 6E-890) and cheapest pick is 6E-890 at ₹3600 — verified against the embedded dataset. Solution code produces the correct result. |
| No Presentation Mistakes | True | Clear step-by-step structure, consistent numbering, code blocks properly formatted, expected output provided. |

---

## QC Summary

All ratings meet the required threshold (5/5). No logical or presentation mistakes detected.
Both assignments are approved and ready for platform upload.
