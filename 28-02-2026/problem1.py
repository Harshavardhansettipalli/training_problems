cart = []  

def add_item():
    item = input("Enter item to add: ").strip()
    if item:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item name cannot be empty.")

def remove_item():
    if not cart:
        print("Cart is empty. Nothing to remove.")
        return
    
    item = input("Enter item to remove: ").strip()
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print(f"{item} is not in the cart.")

def display_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item}")

def count_items():
    print(f"Total items in cart: {len(cart)}")

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display cart")
    print("4. Count total items")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        count_items()
    elif choice == "5":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please select 1-5.")