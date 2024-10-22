a=["akshay","abhijith","adarsh","amal","akhil"]
a
for name in range (0,len(a)):
    print(a[name])
for name in a:
    print(name[:3])
for name in a:
    print(name[::2])


c="cRisTianO 666,,[]\RonLdo"
c
for name in c:
    print(name[::1])
for value in c:
    if value.isupper():
        print(value)
list1=[]
for value in c:
    if value.islower():
        list1.append(value)
       
list1

list2=[]
for value in c:
    if value.isupper():
        list2.append(value)
list2

list3=[]
list4=[]
others=[]
for value in c:
    if value.isupper():
        list3.append(value)
    elif value.islower():
        list4.append(value)
    else:
        others.append(value)
print(list3)
print(list4)
print(others)
list5=[]
list6=[]
others=[]
for value in c:
    if value.islower():
        list5.append(value)
    elif value.isupper():
        list6.append(value)
    else:
        others.append(value)
print(list5)
print(list6)
print(others)

list4=[24,34,66,100]
list4
sum(list4)
sum1=2
for value in list4:
    sum1=sum1-value
sum1

list5=[1,2,3,4,5,6,7,8]
list5
sum1=0
for value in list5:
    sum1=sum1+value
sum1

b="LIONEL messi"
count=0
for name in b:
    if name.isupper():
        count=count+1
count       
count=0   
for name in b:
    if name.islower():
        count=count+1
count        

u="usainBOLT"
count=0
count1=0
for name in u:
    if name.isupper():
        count=count+1
    else:
        count1=count1+1
count
count1

u="usainBOLT"
list1=[]
list2=[]
count=0
count1=0
for name in u:
    if name.isupper():
        list1.append(name)
        count=count+1
    else:
        list2.append(name)
        count1=count1+1
print(list1)
print(list2)

a='ROBERTlewendowski123'
a
list3=[]
list4=[]
others=[]
count=0
count1=0
count2=0
for name in a:
    if name.islower():
        list3.append(name)
        count=count+1
    elif name.isupper():
        list4.append(name)
        count1=count1+1
    else:
        others.append(name)
        count2=count2+1
print(list3)
print(list4)
print(others)
count
count1
count2
evensum=0
oddsum=0
for value in range (0,51):
    if value%2==0:
        evensum=evensum+value
    else:
        oddsum=oddsum+value
evensum
oddsum
"*"*5
for value in range (0,4):
    print(value*"*")
for value in range (4,0,-1):
    print(value*"*")

for value in range (4,0,-1):
    print(value*"*")
for value in range (0,5):
    print(" "*(4-value),value*" * ")

for value in range (0,10):
    print(" "*(9-value),value*" * ")

