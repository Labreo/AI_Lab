from collections import deque
import math

def solve_water_jug_exact(m, n, dx, dy):
    # Step 1: Input Bounds and GCD Validation
    if dx < 0 or dx > m:
        print(f"\nError: Desired Jug 1 quantity ({dx}) must be between 0 and capacity {m}.")
        return
    if dy < 0 or dy > n:
        print(f"\nError: Desired Jug 2 quantity ({dy}) must be between 0 and capacity {n}.")
        return

    gcd_val = math.gcd(m, n)
    if (dx + dy) % gcd_val != 0:
        print(f"\nError: Target state ({dx}, {dy}) is mathematically impossible.")
        print(f"Reason: Total target water ({dx + dy}) is not a multiple of gcd({m}, {n}) = {gcd_val}.")
        return

    # Step 2: Breadth-First Search (BFS) to find the shortest path
    start_state = (0, 0)
    target_state = (dx, dy)

    # Base case: Already at target
    if start_state == target_state:
        print("\nInitial state matches target state. 0 steps required.")
        return

    # Queue stores: ((current_x, current_y), [list_of_transitions])
    queue = deque([(start_state, [("Initial State", start_state)])])
    visited = {start_state}
    found = False

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if (x, y) == target_state:
            found = True
            print(f"\nTarget state ({dx}, {dy}) reached in {len(path) - 1} steps:")
            print("-" * 68)
            print(f"{'Step':<6} | {'Action Taken':<28} | {'State (x, y)':<14} | {'Jug 1':<6} | {'Jug 2':<6}")
            print("-" * 68)
            for step_num, (action, (jx, jy)) in enumerate(path):
                print(f"{step_num:<6} | {action:<28} | {str((jx, jy)):<14} | {jx:<6} | {jy:<6}")
            print("-" * 68)
            break

        # 6 Production Rules
        transitions = [
            ("Fill Jug 1", (m, y)),
            ("Fill Jug 2", (x, n)),
            ("Empty Jug 1", (0, y)),
            ("Empty Jug 2", (x, 0)),
            ("Pour Jug 1 -> Jug 2", (x - min(x, n - y), y + min(x, n - y))),
            ("Pour Jug 2 -> Jug 1", (x + min(y, m - x), y - min(y, m - x))),
        ]

        for action, next_state in transitions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, next_state)]))

    if not found:
        print(f"\nTarget state ({dx}, {dy}) is unreachable with capacities ({m}, {n}).")

def main():
    try:
        m = int(input("Enter capacity of Jug 1 (m): "))
        n = int(input("Enter capacity of Jug 2 (n): "))
        dx = int(input("Enter desired quantity for Jug 1 (dx): "))
        dy = int(input("Enter desired quantity for Jug 2 (dy): "))

        if m <= 0 or n <= 0:
            print("Error: Capacities must be positive integers.")
            return

        solve_water_jug_exact(m, n, dx, dy)

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()