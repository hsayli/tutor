class Horse:
    def __init__(self,n,rider):
        self.n = n
        self.r = rider

class Rider:
    def __init__(self,n):
        self.n = n

the_rider = Rider("Ronny")
sally = Horse("Sally",the_rider)

print("the name of the horse is {}".format(sally.n))
print("the name of rider is {}".format(the_rider.n))