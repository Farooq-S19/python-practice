a = int(10)
print(type(a))
class floating:
    def __init__(self,value):
        self.value  = value
    def __repr__(self):
     return str(self.value)

b = floating(10.7)
print(type(b))
print(b)
print(id(b))