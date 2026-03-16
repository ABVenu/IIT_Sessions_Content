## Client-Server Architecture and APIs

Every app on your phone — Zomato, Instagram, GPay — works the same way under the hood. The app on your device (the client) sends a request over the internet to a remote machine (the server), which processes it and sends back a response. The invisible middleman that defines the rules of this conversation is the API.

### Concept Breakdown

1. **Client** — any software that initiates a request. Your browser, a mobile app, a Python script, even another server. The client doesn't store all the data — it asks for what it needs, when it needs it.

2. **Server** — a program (not necessarily a physical box) that listens for incoming requests, processes them, and returns responses. One server handles requests from thousands of clients at the same time.

3. **API (Application Programming Interface)** — the contract between client and server. It specifies:
   - What endpoints (URLs) are available
   - What data the client must send
   - What data the server will return
   - The API is the menu, not the kitchen.

4. **Request-Response cycle** — the fundamental pattern. Client sends a request → server processes → server returns a response. Every web interaction follows this pattern.

### Real-Life Analogy

A restaurant: you (client) want food but can't enter the kitchen (server). You use the waiter (API) — you pick from a menu (endpoint), the kitchen prepares it, and the waiter brings it back. You don't know how the kitchen works. The kitchen doesn't know your name. The waiter is the defined interface between you.

![Diagram comparing a customer, waiter, and kitchen to client, API, and server, illustrating the request-response flow.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/images/LO-5.1.1--Explain-the-client-server-architect_Lecture-Notes_feea9923.png)


## Use the requests Library

Making HTTP requests to interact with web APIs

---

<div align="center">

![Python requests Library GET POST Response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.18.png)

*HTTP operations follow the Input-Process-Output pattern: send a request, server processes it, receive a response*

</div>

---

## Introduction

The `requests` library implements **HTTP client functionality** - talking to web servers using the internet's protocol! HTTP is how browsers fetch web pages, but `requests` lets Python programs interact with **web APIs** programmatically. This is **HTTP for humans** - the tagline emphasizes simplicity!

### Why requests is Revolutionary

**Before requests** (urllib): Complex, verbose, frustrating:
```python
# urllib - painful!
import urllib.request
req = urllib.request.Request('http://api.com/data')
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
# So much boilerplate!
```

**With requests**: Simple, elegant, Pythonic:
```python
# requests - beautiful!
import requests
response = requests.get('http://api.com/data')
data = response.json()
# Two lines!
```
### Code Example

```python
import requests

# Client: this script | Server: api.github.com | API: GitHub's REST API
response = requests.get("https://api.github.com/users/torvalds")

print(response.status_code)       # 200 = success
print(response.json()["name"])    # Linus Torvalds
```

**What's happening:**
1. `requests.get(...)` sends an HTTP GET request — your script is the client
2. GitHub's server receives the request, looks up "torvalds" in its database
3. The server packages the data as JSON and sends it back with status 200
4. `response.json()` parses the JSON response into a Python dictionary

![Diagram illustrating a Python script sending an HTTP GET request to a GitHub server, which processes data and returns a JSON response to the script for parsing.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/images/LO-5.1.1--Explain-the-client-server-architect_Lecture-Notes_e6816e89.png)


### Gotchas to Remember

- An API is the **interface**, not the server. "I built an API" means "I defined the endpoints and contracts," not "I set up a machine."
- Servers can be clients too — in microservices, Service A calls Service B's API. A is the client in that interaction.
- Not all APIs are web APIs. Library functions, OS calls, and database drivers all expose APIs.

### Key Takeaways

- Client-server architecture separates the requester (client) from the provider (server)
- An API defines the contract — what you can ask for and what you'll get back
- Every web and mobile app relies on this model; backend development means building the server side


---

**This is API ergonomics** - making common tasks trivially easy!

### Historical Context

**requests created by Kenneth Reitz** (2011) to simplify HTTP in Python. Became **most downloaded Python package** - over 1 billion downloads! Motto: "**HTTP for Humans**" - emphasizing usability.

