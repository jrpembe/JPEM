import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("C:\\JPEM_Git_Main\\JPEM\\JPEM_Datacamp\\data\\tuition.csv")
df.head()
fig, ax = plt.subplots()

mean_tuition = df["tuition"].mean()

sns.histplot(df['tuition'], ax=ax)
ax.set(xlabel = "tuition",
       ylabel = "Distribution",
       title = "Tuition Distribution",
       xlim=(0,100000))
ax.axvline(x=mean_tuition, color='b', label = 'My Budget', linestyle = '--')

# Combining two plots

# fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(7,4))

# sns.histplot(df['tuition'], stat='density', ax=ax0)
# sns.histplot(df.query('State == "MN')['tuition'], stat='density', ax=ax1)

# ax1.set(xlabel = 'Tuition (MN)', xlim=(0,100000))
# ax1.avline(x=20000, label = 'My Budget', linestyle = '--')
# ax1.legend()
