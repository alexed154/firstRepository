#For loops
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)): #Standard
    print(nums[i])

print("\n")

for i in range(2, len(nums)): #Change the start or stop index
    print(nums[i])

print("\n")

for num in nums: #Allows you to access each element within the loop, but cant change actual values in this kind of loop
    num += 7
    print(num)
print(nums)

print("\n")

for i, v in enumerate(nums): #
    print("Index", i, "is", v)



dogs = ("boomer", "rocky", "jack", "jax")
# 1.) Use the 3 kinds of loops to iterate through the list of strings.
for s in range(len(dogs)):
    print(dogs[s])

print("\n")

for s in dogs:
    print(s)

print("\n")

for index, name in enumerate(dogs):
    print("Index", index, "is the name", name)

print("\n")

# 2.) Create a list of numbers.  Use any loops to sum the values in the list.
nums2 = [3, 45, 10, -7]
sum = 0
for el in nums2:
    sum += el
#2 ways to print it
print("The sum is", sum)
print(f"The sum is {sum}")

print("\n")


#Functions
def hello(name = "friend"):
    print(f"Hello {name}!")
hello()
hello("Alex")

print("\n")


#Strings
first = 'Alex'
last = "Edmonds"
print("She's a great dancer.")
print('He said "Hello!"')
print("\n")

full_name = first + " " + last
print(full_name)
first_initial = first[0]
last_letter_first_name = first[-1]
print(last_letter_first_name * 4)
if first_initial == "A":
    print(first_initial * 6)

course = "Platform Computing"
platform = course[0:8]
print(platform)
computing = course[9:]
print(computing)
course_copy = course[:]
print(course_copy)

print("\n")

#Example (swap 4 and 8 to make the list in order)
swap = [0, 3, 8, 5, 4]
temp = swap[4]
swap[4] = swap[2]
swap[2] = temp
print(swap)

def sum67(nums):
  total = 0
  switch = 0
  if len(nums) == 0:
    return 0
  for i in nums:
    if switch == 0:
      if i == 6:
        switch = 1
      else:
        total += i
    else:
      if i == 7:
        switch = 0
      else:
        continue
  return total


