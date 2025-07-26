# 🌿 Oil Palm Leaf Nutrient Estimation from Spectroradiometer Data 🔬

[![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/YOUR_REPO_NAME.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO_NAME.svg?style=social)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/YOUR_REPO_NAME.svg?style=social)](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/network/members)
---

## 🌟 Introduction

Oil palm trees are vital for global palm oil production, a commodity widely used in food, cosmetics, and biofuels. Ensuring their optimal growth and yield requires precise management of essential nutrients: **Nitrogen (N), Phosphorus (P), Potassium (K), and Magnesium (Mg)**.

This project introduces a robust machine learning system designed to estimate nutrient levels in oil palm leaves directly from spectroradiometer data. By accurately assessing nutrient status, we can prevent over-fertilization, promote sustainable agricultural practices, and enhance tree health and productivity.

---

## 🔬 Dataset

The project utilizes spectroradiometer data from oil palm leaves. This dataset is the foundation for training models to correlate spectral signatures with specific nutrient levels.

---

## 📐 System Architecture

Our system is engineered to analyze and predict nutrient levels using a comprehensive machine learning pipeline. It encompasses data preprocessing, model training, and prediction for nutrient deficiency levels, leveraging both classification and regression approaches.

### ⚙️ Preprocessing Pipeline

A critical component of our system is the sophisticated preprocessing pipeline, designed to transform raw spectroradiometer data into a clean, normalized, and optimized format for machine learning.

#### 🌊 Noise Reduction
Applies the **Savitzky-Golay filter** to smooth spectral data, effectively reducing noise while preserving important signal characteristics.

#### 📊 Baseline Correction
Implements a **polynomial detrending method** to remove baseline effects from the spectral data, significantly improving its quality for analysis.

#### ⚖️ Normalization
Scales the spectral data to a range of $[0, 1]$ using **Min-Max scaling**, ensuring consistency and comparability between features for robust model training.

#### 🎯 Feature Selection with PCA
Utilizes **Principal Component Analysis (PCA)** to reduce the dimensionality of the spectral data. Components that collectively explain **95% of the variance** are retained, yielding a smaller, more meaningful feature set.

#### 📈 Data Augmentation
Generates synthetic data by adding small random noise to the first four principal components (PCs). This process combines synthetic data with the original dataset to increase the size and diversity of the training data, enhancing model generalization.

#### 🏷️ Target Label Encoding
Encodes the categorical target variable (Rule) into numeric values for machine learning compatibility, ensuring the presence of the target column before processing.

---

## 🧠 Model Training

### Data Splitting

The dataset is rigorously split into **80% training data** and **20% testing data** using **Stratified Sampling** via the `train_test_split()` method. This stratification ensures that the class distribution in both the training and testing sets closely mirrors that of the original dataset, leading to more reliable model evaluation.

### Classification Models

An **ensemble learning approach** combines multiple powerful models using a **Voting Classifier** to leverage their diverse strengths for robust classification.

* **XGBoost (XGBClassifier)**
* **LightGBM (LGBMClassifier)**
* **CatBoost (CatBoostClassifier)**
* **MLPClassifier**

### Regression Model

The **Gradient Boosting Regressor** was specifically selected for its exceptional ability to handle complex, non-linear relationships within the data, providing robust and accurate predictions for continuous nutrient levels.

### Hyperparameter Tuning

(You mentioned this but didn't detail the method. If you used a specific technique like GridSearchCV or Optuna, briefly mention it here.)

---

## 📈 Evaluation

Our models were rigorously evaluated using a suite of metrics tailored for both classification and regression tasks.

### Evaluation Metrics

#### For Classification Models
* **Accuracy:** The proportion of correctly predicted instances.
* **F1-Score:** The harmonic mean of precision and recall, providing a balanced measure of a model's performance on imbalanced datasets.

#### For Regression Models
* **Mean Squared Error (MSE):** The average of the squared differences between predicted and actual values.
* **Root Mean Squared Error (RMSE):** The square root of MSE, providing error in the same units as the target variable.
* **Mean Absolute Error (MAE):** The average of the absolute differences between predicted and actual values.
* **R-squared ($R^2$):** The proportion of variance in the dependent variable that can be predicted from the independent variable(s).

### Nutrient Prediction Performance

Here's a summary of the performance for each nutrient:

| Nutrient    | Classification Accuracy | Regression Accuracy |
| :---------- | :---------------------- | :------------------ |
| **Magnesium** | 73%                     | 70%                 |
| **Nitrogen** | 81%                     | 80%                 |
| **Phosphorus**| 83%                     | 86%                 |
| **Potassium** | 76%                     | 79%                 |

Our findings demonstrate the promising capability of spectroradiometer data combined with advanced machine learning techniques to accurately estimate essential nutrient levels in oil palm leaves.

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.x
* Pip

### Installation

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
pip install -r requirements.txt
