# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def sil(filename, size, ran_sta):

  # Importing the dataset
  dataset = pd.read_csv(filename)
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values

  # Splitting the dataset into the Training set and Test set
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = size, random_state = ran_sta)

  # Training the Simple Linear Regression model on the Training set
  regressor = LinearRegression()
  regressor.fit(X_train, y_train)

  #saving model
  joblib.dump(regressor, f"{filename}.pk1")
