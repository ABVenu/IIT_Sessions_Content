# API Security & Ethics

## What You’ll Learn

In this lesson, you’ll learn how to use APIs responsibly and securely. You’ll understand why API Terms of Service (ToS) matter, how rate limiting protects services from abuse, how to store API keys safely using environment variables, and why data privacy must be considered when interacting with external systems. As AI systems increasingly rely on APIs, engineers must ensure that integrations are not only functional but also ethical and secure.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/f2fd3258-ae97-4308-941b-a8045b2b3964/PdedBidOmGeoaBiD.png)

---

## 1. Why Security and Ethics Matter for APIs

APIs allow software to access external services such as language models, financial data, or cloud infrastructure. These services often provide powerful capabilities, but they also impose responsibilities on developers.

When interacting with APIs, engineers must consider:

- **Security** — protecting credentials and preventing unauthorized access  
- **Reliability** — avoiding excessive requests that overload services  
- **Compliance** — respecting the provider’s terms of service  
- **Privacy** — ensuring sensitive user data is not exposed  

Ignoring these considerations can lead to:
- revoked API access
- financial costs
- security breaches
- legal consequences

Responsible API usage is therefore a fundamental part of professional software engineering.

---

## 2. API Terms of Service (ToS)

### What Is an API Terms of Service Agreement?

Most APIs are governed by a **Terms of Service (ToS)** document. This agreement defines how developers are allowed to use the API.

Typical ToS rules may include:

- restrictions on data usage
- limitations on storing responses
- requirements for attribution
- restrictions on redistributing data
- limits on automated usage

For example, an API might allow developers to query data but prohibit storing that data permanently.

---

### Why Developers Must Read ToS

Ignoring API terms can lead to service suspension or legal issues.

Professional developers should always check:

- allowed use cases
- commercial usage restrictions
- rate limits
- data retention policies

When building AI systems that rely on external data, understanding these constraints is essential for long-term reliability.

---

## 3. Rate Limiting

### What Is Rate Limiting?

Rate limiting restricts how many requests a client can make within a given time period.

Example limits:

- 100 requests per minute
- 1,000 requests per day
- 10 requests per second

These limits protect APIs from abuse and ensure fair access for all users.

---

### Handling Rate Limits

If a client exceeds the allowed request rate, the API typically returns a **429 Too Many Requests** status code.

Example handling in Python:

```python
import requests

response = requests.get("https://api.example.com/data")

if response.status_code == 429:
    print("Rate limit exceeded. Please wait and retry.")
````

Developers often implement strategies such as:

* request throttling
* retry logic with delays
* caching previous responses

These approaches prevent unnecessary API calls and maintain system stability.

---

## 4. Environment Variables for API Keys

### Why API Keys Must Be Protected

Many APIs require authentication using an **API key**. This key identifies the client and often controls billing and access permissions.

Example:

```python
api_key = "123456789abcdef"
```

Hardcoding keys directly into source code is dangerous because:

* the key may be exposed in public repositories
* unauthorized users could misuse the API
* billing charges may accumulate unexpectedly

---

### Using Environment Variables

Environment variables allow credentials to be stored outside the codebase.

Example in Python:

```python
import os

api_key = os.getenv("API_KEY")
```

Setting the environment variable:

**Linux / macOS**

```bash
export API_KEY="your_secret_key"
```

**Windows**

```powershell
setx API_KEY "your_secret_key"
```

This approach ensures credentials remain separate from application code.

---

### Using `.env` Files

Another common method uses a `.env` file with the `python-dotenv` package.

Example `.env` file:

```
API_KEY=your_secret_key
```

Python usage:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

This approach is widely used in development environments.

---

## 5. Data Privacy Basics

### Why Privacy Matters

When applications interact with APIs, they may process sensitive information such as:

* personal user data
* financial transactions
* location data
* medical information

Protecting this data is both an ethical and legal responsibility.

---

### Principles of Responsible Data Use

Responsible systems follow several core principles:

**Data Minimization**

Only collect or transmit the data that is necessary.

**User Consent**

Users should understand how their data is used.

**Secure Storage**

Sensitive data should be encrypted or protected appropriately.

**Transparency**

Systems should document what data is processed and why.

---

### Example: Safe API Request

Instead of sending unnecessary personal information:

```python
payload = {
    "query": "weather forecast"
}
```

Avoid sending unrelated personal data.

Responsible design reduces risk and builds trust.

---

## 6. Ethical Considerations in AI Systems

When APIs are integrated into AI systems, additional ethical questions arise.

Developers must consider:

* whether external data sources are trustworthy
* whether the API usage aligns with user expectations
* whether automated decisions may affect individuals unfairly

Responsible AI development includes careful evaluation of the tools and services used.

---

## 7. A Secure API Workflow Example

```python
import os
import requests

api_key = os.getenv("API_KEY")

url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
elif response.status_code == 429:
    print("Rate limit reached. Try again later.")
else:
    print("Request failed:", response.status_code)
```

This example demonstrates:

* secure key usage
* authenticated requests
* status code handling

These practices are essential for building reliable API integrations.

---

## Key Takeaways

API usage must balance functionality with responsibility. Developers must follow API Terms of Service, respect rate limits, protect credentials using environment variables, and handle user data responsibly. Security and ethical considerations are fundamental to building trustworthy AI systems that interact with external services.

**Mental model:**
Respect the service.
Protect credentials.
Limit requests.
Protect user data.

---

## Additional Reading

* Google API Security Best Practices:
  [https://cloud.google.com/docs/security/best-practices](https://cloud.google.com/docs/security/best-practices)

* OWASP API Security Guide:
  [https://owasp.org/www-project-api-security/](https://owasp.org/www-project-api-security/)

* Python `os` Module (Environment Variables):
  [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

* Responsible AI and Data Governance (Google AI):
  [https://ai.google/responsibility/](https://ai.google/responsibility/)