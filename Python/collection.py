#List operations
list = [10, 20, 30, 40, 50]
list.append(5)
list.append(6)
list.append(7)
print(list)

list.remove(40) #removes 40
print(list)

list.pop(0) #removes 10
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list[0] = 500
print(list)

list = list[1:]
print(list)

index30 = list.index(30)
print(index30)

list.append(20)
list.append(20)
list.append(20)
print(list)

count20 = list.count(20)
print(count20)

list_copy = list
print(list_copy)
list_copy[1] = 99
print("List copy:", list_copy)
print("Orignal list:", list)
#Editing copy will edit original 

new_copy = list.copy()
print(new_copy)
new_copy[0] = 1000
print("Copy:", new_copy)
print("Original:", list)

new_copy = list[:]

empty_list = []
for i in list:
    empty_list.append(i)
print("Empty:", empty_list)

squares = []
for i in range(1, 10):
    squares.append(pow(i, 2))
print(squares)

print(list)

plus5 = [i + 5  for i in list]
print(plus5)

smallVals = [i for i in list if i < 20]
print(smallVals)

#Dictionaries
favFoods = {"Kathleen": "Pizza", "Alex": "Pancakes", "Timmy":"Bananas", "Tom": "Ice Cream"}
print(favFoods)

AFF = favFoods["Alex"]
print(AFF)

for key in favFoods:
    print(f"{key}'s favorite food is {favFoods[key]}")

for person, food in favFoods.items():
    print(f"{person}'s favorite food is {food}")

if "Bob" in favFoods:
    print(favFoods["Bob"])
else:
    favFoods["Bob"] = "Wings"
print(favFoods)

