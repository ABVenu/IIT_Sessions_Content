# Subjective Assignment — Working with APIs and JSON

**Total Questions:** 1 | **Practical Coding Task** | **Difficulty: Medium**

---

## Q1. Build a Flight Deal Finder Utility

You are a backend developer at a travel startup called **TripZen**. Your team is building a smart travel assistant, and your first task is to write the data processing utility that handles raw JSON responses from a flight search API.

The flight search API returns a JSON string containing a list of available flights. Your utility must process this data, filter out unavailable options, identify the best deal, and prepare a structured booking summary — ready to be sent back to the frontend as a JSON response.

### Your Task

Write a Python program (`flight_deal_finder.py`) that does the following:

**Step 1 — Parse the API Response**
Parse the following JSON string (simulating a raw API response) into a Python dictionary using `json.loads()`:

```json
{
  "route": "Delhi → Mumbai",
  "search_date": "2026-06-10",
  "flights": [
    {"flight_id": "AI-201", "airline": "Air India", "departure": "06:00", "price": 4500, "seats_available": 3},
    {"flight_id": "6E-305", "airline": "IndiGo", "departure": "09:30", "price": 3800, "seats_available": 1},
    {"flight_id": "SG-112", "airline": "SpiceJet", "departure": "13:15", "price": 3200, "seats_available": 0},
    {"flight_id": "UK-444", "airline": "Vistara", "departure": "17:45", "price": 5100, "seats_available": 5},
    {"flight_id": "6E-890", "airline": "IndiGo", "departure": "21:00", "price": 3600, "seats_available": 2}
  ]
}
```

**Step 2 — Filter Unavailable Flights**
From the list of flights, filter out any flight that has **fewer than 2 seats available** (i.e., keep only flights where `seats_available >= 2`).

Print the number of available flights after filtering.

**Step 3 — Find the Best Deal**
Among the filtered (available) flights, find the one with the **lowest price**.

Print the airline name, flight ID, and price of the cheapest available flight.

**Step 4 — Build a Booking Summary**
Create a new Python dictionary called `booking_summary` with the following fields:
- `"route"` — copied from the original data
- `"selected_flight_id"` — the flight ID of the cheapest available flight
- `"airline"` — the airline name
- `"departure"` — the departure time
- `"price"` — the ticket price
- `"status"` — set this to `"ready_to_book"`

**Step 5 — Convert to JSON and Print**
Convert `booking_summary` into a formatted JSON string using `json.dumps()` with `indent=2` and print it.

### Expected Output (approximate)

```
Available flights after filtering: 3
Best deal: IndiGo (6E-890) at ₹3600

Booking Summary (JSON):
{
  "route": "Delhi → Mumbai",
  "selected_flight_id": "6E-890",
  "airline": "IndiGo",
  "departure": "21:00",
  "price": 3600,
  "status": "ready_to_book"
}
```

---

### Submission Instructions

- Code all the steps mentioned above in VS Code in a single file called `flight_deal_finder.py`
- Run the code and verify the output matches the expected result
- Then submit the code in the code editor / answer box in the LMS

---

### Answer Explanation

**Ideal Solution:**

```python
import json

# Step 1: Parse the JSON string into a Python dictionary
json_response = '''
{
  "route": "Delhi → Mumbai",
  "search_date": "2026-06-10",
  "flights": [
    {"flight_id": "AI-201", "airline": "Air India", "departure": "06:00", "price": 4500, "seats_available": 3},
    {"flight_id": "6E-305", "airline": "IndiGo", "departure": "09:30", "price": 3800, "seats_available": 1},
    {"flight_id": "SG-112", "airline": "SpiceJet", "departure": "13:15", "price": 3200, "seats_available": 0},
    {"flight_id": "UK-444", "airline": "Vistara", "departure": "17:45", "price": 5100, "seats_available": 5},
    {"flight_id": "6E-890", "airline": "IndiGo", "departure": "21:00", "price": 3600, "seats_available": 2}
  ]
}
'''

data = json.loads(json_response)

# Step 2: Filter flights with seats_available >= 2
available_flights = [f for f in data["flights"] if f["seats_available"] >= 2]
print(f"Available flights after filtering: {len(available_flights)}")

# Step 3: Find the cheapest available flight
cheapest = min(available_flights, key=lambda f: f["price"])
print(f"Best deal: {cheapest['airline']} ({cheapest['flight_id']}) at ₹{cheapest['price']}")

# Step 4: Build a booking summary dictionary
booking_summary = {
    "route": data["route"],
    "selected_flight_id": cheapest["flight_id"],
    "airline": cheapest["airline"],
    "departure": cheapest["departure"],
    "price": cheapest["price"],
    "status": "ready_to_book"
}

# Step 5: Convert to formatted JSON string and print
json_output = json.dumps(booking_summary, indent=2)
print("\nBooking Summary (JSON):")
print(json_output)
```

**Step-by-step walkthrough:**
- `json.loads()` converts the raw API response string into a nested Python dictionary. The `"flights"` key holds a Python list of dictionaries.
- The list comprehension `[f for f in data["flights"] if f["seats_available"] >= 2]` filters out IndiGo 6E-305 (1 seat) and SpiceJet SG-112 (0 seats), leaving **3 available flights**: AI-201 (3 seats ✓), UK-444 (5 seats ✓), and 6E-890 (2 seats ✓). The cheapest among these is **6E-890 at ₹3600**.

- `min(available_flights, key=lambda f: f["price"])` uses Python's built-in `min()` with a key function to find the flight dictionary with the lowest price — no manual loop required.
- Building `booking_summary` as a dictionary picks specific fields and adds a `"status"` field that was not in the original data — a common real-world pattern when transforming API data.
- `json.dumps(booking_summary, indent=2)` converts the dictionary back to a JSON string with 2-space indentation for readability — exactly what a backend would send in its API response to the frontend.

**Alternative approach:** Instead of `min()` with a lambda, learners could also sort the list with `sorted(available_flights, key=lambda f: f["price"])` and pick index `[0]`. Both are valid.
