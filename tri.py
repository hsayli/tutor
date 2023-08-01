class Triangle:
    def __init__(self,h,w):
        self.height = h
        self.width = w
    def tri_area(self):
        return self.height * self.width / 2
tri = Triangle(5,10)
print(tri.tri_area())