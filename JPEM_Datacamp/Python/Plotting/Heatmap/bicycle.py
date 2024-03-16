import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/hour.csv")

# Create a crosstab DataFrame with means rounded to integers
df_crosstab = pd.crosstab(df["mnth"], df["weekday"], values=df["registered"], aggfunc="mean").fillna(0).round(0).astype(int)

# Build a heatmap with Seaborn
sns.heatmap(df_crosstab, annot=True, fmt="d", cmap="YlGnBu", cbar=False, linewidths=.5, center=df_crosstab.loc[9,6])

# Adjust the annotation positions to avoid duplication
for i in range(len(df_crosstab)):
    for j in range(len(df_crosstab.columns)):
        if i >= j:
            plt.text(j + 0.5, i + 0.5, df_crosstab.iloc[i, j], ha='center', va='center', color='black')

# Display the plot
plt.show()

