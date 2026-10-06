def evaluation_function(x1, x2):
    return -(x1**2) - (x2**2) + 5

def steep_hill_climbing(start_x1, start_x2, step_size=0.1):
    current_x1 = round(start_x1, 4)
    current_x2 = round(start_x2, 4)
    current_val = evaluation_function(current_x1, current_x2)
    
    step = 0
    print(f"Step {step}: Current state x1 = {current_x1:.2f}, x2 = {current_x2:.2f}, f(x1,x2) = {current_val:.4f}")

    while True:
        neighbours1 = [round(current_x1 + step_size, 4), current_x1, round(current_x1 - step_size, 4)]
        neighbours2 = [round(current_x2 + step_size, 4), current_x2, round(current_x2 - step_size, 4)]
        
        best_x1 = current_x1
        best_x2 = current_x2
        best_val = current_val

        for next_x1 in neighbours1:
            for next_x2 in neighbours2:
                if next_x1 == current_x1 and next_x2 == current_x2:
                    continue
                next_val = evaluation_function(next_x1, next_x2)
                if next_val > best_val:
                    best_val = next_val
                    best_x1 = next_x1
                    best_x2 = next_x2

        if best_val > current_val:
            current_x1 = best_x1
            current_x2 = best_x2
            current_val = best_val
            step += 1
            print(f"Step {step}: Moved to neighbour x1 = {current_x1:.2f}, x2 = {current_x2:.2f}, f(x1,x2) = {current_val:.4f}")
        else:
            print("\nAll neighbours checked. None are better.")
            print("Stopping search: Reached peak / local maximum.")
            break

    return current_x1, current_x2, current_val

def main():
    start_input1 = float(input("Enter starting value of x1: "))
    start_input2 = float(input("Enter starting value of x2: "))
    step_size = float(input("Enter your step size"))
    peak_x, peak_y, peak_val = steep_hill_climbing(start_input1, start_input2, step_size)
    
    print("-" * 45)
    print(f"Optimal x1: {peak_x:.2f}") 
    print(f"Optimal x2: {peak_y:.2f}")
    print(f"Maximum f(x): {peak_val:.4f}")

if __name__ == "__main__":
    main()  