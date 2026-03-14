# APIs: The Agent’s Hands

## What You’ll Learn

In this lesson, you’ll learn how software systems interact with external services using APIs (Application Programming Interfaces). You’ll understand how to fetch data from the web using Python’s `requests` library, the difference between `GET` and `POST` requests, how to interpret HTTP status codes, and how to read API documentation effectively. These skills are fundamental for AI agents and modern applications, which frequently rely on APIs to retrieve data, trigger actions, and integrate with external tools.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/bdfaebd8-78af-439d-8e4d-1bccd377a812/fKfyMtTMYPRfajbB.png)

---

## 1. Why APIs Matter in Modern AI Systems

Modern software rarely works alone. Instead, systems communicate with many external services such as:

- Language model APIs
- Weather and financial data services
- Search engines
- Payment systems
- Cloud platforms

APIs allow programs to request information or trigger actions from other systems through structured network calls.

In agent-based systems, APIs act like **the agent’s hands**. While the AI model may reason about what to do next, APIs allow the system to actually perform tasks such as retrieving information, posting updates, or triggering workflows.

Understanding how APIs work is therefore essential for building AI agents that interact with the real world.

---

## 2. The Basic Structure of an API Request

An API request typically includes:

- **Endpoint URL** — the address of the service
- **HTTP method** — the type of action (GET, POST, etc.)
- **Headers** — metadata such as authentication
- **Parameters or body** — data sent with the request

Example API request flow:

```

Client (your Python program)
↓
HTTP Request
↓
API Server
↓
JSON Response

````

Most modern APIs return responses in **JSON format**, which can easily be converted into Python dictionaries.

---

## 3. The `requests` Library in Python

Python’s `requests` library is the most widely used tool for making HTTP requests.

Install it if needed:

```bash
pip install requests
````

Import it in Python:

```python
import requests
```

The `requests` library simplifies sending HTTP requests and handling responses.

---

## 4. GET Requests: Retrieving Data

A `GET` request retrieves information from a server without modifying anything.

Example:

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)
```

This sends a request to the GitHub API and prints the response.

---

### Parsing JSON Responses

Most APIs return JSON data. You can convert it into Python objects using `.json()`.

```python
data = response.json()
print(data)
```

Now `data` is a Python dictionary that can be accessed normally.

Example:

```python
print(data["current_user_url"])
```

This step is essential when working with AI APIs or external services.

---

## 5. GET Requests with Parameters

APIs often require query parameters.

Example:

```python
params = {
    "q": "machine learning",
    "limit": 5
}

response = requests.get("https://api.example.com/search", params=params)
```

The request URL becomes:

```
https://api.example.com/search?q=machine+learning&limit=5
```

Using parameters keeps requests structured and readable.

---

## 6. POST Requests: Sending Data

A `POST` request sends data to a server, often to create or process something.

Example:

```python
import requests

data = {
    "name": "Alice",
    "score": 95
}

response = requests.post("https://api.example.com/users", json=data)
print(response.status_code)
```

POST requests commonly appear when:

* Submitting forms
* Creating resources
* Sending prompts to AI APIs
* Triggering workflows

---

## 7. Handling HTTP Status Codes

Every API response includes a status code indicating the result.

Common status codes:

| Code | Meaning          |
| ---- | ---------------- |
| 200  | Success          |
| 201  | Resource created |
| 400  | Bad request      |
| 401  | Unauthorized     |
| 404  | Not found        |
| 500  | Server error     |

Example:

```python
response = requests.get("https://api.example.com/data")

if response.status_code == 200:
    print("Request successful")
else:
    print("Error:", response.status_code)
```

Proper error handling prevents systems from crashing when APIs fail.

---

## 8. Reading API Documentation

Good API documentation explains:

* Available endpoints
* Required parameters
* Authentication methods
* Response structure
* Rate limits

A typical documentation section might include:

Endpoint:

```
GET /users/{id}
```

Example request:

```
GET https://api.example.com/users/123
```

Example response:

```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

From this documentation, a Python request might look like:

```python
response = requests.get("https://api.example.com/users/123")
user = response.json()
print(user["name"])
```

Learning to read documentation efficiently is one of the most important skills for engineers working with APIs.

---

## 9. A Practical Example: Fetching Weather Data

```python
import requests

url = "https://api.example.com/weather"

params = {
    "city": "London"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["temperature"])
else:
    print("Failed to retrieve weather data")
```

This example demonstrates:

* Making a GET request
* Passing parameters
* Checking status codes
* Parsing JSON

This same pattern applies to many AI and data APIs.

---

## 10. Common Beginner Mistakes

* Ignoring status codes
* Assuming responses always contain expected fields
* Sending incorrect parameters
* Misreading API documentation
* Forgetting authentication requirements

Robust API usage requires defensive programming and careful reading of documentation.

---

## Key Takeaways

APIs allow programs to communicate with external services over the web. The `requests` library makes sending HTTP requests simple in Python. `GET` requests retrieve data, while `POST` requests send data. Status codes indicate success or failure, and reading API documentation carefully ensures correct usage. In AI systems, APIs act as the mechanism through which agents interact with the outside world.

**Mental model:**
APIs connect systems.
GET retrieves data.
POST sends data.
Status codes signal outcomes.
Documentation explains the contract.

---

## Additional Reading

* Python Requests Documentation:
  [https://docs.python-requests.org/en/latest/](https://docs.python-requests.org/en/latest/)

* HTTP Status Codes Reference:
  [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

* Google API Design Guide:
  [https://cloud.google.com/apis/design](https://cloud.google.com/apis/design)