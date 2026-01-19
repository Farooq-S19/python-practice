with open ("lo.txt", "r") as f:
    lines=f.readlines()
word ="python"
a=1
for i in lines:
    if word in i:
        print(f"{word} is present in the line {a}")
        
    a+=1