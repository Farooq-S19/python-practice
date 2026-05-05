def sum_nums(*nums):
    sum_num=0
    for num in nums:
        sum_num+=num
    return sum_num
print(sum_nums(1,2,3,4,5,6,7,8,9))