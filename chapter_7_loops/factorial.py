num=int(input("Enter a number: "))
factorial = 1
for i in range(2,num + 1):
    factorial *=i
else:
    print(f"Factorial of {num} is: {factorial}")