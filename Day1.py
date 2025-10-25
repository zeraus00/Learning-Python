# Printing Text
print("Hello 'Julius' world")
print('Hello "Julius" world')
print("Hello \"Julius\" world")
print("Hello\nworld") # with break \n to print in the next line
print("Julius", end = " ")# end " " prevent from new line
print("Aboy", end = " ")
print("Trinidad", end = " ")
print() # print only a new line to ensure the cursor moves to the next line

print("helloo")
success = "Sucessfully uploaded.\n"
print(f"Message{success}")

# printsep.py or separate syntax
w, x, y, z = 10, 15, 20, 25
print(f"w, x, y, z = {w}, {x}, {y}, {z}")

#input text
name = input("\nEnter your name: ")
print(f"Hello {name}! have a nice day ahead")
#///////////////////////////////////////////////

# init, float, and double
#int
num1 = 1
print(f"number : 1: {num1}, type: {type(num1)}\n")
#float
num2 = 2.12313
print(f"number 2: {num2:.2f}, type: {type(num2)}\n") # using :.2f to control the decimal point


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
