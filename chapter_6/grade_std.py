m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
m4=int(input("Enter marks of subject 4: "))
m5=int(input("Enter marks of subject 5: "))
m6=int(input("Enter marks of subject 6: "))
#caluclate grade
grade = (m1 + m2 + m3 + m4 + m5 + m6) / 6
#if user enters invalid marks
if(m1 < 0 or m2 < 0 or m3 < 0 or m4 < 0 or m5 < 0 or m6 < 0 or m1 > 100 or m2 > 100 or m3 > 100 or m4 > 100 or m5 > 100 or m6 > 100):
    print("Invalid marks entered")
else:
    if grade >= 90:
        print("You got A+ grade")   
    elif grade >= 80:
        print("You got A grade")
    elif grade >= 70:
        print("You got B grade")
    elif grade >= 60:
        print("You got C grade")
    elif grade >= 50:
        print("You got D grade")
    elif grade >= 40:
        print("You got E grade")
    else:
        print("You got F grade, you have failed")
    print("Your grade is: ", grade)