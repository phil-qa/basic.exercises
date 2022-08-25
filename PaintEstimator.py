'''This is a calculator for costing out the painting of rooms
It uses standard values but is written so that customisation is possible'''


def area_of_wall(wall_length, wall_height):
    return wall_length * wall_height


def cans_needed(area, coverage):
    return area/coverage

def cost_of_job(length, height, coverage, cost_per_can):
    total_cans = cans_needed(area_of_wall(length, height),coverage)
    total_cost = total_cans*cost_per_can
    return total_cost

def door_area(width=1.5, height=2):
    return width*height

def job_parameters():
    width = float(input("wall width "))
    height = float(input("wall height "))
    coverage = float(input("How much does one can cover ?"))
    cost = float(input("How much does a can cost"))
    doors = int(input("How many doors"))
    doors_area = 0
    if doors > 0:
        for door in range(doors):
            doors_area += doors_area()
    parameters = {
        "width" : width,
        "height" : height,
        "coverage" : coverage,
        "cost" : cost,
        "door_area" :doors_area
    }
    return parameters

params = job_parameters()
for k in params:
    print(f"{k}, {params[k]}")



