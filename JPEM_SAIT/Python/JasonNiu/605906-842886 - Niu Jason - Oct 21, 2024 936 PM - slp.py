# Import necessary libraries
import pulp
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpInteger, value

# Create the problem instance
prob = LpProblem("Cake_Production_Optimization", LpMaximize)

# Decision variables
x1 = LpVariable('Strawberry_Mango', lowBound=0, cat='Integer')
x2 = LpVariable('Chocolate_Cinnamon_Vanilla', lowBound=0, cat='Integer')
x3 = LpVariable('Pure_Mango_Banana', lowBound=0, cat='Integer')
x4 = LpVariable('Strawberry_Twist', lowBound=0, cat='Integer')

# Objective function coefficients
profit = {
    x1: 10.00,
    x2: 12.00,
    x3: 11.50,
    x4: 14.00
}

# Add the objective function to the problem
prob += lpSum([profit[var] * var for var in [x1, x2, x3, x4]]), "Total_Profit"

# Ingredient usage per cake type
ingredient_usage = {
    'Strawberry': {x1: 5, x2: 0, x3: 0, x4: 6},
    'Mango': {x1: 2, x2: 0, x3: 6, x4: 0},
    'Chocolate': {x1: 0, x2: 6, x3: 0, x4: 0},
    'Cinnamon': {x1: 0, x2: 2, x3: 0, x4: 0},
    'Vanilla': {x1: 0, x2: 3, x3: 0, x4: 0},
    'Banana': {x1: 0, x2: 0, x3: 3, x4: 0}
}

# Available inventory
available_inventory = {
    'Strawberry': 60,
    'Mango': 80,
    'Chocolate': 95,
    'Cinnamon': 56,
    'Vanilla': 96,
    'Banana': 100
}

# Add constraints to the problem: Ingredient usage should not exceed available inventory
for ingredient, usage in ingredient_usage.items():
    prob += lpSum([usage[var] * var for var in [x1, x2, x3, x4]]) <= available_inventory[ingredient], f"{ingredient}_Constraint"

# Solve the problem
prob.solve()

# Solution status
print(f"Status: {pulp.LpStatus[prob.status]}")

# Optimal values of decision variables
print("Optimal Production Plan:")
for var in [x1, x2, x3, x4]:
    print(f"{var.name}: {var.varValue}")

# Total Profit
print(f"Total Profit: ${value(prob.objective):.2f}")

