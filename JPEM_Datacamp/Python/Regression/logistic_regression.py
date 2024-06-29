import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols


fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

fish.head()

sns.displot(data=fish,
            x='mass_g',
            col="species",
            col_wrap=2,
            bins=9)

plt.show()

summary_stats = fish.groupby("species")["mass_g"].mean()
print(summary_stats)

mdl_mass_vs_species = ols("mass_g ~ species", data = fish).fit()

print(mdl_mass_vs_species.params)

# This model produces negative slopes for Perch and Roach fish, we can fix this as follows:
# all coefficients should be given relative to zero (fitting the linear regression without an intercept)

mdl_mass_vs_species2 = ols("mass_g ~ species + 0", data=fish).fit()
print(mdl_mass_vs_species2.params)

# When you only have a single categorical explanatory variable, the
# linear regression coefficients are simply the means of each category
