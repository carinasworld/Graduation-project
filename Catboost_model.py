# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:02:53 2021

@author: Nelly
"""
import pandas as pd
import numphy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df = pd.read_csv(' ')


## X and Y 
X = df.copy()
X.columns  #check
#del(X['Y_column'])

y = df['Y_column']



# splitting 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=123)


## Catboost model 
model = CatBoostRegressor(iterations=10,
                           depth=4,
                           learning_rate=0.0045,
                           loss_function='MSE',
                           verbose=True)


model.fit(X_train, y_train)

# make the prediction using the model
train_pred = model.predict(X_train)
Train_MSE = mean_squared_error(y_train, train_pred)
Train_MAE = mean_absolute_error(y_train, train_pred)

train_pred = model.predict(X_train)


## test data 
test_pred = model.predict(X_test)
Test_MSE = mean_squared_error(y_test, test_pred)
Test_MAE = mean_absolute_error(y_train, test_pred)

test_pred = model.predict(X_test)



## naive model

naive_forecast = np.ones*mean(y_test)

naive_MAE = mean_absolute_error(y_test, naive_forecast)

print(f'test_MAE: {train_MAE}, Naive_MAE: {naive_MAE}, Train_MAE: {train_MAE}')
print(f'test_MSE: {test_MSE}, Naive_MSE: {naive_MSE}, Test_MSE: {test_MAE}')

test_pred_catboost = model.predict(X_test)








