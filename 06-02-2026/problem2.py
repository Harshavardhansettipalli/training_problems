# Online Shopping Cart System

cart = []  # list to store product prices

n = int(input("Enter number of products: "))

# adding products
for i in range(n):
    price = float(input(f"Enter price of product {i+1}: ₹"))
    cart.append(price)

# add a new product
new_price = float(input("Enter price of new product to add: ₹"))
cart.append(new_price)

# remove a product
remove_price = float(input("Enter price of product to remove: ₹"))
if remove_price in cart:
    cart.remove(remove_price)
else:
    print("Product not found in cart!")

# total calculation
total = sum(cart)

# discount logic
discount = 0
if total > 5000:
    discount = total * 0.10

final_amount = total - discount

# display bill
print("\nShopping Cart Summary")
print("Cart Items:", cart)
print("Total Amount: ₹", total)
print("Discount: ₹", discount)
print("Final Payable Amount: ₹", final_amount)
