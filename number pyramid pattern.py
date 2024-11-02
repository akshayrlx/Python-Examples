
for row in range (0,5):
    for five in range (0,row):
        print(row,end=" ")
    print(" ")

for row in range (0,5):
    for space in range (row,5):
        print(" ",end=" ")
    for five in range (0,row):
        print("  ",row,end=" ")
    print("")

for row in range (6,0,-1):
    for space in range (row,6):
        print(" ",end=" ")
    for num in range (0,row):
        print("  ",row,end=" ")
    print("")

for row in range (7,-1,-1):
    for seven in range (1,row+1):
        print(seven,end=" ")
    print("")

for row in range (5,-1,-1):
    for five in range (row,0,-1):
        print(five,end=" ")
    print(" ")

for row in range (1,5):
    for dfg in range (row,5):
        print(dfg,end=" ")
    print(" ")


for row in range (0,5):
    for dfg in range (row,0,-1):
        print(dfg,end=" ")
    print(" ")


for row in range (1,6):
    for space in range( row,5):
        print(" ",end=" ")
    for five in range (1,row+1):
        print(five,end=" ")
    print(" ")

for row in range (6,-1,-1):
    for space in range( row,6):
        print(" ",end=" ")
    for five in range (1,row+1):
        print(five,end=" ")
    print(" ")


for row in range (0,5):
    for space in range (row,5):
        print(" ",end=" ")
    for num in range (1,row+1):
        print(" ",num,end=" ")
    print("")

for row in range (5,-1,-1):
    for space in range (row,5):
        print(" ",end=" ")
    for num in range (1,row+1):
        print(" ",num,end=" ")
    print("")

value=1
for row in range(0,5):
    for space in range (row,5):
        print(" ",end=" ")
    for five in range (0,row):
        print(" ",value,end=" ")
        value=value+1
    print(" ")

value=1
for row in range(4,-1,-1):
    for space in range (row,5):
        print(" ",end=" ")
    for five in range (0,row):
        print(" ",value,end=" ")
        value=value+1
    print(" ")

value=1
for row in range(0,5):
    for space in range (row,5):
        print(" ",end=" ")
    for num in range (0,row):
        print(" ",row,end=" ") 
    print(" ")

value=1

for row in range(7,-1,-1):
    for space in range (row,7):
        print(" ",end="")
    for num in range (1,row+1):
        print(" ",row,end="")
    print(" ")


for raw in range(0,6):
    for col in range (0,1):
        print("5"*raw)

for row in range (5,0,-1):
    for five in range (1,row+1):
        print(five,end=" ")
    print(" ")

for row in range (0,6):
    for five in range (1,row+1):
        print(five,end=" ")
    print(" ")

for row in range (6,0,-1):
    for five in range (0,row):
        print(row,end=" ")
    print("")

for row in range (0,6):
    for five in range (0,row):
        print(row,end=" ")
    print("")

value=1
for row in range (1,5):
    for five in range (1,row+1):
        print(value,end=" ")
        value=value+1
    print(" ")

