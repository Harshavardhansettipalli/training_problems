queue = []

def add_customer(name):
    queue.append(name)
    print("Customer added:", name)

def serve_customer():
    if len(queue) == 0:
        print("No customers in queue.")
    else:
        served = queue.pop(0)
        print("Customer served:", served)

def display_queue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Customers in queue:")
        for customer in queue:
            print(customer)

while True:
    print("\n1.Add Customer")
    print("2.Serve Customer")
    print("3.Display Queue")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        add_customer(name)

    elif choice == 2:
        serve_customer()

    elif choice == 3:
        display_queue()

    elif choice == 4:
        break

    else:
        print("Invalid choice")