"""
Experiment 1 Runner Script
Use this script to easily launch any of the 12 sub-experiments in Experiment 1.
"""

import os
import subprocess
import sys

SUBEXPERIMENTS = {
    "1": ("Variables & Data Types", "subexp1_variables_datatypes.py"),
    "2": ("Menu Driven Calculator", "subexp2_calculator.py"),
    "3": ("Check Positive/Negative/Zero", "subexp3_number_check.py"),
    "4": ("Find Largest of 3 Numbers", "subexp4_largest_of_three.py"),
    "5": ("Print Numbers 1 to 10", "subexp5_print_1_to_10.py"),
    "6": ("Multiplication Table of a Number", "subexp6_multiplication_table.py"),
    "7": ("Multiplication Tables 1 to 10", "subexp7_multiplication_tables_1_to_10.py"),
    "8": ("Area of Circle Function", "subexp8_area_of_circle.py"),
    "9": ("List Operations", "subexp9_list_operations.py"),
    "10": ("Graph Adjacency List", "subexp10_graph_adjacency_list.py"),
    "11": ("Graph Adjacency Matrix", "subexp11_graph_adjacency_matrix.py"),
    "12": ("Student Report Card System", "subexp12_student_report_card.py"),
}

def main():
    exp_dir = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        print("\n=======================================================")
        print("               EXPERIMENT 1 SUB-EXPERIMENTS            ")
        print("=======================================================")
        for key, (title, filename) in SUBEXPERIMENTS.items():
            print(f"{key:>2}. {title:<35} ({filename})")
        print(" 0. Exit")
        print("=======================================================")

        choice = input("Enter sub-experiment number to run (0 to exit): ").strip()
        
        if choice == "0":
            print("Exiting Experiment 1 runner. Bye!")
            break
            
        if choice in SUBEXPERIMENTS:
            title, filename = SUBEXPERIMENTS[choice]
            filepath = os.path.join(exp_dir, filename)
            print(f"\n>>> Running Sub-experiment {choice}: {title} <<<\n")
            subprocess.run([sys.executable, filepath])
        else:
            print("Invalid selection! Please enter a number between 0 and 12.")

if __name__ == "__main__":
    main()
