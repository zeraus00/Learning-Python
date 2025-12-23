# day 2 of learning python

# math library function

import math

pi = 3.14
negative_pi = -3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(negative_pi))
print(pow(pi, 2))
print(math.sqrt(420))
x, y, z = 1, 2, 3
print(max(x, y, z))
print(min(x, y, z))

# slicing and indexing

name = "yus pogi"
print(name, end="\n")
first_name = name[:3]
print(f"output of [:3] is: {first_name}\n")
second_name = name[4:]
print(f"output of [4:] is: {second_name}\n")
third_name = name[0:8:2]
print(f"output of [0:8:2] is: {third_name}\n")
reversed_name = name[::-1]
print(f"reverse name using [::-1], the output is: {reversed_name}\n")
alt_reverse_name = ''.join(reversed(name))
print(f"alternative reversed using ''.join(reversed(name)): {alt_reverse_name}\n")

print("string list\n")
names = ["julius", "April", "Nalyn", "Faith", "Carlo"]
print(names[0])
print(names[-2]) #negative index -3, -2, 1, start from the end element in the list

# specifying index
# note that end index is excluded
names = ["julius", "April", "Nalyn", "Faith", "Carlo"]
print(names)
print(f"From 3 index to the last index: {names[3:]}\n")
print(f"From the start to 2 index: {names[:3]}\n")
print(f"From 1 index to 3: {names[1:4]}\n")
print(f"From 1 index to 4 index: {names[:5]}")

# use ', 'join(names[index]) to remove the [''] in output
# sample
print(f"Using ', '.join(names[index]) to remove the [''] in the output: {', '.join(names[1:3])}")

# using slice function

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])

# logical operators (and, or, not)
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

# using chaining 
if 18 <= age < 65: # check if age is greater than or equal to 18 and if age is less than 65
    print("Eligible") 
# or
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("\nthe temperature is good, go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today! stay inside!")

# weight converter
weight = int(input('Weight: '))
unit = input(" (L)bs or (k)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

# using loop in python
days = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']

for d in days:
    if (d == "thurs"):
        continue
    print(d)

name = ''
while len(name) == 0:
    name = input("Enter your name: ")

print(f"Hello {name}\n")

i = 1
while i <= 5:
    print(f"{'*' * i}")
    i += 1
print("Done\n")

successful = False
for number in range(1, 5):
    print(f"Attempt: {number}")
    if number == 3:
        successful = True

    if successful:    
        print("Successful\n")
        break

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# rows and column generator
rows = int(input("How many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

print("while loop")
numbers = 100
while numbers > 0:
    print(numbers)
    numbers //= 2

print("for loop")
count = 0
for even_num in range(1, 10):
    if even_num % 2 == 0:
        count += 1
        print(even_num)
print(f"We have {count} even numbers.\n")


# count down
import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Merry Christmas\n")