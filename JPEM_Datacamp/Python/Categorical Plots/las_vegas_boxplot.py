import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/lasvegas_tripadvisor.csv")
reviews.info()

reviews["Score"].value_counts()
sns.set(font_scale=1.4)
sns.set_style("whitegrid")
sns.catplot(
    x="Pool",
    y="Score",
    data=reviews,
    kind="box",
    hue="Pool"
    )

plt.show()

sns.boxplot(data=reviews, x="Pool", y="Score", hue="Pool")
plt.show()

