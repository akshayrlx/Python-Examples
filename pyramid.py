list1=[19,29,39,49,59,69]
for number in list1:
    print(number)
for number in range(0,len(list1)):
    print(list1[number])

for raw in range(0,5):
    for col in range (0,5):
        print("*",end="")
    print("")

for raw in range(0,5):
    for col in range (0,raw):
        print("*",end="")
    print("")

for raw in range(7,-1,-1):
    for col in range (0,raw):
        print("*",end="")
    print("")
for raw in range(0,7):
    for col in range (0,raw):
        print("*",end="")
    print("")

for raw in range(0,7):
    for col in range (0,raw):
        print("*",end="")
    print("")
for raw in range(7,-1,-1):
    for col in range (0,raw):
        print(col,end="")
    print("")
for raw in range(7,-1,-1):
    for col in range (0,raw):
        print(raw,end="")
    print("")

for raw in range(0,7):
    for col in range (1,raw):
        print(col,end="")
    print("")

for raw in range(0,6):
    for col in range (0,1):
        print("5"*raw)
    
for raw in range(0,5):
    for space in range (raw,5):
        print(" ",end=" ")
    for star in range (0,raw):
        print(" * ",end=" ")
    print("")

for raw in range(5,-1,-1):
    for space in range (raw,5):
        print(" ",end=" ")
    for star in range (0,raw):
        print(" * ",end=" ")
    print("")

    
