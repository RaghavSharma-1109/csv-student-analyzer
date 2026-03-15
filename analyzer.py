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


def main():
    students = load_student_data("data/students.csv")

    for student in students:
        avg = calculate_average(student)
        print(f"{student['name']} average: {avg:.2f}")


main()