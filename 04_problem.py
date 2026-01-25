

list1 = [i for i in range (1, 20)]
def divi(n):
    if n%5==0:
        return True
    else:
        return False
list2 = list(filter(divi,list1))
print(list2)