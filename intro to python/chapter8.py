cars = ["audi", "ferrari", "ford focus", "toyota sienna hybrid"]

def car_adder(car_to_add):
    cars.append(car_to_add)

cartoadd = input("please add a car\n")

if cartoadd:
    car_adder(cartoadd)

# car_adder("BMW")
# car_adder("Honda")
# car_adder("Chrystler")

print(cars)

#####################################################



