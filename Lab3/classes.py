# ex 1 

class String:
    def inp(self):
        self.input_str = ""
    
    def getStr(self):
        self.input_str = input()

    def printStr(self):
        print(self.input_str.upper())

word = String()
word.getStr()
word.printStr()

# ex 2 

class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of the figure: 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area_value = self.length ** 2
        print(f"Area of the figure: {area_value}")

shape = Shape()
shape.area()

square = Square(5)
square.area()

# ex 3

class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(length = 5, width = 10)
area = rectangle.calculate_area()
print(f"Area of rectangle: {area}")

# ex 4 

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y - new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between points: {distance}")

point1.move(3, 5)
point1.show()

# ex 5

class BankAccount:
    def __init__(self, owner, initial_balance = 0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The {amount} deposit has been successfully completed. New balance: {self.balance}")
        else:
            print("The deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawal completed successfully. New balance: {self.balance}")
        else:
            print("Error: Insufficient funds or incorrect withdrawal amount.")

account = BankAccount(owner = "Azim", initial_balance = 1000)

account.deposit(555)
account.withdraw(187)
account.deposit(444)
account.withdraw(500)

# ex 6 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 15, 17, 83, 19, 11]
prime_nums = list(filter(lambda x: is_prime(x), nums))
print(nums)
print(prime_nums)