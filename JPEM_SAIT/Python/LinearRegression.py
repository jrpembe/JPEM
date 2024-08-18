import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/boston.csv")
df = df.drop(['TOWN'], axis=1)
y = df["MEDV"]
x = df.drop(["MEDV"], axis=1)

regressor = LinearRegression()
regressor.fit(x, y)
print(regressor.coef_)
print(regressor.intercept_)

################ Train Test Split ###########################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1234)

regressor.fit(x_train, y_train)
print(regressor.coef_)
print(regressor.intercept_)

y_pred = regressor.predict(x_test)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

print(mean_squared_error(y_test, y_pred))
print(mean_absolute_error(y_test, y_pred))
print(r2_score(y_test, y_pred))