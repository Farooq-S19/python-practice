from random import randint
class ncnc:
    def __init(self, trainNo, ):
        self.trainNo = trainNo
        
    def book(self ,fro, to):
        self.fro = fro
        self.to = to
        print(f"Your ticket is booked in train no : {self.trainNo} from {self.fro} to {self.to}")
    def satuts(self, fro, to):
        self.fro = fro
        self.to = to
        print(f"Your ticked is booked in train no : {self.trainNo} from {self.fro} to {self.to}")
    def fare(self, fro, to):
        self.fro = fro
        self.to = to
        print(f"The tickect cost you {randint(80, 1500)} rupees in train no : {self.trainNo} from {self.fro} to {self.to}")
obj = ncnc()
obj.trainNo = 436262
obj.book("Delhi", "Banglore")
obj.satuts("Delhi", "Banglore")
obj.fare("Delhi", "Banglore")
