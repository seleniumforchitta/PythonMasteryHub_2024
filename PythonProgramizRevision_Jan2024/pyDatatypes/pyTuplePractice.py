numbers = (1, -2, 3, 4, 56)
print(numbers)  # (1, -2, 3, 4, 56)

# Create a Tuple Using tuple() Constructor
num_tup = tuple((3, 45, 0, 56, 45, -3))
print(num_tup)  # (3, 45, 0, 56, 45, -3)

# Empty Tuple
tup = ()
print(tup)  # ()

# tuple including string and integer
mixed_tuple = (2, 'Hello', 'Python')
print(mixed_tuple)  # (2, 'Hello', 'Python')

# access the first item
print(num_tup[0])  # 3

# Tuple can't be modified
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# cars[0] = 'Tata'
print(cars)  # TypeError: 'tuple' object does not support item assignment
print("length of brands - ", len(cars))  # length of brands -  4

# Iterate Through a Tuple
for car in cars:
    print(car)

# deleting the tuple
del mixed_tuple

# Create a Python Tuple With One Item
car = ('Tata')
print(type(car))  # <class 'str'>
# But this would not create a tuple; instead, it would be considered a string.
# To solve this, we need to include a trailing comma after the item. For example,
car = ('Tata',)
print(type(car))  # <class 'tuple'>

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# counts the number of i's in the tuple
count = vowels.count('i')
print(count)  # Output: 2

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')
# index of 'e' in vowels
index = alphabets.index('e')
print(index)  # Output: 1
# Syntax - tuple.index(element, start_index, end_index)
# scans 'i' from index 4 to 7 and returns its index
index = alphabets.index('i', 4, 7)
print(index)  # 6
