 # ex 1
def function(a):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input()) 
ounces = function(grams)
print(ounces)

# ex 2
def to_C(F):
    a = (5 / 9) * (F - 32)
    return a
    
F  = int(input())
C = to_C(F)
print(C)

# ex 3

def solve (numheads, numlegs):
    for num_chickens in range(numheads+1):
        num_rabbits = numheads - num_chickens
        if (2*num_chickens)+(4*num_rabbits)==numlegs:
            return num_rabbits , num_chickens
    return 0

numheads = int(input())
numlegs = int(input())
a = solve(numheads,numlegs)
print("rabbits" , a[0])
print( "checkens" , a[1])

# ex 4
def prime(numbers):
    sorted = []
    for x in numbers:
        for i in range(2,x):
            if x%i==0 :
                break
        else :
            sorted.append(x)
    return sorted
              

numbers = list(map(int ,input().split()))
result = prime(numbers)
print(result)

# ex 5
from itertools import permutations

def permutation(a):
    b = permutations(a)
    for x in b :
        print(x)
        
a = input()
permutation(a)

# ex 6
def reverse(user):
    print(*user[::-1])
    
user = list(map(str , input().split()))
result = reverse(user)

# ex 7
def check(a):
    for i in range(len(a)-1):
        if a[i]==a[i+1]==3:
            return True
    else:
        return False

a = list(map(int, input().split()))
result = check(a)
print(result)

# ex 8
def check(a):
    c = 0
    for i in range(len(a)):
        if c == 2:
            if a[i]==7:
                return True       
        if a[i] == 0 and c!=2:
            c += 1          
    else:
        return False

a = list(map(int, input().split())) 
result = check(a)
print(result)

# ex 9 
def g(r):
    a = (4/3)*pow(r,3)*3.14
    return a

r = int(input())
V = g(r)
print(V)

# ex 10
def unique(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b
    

a = list(map(int,input().split()))
result = unique(a)
print(*result)

# ex 11
def check(a):
    b= ''
    b=a[::-1]
    return a == b   

a =str(input())
result = check(a)
if result:
    print("Palindrome")
else:
    print("This is not a palindrome")

# ex 12

def histogram(a):
    for x in a:
        print(x*"*")
        
a = list(map(int,input().split()))
result = histogram(a)

# ex 13
import random

def guess(a):
    random_number = random.randint(1,20)
    c = 1
    while a!=random_number:
        if random_number > a:
            a=int(input("Your guess is too low.\nTake a guess."))
            print()
            c+=1
        else:
            a=int(input("Your guess is too high.\nTake a guess."))
            print()
            c+=1
    else:
        print("Good job," , name + "! You guessed my number in", c , "guesses!")
        

name = str(input("Hello! What is your name? \n"))
print()
print("Well," , name + "! , I am thinking of a number between 1 and 20.\nTake a guess. ", )
take_guess=int(input())
print()
result = guess(take_guess)