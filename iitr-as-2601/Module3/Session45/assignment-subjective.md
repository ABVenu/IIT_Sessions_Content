# Subjective Assignment: ShopEasy Order Lookup Retry Handler

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

**ShopEasy** is an e-commerce platform. During the **Diwali flash sale**, the customer-support backend calls an LLM-powered **order-status service** thousands of times per minute. When traffic spikes, the provider returns **HTTP 429 Too Many Requests** and order lookups fail — customers see a blank screen instead of delivery updates.

You are on the platform engineering team. Before wiring the live Groq client, you must build and test a **retry handler** locally: a script that simulates a flaky order-status API, recovers with **Tenacity** exponential backoff, and writes **visible retry logs** so the team can debug throttling during the sale.

---

## Task

Implement a complete Python script: **`shopeasy_order_retry.py`**

Build the full file from scratch. Your script must meet **all** requirements below.

### Functional requirements

1. **Simulated order lookup function** named `lookup_order_status(order_id: str) -> str`
   - Maintain an **attempt counter** (module-level dict or similar) that tracks how many times the simulated API body has run.
   - On the **first two** calls, raise `Exception("HTTP 429 Too Many Requests")` to mimic provider throttling during peak sale traffic.
   - On the **third** call, return exactly:  
     `Order {order_id} — out for delivery. Expected by 6 PM today.`
   - Wrap this function with Tenacity **`@retry`** using:
     - `stop=stop_after_attempt(4)`
     - `wait=wait_exponential(multiplier=1, min=1, max=10)`
     - `before_sleep=before_sleep_log(logger, logging.WARNING)`

2. **Logging setup**
   - Configure Python `logging` at **INFO** level.
   - Write logs to **`logs/api_retries.log`** (create the `logs/` folder if needed) **and** print to the console.
   - Log format must include timestamp, level, and message (for example: `%(asctime)s | %(levelname)s | %(message)s`).

3. **Main block**
   - When run as `python shopeasy_order_retry.py`, call `lookup_order_status("ORD-7842")`.
   - Print the returned order-status string.
   - Print a summary line: `Total API attempts: <n>` where `<n>` is the final attempt count (expected: **3**).

4. **Constraints**
   - Use only **`tenacity`** and the Python standard library — **no live Groq API calls** and **no API key** required for this exercise.
   - The script must **not crash** on the first fake 429; Tenacity should retry and recover automatically.

---

## Expected behaviour

When you run `python shopeasy_order_retry.py`:

```text
<WARNING log lines about retrying lookup_order_status — at least two, with wait times around 1s and 2s>
Order ORD-7842 — out for delivery. Expected by 6 PM today.
Total API attempts: 3
```

- **`logs/api_retries.log`** must contain the same WARNING retry lines.
- The process exits successfully without an unhandled exception.

---

## Submission Instructions

- Implement all requirements in a single `.py` file named `shopeasy_order_retry.py` in VS Code.
- Run the script and verify the output and log file match the expected behaviour above.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. **`lookup_order_status`** stands in for the ShopEasy support bot's order-status API call during high-traffic sale windows.
2. **`@retry`** catches the simulated **429** exceptions and re-invokes the function after exponential delays instead of failing the customer flow.
3. **`stop_after_attempt(4)`** caps retries at four total tries — enough for two throttles plus success, with one spare attempt.
4. **`wait_exponential(multiplier=1, min=1, max=10)`** produces waits of roughly 1s, then 2s, matching the backoff pattern used in production integrations.
5. **`before_sleep_log`** writes a WARNING before each sleep — the retry audit trail engineers review when Diwali traffic spikes.
6. **`logs/api_retries.log`** persists events so yesterday's sale debugging is possible without re-running traffic.

### Reference Solution

```python
# pip install tenacity
import logging
from pathlib import Path
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "api_retries.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("shopeasy_order_retry")

attempt_counter = {"n": 0}


@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    before_sleep=before_sleep_log(logger, logging.WARNING),
)
def lookup_order_status(order_id: str) -> str:
    attempt_counter["n"] += 1
    if attempt_counter["n"] <= 2:
        raise Exception("HTTP 429 Too Many Requests")
    return f"Order {order_id} — out for delivery. Expected by 6 PM today."


if __name__ == "__main__":
    status = lookup_order_status("ORD-7842")
    print(status)
    print("Total API attempts:", attempt_counter["n"])
```

### Alternative approaches

- Use a custom `RateLimitError` exception class instead of a generic `Exception`.
- Accept `order_id` from `sys.argv` so QA can test multiple order IDs from the terminal.
- Add `retry=retry_if_exception_type(Exception)` to narrow retries to rate-limit errors only.

### Notes for evaluation

- Full credit: script recovers after two fake 429s, prints the exact order-status line for `ORD-7842`, shows `Total API attempts: 3`, and writes retry WARNING lines to both console and `logs/api_retries.log`.
- Partial credit: backoff works but log file missing or `before_sleep_log` not wired — note which requirement failed.
- No Groq API key required; live API integration is out of scope for this assignment.
