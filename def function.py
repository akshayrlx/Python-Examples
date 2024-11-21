def akshay():
    for raw in range(0,5):
        for space in range (raw,5):
            print(" ",end=" ")
        for star in range (0,raw):
            print(" * ",end=" ")
        print(" * ")
akshay()

 

def akshay1(d):
    
    for row in range(1,d):
        for star in range(1,d):
            if row>star:
               print(row,end="")
            else:
               print(star,end="")
        
        print(" ")
akshay1(10)

