import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols
import numpy as np

churn = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/churn.csv")

mdl_churn_vs_recency_lm = ols("has_churned ~ time_since_last_purchase", data=churn).fit()

print(mdl_churn_vs_recency_lm.params)

intercept, slope = mdl_churn_vs_recency_lm.params

# Using a linear model to predict a binary outcome creates a problem
sns.scatterplot(x = "time_since_last_purchase",
                y="has_churned",
                data=churn)

plt.axline(xy1=(0, intercept),
           slope=slope)

plt.xlim(-10,10)
plt.ylim(-0.2,1.2)

plt.show()

# Lets use logistic regression (a type of generalized linear model) used when a reponse variable is binary
from statsmodels.formula.api import logit

mdl_churn_vs_recency_logit = logit("has_churned ~ time_since_last_purchase", data=churn).fit()

print(mdl_churn_vs_recency_logit.params)

# Plotting the logistic regression model
sns.scatterplot(x = "time_since_last_purchase", y = "has_churned", data = churn)
sns.regplot(x = "time_since_last_purchase", y = "has_churned", data = churn, ci = None, logistic = True)

# Create a range of time_since_last_purchase values
x_values = np.linspace(-20, 20, 400)
# Predict has_churned values using the logistic regression model
y_values = mdl_churn_vs_recency_logit.predict(pd.DataFrame({"time_since_last_purchase": x_values}))

# Plot the logistic curve
plt.plot(x_values, y_values, color = 'blue')

# Add the linear model line for comparison
plt.axline(xy1 = (0, intercept), slope = slope, color = "black")

plt.xlim(0, 10)
plt.ylim(-0.2, 1.2)

plt.show()

plt.show()