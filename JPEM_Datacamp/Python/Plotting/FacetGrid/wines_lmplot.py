import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# Creating the scatterplot using lmplot without the trend line and error bars
sns.lmplot(x='volatile acidity', y='alcohol', data=df, col='quality', col_order=[3, 4, 5, 6, 7, 8], col_wrap=3, 
           line_kws={'color': 'black'}, ci=None, fit_reg=False)

plt.show()