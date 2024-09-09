# Function Argument with default values
def add_num(a=3, b=7):
    print(a + b)


add_num(4, 5)  # 9
add_num()  # 10
add_num(3)  # 10
add_num(122)  # 129
add_num(b=34)  # 37
add_num(a=23)  # 30
add_num(a=100, b=200)  # 300


# Python Keyword Argument
def display_info(fname, lname):
    print('First Name:', fname)
    print('Last Name:', lname)


display_info(fname="Chitta", lname="Swain")
display_info("Kangaroo", "Court")


# display_info("Court") # TypeError: display_info() missing 1 required positional argument: 'lname'
# First Name: Chitta
# Last Name: Swain
# First Name: Kangaroo
# Last Name: Court

# Python Function with Arbitrary Arguments
def find_sum(*nums):
    result = 0
    for i in nums:
        result = result + i
    return result


total = find_sum(2, 34, 56, 5, 6, 7, 8)
print(total) # 118


