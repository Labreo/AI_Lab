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
    n = int(input("No of vertices: "))
    print(f"Enter the {n}x{n} adjacency matrix (row by row):")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                graph[i].append(j)
    source = int(input("Source vertex: "))
    target = int(input("Search node: "))
    d = bfs_search(source, target, graph, n)
    print(f"Distance from {source} to {target}: {d}")

if __name__ == "__main__":
    main()