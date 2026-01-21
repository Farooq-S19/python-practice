class bank:
    user_name="admin"
    __password="admin123"
    def __init__(self, acc_no):
        self.acc_no=acc_no
        self.balance=0
        print(f"Account number {self.acc_no} created successfully")
    def details(self):
        print(f"Account number: {self.acc_no}")
        print(f"Account holder name: {self.user_name}")
        print(f"Password: {self.__password}")
    def __good_morning(self):
        print("Good morning, sir")
    def welcome(self):
        print("Welcome to the bank")
        self.__good_morning()

a=bank(1234567890)
a.details()
a.welcome()
