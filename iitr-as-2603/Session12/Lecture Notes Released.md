# Plotting & Storytelling with Data

## What We Covered So Far and What's Coming Next

In the previous session, we went deep into **SQL aggregation and joining tables**. We learnt how to use `GROUP BY` with aggregate functions like `COUNT`, `SUM`, and `AVG` to summarise data, how `HAVING` filters those summaries, and how `INNER JOIN` and `LEFT JOIN` connect data spread across multiple tables. We also mapped these SQL ideas to familiar pandas operations like `groupby()` and `merge()`.

Now that you know how to *query* and *summarise* data, the next natural step is to *see* it. Numbers in rows and columns only tell part of the story — a well-made chart can reveal trends, outliers, and patterns in seconds that would take minutes to spot in a table.

This session introduces you to the full cycle of **Exploratory Data Analysis (EDA)** and **data visualisation** — from inspecting a raw dataset to building interactive charts and ultimately communicating your findings as a clear story.

---

## Introduction to EDA — Why You Must Look Before You Analyse

Before writing a single line of code or making any chart, every good data analyst does one thing first: they *inspect* the data. This step is called **Exploratory Data Analysis**.

- **Official Definition:** **EDA (Exploratory Data Analysis)** is the process of inspecting, summarising, and visualising a dataset to understand its structure, spot patterns, and identify problems before deeper analysis.
- **In Simple Words:** It is like checking the ingredients before cooking. You check what you have, whether anything is missing, and whether anything looks wrong.
- **Real-Life Example:** Think of a doctor reviewing a patient's file before giving a diagnosis — checking age, weight, existing conditions, missing reports. That review is EDA for the doctor.

EDA is not a one-time step. You keep going back to it as you discover new things about the data.

![EDA means inspecting and summarising data before deeper analysis — like checking ingredients before cooking or a doctor reviewing a file before a diagnosis](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-eda-inspect-first.png)

---

## The EDA Inspection Checklist

Every time you pick up a new dataset, go through this checklist in order. Each step answers a specific question about the data.

![Four-step EDA checklist: load and peek, column types and missing values, summary statistics, then distributions and outliers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-eda-four-step-checklist.png)

**Step 1 — Load and Peek at the Data**

```python
import pandas as pd                        # import pandas for data handling

df = pd.read_csv('sales_data.csv')         # load the dataset from a CSV file

print(df.shape)                            # print the number of rows and columns
print(df.head())                           # print the first 5 rows to see what the data looks like
print(df.tail())                           # print the last 5 rows to check for trailing issues
```

**How the code works:**
- `pd.read_csv()` loads the file into a DataFrame (a table in memory)
- `df.shape` gives you `(rows, columns)` — a quick size check
- `df.head()` and `df.tail()` give you a preview of the data without loading everything

---

**Step 2 — Understand Column Types and Missing Values**

```python
print(df.info())                           # shows column names, data types, and non-null counts
print(df.isnull().sum())                   # counts missing values in each column
```

**How the code works:**
- `df.info()` is your most important single command — it tells you what type each column is (number, text, date) and whether there are any missing values
- `df.isnull().sum()` counts how many `NaN` (missing) values exist per column — a high number here is a red flag

**Common Doubt:** "What is a missing value?"
- A **missing value (NaN)** means that data was not recorded or is unavailable for that row and column.
- If you ignore them, some functions will give you wrong results or throw errors.

---

**Step 3 — Summary Statistics**

```python
print(df.describe())                       # shows count, mean, min, max, and percentiles for numeric columns
print(df['category'].value_counts())       # counts how many times each category appears in a text column
```

**How the code works:**
- `df.describe()` instantly shows you the **range**, **average**, and **spread** of every numeric column
- `value_counts()` is used for text/categorical columns to see which values are most common
- Together, these two commands tell you whether your numbers are in a sensible range and whether any category is dominating the data

---

**Step 4 — Identify Distributions and Anomalies**

After looking at summary stats, you check for two things:

- **Distribution** — How are the values spread? Are they mostly clustered around the average, or spread all over?
- **Anomalies / Outliers** — Are there any values that seem unrealistically high or low?

| Signal | What to Look For |
|--------|-----------------|
| **Min / Max are extreme** | Possible data entry error or genuine outlier |
| **Mean is far from Median** | The distribution is skewed (not symmetric) |
| **A category has 90% of rows** | Imbalanced data — may distort analysis |
| **Missing values > 20%** | Column may not be reliable for analysis |

