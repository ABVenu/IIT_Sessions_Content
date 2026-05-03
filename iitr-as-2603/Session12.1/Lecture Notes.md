# Problem Solving Session: Plotting & Storytelling with Data

## What You Will Learn

In the previous session, we built the full foundation of data visualisation. We covered **Exploratory Data Analysis (EDA)** — how to inspect a dataset using `df.info()`, `df.describe()`, and `df.isnull().sum()`. We then learnt how to draw three core chart types in **Matplotlib** (line, bar, histogram), how to build **interactive charts in Plotly**, how to pick the right chart for the right question, and finally how to turn a chart into a **data story** using annotations and insight-first titles.

Now it is time to put all of that knowledge into action. This session is a structured **hands-on practice session** — you will work through a complete real-world-style workflow from loading a raw dataset all the way to writing a final summary with insights.

**In this session you will:**
- Load a CSV dataset and quickly inspect its structure
- Check for missing values and data type issues before plotting
- Run simple summary analyses to find useful patterns
- Create bar charts, line charts, and histograms using Matplotlib
- Recreate one key chart as an interactive Plotly chart
- Practise choosing the correct chart type for different questions
- Format and label your charts professionally
- Write short, clear insights under each chart
- Assemble everything into a clean, notebook-style mini output

![Practice session roadmap: load a CSV → inspect columns and types → run a readiness check → summarise with groupby → chart in Matplotlib and Plotly → write insights → package a notebook-style mini report](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-workflow-overview.png)

---

## Setting Up Your Notebook

Before writing a single line of analysis code, every data session starts with one standard block that loads all the tools you will need.

- **Official Definition:** A **library import block** is the section at the very top of your notebook where you load all the Python packages your code depends on.
- **In Simple Words:** Think of it like laying out your tools on a table before starting a repair job — you gather your screwdriver, wrench, and pliers first so you are not hunting for them mid-work.
- **Real-Life Example:** A chef sets up all spices, vessels, and chopping boards before cooking. The import block is that preparation step.

![The import block loads pandas for tables, Matplotlib for static charts, Plotly for interactivity, and optionally quiets warnings — like laying out tools before you start the job](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-import-block-tools.png)

```python
# ── Standard import block for this session ──────────────────────────────────

import pandas as pd                   # for loading, inspecting, and summarising data
import matplotlib.pyplot as plt       # for static charts (bar, line, histogram)
import plotly.express as px           # for interactive charts
import warnings                       # to suppress harmless warning messages

warnings.filterwarnings('ignore')     # keep the notebook output clean and readable
```

**How the code works:**
- `pandas` handles all data loading and analysis — it is the spreadsheet of Python
- `matplotlib.pyplot` is your static drawing board — every basic chart lives here
- `plotly.express` adds hover, zoom, and filter to your charts with very little code
- `warnings.filterwarnings('ignore')` hides library version warnings so your output looks clean

---

## Step 1 — Dataset Loading and Quick Inspection

The dataset we will use throughout this session is a **superstore orders dataset** — a common beginner dataset that resembles what a retail business might track. It contains columns like order date, product category, sales amount, and region.

- **Official Definition:** **Dataset loading** is the process of reading a data file (like a CSV) into a Python DataFrame so you can work with it in code.
- **In Simple Words:** Think of a CSV file as a printed table on paper. Loading it into pandas is like scanning it into your computer so you can edit, filter, and calculate from it.
- **Real-Life Example:** Before a shop owner does monthly accounting, they pull out the sales register and open it on the table. Loading the CSV is that same action.

![Reading a CSV with pandas pulls a flat file off disk into a DataFrame df — turning a spreadsheet file into rows and columns you can filter, aggregate, and plot](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-csv-to-dataframe.png)

```python
# ── Load the dataset ─────────────────────────────────────────────────────────

df = pd.read_csv('superstore_orders.csv')   # read the CSV file into a DataFrame called df

# ── First look at size ───────────────────────────────────────────────────────

print("Shape of dataset:")
print(df.shape)                             # prints (number of rows, number of columns)

# ── Preview the first few rows ───────────────────────────────────────────────

print("\nFirst 5 rows:")
print(df.head())                            # shows the first 5 rows so you can see column names and sample values

# ── Preview the last few rows ────────────────────────────────────────────────

print("\nLast 5 rows:")
print(df.tail())                            # shows the last 5 rows to check for any trailing issues
```

