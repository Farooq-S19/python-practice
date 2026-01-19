word="twinkle"
with open("poem.txt") as p:
    lines = p.readlines()
    for i in lines:
        if word in i:
            print(i)
        else:
            print("word not found")
p.close()