from Car import *

myCar = Car("Toyota", "Celica", 140, "Zippy", 30, 20)

while not myCar.speed == myCar.max_speed:
    myCar.accelerate()

print(myCar.speed)

while not myCar.speed == 0:
    myCar.brake()

print(myCar.speed)
