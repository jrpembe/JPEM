import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/cars.csv")

cars["engine_fuel"] = cars["engine_fuel"].astype("category")
codes = cars["engine_fuel"].cat.codes
categories = cars["engine_fuel"]
dict(zip(codes, categories))

# one-hot encoding
cars[["odometer_value", "color"]].head()

cars_onehot = pd.get_dummies(cars[["odometer_value", "color"]])

cars_onehot.astype(int).head()

cars_onehot = pd.get_dummies(cars, columns=["color"], prefix="")
cars_onehot.head()

# NaN values get their own column