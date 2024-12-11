summ=lambda a: a+1
print(summ(10))

values=lambda b,c:b+c
print(values(4,5))

values=lambda b,c:b*c
print(values(4,5))

index=lambda e,f,g:e-f+g
print(index(100,50,100))

index=lambda e,f,g:e*f+g
print(index(100,50,100))

index=lambda e,f,g:e*f/g
print(index(100,50,100)) 


"even" if 4%2==0 else "odd"

ef=lambda a:" even " if a%2==0 else "odd"
print(ef(11))

[i**2 for i in range (7)]

ab=lambda c: [i**2 for i in range (c)]
print(ab(7))

for raw in range(0,5):
    for col in range (0,5):
        print("*",end="")
    print("")

#content
['*'*i for i in range(5)]

#
value=lambda i :['*'*5 for i in range(i)]
print(value(5))
print("") 

y=lambda z:z.upper()
print(y("aroma"))

z=lambda a:sorted(a)
print(z([1,5,3,8,6]))

x=[(1,3,5,4),(7,5,4,1),(3,5,1)]
x.sort(key=lambda x:x[2])
print(x)


