# 📡 Interconnect — Customer Churn Prediction

## 📌 Project Summary
Interconnect, a telecom operator, wants to proactively identify customers who are likely to churn so the marketing team can offer targeted promotions before they leave. This project builds, tunes, and rigorously validates a classification model to predict churn from customer contract, billing, and service usage data.

**Target:** Churn, defined as `EndDate != 'No'`
**Primary metric:** AUC-ROC (minimum threshold: 0.75)

## 🗂 Dataset
Four related tables, joined on `customerID`:
- `contract.csv` — contract type, billing method, monthly/total charges, start/end dates
- `personal.csv` — demographics (gender, senior citizen status, partner/dependents)
- `internet.csv` — internet service type and add-ons (security, backup, tech support, streaming)
- `phone.csv` — phone service and multiple-lines status

## 🔧 Approach
- Cleaned `TotalCharges` (fixed a text-encoded numeric column with 11 blank values, all from brand-new customers not yet billed) and built the churn target relative to a fixed snapshot date
- Merged all four tables and filled structurally-missing service columns (e.g., "no internet service") with explicit labels rather than dropping rows
- Engineered features based on EDA findings: number of add-on services, has-internet/has-phone flags, and average charge per month
- Split data into **train / stratified validation holdout / test** sets — a strict three-way separation, with the test set touched only once at the very end
- Built a leak-free `ColumnTransformer` + `Pipeline` for preprocessing (scaling numeric features, one-hot encoding categoricals)
- Established a `DummyClassifier` baseline (~0.50 AUC-ROC) before modeling
- Compared **Logistic Regression, Random Forest, and Histogram Gradient Boosting** using 5-fold cross-validation, then tuned all three with `RandomizedSearchCV` — model ranking changed meaningfully after tuning, so the final model wasn't the best-looking default
- Confirmed the selected model on the untouched validation holdout before final test evaluation
- Analyzed feature importance using **permutation importance** on the test set

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn (Pipeline, ColumnTransformer, RandomizedSearchCV, Logistic Regression, Random Forest, Histogram Gradient Boosting, permutation importance)

## 📈 Key Findings
- **Final model:** tuned Random Forest, selected after comparing three model families
- Cross-validation AUC-ROC (training): **0.8465** | Validation AUC-ROC: **0.8430** | **Test AUC-ROC: 0.8417**
- These three scores landing close together confirms the model generalizes well rather than being overfit to the tuning process
- Churn is concentrated among customers on **month-to-month contracts**, with **short tenure**, **higher monthly charges**, **fiber optic internet**, and **electronic check** payment — while customers with **TechSupport**, **OnlineSecurity**, or a partner/dependents churn less. Permutation importance on the final model confirmed tenure and contract-related features as the strongest predictors, matching the EDA findings
- **Next steps identified:** trying gradient boosting libraries with stronger built-in regularization (LightGBM, CatBoost), engineering contract-type × tenure interaction features, and exploring classification threshold adjustments to improve recall on churned customers specifically — since catching at-risk customers matters more to the business than raw accuracy

---
*This project was completed as part of the TripleTen Data Science bootcamp (final capstone project).*
