"""
Author - Chittaranjan Swain
This file contains below basic concepts required to start with Python.
1. Python Datatypes
2. Type Conversions
3. Python I/O & imports
4. Operators
5. Python Namespace
"""

a = 5  # Numeric, no need to declare int a = 5, Python interpreter automatically detects the type.
name = "PythonPractice"
b = None  # None is a special literal

# Taking input
name = input("Tell me you name: ")
age = int(input("Tell me you age: "))
print(name, type(name), age, type(age))
print(name, " is ", age, " years old!")

# Conversion between data types - We convert between different datatypes using type conversion function like int(), float(), str() etc.
print(float(5))
print(int(4.5))
print(float('5.6'))
print(str(25))
# print(int('1p')) #error

print(set([1, 2, 2, 3]))  # {1,2,3}
print(tuple([1, 2, 2, 3]))  # (1,2,2,3)
print(list('hello'))  # ['h', 'e', 'l', 'l', 'o']
print(dict([[1, 22], [2, 32]]))  # {1: 22, 2: 32}
print(tuple({5, 6, 6, 7}))  # (5, 6, 7)

# imports
import math

print(math.pi)  # 3.141592653589793
import sys

print(sys.path[0])  # C:\Users\chitt\PycharmProjects\PythonMasteryHub_2024\PythonProgramizRevision_Jan2024

# Python Namespace
a = 2
print(id(a))  # 1876981580048
print(id(2))  # 1876981580048
a = a + 1
print(id(a))  # 1831273038128
b = 2
print(id(b))  # 1876981580048
