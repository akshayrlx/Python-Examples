list1=[10,20,30,40,50,60,70,80]
index=0
while list1[index]!=70:
    print(list1[index])
    index=index+1

list2=[100,200,300,400,500,600,700]
index=0
while list2[index]!=600:
    print(list2[index])
    index=index+1

list2=[100,200,300,400,500,600,700]
index=0
while index<7:
    if list2[index]!=500:
        print(list2[index])
    index=index+1

list2=[100,200,300,400,500,600,700]
index=0
while index<7:
    if list2[index]==500:
        index=index+1
        continue
    print(list2[index])
    index=index+1

index=0
while index<7:
    if list2[index]==500:
        break
    print(list2[index])
    index=index+1
    
list2=[100,200,300,400,500,600,700]
index=0
while index <len(list2):
    if list2[index]!=500 and list2[index]!=600:
        print(list2[index])
    index=index+1

    
list2=[100,200,300,566,700,400,500,600,700]
index=0
while index <len(list2):
    if list2[index]==500 or list2[index]==600:
        index=index+1
        continue
    print(list2[index])
    index=index+1

list3=[100,200,300,400,500,600,700]
def pattern1(list2):
   
    index=0
    while index <len(list2):
        if list2[index]==500 or list2[index]==600:
            index=index+1
            continue
        print(list2[index])
        index=index+1
pattern1(list2)
