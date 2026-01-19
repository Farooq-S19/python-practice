def star(n):
    if(n==1):
        return "*"
    print("*"*n)
    return star(n-1)    
n = int(input("Enter the number of stars: "))
print(star(n))