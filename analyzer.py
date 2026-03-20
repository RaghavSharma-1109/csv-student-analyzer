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
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def get_bottom_n_students(students,n):
    return sorted(students, key=lambda x: x["avg"])[:n]
def get_top_n_students(students,n):
    sorted_students = sorted(students,key=lambda x: x["avg"], reverse=True)
def get_subject_topper(students,subject):
    
    return sorted_students[:n]
def main():
    students = load_student_data("students.csv")

    for student in students:
        student["avg"] = calculate_average(student)

    top_students = get_top_n_students(students, 3)

    for i, s in enumerate(top_students, 1):
        print(f"{i}. {s['name']} - {s['avg']:.2f}")
    
    bottom_students = get_bottom_n_students(students,2)
    for i, s in enumerate(bottom_students, 1):
        print(f"Bottom {i}: {s['name']} - {s['avg']:.2f}")

if __name__ == "__main__":
    main()