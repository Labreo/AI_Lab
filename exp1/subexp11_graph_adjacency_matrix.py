"""Sub-experiment 11: Graph Representation using Adjacency Matrix & Matplotlib"""
import matplotlib.pyplot as plt
import networkx as nx

n = int(input("Enter number of vertices: "))
print(f"\nEnter the {n}x{n} adjacency matrix (row by row):")
adj = [list(map(int, input().split())) for _ in range(n)]

vertices = [chr(65 + i) for i in range(n)]
G = nx.Graph()
G.add_nodes_from(vertices)

edges = []
for i in range(n):
    for j in range(i + 1, n):
        if adj[i][j] == 1:
            edges.append((vertices[i], vertices[j]))
            G.add_edge(vertices[i], vertices[j])

print(f"\nVertices: {vertices}")
print(f"Edges: {edges}")

nx.draw(G, with_labels=True, node_color="lightgreen", node_size=1000, font_weight="bold")
plt.title("Graph using Adjacency Matrix")
plt.show()