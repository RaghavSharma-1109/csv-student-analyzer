# Student Analyzer CLI Tool

A Python-based command-line application designed to analyze and process student performance data from CSV files in a structured and efficient way.

---

## 🚀 Issue Resolved

Raw CSV data is difficult to interpret and analyze manually.
There is no quick way to:

* identify top performers
* evaluate student performance
* extract meaningful insights

This project solves that by transforming raw student data into structured, actionable information.

---

## ✨ Features

* Load student data from a CSV file
* Validate and clean inconsistent or invalid data
* Calculate:

  * Average score
  * Grade
  * Pass/Fail result
* Identify overall topper
* Identify subject-wise topper
* Search students by name
* Interactive CLI-based user interface

---

## 🛠️ Tech Stack

* Python
* CSV module (built-in)

---

## 📁 Project Structure

```
csv-student-analyzer/
│
├── main.py         # Entry point of the application
├── students.csv    # Sample dataset
└── README.md       # Project documentation
```

---

## ▶️ How to Use

1. Clone the repository:

```
git clone https://github.com/RaghavSharma-1109/csv-student-analyzer.git
```

2. Navigate to the project directory:

```
cd csv-student-analyzer
```

3. Run the application:

```
python main.py
```

---

## 💻 Sample Output

```
Select option:
1. Search Student
2. Show Topper
3. Subject Topper
4. Exit

> 2

Topper of This section is ---
Name: neha
Overall Score: 94.33
```

---

## 📈 Future Improvements

* Add graphical user interface (GUI)
* Support additional subjects dynamically
* Export analysis reports to files
* Add sorting and filtering capabilities

---

## 🧠 What This Project Demonstrates

* Clean code structure and modular design
* Separation of concerns (data handling, validation, analysis, interaction)
* Defensive programming and error handling
* Practical use of Python for real-world data processing

---
## 📸 Sample Output

### 🔍 Search Student
![Search](assets/search.png)

### 🏆 Topper
![Topper](assets/topper.png)

## 📌 Author

Raghav Sharma

---
