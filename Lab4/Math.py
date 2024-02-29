import math

# ex 1

n = int(input("Input degree: "))
rad = n* (math.pi/180)
print("Output radian:" , rad)


# ex 2

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print(((a+b)/2)*h)

# ex 3 

def _area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

n = float(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = int(_area(n, s))
print(f"Expected Output: {area}")

# ex 4 

n = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print("Expected Output:" , n*h)