**How the code works:**
- `pd.read_csv('filename.csv')` reads the file from disk and stores it in the variable `df`
- `df.shape` returns a tuple like `(9994, 13)` — meaning 9994 rows and 13 columns
- `df.head()` and `df.tail()` let you see a small sample without printing thousands of rows
- Always check `shape` first — it tells you immediately how large the dataset is

**What to look for after this step:**
- Do the column names make sense?
- Are there any columns that look like they have wrong or unexpected values?
- How many rows does the dataset have — is it small enough to work with or very large?

---

## Step 2 — Understanding the Columns

After you see the first few rows, the next step is to understand **what each column contains** — its data type and how it behaves.

- **Official Definition:** A **data type** (or dtype) defines what kind of value is stored in a column — for example, whole numbers (`int`), decimal numbers (`float`), or text (`object`).
- **In Simple Words:** Just like a form has fields for "Name" (text), "Age" (number), and "Date of Birth" (date), every column in a DataFrame has a specific type.
- **Real-Life Example:** If you have a column called `Sales` but it is stored as text instead of a number, pandas cannot add or average it — just like a calculator cannot add the word "forty" to another number.

```python
# ── Inspect column names, data types, and non-null counts ────────────────────

print("Column information:")
print(df.info())                            # shows each column name, its data type, and how many non-null values exist

# ── List all column names clearly ────────────────────────────────────────────

print("\nColumn names:")
print(df.columns.tolist())                  # prints a clean list of all column names
```

**How the code works:**
- `df.info()` is the most information-dense single command in pandas — it shows column names, types, and whether there are any missing values all at once
- `df.columns.tolist()` gives you a simple, clean list of column names — useful when you need to type column names in later steps
- If a date column shows `object` dtype instead of `datetime`, that is a flag to fix it before time-based analysis

---

## Step 3 — Basic Data Readiness Check

Before creating any charts, you must check whether the data has issues — missing values, wrong types, or obvious errors. This step is called a **data readiness check**.

- **Official Definition:** A **data readiness check** is the process of identifying and handling data quality issues — such as missing values, duplicate rows, or incorrect data types — before analysis.
- **In Simple Words:** Imagine printing a report from a spreadsheet that has blank cells or typos. The charts based on that data would be misleading. The data readiness check is like proofreading before you submit.
- **Real-Life Example:** A bank before processing a loan checks if the applicant's income field, credit score, and address are all filled in correctly. That is a readiness check on the application form.

![Before plotting, scan for missing values, duplicate rows, and wrong dtypes — the same instinct as proofreading a report before you print it](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-data-readiness.png)

```python
# ── Check for missing values in every column ────────────────────────────────

print("Missing values per column:")
print(df.isnull().sum())                    # counts the number of NaN (missing) values in each column

# ── Check for duplicate rows ─────────────────────────────────────────────────

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())               # counts rows that are exact copies of another row

# ── Check data types again in a focused way ──────────────────────────────────

print("\nData types:")
print(df.dtypes)                           # prints the dtype of every column — useful to spot columns stored in the wrong type
```

**How the code works:**
- `df.isnull().sum()` — if any column returns a number greater than 0, that column has missing values that need a decision: fill them, drop them, or leave them if they do not affect your analysis
- `df.duplicated().sum()` — duplicate rows can skew totals and counts; if the number is high, you should drop duplicates with `df.drop_duplicates()`
- `df.dtypes` is a focused type-only view — use this to confirm numeric columns are `int64` or `float64` and not `object`

**Simple fixes for common issues:**

```python
# ── Drop duplicate rows if any exist ────────────────────────────────────────

df = df.drop_duplicates()                  # removes any rows that are exact duplicates, resets the DataFrame

# ── Fill missing values in a numeric column with the column's median ────────

df['Sales'] = df['Sales'].fillna(df['Sales'].median())   # replace NaN in Sales with the median value

# ── Drop rows where a key column is completely missing ───────────────────────

df = df.dropna(subset=['Order Date', 'Category'])        # remove rows where Order Date or Category is blank
```

**How the code works:**
- `drop_duplicates()` removes rows that are identical copies — good practice before any counting or summing
- `fillna(median)` is a safe default for numeric columns — the median is less affected by extreme values than the mean
- `dropna(subset=[...])` only drops rows where *specific* columns are missing — safer than dropping all rows with any NaN

