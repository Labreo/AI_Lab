def steepest_ascent_hill_climbing(start_state, goal_state, heuristic_val, neighbors_map):
    current_state = start_state
    traversal_order = [current_state]
    
    while True:
        best_neighbour = None
        best_heuristic = float("-inf")
        
        for neighbor in neighbors_map.get(current_state, []):
            heuristic = heuristic_val.get(neighbor)
            if heuristic is not None and heuristic > best_heuristic:
                best_heuristic = heuristic
                best_neighbour = neighbor
        
        if best_neighbour is None or best_heuristic <= heuristic_val[current_state]:
            if current_state == goal_state:
                return traversal_order, "Reached goal state"
            elif best_heuristic == heuristic_val[current_state]:
                return traversal_order, "Stuck on local maxima or shoulder (plateau)"
            else:
                return traversal_order, "Stuck in local minima"
            
        current_state = best_neighbour
        traversal_order.append(current_state)

if __name__ == "__main__":
    num_states = int(input("Enter the total number of states: "))
    
    neighbors_map = {}
    heuristic_val = {}
    
    for _ in range(num_states):
        state = input("Enter state: ")
        neighbours = input(f"Enter neighbours of {state} (separated by space): ").split()
        neighbors_map[state] = neighbours
        if state not in heuristic_val:
            heuristic_val[state] = int(input(f"Enter heuristic value of {state}: "))
        for neighbour in neighbours:
            if neighbour not in heuristic_val:
                heuristic_val[neighbour] = int(input(f"Enter heuristic value of {neighbour}: "))
        
    start_state = input("Enter start state: ")
    if start_state not in heuristic_val:
        heuristic_val[start_state] = int(input(f"Enter the heuristic value of {start_state}: "))
    goal_state = input("Enter the goal state: ")

    traversal_order, message = steepest_ascent_hill_climbing(start_state, goal_state, heuristic_val, neighbors_map)
    print(message)
    print("Traversal order: ", traversal_order)