**Why needed?** Python's built-in `urllib` is powerful but complex. `requests` provides **beautiful API** - simple methods, automatic JSON handling, session management. **Developer happiness matters!**

**REST APIs**: `requests` designed for **RESTful** APIs (Roy Fielding, 2000). REST uses HTTP methods (GET/POST/PUT/DELETE) to manipulate resources. JSON became standard format - `requests` handles it natively!

### Real-World Analogies

**HTTP like postal service**:
- **GET**: Request information ("send me catalog")
- **POST**: Send new data ("here's my order")
- **PUT**: Update existing ("change my address")
- **DELETE**: Remove data ("cancel subscription")

**requests is your postal worker!**

**Or like restaurant ordering**:
```python
# GET menu
menu = requests.get('https://restaurant.api/menu')

# POST order
order = {'item': 'pizza', 'size': 'large'}
receipt = requests.post('https://restaurant.api/orders', json=order)

# Check order status
status = requests.get(f'https://restaurant.api/orders/{receipt.json()["id"]}')
```

**Or like library requests**:
- **GET**: Borrow book (retrieve data)
- **POST**: Suggest new book (create data)
- **PUT**: Update book review (modify data)
- **DELETE**: Remove hold (delete data)

**Web APIs work like library systems!**

---

### Key Concepts

The requests library allows you to:
- Make HTTP requests (GET, POST, PUT, DELETE)
- Interact with RESTful APIs
- Send and receive JSON data
- Handle authentication
- Download files from the web

### Core Principles

**HTTP methods**: GET (retrieve), POST (create), PUT (update), DELETE (remove)
**Key functions**: `requests.get()`, `requests.post()`, `response.json()`, `response.status_code`

### Installation

```bash
pip install requests
```

### Syntax and Usage

```python
import requests

# GET request
response = requests.get('https://api.example.com/data')
print(response.status_code)  # 200
data = response.json()       # Parse JSON response

# POST request
payload = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=payload)

# With parameters
params = {'search': 'python', 'limit': 10}
response = requests.get('https://api.example.com/search', params=params)
```

### Practical Examples

#### Example 1: Basic GET Request

```python
import requests

# Make GET request
response = requests.get('https://api.github.com')

# Check response
print(f"Status code: {response.status_code}")  # 200 = success
print(f"Content type: {response.headers['content-type']}")

# Get JSON data
data = response.json()
print(f"\nAPI endpoints available:")
for key, url in list(data.items())[:5]:
    print(f"  {key}: {url}")

# Output:
# Status code: 200
# Content type: application/json; charset=utf-8
#
# API endpoints available:
#   current_user_url: https://api.github.com/user
#   current_user_authorizations_html_url: https://github.com/settings/connections/applications{/client_id}
#   ...
```

#### Example 2: GET with Parameters

```python
import requests

# Search GitHub repositories
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 5
}

response = requests.get(
    'https://api.github.com/search/repositories',
    params=params
)

if response.status_code == 200:
    data = response.json()
    print(f"Total repositories found: {data['total_count']:,}\n")

    print("Top 5 Python repositories:")
    for repo in data['items']:
        print(f"  ⭐ {repo['stargazers_count']:,} - {repo['full_name']}")
        print(f"     {repo['description'][:80]}...")
        print()

# Output:
# Total repositories found: 5,234,567
#
# Top 5 Python repositories:
#   ⭐ 180,234 - vinta/awesome-python
#      A curated list of awesome Python frameworks, libraries, software and res...
#   ...
```

#### Example 3: POST Request

