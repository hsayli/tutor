import math

class Circle:
    def __init__(self,r):
         self.radius = r
    def area(self):
        return self.radius ** 2 * math.pi
cir = Circle(5)
print(cir.area())
    