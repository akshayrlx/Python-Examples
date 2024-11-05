for row in range (1,9):
    for space in range(9-row):
        print(' ',end='')
    for star in range(1,row+1):
        print(star,end=' ')
    print("")


list1=[1,2,3,4,5]
for index in range(0,len(list1)):
    print(list1[index])



index=0
while index<7:
    print(index,end="")
    index=index+1
print("")



list1=[1,2,3,4,5]
index=5
while index<3:
    print(list1[index])
    index=index+1

list1=1
while list1<8:
    print(list1)
    list1=list1+1

list1=7
while list1>0:
    print(list1)
    list1=list1-1


list1=1
while list1<8:
    print(list1)
    list1=list1+2
     

list1=7
while list1>0:
    print(list1)
    list1=list1-2

list1=[1,2,3,4,5]
index=4
while index>-1:
    print(list1[index])
    index=index-1

for row in range (1,9):
    for space in range(9-row):
        print(' ',end='')
    for star in range(1,row+1):
        print(star,end=' ')
    print("")

row=1
while row<9:
    space=0
    while space<9-row:
        print(" ",end="")
        space=space+1
    star=1
    while star<row+1:
        print(star,end=" ")
        star=star+1
    print("")
    row=row+1
        
for row in range (6,0,-1):
    for space in range (row,6):
        print(" ",end=" ")
    for num in range (0,row):
        print("  ",row,end=" ")
    print("")

row=6
while row>0:
    space=row
    while space<6:
        print(" ",end=" ")
        space=space+1
    star=0
    while star<row:
        print(' ',row,end=" ")
        star=star+1
    print("")
    row=row-1
    
