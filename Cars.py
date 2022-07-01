import pandas as pd


cars = ["Corsa", "Mini", "Tesla"]
makes= ["Vaxhaul", "BMW", "Tesla"]
model=["kmi009", "haeokl", "zippy1"]
max_speed = [90,100,230]
acceleration = [5,10,30]

combined = []

for c, m, mo, sp, ac in zip(cars,makes,model,max_speed, acceleration):
    combined.append(f"{c} ,{m} ,{mo} ,{sp} ,{ac} ")

print(combined)
my_file = open("cars.csv", 'w')
my_file.write("name, make, model, max_speed, acceleration\n")
for car in combined:
    my_file.write(car+'\n')

my_file.close()

