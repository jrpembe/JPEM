import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame named df
df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# g = sns.JointGrid(data=df, x="volatile acidity", y="alcohol")
# g.plot(sns.regplot, sns.histplot)


# advanced JointGrid
g = sns.JointGrid(data=df, x="volatile acidity", y="alcohol")
g = g.plot_joint(sns.kdeplot)
g = g.plot_marginals(sns.kdeplot, shade=True)