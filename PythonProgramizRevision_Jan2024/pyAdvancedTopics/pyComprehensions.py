import math

# num = []
# for i in range(1,6):
#     num.append(2**i)
# List Comprehension
# Find out the first 5 powers of 2
num = [2 ** i for i in range(1, 6)]
print(num)  # [2, 4, 8, 16, 32]

# Find out the square root of a list of numbers
numbers = [49, 64, 81, 100, 121]
newList = [int(math.sqrt(i)) for i in numbers]
newListEven = [int(math.sqrt(i)) for i in numbers if i % 2 == 0]
print(newList)  # [7, 8, 9, 10, 11]
print(newListEven)  # [8, 10]

# Merge values of 2 lists and make it a list of tuples
team1 = ["Jessy", "Aryan", "Rabec"]
team2 = ["Haria", "Bhagia", "Dama"]
mergedTeam = [(x, y) for x in team1 for y in team2]
print(mergedTeam)  # [('Jessy', 'Haria'), ('Jessy', 'Bhagia'), ('Jessy', 'Dama'), ('Aryan', 'Haria'),
# ('Aryan', 'Bhagia'),('Aryan', 'Dama'),('Rabec', 'Haria'), ('Rabec', 'Bhagia'), ('Rabec', 'Dama')]

# Set Comprehension
# Find out all the unique characters in string
str = "Programming"
uniChars = {x for x in str}
print(uniChars)  # {'a', 'r', 'P', 'o', 'g', 'm', 'n', 'i'}

# Dictionary Comprehension
num = [1, 2, 3, 4, 5]
squareDict = {i: i ** 2 for i in num}
print(squareDict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