```python
import requests

# API endpoint for testing POST requests
url = 'https://httpbin.org/post'

# Data to send
user_data = {
    'username': 'alice',
    'email': 'alice@example.com',
    'age': 28,
    'active': True
}

# Send POST request with JSON data
response = requests.post(url, json=user_data)

print(f"Status: {response.status_code}")

# The server echoes back what we sent
result = response.json()
print(f"\nSent data:")
print(f"  Username: {result['json']['username']}")
print(f"  Email: {result['json']['email']}")
print(f"  Age: {result['json']['age']}")

# Output:
# Status: 200
#
# Sent data:
#   Username: alice
#   Email: alice@example.com
#   Age: 28
```

#### Example 4: Using an API Client

```python
# Usage
client = APIClient('https://api.github.com')

# Get user info
user = client.get('users/torvalds')
if user:
    print(f"User: {user['name']}")
    print(f"Followers: {user['followers']:,}")
    print(f"Public repos: {user['public_repos']}")

# Output:
# User: Linus Torvalds
# Followers: 123,456
# Public repos: 15
```

#### Example 5: GitHub API Wrapper

```python
# Usage (without token for public data)
api = GitHubAPI()

# Get user info
user = api.get_user('octocat')
if user:
    print(f"User: {user['name']}")
    print(f"Bio: {user['bio']}")
    print(f"Location: {user['location']}")

# Get repo info
repo = api.get_repo('psf', 'requests')
if repo:
    print(f"\nRepo: {repo['full_name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']:,}")
    print(f"Language: {repo['language']}")

# Check rate limit
limit = api.get_rate_limit()
if limit:
    print(f"\nAPI Rate Limit:")
    print(f"  Limit: {limit['limit']} requests/hour")
    print(f"  Remaining: {limit['remaining']}")

# Output:
# User: The Octocat
# Bio: None
# Location: San Francisco
#
# Repo: psf/requests
# Description: A simple, yet elegant, HTTP library.
# Stars: 51,234
# Language: Python
#
# API Rate Limit:
#   Limit: 60 requests/hour
#   Remaining: 58
```

### Common HTTP Status Codes

```python
# Success codes (2xx)
200  # OK - Request succeeded
201  # Created - Resource created successfully
204  # No Content - Success, no response body

# Client error codes (4xx)
400  # Bad Request - Invalid request
401  # Unauthorized - Authentication required
403  # Forbidden - No permission
404  # Not Found - Resource doesn't exist
429  # Too Many Requests - Rate limit exceeded

# Server error codes (5xx)
500  # Internal Server Error
503  # Service Unavailable
```

### Best Practices

1. **Always handle errors**: Use try/except for network requests
2. **Set timeouts**: Prevent requests from hanging forever
3. **Use sessions**: For multiple requests to same host
4. **Respect rate limits**: Don't spam APIs
5. **Use HTTPS**: For secure communication
6. **Handle status codes**: Check `response.status_code`
7. **Close resources**: Use context managers or sessions

### Common Mistakes

1. **Not checking status codes**: Always verify request succeeded
2. **No timeout**: Requests can hang indefinitely
3. **Hardcoding credentials**: Use environment variables
4. **Not handling exceptions**: Network requests can fail
5. **Making too many requests**: Respect API rate limits

### Session Usage

```python
import requests

# Create session for multiple requests
session = requests.Session()
session.headers.update({'User-Agent': 'MyApp/1.0'})

# All requests use same session
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')

# Close session
session.close()

# Or use context manager
with requests.Session() as session:
    response = session.get('https://api.example.com/data')
    # Session automatically closed
```

### Key Takeaways

1. `requests` is the standard library for HTTP in Python
2. Use `requests.get()` for GET requests
3. Use `requests.post()` for sending data
4. Check `response.status_code` for success (200-299)
5. Use `response.json()` to parse JSON responses
6. Always handle exceptions and timeouts
7. Respect API rate limits and terms of service

---

## API Documentation Reading

Understanding and navigating API documentation to use web services effectively

---

### Introduction

API documentation is the **blueprint for any web service** - it tells you exactly what endpoints exist, what data to send, and what to expect back. Before writing a single line of `requests` code, reading the docs is step zero!

### Why API Docs Matter

