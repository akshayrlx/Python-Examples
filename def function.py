def akshay():
    for raw in range(0,5):
        for space in range (raw,5):
            print(" ",end=" ")
        for star in range (0,raw):
            print(" * ",end=" ")
        print(" * ")
akshay()
def akshay(a=5):
    for raw in range(0,a):
        for space in range (raw,a):
            print(" ",end=" ")
        for star in range (0,raw):
            print(" * ",end=" ")
        print(" * ")
akshay(8)

 

def akshay1(d=5):
    
    for row in range(1,d):
        for star in range(1,d):
            if row>star:
               print(row,end="")
            else:
               print(star,end="")
        
        print(" ")
akshay1()


def pattern():
    a=int(input("enter a value and sum"))
    sum=0
    while a<7:
       sum=sum+a
       print(sum)
       a=int(input("enter a value and sum"))
pattern()

def values():
    list1=[]
    x=int(input("enter a value "))
    while x<10:
        list1.append(x)
        print(x)
        x=int(input("enter a value"))
    print(list1)
values()


