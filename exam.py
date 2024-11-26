1# 
list1=[10,20,30,40,50,60,70,80,90]
square=1
for i in list1:
    square=square*i
    print(square) 

2#
list2=[10,20,30,40,50,60,70,80,90]
index=list2[0]
for i in list2:
    if i>index:
        index=i
print(index)  

3#
index=list2[0]
for i in list2:
    if i<index:
        index=i
print(index)   
   
4#

list3=["abba","accc","daa","OCCCO","AAA","aa"]
count=0
for i in list3:
    if len(i)>=2:
        if i[0]==i[-1]:
            count=count+1
print(count)

5#

list4=[100,200,300,400,100,200,700,100]
list5=[]
for i in list4:
    if i not in list5:
        list5.append(i)
print(list5)

6#
