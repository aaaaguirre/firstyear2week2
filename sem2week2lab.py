# Question 1

import random

number_list = []  # initialise empty list
randoms = []
LIMIT = 5  # 5 random integers
numbers = []
for number in range(LIMIT):
    randoms = random.randint(1, 100)
    number_list.append(randoms)

print(f'{"Index":10}{"Value":10}')

for index, item in enumerate(number_list):
    print(index, "\t\t", item)

max_value = max(number_list)  # finding the highest number
min_value = min(number_list)  # finding the lowest number
difference = max_value - min_value  # difference from max value and min value

print("Min:", min_value, "Max:", max_value, "Difference:", difference)

# Question 2

print("----------------------------------------")
print("--Welcome to Student Processing System--")
print("----------------------------------------")

student_numbers = []
marks = []
grades = []
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'F': 0}

for _ in range(4):  # 4 for students in a group
    student_number = input("Enter student number: ")
    mark = random.randint(0, 100)
    student_numbers.append(student_number)
    marks.append(mark)

    if mark < 40:
        grade = 'F'
    elif mark < 60:
        grade = 'C'
    elif mark < 80:
        grade = 'B'
    else:
        grade = 'A'

    grades.append(grade)
    grade_counts[grade] += 1
print("----------------------------------------")
print("{:<15} {:<10} {:<5}".format("Student Number", "Mark", "Grade"))
for i in range(4):
    print("{:<15} {:<10} {:<5}".format(student_numbers[i], marks[i], grades[i]))
print("----------------------------------------")
print("----------------------------------------")
print("\nGrade Counts:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count}")
max_mark_index = marks.index(max(marks))
print("----------------------------------------")
print("\nStudent with the highest mark:")
print("{:<15} {:<10} {:<5}".format(student_numbers[max_mark_index], marks[max_mark_index], grades[max_mark_index]))
