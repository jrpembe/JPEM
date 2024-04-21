import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/lasvegas_tripadvisor.csv")


reviews["Traveler type"].value_counts().plot.bar()

# bar chart using Seaborn
sns.set(font_scale=1.3)
sns.set_style("darkgrid")
sns.catplot(
    x="Traveler type",
    y="Score",
    data=reviews,
    kind="bar",
    hue="Traveler type"
)
plt.show()

reviews["Traveler type"] = reviews["Traveler type"].astype("category")
reviews["Traveler type"].cat.categories

sns.set(font_scale=1.2)
sns.set_style("darkgrid")
sns.catplot(
    x="Traveler type",
    y="Score",
    data=reviews,
    kind="bar",
    hue="Tennis court"
)
plt.show()