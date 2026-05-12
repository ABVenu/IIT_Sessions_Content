# Objective Assignment — Working with APIs and JSON

**Total Questions:** 10 | **6 MCQs + 4 MSQs**
**Order:** Easy → Moderate → Hard

---

## MCQ — Easy (Single Correct)

### Q1. (Easy | MCQ)

Priya is building a food delivery app. When a user taps "My Orders", the app needs to fetch the user's past order history from the server — without modifying any data. Which HTTP method should the frontend use for this request?

**Options:**

- A) POST
- B) DELETE
- C) GET
- D) PATCH

**Correct Answer:** C) GET

**Answer Explanation:**
`GET` is the HTTP method used exclusively to *read or retrieve* data without causing any changes on the server. Here, the app is simply fetching existing order data — no creation, modification, or deletion is involved.

- A) POST — incorrect; POST is used to *create* a new resource (e.g., placing a new order).
- B) DELETE — incorrect; DELETE is used to *remove* a resource permanently.
- D) PATCH — incorrect; PATCH is used to *partially update* an existing resource.

---

### Q2. (Easy | MCQ)

Arjun is testing his e-commerce app and searches for a product using the URL `https://shop.com/product/99999`. The server returns a response with status code **404**. What does this mean?

**Options:**

- A) Arjun's request was processed successfully and the product was found
- B) Arjun is not logged in, so the server rejected his request
- C) The server crashed while trying to find the product
- D) The product with ID 99999 does not exist on the server

**Correct Answer:** D) The product with ID 99999 does not exist on the server

**Answer Explanation:**
**404 Not Found** means the URL or the resource being requested simply does not exist on the server. The client made a valid request, but there is nothing at that location.

- A) Incorrect — a successful response would be **200 OK**.
- B) Incorrect — not being logged in returns **401 Unauthorized**.
- C) Incorrect — a server-side crash returns **500 Internal Server Error**.

---

### Q3. (Easy | MCQ)

Meera's Python script calls a weather API and receives this response: `'{"city": "Delhi", "temp": 38, "condition": "Sunny"}'`. She tries to run `print(response["city"])` immediately but gets a `TypeError`. What is the most likely reason, and how should she fix it?

**Options:**

- A) The JSON module is not imported; she should add `import json` and call `json.dumps(response)`
- B) The response is a plain text string, not a dictionary; she should first call `json.loads(response)` to parse it
- C) She should use `response.city` instead of `response["city"]` to access string fields
- D) The `temp` field is an integer, which causes JSON to reject the data

**Correct Answer:** B) The response is a plain text string, not a dictionary; she should first call `json.loads(response)` to parse it

**Answer Explanation:**
API responses arrive as **text strings** over the network — even if they look like dictionaries. You cannot index into a string using `["city"]`. `json.loads()` (Load String) converts the JSON string into an actual Python dictionary, after which `response["city"]` works perfectly.

- A) Incorrect — `json.dumps()` converts a Python dict *to* a JSON string (the opposite direction).
- C) Incorrect — Python dictionaries use `[]` notation, not dot notation.
- D) Incorrect — JSON fully supports integer values; that is not the cause of the error.

---

### Q4. (Easy | MCQ)

When Riya places an order on Swiggy, the system checks her login session, applies discount codes, calculates delivery time, and fetches restaurant data — all before confirming the order. Which layer of the three-tier application architecture is responsible for this processing?

**Options:**

- A) Frontend — it is the layer closest to the user
- B) Database — it stores all order and discount data
- C) Backend — it is the brain that processes requests and enforces business logic
- D) JSON layer — it converts all the data into readable format

**Correct Answer:** C) Backend — it is the brain that processes requests and enforces business logic

**Answer Explanation:**
The **Backend** is the processing layer — it receives requests from the frontend, runs all business logic (validation, discounts, delivery time calculation), fetches data from the database, and prepares the response. It is the "kitchen" of the application.

- A) Incorrect — the Frontend only displays data and captures user input; it does not process logic.
- B) Incorrect — the Database only stores and retrieves data; it does not apply business rules.
- D) Incorrect — JSON is a data format, not an architectural layer.

