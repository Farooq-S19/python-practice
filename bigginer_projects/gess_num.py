import random
ranNum = random.randint(1,100)
attempts = 0
print("Welcome to the game \n guess a number between 1 - 100")
print("OK computer has genrated a number")
while True:
    try:
        n =int(input("Guess the number : "))
    except ValueError:
        print("Please enter a valid input")
        continue
    attempts +=1
    dif = abs(ranNum-n)
    if n == ranNum:
        print("You guess the correct num")
        print(f"And you have completed in {attempts} attempts")
    elif ranNum>n:
        if dif<=5:
            print("You are too close. guess little higher number")
        elif dif<=15:
            print("You are close. guess higher number")
        else:
            print("Guess higher number")
    else:
        if dif<=5:
            print("You are too close. guess little smaller number")
        elif dif<=15:
            print("You are close. guess smaller number")
        else:
            print("Guess smaller number")

            

