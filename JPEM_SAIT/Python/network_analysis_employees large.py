import csv
import networkx as nx
import pandas as pd
import random
import plotly.graph_objects as go

# Load connections from CSV
connections = []
with open('C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/connections.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) == 2:
            connections.append(tuple(row))

# Create NetworkX graph and add edges
G = nx.Graph()
G.add_edges_from(connections)

# Generate node positions using a layout algorithm
pos = nx.spring_layout(G)

# Extract node and edge information for Plotly
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Plotly trace for edges
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# Plotly trace for nodes
node_x = []
node_y = []
node_text = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(f'{node}<br>Connections: {G.degree[node]}')

# Node trace with color and size based on degree
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text,
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=[5 + 3 * G.degree[node] for node in G.nodes()],  # Node size by degree
        color=[G.degree[node] for node in G.nodes()],  # Color by degree
        colorbar=dict(
            thickness=15,
            title='Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

# Layout and create Plotly Figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Employee Network Connections',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20, l=5, r=5, t=40),
                    annotations=[dict(
                        text="Employee Network Visualization",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002)],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

fig.show()