---

## MCQ — Moderate (Single Correct)

### Q5. (Moderate | MCQ)

Rahul is building a REST API for a gym management app. A member wants to update *only their mobile number* in their profile — without changing their name, address, or membership plan. Which of the following API calls correctly follows REST conventions for this operation?

**Options:**

- A) `POST /update-phone` with `{"phone": "9876543210"}` in the body
- B) `PUT /members/42` with `{"phone": "9876543210"}` in the body
- C) `PATCH /members/42` with `{"phone": "9876543210"}` in the body
- D) `GET /members/42?phone=9876543210`

**Correct Answer:** C) `PATCH /members/42` with `{"phone": "9876543210"}` in the body

**Answer Explanation:**
**PATCH** is the HTTP method for *partial updates* — it only modifies the fields you include in the request body, leaving all other fields untouched. REST also requires the URL to be resource-based (`/members/42`), not action-based.

- A) Incorrect — `POST /update-phone` is not REST style (action in URL), and POST is for *creating* new resources.
- B) Incorrect — `PUT` performs a *full replacement* of the entire resource. Sending only the phone number would erase all other fields.
- D) Incorrect — `GET` is for reading data; query parameters are not used to send update data. Also, GET requests should not modify server state.

---

### Q6. (Moderate | MCQ)

Sana logs into her company's HR portal in the morning. Later in the day, she accesses her payslip page. The browser sends a new request to the server — but she is not prompted to log in again. The server still knows who she is. Which component of the API request carries her identity on this second request?

**Options:**

- A) Request Body — it stores her credentials so she never has to re-enter them
- B) URL / Endpoint — her username is embedded in the URL path
- C) Headers — an authentication token issued at login is automatically attached to every request
- D) HTTP Method — using GET instead of POST signals that the user is already authenticated

**Correct Answer:** C) Headers — an authentication token issued at login is automatically attached to every request

**Answer Explanation:**
When Sana logged in, the server issued an **authentication token** (a digital ID card). Her browser stores this token and automatically attaches it in the **request headers** with every subsequent request. The server reads the token to identify her without asking for credentials again.

- A) Incorrect — storing credentials in the request body for every call is a security anti-pattern; that is not how modern authentication works.
- B) Incorrect — embedding usernames in URLs is insecure and not standard practice for authentication.
- D) Incorrect — the HTTP method indicates the type of action (read/create/update/delete), not the user's identity.

---

## MSQ — Moderate (Multiple Correct)

### Q7. (Moderate | MSQ)

Divya is testing her hotel booking API. During testing, she encounters various HTTP responses. **Which of the following status code and description pairs are correctly matched?** *(Select all that apply)*

- A) **201** — A new hotel booking was successfully created after the user submitted their details
- B) **401** — The user tried to access the admin dashboard, but they only have a guest account (no admin rights)
- C) **400** — The user's booking request was missing the check-in date, which is a required field
- D) **500** — The hotel's database server crashed unexpectedly while processing the request

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A — Correct:** `201 Created` is returned when a new resource (here, a booking) is successfully created on the server.
- **B — Incorrect:** Accessing a page without the required *permission* returns `403 Forbidden`. `401 Unauthorized` means the user is not logged in at all or has an invalid token.
- **C — Correct:** `400 Bad Request` is returned when the client sends incomplete or invalid data — like a missing required field.
- **D — Correct:** `500 Internal Server Error` is returned when the fault is on the server side (e.g., database crash), not the client's.

---

### Q8. (Moderate | MSQ)

Karan receives the following JSON string from a cricket scores API:

```
'{"match": "IND vs AUS", "score": 287, "is_completed": false, "top_scorers": ["Rohit", "Virat"]}'
```

After parsing it with `json.loads()`, **which of the following Python operations are valid and produce the described result?** *(Select all that apply)*

- A) `data["score"] + 13` → produces `300`
- B) `data["is_completed"]` → returns Python `False` (a boolean, not a string)
- C) `data["top_scorers"][1]` → returns `"Virat"`
- D) `data["match"] + data["score"]` → returns `"IND vs AUS287"`

