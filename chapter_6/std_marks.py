m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
total_percentage = (m1 + m2 + m3) / 3
print("Total percentage is: ", total_percentage)
if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("You have passed ")
else:
    print("You have failed ")