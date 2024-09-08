str = "Automation"

# indexing, negative indexing, slicing & reversing
print(str)  # Automation
print(str[0])  # A
print(str[-1])  # n
print(str[1:4])  # uto
print(str[-1::-1])  # noitamotuA - Reverse a string

# String comparison
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"
print(str1 == str2)  # False
print(str1 == str3)  # True

# Join Two or More Strings
str4 = str1 + str2 + str3
print(str4)  # Hello, world!I love Swift.Hello, world!

# Iterate Through a Python String
for i in str1:
    print(i)

# Python String Length
print(len(str4)) # 39

# String Membership Test
print('lo' in str1) # True
print('ee' in str2) # False