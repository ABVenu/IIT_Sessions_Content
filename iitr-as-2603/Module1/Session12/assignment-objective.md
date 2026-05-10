# Assignment — Objective: Plotting & Storytelling with Data

> **Total Questions:** 10 | **MCQs:** 6 (4 Easy + 2 Moderate) | **MSQs:** 4 (2 Moderate + 2 Hard)  
> Ordered progressively: Easy → Moderate → Hard

---

## MCQ — Easy (Questions 1–4)

---

**Question 1**

Riya receives a new `sales_data.csv` file from her manager. Before creating any chart or drawing conclusions, what should she do first as part of EDA?

- A. Directly create a dashboard in Plotly
- B. Inspect the data shape, first few rows, column types, and missing values
- C. Delete all rows with missing values immediately
- D. Use a pie chart for every column

**Correct Answer:** B

**Answer Explanation:**  
The first EDA step is to inspect the dataset using commands such as `df.shape`, `df.head()`, `df.tail()`, `df.info()`, and `df.isnull().sum()`. This helps understand the structure, data types, missing values, and possible issues before analysis. Option A skips inspection. Option C is risky because missing values should be investigated before deletion. Option D is incorrect because chart choice depends on the question and data type.

---

**Question 2**

A marketing team wants to show how website visits changed from January to June. Which chart is most suitable?

- A. Line chart
- B. Histogram
- C. Pie chart
- D. Scatter plot

**Correct Answer:** A

**Answer Explanation:**  
A line chart is best when showing change over time because the x-axis has a natural order. A histogram shows the distribution of one numeric column, not a time trend. A pie chart shows parts of a whole. A scatter plot shows relationships between two numeric variables.

---

**Question 3**

During EDA, Aman runs:

```python
print(df.isnull().sum())
```

What does this command tell him?

- A. The number of duplicate rows in the dataset
- B. The number of missing values in each column
- C. The average value of each numeric column
- D. The data type of each column only

**Correct Answer:** B

**Answer Explanation:**  
`df.isnull().sum()` counts missing values column-wise. It helps identify columns where data was not recorded or is unavailable. Duplicate rows require other methods. Averages are shown by `df.describe()`. Data types are mainly shown by `df.info()`.

---

**Question 4**

A store owner wants to compare total revenue from four product categories: Laptop, Phone, Tablet, and Watch. Which Matplotlib function should be used?

- A. `plt.hist()`
- B. `plt.plot()`
- C. `plt.bar()`
- D. `plt.annotate()`

**Correct Answer:** C

**Answer Explanation:**  
`plt.bar()` is used to compare values across categories. Product categories are unordered groups, so a bar chart is suitable. `plt.hist()` shows distribution of one numeric column. `plt.plot()` is mainly used for trends over ordered values such as time. `plt.annotate()` adds labels or notes to an existing chart.

---

## MCQ — Moderate (Questions 5–6)

---

**Question 5**

A salary histogram shows most employees earning between Rs. 30,000 and Rs. 60,000, but a few executives earn above Rs. 5,00,000. Which statement is most accurate?

- A. The distribution is left skewed and the mean is less than the median
- B. The distribution is right skewed and the mean is likely greater than the median
- C. The distribution is symmetric and mean equals median exactly
- D. The distribution has no outliers because salaries are numeric

**Correct Answer:** B

**Answer Explanation:**  
The few very high salaries create a long right tail, so the distribution is right or positively skewed. These high values pull the mean upward, making the mean greater than the median. Option A describes left skew. Option C is incorrect because the distribution is not balanced. Option D is wrong because numeric columns can definitely contain outliers.

---

**Question 6**

Neha wants her audience to hover over points, zoom into a time range, and interact with the chart in a browser. Which library is better suited for this requirement?

- A. Matplotlib, because it is mainly used for interactive browser dashboards
- B. Plotly, because it supports hover, zoom, and browser-based interactivity
- C. pandas only, because it replaces all plotting libraries
- D. `df.describe()`, because it creates an interactive chart

**Correct Answer:** B

**Answer Explanation:**  
Plotly is designed for interactive, browser-based visualisations with hover tooltips, zoom, pan, and filtering. Matplotlib is better for static charts used in reports or polished outputs. pandas helps with data handling and can support plotting, but it does not replace Plotly for interactive dashboards. `df.describe()` gives summary statistics, not charts.

---

## MSQ — Moderate (Questions 7–8)

*Select all correct options.*

---

**Question 7**

Which commands help inspect a newly loaded pandas DataFrame during EDA? *(Select all that apply)*

- A. `df.head()`
- B. `df.info()`
- C. `df.isnull().sum()`
- D. `plt.show()`

**Correct Answers:** A, B, C

**Answer Explanation:**  
`df.head()` previews the first rows, `df.info()` shows column names, data types, and non-null counts, and `df.isnull().sum()` counts missing values. These are all EDA inspection commands. `plt.show()` displays a chart after it has been created, but it does not inspect the raw DataFrame structure.

---

**Question 8**

Which chart choices are appropriate? *(Select all that apply)*

- A. Use a line chart to show stock price over dates
- B. Use a histogram to show the distribution of student marks
- C. Use a scatter plot to study the relationship between study hours and marks
- D. Use a line chart to compare unordered product categories

**Correct Answers:** A, B, C

**Answer Explanation:**  
A line chart is suitable for time-based trends such as stock price over dates. A histogram is suitable for the distribution of one numeric column such as marks. A scatter plot is suitable for relationships between two numeric columns such as study hours and marks. A line chart should not be used for unordered categories because it implies sequence or continuity; a bar chart is better for categories.

---

## MSQ — Hard (Questions 9–10)

*Select all correct options.*

---

**Question 9**

A learner creates a chart titled "Monthly Sales" with many gridlines, unnecessary colours, and no explanation. Which changes would improve the data story? *(Select all that apply)*

- A. Replace the title with an insight-first title such as "Sales Grew 40% in Q2"
- B. Remove visual clutter that does not help the audience understand the message
- C. Add an annotation to highlight an important campaign launch or sales spike
- D. Hide the conclusion so the audience must guess the insight

**Correct Answers:** A, B, C

**Answer Explanation:**  
A strong data story combines data, visuals, and narrative. An insight-first title leads with the conclusion, removing clutter improves readability, and annotations highlight important moments directly on the chart. Hiding the conclusion is poor storytelling because the audience should not be forced to guess the key insight.

---

**Question 10**

During EDA, a learner sees that a delivery-time column has a mean much higher than the median. The histogram has most values clustered on the left and a long tail to the right. Which conclusions or next steps are valid? *(Select all that apply)*

- A. The distribution is likely right skewed
- B. A few very high delivery times may be pulling the mean upward
- C. The learner should check min/max values in `df.describe()` to investigate possible outliers
- D. The median may describe a typical delivery time better than the mean

**Correct Answers:** A, B, C, D

**Answer Explanation:**  
A long right tail with mean greater than median indicates right skew. Very high values on the right can pull the mean upward. Checking `df.describe()` helps confirm extreme min/max values and possible outliers. In skewed data, the median is often a better measure of the typical value because it is less affected by extreme values.
