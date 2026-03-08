# Matplotlib: Basic Plotting

## What You’ll Learn

In this lesson, you’ll learn how to visualize data using Matplotlib, Python’s foundational plotting library. You’ll understand how to create line plots, scatter plots, and bar charts, how to label axes and add titles, and how to apply basic aesthetic improvements. Visualization is not decorative—it is a core analytical tool used to detect patterns, debug models, and communicate insights clearly.

![Matplot](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/7a7e4eb1-1cb0-48bd-92d7-e825c8739f45/BtvxsuojRjmlVuEz.png)

---

## 1. Why Visualization Matters in AI

Before building a model, you must understand your data. After training a model, you must understand its behavior.

Visualization helps you:
- Detect trends
- Identify outliers
- Compare groups
- Inspect distributions
- Diagnose errors

Many modeling mistakes can be caught early by simply plotting the data.

Matplotlib is widely used because it provides:
- Fine-grained control
- Reproducible visualizations
- Integration with NumPy and Pandas
- Production-level customization

---

## 2. Getting Started with Matplotlib

Matplotlib is typically imported as:

```python
import matplotlib.pyplot as plt
````

The general plotting workflow:

1. Prepare data
2. Create a plot
3. Add labels and titles
4. Display the figure

```python
plt.plot([1, 2, 3], [2, 4, 6])
plt.show()
```

This minimal structure underlies all Matplotlib visualizations.

---

## 3. Line Plots: Showing Trends Over Time

### When to Use Line Plots

Line plots are best for:

* Time series data
* Trends across ordered values
* Model performance across epochs

Example:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot")
plt.show()
```

This connects points in order, making trends visible.

In AI:

* Training loss vs epoch
* Accuracy over time
* Learning rate schedules

---

## 4. Scatter Plots: Understanding Relationships

### When to Use Scatter Plots

Scatter plots show relationships between two variables.

Example:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Scatter Plot Example")
plt.show()
```

Scatter plots are useful for:

* Checking correlations
* Detecting clusters
* Identifying outliers

In AI:

* Visualizing predictions vs actual values
* Inspecting feature interactions
* Exploring embedding projections

---

## 5. Bar Charts: Comparing Categories

### When to Use Bar Charts

Bar charts are ideal for comparing discrete categories.

Example:

```python
categories = ["A", "B", "C"]
values = [10, 20, 15]

plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart Example")
plt.show()
```

Bar charts are commonly used for:

* Class distribution
* Model comparison
* Aggregated statistics

They make categorical differences immediately visible.

---

## 6. Labeling and Titles: Making Plots Understandable

A plot without labels is ambiguous.

Always include:

* X-axis label
* Y-axis label
* Title

Example:

```python
plt.plot(x, y)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Time")
plt.show()
```

Clear labeling ensures:

* Reproducibility
* Interpretability
* Professional presentation

In collaborative environments, unlabeled plots cause confusion.

---

## 7. Basic Aesthetics: Improving Clarity

Matplotlib allows simple adjustments that improve readability.

### Adding Gridlines

```python
plt.plot(x, y)
plt.grid(True)
plt.show()
```

Gridlines help interpret values visually.

---

### Changing Line Style and Markers

```python
plt.plot(x, y, linestyle="--", marker="o")
plt.show()
```

Markers highlight individual data points.

---

### Adjusting Figure Size

```python
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.show()
```

This improves readability in reports and presentations.

---

### Adding a Legend

When plotting multiple lines:

```python
plt.plot(x, y, label="Line 1")
plt.plot(x, [i*1.5 for i in y], label="Line 2")
plt.legend()
plt.show()
```

Legends clarify what each line represents.

---

## 8. A Practical AI Example

```python
import numpy as np
import matplotlib.pyplot as plt

epochs = range(1, 11)
loss = np.random.rand(10)

plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker="o")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Model Training Loss")
plt.grid(True)
plt.show()
```

This type of plot is used constantly in machine learning workflows.

---

## 9. Common Beginner Mistakes

* Forgetting `plt.show()`
* Not labeling axes
* Overcrowding plots
* Misinterpreting scatter density
* Plotting unsorted data when order matters

Visualization is powerful, but clarity must be intentional.

---

## Key Takeaways

Matplotlib enables clear and flexible data visualization. Line plots show trends, scatter plots reveal relationships, and bar charts compare categories. Labels and titles make plots interpretable, and basic aesthetics improve clarity. Visualization is a diagnostic tool in AI—not just a presentation layer.

**Mental model:**
Line plots show change.
Scatter plots show relationships.
Bar charts compare groups.
Labels create clarity.
Aesthetics improve understanding.

---

## Additional Reading

* Matplotlib Official Documentation:
  [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)

* Matplotlib Quick Start Guide:
  [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

* Visualizing Data with Python (Google Developers):
  [https://developers.google.com/machine-learning/crash-course/data-prep/visualizing-data](https://developers.google.com/machine-learning/crash-course/data-prep/visualizing-data)