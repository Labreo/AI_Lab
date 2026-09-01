import heapq
from collections import defaultdict

def best_first_search(graph, heuristics, s, G):
    open = []
    closed = set()
    parent = {s: None}
    
    heapq.heappush(open, (heuristics[s], s))
    
    while len(open) != 0:
        h, n = heapq.heappop(open)
        
        if n == G:
            curr = G
            path = []
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            
            print("Path:", path)
            return path
            
        closed.add(n)
        
        for successor in graph[n]:
            if successor not in closed and successor not in parent:
                parent[successor] = n
                heapq.heappush(open, (heuristics[successor], successor))
                closed.add(successor)

    print("G node is not reachable from S node")
    return None

def main():
    n = int(input("No of vertices: "))
    heuristics = {}
    print("Enter heuristic values (node heuristic):")
    for _ in range(n):
        node, h = input().split()
        heuristics[node] = int(h)
        
    e = int(input("No of edges: "))
    graph = defaultdict(list)
    print("Enter edges (u v):")
    for _ in range(e):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
        
    s = input("s node: ")
    G = input("G node: ")
    
    best_first_search(graph, heuristics, s, G)

if __name__ == "__main__":
    main()
