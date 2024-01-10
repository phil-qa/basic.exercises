'''This is a calculator for costing out the painting of rooms
It uses standard values but is written so that customisation is possible'''
import math


def area_of_surface(length, height):
    return length * height


def cans_needed(area, coverage):
    return math.ceil(area / coverage)


def cost_of_job(args):
    total_cans = cans_needed((area_of_surface(args['width'], args['height'])-args['door_area']), args['coverage'])
    total_cost = total_cans * args['cost']
    return total_cost


def door_area(width=1.5, height=2):
    return area_of_surface(width, height)


def job_parameters():
    width = float(input("wall width "))
    height = float(input("wall height "))
    coverage = float(input("How much does one can cover ?"))
    cost = float(input("How much does a can cost "))
    doors = int(input("How many doors "))
    total_doors_area = 0
    if doors > 0:
        for door in range(int(doors)):
            total_doors_area += door_area()
    parameters = {
        "width": width,
        "height": height,
        "coverage": coverage,
        "cost": cost,
        "door_area": total_doors_area
    }
    return parameters


def cost_job():
    return cost_of_job(job_parameters())
