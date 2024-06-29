import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np 
from statsmodels.formula.api import ols


fish = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fish.csv')

# Quantifying model fit using coefficient of determination or R-Squared
# r-squared for one explanatory variable, R-sqaured when you have more than one

bream = fish[fish["species"] == "Bream"]
perch = fish[fish["species"] == "Perch"]

sns.regplot(
    x = "length_cm",
    y = "mass_g",
    ci=None,
    data=bream)

sns.regplot(
    x = "length_cm",
    y = "mass_g",
    ci=None,
    data=perch)

mdl_bream = ols("mass_g ~ length_cm", data=bream).fit()

print(mdl_bream.summary())
print(mdl_bream.rsquared)

coefficient_determination = bream["length_cm"].corr(bream["mass_g"]) ** 2
print(coefficient_determination)

# Residual Standard Error (RSE) (square root of mse)
# Difference between an observed value and a predicted value

mse = mdl_bream.mse_resid
print('mse: ', mse)

rse = np.sqrt(mse)
print("rse: ", rse)

# Calculating RSE manually

residuals_sq = mdl_bream.resid ** 2
print("residuals sq: \n", residuals_sq)

resid_sum_of_sq = sum(residuals_sq)

print("resid sum of square: ", resid_sum_of_sq)

# degrees of freedom - number of observations minus number of model coefficients
deg_freedom = len(bream.index) - 2
print("deg freedom: ", deg_freedom)

# calculating rse
rse = np.sqrt(resid_sum_of_sq/deg_freedom)
print("rse: ", rse)

# Calculating RMSE
n_obs = len(bream.index)

# same as rse except you don't subtract the number of coefficients
rmse = np.sqrt(resid_sum_of_sq/n_obs)
print("rmse: ", rmse)