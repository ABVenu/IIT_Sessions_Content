## Assignment 2: Subjective Type Questions

### Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** (name it as per your convenience, e.g., `python-json-assignment`).

3. Write **separate Python files** for each question inside this folder.

4. For each program:

   * Run the code in the **terminal**
   * Verify the **output**

5. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

6. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repo).

---

### **Question: JSON-Based API Response Processor**

**Task:**
Build a Python program that simulates processing a real-world API response using JSON.

Your program must:

1. Store a **JSON-formatted string** representing an API response.
2. Parse the JSON string into Python objects using `json.loads()`.
3. Extract and print:

   * Request ID
   * Status
   * Text result
   * Confidence score
4. If the confidence score is below `0.9`, print a warning message.
5. Convert a new Python dictionary representing a follow-up result into JSON using `json.dumps()`.
6. Write this JSON output to a file named `response.json`.

**Example API Response (input):**

```json
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
```

**Requirements:**

* Use Python’s built-in `json` module
* Handle nested JSON correctly
* Do not hardcode extracted values
* Use clear variable names
* Demonstrate both parsing and generation of JSON

**Sample Output (example):**

```
Request ID: req_123
Status: success
Text: Hello world
Confidence: 0.98
```