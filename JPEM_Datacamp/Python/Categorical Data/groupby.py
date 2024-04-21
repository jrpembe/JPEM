import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

adult = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/adult.csv")

# splitting data using .groupby()

# These two lines of code can be replaced by a single line using groupby()
adult1 = adult[adult["Above/Below 50k"] == " <=50K"]
adult2 = adult[adult["Above/Below 50k"] == " >50K"]

#groupby_object = adult.groupby(by=["Above/Below 50k"])

# Selecting only numeric columns
numeric_columns = adult.select_dtypes(include=[np.number])

# Adding the target column to the numeric columns
numeric_columns["Above/Below 50k"] = adult["Above/Below 50k"]

# Group by and calculate the mean
grouped_means = numeric_columns.groupby(by=["Above/Below 50k"]).mean()

print(grouped_means)

# specifying columns, the example on Data Camp produces an error with single square brackets
adult.groupby(by=["Above/Below 50k"])[['Age', 'Education Num']].sum()
# grouped_sum = adult.groupby(by=["Above/Below 50k"])[['Age', 'Education Num']].sum()
# print(grouped_sum)

# groupby multiple columns
adult.groupby(by=["Above/Below 50k", "Marital Status"]).size()

gb = adult.groupby(by=[ "Workclass",
                        "Above/Below 50k", 
                        "Education"])

gb.head()