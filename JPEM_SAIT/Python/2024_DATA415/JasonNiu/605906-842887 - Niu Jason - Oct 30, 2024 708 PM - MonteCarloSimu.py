import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given Data
revenue_mean = 75e6
revenue_std = 3.5e6

variable_expenses_mean = 5398393.74
variable_expenses_std = 2537882.978

fixed_expenses_total = 40970113.3

# Number of simulations
n_simulations = 10000

# Monte Carlo Simulation
np.random.seed(42)  # For reproducibility
revenue_sim = np.random.normal(revenue_mean, revenue_std, n_simulations)
variable_expenses_sim = np.random.normal(variable_expenses_mean, variable_expenses_std, n_simulations)
fixed_expenses_sim = np.full(n_simulations, fixed_expenses_total)

# Profit calculation
profit_sim = revenue_sim - (variable_expenses_sim + fixed_expenses_sim)

# Convert to a DataFrame for easier manipulation
df_simulation = pd.DataFrame({
    'Revenue': revenue_sim,
    'Variable Expenses': variable_expenses_sim,
    'Fixed Expenses': fixed_expenses_sim,
    'Profit': profit_sim
})

# Profit thresholds to evaluate
profit_thresholds = [i * 1e6 for i in range(1, 45)]
probabilities_below = []
probabilities_above = []

# Calculate probabilities for each threshold
for threshold in profit_thresholds:
    prob_below = (df_simulation['Profit'] < threshold).mean() * 100
    prob_above = (df_simulation['Profit'] >= threshold).mean() * 100
    probabilities_below.append(prob_below)
    probabilities_above.append(prob_above)

    print(f"Threshold: ${threshold/1e6:.1f}M")
    print(f"Probability below: {prob_below:.2f}%")
    print(f"Probability above: {prob_above:.2f}%")
    print("-" * 30)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot([t / 1e6 for t in profit_thresholds], probabilities_below, label='Probability Below Threshold', marker='o', linestyle='--')
plt.plot([t / 1e6 for t in profit_thresholds], probabilities_above, label='Probability Above Threshold', marker='o', linestyle='-')
plt.xlabel('Profit Threshold (Millions $)')
plt.ylabel('Probability (%)')
plt.title('Probability of Profit vs. Threshold')
plt.legend()
plt.grid(True)
plt.show()