**Correct Answers:** A, B, C

**Answer Explanation:**
- **A — Correct:** JSON numbers map to Python `int`/`float`. `287 + 13 = 300` is valid arithmetic.
- **B — Correct:** JSON `false` maps to Python `False` (boolean). `json.loads()` handles this conversion automatically.
- **C — Correct:** JSON arrays map to Python `list`. Index `[1]` accesses the second element, `"Virat"`.
- **D — Incorrect:** You cannot concatenate a `str` and an `int` in Python directly. This would raise a `TypeError`. You would need `str(data["score"])` first.

---

## MSQ — Hard (Multiple Correct)

### Q9. (Hard | MSQ)

Vikram uses a flight booking app to search for flights from Hyderabad to Bangalore on June 5th. Results appear within 2 seconds. **Which of the following statements correctly describe what happened in the background?** *(Select all that apply)*

- A) The frontend sent a request (GET or POST) to the backend with search parameters such as source, destination, and date
- B) The backend directly queried Make My Trip's public website using web scraping to fetch flight data
- C) The backend processed the request, queried the flight database or a third-party flight API, and prepared the results
- D) The backend formatted the results as a **JSON response** and sent it back to the frontend
- E) The frontend received the JSON response and rendered it as a list of flight cards on the screen
- F) A status code of **200 OK** was included in the response, indicating the search was successful

**Correct Answers:** A, C, D, E, F

**Answer Explanation:**
- **A — Correct:** The frontend always communicates with the backend via an API request, passing the user's search parameters in the request.
- **B — Incorrect:** Backends do not scrape websites — they call structured **APIs** provided by services like Make My Trip. Web scraping is unreliable and violates terms of service.
- **C — Correct:** The backend is the processing layer — it receives the request, calls data sources (database or third-party APIs), and prepares the result.
- **D — Correct:** Backend responses to frontends are almost always formatted as **JSON**.
- **E — Correct:** The frontend's job is to receive the JSON response and render it visually for the user.
- **F — Correct:** A successful request-response cycle returns `200 OK` in the status code.

---

### Q10. (Hard | MSQ)

Aisha is building a Python-based AI resume screener. Her system takes a candidate's resume text, sends it to OpenAI's API with a scoring prompt, and returns a score and feedback. **Which of the following statements about her system's API architecture are correct?** *(Select all that apply)*

- A) Calling `client.responses.create(...)` in Python sends a **POST** request to OpenAI's server under the hood, with the prompt in the request body
- B) The `OpenAI()` client uses the `OPENAI_API_KEY` environment variable as an **authentication token** in the request headers — similar to how any other API uses tokens
- C) The response from OpenAI arrives as a plain human-readable sentence, so `json` module functions are irrelevant here
- D) Aisha's AI screener lives in the **backend layer** of her application — the frontend just sends the resume text via an API call to Aisha's backend
- E) If Aisha wants to switch from OpenAI to Gemini, she must completely rewrite her entire application backend from scratch
- F) The overall flow — create client → authenticate → send request → receive JSON response — follows the same pattern as any REST API call

**Correct Answers:** A, B, D, F

**Answer Explanation:**
- **A — Correct:** Internally, the OpenAI Python library sends an authenticated **POST** request to OpenAI's servers with the prompt in the JSON request body. The Python SDK just abstracts this away.
- **B — Correct:** The API key is an authentication token. The OpenAI client attaches it to request headers — exactly like any other API that uses token-based auth.
- **C — Incorrect:** The OpenAI response is structured data (a JSON object with fields like `output_text`, usage stats, etc.). The Python library may deserialize it for you, but JSON is very much involved under the hood.
- **D — Correct:** AI agents and model calls happen in the **backend**. The frontend sends the user input to the backend, which then calls the LLM API.
- **E — Incorrect:** Switching providers requires swapping the client and method calls, but the **overall architecture** (create client → authenticate → call → read response) remains the same. It is not a full rewrite.
- **F — Correct:** LLM APIs follow the same request-response pattern as all other REST APIs: authenticate, send a structured request, receive a structured JSON response.
