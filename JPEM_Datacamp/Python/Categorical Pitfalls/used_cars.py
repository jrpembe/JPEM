import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

cars = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/cars.csv")

cars["manufacturer_name"].describe()

# 90% memory reduction
print("As object: ", cars["manufacturer_name"].nbytes)
print("As category: ", cars["manufacturer_name"].astype('category').nbytes)

cars["odometer_value"].astype('object').describe()

# 60% memory reduction
print(f"As float: , {cars["odometer_value"].nbytes}")
print(f"As category: ", cars["odometer_value"].astype('category').nbytes)

# check - using the str() and apply() methods force the data back to object, 
# so you must convert again after using these
cars["color"] = cars["color"].astype('category')
cars["color"] = cars["color"].str.upper()
print(cars["color"].dtype)

# Look for missing values
cars["color"] = cars["color"].astype('category')
cars["color"].cat.set_categories(["black", "silver", "blue"]) 
cars["color"].value_counts(dropna=False)

# Using NumPy arrays
cars["number_of_photos"] = cars["number_of_photos"].astype("category")
cars["number_of_photos"].sum() # gives an error, categorical does not support sum
cars["number_of_photos"].astype(int).sum() # convert to an integer

print("As object: ", cars["price_usd"].nbytes)
print("As category: ", cars["price_usd"].astype('category').nbytes)

print("As object: ", cars["drivetrain"].nbytes)
print("As category: ", cars["drivetrain"].astype('category').nbytes)

print("As object: ", cars["model_name"].nbytes)
print("As category: ", cars["model_name"].astype('category').nbytes)