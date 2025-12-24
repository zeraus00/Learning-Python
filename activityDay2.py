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

tax = math.ceil(subtotal * 0.12)
discount_rate = 0.0

if is_vip:
    print("VIP Discount applied: 15% off!")
    discount_rate = 0.15
elif 100 < subtotal <= 500:
    print("Standard Discount applied: 5% off!")
    discount_rate = 0.05
elif subtotal > 500:
    print("Big Spender Discount applied: 10% off!")
    discount_rate = 0.10
else:
    print("No discount available for this amount.")

discount_amount = subtotal * discount_rate
final_total = subtotal + tax - discount_amount

print("FEEDBACK")
feedback = input("Please leave a comment about your experience: ")

# you can use this to find the word if present
# if feedback.lower().find("bad") != -1:
#     print("we are sorry to hear that.")
# elif feedback.lower().find("slow") != -1:
#     print("Sorry, We will try to speed up next time!")
# or you can use this for basic

if "bad" in feedback.lower():
    print("we are sorry to hear that.")
elif "slow" in feedback.lower():
    print("Sorry, We will try to speed up next time.")
else:
    print("Thank you for purchasing our product!")

print(F"\nOFFICIAL RECEIPT FOR: {customer_name}")
print(f"\nTotal Items: {quantity}")
print(f"\nSubtotal: ${subtotal}")
print(f"\nTax (12%): +${tax}")
print(f"\nDiscount: -${discount_amount}")
print(f"\nFINAL TOTAL: ${final_total}")