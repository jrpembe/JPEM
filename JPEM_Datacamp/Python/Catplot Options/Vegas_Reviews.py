import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/lasvegas_tripadvisor.csv")

# facetgrid
sns.catplot(
    x="Traveler type",
    kind="count",
    col="User continent",
    col_wrap=3,
    palette=sns.color_palette("Set1"),
    data=reviews
)
plt.show()

# save your graphic as an object "ax"
# use matplotlib to update specific items of the object
ax = sns.catplot(
    x="Traveler type",
    kind="count",
    col="User continent",
    col_wrap=3,
    palette=sns.color_palette("Set1"),
    data=reviews
)
ax.fig.suptitle("Hotel Score by Traveler Type & User Continent")
ax.set_axis_labels("Traveler Type", "Number of Reviews")
plt.subplots_adjust(top=.9)
plt.show()