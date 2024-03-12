number_to_extrapolate = int(input("What number to do in the tables"))

for base in range(number_to_extrapolate):
    print(f"{base+1} x {number_to_extrapolate} = {(base+1) * (number_to_extrapolate)}")

