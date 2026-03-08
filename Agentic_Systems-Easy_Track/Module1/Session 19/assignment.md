# **Assignment: Matplotlib Basic Plotting**

---

## **Question 1. (MCQ)**

What is the correct import statement for using Matplotlib’s plotting interface?

A) `import matplotlib as plt`
B) `import matplotlib.pyplot as plt`
C) `import pyplot as matplotlib`
D) `from matplotlib import plot`

**Correct answer:** B

**Explanation:**
Matplotlib’s plotting module is accessed through `matplotlib.pyplot`, which is conventionally aliased as `plt`. This provides access to functions like `plot()`, `scatter()`, `bar()`, and `show()`.

---

## **Question 2. (MCQ)**

What is the purpose of `plt.show()`?

A) Saves the figure to disk
B) Clears the current plot
C) Displays the figure window
D) Adds a title

**Correct answer:** C

**Explanation:**
`plt.show()` renders and displays the plot. Without it, especially in script-based environments, the plot may not appear.

---

## **Question 3. (MCQ)**

When is a line plot most appropriate?

A) Comparing discrete categories
B) Showing trends across ordered data
C) Displaying frequency counts
D) Showing distribution histograms

**Correct answer:** B

**Explanation:**
Line plots are best for visualizing trends over ordered values such as time, epochs, or sequential measurements.

---

## **Question 4. (MCQ)**

What does `plt.scatter(x, y)` primarily help visualize?

A) Categorical comparisons
B) Relationships between two variables
C) Aggregated totals
D) Time series trends only

**Correct answer:** B

**Explanation:**
Scatter plots show the relationship between two variables and help detect correlations, clusters, and outliers.

---

## **Question 5. (MCQ)**

Which plot type is most suitable for comparing categories like model A, model B, and model C?

A) Line plot
B) Scatter plot
C) Bar chart
D) Pie chart

**Correct answer:** C

**Explanation:**
Bar charts are ideal for comparing discrete categories. They make differences between groups visually clear.

---

## **Question 6. (MCQ)**

What is the function of `plt.xlabel()`?

A) Adds legend
B) Sets x-axis label
C) Changes axis scale
D) Adjusts plot size

**Correct answer:** B

**Explanation:**
`plt.xlabel()` assigns a descriptive label to the x-axis, improving interpretability and clarity.

---

## **Question 7. (MCQ)**

What does `plt.grid(True)` accomplish?

A) Changes background color
B) Adds gridlines to improve readability
C) Saves the plot
D) Removes ticks

**Correct answer:** B

**Explanation:**
Gridlines help viewers estimate values more easily and interpret trends accurately.

---

## **Question 8. (MCQ)**

What is the purpose of `plt.legend()`?

A) Adds a title
B) Displays labels for multiple plotted elements
C) Changes font style
D) Removes duplicate lines

**Correct answer:** B

**Explanation:**
When multiple lines or elements are plotted, `plt.legend()` identifies them using the provided labels.

---

## **Question 9. (Subjective)**

### **AI-Style Visualization Pipeline**

You are analyzing training performance of a machine learning model.

### **Tasks**

1. Create a list of 10 epochs (1 to 10).
2. Generate synthetic training loss values (you may use NumPy).
3. Plot:

   * A line plot of Loss vs Epoch (with markers and grid).
   * A scatter plot of Epoch vs Loss.
4. Create a bar chart comparing accuracy of three models:

   * Model A: 0.85
   * Model B: 0.90
   * Model C: 0.88
5. Ensure all plots include:

   * Proper axis labels
   * Title
   * Figure size adjustment
6. Display all plots correctly.

---

# ✅ **Solution**

```python
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create epochs
epochs = list(range(1, 11))

# Step 2: Generate synthetic loss values
np.random.seed(0)
loss = np.random.rand(10)

# ---- Line Plot ----
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker="o", linestyle="--", label="Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.grid(True)
plt.legend()
plt.show()

# ---- Scatter Plot ----
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Scatter Plot of Loss vs Epoch")
plt.grid(True)
plt.show()

# ---- Bar Chart ----
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")
plt.grid(True)
plt.show()
```