"""Experiment 2: BFS Search & Shortest Distance"""
from collections import defaultdict, deque

def bfs_search(source, target, graph, n):
    dist = {source: 0}
    q = deque([source])
    print("Traversal:", end=" ")
    while q:
        u = q.popleft()
        print(u, end=" ")
        if u == target:
            print()
            return dist[u]
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    print()
    return -1

def main():
    n, e = int(input("No of vertices: ")), int(input("No of edges: "))
    graph = defaultdict(list)
    for i in range(e):
        u, v = map(int, input(f"Edge {i+1} (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)
    target = int(input("Search node: "))
    source = int(input("Source vertex: "))
    d = bfs_search(source, target, graph, n)
    print(f"Distance from {source} to {target}: {d}")

if __name__ == "__main__":
    main()