import math


def greet(name):
    print("Hello " + name)


greet("Pravash")


def add_numbers(a, b):
    return a + b


sum_num = add_numbers(4, 7.9786)
print(sum_num)


# Pass Statement  - it serves as a placeholder for future code, preventing errors from empty code block.
def future_func():
    pass


future_func()

# Library Functions
print("I am a library function")
square_root = math.sqrt(1664)
print(square_root)  # 40.792156108742276


# Default Argument
def greet(name, message="Hello"):
    print(message, name)


# calling function with both arguments
greet("Alice", "Good Morning")  # Good Morning Alice

# calling function with only one argument
greet("Bob")  # Hello Bob


# Using *args and **kwargs# in Functions
# function to sum any number of arguments
def add_all(*nums):
    return sum(nums)


print(add_all(2, 3, 4, 5))


# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")


# pass any number of keyword arguments
greet(name="John", greeting="Hello")  # name: John - greeting: Hello
