import csv
SUBJECTS = ['math', 'physics', 'chemistry']
def print_student(student:dict):
    print(f"Name: {student['name']} ")
    print(f"Maths Score: {student['math']} ")
    print(f"Physics Score: {student['physics']} ")
    print(f"Chemistry Score: {student['chemistry']}")
    print(f"Overall Score: {student['avg']} ")
    print(f"Grade: {student['grade']} ")
    print(f"Result: {student['result']} ")
    print('-----------------')
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
            for subject in SUBJECTS:
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
class StudentAnalyzer:
    def __init__(self, data) -> None:
        self.students = data
        self.is_processed = False
    def process_students(self):
        if not self.is_processed:
            for student in self.students:
                total =0
                count = 0
                for subject in SUBJECTS:
                    total+=student[subject]
                    count +=1
                avg = total/count
                student['avg'] = avg
                if avg>=90:
                    student['grade'] = 'A+'
                elif avg>=80:
                    student['grade'] = 'A'
                elif avg>=70:
                    student['grade'] = 'B+'
                elif avg>=60:
                    student['grade'] = 'B'
                elif avg>=50:
                    student['grade'] = 'C'
                else:
                    student['grade'] = 'F'

                if avg>=50:
                    student['result'] = 'Passed'
                else:
                    student['result'] = 'Failed'
            self.is_processed = True
    def get_topper(self):
        if not self.students or not self.is_processed:
            return None
        topper = max(self.students, key=lambda student :student['avg'])
        return topper
    def get_subject_topper(self,subject):
        if not self.students or not self.is_processed:
            return None
        subject = subject.lower()
        if subject not in SUBJECTS:
            return None
        subject_topper = max(self.students, key=lambda student: student[subject])
        return subject_topper
    def search_student(self,name):
        if not isinstance(name,str):
            return None
        name = name.lower().strip()
        if not self.is_processed:
            return None
        found_students = [] 
        for student in self.students:
            if name == student['name']:
                found_students.append(student)
        if not found_students:
            return []
        return found_students
def main(analyzer):
    while(True):
        choice = (input("Select option: \n1. Search Student \n2. Show Topper \n3. Subject Topper \n4. Exit"))
        if choice == '1':
            name = input("Enter Student name")
            result = analyzer.search_student(name)
            if result is None:
                print("Invalid input or data not processed.")
                continue
            for student in result :
                print_student(student)
            continue
        elif choice == '2':
            topper = analyzer.get_topper()
            if topper is None:
                print("No topper available. Ensure data is loaded and processed.")
                continue
            print(f"Topper of This section is ---\n")
            print_student(topper)
            continue
        elif choice =='3':
            subject = input("Enter subject to find topper (Math/Chemistry/physics):")
            topper = analyzer.get_subject_topper(subject)
            if topper is None:
                print("Unable to find subject topper. Check subject or data.")
                continue
            print_student(topper)
            continue
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    file1 = FileHandler('students.csv')
    raw_data = file1.load_student_data()
    data = DataValidator(raw_data)
    cleaned_data = data.validator()
    analyzer = StudentAnalyzer(cleaned_data)
    analyzer.process_students()
    main(analyzer)