"""
Sub-experiment 10: Interactive Graph Representation using Adjacency List
"""

class GraphAdjacencyList:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if not self.directed and u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def print_vertices(self):
        vertices = list(self.adj_list.keys())
        print(f"\nVertices ({len(vertices)}): {vertices}")

    def print_edges(self):
        edges = []
        for u in self.adj_list:
            for v in self.adj_list[u]:
                if self.directed or (v, u) not in edges:
                    edges.append((u, v))
        print(f"Edges ({len(edges)}): {edges}")

    def display(self):
        print("\n--- Adjacency List Structure ---")
        if not self.adj_list:
            print("(Graph is empty)")
        for node, neighbors in self.adj_list.items():
            print(f"Vertex '{node}' -> {neighbors}")

def main():
    g = GraphAdjacencyList(directed=False)
    # Default sample graph
    sample_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for u, v in sample_edges:
        g.add_edge(u, v)

    while True:
        print("\n=============================================")
        print("  SUB-EXP 10: GRAPH (ADJACENCY LIST) MENU    ")
        print("=============================================")
        print("1. Display Adjacency List Structure")
        print("2. Print all Vertices")
        print("3. Print all Edges")
        print("4. Add a new Vertex")
        print("5. Add a new Edge (u, v)")
        print("6. Load Default Sample Graph (A-B-C-D-E)")
        print("7. Clear Graph")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-7): ").strip()
        
        if choice == '0':
            print("Exiting Graph Adjacency List sub-experiment.")
            break
        elif choice == '1':
            g.display()
        elif choice == '2':
            g.print_vertices()
        elif choice == '3':
            g.print_edges()
        elif choice == '4':
            v = input("Enter vertex name: ").strip()
            if v:
                g.add_vertex(v)
                print(f"Vertex '{v}' added.")
        elif choice == '5':
            u = input("Enter starting vertex (u): ").strip()
            v = input("Enter ending vertex (v): ").strip()
            if u and v:
                g.add_edge(u, v)
                print(f"Edge ({u}, {v}) added.")
        elif choice == '6':
            g = GraphAdjacencyList(directed=False)
            for u, v in sample_edges:
                g.add_edge(u, v)
            print("Sample graph loaded.")
        elif choice == '7':
            g = GraphAdjacencyList(directed=False)
            print("Graph cleared.")
        else:
            print("Invalid choice! Please enter a number between 0 and 7.")

if __name__ == "__main__":
    main()
