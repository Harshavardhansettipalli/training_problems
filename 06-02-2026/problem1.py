# Student Marks Management System

marks = []  # empty list to store marks

# number of students
n = int(input("Enter number of students: "))

# taking marks input
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# adding a new mark
new_mark = int(input("Enter a new mark to add: "))
marks.append(new_mark)

# removing a wrong mark
wrong_mark = int(input("Enter a wrong mark to remove: "))
if wrong_mark in marks:
    marks.remove(wrong_mark)
else:
    print("Mark not found!")

# calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# sorting marks
marks.sort()

# displaying results
print("\nFinal Student Marks Report")
print("Marks List:", marks)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", average)
