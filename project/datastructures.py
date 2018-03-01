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


    def calculateDistance(self):
        return calculateGenericDistance(self.a,self.b,self.x,self.y)

    def calculateTime(self, car):
        return car.



class Car():

    def __init__(self, id, xInit, yInit):
        super(Car, self).__init__()
        # self.id = id
        self.x = xInit
        self.y = yInit
        self.steps = 0
        self.rideList = []

    def addRide(self, ride):
        self.steps += ride.s
        self.rideList.append(ride)

    def calculatePreDistance(self, ride):
        return calculateGenericDistance(self.x, self.y, ride.a, ride.b)


def calculateGenericDistance(xi, yi, xf, yf):
    return abs(xf - xi) + abs(yf - yi)