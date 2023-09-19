def drive(cars_dict, car_model, travel_distance, needed_fuel):
    if cars_dict[car_model][1] < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[car_model][0] += travel_distance
        cars_dict[car_model][1] -= needed_fuel
        if cars_dict[car_model][0] >= 100000:
            del cars_dict[car_model]
            print(f"{car_model} driven for {travel_distance} kilometers. {fuel_needed} liters of fuel consumed.")
            print(f"Time to sell the {car_model}!")
        else:
            print(f"{car_model} driven for {travel_distance} kilometers. {fuel_needed} liters of fuel consumed.")


def refuel(cars_dict, car_model, needed_fuel):
    cars_dict[car_model][1] += needed_fuel
    if cars_dict[car_model][1] > 75:
        added_fuel = needed_fuel - (cars_dict[car_model][1] - 75)
        cars_dict[car_model][1] = 75
        print(f"{car_model} refueled with {added_fuel} liters")
    else:
        print(f"{car_model} refueled with {needed_fuel} liters")


def revert(cars_dict, car_model, kilometers_to_decrease):
    cars_dict[car_model][0] -= kilometers_to_decrease
    if cars_dict[car_model][0] < 10000:
        cars_dict[car_model][0] = 10000
    else:
        print(f"{car_model} mileage decreased by {kilometers_to_decrease} kilometers")


number_of_cars = int(input())
cars_info = {}

for _ in range(number_of_cars):
    car_info = input().split('|')
    car, mileage, fuel = car_info[0], int(car_info[1]), int(car_info[2])

    cars_info[car] = [mileage, fuel]

command = input().split(' : ')

while command[0] != 'Stop':
    if command[0] == 'Drive':
        car, distance, fuel_needed = command[1], int(command[2]), int(command[3])
        result = drive(cars_info, car, distance, fuel_needed)
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        result = refuel(cars_info, car, fuel)
    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        result = revert(cars_info, car, kilometers)

    command = input().split(' : ')

for car, mileage_fuel in cars_info.items():
    print(f"{car} -> Mileage: {mileage_fuel[0]} kms, Fuel in the tank: {mileage_fuel[1]} lt.")