---

## Step 4 — Simple Summary Analysis

Now that the data is clean and ready, you extract **2–3 key observations** before drawing any chart. This gives you a direction — you know what is interesting and worth visualising.

- **Official Definition:** **Summary analysis** uses aggregation functions like `value_counts()` and `groupby()` to collapse raw rows into meaningful summaries — totals, averages, and counts by category.
- **In Simple Words:** If you have 10,000 order rows, you do not analyse each row one by one. You group them: "What is total sales per category?" or "Which region has the most orders?" That grouping is summary analysis.
- **Real-Life Example:** A cricket scorecard is a summary. Instead of listing every single ball bowled, it shows total runs per player per match. `groupby()` creates scorecards from raw data.

![value_counts() and groupby() collapse thousands of orders into totals and averages — the numbers you actually want on a chart](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-groupby-summary.png)

```python
# ── How many orders per category? ────────────────────────────────────────────

print("Order count by Category:")
print(df['Category'].value_counts())       # counts how many rows (orders) belong to each category

# ── What is total sales by Category? ────────────────────────────────────────

category_sales = df.groupby('Category')['Sales'].sum()   # group by Category, then sum the Sales column
print("\nTotal Sales by Category:")
print(category_sales)                                      # prints total revenue per category

# ── What is average sales by Region? ────────────────────────────────────────

region_avg = df.groupby('Region')['Sales'].mean()          # group by Region, then find the average sale value
print("\nAverage Sales by Region:")
print(region_avg.sort_values(ascending=False))             # sort from highest to lowest for easy reading

# ── Monthly order trend ──────────────────────────────────────────────────────

df['Order Date'] = pd.to_datetime(df['Order Date'])        # convert the Order Date column from text to a proper date type
df['Month'] = df['Order Date'].dt.to_period('M')           # extract the year-month (e.g. 2023-01) from the date
monthly_orders = df.groupby('Month').size()                # count the number of orders in each month
print("\nMonthly Order Count:")
print(monthly_orders.tail(12))                             # print the last 12 months for a recent trend view
```

**How the code works:**
- `value_counts()` is for categorical columns — it counts how often each unique value appears
- `groupby('Category')['Sales'].sum()` reads as: "Group by Category, then for each group, sum the Sales column" — this gives total revenue per category
- `pd.to_datetime()` converts a text date like `"2023-01-15"` into a real date object so you can extract months, years, and days from it
- `dt.to_period('M')` extracts the year-month from each date — turning `2023-01-15` into `2023-01`
- `groupby('Month').size()` counts the number of rows (orders) in each month

**Observations you should note after this step:**
- Which category has the highest total sales?
- Is there a region consistently ahead in average sales?
- Is there a visible monthly trend — are orders growing, declining, or seasonal?

---

## Step 5 — Matplotlib Practice

Now you have 3 clear observations. It is time to visualise them. You will create one chart for each type of question — comparison, trend, and distribution.

![Bar charts compare categories side by side, line charts show change over time, and histograms show how one numeric column spreads across ranges — match the shape to the question](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-three-chart-types.png)

### 5a — Bar Chart: Category Sales Comparison

Use a bar chart when you want to compare a single number (like total sales) across different categories side by side.

```python
# ── Bar chart: Total Sales by Category ──────────────────────────────────────

category_sales = df.groupby('Category')['Sales'].sum().reset_index()
# group by Category, sum Sales, and reset_index() converts the result back to a clean DataFrame

plt.figure(figsize=(8, 5))                              # create a canvas 8 inches wide and 5 inches tall

plt.bar(category_sales['Category'],                    # x-axis: category names
        category_sales['Sales'],                       # y-axis: total sales for each category
        color=['#4C72B0', '#DD8452', '#55A868'],       # one distinct colour per bar
        edgecolor='white',                             # white border between bars for visual clarity
        width=0.5)                                     # bar width (0 to 1 scale)

plt.title('Technology Leads in Total Sales', fontsize=14)   # insight-first title — tells the story upfront
plt.xlabel('Product Category', fontsize=11)                  # label for x-axis
plt.ylabel('Total Sales (₹)', fontsize=11)                  # label for y-axis
plt.xticks(fontsize=10)                                      # increase font size of x-axis labels for readability
plt.yticks(fontsize=10)                                      # increase font size of y-axis labels
plt.tight_layout()                                           # auto-adjust layout so nothing is cut off
plt.show()                                                   # display the chart
```

