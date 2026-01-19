name=input("Enter your name: ")
if len(name)<10:
    print("Username is valid")
else:
    print("Username is not valid, it should be less than 10 characters")
print("Length of username is: ", len(name))