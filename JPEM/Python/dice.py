import numpy as np
import matplotlib.pyplot as plt

def roll_dice():
    return np.random.randint(1, 7) + np.random.randint(1, 7)

def monte_carlo_simulation(num_simulations):
    count_sevens = 0
    probabilities = []
    for i in range(1, num_simulations + 1):
        if roll_dice() == 7:
            count_sevens += 1
        probabilities.append(count_sevens / i)
    return probabilities

# Number of simulations
num_simulations = 10000

# Run the simulation
probabilities = monte_carlo_simulation(num_simulations)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(probabilities, label='Estimated Probability')
plt.axhline(y=1/6, color='r', linestyle='--', label='True Probability (1/6)')
plt.xlabel('Number of Simulations')
plt.ylabel('Probability')
plt.title('Monte Carlo Simulation for Rolling Two Dice and Getting a Sum of 7')
plt.legend()
plt.grid(True)
plt.show()
