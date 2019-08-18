import numpy as np
# Create a dictionary with keys as student names and values as student GPA (float)
students = {'John':7.5, 'Paul':6.5, 'Ringo':8.0, 'George':6.0}

name = input("Enter new student name: ")
gpa = float(input("Enter student GPA: "))

students[name] = gpa

name = input("Enter new student name: ")
gpa = float(input("Enter student GPA: "))

students[name] = gpa

print(students)

print("Student who has max GPA: ", max(students))
print("Student who has min GPA: ", min(students))
print("Mean of GPA: ", np.mean(list(students.values())))

name = input("Enter student name: ")
print("Student GPA = ", students[name])

name = input("Enter student name: ")
gpa = float(input("Enter student new GPA: "))

students[name] = gpa

name = input("Enter student name: ")
students.pop(name)

print(students)
