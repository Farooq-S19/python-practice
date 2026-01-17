
def armstrong(num:int) ->bool:
    num_str =str(num)
    power =len(num_str)
    total = sum(int(i)**power for i in num_str)
    if num==total:
        return True
    else:
        return False
num=int(input("Enter a number :"))
try:
    if armstrong(num)==True:
        print(f"{num} is a armstrong number")
    else:
        print(f"{num} is not a armstrong number")
except:
    print("Please enter a number")

ran = int(input("Enter range : "))
arm = []
for i in range (0,ran+1):
    val = armstrong(i)
    if val ==True:
        arm.append(i)
print(f"Tne all armstrong numbers from 0 to {ran} are : {arm}")
