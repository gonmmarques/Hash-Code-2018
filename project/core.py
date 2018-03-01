# R – number of rows of the grid (1 ≤ R ≤ 10000)
# C – number of columns of the grid (1 ≤ C ≤ 10000)
# F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
# N – number of rides (1 ≤ N ≤ 10000)
# B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
# T – number of steps in the simulation (1 ≤ T ≤ 10 )

# next N lines

# a – the row of the start intersection (0 ≤ a < R)
# b – the column of the start intersection (0 ≤ b < C)
# x – the row of the finish intersection (0 ≤ x < R)
# y – the column of the finish intersection (0 ≤ y < C)
# s – the earliest start(0 ≤ s < T)
# f – the latest finish (0 ≤ f ≤ T) , (f ≥ s + |x − a| + |y − b|)

# note that f can be equal to T – this makes the latest finish equal to the end of the simulation

from .datastructures import Car, Ride


def parser():
    """ void -> tuple( list(Cars), list(Rides)) """

    R, C, F, N, B, T = [int(i) for i in input().split()]

    #print('R =', R, 'C =', C, 'F =', F, 'N =', N, 'B =', B, 'T =', T)

    cars = [Car(0, 0) for _ in range(F)]
    rides = []

    for i in range(N):
        a, b, x, y, s, f = [int(n) for n in input().split()]
        rides += [Ride(i, a, b, x, y, s, f)]

    return (rides, cars)


def cost(ride, car):

    print("Cost with ride", str(ride.ride_id))

    cost = 0

    # distance
    predistance = car.calculatePreDistance(ride)
    waitingTime = ride.calculateWaitingTime(predistance)
    preTime = predistance + waitingTime
    cost += preTime

    print("preTime", str(preTime))

    # proximity to arrival time
    cost += car.isAvailableStart(ride)

    print("isavailablestart", str(car.isAvailableStart(ride)))

    # proximity to finish time
    cost += car.arrivesBeforeFinish(ride)
    print("arrivesbeforefinish", str(car.arrivesBeforeFinish(ride)))

    print("total", str(cost))

    return cost


def main():

    rides, cars = parser()

    rides = sorted(rides)

    for ride in rides:

        max_car = (None, 9999999)

        for i, car in enumerate(cars):

            print("Costs with car", i, "; ridelist: ", [str(ride.ride_id) for ride in car.rideList])

            car_cost = cost(ride, car)
            if car_cost < max_car[1]:
                max_car = (car, car_cost)

        # assign ride to car
        max_car[0].addRide(ride)

    # print out result
    result = ""
    for car in cars:
        result += str(len(car.rideList)) + " " + " ".join([str(ride.ride_id) for ride in car.rideList]) + "\n"
    print(result[:-1])
