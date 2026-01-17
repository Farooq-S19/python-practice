def find_miss(num):
    n=len(num)+1
    exp_sum=n*((n+1)/2)
    act_sum=sum(num)
    return exp_sum-act_sum
num=(1,2,4,5,6,7,8,9)
print(find_miss(num))