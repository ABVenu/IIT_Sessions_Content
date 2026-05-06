# Assignment Subjective: Plotting & Storytelling with Data
**Difficulty:** Medium  
**Submission Type:** Coding implementation in a single Python file


## Practical Task: Build a Mini EDA and Data Story Report

You are working as a junior data analyst for a small online learning platform. The team has collected weekly learner activity data and wants you to inspect the data, create useful charts, and write a short data story that explains what the charts mean.

Create a Python file named `eda_story_report.py` and complete the following task.

---

## Dataset

Use the following data directly inside your Python file as a pandas DataFrame. Do not load an external CSV.

```python
data = {
    "week": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"],
    "course": ["Python", "Python", "SQL", "SQL", "Python", "SQL", "Python", "SQL"],
    "active_learners": [120, 135, 98, 110, 160, 150, 175, 145],
    "avg_quiz_score": [68, 72, 64, 70, 78, 76, 82, 74],
    "watch_hours": [240, 270, 190, 220, 330, 310, 360, 295]
}
```

---

## Requirements

1. Create a pandas DataFrame from the given data.
2. Perform basic EDA by printing:
   - DataFrame shape
   - First five rows
   - Column information
   - Missing value count for each column
   - Summary statistics for numeric columns
3. Create the following Matplotlib charts:
   - A line chart showing `active_learners` across `week`
   - A bar chart comparing total `watch_hours` by `course`
   - A histogram showing the distribution of `avg_quiz_score`
4. Add proper titles, x-axis labels, y-axis labels, and `plt.tight_layout()` to each chart.
5. Add one annotation on the line chart to highlight the highest learner activity week.
6. Create one Plotly scatter plot with:
   - `watch_hours` on the x-axis
   - `avg_quiz_score` on the y-axis
   - colour based on `course`
7. At the end of the file, print a short data story of 4-6 lines explaining:
   - What changed across the weeks
   - Which course had higher total watch hours
   - Whether higher watch hours seem connected with higher quiz scores
   - One recommendation for the learning team

---

## Expected Output

Your script should:

- Print EDA outputs in the terminal.
- Display three Matplotlib charts.
- Open one interactive Plotly scatter plot.
- Print a clear 4-6 line data story.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor/answer box in the LMS.

---

## Answer Explanation

An ideal solution should create the DataFrame, inspect it with pandas commands, use Matplotlib for static charts, use Plotly for an interactive scatter plot, and finish with a short written insight.

One possible complete solution is:

```python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


data = {
    "week": ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8"],
    "course": ["Python", "Python", "SQL", "SQL", "Python", "SQL", "Python", "SQL"],
    "active_learners": [120, 135, 98, 110, 160, 150, 175, 145],
    "avg_quiz_score": [68, 72, 64, 70, 78, 76, 82, 74],
    "watch_hours": [240, 270, 190, 220, 330, 310, 360, 295],
}

df = pd.DataFrame(data)

print("Shape:")
print(df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())


highest_activity_index = df["active_learners"].idxmax()
highest_activity_week = df.loc[highest_activity_index, "week"]
highest_activity_value = df.loc[highest_activity_index, "active_learners"]

plt.figure(figsize=(8, 4))
plt.plot(df["week"], df["active_learners"], marker="o", color="steelblue", linewidth=2)
plt.annotate(
    "Highest activity",
    xy=(highest_activity_week, highest_activity_value),
    xytext=("W5", highest_activity_value - 15),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=9,
    color="red",
)
plt.title("Learner Activity Peaked in Week 7")
plt.xlabel("Week")
plt.ylabel("Active Learners")
plt.tight_layout()
plt.show()


watch_hours_by_course = df.groupby("course")["watch_hours"].sum()

plt.figure(figsize=(7, 4))
plt.bar(watch_hours_by_course.index, watch_hours_by_course.values, color=["#4C72B0", "#55A868"])
plt.title("Total Watch Hours by Course")
plt.xlabel("Course")
plt.ylabel("Total Watch Hours")
plt.tight_layout()
plt.show()


plt.figure(figsize=(7, 4))
plt.hist(df["avg_quiz_score"], bins=5, color="mediumseagreen", edgecolor="white")
plt.title("Distribution of Average Quiz Scores")
plt.xlabel("Average Quiz Score")
plt.ylabel("Number of Weeks")
plt.tight_layout()
plt.show()


fig = px.scatter(
    df,
    x="watch_hours",
    y="avg_quiz_score",
    color="course",
    title="Watch Hours vs Average Quiz Score",
)
fig.show()


python_watch_hours = watch_hours_by_course["Python"]
sql_watch_hours = watch_hours_by_course["SQL"]
higher_watch_course = "Python" if python_watch_hours > sql_watch_hours else "SQL"

print("\nData Story:")
print("Learner activity generally increased across the weeks, with the highest activity in Week 7.")
print(f"{higher_watch_course} had higher total watch hours across the given records.")
print("The scatter plot suggests that weeks with higher watch hours also tend to have higher quiz scores.")
print("This indicates that learner engagement may be connected with better quiz performance.")
print("The learning team should study the high-engagement weeks and repeat similar activities in future weeks.")
```

Alternative approaches are acceptable if they satisfy all requirements, use the same dataset correctly, and produce clear EDA outputs, charts, and a meaningful data story.
