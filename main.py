
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    grades = []
    m = int(input("Enter number of subjects: "))

    for j in range(m):
        grade = float(input("Enter grade: "))
        grades.append(grade)

    avg = sum(grades) / m
    if avg >= 85:
        status = "Excellent"
    elif avg >= 75:
        status = "Very Good"
    elif avg >= 65:
        status = "Good"
    elif avg >= 50:
        status = "Pass"
    else:
        status = "Fail"
    student = {
        "name": name,
        "grades": grades,
        "average": avg,
        "status": status
    }

    students.append(student)
print("\n=====students results=====")

for student in students:
    print("name:", student["name"])
    print("grades:", student["grades"])
    print("average:", round(student["average"], 2))
    print("status:", student["status"])
    print("----------------------")
best = students[0]
for student in stdents:
    if student["average"] > best["average"]:
        best = student

print("Top Student:", best["name"])
print("Highest Average:", round(best["average"], 2))

total = 0

for student in students:
    total += student["average"]

print("Class Average:", round(total / n, 2))
