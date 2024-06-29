from statsmodels.formula.api import ols
import pandas as pd
# OLS = Ordinary Least Squares

smi = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/SwedishMotorInsurance.csv')

mdl_payment_vs_claims = ols("Payment ~ Claims", data=smi)

mdl_payment_vs_claims = mdl_payment_vs_claims.fit()

print(mdl_payment_vs_claims.params)