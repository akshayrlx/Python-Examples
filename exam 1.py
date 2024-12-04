p=int(input("enter number:"))
def prime(a):
    if a>1:
        for i in range (2,a):
            if a%i==0:
                return False
            else:
                return True
prime(p)

10#

letters=['a','k','s','h','a','y']
for i in letters:
    if i not in '':
        print(i,end="")
type(i)

11#
list17=[5,8,45,2,75,11,1]
index=0
for i in list17:
    list17.sort()
print(list17[-2])

12#
list17=[5,8,45,2,75,11,1]
index=0
for i in list17:
    list17.sort()
print(list17[2])

13#
def sub():

    data1=[10,20,50,40,80]
    data2=[10,70,50,40,80,100,20]
    for i in data1:
        if i  in data2:
            return ("yes")
    return ("no")

sub()

14#

list20=[100,200,400,500]
list21=[100,700,400,699]
for i in list20:
    if i in list21:
        print(i)