**How the code works:**
- `reset_index()` after a `groupby` turns the grouped result into a clean DataFrame with standard numbered rows — easier to pass into `plt.bar()`
- `plt.bar(x, y)` draws one vertical bar for each value in the `x` list, with height equal to the corresponding `y` value
- The `color` list assigns a different colour to each bar — making it easy to tell them apart at a glance
- The title *"Technology Leads in Total Sales"* communicates the finding immediately, instead of a generic *"Sales by Category"*

---

### 5b — Line Chart: Monthly Order Trend

Use a line chart when your data has a time dimension — you want to show how something changes across months or years.

```python
# ── Prepare monthly order data ───────────────────────────────────────────────

monthly_orders = df.groupby('Month').size().reset_index(name='OrderCount')
# group by Month, count rows per month, and name the count column 'OrderCount'

monthly_orders['Month'] = monthly_orders['Month'].astype(str)
# convert Month from Period type to string so matplotlib can read it on the x-axis

# ── Line chart: Monthly Order Volume ────────────────────────────────────────

plt.figure(figsize=(12, 5))                             # wide canvas so monthly labels do not overlap

plt.plot(monthly_orders['Month'],                      # x-axis: month labels (strings)
         monthly_orders['OrderCount'],                 # y-axis: number of orders per month
         marker='o',                                   # show a dot at each monthly data point
         color='steelblue',                            # line colour
         linewidth=2,                                  # line thickness
         markersize=5)                                 # size of the dot at each point

plt.title('Orders Spike Every Year-End — Q4 Is Strongest', fontsize=14)   # insight-first title
plt.xlabel('Month', fontsize=11)                                            # x-axis label
plt.ylabel('Number of Orders', fontsize=11)                                 # y-axis label
plt.xticks(rotation=45, ha='right', fontsize=8)                            # rotate month labels so they don't overlap
plt.tight_layout()                                                          # auto-fix spacing
plt.show()                                                                  # display the chart
```

**How the code works:**
- `.astype(str)` converts the `Period` objects (like `2023-01`) into plain strings that Matplotlib can display on the x-axis
- `rotation=45` tilts the x-axis labels at 45 degrees — without this, all the month labels crash into each other
- `ha='right'` (horizontal alignment = right) aligns each rotated label to the right so it points toward its tick mark
- The insight-first title tells the audience the main finding before they even read the chart

---

### 5c — Histogram: Distribution of Individual Sale Values

Use a histogram when you want to understand how a single numeric column is spread — are most sales small, or are they evenly distributed?

```python
# ── Histogram: Distribution of individual order sale values ─────────────────

plt.figure(figsize=(8, 5))                             # set canvas size

plt.hist(df['Sales'],                                  # the column whose distribution we want to see
         bins=30,                                      # divide the full range into 30 equal buckets
         color='mediumseagreen',                       # bar fill colour
         edgecolor='white')                            # white border between bars for clarity

plt.title('Most Orders Are Small Ticket — Few Are High Value', fontsize=14)  # insight-first title
plt.xlabel('Sale Value per Order (₹)', fontsize=11)                           # x-axis: the numeric range
plt.ylabel('Number of Orders (Frequency)', fontsize=11)                       # y-axis: how many orders fall in each range
plt.tight_layout()                                                             # prevent clipping
plt.show()                                                                     # display the chart
```

**How the code works:**
- `plt.hist(df['Sales'], bins=30)` automatically divides the range of `Sales` into 30 equal segments and counts how many rows fall in each
- A tall bar on the left side means many orders have low sale values — this is very common in retail data
- A thin tail stretching to the right means a few very high-value orders exist (potential bulk orders)
- This shape — many small values and a long right tail — is called a **right-skewed distribution** and is important to understand before computing averages

---

## Step 6 — Basic Plotly Practice

You have already seen the story in Matplotlib charts. Now recreate the **most important chart** — the Category Sales bar chart — as an interactive Plotly chart so stakeholders can hover and explore it themselves.

