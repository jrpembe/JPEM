import seaborn as sns 
import pandas as pd

df = pd.read_csv('C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv')

# regression plot
#sns.regplot(data=df, x="alcohol", y="pH")

# regplot vs lmplot

sns.regplot(data=df, x="alcohol", y="quality")

sns.lmplot(data=df, x="alcohol", y="quality")

# lmplot with faceting hue or col. Note, "type" does not exist in this dataset

# sns.lmplot(data=df, x="quality", y="alcohol", hue="type")

# sns.lmplot(data=df, x="quality", y="alcohol", col="type")