import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols
import numpy as np


fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

perch = fish[fish["species"] == "Perch"]
print(perch.head())

sns.regplot(x = "length_cm",
            y = "mass_g",
            data = perch,
            ci=None)

plt.show()

# The relationship for Perch is not linear. Lets try cubed instead
perch["length_cm_cubed"] = perch["length_cm"]**3

sns.regplot(x = "length_cm_cubed",
            y = "mass_g",
            data = perch,
            ci=None)

plt.show()

mdl_perch = ols("mass_g ~ length_cm_cubed", data=perch).fit()
mdl_perch.params

explanatory_data = pd.DataFrame({"length_cm_cubed": np.arange(10, 41, 5) ** 3,
                                 "length_cm": np.arange(10, 41, 5)})

prediction_data = explanatory_data.assign(
    mass_g=mdl_perch.predict(explanatory_data)
)
print(prediction_data)

fig = plt.figure()
sns.regplot(x = "length_cm_cubed",
            y = "mass_g",
            data = perch,
            ci=None)
sns.scatterplot(data=prediction_data,
                x = "length_cm_cubed",
                y = "mass_g",
                color="red", marker = "s")

fig = plt.figure()
sns.regplot(x = "length_cm",
            y = "mass_g",
            data = perch,
            ci=None)
sns.scatterplot(data=prediction_data,
                x = "length_cm",
                y = "mass_g",
                color="red", marker = "s")