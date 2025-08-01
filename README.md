# Stroke Risk Analysis

## Project Overview

Stroke is defined as a medical condition in which there is poor blood flow towards the brain, leading to cell death. The World Health Organization cites stroke as the 2nd leading cause of death globally, accounting for approximately 11% of total deaths. 

This project aims to build a predictive model to assess the likelihood of the onset of stroke of a patient using various potential parameters such as gender, age, medical history and smoking status. Ideally, the model should prioritise identifyingh high-risk patients while maintaining clinical practicality, ensuring that healthcare professionals can rely on the predictions for decision-making support.

## Data Information

The original data was obtained from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). In order to simulate real-world data issues, the dataset has been purposefully augmented to include formatting inconsistencies, missing values, duplicate entries as well as invalid values. The augmented dataset can be viewed [here](data/stroke_dataset_messy.csv).

## Workflow

1.  Data Cleaning 
    - Standardized inconsistent formatting such as trailing whitespaces and capitalisation
    - Filtered invalid values out of the dataset
    - Handled missing values through removal and imputation
    - Detailed cleaning procedure can be found [here](notebooks/01_data_cleaning.ipynb)

2. Exploratory Data Analysis
    - Analysed distribution of target variable and features
    - Studied interactions between target variable and features, as well as relationships within features
    - Detailed EDA can be found [here](notebooks/02_exploratory_data_analysis.ipynb)

3. Feature Engineering
    - Removed irrelevant columns that were deemed not important during the EDA process
    - Encoding categorical columns prior to modeling
    - Detailed Feature Engineering process can be found [here](notebooks/03_data_preprocessing.ipynb)

4. Modeling
    - Assessed various classification models to determine the best model for stroke prediction (Logistic Regression, KNN, Random Forest & XGBoost)
    - Models were cross-validated and evaluated based on various metrics (Precision, Recall, F1, ROC-AUC)
    - Performed hyperparameter tuning using GridSearchCV to find the best hyperparameters for the most optimal model
    - Assessed best estimator using Confusion Matrix, Classification Report and Feature Importance Analysis
    - Detailed Modeling process can be found [here](notebooks/04_modeling.ipynb)

## Key Findings

- Best Model: Logistic Regression model with the following hyperparameters: {'C': 10, 'penalty': 'l1', 'solver': 'saga'}
- Top Predictors of Stroke : Age, Heart Disease and Hypertension
- Challenge: Addressing extreme class imbalance

## Technologies Used

- Python (Pandas, NumPy, Seaborn, Scikit-learn, XGBoost)
- Jupyter Notebook
- Git and Github

## Recommendations for Future Work

- Collect more balanced and enriched data to ensure a more even spread of data amongst classes to mitigate class imbalance
- Using ensemble modelling to better handle class imbalances
- Model deployment using Flask or FastAPI on cloud platforms