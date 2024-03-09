lst=[23,4,65,67,96]
la=list(filter(lambda x: x%2==0,lst))
print(la)

#odd elements
lst=[23,4,65,67,96]
la=list(filter(lambda x: x%2!=0,lst))
print(la)
#reduce function
from functools import reduce
lst=[23,4,65,67,96]
def fun(x,y):
    return x+y
res=reduce(fun,lst)
print(res)

