# set for student IDS
stud_id = {101, 115, 117, 149, 151}
print("Student IDs : ", stud_id)

vowels = {'a', 'e', 'i', 'o', 'u'}
print("vowels : ", vowels)

mixedData = {"num", 23, -34, 45.50}
print("mixedData : ", mixedData)

# Duplicate items in a set
num = {3, 2, 2, 4, 5, 6, 8, 9, 2, 3, 5, 4}
print("num : ", num)  # num :  {2, 3, 4, 5, 6, 8, 9}

# Add item to a set
num.add(45)
print(num)  # {2, 3, 4, 5, 6, 8, 9, 45}

# update() method is used to update the set with items other collection types (lists, tuples, sets, etc).
num1 = {2, 2, 3, 4, 5, 5}
num2 = [2, 6, 7]
num1.update(num2)
print(num1)  # {2, 3, 4, 5, 6, 7}

# Another Example
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)  # Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# Remove an element from a set
num1 = {2, 2, 3, 4, 5, 5}
num1.discard(2)
print(num1)  # {3, 4, 5}
num1.remove(3)
print(num1)  # {4, 5}

my_set = {1, 2, 3}
my_set.discard(2)  # Removes 2 from the set
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # Element 4 is not in the set; nothing happens
print(my_set)  # Output: {1, 3}

my_set = {1, 2, 3}
my_set.remove(2)  # Removes 2 from the set
print(my_set)  # Output: {1, 3}
# my_set.remove(4)  # Element 4 is not in the set; raises KeyError
# Output: KeyError: 4

# iterate over a set
for company in companies:
    print(company)

print(len(companies))  # 4

