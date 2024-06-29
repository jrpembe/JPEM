import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols
import numpy as np

fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

bream = fish[fish["species"] == "Bream"]

sns.regplot(x = "length_cm",
            y = "mass_g",
            data=bream,
            ci=None)

plt.show()

# response on the left, exploratory variable on the right
mdl_mass_vs_length = ols("mass_g ~ length_cm", data=bream).fit()
print(mdl_mass_vs_length.params)

explanatory_data = pd.DataFrame({"length_cm": np.arange(20,41)})
print(mdl_mass_vs_length.predict(explanatory_data))

# Predicting inside a DataFrame
explanatory_data = pd.DataFrame(
    {"length_cm": np.arange(20,41)}
)
prediction_data = explanatory_data.assign(
    mass_g=mdl_mass_vs_length.predict(explanatory_data)
)

# predicting the mass of a Bream of length "x"
print(prediction_data)

fig = plt.figure()
sns.regplot(x = "length_cm",
            y = "mass_g",
            data=bream,
            ci=None)
sns.scatterplot(x = "length_cm",
            y = "mass_g",
            data=prediction_data,
            color="red",
            marker = "s")

plt.show()

# Extrapolating

little_bream = pd.DataFrame({"length_cm": [10]})

pred_little_bream = little_bream.assign(
    mass_g = mdl_mass_vs_length.predict(little_bream))

print(pred_little_bream)
# The predicted mass is a negative number, so the model does not perform well

# Fitted Values
print(mdl_mass_vs_length.fittedvalues)

# Alternatively
explanatory_data = bream["length_cm"]
print(mdl_mass_vs_length.predict(explanatory_data))

# Residuals - Actual Response minus Predicted Response
print(mdl_mass_vs_length.resid)

# Model Summary
mdl_mass_vs_length.summary()

# Regression to the Mean
