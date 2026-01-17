a=1
b=3
print(f"befroe a={a}, b={b}")
#swapping two numbers
#using third variable
t=a
a=b
b=t
print(f"after a={a}, b={b}")
#swapping two numbers without using third variable
a = a + b
b = a - b       
a = a - b
print(f"after a={a}, b={b}")
#swapping two numbers using tuple unpacking
a, b = b, a
print(f"after a={a}, b={b}")
