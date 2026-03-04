library = []

def add_book():
    title = input("Enter book title to add: ").strip()

    if not title:
        print("Book title cannot be empty.")
        return

    if title in library:
        print("This book already exists in the library.")
    else:
        library.append(title)
        print(f'"{title}" has been added successfully.')

def remove_book():
    if not library:
        print("Library is empty. No books to remove.")
        return

    title = input("Enter book title to remove: ").strip()

    if title in library:
        library.remove(title)
        print(f'"{title}" has been removed successfully.')
    else:
        print("Book not found. Cannot remove non-existing book.")


def search_book():
    if not library:
        print("Library is empty.")
        return

    title = input("Enter book title to search: ").strip()

    if title in library:
        print(f'"{title}" is available in the library.')
    else:
        print("Book not found.")


def display_books():
    if not library:
        print("Library is empty.")
    else:
        print("\nBooks in Library:")
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book}")


while True:
    print("\n--- Library Management Menu ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select between 1-5.")