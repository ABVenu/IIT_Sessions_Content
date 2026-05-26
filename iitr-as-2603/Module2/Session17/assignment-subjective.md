# Subjective Assignment: Simple Regression Model Comparison

## Practical Task

**Difficulty:** Easy  
**Type:** Coding implementation

---

## Scenario

A teacher wants a simple report that compares three regression models for predicting student exam scores. The teacher also wants to see whether regularized models reduce the effect of a noisy feature and how far the Ridge model's predictions are from actual scores.

## Task

Create a Python file named `simple_regression_comparison.py` that uses a small given dataset, compares Linear Regression, Ridge, and Lasso, and prints a short error analysis.

### Functional Requirements

1. Import:
   - `numpy as np`
   - `pandas as pd`
   - `LinearRegression`, `Ridge`, and `Lasso` from `sklearn.linear_model`
   - `train_test_split` from `sklearn.model_selection`
   - `mean_absolute_error`, `mean_squared_error`, and `r2_score` from `sklearn.metrics`
2. Create a DataFrame using the exact data given below:

```python
data = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7, 9],
    "sleep_hours": [6, 6, 7, 7, 8, 8, 7, 8, 5, 6, 7, 9],
    "attendance": [62, 68, 72, 75, 80, 84, 88, 92, 65, 78, 86, 95],
    "distractions": [5, 4, 4, 3, 2, 2, 1, 1, 5, 3, 2, 1],
    "random_noise": [9, 2, 7, 1, 8, 3, 6, 4, 5, 10, 1, 7],
    "exam_score": [58, 63, 68, 73, 80, 84, 91, 96, 60, 75, 86, 98],
})
```

3. Use these feature columns:
   - `study_hours`
   - `sleep_hours`
   - `attendance`
   - `distractions`
   - `random_noise`
4. Use `exam_score` as the target column.
5. Split the data using:
   - `test_size=0.2`
   - `random_state=42`
6. Train these three models:
   - `LinearRegression()`
   - `Ridge(alpha=1)`
   - `Lasso(alpha=0.1)`
7. For each model, print:
   - MAE
   - RMSE
   - R-squared
8. Print a coefficient comparison table for the `random_noise` feature only.
9. Use Ridge predictions to create a small error analysis table with:
   - `actual`
   - `predicted`
   - `error` as `actual - predicted`
   - `abs_error`
10. Print two short observations:
    - Which model has the lowest RMSE?
    - Did Ridge or Lasso reduce the `random_noise` coefficient compared with Linear Regression?

### Expected Run Commands

```bash
pip install numpy pandas scikit-learn
python simple_regression_comparison.py
```

If your system uses `pip3` and `python3`, use those commands instead.

### Expected Behaviour

- The script should run without requiring any external dataset.
- All three models must be evaluated on the same test rows.
- The output should show MAE, RMSE, and R-squared for each model.
- The output should show how the `random_noise` coefficient changes across Linear Regression, Ridge, and Lasso.
- The Ridge error analysis table should show actual score, predicted score, error, and absolute error for test rows.

### Constraints

- Write the solution in one Python file only.
- Do not fit any model on the test data.
- Do not hard-code MAE, RMSE, R-squared, prediction, or error values.
- Keep the output readable with clear headings.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor or answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

A strong solution first creates the given DataFrame and separates features from the target. It uses one train-test split for all three models so the comparison is fair. MAE, RMSE, and R-squared are calculated on test predictions only.

The coefficient comparison focuses only on `random_noise`, which keeps the task simple while still showing the effect of regularization. The Ridge error analysis table helps learners see prediction errors row by row.

### Complete Expected Code

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def evaluate_model(name, model):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"\n{name}")
    print(f"MAE       : {mae:.2f}")
    print(f"RMSE      : {rmse:.2f}")
    print(f"R-squared : {r2:.3f}")

    return {
        "name": name,
        "model": model,
        "predictions": predictions,
        "rmse": rmse,
    }


data = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7, 9],
    "sleep_hours": [6, 6, 7, 7, 8, 8, 7, 8, 5, 6, 7, 9],
    "attendance": [62, 68, 72, 75, 80, 84, 88, 92, 65, 78, 86, 95],
    "distractions": [5, 4, 4, 3, 2, 2, 1, 1, 5, 3, 2, 1],
    "random_noise": [9, 2, 7, 1, 8, 3, 6, 4, 5, 10, 1, 7],
    "exam_score": [58, 63, 68, 73, 80, 84, 91, 96, 60, 75, 86, 98],
})

feature_names = ["study_hours", "sleep_hours", "attendance", "distractions", "random_noise"]
X = data[feature_names]
y = data["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge (alpha=1)": Ridge(alpha=1),
    "Lasso (alpha=0.1)": Lasso(alpha=0.1),
}

results = []
for name, model in models.items():
    results.append(evaluate_model(name, model))

noise_coefficients = []
noise_index = feature_names.index("random_noise")

for result in results:
    noise_coefficients.append({
        "model": result["name"],
        "random_noise_coefficient": result["model"].coef_[noise_index],
    })

coefficient_table = pd.DataFrame(noise_coefficients)
print("\nRandom Noise Coefficient Comparison")
print(coefficient_table.round(3).to_string(index=False))

best_result = min(results, key=lambda item: item["rmse"])
ridge_result = next(item for item in results if item["name"] == "Ridge (alpha=1)")

error_analysis = pd.DataFrame({
    "actual": y_test.to_numpy(),
    "predicted": ridge_result["predictions"],
})
error_analysis["error"] = error_analysis["actual"] - error_analysis["predicted"]
error_analysis["abs_error"] = np.abs(error_analysis["error"])

print("\nRidge Error Analysis")
print(error_analysis.round(2).to_string(index=False))

print("\nFinal Interpretation")
print(f"Lowest RMSE model: {best_result['name']}")
print("Compare the random_noise coefficient values to see how regularization changed the noisy feature.")
```

### Alternative Approaches

Learners may use separate variables instead of dictionaries for the three models. The solution is acceptable if all three models use the same train-test split, metrics are calculated from test predictions, and the Ridge error analysis table is printed.
