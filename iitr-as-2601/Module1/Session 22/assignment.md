# **Assignment: APIs The Agent’s Hands**

---

## **Question 1. (MCQ)**

What does API stand for?

A) Automated Programming Interface
B) Application Programming Interface
C) Application Processing Integration
D) Automated Process Integration

**Correct answer:** B

**Explanation:**
API stands for **Application Programming Interface**. It defines how software systems communicate with each other by sending structured requests and receiving responses.

---

## **Question 2. (MCQ)**

What is the primary purpose of an API in modern software systems?

A) Store data locally
B) Enable communication between software systems
C) Replace programming languages
D) Compile Python code

**Correct answer:** B

**Explanation:**
APIs allow programs to communicate with external services. Through APIs, applications can retrieve information, trigger actions, or integrate with other systems such as cloud platforms or AI services.

---

## **Question 3. (MCQ)**

Which Python library is commonly used to make HTTP requests to APIs?

A) `numpy`
B) `requests`
C) `pandas`
D) `matplotlib`

**Correct answer:** B

**Explanation:**
The `requests` library simplifies sending HTTP requests such as `GET` and `POST` from Python. It is widely used for interacting with APIs.

---

## **Question 4. (MCQ)**

What does a `GET` request typically do?

A) Deletes data from a server
B) Retrieves data from a server
C) Updates existing data
D) Creates a database table

**Correct answer:** B

**Explanation:**
A `GET` request retrieves information from a server without modifying anything. It is the most common type of request used when fetching data from APIs.

---

## **Question 5. (MCQ)**

What does the `.json()` method do when applied to an API response?

A) Converts JSON data into a Python dictionary
B) Saves data to a JSON file
C) Sends JSON data to the server
D) Removes JSON formatting

**Correct answer:** A

**Explanation:**
`.json()` converts the JSON response from the API into a Python dictionary so the data can be accessed using standard Python syntax.

---

## **Question 6. (MCQ)**

What is the purpose of query parameters in an API request?

A) Authenticate users automatically
B) Provide additional information to the API request
C) Encrypt the request
D) Stop the request from executing

**Correct answer:** B

**Explanation:**
Query parameters provide additional information to the API, such as search queries or limits. They help specify exactly what data should be retrieved.

---

## **Question 7. (MCQ)**

Which HTTP method is typically used to send data to a server?

A) GET
B) POST
C) FETCH
D) READ

**Correct answer:** B

**Explanation:**
`POST` requests send data to a server, commonly used for creating resources, submitting forms, or sending prompts to AI APIs.

---

## **Question 8. (MCQ)**

What does the HTTP status code **200** indicate?

A) Unauthorized request
B) Resource not found
C) Successful request
D) Server error

**Correct answer:** C

**Explanation:**
Status code **200** indicates that the request was successfully processed by the server and a valid response was returned.

---

## **Question 9. (Subjective)**

### **API Data Retrieval Script**

Write a Python program that demonstrates how to interact with an API using the `requests` library.

### **Tasks**

1. Send a **GET request** to the GitHub API endpoint:

```
https://api.github.com
```

2. Print the **HTTP status code** of the response.

3. Convert the response into a Python dictionary using `.json()`.

4. Print the value of the key:

```
current_user_url
```

5. Implement simple error handling:

   * If the status code is **200**, print `"Request successful"`.
   * Otherwise, print `"Request failed"` along with the status code.

---

## Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** named:

```
api-requests-assignment
```

3. Write the Python program in a file named:

```
api_request_example.py
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
import requests

# API endpoint
url = "https://api.github.com"

# Send GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Check if request was successful
if response.status_code == 200:
    print("Request successful")

    # Convert response to Python dictionary
    data = response.json()

    # Access a field from the JSON response
    print("Current User URL:", data["current_user_url"])
else:
    print("Request failed:", response.status_code)
```