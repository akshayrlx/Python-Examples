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