- **Official Definition:** An **outlier** is a data point that differs significantly from the rest of the observations.
- **In Simple Words:** If 99 students scored between 40 and 80 marks and one student scored 999, that 999 is an outlier — likely a data error.
- **Real-Life Example:** A salary dataset where most employees earn ₹30,000–₹80,000 per month but one row shows ₹90,00,000 — that row needs to be investigated.

**A Quick Note on Auto EDA Tools**

As you grow as a data analyst, you will discover Python packages that can automate many of these inspection steps in a single command. These **auto EDA tools** generate a full HTML report — distributions, missing values, correlations — with almost no code. However, the ability to *interpret* what those charts mean is a skill only you can develop. Tools give you the report; your understanding gives it meaning. We will explore these tools in future sessions.

---

## Introduction to Matplotlib — Your Drawing Board

Once you have inspected the data, you start drawing charts. The first and most foundational library for this in Python is **Matplotlib**.

- **Official Definition:** **Matplotlib** is a Python library used to create static, animated, and interactive visualisations.
- **In Simple Words:** Matplotlib is the pencil and graph paper of Python. It lets you draw any type of chart — you control every detail.
- **Real-Life Example:** Imagine a whiteboard in a classroom. Matplotlib is that whiteboard — you draw exactly what you want, but you have to do it manually.

**Import and Basic Setup:**

```python
import matplotlib.pyplot as plt            # import pyplot module and give it the alias 'plt'
```

The alias `plt` is a standard convention — every Python developer uses it, so always follow this pattern.

![Matplotlib is your drawing board — a flexible foundation for building line, bar, histogram, and custom static charts in Python](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-matplotlib-drawing-board.png)

---

## Line Plot — Showing Change Over Time

A **line plot** connects data points with a line and is best used when your data has a natural order — usually time.

- **Official Definition:** A line plot represents data as a series of points connected by straight lines, typically used to show trends over a continuous variable.
- **In Simple Words:** If you track your daily step count over a month, a line chart will show whether you've been walking more or less.
- **Real-Life Example:** Stock price over time, monthly rainfall, website visitors per day — all of these are naturally shown as line plots.

```python
import matplotlib.pyplot as plt            # import the plotting library

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']   # x-axis values (time)
sales  = [12000, 15000, 13500, 17000, 19000, 21000]   # y-axis values (sales numbers)

plt.figure(figsize=(8, 4))                # create a canvas with width=8, height=4 inches
plt.plot(months, sales, marker='o',       # draw the line; 'o' adds a dot at each data point
         color='steelblue', linewidth=2)  # set the line colour and thickness
plt.title('Monthly Sales Trend')          # add a title at the top
plt.xlabel('Month')                       # label the x-axis
plt.ylabel('Sales (₹)')                  # label the y-axis
plt.tight_layout()                        # automatically adjust spacing so nothing gets cut off
plt.show()                                # display the chart
```

**How the code works:**
- `plt.figure(figsize=...)` sets the canvas size — a wider canvas makes the chart easier to read
- `plt.plot(x, y)` draws the line using the lists as x and y coordinates
- `marker='o'` puts a small circle at each data point so individual values are visible
- `plt.tight_layout()` is good practice — it prevents labels from being clipped at the edges

---

## Bar Chart — Comparing Categories

A **bar chart** is used when you want to compare values across different categories side by side.

- **Official Definition:** A bar chart displays rectangular bars where the height (or length) of each bar is proportional to the value it represents.
- **In Simple Words:** Think of a sports scoreboard — each team has a bar showing their score. You can instantly see who is winning.
- **Real-Life Example:** Total sales per product, number of students per department, revenue per city — all ideal for bar charts.

```python
import matplotlib.pyplot as plt                          # import plotting library

products  = ['Laptop', 'Phone', 'Tablet', 'Watch']      # category labels (x-axis)
revenues  = [85000, 62000, 45000, 31000]                 # values to compare (y-axis)

plt.figure(figsize=(7, 4))                               # set canvas size
plt.bar(products, revenues,                              # draw the bar chart
        color=['#4C72B0', '#DD8452', '#55A868', '#C44E52'])  # one colour per bar
plt.title('Product Revenue Comparison')                  # chart title
plt.xlabel('Product')                                    # x-axis label
plt.ylabel('Revenue (₹)')                               # y-axis label
plt.tight_layout()                                       # prevent clipping
plt.show()                                               # show the chart
```

