for raw in range(0,5):
    for space in range (raw,5):
        print(" ",end=" ")
    for star in range (0,raw):
        print(" * ",end=" ")
    print(" * ")

for row in range (5,0,-1):
    for five in range (0,row+1):
        print(five,end=" ")
    print(" ")

for row in range (5,0,-1):
    for five in range (0,row):
        print(row,end=" ")
    print(" ")

for row in range (1,5):
    for five in range (0,row):
        print(row,end=" ")
    print(" ")

for row in range (0,5):
    for space in range (row,5):
        print(" ",end=" ")
    for num in range (0,row):
        print("  ",row,end=" ")
    print("")

for row in range (6,0,-1):
    for space in range (row,6):
        print(" ",end=" ")
    for num in range (0,row):
        print("  ",row,end=" ")
    print("")


for row in range (1,5):
    for five in range (row,0,-1):
        print(five,end=" ")
    print(" ")

for row in range (5,-1,-1):
    for five in range (row,0,-1):
        print(five,end=" ")
    print(" ")

for row in range (1,6):
    for space in range( row,5):
        print(" ",end=" ")
    for five in range (1,row+1):
        print(five,end=" ")
    print(" ")

value=1
for row in range (1,5):
    for five in range (1,row+1):
        print(value,end=" ")
        value=value+1
    print(" ")

for row in range (1,6):
    for seven in range(0,row)
    