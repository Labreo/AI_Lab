"""Experiment 2: Breadth First Search (BFS) Graph Traversal"""
from collections import defaultdict, deque

def bfs(source, graph, n):
    visited, q = [False] * (n + 1), deque([source])
    visited[source] = True
    print("BFS Traversal:", end=" ")
    while q:
        u = q.popleft()
        print(u, end=" ")
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    print()

def main():
    n, e = int(input("No of vertices: ")), int(input("No of edges: "))
    graph = defaultdict(list)
    for i in range(e):
        u, v = map(int, input(f"Edge {i+1} (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)
    bfs(int(input("Source vertex: ")), graph, n)

if __name__ == "__main__":
    main()