- **Official Definition:** **Plotly Express** is a high-level Python library that creates interactive, browser-based charts using a single function call.
- **In Simple Words:** Matplotlib prints a photograph of your chart. Plotly makes a live digital version — you can hover over any bar to see the exact number, zoom into a region, and click legend items to show or hide them.
- **Real-Life Example:** A news website's interactive election result chart — where you hover over a state and its vote percentage pops up — is the kind of chart Plotly produces.

![Matplotlib gives publication-ready static figures; Plotly adds hover tooltips, zoom, and legend toggles — one dataset, two audiences](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-plotly-interactive.png)

```python
# ── Prepare category sales summary ──────────────────────────────────────────

category_sales = df.groupby('Category')['Sales'].sum().reset_index()
# group by Category, sum Sales, and reset index to get a flat DataFrame

category_sales.columns = ['Category', 'Total Sales']
# rename the columns clearly so Plotly labels them correctly on the chart

# ── Interactive bar chart with Plotly ────────────────────────────────────────

fig = px.bar(category_sales,                           # the DataFrame to plot from
             x='Category',                             # column for the x-axis
             y='Total Sales',                          # column for the y-axis
             color='Category',                         # give each bar a different colour using the Category column
             text='Total Sales',                       # show the sales number directly on each bar
             title='Total Sales by Category (Interactive)')  # chart title

fig.update_traces(texttemplate='₹%{text:,.0f}',        # format the on-bar number as ₹ with comma separators
                  textposition='outside')              # place the number above each bar

fig.update_layout(showlegend=False,                    # hide the legend since bar labels already identify each category
                  xaxis_title='Product Category',      # clear x-axis label
                  yaxis_title='Total Sales (₹)',       # clear y-axis label
                  font=dict(size=13))                  # increase base font size for readability

fig.show()                                             # open the interactive chart in the browser
```

**How the code works:**
- `px.bar()` reads directly from a DataFrame — you just tell it which column goes on which axis
- `color='Category'` automatically assigns a different colour to each category and adds a legend (which we hide since the x-axis already labels everything)
- `text='Total Sales'` adds a number directly on or above each bar — very useful in presentations
- `texttemplate='₹%{text:,.0f}'` formats the number with a Rupee symbol and comma separators (e.g., `₹1,23,456`)
- `fig.update_layout()` lets you customise any aspect of the chart appearance after it is created

---

## Step 7 — Chart Selection Practice

Before drawing any chart, you must ask yourself: **"What question am I answering?"** Each question type has a matching chart type.

![Decision guide: comparisons → bar chart, trends over time → line, distributions → histogram, two numeric columns → scatter, shares of a small set of categories → pie or donut](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-chart-selection-matrix.png)

| Question Type | Example Question | Best Chart |
|---|---|---|
| **Comparison** | Which category has the highest sales? | Bar Chart |
| **Trend over time** | How did orders change month by month? | Line Chart |
| **Distribution** | Are most orders small or large in value? | Histogram |
| **Relationship** | Do high-discount orders always have lower profit? | Scatter Plot |
| **Part of a whole** | What share of total orders does each region hold? | Pie / Donut Chart (only if ≤ 5 categories) |

**Practice Questions — Match the Chart:**

Work through these questions and decide the correct chart type before plotting:

1. *"How do the four regions compare in terms of total profit?"* → **Bar Chart** (comparing 4 categories side by side)
2. *"How has the number of orders changed each month for the past year?"* → **Line Chart** (trend over an ordered time axis)
3. *"Are most discounts small (0–10%) or large (30–50%)?"* → **Histogram** (distribution of one numeric column)
4. *"Is there a pattern between Discount given and Profit earned?"* → **Scatter Plot** (relationship between two numeric columns)
5. *"What percentage of total orders came from each region?"* → **Pie Chart** (only 4 regions — within the 5-category limit)

**Common Mistakes to Avoid:**

- Using a **line chart for categories with no time order** — a line chart implies a sequence; if your x-axis is just category names, use a bar chart
- Using a **pie chart with more than 5 slices** — beyond 5, the slices become too thin to compare; switch to a bar chart
- Using a **bar chart to show the distribution of one numeric column** — that question needs a histogram, not a bar chart
- Using a **histogram to compare two categories** — histograms are for one column; use a grouped bar chart for comparisons

---

## Step 8 — Chart Labelling and Formatting

A chart without labels is like a map without a legend — the viewer has no idea what they are looking at. Every chart you produce must have these five elements:

