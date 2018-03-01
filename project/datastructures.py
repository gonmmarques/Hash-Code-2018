class Ride():
    """docstring for Ride"""

    def __init__(self, a, b, x, y, s, f):
        super(Ride, self).__init__()
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f



class Car():

    def __init__(self, id, xInit, yInit):
        super(Car, self).__init__()
        self.id = id
        self.x = xInit
        self.y = yInit
        self.steps = 0
        self.rideList = []