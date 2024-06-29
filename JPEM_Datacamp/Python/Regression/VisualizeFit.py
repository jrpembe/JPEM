import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np 
import statsmodels.api as sm
from statsmodels.api import qqplot
from statsmodels.formula.api import ols

# Load the data
fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

# Filter data for Bream and Perch
bream = fish[fish["species"] == "Bream"]
perch = fish[fish["species"] == "Perch"]

# Fit linear models
mdl_bream = ols("mass_g ~ length_cm", data=bream).fit()
mdl_perch = ols("mass_g ~ length_cm", data=perch).fit()

# Plot regression for Bream
plt.figure()
sns.regplot(x="length_cm", y="mass_g", ci=None, data=bream)
plt.title("Bream: Length vs Mass")
plt.xlabel("Length (cm)")
plt.ylabel("Mass (g)")
plt.show()

# Plot regression for Perch
plt.figure()
sns.regplot(x="length_cm", y="mass_g", ci=None, data=perch)
plt.title("Perch: Length vs Mass")
plt.xlabel("Length (cm)")
plt.ylabel("Mass (g)")
plt.show()

# Residual plot for Bream
plt.figure()
sns.residplot(x=mdl_bream.fittedvalues, y=bream["mass_g"], lowess=True)
plt.title("Bream: Residuals vs Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Residual plot for Perch
plt.figure()
sns.residplot(x=mdl_perch.fittedvalues, y=perch["mass_g"], lowess=True)
plt.title("Perch: Residuals vs Fitted Values")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()

# Q-Q plot for Bream
plt.figure()
qqplot(data=mdl_bream.resid, fit=True, line="45")
plt.title("Bream: Q-Q Plot of Residuals")
plt.show()

# Q-Q plot for Perch
plt.figure()
qqplot(data=mdl_perch.resid, fit=True, line="45")
plt.title("Perch: Q-Q Plot of Residuals")
plt.show()

# Scale-Location plot for Bream
model_norm_residuals_bream = mdl_bream.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt_bream = np.sqrt(np.abs(model_norm_residuals_bream))
plt.figure()
sns.regplot(x=mdl_bream.fittedvalues, y=model_norm_residuals_abs_sqrt_bream, ci=None, lowess=True)
plt.title("Bream: Scale-Location Plot")
plt.xlabel("Fitted Values")
plt.ylabel("SQRT of ABS Values of Standardized Residuals")
plt.show()

# Scale-Location plot for Perch
model_norm_residuals_perch = mdl_perch.get_influence().resid_studentized_internal
model_norm_residuals_abs_sqrt_perch = np.sqrt(np.abs(model_norm_residuals_perch))
plt.figure()
sns.regplot(x=mdl_perch.fittedvalues, y=model_norm_residuals_abs_sqrt_perch, ci=None, lowess=True)
plt.title("Perch: Scale-Location Plot")
plt.xlabel("Fitted Values")
plt.ylabel("SQRT of ABS Values of Standardized Residuals")
plt.show()
