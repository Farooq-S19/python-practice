class User:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def login(self):
        print("Login successful")
    def register(self):
        print("Registration successful")

class student(User):
    pass
    

user1 = student("ravi Chandra",67)
# user1.login()