**How the code works:**
- `plt.bar(x, y)` draws vertical bars; each element in `products` gets one bar
- The `color` list assigns a different colour to each bar — this makes the chart visually distinct
- Bar height directly equals the value in `revenues` — making comparison instant

---

## Histogram — Understanding the Distribution of One Column

A **histogram** looks similar to a bar chart but works very differently. It shows how a *single numeric column* is distributed — how many values fall in each range.

- **Official Definition:** A histogram groups numeric data into ranges called **bins** and shows the frequency (count) of values in each bin.
- **In Simple Words:** If you have 1000 student marks between 0 and 100, a histogram tells you: "How many students scored between 40–50? How many between 80–90?" It shows the shape of the data.
- **Real-Life Example:** A school wants to see if most students are scoring in the 60–70 range or spread evenly. A histogram answers that in one glance.

```python
import matplotlib.pyplot as plt                # import plotting library
import pandas as pd                            # import pandas

df = pd.read_csv('student_scores.csv')         # load the dataset

plt.figure(figsize=(7, 4))                     # set canvas size
plt.hist(df['marks'],                          # the column to analyse
         bins=10,                              # divide the range into 10 equal buckets
         color='mediumseagreen',               # bar colour
         edgecolor='white')                    # add white lines between bars for clarity
plt.title('Distribution of Student Marks')    # chart title
plt.xlabel('Marks')                            # x-axis label
plt.ylabel('Number of Students')              # y-axis label
plt.tight_layout()                             # prevent clipping
plt.show()                                     # show the chart
```

**How the code works:**
- `plt.hist(column, bins=10)` automatically groups the values and counts how many fall in each group
- `bins=10` splits the data range into 10 equal segments — more bins = more detail but can look noisy
- The height of each bar is the *count* of values in that range — this reveals whether data is spread out or concentrated

**Common Doubt:** "What's the right number of bins?"
- Too few bins (e.g., 3) hides the shape. Too many bins (e.g., 100) makes it look like noise.
- Start with 10–15 bins and adjust based on what looks clear.

![Line charts show trends over time, bar charts compare categories, and histograms show how one numeric column is distributed across bins](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-chart-types-line-bar-hist.png)

---

## Skewness — Reading the Shape of Your Data

Once you draw a histogram, the next question is: *what shape is this?* The shape of a histogram tells you whether your data is balanced or lopsided — this is called **skewness**.

- **Official Definition:** **Skewness** is a measure of the asymmetry of a distribution. A perfectly symmetric distribution has zero skew; a lopsided one is either positively or negatively skewed.
- **In Simple Words:** Imagine pouring water into a bowl. If the water piles up on the left and has a long tail stretching to the right, that is right skew. If it piles up on the right with a tail stretching left, that is left skew.
- **Real-Life Example:** In a company's salary dataset, most employees earn ₹30,000–₹60,000 but a handful of senior executives earn ₹5,00,000+. The histogram will pile up on the left with a long tail stretching to the right — this is **right (positive) skew**.

**Right Skew (Positive Skew)**

- The **tail stretches to the right** — there are a few very high values pulling the average up.
- The **mean is greater than the median** because the extreme high values pull the mean.
- **Common examples:** Income data, house prices, startup valuations — most are modest, but a few are extremely large.
- **What it means for analysis:** Outliers on the right are inflating the average. Using the median instead of the mean gives a fairer picture of the "typical" value.

**Left Skew (Negative Skew)**

- The **tail stretches to the left** — there are a few very low values pulling the average down.
- The **mean is less than the median** because the extreme low values pull the mean down.
- **Common examples:** Exam scores in an easy test where most students score high but a few score very low; age at retirement in a dataset where most retire at 60+ but a few retire early.
- **What it means for analysis:** Outliers on the left are dragging the average down. Again, the median is a better representation of the centre.

**The Connection Between Skewness and Outliers**

- Skewness and outliers are directly linked — a highly skewed distribution almost always has outliers on the stretched side.
- When you see a skewed histogram, immediately check the min/max values in `df.describe()` to confirm whether extreme values exist.
- A good analyst always notes skewness in their EDA before deciding which summary statistic (mean or median) to use for reporting.

