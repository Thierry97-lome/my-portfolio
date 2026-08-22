# 🛡️ Sure Tomorrow Insurance — Multi-Task Machine Learning

## 📌 Project Summary
Sure Tomorrow, an insurance company, wants to explore whether Machine Learning can help solve four distinct business problems using customer data. This project evaluates all four tasks and includes an original analytical proof of a data privacy technique.

**Tasks:**
1. **Similar Customers** — find customers similar to a given customer, to support targeted marketing
2. **Benefit Prediction** — predict whether a new customer is likely to receive an insurance benefit, and compare against a baseline (dummy) model
3. **Benefit Amount Regression** — predict the amount of insurance benefits a customer might receive, using a linear regression model built from scratch
4. **Data Obfuscation** — protect customers' personal data using a linear transformation, without degrading model quality

## 🗂 Dataset
`insurance_us.csv` — 5,000 customer records: gender, age, income, family members, and insurance benefits received.

## 🔧 Approach
- Explored the dataset and checked for natural customer clusters using pair plots
- Implemented a custom **k-Nearest Neighbors** function to find similar customers under different distance metrics (Euclidean, Manhattan) and with/without feature scaling
- Framed benefit prediction as binary classification; compared a **dummy baseline classifier** against **kNN** and **Logistic Regression**, evaluated with F1 score
- Built a **linear regression model from scratch** (using the closed-form normal equation) to predict benefit amounts, and validated it against scikit-learn's implementation using RMSE
- Designed a **data obfuscation scheme**: multiplying customer data by a randomly generated invertible matrix, then proved analytically and empirically that linear regression predictions remain unchanged under this transformation — demonstrating the technique protects personal data without sacrificing model performance

## 🛠 Tools & Technologies
Python, NumPy, Pandas, Seaborn, Scikit-learn (kNN, Logistic Regression, Linear Regression, DummyClassifier), linear algebra (matrix inversion, custom regression implementation)

## 📈 Key Findings
- Feature scaling significantly changes which customers are identified as "similar" under kNN — unscaled data lets high-magnitude features like income dominate the distance calculation
- Both kNN and Logistic Regression classifiers **outperformed the dummy baseline** at predicting whether a customer would receive a benefit, confirming that customer features carry real predictive signal
- The custom from-scratch linear regression implementation produced results matching scikit-learn's built-in model, validating the underlying math
- **Proved analytically** that multiplying feature data by an invertible matrix does not change a linear regression model's predictions or RMSE — meaning customer data can be obfuscated for privacy protection with zero cost to model accuracy

**Takeaway:** This project demonstrates that Sure Tomorrow can adopt ML-driven marketing and risk models while also protecting customer privacy through mathematically sound data obfuscation — solving both a business and a compliance need simultaneously.

---
*This project was completed as part of the TripleTen Data Science bootcamp.*
