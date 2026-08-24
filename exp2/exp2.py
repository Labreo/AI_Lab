"""Experiment 2: Breadth First Search (BFS) Graph Traversal and Search"""
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

    while True:
        print("\n--- Menu ---")
        print("1. BFS Traversal")
        print("2. BFS Search")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        match choice:
            case "1":
                source = int(input("Source vertex: "))
                bfs(source, graph, n)
            case "2":
                source = int(input("Source vertex: "))
                target = int(input("Search node: "))
                d = bfs_search(source, target, graph, n)
                print(f"Distance from {source} to {target}: {d}")
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()