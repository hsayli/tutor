class Rectangle():
    def __init__(self,w,l):
        self.width = w 
        self.lenth = l
    def area(self):
        return self.width * self.lenth
    def change_size(self,w,l):
        self.width = w
        self.lenth = l
rect = Rectangle(10,20)
print(rect.area())
rect.change_size(20,40)
print(rect.area()) 