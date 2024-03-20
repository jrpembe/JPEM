import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame named df
df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# sns.jointplot(data=df, x="volatile acidity", y="alcohol", kind="hex")

g = (sns.jointplot(x = "volatile acidity",
                   y = "alcohol",
                   kind = "scatter",
                   xlim = (0, 1.8),
                   data=df.query("quality < 5"))
     .plot_joint(sns.kdeplot))