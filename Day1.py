# Printing Text
print("Hello 'name' world")
print('Hello "name" world')
print("Hello \"name\" world")
print("Hello\nworld") # with break \n to print in the next line
print("name", end = " ")# end " " prevent from new line
print("middlename", end = " ")
print("lastname", end = " ")
print() # print only a new line to ensure the cursor moves to the next line

#Strings
first_name = "FakeName"
food = "pizza"
email = "Name123@fake.com"

# Integers
age = 25
quantity = 3

print(f"Hello {first_name}")
print(f"your favorite food is {food}")
print(f"your email is {email}")
print(f"You are buying {quantity} of {food}")
#string manipulation
name = "Julius"
print(f"length of name: {len(name)}\n")
print(f"finding \"i\" in the name: {name.find("i")}\n")
print(f"capitalize the name: {name.capitalize()}\n")
print(f"convert into upper case: {name.upper()}\n")
print(f"convert into lower case: {name.lower()}\n")
print(f"check if name is digit: {name.isdigit()}\n")
print(f"check if name is letters: {name.isalpha()}\n")
print(f"count the \"u\" in the name: {name.count("u")} \n")
print(f"replace the \"s\" to e: {name.replace("s", "e")} \n")

print("helloo")
success = "Sucessfully uploaded.\n"
print(f"Message{success}")

# printsep.py or separate syntax
w, x, y, z = 10, 15, 20, 25
print(f"w, x, y, z = {w}, {x}, {y}, {z}")

#input text
name = input("\nEnter your name: ")
print(f"Hello {name}! have a nice day ahead\n")
#///////////////////////////////////////////////

#boolean
human = False
Legal_Age = True
print(human)
print(Legal_Age)
age = 20;
if age >= 18:
    print(f"\nYou are {age} years old, you are legal age.\n")
else:
    print(f"\nYou are {age} years old, you are underage.\n")

print(f"Are you a human: {str(human)}\nAre you a legal age: {str(Legal_Age)}\n")
# init, float, and double
#int
num1 = 1
print(f"number : 1: {num1}, type: {type(num1)}\n")
#float
num2 = 2.12313
print(f"number 2: {num2:.2f}, type: {type(num2)}\n") # using :.2f to control the decimal point
num1 += 1
print(num1)

#casting and operators
str_num = str(num1) + str(num2)
print(f"string number: {str_num}\n")
month = 'november'
day, year = 25, 2025
print(f"{month} {day}, {year}")

# addition
sum_num = num1 + num2
print(f"num1 + num2 = {sum_num}")

#subtraction
diff = num2 - num1
print(f"num1 - num2 = {diff}")

multiplication = num1 * num2
print(f"num1 x num2 = {multiplication}")

#exponential
exp = num2 ** num1
print(f"num3 ** num1 = {exp}")

# division
div = num2 / num1
print(f"num2 / num1 = {div:.2f}")

#floor division (to get the whole number only)
fl_dv = num2 // num1
print(f"num2 // num 1 = {fl_dv}")

# modulo or % to get the decimal point or remainder only
modulo = num2 % num1
print(f"num2 % num1 = {modulo:.2f}")


# controling the decimal point and also round function

num_round = 28.7176

print(round(num_round))
print(round(num_round, 2)) # 2 decimal
print(round(num_round, 3)) # 3 decimal
print("\n")

# ask the user for temperature to convert and read the supplied value
degreeF = float(input("Enter the temperature in degrees F: "))
# Perform the conversion
degreesC = 5/9*(degreeF - 32)
# report the result
print(f"{degreeF} = degrees F = {degreesC} degrees C")





# Activity for operations and strings
# simple calculator + converter + age calculator

Name = input("Enter your name: ")
print(f"\n Hello {Name}! welcome to your simple activity program.\n")
print("Press enter to continue...")

print("\nBasic Calculator\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("\nEnter the second number: "))

print("\n1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
operator = int(input("Pick operator: "))
if operator == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}\n")
elif operator == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}\n")
elif operator == 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}\n")
else:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}\n")

print(input("\nPress Enter to continue..."))

print("\ntemperature converter\n")
degreeF = float(input("Enter temperature in F: "))
degreeC = 5/9 * (degreeF - 32)
print(f"{degreeF} F = {degreeC} C,\n")

if degreeC > 30:
    print("It's a hot day!\n")
elif degreeC >=20:
    print("The weather is nice and warm.\n")
else:
    print("It's cold outside!\n")

print(input("Press Enter to continue..."))

print("\nAge Calculator\n")
birth_year = int(input("Enter your birth year: "))
current_year = int(input("\nEnter the current year: "))
age = current_year - birth_year

if age >= 18:
    print(f"\nHi {name}! You are {age} years old, you are of legal age.\n")
else:
    print(f"Hi {name}! You are {age} years old, you are underage.\n")

print(input("Press enter to finish..."))