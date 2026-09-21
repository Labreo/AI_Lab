from collections import deque

def display(state):
    ma, ca, mb, cb, boat_side = state
    print("Current State : ")
    print("Side A \t\t\tSide B")
    for i in range(ma):
        print("M", end=" ")
    print("\t\t\t", end="")
    for i in range(mb):
        print("M", end=" ")
    print()
    for i in range(ca):
        print("C", end=" ")
    print("\t\t\t", end="")
    for i in range(cb):
        print("C", end=" ")
    print()
    print("Boat Side : " + boat_side)
    print()

def is_valid_state(ma, ca, mb, cb,boat_side):
    if ma >= 0 and mb >= 0 and ca >= 0 and cb >= 0 and (ma == 0 or ma >= ca) and (mb == 0 or mb >= cb):
        return True
    return False

def get_possible_moves(state):
    ma, ca, mb, cb, boat_side = state
    possible_moves = []
    if boat_side == 'A':
        new_states = [
            (ma-2, ca, mb+2, cb, 'B'),  # Move two missionaries
            (ma, ca-2, mb, cb+2, 'B'),  # Move two cannibals
            (ma-1, ca-1, mb+1, cb+1, 'B'),  # Move one missionary and one cannibal
            (ma-1, ca, mb+1, cb, 'B'),  # Move one missionary
            (ma, ca-1, mb, cb+1, 'B')   # Move one cannibal
        ]
    else:
        new_states = [
            (ma+2, ca, mb-2, cb, 'A'),  # Move two missionaries
            (ma, ca+2, mb, cb-2, 'A'),  # Move two cannibals
            (ma+1, ca+1, mb-1, cb-1, 'A'),  # Move one missionary and one cannibal
            (ma+1, ca, mb-1, cb, 'A'),  # Move one missionary
            (ma, ca+1, mb, cb-1, 'A')   # Move one cannibal
        ]
    
    for new_state in new_states:
        if is_valid_state(*new_state):
            possible_moves.append(new_state)
    
    return possible_moves

def bfs_solution(start_state):
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    
    while queue:
        (current_state, path) = queue.popleft()
        if current_state == (0, 0, num_missionaries, num_cannibals, 'B'):
            return path + [current_state]
        
        for next_state in get_possible_moves(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    
    return None

num_missionaries = int(input("Enter the number of missionaries: "))
num_cannibals = int(input("Enter the number of cannibals: "))

start_state = (num_missionaries, num_cannibals, 0, 0, 'A')
solution_path = bfs_solution(start_state)

if solution_path:
    for state in solution_path:
        display(state)
    print("Solution found!")
else:
    print("No solution exists.")
