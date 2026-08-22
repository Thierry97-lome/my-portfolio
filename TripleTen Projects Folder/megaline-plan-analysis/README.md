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

## 📈 Key Takeaways
The analysis compares revenue distributions between the two plans and uses hypothesis testing to determine whether observed differences are statistically significant — providing a data-driven recommendation for where to focus marketing spend.

---
*This project was completed as part of the TripleTen Data Analytics bootcamp.*
