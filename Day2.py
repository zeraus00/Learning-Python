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