**Without docs**: Guessing endpoints, wrong parameters, wasted requests:
```python
# Guessing - painful!
response = requests.get('https://api.github.com/user/repos')   # Wrong!
response = requests.get('https://api.github.com/repos')         # Wrong!
```

**With docs**: Precise, correct requests first try:
```python
# From docs - correct!
# GET /users/{username}/repos
response = requests.get('https://api.github.com/users/octocat/repos')
```

**Docs are the map - requests is the vehicle!**

### Real-World Analogy

**API docs like a restaurant menu**:
- **Menu** = API documentation
- **Dishes** = endpoints
- **Ingredients** = parameters
- **Allergen info** = authentication requirements
- **"How it's served"** = response format

You wouldn't order without reading the menu - don't call APIs without reading the docs!

### Key Concepts

API documentation tells you:
- What **endpoints** are available (URLs to call)
- Which **HTTP method** to use (GET, POST, PUT, DELETE)
- What **parameters** to send (required vs optional)
- What the **response** looks like (JSON structure)
- How **authentication** works (API keys, tokens)

### Core Principles

**Anatomy of an endpoint doc entry**:
```
Method:   GET
URL:      /users/{id}
Params:   id (required, path), fields (optional, query)
Auth:     Bearer token required
Response: { "id": 1, "name": "Alice", "email": "..." }
```

**Parameter types**: path `{id}` (in URL), query `?page=2` (after `?`), body `{"key": "val"}` (POST/PUT)

### Syntax and Usage

```python
import requests, os

# Translating docs into code:
# "GET /repos/{owner}/{repo}/issues | Params: state, per_page | Auth: optional"

response = requests.get(
    'https://api.github.com/repos/psf/requests/issues',
    params={'state': 'open', 'per_page': 5},
    headers={'Accept': 'application/vnd.github+json'}
)

data = response.json()
```

### Practical Examples

#### Example 1: Translating Docs into Code

```python
import requests

# GitHub Docs says:
# GET /repos/{owner}/{repo}/issues
# Params: state (open/closed/all), per_page, page

response = requests.get(
    'https://api.github.com/repos/psf/requests/issues',
    params={'state': 'open', 'per_page': 5},
    headers={'Accept': 'application/vnd.github+json'}
)

if response.status_code == 200:
    for issue in response.json():
        print(f"#{issue['number']}: {issue['title']}")

# Output:
# #6789: Add support for HTTP/2
# #6780: Timeout not working as expected
```

#### Example 2: Reading Authentication Docs

```python
import requests, os

API_KEY = os.environ.get('MY_API_KEY')  # Never hardcode credentials!

# Docs say: "Pass Bearer token in Authorization header"
response = requests.get(
    'https://api.example.com/data',
    headers={'Authorization': f'Bearer {API_KEY}'}
)

# Docs say: "Pass api_key as a query parameter"
response = requests.get(
    'https://api.example.com/data',
    params={'api_key': API_KEY}
)

print(f"Status: {response.status_code}")  # 200 = auth worked!

# Output:
# Status: 200
```

### Best Practices

1. **Read authentication first**: Set up auth before testing any endpoint
2. **Use provided examples**: Copy-paste, then modify to your needs
3. **Check required vs optional**: Missing required params = 400 error
4. **Note the response structure**: Use exact field names from the docs
5. **Check rate limits**: Know your quota before building

### Common Mistakes

1. **Skipping auth docs**: Wrong/missing auth causes instant 401 errors
2. **Ignoring pagination**: List endpoints return pages, not all records at once
3. **Wrong HTTP method**: Using GET instead of POST returns 405 errors
4. **Using outdated endpoints**: Always verify the API version (`/v1/` vs `/v2/`)

### Key Takeaways

1. Always read authentication docs before writing any code
2. Identify path params `{id}`, query params `?key=val`, and body params
3. Match the HTTP method exactly as documented (GET vs POST matters!)
4. Use exact JSON field names from the response examples in docs
5. Good API docs always include working examples - start there and adapt

---

