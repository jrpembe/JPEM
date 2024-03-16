import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 


df = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/wines.csv")

plt.figure(figsize=(10,6))

sns.regplot(data=df
            , y ='alcohol', x='volatile acidity', marker='+')
plt.show()

plt.figure(figsize=(10,6))
sns.residplot(data=df, x = 'volatile acidity', y='alcohol')
plt.show()