#Alex Edmonds

def range(nums):
    """Takes a list of numbers and finds 
    the maximum and minimum values and returns their difference"""

    maximum = max(nums)
    minimum = min(nums)

    difference = maximum - minimum

    return difference

def greater(num1, num2):
    """Takes 2 number and returns the greater value"""
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("Numbers are equal")

#Range function calls
List1 = [5, 7, 99, 1, -9]
print(range(List1))

List2 = [8, 1, 0]
print(range(List2))

List3 = [1, 2, 3, 4, 5, 78, 18]
print(range(List3))

print("\n")

#greater function calls
greater(5, 17)
greater(-12, -9.5)
greater (7, 7)
