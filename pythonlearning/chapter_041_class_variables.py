from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
print(car_1.wheels)

car_1.wheels = 3
print(car_1.wheels)

print(Car.wheels)

Car.wheels = 2          # changing a class variable will affect all new instances of a class

car_2 = Car("Tesla","Model X",2023,"black")
print(car_2.wheels)