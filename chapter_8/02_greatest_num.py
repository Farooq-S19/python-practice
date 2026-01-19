def great(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
print("The gratest number is :", great(10,20,30))