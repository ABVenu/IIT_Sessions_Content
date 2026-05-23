# Assignment: Objective — Session 16: Linear Regression Fundamentals

**Total Questions: 10 | Format: 6 MCQs (Single Correct) + 4 MSQs (Multiple Correct)**  
**Order: Easy → Moderate → Hard**

**Instructions:** Choose the best answer for MCQs. For MSQs, **select all that apply**. Submit via the LMS objective assessment.

---

## MCQ 1 — Easy (Single Correct)

QuickRide wants to estimate **trip fare in rupees** from distance and traffic delay before the ride ends. The product team needs a number customers can compare, not a category label. Which ML task family fits this goal?

**A)** Classification — the output is a named bucket  
**B)** Regression — the output is a continuous amount on a scale  
**C)** Clustering — the output is an unlabelled group ID  
**D)** Reinforcement learning — the output is the next action in a game  

**Correct Answer: B**

**Answer Explanation:**  
Fare in rupees is a **measurable number**, which is the signature of **regression**. **A** would apply if the app only returned labels like “cheap / medium / expensive.” **C** is unsupervised grouping without a numeric target. **D** is about sequential decisions, not predicting a fare amount.

---

## MCQ 2 — Easy (Single Correct)

A HR analytics table has a column `job_level` with values `1 = junior`, `2 = mid`, `3 = senior`. The team wants to predict **monthly salary in INR**. How should they treat `job_level` when building a salary model?

**A)** Use `job_level` as the **numeric target** because it contains digits  
**B)** Treat `job_level` as a **category encoded into features**; keep **salary in INR** as the numeric target  
**C)** Drop salary and predict `job_level` instead because regression needs integer columns  
**D)** Convert salary to “junior / mid / senior” labels so regression can run  

**Correct Answer: B**

**Answer Explanation:**  
**Regression** needs a **numeric target** (salary). `job_level` is a **label disguised as numbers**, so it belongs in **features** (e.g. one-hot encoding), not as **y**. **A** confuses coded categories with a measurement scale. **C** reverses the business question. **D** turns the problem into classification, not salary prediction.

---

## MCQ 3 — Easy (Single Correct)

A coaching app fits a simple line: **exam score ≈ 7.5 × study_hours + 40**. In plain language, what does **40** represent?

**A)** The extra marks added for each additional study hour  
**B)** The model’s starting prediction when study hours are zero — the **intercept**  
**C)** The average error on the test set  
**D)** The maximum possible exam score in the dataset  

**Correct Answer: B**

**Answer Explanation:**  
In **y = mx + c**, the constant **c** is the **intercept** — the baseline before the slope term acts. Here **7.5** is the per-hour **coefficient** (**A**). **C** describes residuals or metrics, not the intercept. **D** is unrelated to the line’s constant term.

---

## MCQ 4 — Easy (Single Correct)

For one student, the model predicted **58** marks but the actual score was **62**. Using **residual = actual − predicted**, what is the residual and what does it mean?

**A)** Residual = **+4** ; the model **under-predicted**  
**B)** Residual = **−4** ; the model **under-predicted**  
**C)** Residual = **+4** ; the model **over-predicted**  
**D)** Residual = **−4** ; the model **over-predicted**  

**Correct Answer: A**

**Answer Explanation:**  
**62 − 58 = +4**. A **positive** residual means truth is **above** the line → **under-prediction**. **B** and **D** use the wrong sign. **C** has the right magnitude but the wrong direction label.

---

## MCQ 5 — Moderate (Single Correct)

A property analyst reads a fitted housing model: **median_house_value ≈ 0.8 × median_income + …** (other features held fixed). If **median_income** rises by **1** unit (same scale as training), what is the best business reading of **0.8**?

**A)** Every district will sell for exactly ₹0.8  
**B)** On average, predicted median house value moves by about **0.8 units** when income rises by one unit, holding other features fixed  
**C)** 80% of districts have income above average  
**D)** The model is wrong because coefficients must always be larger than 1  

**Correct Answer: B**

