a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
#print the quratic equation
print(f"The quradratic equation is : {a}x^2 + {b}x + {c} = 0")
# calculate the discriminant
d= b**2-4*a*c
print(f"The discriminant is : {d}")
# check if the discriminant is negative
if (d>0):
    #d value is positive then there are two distinct real roots
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print(f"the root-1 :{r1}")
    print(f"the root-2 :{r2}")
elif (d==0):
    #d value is zero then there is one real root
    r=(-b)/(2*a)
    print(f"the root :{r}")
else:#the d value is negitve which is unreal , so we will get imaginary roots
    real_part = -b / (2 * a)
    imaginary_part = (abs(d) ** 0.5) / (2 * a)
    #two separate imaginary roots
    print(f"The roots are complex and different.")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
