# Day 2 activity

import math 
import time

print("\n============================")
print("\nWelcome to the daily utility app!")
print("\n============================")

while True:
    name = input("Enter your name: ").strip()
    if name.replace(" ", "").isalpha():
        while True:
            age = input("Enter your age: ").strip()
            if age.isdigit():
                age = int(age)
                break
            else:
                print("Please enter a valid age! (number).\n")
                continue
        break
    else:
        print("Please enter a valid name!\n")

print(f"Hello {name.upper()}! You are {age} years old.\n")

if  18 <= age < 65:
    print("You are in the working age group.\n")
elif age < 18:
    print("You are underage.\n")
else:
    print("You are senior citizen.\n")

input("\nPress enter to continue...")

# Temperature Check
while True:
    Temp = input("\nWhat is the Temperature outside (C)?: ").strip()
    if Temp.lstrip('-').replace('.', '', 1).isdigit():
        Message = "The weather is nice, you can go outside!" if 0 <= float(Temp) <= 30 else "Better stay inside, the weather is not ideal.\n" 
        print(Message)
        break
    else:
        print("Enter a valid input! (Number only).")
print("Press Enter to continue...")