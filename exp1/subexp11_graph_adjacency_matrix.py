"""
Sub-experiment 11: Interactive Graph Representation using Adjacency Matrix
"""

class GraphAdjacencyMatrix:
    def __init__(self, vertices=None, directed=False):
        self.vertices = sorted(list(vertices)) if vertices else []
        self.vertex_index = {v: i for i, v in enumerate(self.vertices)}
        self.size = len(self.vertices)
        self.matrix = [[0] * self.size for _ in range(self.size)]
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.vertex_index:
            self.vertices.append(v)
            self.vertices.sort()
            self.size = len(self.vertices)
            self.vertex_index = {v: i for i, v in enumerate(self.vertices)}
            # Reconstruct matrix
            new_matrix = [[0] * self.size for _ in range(self.size)]
            self.matrix = new_matrix

    def add_edge(self, u, v, weight=1):
        if u not in self.vertex_index:
            self.add_vertex(u)
        if v not in self.vertex_index:
            self.add_vertex(v)
        
        i, j = self.vertex_index[u], self.vertex_index[v]
        self.matrix[i][j] = weight
        if not self.directed:
            self.matrix[j][i] = weight

    def display(self):
        print("\n--- Adjacency Matrix ---")
        if not self.vertices:
            print("(Graph is empty)")
            return
        header = "    " + "  ".join(f"{v:^3}" for v in self.vertices)
        print(header)
        print("    " + "-" * (len(header) - 4))
        for i, row in enumerate(self.matrix):
            row_str = "  ".join(f"{val:^3}" for val in row)
            print(f"{self.vertices[i]} | {row_str}")

def main():
    nodes = ['A', 'B', 'C', 'D', 'E']
    sample_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    
    g = GraphAdjacencyMatrix(nodes, directed=False)
    for u, v in sample_edges:
        g.add_edge(u, v)

    while True:
        print("\n=============================================")
        print("  SUB-EXP 11: GRAPH (ADJACENCY MATRIX) MENU   ")
        print("=============================================")
        print("1. Display Adjacency Matrix")
        print("2. Add Edge (u, v)")
        print("3. Add Vertex")
        print("4. Reload Default Sample Graph")
        print("5. Clear Matrix")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-5): ").strip()
        
        if choice == '0':
            print("Exiting Graph Adjacency Matrix sub-experiment.")
            break
        elif choice == '1':
            g.display()
        elif choice == '2':
            u = input("Enter vertex u: ").strip()
            v = input("Enter vertex v: ").strip()
            if u and v:
                g.add_edge(u, v)
                print(f"Edge ({u}, {v}) added.")
        elif choice == '3':
            v = input("Enter vertex name: ").strip()
            if v:
                g.add_vertex(v)
                print(f"Vertex '{v}' added.")
        elif choice == '4':
            g = GraphAdjacencyMatrix(nodes, directed=False)
            for u, v in sample_edges:
                g.add_edge(u, v)
            print("Sample graph reloaded.")
        elif choice == '5':
            g = GraphAdjacencyMatrix([], directed=False)
            print("Matrix cleared.")
        else:
            print("Invalid choice! Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