| Skew Type | Tail Direction | Mean vs Median | Typical Cause |
|-----------|---------------|----------------|---------------|
| **Right / Positive** | Stretches right | Mean > Median | A few very high values (income, prices) |
| **Left / Negative** | Stretches left | Mean < Median | A few very low values (test scores on easy exam) |
| **Symmetric (no skew)** | Balanced on both sides | Mean ≈ Median | Normally distributed data (height, weight) |

---

## Introduction to Plotly — Interactive Charts

Matplotlib gives you static charts — images you can save and share. **Plotly** takes it a step further with interactive charts that you can zoom, hover over, and filter.

- **Official Definition:** **Plotly** is a Python graphing library that produces interactive, web-based visualisations.
- **In Simple Words:** If Matplotlib is a printed graph, Plotly is a touchscreen dashboard. The viewer can hover over a bar to see the exact value, zoom into a time range, or click to hide a line.
- **Real-Life Example:** Business dashboards you see on websites — where you hover over a sales chart and it shows you the exact number — are typically built with tools like Plotly.

**Matplotlib vs Plotly — When to Use Which**

| | Matplotlib | Plotly |
|---|---|---|
| **Output type** | Static image (PNG, PDF) | Interactive (browser-based) |
| **Best for** | Reports, printed documents, publications | Exploration, presentations, dashboards |
| **Ease of use** | More manual setup required | Reads directly from DataFrames — less code |
| **Performance** | Fast even on very large datasets | Can slow down on extremely large data |
| **Interactivity** | None (static) | Hover tooltips, zoom, pan, click to filter |

The practical rule: use **Matplotlib** when you need a polished, static final output; use **Plotly** when you are still *exploring* the data and want to interact with charts quickly.

![Matplotlib excels at polished static figures you can save and share; Plotly adds hover tooltips, zoom, and filtering for interactive exploration](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-static-vs-interactive-plotly.png)

```python
import plotly.express as px                   # import Plotly Express (the easy-to-use version of Plotly)
import pandas as pd                           # import pandas

df = pd.read_csv('sales_data.csv')            # load the dataset

fig = px.bar(df,                              # create a bar chart from the DataFrame
             x='month',                      # column for the x-axis
             y='sales',                      # column for the y-axis
             color='region',                 # colour the bars by region — automatically adds a legend
             title='Monthly Sales by Region') # chart title

fig.show()                                    # open the chart in the browser (interactive)
```

**How the code works:**
- `px.bar()` reads directly from a DataFrame — no need to extract lists manually
- `color='region'` automatically groups and colours bars by the `region` column
- `fig.show()` opens the chart in a browser tab where it is fully interactive — hover, zoom, click

---

## Scatter Plot — Spotting Relationships Between Two Columns

A **scatter plot** is one of the most powerful EDA tools for understanding *relationships*. Each dot on the chart represents one row of data, plotted using two numeric columns as its x and y coordinates.

- **Official Definition:** A scatter plot displays individual data points as dots on a two-dimensional plane, used to reveal the relationship (correlation) between two numeric variables.
- **In Simple Words:** Imagine you have data on students — their study hours and their marks. Each student is one dot. If you see the dots going from bottom-left to top-right, it means "more study = higher marks." That pattern is called a **positive relationship**.
- **Real-Life Example:** A startup dataset with funding amount and valuation — if companies with more funding tend to have higher valuations, the scatter plot will show an upward trend.

**Reading a Scatter Plot:**

- **Positive relationship (positive correlation):** Dots go from bottom-left to top-right — as X increases, Y increases. Example: study hours vs marks.
- **Negative relationship (negative correlation):** Dots go from top-left to bottom-right — as X increases, Y decreases. Example: hours of TV watched vs exam score.
- **No relationship:** Dots are scattered randomly — X and Y have no pattern. Example: shoe size vs salary.
- **Outliers on scatter plots:** A dot far away from the main cluster — one company with massive funding but very low valuation, for example — stands out immediately and needs investigation.

```python
import plotly.express as px                   # import Plotly Express
import pandas as pd                           # import pandas

df = pd.read_csv('startups.csv')              # load startup funding and valuation data

fig = px.scatter(df,                          # create a scatter plot
                 x='funding',                 # x-axis: funding amount
                 y='valuation',               # y-axis: company valuation
                 title='Funding vs Valuation — Do More Funded Startups Get Valued Higher?')
fig.show()                                    # display in browser — hover each dot to see details
```

