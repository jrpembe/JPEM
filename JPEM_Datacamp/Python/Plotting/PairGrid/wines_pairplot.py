import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame named df
df = pd.read_csv("C:\JPEM_Git_Main\JPEM\JPEM_Datacamp\data\wines.csv")

# sns.pairplot(df, vars=['volatile acidity', 'alcohol'], kind="reg",
#                        diag_kind="hist")


sns.pairplot(df.query("quality < 6"),
             vars=["volatile acidity",
                   "pH", "alcohol"],
             hue="quality", palette="bright",
             plot_kws={"alpha": 0.5})