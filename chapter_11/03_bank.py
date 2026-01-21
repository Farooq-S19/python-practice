class Animals:
    pass
    # def __init__(self, name):
    #     self.name=name
    #     print(f"Animal name is {self.name}")

class pet(Animals):
    pass
    # def __init__(self, name):
    #     super().__init__(name)
    #     print(f"{self.name} is a pet")
class dog(pet):
    @staticmethod
    def bark():
        print("Dog barks")
#i want to use bark method for a1 object tommy
# how can i use like this a1.bark()
#give me solution
d1 = dog()
d1.bark()
