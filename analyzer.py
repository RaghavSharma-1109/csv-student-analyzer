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
        student["avg"] = calculate_average(student)

    rankers_list = sorted(students, key=lambda x: x["avg"], reverse=True)
    print("\nTop 3 students are:")
    for ranker in range(3):
        student =   rankers_list[ranker]
        print(f"{ranker+1}. {student['name']} - {student['avg']:.2f}")


if __name__ == "__main__":
    main()