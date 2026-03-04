students = {}   

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
dept = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))

students[roll] = {
    "Name": name,
    "Department": dept,
    "CGPA": cgpa
}

update_roll = int(input("\nEnter roll number to update CGPA: "))
if update_roll in students:
    new_cgpa = float(input("Enter new CGPA: "))
    students[update_roll]["CGPA"] = new_cgpa
else:
    print("Student not found!")

search_roll = int(input("\nEnter roll number to search: "))
if search_roll in students:
    print("Student Details:", students[search_roll])
else:
    print("Student not found!")

print("\nAll Student Records")
for roll, details in students.items():
    print("Roll:", roll, "Details:", details)
