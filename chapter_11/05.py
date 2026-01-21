class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    # def area(self):
    #      print(f"Area : {self._height*self._width}")
    @property
    def width(self):
        return f"Width : {self._width}"
    @property
    def height(self):
        return f"height : {self._height}"
    @property
    def area(self):
        return f"Area : {self._height*self._width}"

    
obj = Rectangle(8,12)
print(obj._width,obj._height)
print(obj.area)
obj = Rectangle(10,15)
print(obj._width,obj._height)
print(obj.area)
