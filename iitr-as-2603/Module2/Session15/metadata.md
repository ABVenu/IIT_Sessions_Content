lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins

title: Leakage & Imbalance

objective: Learn to avoid common traps in model training.

topics be covered: Data leakage guard; Class imbalance basics; Synthetic data concepts; Cross-validation


detailed subtopics to be covered:

- Data Leakage: Definition, Scenarios & Guards — Define data leakage and why it creates misleadingly high performance; cover common scenarios (preprocessing before split, target-related features, test-set statistics in transforms) with a brief link to the previous session workflow; establish the guard checklist: split first, fit preprocessing on training data only, isolate test data, and simulate real-world prediction conditions.
- Introduce Class Imbalance — Explain imbalance using intuitive examples (e.g., fraud detection, rare diseases); show how datasets can be skewed toward one class.
- Understand the Impact of Imbalance — Demonstrate why models become biased toward the majority class and why accuracy becomes unreliable on skewed data.
- Introduce Precision and Recall (Conceptual Only) — Explain using real-world scenarios without formulas; focus on intuition of false positives and false negatives.
- Handling Imbalance: Resampling & Synthetic Data — Introduce oversampling and undersampling with simple intuition and trade-offs; explain synthetic balancing (e.g., SMOTE intuition) as generating artificial but similar minority examples; keep conceptual, no deep implementation.
- Cross-Validation: Why & How (Conceptual) — Explain why a single train-test split is unreliable; introduce multiple splits, how performance varies across folds, and why averaging results gives better confidence; diagram or verbal walkthrough preferred over a full coding lab.
- Connect Leakage, Imbalance, and Evaluation — Reinforce how improper handling of these concepts leads to incorrect conclusions about model performance.


		