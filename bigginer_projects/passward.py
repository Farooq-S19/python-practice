#lets create a program to generate passward of desried length
import random
import string
n=0
def pass_gen(n:int) ->str:
    allStr = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.punctuation
    passward = ""
    passward = "".join([random.choice(allStr) for i in range(n)])
    return passward

def main():
    try:
        n = int(input("Passward length needed : "))
    except ValueError:
        print("Please enter a number.")
        return
        
    if n>=0 and n<12:
        print(f"Your {n} length passward is : {pass_gen(n)}")
    else:
        print("Pleae select the lengt between 1 - 12.")

if __name__ == "__main__":
    main()