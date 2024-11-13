import csv
import random
import networkx as nx
import pandas as pd
import os 

# List of 10 employees
employees = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

# Randomly assign each employee between 5 and 15 connections
num_connections = {employee: random.randint(5, 15) for employee in employees}

# Initialize an empty list to store the connections
connections = []

# Create connections based on the number of connections each employee should have
for employee, num in num_connections.items():
    while len([conn for conn in connections if employee in conn]) < num:
        partner = random.choice(employees)
        if partner != employee and (employee, partner) not in connections and (partner, employee) not in connections:
            connections.append((employee, partner))

# Write the connections to a CSV file
file_name = 'variable_connections.csv'
with open(file_name, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    for connection in connections:
        csv_writer.writerow(connection)

print(f"CSV file saved at: {os.path.abspath(file_name)}")

# Create a graph object and add edges from the CSV connections
G = nx.Graph()
G.add_edges_from(connections)

# Create an adjacency matrix (as a pandas DataFrame)
adj_matrix = nx.to_pandas_adjacency(G)

# Calculate the sum of connections for each employee (degree of each node)
employee_connections = adj_matrix.sum(axis=1)

# Print the adjacency matrix and sum of connections
print("\nAdjacency Matrix:")
print(adj_matrix)

print("\nSum of Connections for Each Employee:")
print(employee_connections)

# Optionally, save the adjacency matrix to a CSV
adj_matrix.to_csv('adjacency_matrix.csv')
