import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


air_df_mean = pd.read_csv("C:\\JPEM_Git_Main\\JPEM\\JPEM_Datacamp\\data\\no2.csv")

# Scatterplot
sns.relplot(
    x = "hour",
    y = "NO_2_mean",
    data = air_df_mean,
    kind = "scatter"
)

plt.show()

# Lineplot
sns.relplot(
    x = "hour",
    y = "NO_2_mean",
    data = air_df_mean,
    kind = "line",
    style = "location",
    hue = "location",
    markers = True,
    dashes = False
)

plt.show()

# Lineplot with confidence intervals

# when your data has more than one observations per hour
# Seaborn will automatically calculate CI
# set ci = "sd" to make confidence interval based on standard deviation