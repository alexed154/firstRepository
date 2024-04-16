from dog import Dog

dogsList = []
with open("dogs.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        dogObject = Dog(tokens[0], tokens[1], tokens[2], tokens[3])
        dogsList.append(dogObject)
        print(dogObject)
print(dogsList)

print(dogsList[0].get_name())
print(dogsList[0].get_breed())
print(dogsList[0].get_trick())
print(dogsList[0].isHungry())

dogsList[0].speak()
dogsList[0].feed()
dogsList[0].change_trick("fetch")

print(dogsList[0].get_name())
print(dogsList[0].get_breed())
print(dogsList[0].get_trick())
print(dogsList[0].isHungry())


