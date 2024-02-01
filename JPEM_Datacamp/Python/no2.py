import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

air_df_mean = pd.read_csv("C:/Users/jason/OneDrive/Documents/Datacamp/DATACAMP - Data Scientist Professional with Python Career Track/data/no2.csv")

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