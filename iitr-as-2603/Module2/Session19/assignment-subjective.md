# Subjective Assignment - Medium Difficulty

## Practical Task: Model Comparison and Decision Memo

A student support team wants to identify students likely to **Pass** so they can plan mentorship outreach for students likely to **Fail**.  
Build and evaluate three classifiers - **Logistic Regression**, **Decision Tree**, and **Random Forest** - on a synthetic student dataset, then recommend one model using metric evidence.

### Requirements
1. Generate a dataset of at least 400 rows with the following features:
   - `study_hours` (float)
   - `sleep_hours` (float)
   - `distractions` (float)
   - target label `pass_fail` (0/1)
2. Split data into train and test (80/20) using a fixed random seed.
3. Train:
   - `LogisticRegression`
   - `DecisionTreeClassifier` (with controlled depth)
   - `RandomForestClassifier` (at least 100 trees)
4. For each model, report:
   - Confusion matrix values (TN, FP, FN, TP)
   - Accuracy
   - Precision
   - Recall
   - F1 score
   - ROC-AUC (must use predicted probabilities)
5. Print a final recommendation paragraph that:
   - picks one model,
   - justifies the choice using at least two metrics,
   - explains one trade-off (e.g., interpretability vs stability).

### Expected Output (minimum)
- Clearly printed metric summary for all three models
- One recommendation paragraph (4-6 lines)

### Submission Instruction
- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

### Answer Explanation (Reference Approach)
- Ideal workflow:
  1. Create reproducible synthetic data using NumPy with a fixed seed.
  2. Use `train_test_split` to avoid evaluation on training data.
  3. Fit the three models on the same split for fair comparison.
  4. Use `predict()` for confusion matrix, precision, recall, and F1.
  5. Use `predict_proba()[:, 1]` for ROC-AUC.
  6. Compare metrics and provide model recommendation with reasoning.
- Alternative approaches are acceptable if they satisfy all constraints and use correct metric logic.

