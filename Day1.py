# Printing Text
print("Hello 'Julius' world")
print('Hello "Julius" world')
print("Hello \"Julius\" world")
print("Hello\nworld") # with break \n to print in the next line
print("Julius", end = " ")# end " " prevent from new line
print("Aboy", end = " ")
print("Trinidad", end = " ")
print() # print only a new line to ensure the cursor moves to the next line

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

num1, num2 = 0, 0
result = num1
print()