# **Assignment: API Security & Ethics**

---

## **Question 1. (MCQ)**

Why is API security important when building software systems?

A) It improves visualization quality
B) It protects credentials, prevents misuse, and ensures responsible API usage
C) It increases internet speed
D) It replaces authentication systems

**Correct answer:** B

**Explanation:**
API security protects sensitive credentials, prevents unauthorized access, and ensures developers follow responsible practices such as respecting service limits and protecting user data.

---

## **Question 2. (MCQ)**

What is the purpose of an API **Terms of Service (ToS)**?

A) To define allowed usage and restrictions for an API
B) To automatically encrypt API responses
C) To increase API speed
D) To replace authentication mechanisms

**Correct answer:** A

**Explanation:**
The Terms of Service specifies how developers are allowed to use an API, including restrictions on data usage, request limits, storage policies, and commercial usage rules.

---

## **Question 3. (MCQ)**

What is **rate limiting**?

A) Encrypting API data
B) Limiting how many requests can be made within a certain time period
C) Reducing network latency
D) Compressing API responses

**Correct answer:** B

**Explanation:**
Rate limiting restricts the number of API requests a client can make during a specific time window. This prevents abuse and ensures fair usage across all users.

---

## **Question 4. (MCQ)**

Which HTTP status code typically indicates that a rate limit has been exceeded?

A) 200
B) 404
C) 429
D) 500

**Correct answer:** C

**Explanation:**
Status code **429 (Too Many Requests)** is returned when a client exceeds the allowed number of requests within a specified time period.

---

## **Question 5. (MCQ)**

Why is hardcoding API keys directly in source code considered dangerous?

A) It slows down the application
B) It increases memory usage
C) The keys may be exposed publicly and misused
D) It prevents API requests from working

**Correct answer:** C

**Explanation:**
Hardcoded keys may be accidentally exposed in repositories or shared code. Unauthorized users could then access the API using those credentials.

---

## **Question 6. (MCQ)**

Which Python module is commonly used to retrieve environment variables?

A) `sys`
B) `os`
C) `json`
D) `math`

**Correct answer:** B

**Explanation:**
The `os` module provides access to environment variables through functions such as `os.getenv()`.

---

## **Question 7. (MCQ)**

What is the main purpose of using environment variables for API keys?

A) Increase request speed
B) Store credentials outside the source code for security
C) Compress API responses
D) Automatically authenticate users

**Correct answer:** B

**Explanation:**
Environment variables allow sensitive credentials such as API keys to remain outside the codebase, preventing accidental exposure.

---

## **Question 8. (MCQ)**

Which principle refers to collecting only the necessary data when interacting with APIs?

A) Data maximization
B) Data replication
C) Data minimization
D) Data duplication

**Correct answer:** C

**Explanation:**
Data minimization ensures that systems only collect or transmit the data required for a specific task, reducing privacy risks.

---

## **Question 9. (Subjective)**

### **Secure API Request Script**

Write a Python script that demonstrates secure and responsible API usage.

### **Tasks**

Your program should:

1. Retrieve an **API key from an environment variable** using the `os` module.
2. Send a **GET request** to the endpoint:

```text
https://api.example.com/data
```

3. Include the API key in the request headers using the **Authorization Bearer format**.
4. Handle the following status codes:

   * **200** → Print the JSON response
   * **429** → Print `"Rate limit reached. Try again later."`
   * Any other status → Print `"Request failed"` and the status code

This exercise demonstrates:

* Secure API key usage
* Authenticated API requests
* Status code handling

---

## Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** named:

```text
api-security-ethics-assignment
```

3. Write the Python program in a file named:

```text
secure_api_request.py
```

4. For the program:

   * Run the code in the **terminal**
   * Verify the **output**

5. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

6. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repo).

---

# ✅ **Solution**

```python
import os
import requests

# Retrieve API key securely from environment variable
api_key = os.getenv("API_KEY")

# API endpoint
url = "https://api.example.com/data"

# Headers with authentication
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Send GET request
response = requests.get(url, headers=headers)

# Handle responses
if response.status_code == 200:
    data = response.json()
    print(data)

elif response.status_code == 429:
    print("Rate limit reached. Try again later.")

else:
    print("Request failed:", response.status_code)
```