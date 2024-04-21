import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/lasvegas_tripadvisor.csv")

sns.catplot(x="Pool", y="Score", data=reviews, kind="point")
plt.show()

sns.catplot(x="Spa", y="Score", data=reviews, kind="point",
            hue="Tennis court", dodge=True)
plt.show()

sns.catplot(x="Score", y="Review weekday", data=reviews, kind="point", join=False)
plt.show()

sns.catplot(x="Tennis court", data=reviews, kind="count", hue="Spa")
plt.show()
