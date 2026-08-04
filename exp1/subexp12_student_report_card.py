"""
Sub-experiment 12: Comprehensive Student Report Card System (User Input Driven)
Calculates Theory + Practical/Lab marks for 5 subjects across 2 semesters, SGPA per sem, % per sem, and overall CGPA & Percentage.
"""

def get_mark_input(prompt, max_val):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= max_val:
                return val
            print(f"Invalid input! Marks must be between 0 and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def marks_to_grade_point(percentage):
    if percentage >= 90:
        return 10.0, "O"
    elif percentage >= 80:
        return 9.0, "A+"
    elif percentage >= 70:
        return 8.0, "A"
    elif percentage >= 60:
        return 7.0, "B+"
    elif percentage >= 50:
        return 6.0, "B"
    elif percentage >= 40:
        return 5.0, "C"
    else:
        return 0.0, "F"

def input_semester_data(sem_num, subject_names=None):
    print(f"\n=======================================================")
    print(f"            ENTER MARKS FOR SEMESTER {sem_num}           ")
    print(f"=======================================================")
    
    subjects = []
    
    for i in range(1, 6):
        if subject_names and len(subject_names) >= i:
            default_name = subject_names[i-1]
            sub_name = input(f"\nSubject {i} Name [{default_name}]: ").strip()
            if not sub_name:
                sub_name = default_name
        else:
            sub_name = input(f"\nEnter Subject {i} Name: ").strip()
            if not sub_name:
                sub_name = f"Subject_{i}"

        print(f"--- Entering Marks for {sub_name} ---")
        theory_marks = get_mark_input(f"  Enter Theory Marks (out of 100): ", 100)
        lab_marks = get_mark_input(f"  Enter Lab/Practical Marks (out of 50): ", 50)
        
        total_obtained = theory_marks + lab_marks
        max_marks = 150
        percentage = (total_obtained / max_marks) * 100
        gp, grade = marks_to_grade_point(percentage)

        subjects.append({
            "name": sub_name,
            "theory": theory_marks,
            "lab": lab_marks,
            "total": total_obtained,
            "max": max_marks,
            "percentage": percentage,
            "gp": gp,
            "grade": grade
        })

    # SGPA Calculation (Assuming equal weightage/credits across the 5 subjects)
    total_gp = sum(s["gp"] for s in subjects)
    sgpa = total_gp / 5.0

    total_sem_obtained = sum(s["total"] for s in subjects)
    total_sem_max = sum(s["max"] for s in subjects)
    sem_percentage = (total_sem_obtained / total_sem_max) * 100

    return {
        "sem_num": sem_num,
        "subjects": subjects,
        "total_obtained": total_sem_obtained,
        "total_max": total_sem_max,
        "percentage": sem_percentage,
        "sgpa": sgpa
    }

def print_report_card(student_name, roll_no, sem1_data, sem2_data):
    print("\n" + "="*75)
    print(f"{'STUDENT ACADEMIC REPORT CARD':^75}")
    print("="*75)
    print(f" Student Name : {student_name:<30} Roll No : {roll_no}")
    print("="*75)

    for sem_data in [sem1_data, sem2_data]:
        print(f"\n--- SEMESTER {sem_data['sem_num']} DETAILS ---")
        print(f"{'Subject Name':<20} | {'Theory(100)':<11} | {'Lab(50)':<8} | {'Total(150)':<10} | {'Grade':<5} | {'GP':<4}")
        print("-" * 75)
        for s in sem_data["subjects"]:
            print(f"{s['name']:<20} | {s['theory']:^11.1f} | {s['lab']:^8.1f} | {s['total']:^10.1f} | {s['grade']:^5} | {s['gp']:^4.1f}")
        print("-" * 75)
        print(f" Semester {sem_data['sem_num']} Total Marks : {sem_data['total_obtained']:.1f} / {sem_data['total_max']}")
        print(f" Semester {sem_data['sem_num']} Percentage  : {sem_data['percentage']:.2f}%")
        print(f" Semester {sem_data['sem_num']} SGPA        : {sem_data['sgpa']:.2f}")

    # Overall Metrics
    overall_obtained = sem1_data["total_obtained"] + sem2_data["total_obtained"]
    overall_max = sem1_data["total_max"] + sem2_data["total_max"]
    overall_percentage = (overall_obtained / overall_max) * 100
    cgpa = (sem1_data["sgpa"] + sem2_data["sgpa"]) / 2.0

    print("\n" + "="*75)
    print(f"{'CUMULATIVE PERFORMANCE SUMMARY':^75}")
    print("="*75)
    print(f" Total Marks (Sem 1 + Sem 2) : {overall_obtained:.1f} / {overall_max}")
    print(f" Overall Aggregate Percentage: {overall_percentage:.2f}%")
    print(f" Semester 1 SGPA             : {sem1_data['sgpa']:.2f}")
    print(f" Semester 2 SGPA             : {sem2_data['sgpa']:.2f}")
    print(f" Final CGPA                  : {cgpa:.2f}")
    print("="*75 + "\n")

def main():
    print("=======================================================")
    print("      STUDENT REPORT CARD GENERATOR (2 SEMESTERS)       ")
    print("=======================================================")
    
    student_name = input("Enter Student Name: ").strip()
    if not student_name:
        student_name = "John Doe"
        
    roll_no = input("Enter Roll Number: ").strip()
    if not roll_no:
        roll_no = "101"

    sem1_data = input_semester_data(1)
    sem2_data = input_semester_data(2)

    print_report_card(student_name, roll_no, sem1_data, sem2_data)

if __name__ == "__main__":
    main()
