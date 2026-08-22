# 🏦 Predicting Customer Churn — Beta Bank

## 📌 Project Summary
Beta Bank is losing customers gradually over time. Since retaining an existing customer is cheaper than acquiring a new one, this project builds a classification model to predict whether a customer will leave (churn) the bank, so retention efforts can be targeted at customers most at risk.

**Goal:** Achieve an F1 score of at least 0.59 on the test set, using AUC-ROC as a secondary evaluation metric.

## 🗂 Dataset
`Churn.csv` — 10,000 customer records including:
- Demographics: age, geography, gender
- Financial: credit score, balance, estimated salary, number of products
- Behavioral: tenure, active membership status, credit card ownership
- Target: `Exited` (1 = customer churned, 0 = customer stayed)

## 🔧 Approach
- Cleaned data (filled missing `Tenure` values with the median, removed non-informative identifier columns)
- Encoded categorical features (`Geography`, `Gender`) using one-hot encoding
- Split data into training, validation, and test sets, with feature scaling
- Diagnosed **significant class imbalance** — far more customers stayed than churned
- Trained a baseline Logistic Regression model with no imbalance handling to establish a reference point
- Addressed the imbalance using two techniques:
  - **Class weighting**
  - **Upsampling** the minority (churned) class
- Compared Logistic Regression and Random Forest models across both techniques
- Selected the best-performing model, retrained it on combined train + validation data, and evaluated on the held-out test set

## 🛠 Tools & Technologies
Python, Pandas, Scikit-learn (Logistic Regression, Random Forest, StandardScaler, train_test_split, F1 score, AUC-ROC)

## 📈 Key Findings
- The baseline model (no imbalance handling) performed very poorly — **F1 ≈ 0.07** — confirming that class imbalance was a critical problem to solve
- Class weighting alone improved the F1 score to **≈ 0.46**
- The best approach was a **Random Forest model trained on upsampled data**, reaching an F1 score of **≈ 0.62** on the validation set — above the 0.59 target
- On the final held-out test set, the model achieved an **F1 score of 0.556** and an **AUC-ROC of 0.873**, indicating strong ability to distinguish customers likely to churn from those likely to stay

**Takeaway:** Addressing class imbalance was the single most important step in this project — a plain baseline model was nearly unusable for identifying churners, while targeted resampling techniques produced a model with genuinely reliable predictive power.

---
*This project was completed as part of the TripleTen Data Science bootcamp.*
