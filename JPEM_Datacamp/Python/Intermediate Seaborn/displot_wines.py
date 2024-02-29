import matplotlib.pyplot as plt
import pandas as pd

# importing data using pandas
df = pd.read_csv('C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv')

# plotting the data using pandas
fig, ax = plt.subplots()

#ax.hist(df['alcohol'])

# alternatively

# df['alcohol'].plot.hist()

# plotting the data using seaborn distplot

import seaborn as sns 

sns.histplot(df['alcohol'])

sns.displot(df['alcohol'], kind='kde')

sns.displot(df['alcohol'], kde=True, bins=10)

sns.displot(df['alcohol'], kind='kde', rug=True, fill=True)

