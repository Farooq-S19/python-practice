num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if(num2==0):
    print("Division by zero is not allowed.")
else:
    div=num1/num2
    print(f"{num1}/{num2} = {div}")