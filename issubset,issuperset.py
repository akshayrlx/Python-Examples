data=[77,48,48,45.3]
data
data.insert(2,True)
data.append(False)
h=(47,56)
data.extend(h)
data.pop(0)
data.remove(77)
data.sort(reverse=False)
data.clear()
data
data1=data.copy()
data2=data
id(data)
id(data2)

data={10,40,10,70,10,80,70,700,900,3,2,700,1000}
data
type(data)
dir(data)
values={10,20,40,50,500,7,70,90,1000,600,100,3}
values
type(values)
dir(values)
data.union(values)
data.intersection(values)
data.difference(values)
values.difference(data)
data.symmetric_difference(values)

number1={1,2,3,5,4}
number2={1,2,3,4,5,6,7,8}
number1.issubset(number2)
number1.issuperset(number2)
number2.issubset(number1)
number2.issuperset(number1)

set1={5,6,7,8,9,}
set2={10,11,12,13,14,15,16,17}
set1.isdisjoint(set2)
