print("Add new student")
student_data = [
    {
        "Name": "Ram",
        "roll_no": 10,
        "age": 20,
        "course": "Python"
    },
    {
        "Name": "Mohan",
        "roll_no": 20,
        "age": 22,
        "course": "Java"
    }
]
print(f"Student data: {student_data}")


def new_student(**new_student):
    for key, value in new_student.items():
        new_student[key] = value
    student_data.append(new_student)


new_student(Name="Shyam", roll_no=22, age=18, course="Python")

print(f"after adding new student\nStudent data: {student_data}")
