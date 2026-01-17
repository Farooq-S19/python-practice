import random
your_option=int(input("Enter your option : "))
if your_option>3 or your_option<1:
    print("Invalid option")
    exit()
dict={1:"rock",2:"paper",3:"scissor"}
your_dict=dict[your_option]
computer_option = random.randint(1,3)
comp_dict=dict[computer_option]
print(f"Your option is {your_dict}")
print(f"Computer option is {comp_dict}")
if your_option==computer_option:
    print("Match is draw")
else:
    if (your_option==1 and computer_option==3) or (your_option==2 and computer_option==1) or (your_option==3 and computer_option==2):
        print("You win")
    else:
        print("You lose")
