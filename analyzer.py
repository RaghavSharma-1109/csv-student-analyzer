import csv
from sqlite3.dbapi2 import PARSE_COLNAMES
class DataTypeError(Exception):
    pass
class InvalidEntry(Exception):
    pass
class FileHandler:
    def __init__(self,filepath) -> None:
        if not filepath:
            raise ValueError('Invalid Filepath!')
        self.file_path = filepath
    required_columns = {'Name', 'Math', 'Physics', 'Chemistry'}
    def load_student_data(self):
        self.data = []
        try:
            with open(self.file_path,'r') as file:
                    
                reader = csv.DictReader(file)
                if not self.required_columns.issubset(reader.fieldnames):
                    raise ValueError('CSV missing required columns')
                for row in reader:
                    student = {
                        "name": row["Name"],
                        "math": row["Math"],
                        "physics": row["Physics"],
                        "chemistry":row["Chemistry"]
                    }

                    self.data.append(student)

            return self.data
        except FileNotFoundError:
            raise FileNotFoundError('CSV file not found. Check path.')
class DataValidator:
    def validator(self,data):
        self.data = []

        for newdata in data:
            new_data = {}
            error = False
            name = newdata.get('name')
            if not name:
                continue
            name = name.strip().lower()
            new_data['name'] = name
            subjects = ['math', 'physics', 'chemistry']
            for subject in subjects:
                try:
                    score = int(newdata.get(subject))
                    if score<0 or score>100:
                        error = True
                        break
                    new_data[subject] = score
                except (ValueError, TypeError):
                    error = True
                    break
            if not error:
                self.data.append(new_data)
        return self.data
class StudentAnalyzer:
    def calculate_average(self,student):
        avg = ((student["math"] + student["physics"] + student["chemistry"]) / 3)
        return avg
    def calculate_grade(self,avg):
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
    def get_result(self,avg):
        if avg>=50:
            return 'Passed'
        return 'Failed'
    def get_subject_topper(self,subject):
        return max(self.students,key=lambda x: x[subject])
    def process_students(self):
        for student in self.students:
            avg = self.calculate_average(student)
            student['avg'] = avg
            student['grade'] = self.calculate_grade(avg)
            student['result'] = self.get_result(avg)
    def search_student(self):
        name = input("Enter student name:")
        found = False
        for student in self.students:
            if student['name'].lower() == name.lower():
                print(f"Name: {name}\n")
                print(f"SUBJECTS ->\n")
                for subject in ['math', 'physics', 'chemistry']:
                    print(f"-{subject} = {student[subject]}")
                print(f"Average: {student['avg']}")
                print(f"Grade: {student['grade']}")
                print(f"Result: {student['result']}")
                found = True
        if not found:
            print("Student Not Found!")
    def show_topper(self):
        topper = None
        topper_avg = float('-inf')
        for student in self.students:
            if student['avg']>topper_avg:
                topper = student
                topper_avg = student['avg']
        print(f"Topper: {topper['name']}")
        print(f"Score: {topper_avg}")

    def save_students_report(self,filename):
        with open(filename, "w") as file:
        
            file.write(f"{'Name':<8}  {'Avg':>8}  {'Grade':<6}  {'Result':<8}\n")
            file.write(f"-"*38)
            for student in self.students:
                file.write(f"\n{student['name']:<8}  {(student['avg']):>8.2f}  {student['grade']:<6}  {student['result']:<8}")
            
    def main(self):
        while True:
            print("\n1.Search Student")
            print("2. Show Topper")
            print("3. Generate Report")
            print("4.Exit")

            choice = input("Enter choice:")
            if choice == '1':
                self.search_student()
            elif choice == '2':
                self.show_topper()
            elif choice == '3':
                self.save_students_report("report.txt")
            elif choice == '4':
                break
            else:
                print("Invalid Choice")
    if __name__ == "__main__":
        # analyzer = StudentAnalyzer("data/students.csv")
        # analyzer.load_student_data()
        # analyzer.process_students()
        # analyzer.main()
