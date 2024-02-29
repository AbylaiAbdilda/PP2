# ex 1
def gen_numbers(n):
    for i in range(1,n+1):
        yield i*i

n = int(input())
gen = gen_numbers(n)

for x in gen:
    print(x)

# ex 2

def gen_numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i

n = int(input())
gen = gen_numbers(n)

print(*gen , sep=' , ')

# ex 3

def gen_numbers(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
gen = gen_numbers(n)

print(*gen , sep=' , ')

# ex 4 

def squares(a ,b):
    for i in range(a,b+1):
        yield i*i

a = int(input())
b = int(input())
gen = squares(a , b)

for x in gen:
    print(x)

# ex 5

def gen_numbers(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
gen = gen_numbers(n)

print(*gen , sep=' , ')