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

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("\nthe temperature is good, go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today! stay inside!")