import csv
def load_student_data(file_path):
    students = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            student={
                "name": row["Name"],
                "math": int(row["Math"]),
                "physics": int(row["Physics"]),
                "chemistry": int(row["Chemistry"])
            }
            students.append(student)
    return students

data = load_student_data("data/students.csv")
for student in data:
    print(student) 