import random
a=int(input("Enter a number:"))
b=random.randint(1,10)
print(f"a={a}, b ={b}")
def game(a,b):
    if a==b:
        return"tie"
    elif a>b:
        return"you win"
    else:
        return"you lose"
print(game(a,b))
with open("game.txt","w") as g:
    g.write(game(a,b))