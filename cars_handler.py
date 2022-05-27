# "name, make, model, max_speed, acceleration
class Car:
    def __init__(self, line):
        self.name = line[0]
        self.make = line[1]
        self.model = line[2]
        self.max_speed = line[3]
        self.acceleration = int(line[4])
        self.speed = 0

    def accelerate(self):
        self.speed += self.acceleration




# open a csv
import csv

cars = []

# read a csv
with open("cars.csv",newline='') as csvfile:
    read_data = csv.reader(csvfile, delimiter = ',')
    next(read_data)
    for row in read_data:
        cars.append(Car(row))


active_car = cars[1]
print(active_car.name)
print(active_car.speed)
active_car.accelerate()
print(active_car.speed)
active_car.accelerate()
print(active_car.speed)

