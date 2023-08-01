class Hexagon:
    def __init__(self,l,l1,l2,l3,l4,l5):
        self.l = l
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
    def hex_perimeter(self):
        return self.l + self.l1 + self.l2 + self.l3 + self.l4 + self.l5
hex = Hexagon(7,4,5,7,2,56)
print(hex.hex_perimeter())