# Study Repository

## Supervised Learning
    Supervised learning is a type of machine learning where the algorithm learns to map inputs to outputs based on labeled training data. There are several types of supervised learning algorithms, including:

1. Regression: Regression algorithms are used for predicting continuous numerical values, such as the price of a house, the stock price of a company, or the temperature of a room. Linear regression and logistic regression are some common types of regression algorithms.

    1. Linear Regression: Linear regression is a basic regression technique that assumes a linear relationship between the input features and the output variable. In other words, it assumes that there is a straight-line relationship between the input variables and the outcome variable.

    2. Polynomial Regression: Polynomial regression is a more complex form of linear regression that allows for non-linear relationships between the input features and the output variable. It involves adding higher-order terms to the model to capture non-linearities in the data.

    3. Ridge Regression: Ridge regression is a type of linear regression that includes a regularization term to prevent overfitting. The regularization term adds a penalty to the size of the coefficients in the model, which helps to prevent the model from becoming too complex and overfitting the training data.

    4. Lasso Regression: Lasso regression is another type of linear regression that uses a different type of regularization to prevent overfitting. Instead of adding a penalty to the size of the coefficients, it adds a penalty to the absolute value of the coefficients. This has the effect of shrinking some of the coefficients to zero, effectively performing feature selection and making the model simpler.
    
    5. Elastic Net Regression: Elastic net regression is a combination of ridge and lasso regression that combines the strengths of both techniques. It includes both a L1 and L2 penalty, allowing it to perform both feature selection and regularization.

    6. Logistic Regression: Logistic regression is a regression technique used for binary classification problems, where the output variable is binary (i.e., 0 or 1). It models the probability of the output variable being 1 as a function of the input features.

2. Classification: Classification algorithms are used for predicting discrete categorical values, such as whether an email is spam or not, whether a patient has a certain disease or not, or whether a credit card transaction is fraudulent or not. In addition to choosing an appropriate algorithm, it is also important to select appropriate evaluation metrics to measure the performance of the classification model. Some common metrics include accuracy, precision, recall, F1-score, and ROC curves..

    1. Logistic Regression: A linear model that uses the logistic function to map the input features to a binary output (i.e., a class label of 0 or 1).

    2. Decision Trees: A model that uses a tree-like structure to classify data points based on a series of hierarchical decisions.

    3. Random Forests: An ensemble learning method that combines multiple decision trees to improve accuracy and reduce overfitting.

    4. Support Vector Machines (SVMs): A model that maps the input features to a high-dimensional space and finds the optimal hyperplane that separates the different classes.

    5. Naive Bayes: A probabilistic model that calculates the likelihood of each class given the input features, and selects the most probable class.

    6. k-Nearest Neighbors (k-NN): A non-parametric model that classifies data points based on the majority class label of its k nearest neighbors in the training dataset

3. Time Series Analysis: Time series analysis algorithms are used to predict values in a time series, such as stock prices or weather patterns. Examples of time series analysis algorithms include ARIMA, Prophet, and LSTM.

4. Ensemble Learning: Ensemble learning is a technique that combines multiple models to improve the accuracy of predictions. Bagging, Boosting, and Stacking are some common types of ensemble learning algorithms.



## What type of algorithm can be used in what type of area?

### Image classification
    Convolutional Neural Networks (CNNs) are a popular choice for image classification problems because they can automatically learn relevant features from images.

### Fraud detection
    Random Forest or Support Vector Machine (SVM) algorithms are commonly used for fraud detection because they can handle large datasets and identify outliers.

### Customer segmentation
     K-means clustering is a popular algorithm for customer segmentation because it can identify groups of customers with similar characteristics.

### Time series forecasting
    Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks are often used for time series forecasting because they can capture time-dependent patterns.

### Recommender systems
    Collaborative Filtering and Matrix Factorization are common approaches to building recommender systems that can predict user preferences and suggest relevant items.