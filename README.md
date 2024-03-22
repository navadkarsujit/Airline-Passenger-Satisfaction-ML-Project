# Airline Passenger Satisfaction Prediction

## Overview
This project focuses on predicting passenger satisfaction with airline services based on various features such as flight distance, service ratings, departure/arrival time convenience, etc. The goal is to build machine learning models that can accurately classify whether a passenger is satisfied or dissatisfied.

## Table of Contents
- [Importing Data](#importing-data)
- [Data Understanding and Cleaning](#data-understanding-and-cleaning)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Conclusion](#conclusion)
- [Testing New Data](#testing-new-data)

## Importing Data
The data is imported using pandas library, and necessary preprocessing steps such as handling missing values are performed.

## Data Understanding and Cleaning
- Irrelevant columns like 'id' and 'Unnamed: 0' are dropped.
- Missing values in numerical columns are handled by imputing mean or median values.
- Missing values in categorical columns are replaced with mode values.

## Exploratory Data Analysis
- Statistical analysis is performed on the dataset to understand the distribution of numerical features.
- Visualization techniques like histograms and boxplots are used to visualize the distributions and identify outliers.
- The correlation between features is analyzed using a heatmap.

## Feature Engineering
- Skewness of numerical features is reduced.
- Categorical features are encoded using one-hot encoding and label encoding.

## Model Building
- Various classification models such as Logistic Regression, K Nearest Neighbors, Support Vector Machine, Decision Tree, Random Forest, AdaBoost, and Gradient Boosting are trained on the data.
- Hyperparameter tuning is performed using GridSearchCV to improve model performance.
- Model accuracy and classification reports are generated for each model.
- Random Forest achieves the highest accuracy of 96% among the models.

## Conclusion
- Random Forest demonstrates the best performance with an accuracy of 96% in predicting passenger satisfaction.
- Support Vector Machine and Decision Tree also perform well with an accuracy of 95%.
- Logistic Regression has the lowest accuracy of 89% among the models evaluated.

## Testing New Data
- Test data is used to predict passenger satisfaction using the trained models, and predictions are found to be correct.

