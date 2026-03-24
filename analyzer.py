import csv

def load_student_data(file_path):
    students = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "name": row["Name"],
                "math": int(row["Math"]),
                "physics": int(row["Physics"]),
                "chemistry": int(row["Chemistry"])
            }

            students.append(student)

    return students


def calculate_average(student):
    avg = ((student["math"] + student["physics"] + student["chemistry"]) / 3)
    return avg
def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B+'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'
def get_result(avg):
    if avg>=50:
        return 'Passed'
    return 'Failed'
def get_subject_topper(students,subject):
    return max(students,key=lambda x: x[subject])
def save_students_report(filename,students):
    with open(filename, "w") as file:
        
        file.write(f"{'Name':<8}  {'Avg':>8}  {'Grade':<6}  {'Result':<8}\n")
        file.write(f"-"*38)
        for student in students:
            file.write(f"\n{student['name']:<8}  {(student['avg']):>8.2f}  {student['grade']:<6}  {student['result']:<8}")
        
def main():
    students = load_student_data("data\students.csv")

    for student in students:
        student["avg"] = calculate_average(student)


    for student in students:
        student['grade'] = calculate_grade(student['avg'])
        student['result'] = get_result(student['avg'])
    
    name = input("Enter name of student:").lower()
    found = False
    for student in students:
        if student['name'].lower() == name:
            print(f"\nName: {student['name']}")
            print("SCORECARD -->")
            print(f"Math: {student['math']}")
            print(f"Physics: {student['physics']}")
            print(f"Chemistry: {student['chemistry']}")
            print(f"Average: {student['avg']:.2f}")
            print(f"Grade: {student['grade']}")
            print(f"Result: {student['result']}")
            found = True
            break
    if not found:
        print(f"No student found with name: {name}")
        
    subject = input("Enter subject (math/physics/chemistry): ").lower()
    if subject not in ["math", "physics", "chemistry"]:
        print("Invalid subject")
        return
    topper = get_subject_topper(students,subject)
    print(f"Topper of {subject}: {topper['name']} - Marks: {topper[subject]}")

    save_students_report("report.txt",students)

if __name__ == "__main__":
    main()
