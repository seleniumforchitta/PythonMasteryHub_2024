# define python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18."
    pass


num = 18

try:
    input_num = int(input("Enter a number : "))
    if input_num < num:
        raise InvalidAgeException
    else:
        print("Eligible to vote.")

except InvalidAgeException:
    print("Exception Occurred: Invalid Age")



