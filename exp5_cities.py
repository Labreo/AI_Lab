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
            
            print("The path between those cities is:", path[::-1])
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
    n = int(input("No of cities: "))
    heuristics = {}
    print("Enter heuristic values (city heuristic):")
    for _ in range(n):
        city, h = input().split()
        heuristics[city] = int(h)
        
    e = int(input("No of paths between cities: "))
    graph = defaultdict(list)
    print("Enter paths between cities (City_1 City_2):")
    for _ in range(e):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
        
    s = input("Enter starting city: ")
    G = input("Enter destination city: ")
    
    best_first_search(graph, heuristics, s, G)

if __name__ == "__main__":
    main()
