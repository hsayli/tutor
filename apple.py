class Apple:
    def __init__(self,w,c,s,):
        self.weight = w
        self.color = c
        self.sort = s
        self.mold = 0
    def rot(self,days,temp):
        self.mold = days * temp 
ap = Apple(150,"green","antonovka")
print(ap.weight)
print(ap.color)
print(ap.sort)
ap.rot(10, 20)
print(ap.mold)