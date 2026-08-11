from collections import defaultdict
from collections import deque

def distance_bfs(S,graph,n,Node):
    if S == Node:
        print(S, end = " ")
        return 0
    count = 1
    visted = [False] * (n + 1)
    Q = deque()
    Q.append(S)
    visted[S] = True

    while Q:
        u = Q.popleft()
        if Node == u:
           print(u, end=" ")
           count = count + 1
           return count
        
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
    Node = int(input("Enter the node you want to search for:"))
    S = int(input("Enter the source vertex:"))
    distance = distance_bfs(S, graph, n,Node)
    print(f"\nThe distance is {distance}")


if __name__ == "__main__":
    main()