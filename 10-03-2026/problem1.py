file_name = "students.txt"

def write_data():
    with open(file_name, "w") as f:
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input("Enter name: ")
            sid = input("Enter ID: ")
            marks = input("Enter marks: ")
            f.write(name + "," + sid + "," + marks + "\n")
    print("Data written to file.")

def read_data():
    try:
        with open(file_name, "r") as f:
            print("\nStudent Records:")
            print(f.read())
    except FileNotFoundError:
        print("File does not exist.")

def append_data():
    with open(file_name, "a") as f:
        name = input("Enter name: ")
        sid = input("Enter ID: ")
        marks = input("Enter marks: ")
        f.write(name + "," + sid + "," + marks + "\n")
    print("Record appended successfully.")

def search_data():
    key = input("Enter student name to search: ")
    found = False
    try:
        with open(file_name, "r") as f:
            for line in f:
                if key.lower() in line.lower():
                    print("Record Found:", line)
                    found = True
        if not found:
            print("Record not found.")
    except FileNotFoundError:
        print("File does not exist.")

while True:
    print("\n1.Write Data")
    print("2.Read Data")
    print("3.Append Data")
    print("4.Search Record")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        write_data()
    elif choice == 2:
        read_data()
    elif choice == 3:
        append_data()
    elif choice == 4:
        search_data()
    elif choice == 5:
        break
    else:
        print("Invalid choice")