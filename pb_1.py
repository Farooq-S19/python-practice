def prime(n):
    if (n&1)==0:
        return True
    else:
        return False
if __name__=="__main__":
    print(prime(int(input("Enter a number"))))