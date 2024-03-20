import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame named df
df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# Create a PairGrid
g = sns.PairGrid(df[['volatile acidity', 'alcohol']])

# Map the plots to the grid
g = g.map_diag(sns.histplot)  # For diagonal: histogram
g = g.map_offdiag(sns.scatterplot)  # For off-diagonal: scatter plot

plt.show()
