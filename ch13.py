class Perimeter:
    def __init__(self,l,w):
        self.len = l
        self.width = w

class Rectangle(Perimeter):
    def perimeter(self):
        return (self.width + self.len) * 2
        
class Square(Perimeter):
    def perimeter(self):
        return (self.len + self.width) * 2
    
p_rect = Rectangle(21,20)
p_sq = Square(2,2)

print(p_rect.perimeter())
print(p_sq.perimeter())