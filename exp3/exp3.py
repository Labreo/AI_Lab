from collections import defaultdict,deque

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

def checkpath(s,target,graph,n):
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

def noofconnectedverticestonode(s,graph,n):
    visited = [False] * (n + 1)
    S = [s]
    while S:
        u = S.pop()
        if not visited[u]:
            visited[u] = True
            for v in graph[u][::-1]:
                if not visited[v]:
                    S.append(v)
    return visited.count(True)-1


def distancebetweentwonodes(s, target, graph, n):
    visited = [False] * (n + 1)
    visited[s] = True
    q = deque([s])
    d = 0
    while q:

        u= q.popleft()


        for v in graph[u]:
            if not visited[v]:
                if u == target:
                    print(f"the distance between {s} and {target} is {d-1}")

                else:
                    d=d+1   
                    visited[v] = True
                    q.append(v)
                    
    
        


def main():
    n, e = int(input("No of vertices: ")), int(input("No of edges: "))
    graph = defaultdict(list)
    for i in range(e):
        u, v = map(int, input(f"Edge {i+1} (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(int(input("s vertex: ")), graph, n)
    print("\nInput for checking path existance:")
    s=int(input("s vertex: "))
    t=int(input("target vertex: "))
    print(checkpath(s, t, graph, n))
    print("\nInput for checking no of connected vertices to a node:")
    s=int(input("s vertex: "))
    print(noofconnectedverticestonode(s, graph, n))
    print("\nInput for checking distance between two nodes:")
    s=int(input("s vertex: "))
    t=int(input("target vertex: "))
    distancebetweentwonodes(s, t, graph, n)
    
if __name__ == "__main__":
    main()