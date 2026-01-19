with open("donkey.txt", "r") as f:
    content = f.read()
    f.close()
with open("donkey.txt", "w") as f:
    contentnew = content.replace("donkey", "######")
    f.write(contentnew)