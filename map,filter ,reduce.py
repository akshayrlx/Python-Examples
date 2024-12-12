#map

def cube(n):
    return n**3
print(list(map(cube,[1,2,3,4])))

def sqare(a):
    return a**2
print(tuple(map(sqare,[4,5,6,7])))

print(list(map(lambda n:n.isupper(),"akshay123")))

print(list(map(lambda n:n**2,[2,4,6,8])))

from math import sqrt
print(list(map(sqrt,[25,9,16,49])))

def cube(n):
    return n.upper()
cube("akshay")

print(list(map(lambda n:n.upper(),"Akshay")))


#filter

print(list(filter(lambda n:n.isalpha(),"akshay123")))

print(list(filter(lambda a:a.isupper(),"akShay133")))

print(list(filter(lambda a:a.isnumeric(),"akShay133")))

print(list(filter(lambda a:a.islower(),"akshay133")))



#reduce
from functools import reduce
def sum(x,y):
    return x+y
print(reduce(sum,[1,2,3]))

print(reduce(lambda x,y:x+y,[1,2,3]))


