num=int(input("Enter a number : "))
if (num ==1):
    print("1 is not a prime number")
else:
    for i in range(2,num):
        if((num % i) == 0):
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
# if the number is big and its a squre of prime number then it will take a lot of time to check
# so we can check only till the square root of the number       
#we also can use the below code to check prime number
import math

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
