import math
class calculator:
    def square(x):
        return pow(x,2)
    def cube(x):
        return x*x*x
    def square_root(x):
        return math.sqrt(x)

num = int(input("Enter a number: "))
print("Square:", calculator.square(num))
print("Cube:", calculator.cube(num))
print("Square Root:", calculator.square_root(num))