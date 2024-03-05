# ex 1 

from functools import reduce

def myltp(num):
    res = reduce(lambda x, y: x * y, num)
    return res

num_list = [2, 11, 1, 2]
print("My List:", num_list)
print("Result:", myltp(num_list))

# ex 2

def count(my_str):
    upper_count = sum(1 for char in my_str if char.isupper())
    lower_count = sum(1 for char in my_str if char.islower())
    return upper_count, lower_count

inp_str = str(input())
upper, lower = count(inp_str)
print("Count upper case:", upper)
print("Count lower case:", lower)

# ex 3 

def Pol(my_str):
    my_str = my_str.lower()
    my_str = my_str.replace(" ", "")
    return my_str == my_str[::-1]

my_str = str(input())
if Pol(my_str):
    print("This string is polindrom")
else:
    print("This string is not polindrom")

# ex 4

import math
import time

def calc(num, millisec):
    time.sleep(millisec / 1000)
    square = math.sqrt(num)
    print(f"Square root of {num} after {millisec} milliseconds is {square}")

num = int(input())
millisec = int(input())

calc(num, millisec)

# ex 5

def all_true(tup):
    return all(tup)

my_tup = (True, True, True, True)
print("All elements of the my_tup are true:", all_true(my_tup))

my_tup = (True, False)
print("All elements of the my_tup are true:", all_true(my_tup))

my_tup = (False, False, False)
print("All elements of the my_tup are true:", all_true(my_tup))