![Insight-first title, axis labels, colour that separates series, sensible defaults, and tight layout together make a chart self-explanatory](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-chart-five-elements.png)

| Element | Why It Matters | Matplotlib Command |
|---|---|---|
| **Title** | Tells the viewer what the chart is about — ideally the insight, not just the variable name | `plt.title('...')` |
| **X-axis Label** | Names what is on the horizontal axis | `plt.xlabel('...')` |
| **Y-axis Label** | Names what is on the vertical axis | `plt.ylabel('...')` |
| **Colour** | Distinguishes categories visually | `color=` or `color=[...]` |
| **Tight Layout** | Prevents labels from being cut off at the edges | `plt.tight_layout()` |

**Before and After — Formatting a Bar Chart Properly:**

```python
# ── BEFORE: An unlabelled, unformatted chart (never submit this) ─────────────

plt.bar(['Furniture', 'Office Supplies', 'Technology'], [100000, 150000, 200000])
plt.show()                                             # no title, no axis labels, no context

# ── AFTER: A properly labelled, formatted chart ──────────────────────────────

categories  = ['Furniture', 'Office Supplies', 'Technology']   # category names for x-axis
sales_total = [100000, 150000, 200000]                          # total sales for each category

plt.figure(figsize=(8, 5))                             # set a clear canvas size — default is often too small

plt.bar(categories,                                    # x-axis: category names
        sales_total,                                   # y-axis: sales values
        color=['#4C72B0', '#DD8452', '#55A868'],       # distinct colour per bar
        edgecolor='white',                             # white gap between bars for clarity
        width=0.55)                                    # slightly narrower bars with breathing space between them

plt.title('Technology Drives the Most Revenue', fontsize=14, fontweight='bold')  # insight-first bold title
plt.xlabel('Product Category', fontsize=12)            # x-axis label with readable font size
plt.ylabel('Total Sales (₹)', fontsize=12)             # y-axis label with Rupee symbol
plt.xticks(fontsize=11)                                # increase x-axis tick label size
plt.yticks(fontsize=11)                                # increase y-axis tick label size
plt.tight_layout()                                     # auto-fix layout spacing
plt.show()                                             # display the chart
```

**How the code works:**
- `fontsize=14` and `fontweight='bold'` on the title make it stand out and draw the eye first
- `edgecolor='white'` adds a thin white line between bars — this separates them visually without needing gaps
- `width=0.55` controls how wide each bar is — a width below 1 leaves space between bars making them easier to read
- Every chart submitted in this course **must** have a title, x-label, y-label, and appropriate colours — failing to format is treated as an incomplete chart

---

## Step 9 — Short Insight Writing

Every chart must be followed by **1–2 sentences** that explain what the chart shows. This is where data becomes communication — you are translating numbers into a human message.

- **Official Definition:** A **chart insight** is a written sentence that states the key finding from a visualisation in plain language, often including a follow-up recommendation or question.
- **In Simple Words:** A chart says "here is what the data looks like." Your insight says "here is what this *means*."
- **Real-Life Example:** If a fitness app shows a graph of your daily steps going down every weekend, the insight would be: *"You walk significantly fewer steps on weekends — consider a morning walk routine on Saturdays."*

![Pair every chart with 1–2 sentences: state the pattern, then why it matters or what to do next — visuals plus narrative complete the story](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session12.1/session12.1-insight-writing.png)

**Structure of a Good Insight Statement:**

> **[What the chart shows]** + **[Why it matters or what it implies]**

**Examples from this session's charts:**

**After the Category Sales Bar Chart:**
> *"Technology has the highest total sales among all three categories, contributing nearly 37% of overall revenue. This suggests the business is heavily dependent on technology products — a risk if that category faces supply disruptions."*

**After the Monthly Orders Line Chart:**
> *"Order volume shows a clear seasonal spike in October–December every year, likely driven by festive season demand. The business should plan higher inventory and staffing in Q4 to handle this surge."*

**After the Sales Distribution Histogram:**
> *"The majority of individual orders are low-value — most fall below ₹500. A small number of very high-value orders (₹5,000+) skew the average upward, so median sale value is a better indicator of typical order size than the mean."*

**Common Mistakes in Insight Writing:**

