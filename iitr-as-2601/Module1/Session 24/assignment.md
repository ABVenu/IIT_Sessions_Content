# **Assignment: EDA Workshop Building a Data Dashboard**

---

## **Question 1. (MCQ)**

What is the first step in the end-to-end data pipeline described in the workshop?

A) Visualization
B) Cleaning the dataset
C) Retrieving data from an external API
D) Building a dashboard

**Correct answer:** C

**Explanation:**
The workflow begins with **data ingestion** from an external API. Raw data must first be retrieved before it can be cleaned, analyzed, or visualized.

---

## **Question 2. (MCQ)**

What format does the API used in the workshop return?

A) CSV
B) XML
C) JSON
D) YAML

**Correct answer:** C

**Explanation:**
Most modern APIs return data in **JSON format**, which can easily be converted into Python dictionaries and then into Pandas DataFrames.

---

## **Question 3. (MCQ)**

Which Python library is used in the workshop to convert API data into a DataFrame?

A) NumPy
B) Pandas
C) Seaborn
D) Matplotlib

**Correct answer:** B

**Explanation:**
Pandas is used to convert JSON data into a structured DataFrame, enabling easier analysis and manipulation.

---

## **Question 4. (MCQ)**

What is the purpose of the following code?

```python
df = pd.DataFrame(data)
```

A) Save data to disk
B) Convert JSON data into a structured table
C) Send API requests
D) Plot the dataset

**Correct answer:** B

**Explanation:**
This line converts the raw JSON response into a **Pandas DataFrame**, which allows structured analysis using rows and columns.

---

## **Question 5. (MCQ)**

What does the following code compute?

```python
post_counts = df.groupby("user_id").size()
```

A) Average post length
B) Number of posts created by each user
C) Total number of users
D) Number of columns in the dataset

**Correct answer:** B

**Explanation:**
`groupby("user_id").size()` counts how many rows belong to each user, effectively calculating the number of posts per user.

---

## **Question 6. (MCQ)**

What does this code accomplish?

```python
df["post_length"] = df["body"].apply(len)
```

A) Deletes the body column
B) Calculates the number of characters in each post
C) Converts text to numbers
D) Counts number of users

**Correct answer:** B

**Explanation:**
`apply(len)` calculates the **length of the text in each post**, creating a new column representing post length.

---

## **Question 7. (MCQ)**

Which library is used to build the interactive dashboard in this workshop?

A) Flask
B) Dash
C) Streamlit
D) Plotly

**Correct answer:** C

**Explanation:**
Streamlit is used to quickly build interactive dashboards using simple Python scripts.

---

## **Question 8. (MCQ)**

What does the following Streamlit command display?

```python
st.dataframe(df.head())
```

A) A static image of the dataset
B) An interactive table showing the first rows of the dataset
C) A chart visualization
D) The dataset summary statistics

**Correct answer:** B

**Explanation:**
`st.dataframe()` displays an interactive table inside the Streamlit dashboard, allowing users to explore the data.

---

## **Question 9. (Subjective)**

### **Build a Simple Data Dashboard**

In this assignment, you will implement the full data workflow demonstrated in the workshop.

### **Tasks**

Create a Python dashboard that performs the following steps:

1. Fetch post data from the API:

```
https://jsonplaceholder.typicode.com/posts
```

2. Convert the JSON response into a **Pandas DataFrame**.

3. Perform basic cleaning:

   * Rename `userId` to `user_id`
   * Drop the `id` column

4. Perform exploratory analysis:

   * Count how many posts each user created using `groupby()`

5. Create a new column:

   * `post_length` representing the number of characters in each post

6. Visualize insights:

   * Bar chart showing **posts per user**
   * Histogram showing **distribution of post length**

7. Build a **Streamlit dashboard** that displays:

   * A dataset preview
   * The posts-per-user chart
   * The post length distribution

---

## Submission Instructions (Read Carefully)

1. You have **already created a GitHub repository**.

2. Inside that repository:

   * Create a **new folder** named:

```
eda-dashboard-assignment
```

3. Inside the folder create two files:

```
fetch_data.py
dashboard.py
```

4. Run the dashboard locally using:

```bash
streamlit run dashboard.py
```

5. Verify that:

   * The dashboard loads correctly
   * Charts and data preview appear

6. Once everything is ready:

   * Add the changes
   * Commit with a proper message
   * Push to GitHub

7. **Final submission:**

   * Submit the **GitHub folder link** (not the entire repository).

---

# ✅ **Solution**

### **fetch_data.py**

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    # Cleaning
    df = df.rename(columns={"userId": "user_id"})
    df = df.drop(columns=["id"])

    print(df.head())

else:
    print("Failed to fetch data")
```

---

### **dashboard.py**

```python
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Fetch data
url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

df = pd.DataFrame(data)

# Cleaning
df = df.rename(columns={"userId": "user_id"})
df = df.drop(columns=["id"])

# Feature engineering
df["post_length"] = df["body"].apply(len)

# Aggregation
post_counts = df.groupby("user_id").size()

# Dashboard
st.title("Post Data Dashboard")

st.write("Dataset Preview")
st.dataframe(df.head())

st.write("Posts per User")
st.bar_chart(post_counts)

st.write("Post Length Distribution")
st.bar_chart(df["post_length"])
```