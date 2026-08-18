from collections import defaultdict

def dfs(source, graph, n):

    visited = [False] * (n + 1)
    S = []
    S.append(source)
    
    print("dfs Traversal:", end=" ")
    while S:
        u = S.pop()
       
        if not visited[u]:
            visited[u] = True
            print(u, end=" ")
            for v in range(n,-1,-1):
                if visited[v]==False:
                   S.append(v)
    print(S)







def main():
    n, e = int(input("No of vertices: ")), int(input("No of edges: "))
    graph = defaultdict(list)
    for i in range(e):
        u, v = map(int, input(f"Edge {i+1} (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)
    dfs(int(input("Source vertex: ")), graph, n)

if __name__ == "__main__":
    main()