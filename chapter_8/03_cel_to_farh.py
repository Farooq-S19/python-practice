def convert(c):
    f=((9/5)*c)+32
    return f
c= int (input("Enter temperature in Celsius: "))
print(f"{c} degrees celcius in faahrenheit is {round(convert(c),2)} degrees")