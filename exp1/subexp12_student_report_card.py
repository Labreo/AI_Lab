"""Sub-experiment 12: Student Academic Report Card (2 Semesters, 5 Subjects each)"""

def get_grade(pct):
    for cut, gp, g in [(90, 10.0, "O"), (80, 9.0, "A+"), (70, 8.0, "A"), (60, 7.0, "B+"), (50, 6.0, "B"), (40, 5.0, "C")]:
        if pct >= cut: return gp, g
    return 0.0, "F"

def input_sem(sem):
    print(f"\n--- Enter Marks for Semester {sem} (5 Subjects) ---")
    subs = []
    for i in range(1, 6):
        name = input(f"Subject {i} Name: ").strip() or f"Sub{i}"
        th = float(input(f"  {name} Theory/IT Marks (out of 100): "))
        pr = float(input(f"  {name} Practical/Lab Marks (out of 50): "))
        tot = th + pr
        gp, g = get_grade((tot / 150) * 100)
        subs.append((name, th, pr, tot, g, gp))
    tot = sum(s[3] for s in subs)
    return {"sem": sem, "subs": subs, "tot": tot, "pct": (tot / 750) * 100, "sgpa": sum(s[5] for s in subs) / 5}
 
name = input("Enter Student Name: ").strip() or "Student"
roll = input("Enter Roll Number: ").strip() or "101"
sems = [input_sem(1), input_sem(2)]

print("\n" + "="*65 + f"\n{'STUDENT REPORT CARD':^65}\n" + "="*65)
print(f"Name: {name:<25} Roll No: {roll}\n" + "-"*65)
for s in sems:
    print(f"\nSemester {s['sem']}:\n{'Subject':<15} {'Theory':>7} {'Lab':>5} {'Total':>6} {'Grade':>6} {'GP':>4}")
    for sub, th, pr, tot, g, gp in s["subs"]:
        print(f"{sub:<15} {th:>7.1f} {pr:>5.1f} {tot:>6.1f} {g:>6} {gp:>4.1f}")
    print(f"Sem {s['sem']} Total: {s['tot']:.1f}/750 | Percentage: {s['pct']:.2f}% | SGPA: {s['sgpa']:.2f}")

tot_all = sum(s['tot'] for s in sems)
cgpa = sum(s['sgpa'] for s in sems) / len(sems)
print("="*65 + f"\nOVERALL: Marks: {tot_all:.1f}/1500 | Aggregate: {tot_all/15:.2f}% | CGPA: {cgpa:.2f}\n" + "="*65)
