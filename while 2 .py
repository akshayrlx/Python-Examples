for row in range(1,5):
    for star in range(1,5):
        if row>star:
            print(row,end="")
        else:
           print(star,end="")
    print(" ")



row=1
while row<5:
    star=0
    while star<4:
        star=star+1
        if row>star:
            print(row,end="")
        else:
            print(star,end="")
    print("")
    row=row+1    



for row in range(1,5):
    for col in range(1,5):
        if col<=row:
            print(row, end=" ")
        else:
            print(star, end=" ")
    print(" ")

row=1
while row<5:
    col=0
    while col<4:
        col=col+1
        if col<=row:
            print(row, end=" ")
        else:
            print(star, end=" ")
    print(" ")
    row=row+1
        

for row in range (1,5):
    for number in range (0,row):
        print(row*2,end=" ")
    print(" ")

row=1
while row<5:
    number=0
    while number<row:
        print(row*2,end=" ")
        number=number+1
    print(" ")
    row=row+1

a=input("enter a value and 0 for quit")
while a!='0':
    print(a)
    a=input("enter a value and 0 for quit ")
    
b=input("enter a value and 4 for quit")
while b!='4':
    print(b)
    b=input("enter a value and 4 for quit")

list1=[]
c=input(" enter a value and 0 for quit ")
while c!='0':
    list1.append(c)
    c=input(" enter a value and 0 for quit ")
list1

list2=[45,45,45,67]
d=input("enter a value and >100 for quit")
while d!=">100":
    print(d)
    d=input("enter a value and >100 for quit ")

sum(list2)



    