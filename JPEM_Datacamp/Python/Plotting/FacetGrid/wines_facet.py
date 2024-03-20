import seaborn as sns 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# # Creating a FacetGrid and mapping boxplot
# g = sns.FacetGrid(df, col='quality', col_order=[3, 4, 5, 6, 7, 8], col_wrap=3)
# g.map(sns.boxplot, 'volatile acidity')

# plt.show()


# Creating a FacetGrid and mapping scatterplot with 'volatile acidity' and 'alcohol'
g = sns.FacetGrid(df, col='quality', col_order=[3, 4, 5, 6, 7, 8], col_wrap=3)
g.map(plt.scatter, 'volatile acidity', 'alcohol')

plt.show()