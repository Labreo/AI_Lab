from collections import defaultdict
from collections import deque

def bfs(S,graph,n):
    visted = [False] * (n + 1)
    Q = deque()
    Q.append(S)
    visted[S] = True

    while Q:
        u = Q.popleft()
        print(u, end=" ")
        for v in graph[u]:
            if not visted[v]:
                visted[v] = True
                Q.append(v)

def main():
    n = int(input("No of vertices:"))
    e = int(input("No of edges:"))
    
    graph = defaultdict(list)
    for i in range(e):
        u, v = map(int, input(f"Enter edge {i+1} (u v separated by space): ").split())
        graph[u].append(v)
        graph[v].append(u)
    
    S = int(input("Enter the source vertex:"))
    bfs(S, graph, n)


if __name__ == "__main__":
    main()