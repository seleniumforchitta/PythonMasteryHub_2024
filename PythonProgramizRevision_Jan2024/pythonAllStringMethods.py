# Python String capitalize()
# This converts the first character of a string to an uppercase letter & all other alphabets to lowercase.
str = "I Am A Good Boy !"
print(str.capitalize())  # I am a good boy !
# capitalize() doesn't change the original string

# Python String center()
# The center() method returns a new centered string after padding it with the specified character.
sentence = "Python is awesome"
new_string = sentence.center(50, '*')
print(new_string)  # Output: ****************Python is awesome*****************

# Python String casefold()
# converts all characters of the string into lowercase letters and returns a new string.
text = "pYtHon"
print(text.casefold())  # python

print(sentence.count(' '))  # 2

# Python String endswith()
message = 'Python is fun'
print(message.endswith('fun'))  # Output: True

# expandtabs() With or without Argument
str = "xyz\t12345\tabc"
print('Original String:', str)
# tabsize is # default tabsize is 8
print('Tabsize 2:', str.expandtabs())
# tabsize is set to 10
print('Tabsize 6:', str.expandtabs(10))

# Python String encode()
title = 'Python Programming'
print(title.encode())  # b'Python Programming'
print(title.encode(encoding='UTF-8', errors='strict'))  # b'Python Programming'
newTitle = title.encode()
print(newTitle)
# ignore error
print('The encoded version (with ignore) is:', title.encode("ascii", "ignore"))
# replace error
print('The encoded version (with replace) is:', title.encode("ascii", "replace"))

# Python String find()
message = 'Python is a fun programming fun language fun'
print(message.find('fun'))  # 12
print(message.find('fun', 29))  # 41
print(message.find('fun', 13, 39))  # 28
text = "Hello world, welcome to the world of Python"
# Using find() to search for the first occurrence of 'world'
first_occurrence = text.find('world')
print(f"First occurrence of 'world': {first_occurrence}")  # First occurrence of 'world': 6
# Using rfind() to search for the last occurrence of 'world'
last_occurrence = text.rfind('world')
print(f"Last occurrence of 'world': {last_occurrence}")  # Last occurrence of 'world': 28

# Python String format()
# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))
# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))
# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))
# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

# Python String index()
text = 'Python is fun'
result = text.index('is')
print(result)  # 7
# find(): Returns -1 if the substring is not found.
# index(): Raises a ValueError if the substring is not found.

# Python String join()
# Returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))
# Output: Python is a fun programming language
# .join() with sets
test = {'2', '1', '3'}
s = ', '
print(s.join(test))  # 1, 2, 3
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))  # Python->->Ruby->->Java
# .join() with dictionaries
test = {'mat': 1, 'that': 2}
s = '->'
# joins the keys only
print(s.join(test))  # mat -> that
test = {1: 'mat', 2: 'that'}
s = ', '
# this gives error since key isn't string
# print(s.join(test))

# Python String replace()
# syntax - str.replace(old, new [, count])
text = 'bat ball'
# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)  # rot roll
song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))  # Let it be, don't let it be, don't let it be, let it be

# Python String split()
text = 'Python is fun'
# split the text from space
print(text.split())  # ['Python', 'is', 'fun']
# We can use the maxsplit parameter to limit the number of splits that can be performed on a string.
grocery = 'Milk#Chicken#Bread#Butter'
# maxsplit: 1
print(grocery.split('#', 1))  # ['Milk', 'Chicken#Bread#Butter']
# splitlines() with Multi Line String
grocery = '''Milk
Chicken
Bread
Butter'''
# returns a list after splitting the grocery string
print(grocery.splitlines())  # ['Milk', 'Chicken', 'Bread', 'Butter']

# Python String title()
text = 'My favorite number is 25.'
print(text.title())  # My Favorite Number Is 25.
