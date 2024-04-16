#Inputs
num= int(input("Enter a number: "))
print(num)
num += 10
print(num)

try:
    num = int(input("Enter a number: "))
    num += 10
except:
    print("You did not enter a number.")

print("continue\n")

#Accessing and opening files
with open("movies.txt") as file:
    for line in file:
        line = line.strip() #removes the 2nd new line already in the text file
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        print(tokens)

from bank_account import BankAccount

account1 = BankAccount(1234567)
account2 = BankAccount(7654321, 150.00)
account3 = BankAccount(3232323, 584.73)

print(account1)
print(account2)
print(account3)
print()