def evaluation_function(x):
    return -(x**2) + 5

def hill_climbing(start_x, step_size=0.1):
    current_x = round(start_x, 4)
    current_val = evaluation_function(current_x)
    
    step = 0
    print(f"Step {step}: Current state x = {current_x:.2f}, f(x) = {current_val:.4f}")

    while True:
        # Generate the two neighbouring states (x + step_size and x - step_size)
        neighbours = [round(current_x + step_size, 4), round(current_x - step_size, 4)]
        moved = False

        # Compare neighbours to current state
        for next_x in neighbours:
            next_val = evaluation_function(next_x)
            
            # If neighbour is better, move to it and continue search from new state
            if next_val > current_val:
                current_x = next_x
                current_val = next_val
                moved = True
                step += 1
                print(f"Step {step}: Moved to neighbour x = {current_x:.2f}, f(x) = {current_val:.4f}")
                break  # Move immediately to this neighbour and search again
        
        # If all neighbours checked and none is better: stop
        if not moved:
            print("\nAll neighbours checked. None are better.")
            print("Stopping search: Reached peak / local maximum.")
            break

    return current_x, current_val

def main():
    start_input = float(input("Enter starting value of x: "))
    peak_x, peak_val = hill_climbing(start_input)
    
    print("-" * 45)
    print(f"Optimal x: {peak_x:.2f}")
    print(f"Maximum f(x): {peak_val:.4f}")

if __name__ == "__main__":
    main()