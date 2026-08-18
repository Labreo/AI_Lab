"""Experiment 1 Master Runner Script"""
import os, subprocess, sys

EXPERIMENTS = [
    ("Variables & Data Types", "subexp1_variables_datatypes.py"),
    ("Menu Driven Calculator", "subexp2_calculator.py"),
    ("Check Positive/Negative/Zero", "subexp3_number_check.py"),
    ("Find Largest of 3 Numbers", "subexp4_largest_of_three.py"),
    ("Print Numbers 1 to 10", "subexp5_print_1_to_10.py"),
    ("Multiplication Table", "subexp6_multiplication_table.py"),
    ("Tables 1 to 10", "subexp7_multiplication_tables_1_to_10.py"),
    ("Area of Circle", "subexp8_area_of_circle.py"),
    ("List Operations", "subexp9_list_operations.py"),
    ("Graph Adjacency List", "subexp10_graph_adjacency_list.py"),
    ("Graph Adjacency Matrix", "subexp11_graph_adjacency_matrix.py"),
    ("Student Report Card", "subexp12_student_report_card.py"),
]

def main():
    exp_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        print("\n=======================================================")
        print("              EXPERIMENT 1 SUB-EXPERIMENTS             ")
        print("=======================================================")
        for i, (title, f) in enumerate(EXPERIMENTS, 1):
            print(f"{i:>2}. {title:<30} ({f})")
        print(" 0. Exit")
        print("=======================================================")

        c = input("Choice (0-12): ").strip()
        if c == '0':
            print("Exiting Experiment 1 Runner.")
            break
        if c.isdigit() and 1 <= int(c) <= len(EXPERIMENTS):
            title, f = EXPERIMENTS[int(c) - 1]
            print(f"\n>>> Running: {title} <<<\n")
            subprocess.run([sys.executable, os.path.join(exp_dir, f)])
        else:
            print("Invalid selection! Please enter a number between 0 and 12.")

if __name__ == "__main__":
    main()
