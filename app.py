import logic as lg
import networkx as nx
import matplotlib.pyplot as plt

# Define the automaton using your logic module
start = lg.State(True, False, 0)
broken = lg.State(False, False, 1)
end = lg.State(False, True, 2)

lg.connect(start, end, "D", "ON")  # Turn switch on
lg.connect(end, start, "D", "OFF")  # Turn switch off
lg.connect(end, broken, "S", "BROKEN")  # Break switch

# Define the automaton
states = ["q0", "q1", "q2"]  # Nodes
transitions = [  # Edges with labels
    ("q0", "q2", "D / ON"),
    ("q2", "q0", "D / OFF"),
    ("q2", "q1", "S / BROKEN"),
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes
for state in states:
    G.add_node(state)

# Add edges with labels
for src, dest, label in transitions:
    G.add_edge(src, dest, label=label)

# Use a stable layout
pos = nx.circular_layout(G)  # Circular layout for clear separation

# Draw nodes and edges with curved connections
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=3000,
    font_size=10,
    font_weight="bold",
    arrowsize=20,
    connectionstyle="arc3,rad=0.2",  # Curved arrows
)

# Add edge labels
edge_labels = nx.get_edge_attributes(G, "label")  # Ensure all edge labels are fetched
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Show plot
plt.title("Automaton Visualization")
plt.show()

# Debugging: Print all edges and their labels
print("Edges and labels in the graph:")
for edge in G.edges(data=True):
    print(edge)

print(lg.run("DDDS"))