- **Just describing the chart:** *"The bar chart shows sales for three categories"* — this adds nothing; the viewer can already see the chart
- **Too long:** An insight is 1–2 sentences, not a paragraph — keep it sharp and specific
- **No implication:** Always answer "so what?" — what does this mean for the business or the analysis?

---

## Step 10 — Final Mini Output

Now you assemble everything into a clean, complete notebook-style solution. This is the deliverable you would share with a manager or submit as a project.

```python
# ════════════════════════════════════════════════════════════════════════════
#  FINAL MINI OUTPUT — Superstore Data Analysis
#  Includes: data load, readiness check, 3 matplotlib charts, 1 plotly chart,
#            and short written insights under each chart
# ════════════════════════════════════════════════════════════════════════════

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load and inspect ──────────────────────────────────────────────────────

df = pd.read_csv('superstore_orders.csv')              # load dataset
print(f"Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")   # confirm shape

# ── 2. Quick readiness check ─────────────────────────────────────────────────

df = df.drop_duplicates()                              # remove duplicate rows
df['Order Date'] = pd.to_datetime(df['Order Date'])    # convert Order Date to datetime
df['Month'] = df['Order Date'].dt.to_period('M')       # extract year-month
print(f"Missing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")  # only print columns that have missing values

# ── 3. Chart 1: Bar Chart — Category Sales ───────────────────────────────────

category_sales = df.groupby('Category')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(category_sales['Category'],
        category_sales['Sales'],
        color=['#4C72B0', '#DD8452', '#55A868'],
        edgecolor='white', width=0.5)
plt.title('Technology Leads in Total Sales', fontsize=14, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales (₹)', fontsize=12)
plt.tight_layout()
plt.show()

# Insight:
print("""
INSIGHT 1:
Technology generates the highest revenue among all categories.
Furniture lags behind significantly, indicating either lower demand or lower price points.
""")

# ── 4. Chart 2: Line Chart — Monthly Order Trend ────────────────────────────

monthly = df.groupby('Month').size().reset_index(name='Orders')
monthly['Month'] = monthly['Month'].astype(str)        # convert Period to string for matplotlib

plt.figure(figsize=(12, 5))
plt.plot(monthly['Month'], monthly['Orders'],
         marker='o', color='steelblue', linewidth=2, markersize=4)
plt.title('Q4 Consistently Sees the Highest Order Volume', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.tight_layout()
plt.show()

# Insight:
print("""
INSIGHT 2:
Orders spike in October–December each year, suggesting strong Q4 festive season demand.
Q1 shows a consistent dip — this could be a good time for off-season promotions.
""")

# ── 5. Chart 3: Histogram — Sales Distribution ───────────────────────────────

plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=30, color='mediumseagreen', edgecolor='white')
plt.title('Most Orders Are Small Value — Long Right Tail Indicates Bulk Orders', fontsize=13, fontweight='bold')
plt.xlabel('Sale Value per Order (₹)', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.tight_layout()
plt.show()

# Insight:
print("""
INSIGHT 3:
The majority of orders have low sale values, with very few high-value bulk orders.
The median order value is a more accurate measure of typical order size than the mean,
since the mean is pulled upward by those rare large orders.
""")

# ── 6. Chart 4: Interactive Plotly Bar Chart ─────────────────────────────────

category_sales.columns = ['Category', 'Total Sales']

fig = px.bar(category_sales,
             x='Category', y='Total Sales',
             color='Category',
             text='Total Sales',
             title='Total Sales by Category — Hover for Exact Values')
fig.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
fig.update_layout(showlegend=False,
                  xaxis_title='Product Category',
                  yaxis_title='Total Sales (₹)',
                  font=dict(size=13))
fig.show()                                             # opens in browser as interactive chart

# ── 7. Final Summary ─────────────────────────────────────────────────────────

print("""
FINAL SUMMARY
─────────────────────────────────────────────────────────────────────────────
1. Technology is the top revenue-generating category.
2. Order volume peaks every Q4 — inventory and staffing should scale accordingly.
3. Most orders are low-value; the business likely relies on volume, not large orders.
4. Furniture has the lowest revenue and may benefit from promotions or repricing.
─────────────────────────────────────────────────────────────────────────────
""")
```