**How the code works:**
- `px.scatter()` places one dot per row of the DataFrame
- Each dot's horizontal position is its `funding` value; its vertical position is its `valuation`
- Hovering over any dot in the browser shows the exact values — making outliers easy to identify
- A clear upward trend (positive relationship) or random scatter (no relationship) is visible instantly

**Line Chart with Plotly:**

```python
import plotly.express as px                   # import Plotly Express
import pandas as pd                           # import pandas

df = pd.read_csv('stock_prices.csv')          # load stock price data

fig_line = px.line(df,                        # create a line chart
                   x='date',                  # x-axis: date column
                   y='price',                 # y-axis: price column
                   title='Stock Price Over Time')  # title
fig_line.show()                               # display in browser
```

**How the code works:**
- `px.line()` draws an interactive line chart — hovering shows the exact date and price
- Interactive zoom lets you narrow down to a specific time window without writing more code

---

## Choosing the Right Chart

One of the most common mistakes beginners make is using the wrong chart type for their data. Every chart type is designed for a specific kind of question.

| Question You're Asking | Best Chart |
|------------------------|-----------|
| How does a value change over time? | **Line Chart** |
| How do different categories compare? | **Bar Chart** |
| How is a single numeric column distributed? | **Histogram** |
| Is there a relationship between two numeric columns? | **Scatter Plot** |
| What share does each category take of a whole? | **Pie / Donut Chart** |
| How does a value vary across two categories? | **Grouped Bar Chart** |

**The Three Questions to Ask Before Drawing Any Chart:**

1. **What type is my data?** — Is it a number, a category, or a date/time?
2. **What relationship am I showing?** — Trend over time? Comparison? Distribution? Correlation?
3. **Who is my audience?** — A technical analyst can read a scatter plot; a business executive may prefer a simple bar chart.

**Common Mistakes and How to Avoid Them:**

- Using a **pie chart with more than 5 categories** — it becomes unreadable. Use a bar chart instead.
- Using a **line chart for unordered categories** — a line implies a sequence; use a bar chart if the order doesn't matter.
- Using a **bar chart to show distribution** — that is the job of a histogram.

---

## Data Storytelling — Turning Charts Into Insights

A chart is not a story by itself. **Data Storytelling** is the skill of combining data, visuals, and words to communicate a clear, meaningful message to your audience.

- **Official Definition:** **Data Storytelling** is the practice of using data visualisations alongside narrative context to explain insights and drive understanding or decisions.
- **In Simple Words:** Anyone can make a chart. A data storyteller explains *what it means*, *why it matters*, and *what should be done about it*.
- **Real-Life Example:** Showing a sales chart is a chart. Saying *"Sales dropped 30% in March because of school holiday season — we should run a promotion in April next year"* is a data story.

**The Three Pillars of a Data Story:**

- **Data** — The numbers and facts (the "what happened")
- **Visuals** — The charts that make the data scannable (the "here's the proof")
- **Narrative** — The explanation that gives context and recommendation (the "so what and what next")

![A strong data story combines three pillars: the facts (data), charts that make them scannable (visuals), and narrative that explains why it matters and what to do next](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12/session12-data-storytelling-three-pillars.png)

**Practical Techniques for Data Storytelling:**

- **Highlight the key insight** — Use a chart title that states the finding, not just the variable. Instead of *"Monthly Sales"*, write *"Sales Grew 40% in Q2"*.
- **Remove clutter** — Every element on a chart should serve a purpose. Extra gridlines, unnecessary colours, and long legends distract from the message.
- **Use annotations** — Add a short text note directly on the chart pointing to the key moment (e.g., "New campaign launched here").
- **Lead with the conclusion** — Don't make the audience discover the insight themselves. State it upfront, then show the chart as evidence.

**Adding Annotations in Matplotlib:**

```python
import matplotlib.pyplot as plt                          # import plotting library

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']     # x-axis months
sales  = [12000, 15000, 13500, 17000, 25000, 21000]     # sales figures

plt.figure(figsize=(8, 4))                               # set canvas size
plt.plot(months, sales, marker='o',                      # draw the line with dots
         color='steelblue', linewidth=2)

plt.annotate('Campaign Launched',                        # text label for the annotation
             xy=('May', 25000),                          # point to annotate (x, y)
             xytext=('Mar', 23000),                      # where to place the text box
             arrowprops=dict(arrowstyle='->',            # draw an arrow pointing to the data point
                             color='red'),
             fontsize=9, color='red')                    # style the annotation text

plt.title('Sales Spike Driven by Marketing Campaign')   # insight-first title
plt.xlabel('Month')                                     # x-axis label
plt.ylabel('Sales (₹)')                                # y-axis label
plt.tight_layout()                                      # prevent clipping
plt.show()                                              # display the chart
```

