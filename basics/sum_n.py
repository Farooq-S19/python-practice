def sumN(n):
    total=sum(int(i) for i in range(1,n+1))
    return total
n=int(input("Enter a number : "))
print(f"The sum of {n} natural numbers is {sumN(n)}:")