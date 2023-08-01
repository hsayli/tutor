class Shape:
    def what_am_i(self):
        print("im a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.w = w
        self.l = l
    def per(self):
        return (self.w +self.l) * 2
    
class Square(Shape):
    def __init__(self,s):
        self.s = s
    def per(self):
        return self.s * 4
    
r = Rectangle(4,5)
s = Square(7)

r.what_am_i()
s.what_am_i()
print(r.per())
print(s.per())