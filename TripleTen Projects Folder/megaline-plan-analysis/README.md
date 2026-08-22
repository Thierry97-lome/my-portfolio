# Which Plan is Better? — Megaline Statistical Analysis

## 📌 Project Summary
Megaline, a telecom operator, offers two prepaid plans: **Surf** and **Ultimate**. The commercial department wants to know which plan generates more revenue, in order to allocate the advertising budget more effectively.

This project analyzes the calling, messaging, and internet usage behavior of a sample of Megaline clients to determine which plan brings in more revenue on average, using descriptive statistics and hypothesis testing.

## 🗂 Dataset
Five tables describing user behavior over time:
- `megaline_users.csv` — user demographics and plan info
- `megaline_calls.csv` — individual call records (date, duration)
- `megaline_messages.csv` — individual text messages sent
- `megaline_internet.csv` — internet session usage (MB)
- `megaline_plans.csv` — plan pricing and included allowances

## 🔧 Approach
- Cleaned and converted data types (dates, numeric fields)
- Aggregated calls, messages, and internet usage per user per month
- Calculated monthly revenue per user based on plan pricing and overage charges
- Compared usage and revenue distributions between Surf and Ultimate users
- Tested statistical hypotheses:
  - Is average revenue different between the Surf and Ultimate plans?
  - Is average revenue different between users in Moscow vs. other regions?

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy (statistical testing)

## 📈 Key Findings
- Ultimate plan users have higher average call duration, message counts, and internet usage than Surf users
- Average revenue **per user** is higher for Ultimate plan users than Surf plan users
- However, **total revenue** collected from Surf users is higher overall, since there are more Surf subscribers
- A two-sample t-test confirmed the difference in mean revenue between Surf and Ultimate is statistically significant (p ≈ 3.17e-15, well below α = 0.05)
- A separate t-test found no statistically significant difference in mean revenue between users in the NY-NJ area and users elsewhere (p ≈ 0.07)

**Business takeaway:** Ultimate plan subscribers are more valuable per user, but Surf drives more revenue in aggregate due to its larger user base — a useful distinction for deciding where to focus retention vs. acquisition efforts.

---
*This project was completed as part of the TripleTen Data Analytics bootcamp.*
