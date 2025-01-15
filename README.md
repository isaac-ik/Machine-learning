Machine Learning Projects Repository
====================================

This repository contains various machine learning projects exploring different datasets and techniques for predictive modeling and data analysis.

Project Structure
-----------------

### 1\. ML Deployment

This section includes projects showcasing model deployment using Flask web applications.

#### a. Wine Quality Prediction

-   **Dataset:** `winequality-red.csv`

-   **Goal:** Predict wine quality based on various chemical properties.

-   **Approach:**

    -   Data preprocessing and feature engineering performed in `WineQuality_exercise.ipynb`

    -   A Flask web app (`app.py`) for predicting wine quality using trained models.

-   **Directory Structure:**

    -   `models/` - Trained models saved for deployment.

    -   `templates/` - HTML templates for the web application.
<img width="928" alt="club comparison visualization" src="https://github.com/isaac-ik/Machine-learning/blob/main/ML%20deployment/Wine%20Quality/Screenshot%202025-01-15%20152455.png" />
#### b. Salary Prediction

-   **Dataset:** `Position_Salaries.csv`

-   **Goal:** Predict salary based on years of experience and job position.

-   **Approach:**

    -   Implemented polynomial regression in `Predicting Salaries by position.ipynb`

    -   A Flask web app (`app.py`) for predicting salaries using a trained model.

-   **Directory Structure:**

    -   `models/` - Trained models saved for deployment.

    -   `templates/` - HTML templates for the web application.

* * * * *

### 2\. Supervised Learning Projects

-   **Purchase Prediction Using Various Classifiers:**

    -   Algorithms applied: Logistic Regression, KNN, Decision Tree, Random Forest, SVM (Linear and RBF Kernels), Naive Bayes.

    -   Datasets: `Social_Network_Ads.csv`

-   **Customer Churn Prediction:**

    -   Applied ANN to predict if a bank customer will churn.

    -   Dataset: `Churn_Modelling.csv`

-   **Breast Cancer Prediction:**

    -   Applied various models for breast cancer classification.

    -   Dataset: `Breast Cancer Data.csv`

-   **Salary Prediction Models:**

    -   Linear Regression, Polynomial Regression, Decision Tree Regression, SVM Regression.

    -   Datasets: `Salary_Data.csv`, `Position_Salaries.csv`

* * * * *

### 3\. Unsupervised Learning Projects

-   **Clustering Models:**

    -   Hierarchical and K-Means clustering on `Mall_Customers.csv`

-   **Market Basket Analysis:**

    -   Association rule learning using `Market_Basket_Optimisation.csv`

* * * * *

### 4\. Reinforcement Learning

-   **Ad Selection Strategies:**

    -   Upper Confidence Bound (UCB) and Thompson Sampling applied to `Ads_CTR_Optimisation.csv`

Tools and Libraries Used
------------------------

-   Python

-   Scikit-Learn

-   Pandas

-   NumPy

-   Matplotlib

-   Seaborn

Usage
-----

Clone the repository and run the `.ipynb` notebooks using Jupyter Notebook or Google Colab.

```
git clone https://github.com/isaac-ik/Machine-learning.git
```

Author
------

**Isaac Ikhaiduwor**
