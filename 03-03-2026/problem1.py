def main():
    visitors = set()

    while True:
        print("\n--- Website Visitor Tracker ---")
        print("1. Add Visitor")
        print("2. Check Visitor Exists")
        print("3. Display All Visitors")
        print("4. Count Total Unique Visitors")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            visitor_id = input("Enter Visitor ID: ")
            
            if visitor_id in visitors:
                print("Duplicate! Visitor already exists.")
            else:
                visitors.add(visitor_id)
                print("Visitor added successfully.")

        elif choice == "2":
            visitor_id = input("Enter Visitor ID to check: ")
            
            if visitor_id in visitors:
                print("Visitor exists.")
            else:
                print("Visitor not found.")

        elif choice == "3":
            if not visitors:
                print("No visitors recorded yet.")
            else:
                print("Unique Visitors:")
                for visitor in visitors:
                    print(visitor)

        elif choice == "4":
            print("Total Unique Visitors:", len(visitors))

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()