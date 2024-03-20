import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame named df
df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# remove the comment from each line one at a time to see what the result

# calling head() shows the first 5 rows of the data (tail() shows the last 5)
# df.head()

# value_counts gives a quick look at the number of rows that fall into each category
# df['quality'].value_counts()

# describe() gives us essential statistics on the values in each column
# df.describe()

# info() reveals the variable data types and whether out data contains nulls
# df.info()

# use histograms to visualize numerical data

import seaborn as sns 
import matplotlib.pyplot as plt

sns.histplot(data=df, x="quality")
plt.show
