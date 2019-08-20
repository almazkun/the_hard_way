cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available today")
print("Which mean", cars_not_driven, "are unavailable")
print("We can transport today", carpool_capacity, "people")
print(passengers, "need to be transported")
print(average_passengers_per_car, "people will be in each")
