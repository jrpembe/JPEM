import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/cars.csv")

cars['manufacturer_name'] = cars['manufacturer_name'].astype('category')

# use .cat.codes

cars['manufacturer_name'] = cars['manufacturer_name'].cat.codes

print(cars[['manufacturer_name', 'model_name']])

cars['manufacturer_name'] = cars['manufacturer_name'].astype('category')
codes = cars['manufacturer_name'].cat.codes
categories = cars['manufacturer_name']

name_map = dict(zip(codes, categories))
print(name_map)

cars['manufacturer_name'] = cars['manufacturer_name'].cat.codes

cars['manufacturer_name'].map(name_map)

# Boolean coding 
cars['body_type'].str.contains("van", regex=False)

cars["van_code"] = np.where(
    cars['body_type'].str.contains("van", regex=False), 1, 0)

cars['van_code'].value_counts()

# one-hot encoding