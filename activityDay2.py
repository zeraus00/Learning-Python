import math

is_vip = False
admin = "Admin"

print("WELCOME TO THE SYSTEM")

while True:
    customer_name = input("Enter your customer name: ").replace(" ", "").strip()
    if customer_name.isalpha():
        customer_name.capitalize()
        if customer_name.capitalize() == admin:
            is_vip = True
            print(f"WElcome back, {customer_name}! VIP Mode Activated.")
            break
        else:
            print(f"Welcome, {customer_name}!")
            break
    else:
        print("Error: Name must only contain letters. Try again.")
        continue

subtotal = 0.0
item_count = 0

while True:
    print("\nNEW ITEM")

    choice = input("Do you want to add an item? (yes/no): ").lower().strip()
    if choice == "no":
        break
    elif choice == "yes":
        product_name = input("Enter product name: ").strip()
        if product_name.replace(" ", "").isalpha():
            product_name = product_name.replace(" ", "").upper()

            price = float(input("Enter the price: "))
            quantity = int(input("How many product?: "))

            item_cost = price * quantity
            subtotal += item_cost
            item_count += 1

            print(f" Added {quantity} x {product_name} Total: ${item_cost}")
            break
        else:
            print("Please enter a product name (e.g Black Shoes)")
            continue
    else:
        print("Please enter yes or no only.")
        continue

print("\nCALCULATING BILL")

