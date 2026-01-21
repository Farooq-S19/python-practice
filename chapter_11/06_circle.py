class circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7)*(self.radius**2)
    def Parameter(self):
        return (22/7)*2*self.radius
c1=circle(28)
print(c1.Area())
print(c1.Parameter())
