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
    def __init__(self, data) -> None:
        self.data = data
    def validator(self):
        self.cleaned_data = []
        for newdata in self.data:
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
                self.cleaned_data.append(new_data)
        return self.cleaned_data
file1 = FileHandler('students.csv')
raw_data = file1.load_student_data()
data = DataValidator(raw_data)
cleaned_data = data.validator()
class StudentAnalyzer:
    def __init__(self, data) -> None:
        self.students = data
    is_processed = True
    def process_student(self):
        for student in self.students:
            total , count = 0
            for subject in ['math', 'physics', 'chemistry']:
                total+=self.students[subject]
                count +=1
            avg = total/count
            student['avg'] = avg
        

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
