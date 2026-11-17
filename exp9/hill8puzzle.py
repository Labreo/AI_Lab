initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbours(state):
    neighbours = []
    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[new_pos] = new_state[new_pos], new_state[blank]
            neighbours.append(tuple(new_state))
    return neighbours


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def hill_climbing(initial):
    current = initial

    print("Initial State:")
    print_board(current)
    print("Heuristic:", heuristic(current))
    print()

    while current != goal:
        neighbours = get_neighbours(current)
        best = neighbours[0]

        for n in neighbours:
            if heuristic(n) < heuristic(best):
                best = n

        if heuristic(best) >= heuristic(current):
            print("No better neighbour found")
            print("Goal not reached")
            return
        current = best

        print("Best Move:")
        print_board(current)
        print("Heuristic:", heuristic(current))
        print()

    print("Goal reached :)")
    print("Goal Matrix:")
    print_board(current)

hill_climbing(initial)
