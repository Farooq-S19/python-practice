class op:
    def __init__(self):
        self.a = "hello"
        print(self.a)
        #why self key word is used
        #it is used to access the instance variable and methods inside the class
    @staticmethod #why use static method
    #it is used when we dont want to use self key word
    def greet():
        print("Good Morning, Sir")
    def ok(self,name):
        self.name = name
        print(f"Welcome {self.name}")
obj = op()
n = input("Enter your name: ")
obj.greet()
obj.ok(n)
