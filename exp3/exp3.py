"""Experiment 3: Depth First Search (DFS) and Graph Operations"""
from collections import defaultdict, deque

def dfs(s, graph, n):
    visited = [False] * (n + 1)
    S = [s]
    
    print("DFS Traversal:", end=" ")
    while S:
        u = S.pop()
        if not visited[u]:
            visited[u] = True
            print(u, end=" ")
            for v in graph[u][::-1]:
                if not visited[v]:
                    S.append(v)
    print()

def checkpath(s, target, graph, n):
    visited = [False] * (n + 1)
    S = [s]
    while S:
        u = S.pop()
        if not visited[u]:
            visited[u] = True
            for v in graph[u][::-1]:
                if not visited[v]:
                    S.append(v)
    if visited[target]:
        return True
    else:
        return False

def noofconnectedverticestonode(s, graph, n):
    visited = [False] * (n + 1)
    S = [s]
    while S:
        u = S.pop()
        if not visited[u]:
            visited[u] = True
            for v in graph[u][::-1]:
                if not visited[v]:
                    S.append(v)
    return visited.count(True) - 1

def distancebetweentwonodes(s, target, graph, n):
    dist = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        if u == target:
            print(f"The distance between {s} and {target} is {dist[u]}")
            return dist[u]
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    print(f"Node {target} is not reachable from {s}")
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
        print("1. DFS Traversal")
        print("2. Check Path Existence")
        print("3. Count Connected Vertices to a Node")
        print("4. Distance Between Two Nodes")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            s = int(input("Source vertex: "))
            dfs(s, graph, n)
        elif choice == "2":
            s = int(input("Source vertex: "))
            target = int(input("Target vertex: "))
            print(f"Path exists: {checkpath(s, target, graph, n)}")
        elif choice == "3":
            s = int(input("Source vertex: "))
            print(f"Connected vertices count: {noofconnectedverticestonode(s, graph, n)}")
        elif choice == "4":
            s = int(input("Source vertex: "))
            target = int(input("Target vertex: "))
            distancebetweentwonodes(s, target, graph, n)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose between 1 and 5.")

if __name__ == "__main__":
    main()