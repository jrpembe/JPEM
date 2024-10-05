import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/housing.csv", header=None, delimiter=r"\s+", names=column_names)

y = df["MEDV"]
x = df.drop(["MEDV"], axis=1)

################ Linear Regression ###########################

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

################ Visualization of data and results ###########################

print(np.shape(df))
# Summarize the data to see the distribution of data
print(df.describe())


fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in df.items():
    sns.boxplot(y=k, data=df, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in df.items():
    sns.histplot(v, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

plt.figure(figsize=(20, 10))
sns.heatmap(df.corr().abs(),  annot=True)