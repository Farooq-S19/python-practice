import random
from functools import reduce
list1 = [random.randint(1,1000) for i in range(1,21)]
print(list1)
def great(a,b):
    if a>b:
        return a
    return b
num = reduce(great,list1)
print(num)