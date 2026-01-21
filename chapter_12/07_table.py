n = int(input("Enter a number : "))
tableList = [n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n} :{tableList} \n")