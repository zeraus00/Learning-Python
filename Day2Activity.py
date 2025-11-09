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

# weight converter

print("\nWeight Converter\n")

while True:
    weight = input("Enter your weight: ").strip()
    if weight.replace('.', '', 1).isdigit():
        weight = float(weight)
        while True:
            unit = input("(L)bs or (K)g?: ").upper().strip()
            if unit.isalpha():
                if unit == "L":
                    converted = weight * 0.45
                    print(f"You are {converted:.2f} kilos.\n")
                    break
                elif unit == "K":
                    converted = weight / 0.45
                    print(f"You are {converted:.2f} pounds.\n")
                    break
                else:
                    print("Invalid unit! Please enter 'L' or 'K' only.\n")
                    continue
            else:
                print("Invalid input! Please enter valid unit(Letters only).\n")
                continue
        break
    else:
        print("Invalid weight! Please enter a number.\n")
        continue
        
print("\nString and name analysis\n")
print(f"\nYour name in reverse: {''.join(reversed(name))}")
print(f"Your name in uppercase: {name.upper()}")

#//////////////////////////
# List Operations and slicing
siblings = ['Nalyn', 'April', 'Faith', 'Carlo']
print(f"\nSiblings' list: {', '.join(siblings)}")
print(f"\nFrom 2nd to last: {', '.join(siblings[2:])}")
print(f"\nMiddle: {', '.join(siblings[1:4])}")
input("\nPress Enter to continue...")

# Rows and columns (Nested Loops)
print("\nPattern Generator\n")
while True:
    try:
        rows = int(input("Enter number of rows: ").strip())
        if rows > 0:
            while True:
                try:
                    cols = int(input("Enter number of columns: ").strip())
                    if cols > 0:
                        symbol = input("Enter a symbol to display: ").strip()
                        for i in range(rows):
                            for j in range(cols):
                                print(symbol, end="")
                            print()
                        break
                    else:
                        print("Enter a number greater than 0 for columns.\n")
                except ValueError:
                    print("Please enter a valid number for column!\n")
            break
        else:
            print("Enter a number greater than 0 for rows.\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Even number counter 
count = 0
while True:
    try:
        even_num = int(input("Enter a number: ").strip())
        if even_num > 0:
            for even in range(1, even_num + 1):
                if even % 2 == 0:
                    print(even, end=" ")
                    count +=1
            print(f"\nTotal even numbers: {count}")
            input("\nPress enter to continue...")
            break    
        else:
            print("Please enter a number greater than 0!\n")
    except ValueError:
        print("Please enter a valid number!\n")