import matplotlib.pyplot as plt
import networkx as nx

# Create a list of connections from your original table
connections = [
    ("Laptop", "Mouse"),
    ("Laptop", "Keyboard"),
    ("Laptop", "Monitor"),
    ("Mouse", "Mouse Pad"),
    ("Keyboard", "Keyboard Tray"),
    ("Monitor", "HDMI Cable"),
    ("HDMI Cable", "Mouse"),
    ("Mouse Pad", "Monitor"),
]

# Create a directed graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(connections)

# Get the position of each node for visualization
pos = nx.spring_layout(G)  # You can choose other layouts like circular, shell, etc.

# Draw the nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', alpha=0.8)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Set plot title and show the plot
plt.title("Product Connections")
plt.axis('off')  # Turn off the axis
plt.show()
