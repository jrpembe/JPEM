import seaborn as sns 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# Assuming you have loaded your dataset into a DataFrame named df

# Creating the boxplot using catplot
sns.catplot(x='quality', y='volatile acidity', data=df, kind='box', order=[3, 4, 5, 6, 7, 8])
plt.show()