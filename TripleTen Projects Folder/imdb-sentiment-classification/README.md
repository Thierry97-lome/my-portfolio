# 🎬 Film Junky Union — IMDB Review Sentiment Classification

## 📌 Project Summary
The Film Junky Union, a community for classic movie enthusiasts, is building a system to automatically filter and categorize movie reviews. This project trains and compares multiple NLP models to classify IMDB movie reviews as positive or negative.

**Goal:** Reach an F1 score of at least **0.85** on the test set.

## 🗂 Dataset
`imdb_reviews.tsv` — ~47,000 labeled IMDB movie reviews with metadata (title, year, genre, rating) and a train/test split flag, sourced from the [Maas et al. 2011 IMDB sentiment dataset](https://ai.stanford.edu/~amaas/data/sentiment/).

## 🔧 Approach
- Performed EDA on review volume, ratings distribution, and class balance across the train/test split
- Built a shared `evaluate_model()` routine to consistently score every model on F1, accuracy, and ROC AUC
- Normalized review text (lowercasing, removing digits/punctuation) and split data into train/test using the dataset's built-in `ds_part` flag
- Trained and compared **five models**:
  - **Model 0** — Dummy baseline (predicts the most frequent class)
  - **Model 1** — NLTK stopwords + TF-IDF + Logistic Regression
  - **Model 2** — NLTK stopwords + TF-IDF + LightGBM
  - **Model 3** — spaCy lemmatization + TF-IDF + Logistic Regression
  - **Model 4** — spaCy lemmatization + TF-IDF + LightGBM
  - **Model 9** — BERT embeddings (subset of data, CPU-trained) + Logistic Regression
- Wrote a set of original custom movie reviews and ran them through all four strongest models to qualitatively compare their predictions
- **Diagnosed and fixed a critical data bug**: an early deduplication step was silently discarding ~85% of the training data, which was the root cause of poor early F1 scores — fixing it dramatically improved every model's performance

## 🛠 Tools & Technologies
Python, Pandas, NumPy, NLTK, spaCy, Scikit-learn (TF-IDF, Logistic Regression), LightGBM, PyTorch, Hugging Face Transformers (BERT)

## 📈 Key Findings
| Model | Approach | Test F1 |
|---|---|---|
| Model 1 | NLTK + TF-IDF + Logistic Regression | **0.88** |
| Model 2 | NLTK + TF-IDF + LightGBM | 0.86 |
| Model 3 | spaCy (lemmatized) + TF-IDF + Logistic Regression | **0.88** |
| Model 4 | spaCy (lemmatized) + TF-IDF + LightGBM | 0.86 |
| Model 9 | BERT embeddings + Logistic Regression | 0.70 |

- **All four TF-IDF-based models cleared the 0.85 F1 target** once the data pipeline bug was fixed — simpler Logistic Regression models slightly outperformed LightGBM
- **spaCy lemmatization didn't meaningfully outperform basic normalization** once the underlying data was fixed, showing that clean, complete data mattered more than preprocessing sophistication
- **BERT (Model 9) fell short of the F1 target**, but this reflects its small training sample (300 reviews vs. ~24,000 for the other models) due to CPU compute constraints — not a weakness of the method itself. It still handled ambiguous, context-heavy reviews more sensibly than the bag-of-words models in the custom review test
- **Biggest lesson:** a single one-line data-cleaning mistake at the start of the pipeline had a bigger impact on final performance than any model or vectorizer choice — a reminder to validate data assumptions early

---
*This project was completed as part of the TripleTen "Machine Learning for Texts" course.*
