# EDA Workshop: Building a Data Dashboard

## What You’ll Learn

In this hands-on workshop, you will apply the tools learned in previous sessions to build a simple **data dashboard**. You will retrieve raw data from an API, clean and structure the data using Pandas, analyze and visualize insights using Python visualization tools, and finally create a simple interactive dashboard using Streamlit.

This workshop mirrors a real-world data workflow used by AI engineers and data scientists:

1. Retrieve data from an external API  
2. Clean and structure the dataset  
3. Explore the data with EDA techniques  
4. Visualize key patterns  
5. Build a simple dashboard to present insights  

By the end of the session, you will have created a working interactive data dashboard.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/f4b145b6-0830-4d52-b194-1bd45d96002b/1ZaS2TQPQtp33pYe.png)

---

# Part 1: The End-to-End Data Pipeline

Before writing any code, it is important to understand the full workflow.

A typical AI data workflow looks like this:

```

External Data Source (API)
↓
Raw JSON Data
↓
Cleaning & Structuring (Pandas)
↓
Exploratory Data Analysis
↓
Visualization
↓
Interactive Dashboard

```

This pipeline transforms raw information into actionable insights.

In this workshop, you will implement each stage step by step.

---

# Part 2: Step 1 — Ingesting Raw API Data

## Understanding the Goal

We will start by retrieving data from a public API. Many APIs provide structured data in JSON format, which can easily be converted into Pandas DataFrames.

For this exercise we will use a public dataset API such as:

```

[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)

```

This API returns sample post data that can be analyzed.

---

## Activity 1: Fetch Data from an API

Create a new Python file called:

```

fetch_data.py

````

Install dependencies if needed:

```bash
pip install requests pandas
````

Example code:

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())
else:
    print("Failed to fetch data")
```

Run the script and inspect the output.

Discussion questions:

* How many columns exist?
* What type of data does each column represent?
* Which columns might be useful for analysis?

---

# Part 3: Step 2 — Cleaning the Dataset with Pandas

Raw API data is rarely ready for analysis.

Typical cleaning steps include:

* removing unnecessary columns
* renaming columns
* handling missing values
* inspecting structure

---

## Activity 2: Inspect the Data

Add the following commands:

```python
print(df.info())
print(df.describe())
```

These help you understand the dataset structure.

---

## Activity 3: Clean the Data

Example cleaning steps:

```python
df = df.rename(columns={
    "userId": "user_id"
})

df = df.drop(columns=["id"])

print(df.head())
```

Questions for exploration:

* Why might the `id` column be unnecessary?
* How does renaming improve clarity?

---

# Part 4: Step 3 — Exploring the Data

Now that the data is structured, we can perform basic exploratory analysis.

Example questions:

* Which users post the most content?
* How long are the posts?
* Are there patterns across users?

---

## Activity 4: Simple Aggregation

```python
post_counts = df.groupby("user_id").size()

print(post_counts)
```

This calculates how many posts each user created.

Discussion:

* Which user has the most posts?
* Is the distribution balanced?

---

# Part 5: Step 4 — Visualizing Insights

Visualization helps transform raw numbers into understandable patterns.

Install visualization libraries if needed:

```bash
pip install matplotlib seaborn
```

---

## Activity 5: Create a Bar Chart

```python
import matplotlib.pyplot as plt

post_counts.plot(kind="bar")

plt.title("Posts Per User")
plt.xlabel("User ID")
plt.ylabel("Number of Posts")

plt.show()
```

Questions:

* Which users are most active?
* Are there outliers?

---

## Activity 6: Visualizing Text Length

We can analyze post length:

```python
df["post_length"] = df["body"].apply(len)

df["post_length"].hist()

plt.title("Distribution of Post Length")
plt.xlabel("Character Count")
plt.ylabel("Frequency")

plt.show()
```

This reveals how long typical posts are.

---

# Part 6: Step 5 — Building a Simple Streamlit Dashboard

Now we convert our analysis into a simple interactive dashboard.

Install Streamlit:

```bash
pip install streamlit
```

Create a new file:

```
dashboard.py
```

---

## Activity 7: Basic Streamlit App

```python
import streamlit as st
import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

df = pd.DataFrame(data)

df["post_length"] = df["body"].apply(len)

st.title("Post Data Dashboard")

st.write("Dataset Preview")
st.dataframe(df.head())

st.write("Posts per User")
post_counts = df.groupby("userId").size()
st.bar_chart(post_counts)

st.write("Post Length Distribution")
st.bar_chart(df["post_length"])
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

Open the URL displayed in the terminal.

You now have an interactive data dashboard.

---

# Part 7: Suggested Extensions

Students can extend the dashboard by adding:

* filtering by user
* additional charts
* interactive controls
* more advanced visualizations

Example filter:

```python
user_filter = st.selectbox("Select User", df["userId"].unique())

filtered_df = df[df["userId"] == user_filter]

st.write(filtered_df)
```

This allows users to explore the data interactively.

---

# Workshop Discussion

Reflect on the workflow:

1. How did the API data differ from clean datasets?
2. What transformations were necessary?
3. Which visualizations communicated the clearest insights?
4. How could this pipeline scale to larger datasets?

Understanding these questions helps build intuition for real-world AI workflows.

---

# Key Takeaways

This workshop demonstrates a complete data workflow: retrieving raw API data, cleaning it with Pandas, performing exploratory analysis, visualizing insights, and presenting results in an interactive dashboard. These steps mirror the process used in professional data science and AI projects to transform raw information into actionable insight.

**Mental model:**

Collect → Clean → Explore → Visualize → Present.

---

# Additional Resources

Streamlit Documentation
[https://docs.streamlit.io](https://docs.streamlit.io)

Pandas Data Analysis Guide
[https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

Python Requests Library
[https://docs.python-requests.org/](https://docs.python-requests.org/)

Matplotlib Tutorials
[https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)