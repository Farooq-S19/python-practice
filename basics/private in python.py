class Details:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if type(name) is str:
            self.__name =name
        else:
            print("Invalid input type")
person1 = Details('hello',24)
print(person1.name)
person1.name = 3
print(person1.name)
