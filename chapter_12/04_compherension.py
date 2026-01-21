num_list = [1,2,3,4,5,6,7,8]
squ_list=[i*i for i in num_list]
print(squ_list)
evenList =[i+1 for i in range (1,10)]
print(evenList)
dictn = {i:i*3 for i in range(1,11)}
print(dictn)
set1 = set(i*4 for i in range(1,11))
print(set1)
print(type(set1))
print(type(squ_list))
print(type(evenList))
print(type(dictn))