**Answer Explanation:**  
A **coefficient** is the change in **predicted y** when that feature increases by **one unit**, other inputs unchanged. **A** misreads the weight as a fixed price. **C** confuses coefficient size with percentile stats. **D** is false — coefficients depend on feature scale.

---

## MCQ 6 — Moderate (Single Correct)

A district-level **linear regression** on census-style housing data reports **train score ≈ 61%** and **test score ≈ 58%** (same split, same metric). What is the most reasonable first diagnosis?

**A)** Severe **overfitting** — test is far below train  
**B)** Likely **underfitting** — both scores are modest and the train–test gap is small  
**C)** Data leakage — test score should always equal train score  
**D)** The model is perfect because 61% exceeds 50%  

**Correct Answer: B**

**Answer Explanation:**  
**Both** scores are **low** and **close**, which matches **underfitting** (too simple a line for a hard pattern), not memorisation. **A** needs a **large** train–test gap (e.g. 95% vs 60%). **C** misstates leakage symptoms. **D** treats a modest score as perfection.

---

## MSQ 7 — Moderate (Multiple Correct) — Select all that apply

A data lead asks which product problems are **regression** (predict a number on a scale). Which items qualify?

**A)** Forecast **next month’s electricity bill in rupees** from usage history  
**B)** Label each email **spam** or **not spam**  
**C)** Estimate a student’s **exact exam score out of 100** from study hours  
**D)** Decide whether a loan is **approved** or **rejected**  

**Correct Answers: A, C**

**Answer Explanation:**  
**A** and **C** need a **numeric** answer (rupees, marks). **B** and **D** are **classification** — fixed category labels, not a continuous measurement.

---

## MSQ 8 — Moderate (Multiple Correct) — Select all that apply

An engineer trains **linear regression** with **MinMaxScaler** inside a sklearn **Pipeline** on housing features. Which workflow steps follow **leakage-safe** habits?

**A)** `train_test_split` **before** calling `.fit()` on the pipeline  
**B)** `.fit(X_train, y_train)` so the scaler learns statistics from **training rows only**  
**C)** Fit the scaler on the **full dataset**, then split train and test  
**D)** Evaluate with `.score(X_test, y_test)` on rows that were **not** used in `.fit()`  

**Correct Answers: A, B, D**

**Answer Explanation:**  
**A**, **B**, and **D** mirror split-first, train-only learning, and honest test evaluation. **C** leaks because test rows influence scaling parameters before the split.

---

## MSQ 9 — Hard (Multiple Correct) — Select all that apply

A model review board sees these **train vs test** score pairs on the **same hold-out split**. Which interpretations are **fair**?

**A)** Train **94%**, test **93%** → scores are close; the simple model likely **generalizes reasonably** on that data  
**B)** Train **95%**, test **60%** → large gap; possible **overfitting** worth investigating  
**C)** Train **61%**, test **58%** → both low with a small gap; likely **underfitting** rather than memorisation  
**D)** Train **40%**, test **90%** → proof that testing on unseen data is unnecessary  

**Correct Answers: A, B, C**

**Answer Explanation:**  
**A** is a stable train–test story. **B** is the classic **overfitting** gap pattern. **C** matches **underfitting** on harder data. **D** is illogical — test beating train by a huge margin on the same workflow is not a reason to skip holdout evaluation.

---

## MSQ 10 — Hard (Multiple Correct) — Select all that apply

A team benchmarks **linear regression** against a **mean baseline** on the same **20% test split**. Which practices are **sound**?

**A)** Compute the baseline mean from **`y_train` only**, then predict that constant for every test row  
**B)** Compare both models on the **same test rows** with the **same score metric**  
**C)** Use all of **`y` (train + test)** to compute the mean so the baseline is “more accurate”  
**D)** If regression’s test score is **much higher** than always guessing the training mean, features likely add signal beyond a lazy average  

**Correct Answers: A, B, D**

**Answer Explanation:**  
**A** avoids leaking test labels into the baseline. **B** ensures a fair comparison. **D** is the right reading when the model beats the mean floor. **C** leaks test information into the baseline mean.

---

**End of objective assignment.**
