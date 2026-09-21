import heapq
import math

GOA_COORDINATES = {
    "Pernem": (15.72, 73.80),
    "Mapusa": (15.60, 73.81),
    "Bicholim": (15.59, 73.95),
    "Valpoi": (15.53, 74.13),
    "Porvorim": (15.53, 73.83),
    "Panaji": (15.49, 73.82),
    "Old Goa": (15.50, 73.91),
    "Vasco": (15.39, 73.81),
    "Ponda": (15.40, 74.01),
    "Margao": (15.28, 73.96),
    "Curchorem": (15.26, 74.11),
    "Canacona": (15.01, 74.04),
}

GOA_BUS_ROUTES = {
    "Pernem": {"Mapusa": 18},
    "Mapusa": {"Pernem": 18, "Bicholim": 16, "Porvorim": 8},
    "Bicholim": {"Mapusa": 16, "Valpoi": 17, "Old Goa": 20},
    "Valpoi": {"Bicholim": 17, "Ponda": 30},
    "Porvorim": {"Mapusa": 8, "Panaji": 5},
    "Panaji": {"Porvorim": 5, "Old Goa": 10, "Vasco": 28, "Margao": 33},
    "Old Goa": {"Panaji": 10, "Bicholim": 20, "Ponda": 18},
    "Vasco": {"Panaji": 28, "Margao": 30},
    "Ponda": {"Old Goa": 18, "Valpoi": 30, "Margao": 17, "Curchorem": 22},
    "Margao": {"Panaji": 33, "Vasco": 30, "Ponda": 17, "Curchorem": 18, "Canacona": 36},
    "Curchorem": {"Ponda": 22, "Margao": 18, "Canacona": 38},
    "Canacona": {"Margao": 36, "Curchorem": 38},
}

def calculate_heuristic(city, goal):
    lat1, lon1 = GOA_COORDINATES[city]
    lat2, lon2 = GOA_COORDINATES[goal]
    dx = (lon1 - lon2) * 107.0
    dy = (lat1 - lat2) * 111.0
    return round(math.sqrt(dx**2 + dy**2), 1)

def best_first_search(graph, heuristics, start, goal):
    open_list = []
    closed = set()
    parent = {start: None}

    heapq.heappush(open_list, (heuristics[start], start))

    while open_list:
        h, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path = path[::-1]

            total_distance = sum(
                graph[path[i]][path[i + 1]] for i in range(len(path) - 1)
            )
            return path, total_distance

        closed.add(current)

        for neighbor in graph[current]:
            if neighbor not in closed and neighbor not in parent:
                parent[neighbor] = current
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))

    return None, 0

def main():
    cities = list(GOA_COORDINATES.keys())
    print("=== KTC / Goa Bus Route Planner (Best-First Search) ===")
    print("Available Cities/Stops in Goa:")
    print(", ".join(cities))
    print("-" * 55)

    start = input("Enter starting city: ").strip().title()
    goal = input("Enter destination city: ").strip().title()

    if start not in GOA_COORDINATES or goal not in GOA_COORDINATES:
        print("\nError: One or both cities are not in the predefined Goa bus network.")
        return

    heuristics = {city: calculate_heuristic(city, goal) for city in GOA_COORDINATES}

    print(f"\nCalculated Heuristic Values (straight-line distance to {goal}):")
    for city, h_val in sorted(heuristics.items(), key=lambda x: x[1]):
        print(f"  {city:<12} : {h_val:>5} km")

    path, total_distance = best_first_search(GOA_BUS_ROUTES, heuristics, start, goal)

    print("\n" + "=" * 55)
    if path:
        print(f"Bus Route Found from {start} to {goal}:")
        print(" -> ".join(path))
        print(f"\nRoute Breakdown:")
        for i in range(len(path) - 1):
            hop_dist = GOA_BUS_ROUTES[path[i]][path[i + 1]]
            print(f"  {path[i]} -> {path[i+1]}: {hop_dist} km")
        print(f"\nTotal Bus Route Distance: {total_distance} km")
    else:
        print(f"Destination {goal} is not reachable by bus from {start}.")
    print("=" * 55)

if __name__ == "__main__":
    main()