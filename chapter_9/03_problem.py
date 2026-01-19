import random
print("Welcome to play the game")
a = random.randint(1,100)
def game(a):
    with open("hi-score.txt") as hs:
        hi_score = hs.read()
        if(hi_score!=""):
            b= int(hi_score)
        else:
            b=0
    if a>b:
        print("You have just broken the high score")
        with open("hi-score.txt","w") as hs:
            hs.write(str(a))
    else:
        print(f"Your score is less than high score which is {b}")
    return a
game(a)  