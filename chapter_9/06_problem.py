word=['donkey', 'happy', 'hello','good','bad']
with open("donkey.txt", "r") as f:
    content = f.read()
    f.close()

for i in word:
    content = content.replace(i, "#"*len(i))
with open("donkey.txt", "w") as f:
    f.write(content)