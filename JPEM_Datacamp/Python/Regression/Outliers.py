import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols
import numpy as np

fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

roach = fish[fish["species"] == "Roach"]
print(roach.head())

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)
plt.show()

# Lets identify which length values are outliers
roach["extreme_l"] = (roach["length_cm"] < 15) | (roach["length_cm"] > 26)

fig = plt.figure()
sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)

sns.scatterplot(
    x="length_cm",
    y="mass_g",
    hue="extreme_l",
    data=roach)

# Now lets identify which weight values are outliers
roach["extreme_w"] = (roach["mass_g"] < 1)

fig = plt.figure()
sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None)

sns.scatterplot(
    x="length_cm",
    y="mass_g",
    hue="extreme_l",
    style="extreme_w",
    data=roach)

# Leverage is a measure of how extreme the explanatory variable values are
# Influence measures how much a model would change if you left the observation out of the dataset when modeling
# We get these values from summary_frame()

mdl_roach = ols("mass_g ~ length_cm", data=roach).fit()
summary_roach = mdl_roach.get_influence().summary_frame()

# Print summary frame to check contents
print(summary_roach.head())

# Assign leverage to the dataframe
roach["leverage"] = summary_roach["hat_diag"]

# Print the updated dataframe to verify leverage values
print(roach.head())

# Cook's Distance is the most common measure of influence
roach["cooks_dist"] = summary_roach["cooks_d"]
print(roach.head())

print(roach.sort_values("cooks_dist", ascending=False))

# Visualizing how influence works
roach_not_short = roach[roach["length_cm"] != 12.9]

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach,
            ci=None,
            line_kws={"color": "green"})

sns.regplot(x="length_cm",
            y="mass_g",
            data=roach_not_short,
            ci=None,
            line_kws={"color": "red"})