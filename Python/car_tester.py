from car import Cars

carsList = []
with open("cars.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        gas = int(tokens[2])
        miles = int(tokens[3])
        carObject = Cars(tokens[0], tokens[1], gas, miles)
        carsList.append(carObject)

print(carsList[0].get_gas_tank())
carsList[0].drive()
print(carsList[0].get_gas_tank())

print(carsList[1].get_gas_tank())
carsList[1].drive()
print(carsList[1].get_gas_tank())

print(carsList[1].get_odometer())

