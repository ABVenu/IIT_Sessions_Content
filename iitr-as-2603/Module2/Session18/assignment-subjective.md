# Subjective Assignment: Student Pass Prediction with Logistic Regression

## Practical Task

**Difficulty:** Easy  
**Type:** Coding implementation

---

## Scenario

An exam-coaching app wants a short script that predicts whether a student **passed (1)** or **failed (0)** using only **study hours**, shows the model’s confidence scores, and prints a simple accuracy and confusion-matrix report on held-out students.

---

## Task

Create a Python file named `student_pass_classifier.py` that trains Logistic Regression on the fixed dataset below and prints a small evaluation report.

### Functional Requirements

1. Import:
   - `pandas as pd`
   - `LogisticRegression` from `sklearn.linear_model`
   - `train_test_split` from `sklearn.model_selection`
   - `accuracy_score` and `confusion_matrix` from `sklearn.metrics`
2. Build a DataFrame using exactly this data:

```python
data = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7, 9, 4, 6, 8, 10],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
})
```

3. Use `study_hours` as the only feature (`X` must be 2D, for example `data[["study_hours"]]`).
4. Use `passed` as the target.
5. Split with `test_size=0.25` and `random_state=42`.
6. Train `LogisticRegression(max_iter=1000)` on training data only.
7. On the test set, print a table for **all test rows** with:
   - `study_hours`
   - `pred` (0 or 1 from `model.predict`)
   - `prob_pass` (probability of class 1 from `model.predict_proba`, rounded to 2 decimals)
8. Print test **accuracy** as a percentage with one decimal place using `accuracy_score`.
9. Print the **confusion matrix** and labelled counts:
   - `TN`, `FP`, `FN`, `TP` using sklearn layout `[[TN, FP], [FN, TP]]`
10. Print one short observation line starting with `Observation:` stating whether most test students were predicted as pass (`1`) or fail (`0`).

### Expected Run Commands

```bash
pip install pandas scikit-learn
python student_pass_classifier.py
```

If your system uses `pip3` and `python3`, use those commands instead.

### Expected Behaviour

- The script runs without any external CSV file.
- The model is fit only on training rows.
- The table shows both hard labels (`pred`) and soft scores (`prob_pass`) for every test row.
- Accuracy and the confusion matrix are computed from test predictions only.

### Constraints

- Write everything in one `.py` file.
- Do not hard-code accuracy, probabilities, or confusion-matrix counts.
- Do not fit on test rows before evaluation.
- Keep printed output readable with short headings.

---

## Submission Instructions

- Code all the points mentioned above in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor or answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

A strong solution builds the given DataFrame, reshapes `study_hours` into a 2D feature matrix, splits once, and fits `LogisticRegression` on training rows only. The test table links `predict()` with `predict_proba()[:, 1]` so learners see the label and the probability together.

Accuracy summarizes overall correctness. Unpacking `confusion_matrix` into TN, FP, FN, and TP shows which mistake types occurred. The final observation is a simple read of whether most `pred` values on the test set are 0 or 1.

### Complete Expected Code

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "study_hours": [2, 3, 4, 5, 6, 7, 8, 9, 3, 5, 7, 9, 4, 6, 8, 10],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
})

X = data[["study_hours"]]
y = data["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
prob_pass = model.predict_proba(X_test)[:, 1]

print("Test set predictions")
print(f"{'study_hours':>12} {'pred':>6} {'prob_pass':>10}")
for i in range(len(X_test)):
    hours = X_test.iloc[i, 0]
    print(f"{hours:>12.0f} {int(y_pred[i]):>6} {prob_pass[i]:>10.2f}")

acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy: {round(acc * 100, 1)}%")

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

print("\nConfusion matrix [[TN, FP], [FN, TP]]:")
print(cm)
print(f"TN={tn}  FP={fp}  FN={fn}  TP={tp}")

majority_label = 1 if (y_pred == 1).sum() >= (y_pred == 0).sum() else 0
label_word = "pass" if majority_label == 1 else "fail"
print(f"\nObservation: Most test students were predicted as {label_word} ({majority_label}).")
```

### Alternative Approaches

Learners may print the test table with a pandas DataFrame. The observation may count `pred` values explicitly. The solution is acceptable if the same split is used, probabilities come from `predict_proba[:, 1]`, and all test rows appear in the output table.
