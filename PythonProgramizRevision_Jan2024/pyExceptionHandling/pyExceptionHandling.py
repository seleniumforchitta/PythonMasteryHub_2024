# Python Built-in Exceptions
print(dir(locals()['__builtins__']))

# Try with Except Block
try:
    a = int(input("Enter numerator - "))
    b = int(input("Enter Denominator - "))
    result = a / b
    print("Result - ", result)
except:
    print("Error : Denominator can't be zero.")

# Try with Multiple Except Block
# For each try block we can have one or more except blocks. Multiple except blocks help us to handle exception
# differently.
try:
    a = int(input("Enter numerator - "))
    b = int(input("Enter Denominator - "))
    result = a / b
    print("Result - ", result)

    list1 = [1, 2, 3, 4, 5]
    print(list1[5])

except ZeroDivisionError:
    print("Error : Denominator can't be zero.")  # When this will occur then following except block will be skipped.
except IndexError:
    print("Error : Index out of Bound.")

# Try with else clause - if you want to run a certain block of code if the try block runs without errors.
try:
    num = int(input("Enter a number - "))
    assert num % 2 == 0
except:
    print("It is not a even number")
else:
    print("The reciprocal of the number is - ", 1 / num)

# Try with Finally - Finally block is always executed no matter there is an exception or not
try:
    a = int(input("Enter numerator - "))
    b = int(input("Enter Denominator - "))
    result = a / b
    print("Result - ", result)
except:
    print("Error : Denominator can't be zero.")
finally:
    print("Finally : Executed no matter what.")
