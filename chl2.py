class Square:
    def __init__(self,s):
        self.side = s
    
    def per (self):
        return self.side * 4
    
    def change_side(self,s1):
         self.side += s1

squ = Square(4)
print(squ.side)
print(squ.per())

squ.change_side(-1)
print(squ.side)
print(squ.per())