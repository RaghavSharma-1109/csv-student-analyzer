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

filepath = "students.csv"
students = load_student_data(filepath)
for student in students:
        student["avg"] = calculate_average(student)
def get_top_n_students(students,n):
    sorted_students = sorted(students,key=lambda x: x["avg"], reverse=True)
    return sorted_students[:n]
top_students = get_top_n_students(students,3)
