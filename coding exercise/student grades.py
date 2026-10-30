print("students and grades")
students_marks = {
    "Jenny": 76,
    "Navin": 67,
    "Chandan": 87,
    "Durga": 67,
    "Sagar": 87
}
student_grades = {}
for student, marks in students_marks.items():
    if students_marks[student] >= 75:
        student_grades[student] = "A+"
    elif students_marks[student] >= 50:
        student_grades[student] = "A"
    else:
        student_grades[student] = "B+"
print(f"Student grades: {student_grades}")