**How the code works:**
- `plt.annotate()` draws a text label with an arrow pointing to a specific data point
- `xy=` is the data point to point *at*, `xytext=` is where the label text should appear
- `arrowprops` controls the arrow style — making the insight unmissable for the viewer
- The title now tells a story: it is not *"Monthly Sales"* but *"Sales Spike Driven by Marketing Campaign"*

---

## Key Takeaways

- **EDA is always the first step** before any visualisation or analysis — inspect shape, types, missing values, and summary statistics using `df.info()`, `df.describe()`, and `df.isnull().sum()`.
- **Skewness reveals the shape of your data** — a right-skewed histogram signals a few very high outliers inflating the mean; a left-skewed one signals a few very low values. Always check skewness before deciding whether to report the mean or the median.
- **Matplotlib** is the foundation library for Python charts — line plots show trends, bar charts compare categories, and histograms reveal how a numeric column is distributed.
- **Plotly** adds interactivity to your charts — viewers can hover, zoom, and filter, making it ideal for exploratory analysis and presentations. Use Matplotlib for polished static output; use Plotly when actively exploring data.
- **Scatter plots** show relationships between two numeric columns — each dot is one row. An upward trend means a positive relationship; a random scatter means no relationship. Outliers are immediately visible as isolated dots.
- **Choosing the right chart matters** — match the chart type to the question you're answering; a wrong chart type hides the insight instead of showing it.
- **Data storytelling completes the cycle** — a chart without context is just a picture; combining a clear insight-first title, minimal clutter, and a narrative explanation turns data into a decision-making tool.

In the upcoming sessions, we will build on these visualisation skills to create complete analytical dashboards, work with real-world datasets, and use AI tools to accelerate the EDA and storytelling workflow.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Description |
|---|---|
| `import pandas as pd` | Import pandas for loading and inspecting data |
| `df.shape` | Returns `(rows, columns)` — size of the DataFrame |
| `df.head()` / `df.tail()` | Preview the first/last 5 rows |
| `df.info()` | Shows column names, data types, and non-null counts |
| `df.describe()` | Summary statistics for all numeric columns |
| `df.isnull().sum()` | Count of missing values per column |
| `df['col'].value_counts()` | Frequency count for each unique value in a column |
| `import matplotlib.pyplot as plt` | Import Matplotlib for static charts |
| `plt.plot()` | Draw a line chart |
| `plt.bar()` | Draw a bar chart |
| `plt.hist()` | Draw a histogram |
| `plt.title()` | Add a title to the chart |
| `plt.xlabel()` / `plt.ylabel()` | Label the x and y axes |
| `plt.tight_layout()` | Auto-fix spacing to prevent label clipping |
| `plt.show()` | Display the chart |
| `plt.annotate()` | Add an arrow + text label pointing to a data point |
| `import plotly.express as px` | Import Plotly Express for interactive charts |
| `px.bar()` | Interactive bar chart |
| `px.line()` | Interactive line chart |
| `px.scatter()` | Interactive scatter plot |
| `fig.show()` | Open the interactive chart in the browser |
| **EDA** | Exploratory Data Analysis — inspecting data before analysis |
| **Outlier** | A value that is unusually far from the rest of the data |
| **Distribution** | How values in a column are spread across their range |
| **Histogram Bins** | Equal-width ranges used to group values in a histogram |
| **Skewness** | The asymmetry of a distribution — right skew has a long right tail; left skew has a long left tail |
| **Right Skew (Positive Skew)** | Tail stretches right; mean > median; caused by a few very high values |
| **Left Skew (Negative Skew)** | Tail stretches left; mean < median; caused by a few very low values |
| **Correlation** | A measure of how strongly two variables move together — positive, negative, or none |
| **Scatter Plot** | A chart using dots to show the relationship between two numeric columns |
| **Data Storytelling** | Combining data, visuals, and narrative to communicate insights |
| **Annotation** | A label with an arrow added to a chart to highlight a key point |
| **Auto EDA Tools** | Python packages that automatically generate summary reports for a dataset |