**How the code works:**
- The final output block brings together all earlier steps into one clean, top-to-bottom notebook
- Each chart is followed immediately by a `print()` block with the insight — this is how notebooks are structured for presentation
- The `f-string` in `print(f"Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")` dynamically inserts the actual row and column count into the message
- The `FINAL SUMMARY` section at the end gives a manager-friendly overview — 4 bullet points covering the most important findings

---

## Key Takeaways

- **Always inspect before you visualise** — use `df.shape`, `df.info()`, `df.isnull().sum()`, and `df.describe()` as a standard checklist every time you open a new dataset; a chart built on dirty data is misleading.
- **`groupby()` is your most powerful summary tool** — pairing it with `.sum()`, `.mean()`, or `.size()` lets you turn thousands of rows into clear, chart-ready summaries.
- **Match the chart to the question** — bar for comparison, line for trend, histogram for distribution, scatter for relationship; using the wrong chart type hides the insight instead of showing it.
- **Formatting is not optional** — every chart must have an insight-first title, labelled axes, and appropriate colours; an unlabelled chart is an incomplete chart.
- **Every chart needs a written insight** — 1–2 sentences explaining what the chart means and why it matters; this is what separates a data analyst from someone who just runs code.

In the upcoming sessions, we will move from single-chart practice to building complete multi-chart dashboards, working with larger and messier real-world datasets, and using AI tools to speed up the EDA and insight-writing process.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Description |
|---|---|
| `import pandas as pd` | Load the pandas library for data handling |
| `pd.read_csv('file.csv')` | Read a CSV file into a DataFrame |
| `df.shape` | Returns `(rows, columns)` — size of the dataset |
| `df.head()` / `df.tail()` | Preview the first / last 5 rows |
| `df.info()` | Column names, data types, and non-null counts in one view |
| `df.dtypes` | Data type of every column |
| `df.isnull().sum()` | Count of missing values per column |
| `df.duplicated().sum()` | Count of exact duplicate rows |
| `df.drop_duplicates()` | Remove all duplicate rows |
| `df['col'].fillna(value)` | Replace missing values with a given value |
| `df.dropna(subset=[...])` | Drop rows where specific columns are missing |
| `df['col'].value_counts()` | Frequency count of each unique value in a column |
| `df.groupby('col')['num'].sum()` | Total of a numeric column grouped by a category |
| `df.groupby('col')['num'].mean()` | Average of a numeric column grouped by a category |
| `df.groupby('col').size()` | Count the number of rows in each group |
| `pd.to_datetime(df['col'])` | Convert a text column to proper datetime type |
| `df['col'].dt.to_period('M')` | Extract the year-month from a datetime column |
| `plt.figure(figsize=(w, h))` | Set the canvas width and height in inches |
| `plt.bar(x, y)` | Draw a vertical bar chart |
| `plt.plot(x, y)` | Draw a line chart |
| `plt.hist(col, bins=n)` | Draw a histogram with n bins |
| `plt.title('...')` | Add a title to the chart |
| `plt.xlabel('...')` / `plt.ylabel('...')` | Label the x and y axes |
| `plt.xticks(rotation=45)` | Rotate x-axis labels to avoid overlap |
| `plt.tight_layout()` | Auto-adjust layout to prevent label clipping |
| `plt.show()` | Display the finished chart |
| `import plotly.express as px` | Load Plotly Express for interactive charts |
| `px.bar(df, x=, y=, color=)` | Create an interactive bar chart from a DataFrame |
| `fig.update_traces(texttemplate=...)` | Format the text labels shown on chart bars |
| `fig.update_layout(...)` | Customise title, axis labels, font, and legend of a Plotly chart |
| `fig.show()` | Open the Plotly chart in a browser as an interactive chart |
| **EDA** | Exploratory Data Analysis — inspect before you analyse |
| **Missing Value (NaN)** | A cell in the dataset with no recorded data |
| **Duplicate Row** | A row that is an exact copy of another row |
| **groupby()** | Pandas operation that groups rows by a column and applies a function |
| **Right-Skewed Distribution** | A shape where most values cluster low and a long tail extends to the right |
| **Insight Statement** | A 1–2 sentence explanation of what a chart means and why it matters |
| **Insight-First Title** | A chart title that states the finding, not just the variable name |
| **Bins (Histogram)** | Equal-width ranges used to group numeric values in a histogram |
| **Interactive Chart** | A chart where the viewer can hover, zoom, and filter — produced by Plotly |
