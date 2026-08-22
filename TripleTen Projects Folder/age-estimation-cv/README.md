# 👶🧓 Age Estimation from Photos — Computer Vision

## 📌 Project Summary
Good Seed, a supermarket chain, wants to build an automated age-verification system for its self-checkout registers. When a customer scans an alcohol product, the system should estimate the customer's age from a photo, so cashiers can be prompted to check ID for anyone who appears underage — without requiring an ID check for every purchase.

This project fine-tunes a pretrained **ResNet50** computer vision model to predict a person's age from a face photo, treated as a regression problem.

**Goal:** Reach a validation MAE (mean absolute error) of **8 years or lower**.

## 🗂 Dataset
Full dataset: **7,591 labeled face images** (`labels.csv` with `file_name` and `real_age` columns), covering the full human age range. This repo includes `labels.csv` and a small sample of images for reference — see [Dataset Access](#-dataset-access) below for the full image set.

## 🔧 Approach
- Explored the age distribution across the dataset and visually inspected a batch of sample images before modeling
- Built a Keras `ImageDataGenerator` pipeline to stream images in batches (avoiding loading all 7,591 images into memory at once), with horizontal-flip augmentation on the training set only
- Used **ResNet50** (pretrained on ImageNet) as a frozen feature-extraction backbone, with `GlobalAveragePooling2D` and a single `Dense(1)` output layer for age regression
- Trained the model on TripleTen's GPU platform for 20 epochs (Adam optimizer, MSE loss, MAE as the interpretable metric)
- Analyzed training and validation curves to check for overfitting
- Assessed practical deployment considerations for the retail use case

## 🛠 Tools & Technologies
Python, Pandas, NumPy, Matplotlib, TensorFlow/Keras, ResNet50 (transfer learning), `ImageDataGenerator`

## 📈 Key Findings
- The fine-tuned model reached a **validation MAE of roughly 6.6–7.7 years**, meeting the ≤8 year target
- Training loss/MAE decreased smoothly across all 20 epochs, but **validation performance was noticeably noisier**, with one instability spike around epoch 12 — a sign of **overfitting**, since the model fit the training data several years more accurately (in MAE) than it generalized to unseen faces
- **Business takeaway:** given the model's real-world error margin, it's well suited as an **automatic first-pass screen** at checkout — flagging any transaction where predicted age falls below a conservative buffer above the legal drinking age, prompting a manual ID check rather than replacing human verification entirely
- The same transfer-learning pipeline generalizes to other retail computer vision applications: self-checkout fraud/scan-avoidance detection, shelf and inventory monitoring, and queue/traffic analytics

## 📦 Dataset Access
The full dataset (7,591 images + labels) is too large to host directly in this repository. This repo includes `labels.csv` in full, plus a small representative sample of images under `faces-sample/` so the pipeline and code are easy to follow. The complete image set follows the same structure as the [ChaLearn Looking at People age estimation dataset](https://chalearnlap.cvc.uab.cat/dataset/26/description/), commonly used for this type of coursework.

---
*This project was completed as part of the TripleTen Data Science bootcamp (Computer Vision module).*
