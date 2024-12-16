import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import requests

# Download the Excel file from the given URL
url = 'https://dissidia.oss-cn-beijing.aliyuncs.com/test/20241024/christian_names_network.xlsx'
response = requests.get(url)
with open('/tmp/christian_names_network.xlsx', 'wb') as file:
    file.write(response.content)

# Load the Excel file from /tmp/ directory
file_path = '/tmp/christian_names_network.xlsx'
df = pd.read_excel(file_path)

# Create a graph from the data
G = nx.Graph()

# Add edges from the dataframe
for idx, row in df.iterrows():
    G.add_edge(row['Name1'], row['Name2'])

# Analyze the network
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
avg_clustering = nx.average_clustering(G)
triangles = sum(nx.triangles(G).values()) // 3

print(f"Nodes: {num_nodes}")
print(f"Edges: {num_edges}")
print(f"Average Clustering Coefficient: {avg_clustering}")
print(f"Triangles: {triangles}")

# Create a 3D spring layout
pos_3d = nx.spring_layout(G, dim=3, seed=42)

# Get edge coordinates
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    edge_x.append([x0, x1, None])
    edge_y.append([y0, y1, None])
    edge_z.append([z0, z1, None])

# Get node coordinates
node_x = []
node_y = []
node_z = []
for node in G.nodes():
    x, y, z = pos_3d[node]
    node_x.append(x)
    node_y.append(y)
    node_z.append(z)

# Get degree centrality for coloring
degree_centrality = nx.degree_centrality(G)
node_colors = [degree_centrality[node] for node in G.nodes()]

# Create plotly graph object
fig = go.Figure()

# Add edges
for i in range(len(edge_x)):
    fig.add_trace(go.Scatter3d(
        x=edge_x[i], y=edge_y[i], z=edge_z[i],
        mode='lines',
        line=dict(color='gray', width=1),
        hoverinfo='none'
    ))

# Add nodes
fig.add_trace(go.Scatter3d(
    x=node_x, y=node_y, z=node_z,
    mode='markers+text',
    marker=dict(size=5, color=node_colors, colorscale='Blues', colorbar=dict(title="Degree Centrality")),
    text=list(G.nodes()),
    hoverinfo='text'
))

# Set layout
fig.update_layout(title="3D Christian Names Social Network Graph",
                  margin=dict(l=0, r=0, b=0, t=50),
                  scene=dict(
                      xaxis_title='X',
                      yaxis_title='Y',
                      zaxis_title='Z'
                  ))

fig.show()